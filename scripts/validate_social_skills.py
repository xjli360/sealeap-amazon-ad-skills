#!/usr/bin/env python3
"""Validate the independently installable Douyin and Weixin Skill collections.

Run from any directory:
  uv run --no-project --with pyyaml python -B scripts/validate_social_skills.py --doctor

This checks package structure and local behavior, not provider availability or
the truth of business claims. It never calls an external MCP service.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required; run with: uv run --no-project --with pyyaml python -B")


SCOPES = ("douyin", "weixin")
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
CODE_REFERENCE = re.compile(r"`((?:references|scripts|assets|agents)/[^`\s]+\.(?:md|py|ya?ml|json|txt|sh))`")


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject silent YAML key replacement in package metadata."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(value):
    result = yaml.load(value, Loader=UniqueKeyLoader)
    if not isinstance(result, dict):
        raise ValueError("expected a YAML mapping")
    return result


def local_references(document: Path, skill: Path):
    text = document.read_text(encoding="utf-8")
    for raw in set(MARKDOWN_LINK.findall(text) + CODE_REFERENCE.findall(text)):
        raw = raw.strip("<>")
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        relative = Path(unquote(parsed.path))
        if any(char in str(relative) for char in "*{}$"):
            continue
        target = (document.parent / relative).resolve()
        # Reference documents also name the package-root script in inline code.
        if not target.exists() and relative.parts[0] in {"references", "scripts", "assets", "agents"}:
            target = (skill / relative).resolve()
        yield raw, target


def workflow_numbers(text):
    match = re.search(r"^## 工作流\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        return []
    return [int(number) for number in re.findall(r"^(?:###\s+)?(\d+)\.\s", match.group(1), re.M)]


def validate(root: Path, run_doctor: bool):
    counts = Counter()
    groups = Counter()
    errors = []
    names = {}
    helper_hashes = defaultdict(list)

    def fail(path, message):
        try:
            label = str(path.relative_to(root))
        except ValueError:
            label = str(path)
        errors.append({"path": label, "error": message})

    for scope in SCOPES:
        directory = root / "amazon-skills" / scope
        skills = sorted(directory.rglob("SKILL.md"))
        if not skills:
            fail(directory, "no SKILL.md files found")
        for entry in skills:
            skill = entry.parent.resolve()
            counts["skills"] += 1
            groups[f"{scope}/{entry.relative_to(directory).parts[0]}"] += 1
            text = entry.read_text(encoding="utf-8")
            front = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.S)
            try:
                if not front:
                    raise ValueError("missing YAML frontmatter")
                metadata = load_yaml(front.group(1))
                unknown = set(metadata) - ALLOWED_FRONTMATTER
                if unknown:
                    fail(entry, f"unsupported frontmatter keys: {sorted(unknown)}")
                name = metadata.get("name")
                description = metadata.get("description")
                if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                    fail(entry, "name must be at most 64 characters in lowercase kebab case")
                elif name != skill.name:
                    fail(entry, "name does not match the installation directory")
                elif name in names:
                    fail(entry, f"duplicate Skill name, also in {names[name]}")
                else:
                    names[name] = str(entry.relative_to(root))
                if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                    fail(entry, "description must contain 1–1024 characters")
                elif "<" in description or ">" in description:
                    fail(entry, "description contains angle brackets")
            except (yaml.YAMLError, ValueError, TypeError) as exc:
                fail(entry, f"invalid frontmatter: {exc}")
                continue

            ui_path = skill / "agents/openai.yaml"
            try:
                ui = load_yaml(ui_path.read_text(encoding="utf-8"))["interface"]
                short = ui.get("short_description")
                if not isinstance(short, str) or not 25 <= len(short) <= 64:
                    fail(ui_path, "short_description must contain 25–64 characters")
                prompt = ui.get("default_prompt")
                if not isinstance(prompt, str) or f"${name}" not in prompt:
                    fail(ui_path, "default_prompt must invoke this $skill-name")
                if not isinstance(ui.get("display_name"), str) or not ui["display_name"].strip():
                    fail(ui_path, "display_name is missing")
                counts["ui_metadata"] += 1
            except (OSError, yaml.YAMLError, ValueError, TypeError, KeyError, AttributeError) as exc:
                fail(ui_path, f"invalid UI metadata: {exc}")

            documents = [entry, *sorted((skill / "references").glob("*.md"))]
            graph = defaultdict(set)
            for document in documents:
                if not document.is_file():
                    continue
                for raw, target in local_references(document, skill):
                    counts["local_references"] += 1
                    if not target.is_relative_to(skill):
                        fail(document, f"reference leaves standalone Skill package: {raw}")
                    elif not target.is_file():
                        fail(document, f"missing referenced file: {raw}")
                    else:
                        graph[document.resolve()].add(target)

            reachable = set()
            pending = [entry.resolve()]
            while pending:
                document = pending.pop()
                if document in reachable:
                    continue
                reachable.add(document)
                pending.extend(graph[document] - reachable)
            for reference in (skill / "references").glob("*.md"):
                if reference.resolve() not in reachable:
                    fail(reference, "reference cannot be reached from SKILL.md")

            lines = Counter(line for line in text.splitlines() if "references/playbook.md" in line)
            if any(number > 1 for number in lines.values()):
                fail(entry, "duplicate execution-manual entry")
            playbook = skill / "references/playbook.md"
            if playbook.is_file():
                rows = [int(number) for number in re.findall(r"^\|\s*(\d+)\s*\|", playbook.read_text(encoding="utf-8"), re.M)]
                steps = workflow_numbers(text)
                if rows and steps:
                    counts["workflow_tables"] += 1
                    if rows != steps:
                        fail(playbook, f"workflow table steps {rows} differ from SKILL.md steps {steps}")

            for script in sorted((skill / "scripts").glob("*.py")):
                counts["python_scripts"] += 1
                try:
                    compile(script.read_bytes(), str(script), "exec")
                except (SyntaxError, ValueError) as exc:
                    fail(script, f"Python compilation failed: {exc}")
            helper = skill / "scripts/mcp_research.py"
            if helper.is_file():
                helper_hashes[hashlib.sha256(helper.read_bytes()).hexdigest()].append(helper)
                if run_doctor:
                    environment = os.environ.copy()
                    for variable in ("SIF_MCP_SECRET_KEY", "SELLERSPRITE_MCP_SECRET_KEY", "APIFY_TOKEN"):
                        environment[variable] = ""
                    # Deny even accidental network access during every doctor's run.
                    wrapper = (
                        "import runpy,socket,sys; "
                        "socket.socket.connect=lambda *a,**k: (_ for _ in ()).throw(RuntimeError('network forbidden')); "
                        "sys.argv=[sys.argv[1],'--provider','sellersprite','doctor']; "
                        "runpy.run_path(sys.argv[0],run_name='__main__')"
                    )
                    try:
                        result = subprocess.run([sys.executable, "-B", "-c", wrapper, str(helper)],
                                                cwd=skill, env=environment, capture_output=True, text=True, timeout=10)
                        doctor = json.loads(result.stdout)
                        if result.returncode or doctor.get("network_called") is not False or doctor.get("credential_configured") is not False:
                            raise ValueError("doctor must succeed offline without configured credentials")
                        counts["offline_doctors"] += 1
                    except (subprocess.SubprocessError, ValueError, OSError) as exc:
                        fail(helper, f"offline doctor failed: {exc}")

    if len(helper_hashes) > 1:
        fail(root / "amazon-skills", f"MCP helper drift: {len(helper_hashes)} different implementations")
    return {
        "ok": not errors,
        "scope": [f"amazon-skills/{scope}" for scope in SCOPES],
        "counts": dict(counts),
        "collections": dict(sorted(groups.items())),
        "mcp_helper_hashes": {digest: len(paths) for digest, paths in helper_hashes.items()},
        "network_called": False,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Repository root")
    parser.add_argument("--doctor", action="store_true", help="Run every helper's doctor with credentials removed and network blocked")
    parser.add_argument("--output", type=Path, help="Also save the JSON validation report")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.doctor)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
