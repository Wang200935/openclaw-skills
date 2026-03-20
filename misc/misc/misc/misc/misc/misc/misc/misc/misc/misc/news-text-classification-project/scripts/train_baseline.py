from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


DEFAULT_TEXT_COLUMN_CANDIDATES = ["clean_text", "text", "title", "content"]
DEFAULT_LABEL_COLUMN_CANDIDATES = ["label", "category", "class"]
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "outputs" / "baseline"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train TF-IDF baseline models for Chinese news title classification."
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Path to input CSV file. Must contain text and label columns.",
    )
    parser.add_argument(
        "--text-column",
        type=str,
        default=None,
        help="Name of text column. If omitted, common candidates will be auto-detected.",
    )
    parser.add_argument(
        "--label-column",
        type=str,
        default=None,
        help="Name of label column. If omitted, common candidates will be auto-detected.",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Test split ratio. Default: 0.2",
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=42,
        help="Random seed for reproducibility. Default: 42",
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=20000,
        help="Max TF-IDF features. Default: 20000",
    )
    parser.add_argument(
        "--min-df",
        type=int,
        default=1,
        help="Minimum document frequency for TF-IDF. Default: 1",
    )
    parser.add_argument(
        "--ngram-max",
        type=int,
        default=2,
        choices=[1, 2, 3],
        help="Upper n-gram bound for TF-IDF. Default: 2",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to save metrics and confusion matrices. Default: {DEFAULT_OUTPUT_DIR}",
    )
    return parser.parse_args()


def detect_column(columns: list[str], explicit_name: str | None, candidates: list[str], role: str) -> str:
    if explicit_name:
        if explicit_name not in columns:
            raise ValueError(f"Specified {role} column '{explicit_name}' not found. Available columns: {columns}")
        return explicit_name

    for candidate in candidates:
        if candidate in columns:
            return candidate

    raise ValueError(
        f"Could not auto-detect {role} column. Available columns: {columns}. "
        f"Please provide --{role}-column explicitly."
    )


def load_dataset(input_path: Path, text_column: str | None, label_column: str | None) -> tuple[pd.DataFrame, str, str]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    if df.empty:
        raise ValueError("Input dataset is empty.")

    text_col = detect_column(df.columns.tolist(), text_column, DEFAULT_TEXT_COLUMN_CANDIDATES, "text")
    label_col = detect_column(df.columns.tolist(), label_column, DEFAULT_LABEL_COLUMN_CANDIDATES, "label")

    df = df[[text_col, label_col]].copy()
    df[text_col] = df[text_col].fillna("").astype(str).str.strip()
    df[label_col] = df[label_col].fillna("").astype(str).str.strip()
    df = df[(df[text_col] != "") & (df[label_col] != "")].reset_index(drop=True)

    if len(df) < 2:
        raise ValueError("Dataset must contain at least 2 non-empty samples after cleaning.")

    if df[label_col].nunique() < 2:
        raise ValueError("Dataset must contain at least 2 unique labels.")

    return df, text_col, label_col


def build_models(max_features: int, min_df: int, ngram_max: int) -> dict[str, Pipeline]:
    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(1, ngram_max),
        max_features=max_features,
        min_df=min_df,
        sublinear_tf=True,
    )

    return {
        "naive_bayes": Pipeline(
            [
                ("tfidf", vectorizer),
                ("classifier", MultinomialNB()),
            ]
        ),
        "logistic_regression": Pipeline(
            [
                ("tfidf", vectorizer),
                (
                    "classifier",
                    LogisticRegression(
                        max_iter=1000,
                        solver="liblinear",
                        random_state=42,
                    ),
                ),
            ]
        ),
    }


def evaluate_model(
    model_name: str,
    pipeline: Pipeline,
    x_train: pd.Series,
    x_test: pd.Series,
    y_train: pd.Series,
    y_test: pd.Series,
    labels: list[str],
) -> dict[str, Any]:
    pipeline.fit(x_train, y_train)
    y_pred = pipeline.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro")
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    report = classification_report(y_test, y_pred, labels=labels, output_dict=True, zero_division=0)

    return {
        "model_name": model_name,
        "accuracy": round(float(accuracy), 6),
        "macro_f1": round(float(macro_f1), 6),
        "labels": labels,
        "confusion_matrix": cm.tolist(),
        "classification_report": report,
        "test_samples": int(len(y_test)),
        "train_samples": int(len(y_train)),
    }


def save_outputs(results: dict[str, dict[str, Any]], output_dir: Path, metadata: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    metrics_summary = []
    for model_name, result in results.items():
        metrics_summary.append(
            {
                "model_name": model_name,
                "accuracy": result["accuracy"],
                "macro_f1": result["macro_f1"],
                "train_samples": result["train_samples"],
                "test_samples": result["test_samples"],
            }
        )

        with (output_dir / f"{model_name}_metrics.json").open("w", encoding="utf-8") as f:
            json.dump({"metadata": metadata, "result": result}, f, ensure_ascii=False, indent=2)

        cm_df = pd.DataFrame(
            result["confusion_matrix"],
            index=result["labels"],
            columns=result["labels"],
        )
        cm_df.to_csv(output_dir / f"{model_name}_confusion_matrix.csv", encoding="utf-8-sig")

    summary_payload = {
        "metadata": metadata,
        "results": metrics_summary,
    }
    with (output_dir / "metrics_summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary_payload, f, ensure_ascii=False, indent=2)

    pd.DataFrame(metrics_summary).to_csv(output_dir / "metrics_summary.csv", index=False, encoding="utf-8-sig")


def main() -> None:
    args = parse_args()

    df, text_col, label_col = load_dataset(args.input, args.text_column, args.label_column)

    stratify_labels = df[label_col] if df[label_col].nunique() > 1 else None
    x_train, x_test, y_train, y_test = train_test_split(
        df[text_col],
        df[label_col],
        test_size=args.test_size,
        random_state=args.random_state,
        stratify=stratify_labels,
    )

    labels = sorted(df[label_col].unique().tolist())
    models = build_models(
        max_features=args.max_features,
        min_df=args.min_df,
        ngram_max=args.ngram_max,
    )

    metadata = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "input_file": str(args.input.resolve()),
        "text_column": text_col,
        "label_column": label_col,
        "num_samples": int(len(df)),
        "num_classes": int(df[label_col].nunique()),
        "class_distribution": df[label_col].value_counts().sort_index().to_dict(),
        "test_size": args.test_size,
        "random_state": args.random_state,
        "tfidf": {
            "analyzer": "char",
            "ngram_range": [1, args.ngram_max],
            "max_features": args.max_features,
            "min_df": args.min_df,
            "sublinear_tf": True,
        },
    }

    results: dict[str, dict[str, Any]] = {}
    print("=== Baseline Training Start ===")
    print(f"Dataset: {args.input}")
    print(f"Text column: {text_col}")
    print(f"Label column: {label_col}")
    print(f"Samples: {len(df)} | Classes: {df[label_col].nunique()}")
    print()

    for model_name, pipeline in models.items():
        result = evaluate_model(model_name, pipeline, x_train, x_test, y_train, y_test, labels)
        results[model_name] = result
        print(f"[{model_name}]")
        print(f"  Accuracy : {result['accuracy']:.4f}")
        print(f"  Macro F1 : {result['macro_f1']:.4f}")
        print(f"  Saved CM : {args.output_dir / f'{model_name}_confusion_matrix.csv'}")
        print()

    save_outputs(results, args.output_dir, metadata)
    print(f"Saved summary: {args.output_dir / 'metrics_summary.json'}")
    print("=== Baseline Training Finished ===")


if __name__ == "__main__":
    main()
