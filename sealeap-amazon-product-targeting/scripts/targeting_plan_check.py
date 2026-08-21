#!/usr/bin/env python3
"""Statically validate a draft Amazon Ads product-targeting experiment plan."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any


ASIN_RE = re.compile(r"^[A-Z0-9]{10}$")
TARGET_TYPES = {"asin", "category", "expanded_product"}
VARIABLES = {"target", "negative_target", "bid", "budget", "placement_modifier", "status"}
REQUIRED = {
    "experiment_id",
    "campaign",
    "ad_group",
    "main_variable",
    "target_type",
    "target_value",
    "relationship",
    "evidence_ids",
    "baseline",
    "old_value",
    "new_value",
    "frozen_variables",
    "budget_cap",
    "success_metric",
    "stop_rule",
    "rollback",
    "approval_status",
}


def nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    scope = payload.get("scope")
    if not isinstance(scope, dict) or not scope.get("marketplace") or not scope.get("profile_id"):
        errors.append("scope.marketplace and scope.profile_id are required")
    if not nonempty(payload.get("objective")):
        errors.append("objective is required and must describe one primary use case")

    experiments = payload.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        errors.append("experiments must be a non-empty array")
        experiments = []

    seen_units: set[tuple[str, str]] = set()
    summaries: list[dict[str, Any]] = []
    for index, experiment in enumerate(experiments, start=1):
        prefix = f"experiments[{index - 1}]"
        if not isinstance(experiment, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = sorted(key for key in REQUIRED if key not in experiment)
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
        for key in REQUIRED - {"old_value"}:
            if key in experiment and not nonempty(experiment[key]):
                errors.append(f"{prefix}.{key} must not be empty")

        variable = experiment.get("main_variable")
        if variable not in VARIABLES:
            errors.append(f"{prefix}.main_variable must be one of {sorted(VARIABLES)}")
        target_type = experiment.get("target_type")
        if target_type not in TARGET_TYPES:
            errors.append(f"{prefix}.target_type must be one of {sorted(TARGET_TYPES)}")
        target_value = str(experiment.get("target_value", "")).upper()
        if target_type == "asin" and target_value and not ASIN_RE.fullmatch(target_value):
            errors.append(f"{prefix}.target_value is not a 10-character ASIN-shaped value")

        evidence = experiment.get("evidence_ids")
        if not isinstance(evidence, list) or not all(nonempty(item) for item in evidence):
            errors.append(f"{prefix}.evidence_ids must be a non-empty list")
        frozen = experiment.get("frozen_variables")
        if not isinstance(frozen, list) or not all(nonempty(item) for item in frozen):
            errors.append(f"{prefix}.frozen_variables must be a non-empty list")

        budget_cap = experiment.get("budget_cap")
        if isinstance(budget_cap, bool) or not isinstance(budget_cap, (int, float)):
            errors.append(f"{prefix}.budget_cap must be numeric")
        elif not math.isfinite(float(budget_cap)) or float(budget_cap) <= 0:
            errors.append(f"{prefix}.budget_cap must be finite and greater than zero")

        campaign = str(experiment.get("campaign", ""))
        ad_group = str(experiment.get("ad_group", ""))
        unit = (campaign, ad_group)
        if campaign and ad_group:
            if unit in seen_units:
                errors.append(f"{prefix} reuses campaign/ad_group; use a unique experiment unit")
            seen_units.add(unit)

        if experiment.get("approval_status") != "DRAFT":
            warnings.append(f"{prefix}.approval_status should remain DRAFT until explicit human approval")
        summaries.append(
            {
                "experiment_id": experiment.get("experiment_id"),
                "unit": f"{campaign}/{ad_group}",
                "main_variable": variable,
                "target": f"{target_type}:{target_value}",
            }
        )

    output = {
        "status": "HOLD" if errors else "DRAFT",
        "objective": payload.get("objective"),
        "experiment_count": len(experiments),
        "experiments": summaries,
        "errors": errors,
        "warnings": warnings,
        "guardrail": "Static validation only; verify live ASIN/category existence, eligibility, economics, store scope, and human approval before writes.",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
