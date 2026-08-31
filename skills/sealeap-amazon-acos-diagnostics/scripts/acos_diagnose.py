#!/usr/bin/env python3
"""Recalculate core Amazon Ads metrics and surface scope/data-quality warnings."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


REQUIRED = ("impressions", "clicks", "spend", "orders", "ad_sales")


def number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric")
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return result


def ratio(numerator: float, denominator: float, scale: float = 1.0) -> float | None:
    return None if denominator == 0 else numerator / denominator * scale


def rounded(value: float | None, digits: int = 4) -> float | None:
    return None if value is None else round(value, digits)


def relative_mismatch(actual: float, expected: float) -> float:
    denominator = max(abs(actual), abs(expected), 1e-9)
    return abs(actual - expected) / denominator


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="UTF-8 JSON input")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    raw_metrics = payload.get("metrics")
    if not isinstance(raw_metrics, dict):
        raise ValueError("input must contain a metrics object")
    missing = [name for name in REQUIRED if name not in raw_metrics]
    if missing:
        raise ValueError("missing metrics: " + ", ".join(missing))

    metrics = {name: number(raw_metrics[name], f"metrics.{name}") for name in REQUIRED}
    if "total_sales" in raw_metrics:
        metrics["total_sales"] = number(raw_metrics["total_sales"], "metrics.total_sales")

    impressions = metrics["impressions"]
    clicks = metrics["clicks"]
    spend = metrics["spend"]
    orders = metrics["orders"]
    ad_sales = metrics["ad_sales"]

    derived: dict[str, float | None] = {
        "ctr_pct": ratio(clicks, impressions, 100),
        "cpc": ratio(spend, clicks),
        "cpm": ratio(spend, impressions, 1000),
        "cvr_pct": ratio(orders, clicks, 100),
        "aov": ratio(ad_sales, orders),
        "cpa": ratio(spend, orders),
        "acos_pct": ratio(spend, ad_sales, 100),
        "roas": ratio(ad_sales, spend),
        "tacos_pct": ratio(spend, metrics["total_sales"], 100) if "total_sales" in metrics else None,
    }

    errors: list[str] = []
    warnings: list[str] = []
    if clicks > impressions:
        errors.append("clicks exceed impressions")
    if orders > clicks:
        warnings.append("orders exceed clicks; verify whether the order field and click scope are comparable")
    if ad_sales > 0 and orders == 0:
        warnings.append("ad sales are positive while orders are zero; verify attribution fields")
    if spend > 0 and clicks == 0:
        warnings.append("spend is positive while clicks are zero; verify ad type and metric scope")
    if ad_sales == 0:
        warnings.append("ACOS is undefined because ad_sales is zero")

    decomposition_acos: float | None = None
    if derived["cpc"] is not None and derived["cvr_pct"] and derived["aov"]:
        decomposition_acos = derived["cpc"] / ((derived["cvr_pct"] / 100) * derived["aov"]) * 100
        if derived["acos_pct"] is not None and relative_mismatch(decomposition_acos, derived["acos_pct"]) > 0.001:
            errors.append("ACOS decomposition does not reconcile")

    comparisons: dict[str, dict[str, Any]] = {}
    reported = payload.get("reported", {})
    if reported is not None and not isinstance(reported, dict):
        raise ValueError("reported must be an object")
    for key in ("ctr_pct", "cpc", "cvr_pct", "aov", "cpa", "acos_pct", "roas", "tacos_pct"):
        if key in reported:
            reported_value = number(reported[key], f"reported.{key}")
            calculated = derived.get(key)
            mismatch = None if calculated is None else relative_mismatch(reported_value, calculated)
            comparisons[key] = {
                "reported": reported_value,
                "calculated": rounded(calculated),
                "relative_mismatch_pct": None if mismatch is None else round(mismatch * 100, 2),
            }
            if mismatch is not None and mismatch > 0.01:
                warnings.append(f"reported {key} differs from recalculation by more than 1%")

    benchmark_findings: list[str] = []
    benchmark = payload.get("benchmark", {})
    if benchmark is not None and not isinstance(benchmark, dict):
        raise ValueError("benchmark must be an object")
    for key in ("ctr_pct", "cpc", "cvr_pct"):
        if key in benchmark:
            benchmark_value = number(benchmark[key], f"benchmark.{key}")
            calculated = derived[key]
            if calculated is not None:
                direction = "above" if calculated > benchmark_value else "below" if calculated < benchmark_value else "equal"
                benchmark_findings.append(f"{key} is {direction} the supplied benchmark")

    economics = payload.get("economics", {})
    if economics is not None and not isinstance(economics, dict):
        raise ValueError("economics must be an object")
    break_even = None
    profitability = "NEEDS_DATA"
    if "break_even_acos_pct" in economics:
        break_even = number(economics["break_even_acos_pct"], "economics.break_even_acos_pct")
        if break_even > 100:
            warnings.append("break_even_acos_pct exceeds 100%; verify percentage units and cost scope")
        if derived["acos_pct"] is None:
            profitability = "UNDEFINED_ACOS"
        elif derived["acos_pct"] < break_even:
            profitability = "BELOW_BREAK_EVEN_ACOS"
        elif math.isclose(derived["acos_pct"], break_even, abs_tol=0.01):
            profitability = "AT_BREAK_EVEN_ACOS"
        else:
            profitability = "ABOVE_BREAK_EVEN_ACOS"

    output = {
        "status": "HOLD" if errors else "DRAFT",
        "scope": payload.get("scope", {}),
        "raw_metrics": metrics,
        "derived": {key: rounded(value) for key, value in derived.items()},
        "decomposition_acos_pct": rounded(decomposition_acos),
        "reported_comparison": comparisons,
        "benchmark_findings": benchmark_findings,
        "break_even_acos_pct": break_even,
        "profitability_signal": profitability,
        "errors": errors,
        "warnings": warnings,
        "guardrail": "Read-only calculation; benchmark and profitability signals require current scope, attribution, costs, and human review.",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
