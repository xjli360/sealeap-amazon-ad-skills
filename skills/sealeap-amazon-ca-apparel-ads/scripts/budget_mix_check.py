#!/usr/bin/env python3
"""Print or validate the course budget mix for the two covered CA apparel cases."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


BASELINES: dict[str, dict[str, dict[str, float]]] = {
    "coat": {
        "new": {"sp_manual_keywords": 40, "sb_sbv": 30, "sp_auto": 20, "sp_product_targeting": 10},
        "growth": {"sp_manual_exact": 35, "sb_sbv": 30, "sd": 20, "sp_product_targeting": 15},
        "mature": {"sp_manual": 30, "sb": 25, "sd": 25, "sp_product_targeting": 20},
    },
    "underpants": {
        "new": {
            "sp_manual_keywords": 50,
            "sp_product_targeting": 20,
            "sp_auto": 20,
            "sb_sbv": 5,
            "sd": 5,
        },
        "growth": {
            "sp_manual_keywords": 40,
            "sb_sbv": 30,
            "sp_product_targeting": 15,
            "sd": 10,
            "sp_auto": 5,
        },
        "mature": {"sp_manual_keywords": 35, "sd": 30, "sb_sbv": 25, "sp_product_targeting": 10},
    },
}


def load_allocation(path: Path) -> dict[str, float]:
    payload: Any = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "allocation" in payload:
        payload = payload["allocation"]
    if not isinstance(payload, dict) or not payload:
        raise ValueError("allocation must be a non-empty JSON object or an object containing 'allocation'")
    result: dict[str, float] = {}
    for key, value in payload.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"allocation {key!r} must be numeric")
        value = float(value)
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"allocation {key!r} must be finite and non-negative")
        result[str(key)] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product", required=True, choices=sorted(BASELINES))
    parser.add_argument("--stage", required=True, choices=("new", "growth", "mature"))
    parser.add_argument("--allocation", type=Path, help="Optional JSON plan to validate and compare")
    args = parser.parse_args()

    baseline = BASELINES[args.product][args.stage]
    proposed = load_allocation(args.allocation) if args.allocation else baseline
    total = sum(proposed.values())
    errors: list[str] = []
    warnings: list[str] = []
    if not math.isclose(total, 100.0, abs_tol=0.01):
        errors.append(f"allocation totals {total:.2f}%, expected 100.00%")
    missing = sorted(set(baseline) - set(proposed))
    added = sorted(set(proposed) - set(baseline))
    if missing:
        warnings.append("course channels omitted: " + ", ".join(missing))
    if added:
        warnings.append("channels outside course baseline: " + ", ".join(added))

    comparison = {
        key: {
            "course_baseline_pct": baseline.get(key),
            "proposed_pct": proposed.get(key),
            "delta_pp": None
            if key not in baseline or key not in proposed
            else round(proposed[key] - baseline[key], 2),
        }
        for key in sorted(set(baseline) | set(proposed))
    }
    output = {
        "status": "HOLD" if errors else "DRAFT",
        "product": args.product,
        "stage": args.stage,
        "proposed_total_pct": round(total, 2),
        "comparison": comparison,
        "errors": errors,
        "warnings": warnings,
        "guardrail": "COURSE_BASELINE only; recalculate with current account, profit, inventory, eligibility, and human approval.",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
