#!/usr/bin/env python3
"""Check SeaLeap Skill names, installation directories, invocation prompts and indexes.

Run: uv run --no-project --with pyyaml python -B scripts/validate_skill_names.py
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


CASE_PATH = "evals/cases/sealeap-skill-names.json"
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def validate(root: Path):
    case = json.loads((root / CASE_PATH).read_text(encoding="utf-8"))
    errors = []
    counts = Counter()
    names = {}
    documents = {root / path for path in case["reference_documents"]}

    def fail(path, message):
        errors.append({"path": str(path.relative_to(root)), "error": message})

    for scope in case["scopes"]:
        directory = root / scope
        entries = sorted(directory.rglob("SKILL.md"))
        counts[scope] = len(entries)
        if not entries:
            fail(directory, "no Skills found")
        documents.update(directory.rglob("README.md"))
        for entry in entries:
            try:
                text = entry.read_text(encoding="utf-8")
                front = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", text, re.S)
                if not front:
                    raise ValueError("missing YAML frontmatter")
                metadata = yaml.safe_load(front.group(1))
                name = metadata.get("name")
                if not isinstance(name, str) or not re.fullmatch(case["name_pattern"], name):
                    fail(entry, "name must start with sealeap- and use lowercase hyphen format")
                if not isinstance(name, str):
                    continue
                if len(name) > case["max_name_length"]:
                    fail(entry, f"name exceeds {case['max_name_length']} characters")
                if entry.parent.name != name:
                    fail(entry, "installation directory differs from Skill name")
                if name in names:
                    fail(entry, f"duplicate name, also in {names[name]}")
                names[name] = str(entry.relative_to(root))
                ui_path = entry.parent / "agents/openai.yaml"
                ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
                prompt = ui["interface"]["default_prompt"]
                invocations = re.findall(r"\$([a-z0-9]+(?:-[a-z0-9]+)*)", prompt)
                if name not in invocations:
                    fail(ui_path, "default_prompt does not invoke this Skill's current name")
            except (OSError, yaml.YAMLError, ValueError, TypeError, KeyError, AttributeError) as exc:
                fail(entry, str(exc))

    link_count = 0
    for document in sorted(documents):
        if not document.is_file():
            fail(document, "reference document is missing")
            continue
        for raw in MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
            parsed = urlsplit(raw.strip("<>"))
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            link_count += 1
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                fail(document, f"broken local link: {raw}")

    return {
        "ok": not errors,
        "case": case["id"],
        "skills": sum(counts.values()),
        "scopes": dict(counts),
        "unique_names": len(names),
        "local_links": link_count,
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
