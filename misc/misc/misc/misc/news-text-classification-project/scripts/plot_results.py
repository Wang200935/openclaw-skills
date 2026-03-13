from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
METRICS_DIR = RESULTS_DIR / "metrics"

DEFAULT_DATASET = PROCESSED_DIR / "news_titles_clean.csv"
DEFAULT_MODEL_METRICS_CSV = METRICS_DIR / "model_metrics.csv"
DEFAULT_MODEL_METRICS_JSON = METRICS_DIR / "model_metrics.json"
DEFAULT_CONFUSION_MATRIX_CSV = METRICS_DIR / "best_model_confusion_matrix.csv"
DEFAULT_CONFUSION_MATRIX_JSON = METRICS_DIR / "best_model_confusion_matrix.json"
DEFAULT_LABELS_PATH = METRICS_DIR / "labels.json"

sns.set_theme(style="whitegrid", context="talk")


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)



def save_figure(output_path: Path, dpi: int = 300) -> None:
    ensure_output_dir(output_path.parent)
    plt.tight_layout()
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close()
    print(f"Saved figure: {output_path}")



def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)



def normalize_model_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
        "macro_f1": "Macro F1",
        "f1_macro": "Macro F1",
        "accuracy": "Accuracy",
        "precision_macro": "Macro Precision",
        "recall_macro": "Macro Recall",
        "model": "Model",
        "feature": "Feature",
        "vectorizer": "Feature",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    if "Model" not in df.columns:
        raise ValueError("Model metrics file must include a 'model' or 'Model' column.")

    if "Feature" not in df.columns:
        df["Feature"] = "Unknown"

    df["Display Name"] = df["Feature"].astype(str) + " + " + df["Model"].astype(str)
    return df



def pick_score_column(df: pd.DataFrame) -> str:
    candidates = ["Macro F1", "Accuracy", "Macro Precision", "Macro Recall"]
    for col in candidates:
        if col in df.columns:
            return col
    raise ValueError(
        "No supported score column found. Expected one of: macro_f1/f1_macro, accuracy, precision_macro, recall_macro."
    )



def load_model_metrics(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Model metrics file not found: {path}")

    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    elif path.suffix.lower() == ".json":
        payload = load_json(path)
        if isinstance(payload, list):
            df = pd.DataFrame(payload)
        elif isinstance(payload, dict):
            if "results" in payload and isinstance(payload["results"], list):
                df = pd.DataFrame(payload["results"])
            else:
                df = pd.DataFrame([payload])
        else:
            raise ValueError(f"Unsupported JSON structure in {path}")
    else:
        raise ValueError(f"Unsupported metrics file format: {path.suffix}")

    return normalize_model_metrics(df)



def infer_label_column(df: pd.DataFrame) -> str:
    for column in ["category_final", "label", "category", "target"]:
        if column in df.columns:
            return column
    raise ValueError(
        "Could not infer label column. Expected one of: category_final, label, category, target."
    )



def load_confusion_matrix(matrix_path: Path, labels_path: Path | None = None) -> tuple[np.ndarray, list[str]]:
    if not matrix_path.exists():
        raise FileNotFoundError(f"Confusion matrix file not found: {matrix_path}")

    suffix = matrix_path.suffix.lower()

    if suffix == ".csv":
        df = pd.read_csv(matrix_path, index_col=0)
        labels = [str(x) for x in df.columns.tolist()]
        matrix = df.to_numpy()
        return matrix, labels

    if suffix == ".json":
        payload = load_json(matrix_path)
        if isinstance(payload, dict) and "matrix" in payload:
            matrix = np.array(payload["matrix"])
            labels = payload.get("labels")
            if labels is None and labels_path and labels_path.exists():
                labels = load_json(labels_path)
            if labels is None:
                labels = [str(i) for i in range(matrix.shape[0])]
            return matrix, [str(x) for x in labels]
        raise ValueError("JSON confusion matrix must contain a 'matrix' key.")

    if suffix == ".npy":
        matrix = np.load(matrix_path)
        labels = None
        if labels_path and labels_path.exists():
            labels = load_json(labels_path)
        if labels is None:
            labels = [str(i) for i in range(matrix.shape[0])]
        return matrix, [str(x) for x in labels]

    raise ValueError(f"Unsupported confusion matrix format: {suffix}")


# ---------------------------------------------------------------------------
# Plotting functions
# ---------------------------------------------------------------------------

def plot_class_distribution(
    dataset_path: Path,
    output_path: Path,
    label_column: str | None = None,
    title: str = "Class Distribution",
) -> None:
    df = pd.read_csv(dataset_path)
    label_column = label_column or infer_label_column(df)

    counts = (
        df[label_column]
        .astype(str)
        .value_counts()
        .sort_values(ascending=False)
        .rename_axis("label")
        .reset_index(name="count")
    )

    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=counts, x="label", y="count", palette="Blues_d")
    ax.set_title(title)
    ax.set_xlabel("Class")
    ax.set_ylabel("Number of Titles")

    for idx, value in enumerate(counts["count"]):
        ax.text(idx, value, str(value), ha="center", va="bottom", fontsize=11)

    save_figure(output_path)



def plot_model_comparison(
    metrics_path: Path,
    output_path: Path,
    score_column: str | None = None,
    title: str = "Model Comparison",
) -> None:
    df = load_model_metrics(metrics_path)
    score_column = score_column or pick_score_column(df)

    plot_df = df.sort_values(score_column, ascending=False).copy()

    plt.figure(figsize=(12, 7))
    ax = sns.barplot(data=plot_df, x=score_column, y="Display Name", palette="viridis")
    ax.set_title(f"{title} ({score_column})")
    ax.set_xlabel(score_column)
    ax.set_ylabel("Pipeline")

    for container in ax.containers:
        ax.bar_label(container, fmt="%.3f", padding=6, fontsize=10)

    save_figure(output_path)



def plot_confusion_matrix(
    matrix_path: Path,
    output_path: Path,
    labels_path: Path | None = None,
    title: str = "Confusion Matrix",
    normalize: bool = False,
) -> None:
    matrix, labels = load_confusion_matrix(matrix_path, labels_path=labels_path)
    matrix = np.asarray(matrix, dtype=float)

    if normalize:
        row_sums = matrix.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        matrix = matrix / row_sums

    annot_fmt = ".2f" if normalize else ".0f"
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(
        matrix,
        annot=True,
        fmt=annot_fmt,
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels,
        cbar=True,
    )
    ax.set_title(title + (" (Normalized)" if normalize else ""))
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("True Label")

    save_figure(output_path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_existing_file(preferred: Path, fallback: Path | None = None) -> Path:
    if preferred.exists():
        return preferred
    if fallback and fallback.exists():
        return fallback
    return preferred



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate charts for the Chinese news title classification paper."
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=DEFAULT_DATASET,
        help="Path to cleaned dataset CSV for class distribution plotting.",
    )
    parser.add_argument(
        "--metrics",
        type=Path,
        default=resolve_existing_file(DEFAULT_MODEL_METRICS_CSV, DEFAULT_MODEL_METRICS_JSON),
        help="Path to model metrics CSV/JSON.",
    )
    parser.add_argument(
        "--confusion-matrix",
        type=Path,
        default=resolve_existing_file(DEFAULT_CONFUSION_MATRIX_CSV, DEFAULT_CONFUSION_MATRIX_JSON),
        help="Path to confusion matrix CSV/JSON/NPY.",
    )
    parser.add_argument(
        "--labels",
        type=Path,
        default=DEFAULT_LABELS_PATH,
        help="Optional labels JSON path for NPY/JSON confusion matrix input.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=FIGURES_DIR,
        help="Directory where generated figures will be saved.",
    )
    parser.add_argument(
        "--label-column",
        type=str,
        default=None,
        help="Optional label column name in dataset CSV.",
    )
    parser.add_argument(
        "--score-column",
        type=str,
        default=None,
        help="Optional metrics score column to plot, e.g. 'Macro F1' or 'Accuracy'.",
    )
    parser.add_argument(
        "--skip-class-distribution",
        action="store_true",
        help="Skip class distribution chart.",
    )
    parser.add_argument(
        "--skip-model-comparison",
        action="store_true",
        help="Skip model comparison chart.",
    )
    parser.add_argument(
        "--skip-confusion-matrix",
        action="store_true",
        help="Skip confusion matrix chart.",
    )
    parser.add_argument(
        "--normalized-confusion-matrix",
        action="store_true",
        help="Also generate a normalized confusion matrix heatmap.",
    )
    return parser



def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    ensure_output_dir(args.output_dir)

    if not args.skip_class_distribution:
        plot_class_distribution(
            dataset_path=args.dataset,
            output_path=args.output_dir / "class_distribution.png",
            label_column=args.label_column,
            title="News Title Class Distribution",
        )

    if not args.skip_model_comparison:
        plot_model_comparison(
            metrics_path=args.metrics,
            output_path=args.output_dir / "model_comparison.png",
            score_column=args.score_column,
            title="Baseline Model Performance Comparison",
        )

    if not args.skip_confusion_matrix:
        plot_confusion_matrix(
            matrix_path=args.confusion_matrix,
            output_path=args.output_dir / "confusion_matrix.png",
            labels_path=args.labels,
            title="Best Model Confusion Matrix",
            normalize=False,
        )

        if args.normalized_confusion_matrix:
            plot_confusion_matrix(
                matrix_path=args.confusion_matrix,
                output_path=args.output_dir / "confusion_matrix_normalized.png",
                labels_path=args.labels,
                title="Best Model Confusion Matrix",
                normalize=True,
            )


if __name__ == "__main__":
    main()
