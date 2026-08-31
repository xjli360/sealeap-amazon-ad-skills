#!/usr/bin/env python3
"""Filter the bundled 2025 Prime Day insight records without dropping qualifiers."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Iterable


DATA_PATH = Path(__file__).resolve().parents[1] / "references" / "prime-day-insights-2025.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"Family Brief", "Content", "Metrics", "Ad Products", "Marketplaces"}
    if not rows or set(rows[0]) != required:
        raise SystemExit(f"Unexpected CSV schema: {set(rows[0]) if rows else 'empty'}")
    return rows


def marketplace_tokens(value: str) -> set[str]:
    return {item.strip().upper() for item in value.split(",") if item.strip()}


def select(
    rows: Iterable[dict[str, str]],
    marketplace: str | None,
    metric: str | None,
    ad_product: str | None,
    contains: str | None,
) -> list[tuple[int, dict[str, str]]]:
    selected: list[tuple[int, dict[str, str]]] = []
    for csv_line, row in enumerate(rows, start=2):
        if marketplace and marketplace.upper() not in marketplace_tokens(row["Marketplaces"]):
            continue
        if metric and metric.casefold() not in row["Metrics"].casefold():
            continue
        if ad_product and ad_product.casefold() not in row["Ad Products"].casefold():
            continue
        if contains and contains.casefold() not in row["Content"].casefold():
            continue
        selected.append((csv_line, row))
    return selected


def print_summary(rows: list[dict[str, str]]) -> None:
    print(f"records\t{len(rows)}")
    for label, key in (("metric", "Metrics"), ("ad_product", "Ad Products")):
        for value, count in Counter(row[key] for row in rows).most_common():
            print(f"{label}\t{count}\t{value}")


def print_markdown(rows: list[tuple[int, dict[str, str]]]) -> None:
    for line, row in rows:
        print(f"### CSV line {line}: {row['Marketplaces']} · {row['Metrics']} · {row['Ad Products']}")
        print()
        print(row["Content"])
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marketplace", help="Exact token such as US, DE, EU, or All")
    parser.add_argument("--metric", help="Substring match, e.g. ROAS or DPV")
    parser.add_argument("--ad-product", help="Substring match, e.g. Sponsored Brands")
    parser.add_argument("--contains", help="Case-insensitive text required in the full qualifier")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    rows = load_rows()
    if args.summary:
        print_summary(rows)
        return

    selected = select(rows, args.marketplace, args.metric, args.ad_product, args.contains)
    if args.format == "json":
        payload = [{"csv_line": line, **row} for line, row in selected]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_markdown(selected)
    if not selected:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
