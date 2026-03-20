from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare plot-friendly files from baseline training outputs.")
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "outputs" / "baseline",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "metrics",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    summary_csv = args.input_dir / "metrics_summary.csv"
    if not summary_csv.exists():
        raise FileNotFoundError(f"Missing summary CSV: {summary_csv}")

    df = pd.read_csv(summary_csv)
    if "model_name" in df.columns and "model" not in df.columns:
        df = df.rename(columns={"model_name": "model"})
    if "feature" not in df.columns and "vectorizer" not in df.columns:
        df["feature"] = "TF-IDF(char)"

    model_metrics_csv = args.output_dir / "model_metrics.csv"
    model_metrics_json = args.output_dir / "model_metrics.json"
    df.to_csv(model_metrics_csv, index=False, encoding="utf-8-sig")
    df.to_json(model_metrics_json, orient="records", force_ascii=False, indent=2)

    best_row = df.sort_values(["macro_f1", "accuracy"], ascending=False).iloc[0]
    best_model = str(best_row["model"])
    src_cm = args.input_dir / f"{best_model}_confusion_matrix.csv"
    dst_cm = args.output_dir / "best_model_confusion_matrix.csv"
    if not src_cm.exists():
        raise FileNotFoundError(f"Missing confusion matrix for best model: {src_cm}")
    cm_df = pd.read_csv(src_cm, index_col=0)
    cm_df.to_csv(dst_cm, encoding="utf-8-sig")

    labels = [str(x) for x in cm_df.columns.tolist()]
    with (args.output_dir / "labels.json").open("w", encoding="utf-8") as f:
        json.dump(labels, f, ensure_ascii=False, indent=2)

    print("Prepared plot inputs")
    print(f"- best_model: {best_model}")
    print(f"- model_metrics: {model_metrics_csv}")
    print(f"- confusion_matrix: {dst_cm}")


if __name__ == "__main__":
    main()
