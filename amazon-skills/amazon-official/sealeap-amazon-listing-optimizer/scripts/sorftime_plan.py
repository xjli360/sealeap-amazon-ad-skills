#!/usr/bin/env python3
"""Plan or execute a quota-aware Sorftime evidence pull through ecomi.

No API key is accepted. ecomi reads the existing user-level configuration.
Without --execute this script performs no network call and writes no evidence.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SITE_ALIASES = {"UK": "GB"}
DEFAULT_ECOMI = Path.home() / "Documents" / "Code" / "ecomi" / ".venv" / "bin" / "ecomi"
ASIN_PATTERN = re.compile(r"^[A-Z0-9]{10}$")


def normalize_site(value: str) -> str:
    site = value.strip().upper()
    site = SITE_ALIASES.get(site, site)
    if not re.fullmatch(r"[A-Z]{2}", site):
        raise ValueError("site must be a two-letter marketplace code such as US, GB, JP, or DE")
    return site


def normalize_asin(value: str) -> str:
    asin = value.strip().upper()
    if not ASIN_PATTERN.fullmatch(asin):
        raise ValueError("ASIN must contain exactly 10 letters or digits")
    return asin


def build_plan(asin: str, site: str, keywords: list[str], deep: bool) -> list[dict[str, Any]]:
    plan: list[dict[str, Any]] = [
        {"tool": "product_detail", "asin": asin, "site": site, "purpose": "third-party product snapshot"},
        {"tool": "product_traffic_terms", "asin": asin, "site": site, "purpose": "observed query exposure"},
        {"tool": "product_reviews", "asin": asin, "site": site, "purpose": "sampled customer language and objections"},
    ]
    if deep:
        plan.extend([
            {"tool": "product_report", "asin": asin, "site": site, "purpose": "broader product and competition estimate"},
            {"tool": "product_variations", "asin": asin, "site": site, "purpose": "observed variation structure"},
        ])
    for keyword in keywords:
        plan.append({"tool": "keyword_detail", "keyword": keyword, "site": site, "purpose": "estimated demand and competition"})
        if deep:
            plan.extend([
                {"tool": "keyword_search_results", "keyword": keyword, "site": site, "purpose": "page-one intent observation", "page": 1},
                {"tool": "keyword_extends", "keyword": keyword, "site": site, "purpose": "long-tail discovery", "page": 1},
                {"tool": "keyword_trend", "keyword": keyword, "site": site, "purpose": "seasonality and CPC trend estimate"},
            ])
    return plan


def locate_ecomi() -> str:
    override = os.environ.get("ECOMI_BIN")
    if override:
        path = Path(override).expanduser()
        if path.is_file() and os.access(path, os.X_OK):
            return str(path)
        raise FileNotFoundError("ECOMI_BIN does not point to an executable file")
    found = shutil.which("ecomi")
    if found:
        return found
    if DEFAULT_ECOMI.is_file() and os.access(DEFAULT_ECOMI, os.X_OK):
        return str(DEFAULT_ECOMI)
    raise FileNotFoundError("ecomi CLI not found; set ECOMI_BIN or install ecomi")


def check_config() -> None:
    path = Path.home() / ".ecomi" / "sorftime.json"
    if not path.is_file():
        raise FileNotFoundError("Sorftime config missing: create ~/.ecomi/sorftime.json outside this Skill")
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode & 0o077:
        raise PermissionError("Sorftime config is accessible by group/others; run chmod 600 ~/.ecomi/sorftime.json")


def command_for(ecomi: str, item: dict[str, Any]) -> list[str]:
    command = [ecomi, "sorftime", "--tool", item["tool"], "--site", item["site"]]
    if item.get("asin"):
        command.extend(["--asin", item["asin"]])
    if item.get("keyword"):
        command.extend(["--keyword", item["keyword"]])
    if item.get("page") is not None:
        command.extend(["--page", str(item["page"])])
    return command


def safe_name(index: int, item: dict[str, Any]) -> str:
    subject = item.get("asin") or item.get("keyword") or "query"
    subject = "".join(char if char.isalnum() or char in "-_" else "_" for char in str(subject))[:60]
    return f"{index:02d}_{item['tool']}_{subject}.json"


def redact_stderr(value: str) -> str:
    return re.sub(
        r"(?i)(api[_ -]?key|access[_ -]?token|token|secret)(\s*[:=]\s*)(\S+)",
        r"\1\2[REDACTED]",
        value,
    )


def execute(plan: list[dict[str, Any]], output_dir: Path) -> dict[str, Any]:
    check_config()
    ecomi = locate_ecomi()
    output_dir.mkdir(parents=True, exist_ok=True)
    runs: list[dict[str, Any]] = []
    for index, item in enumerate(plan, start=1):
        started = datetime.now(timezone.utc).isoformat()
        completed = subprocess.run(command_for(ecomi, item), text=True, capture_output=True, check=False)
        finished = datetime.now(timezone.utc).isoformat()
        raw = completed.stdout.strip()
        try:
            payload: Any = json.loads(raw)
        except json.JSONDecodeError:
            payload = {"raw_text": raw}
        record: dict[str, Any] = {
            "source": "Sorftime via ecomi",
            "evidence_grade": "D",
            "fetched_at": started,
            "finished_at": finished,
            "request": item,
            "returncode": completed.returncode,
            "payload": payload,
            "limitations": "Third-party estimate or observation; not Seller Central actual data.",
        }
        if completed.stderr.strip():
            record["stderr"] = redact_stderr(completed.stderr.strip())
        file_path = output_dir / safe_name(index, item)
        file_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
        runs.append({"file": file_path.name, "tool": item["tool"], "returncode": completed.returncode})
        if completed.returncode != 0:
            break
    manifest = {
        "source": "Sorftime via ecomi",
        "evidence_grade": "D",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "planned_calls": len(plan),
        "completed_calls": len(runs),
        "runs": runs,
        "limitations": "Third-party estimates/observations; do not treat as Amazon first-party or store actuals.",
    }
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asin", required=True)
    parser.add_argument("--site", required=True, help="Amazon marketplace code; UK is normalized to GB")
    parser.add_argument("--keyword", action="append", default=[], help="Repeat for each core query")
    parser.add_argument("--deep", action="store_true", help="Add product report, variations, and three extra calls per query")
    parser.add_argument("--max-calls", type=int, default=8, help="Hard call-budget guard")
    parser.add_argument("--execute", action="store_true", help="Actually call Sorftime; omitted means plan only")
    parser.add_argument("--output-dir", type=Path, default=Path("evidence/sorftime"))
    args = parser.parse_args()

    if args.max_calls < 1:
        parser.error("--max-calls must be at least 1")
    try:
        asin = normalize_asin(args.asin)
        site = normalize_site(args.site)
    except ValueError as exc:
        parser.error(str(exc))
    keywords = list(dict.fromkeys(value.strip() for value in args.keyword if value.strip()))
    plan = build_plan(asin, site, keywords, args.deep)
    output: dict[str, Any] = {
        "mode": "execute" if args.execute else "plan",
        "evidence_grade": "D",
        "estimated_calls": len(plan),
        "max_calls": args.max_calls,
        "calls": plan,
        "limitations": "Third-party estimates/observations; not Amazon first-party or store actuals.",
    }
    if len(plan) > args.max_calls:
        output["blocked"] = f"Plan requires {len(plan)} calls, above --max-calls {args.max_calls}. Reduce scope or raise the limit explicitly."
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 2
    if not args.execute:
        output["next_step"] = "Review scope and quota, then rerun with --execute. No network call was made and no evidence files were written."
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    try:
        manifest = execute(plan, args.output_dir)
    except (FileNotFoundError, PermissionError, OSError) as exc:
        print(json.dumps({"error": str(exc), "mode": "execute"}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if all(item["returncode"] == 0 for item in manifest["runs"]) else 1


if __name__ == "__main__":
    sys.exit(main())
