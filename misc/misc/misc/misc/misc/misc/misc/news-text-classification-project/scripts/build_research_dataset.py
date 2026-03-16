from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert raw collector CSV(s) into a research-schema dataset usable by cleaning/training."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="One or more raw collector CSV files",
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schemas" / "label_mapping.csv",
        help="Path to label mapping CSV",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "interim" / "research_dataset_mapped.csv",
        help="Path to mapped dataset CSV",
    )
    return parser.parse_args()


def normalize(value: Any) -> str:
    return str(value or "").strip()


def load_mapping(path: Path) -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw_label = normalize(row.get("raw_label")).casefold()
            if not raw_label:
                continue
            mapping[raw_label] = {
                "category_final": normalize(row.get("category_final")),
                "include": normalize(row.get("include")).lower() or "yes",
                "notes": normalize(row.get("notes")),
                "example_hint": normalize(row.get("example_hint")),
            }
    return mapping


def candidate_raw_label(row: dict[str, str]) -> str:
    for key in ("category", "section", "category_raw", "label"):
        value = normalize(row.get(key))
        if value:
            return value
    return ""


def date_only(value: str) -> str:
    value = normalize(value)
    if not value:
        return ""
    if "T" in value:
        return value.split("T", 1)[0]
    if " " in value and len(value) >= 10:
        return value[:10]
    return value[:10] if len(value) >= 10 else value


def make_id(source: str, url: str, title: str) -> str:
    h = hashlib.sha1(f"{source}|{url}|{title}".encode("utf-8")).hexdigest()[:12]
    return f"news_{h}"


def transform_row(row: dict[str, str], mapping: dict[str, dict[str, str]]) -> dict[str, str]:
    source = normalize(row.get("source")) or normalize(row.get("source_site"))
    title = normalize(row.get("title"))
    category_raw = candidate_raw_label(row)
    mapping_row = mapping.get(category_raw.casefold(), None)

    category_final = ""
    include = "yes"
    mapping_rule = ""
    note = normalize(row.get("notes"))

    if mapping_row:
        include = mapping_row["include"] or "yes"
        category_final = mapping_row["category_final"]
        mapping_rule = f"{category_raw}->{category_final or 'exclude'}"
        if mapping_row.get("notes"):
            note = "; ".join([x for x in [note, mapping_row["notes"]] if x])
    else:
        include = "no"
        mapping_rule = f"{category_raw}->unmapped"
        if category_raw:
            note = "; ".join([x for x in [note, "raw label not found in mapping"] if x])

    url = normalize(row.get("url")) or normalize(row.get("article_url"))
    collected_at = normalize(row.get("collected_at")) or normalize(row.get("crawl_time_iso"))
    date = normalize(row.get("date")) or date_only(normalize(row.get("published_at_iso")) or normalize(row.get("published_at_raw")))

    return {
        "id": make_id(source, url, title),
        "title": title,
        "label": category_final,
        "category_raw": category_raw,
        "category_final": category_final,
        "source": source,
        "date": date,
        "url": url,
        "collected_at": collected_at,
        "is_included": include,
        "mapping_rule": mapping_rule,
        "note": note,
    }


def main() -> None:
    args = parse_args()
    mapping = load_mapping(args.mapping)
    rows_out: list[dict[str, str]] = []
    stats = Counter()

    for input_path in args.inputs:
        with input_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                stats["rows_read"] += 1
                out = transform_row(row, mapping)
                if not out["title"]:
                    stats["rows_dropped_empty_title"] += 1
                    continue
                rows_out.append(out)
                stats["rows_written"] += 1
                if out["is_included"] == "yes":
                    stats["rows_included"] += 1
                else:
                    stats["rows_excluded"] += 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "title",
        "label",
        "category_raw",
        "category_final",
        "source",
        "date",
        "url",
        "collected_at",
        "is_included",
        "mapping_rule",
        "note",
    ]
    with args.output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_out)

    print("Mapped research dataset built")
    print(f"- output: {args.output}")
    for k in ["rows_read", "rows_written", "rows_included", "rows_excluded", "rows_dropped_empty_title"]:
        print(f"- {k}: {stats[k]}")


if __name__ == "__main__":
    main()
