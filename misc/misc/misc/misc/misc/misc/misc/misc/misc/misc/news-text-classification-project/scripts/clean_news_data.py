from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Iterable


DEFAULT_REQUIRED_FIELDS = ["title", "label"]
DEFAULT_OUTPUT_FIELDS = ["title", "label", "source", "date", "url"]
DEFAULT_LABEL_ALIASES = {
    "politics": "政治",
    "政治": "政治",
    "政經": "政治",
    "國際政治": "政治",
    "society": "社會",
    "社會": "社會",
    "生活": "社會",
    "local": "社會",
    "international": "國際",
    "world": "國際",
    "國際": "國際",
    "global": "國際",
    "business": "財經",
    "finance": "財經",
    "economy": "財經",
    "財經": "財經",
    "經濟": "財經",
    "sports": "體育",
    "sport": "體育",
    "體育": "體育",
    "娛樂": "娛樂",
    "entertainment": "娛樂",
    "showbiz": "娛樂",
    "technology": "科技",
    "tech": "科技",
    "科技": "科技",
    "science": "科技",
    "health": "健康",
    "健康": "健康",
    "education": "教育",
    "教育": "教育",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Clean a raw news-title CSV by validating fields, normalizing labels, "
            "deduplicating titles, and writing a clean CSV."
        )
    )
    parser.add_argument("input_csv", type=Path, help="Path to the raw input CSV")
    parser.add_argument("output_csv", type=Path, help="Path to the cleaned output CSV")
    parser.add_argument(
        "--encoding",
        default="utf-8-sig",
        help="CSV encoding for both input and output (default: utf-8-sig)",
    )
    parser.add_argument(
        "--required-fields",
        nargs="+",
        default=DEFAULT_REQUIRED_FIELDS,
        help="Columns that must be present and non-empty (default: title label)",
    )
    parser.add_argument(
        "--keep-extra-columns",
        action="store_true",
        help="Keep all original columns instead of writing only the standard output fields",
    )
    parser.add_argument(
        "--drop-unknown-labels",
        action="store_true",
        help="Drop rows whose labels cannot be mapped by the alias table",
    )
    return parser.parse_args()


def normalize_text(value: str) -> str:
    text = unicodedata.normalize("NFKC", value or "")
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def normalize_title(title: str) -> str:
    text = normalize_text(title)
    text = re.sub(r"[\u200b\ufeff]", "", text)
    return text


def title_dedupe_key(title: str) -> str:
    text = normalize_title(title)
    text = text.casefold()
    text = re.sub(r"\s+", "", text)
    return text


def normalize_label(label: str, aliases: dict[str, str]) -> str:
    raw = normalize_text(label)
    key = raw.casefold()
    return aliases.get(key, raw)


def validate_header(fieldnames: Iterable[str] | None, required_fields: list[str]) -> list[str]:
    if not fieldnames:
        raise ValueError("Input CSV has no header row.")

    columns = [name.strip() for name in fieldnames if name is not None]
    missing = [field for field in required_fields if field not in columns]
    if missing:
        raise ValueError(f"Input CSV is missing required columns: {', '.join(missing)}")
    return columns


def clean_rows(
    rows: Iterable[dict[str, str]],
    required_fields: list[str],
    drop_unknown_labels: bool,
    aliases: dict[str, str],
) -> tuple[list[dict[str, str]], Counter]:
    stats = Counter()
    cleaned_rows: list[dict[str, str]] = []
    seen_titles: set[str] = set()

    for row_number, row in enumerate(rows, start=2):
        stats["rows_read"] += 1
        normalized_row = {key.strip(): normalize_text(value) for key, value in row.items() if key is not None}

        missing_values = [field for field in required_fields if not normalized_row.get(field, "")]
        if missing_values:
            stats["rows_dropped_missing_required"] += 1
            continue

        normalized_row["title"] = normalize_title(normalized_row["title"])
        normalized_row["label"] = normalize_label(normalized_row["label"], aliases)

        if drop_unknown_labels and normalized_row["label"] == normalize_text(row.get("label", "")):
            original = normalize_text(row.get("label", ""))
            if original.casefold() not in aliases:
                stats["rows_dropped_unknown_label"] += 1
                continue

        dedupe_key = title_dedupe_key(normalized_row["title"])
        if not dedupe_key:
            stats["rows_dropped_empty_title_after_cleaning"] += 1
            continue

        if dedupe_key in seen_titles:
            stats["rows_dropped_duplicate_title"] += 1
            continue

        seen_titles.add(dedupe_key)
        cleaned_rows.append(normalized_row)
        stats["rows_kept"] += 1

    return cleaned_rows, stats


def choose_output_fields(columns: list[str], keep_extra_columns: bool) -> list[str]:
    if keep_extra_columns:
        return columns

    ordered = [field for field in DEFAULT_OUTPUT_FIELDS if field in columns]
    extras = [field for field in columns if field not in ordered and field not in DEFAULT_OUTPUT_FIELDS]
    return ordered + extras


def write_csv(output_path: Path, rows: list[dict[str, str]], fieldnames: list[str], encoding: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()

    if not args.input_csv.exists():
        print(f"Input CSV not found: {args.input_csv}", file=sys.stderr)
        return 1

    try:
        with args.input_csv.open("r", encoding=args.encoding, newline="") as f:
            reader = csv.DictReader(f)
            columns = validate_header(reader.fieldnames, args.required_fields)
            cleaned_rows, stats = clean_rows(
                rows=reader,
                required_fields=args.required_fields,
                drop_unknown_labels=args.drop_unknown_labels,
                aliases=DEFAULT_LABEL_ALIASES,
            )
    except Exception as exc:
        print(f"Cleaning failed: {exc}", file=sys.stderr)
        return 1

    output_fields = choose_output_fields(columns, args.keep_extra_columns)
    write_csv(args.output_csv, cleaned_rows, output_fields, args.encoding)

    print("Cleaning complete")
    print(f"- input: {args.input_csv}")
    print(f"- output: {args.output_csv}")
    print(f"- rows read: {stats['rows_read']}")
    print(f"- rows kept: {stats['rows_kept']}")
    print(f"- dropped missing required: {stats['rows_dropped_missing_required']}")
    print(f"- dropped duplicate title: {stats['rows_dropped_duplicate_title']}")
    print(f"- dropped unknown label: {stats['rows_dropped_unknown_label']}")
    print(f"- dropped empty title after cleaning: {stats['rows_dropped_empty_title_after_cleaning']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
