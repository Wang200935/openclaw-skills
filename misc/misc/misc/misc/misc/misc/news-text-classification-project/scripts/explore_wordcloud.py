from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

import jieba
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager
from wordcloud import WordCloud


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"

DEFAULT_INPUT_CANDIDATES = [
    PROCESSED_DIR / "news_titles_clean.csv",
    DATA_DIR / "news_titles_clean.csv",
    PROJECT_ROOT / "news_titles_clean.csv",
]
DEFAULT_OUTPUT_DIR = FIGURES_DIR / "exploration"
DEFAULT_STOPWORDS = {
    "記者",
    "新聞",
    "中央社",
    "報導",
    "表示",
    "指出",
    "今天",
    "明天",
    "今年",
    "去年",
    "目前",
    "是否",
    "相關",
    "真的",
    "可以",
    "可能",
    "已",
    "將",
    "仍",
    "讓",
    "遭",
    "被",
    "與",
    "和",
    "及",
    "對",
    "在",
    "於",
    "是",
    "了",
    "但",
    "也",
    "又",
    "上",
    "下",
    "中",
    "後",
    "前",
    "個",
    "名",
    "曝",
    "稱",
}
DEFAULT_TEXT_COLUMN_CANDIDATES = ["clean_text", "text", "title", "headline"]
DEFAULT_LABEL_COLUMN_CANDIDATES = ["label", "category_final", "category", "class"]
DEFAULT_FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/msjh.ttc"),
    Path("C:/Windows/Fonts/msyh.ttc"),
    Path("C:/Windows/Fonts/simsun.ttc"),
    Path("C:/Windows/Fonts/kaiu.ttf"),
]


jieba.initialize()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Chinese word clouds and token-frequency summaries for news-title exploration."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help="Path to CSV dataset. If omitted, common project paths will be tried.",
    )
    parser.add_argument(
        "--text-column",
        type=str,
        default=None,
        help="Text column to analyze. If omitted, common title/text columns are auto-detected.",
    )
    parser.add_argument(
        "--label-column",
        type=str,
        default=None,
        help="Optional label column for class-wise exploration.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for generated images and CSV files. Default: {DEFAULT_OUTPUT_DIR}",
    )
    parser.add_argument(
        "--font-path",
        type=Path,
        default=None,
        help="Path to a Chinese font file for wordcloud rendering.",
    )
    parser.add_argument(
        "--stopwords-file",
        type=Path,
        default=None,
        help="Optional text file with one stopword per line.",
    )
    parser.add_argument(
        "--mask-image",
        type=Path,
        default=None,
        help="Optional mask image path for shaped word clouds.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=80,
        help="Max number of tokens to keep in each word cloud. Default: 80",
    )
    parser.add_argument(
        "--min-token-length",
        type=int,
        default=2,
        help="Minimum token length to keep. Default: 2",
    )
    parser.add_argument(
        "--min-frequency",
        type=int,
        default=2,
        help="Minimum token frequency to keep. Default: 2",
    )
    parser.add_argument(
        "--max-per-class",
        type=int,
        default=6,
        help="How many label groups to render for class-wise placeholders. Default: 6",
    )
    parser.add_argument(
        "--background-color",
        type=str,
        default="white",
        help="Wordcloud background color. Default: white",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1600,
        help="Wordcloud canvas width. Default: 1600",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=1000,
        help="Wordcloud canvas height. Default: 1000",
    )
    parser.add_argument(
        "--no-classwise",
        action="store_true",
        help="Only generate overall exploration outputs; skip class-wise placeholders.",
    )
    return parser.parse_args()


def resolve_input_path(explicit_path: Path | None) -> Path:
    if explicit_path is not None:
        if not explicit_path.exists():
            raise FileNotFoundError(f"Input dataset not found: {explicit_path}")
        return explicit_path

    for candidate in DEFAULT_INPUT_CANDIDATES:
        if candidate.exists():
            return candidate

    searched = "\n- ".join(str(path) for path in DEFAULT_INPUT_CANDIDATES)
    raise FileNotFoundError(
        "Could not find an input dataset automatically. Tried:\n- " + searched + "\nPlease pass --input explicitly."
    )


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


def load_stopwords(stopwords_file: Path | None) -> set[str]:
    stopwords = set(DEFAULT_STOPWORDS)
    if stopwords_file is None:
        return stopwords

    if not stopwords_file.exists():
        raise FileNotFoundError(f"Stopwords file not found: {stopwords_file}")

    with stopwords_file.open("r", encoding="utf-8") as f:
        for line in f:
            token = line.strip()
            if token:
                stopwords.add(token)
    return stopwords


def clean_text(text: str) -> str:
    text = str(text or "").strip()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[0-9０-９]+", " ", text)
    text = re.sub(r"[\t\r\n]+", " ", text)
    text = re.sub(r"[\[\]【】()（）<>《》「」『』“”‘’'\"，,。！？!?:：；/\\|~`@#$%^&*_+=-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize_texts(
    texts: Iterable[str],
    stopwords: set[str],
    min_token_length: int,
) -> list[str]:
    tokens: list[str] = []
    for text in texts:
        cleaned = clean_text(text)
        if not cleaned:
            continue
        for token in jieba.lcut(cleaned):
            token = token.strip()
            if not token:
                continue
            if token in stopwords:
                continue
            if len(token) < min_token_length:
                continue
            if re.fullmatch(r"[_\W]+", token):
                continue
            if token.isdigit():
                continue
            tokens.append(token)
    return tokens


def build_frequency(tokens: list[str], top_k: int, min_frequency: int) -> Counter[str]:
    counter = Counter(tokens)
    filtered = Counter({token: freq for token, freq in counter.items() if freq >= min_frequency})
    return Counter(dict(filtered.most_common(top_k)))


def resolve_font_path(explicit_font: Path | None) -> Path:
    if explicit_font is not None:
        if not explicit_font.exists():
            raise FileNotFoundError(f"Font file not found: {explicit_font}")
        return explicit_font

    for candidate in DEFAULT_FONT_CANDIDATES:
        if candidate.exists():
            return candidate

    available = font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
    if available:
        return Path(available[0])

    raise FileNotFoundError("No usable font file found for wordcloud rendering.")


def load_mask(mask_image: Path | None):
    if mask_image is None:
        return None
    if not mask_image.exists():
        raise FileNotFoundError(f"Mask image not found: {mask_image}")

    try:
        from PIL import Image
        import numpy as np
    except ImportError as exc:
        raise ImportError("Using --mask-image requires Pillow and numpy.") from exc

    return np.array(Image.open(mask_image))


def save_frequency_csv(freq: Counter[str], output_path: Path) -> None:
    df = pd.DataFrame(freq.most_common(), columns=["token", "frequency"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Saved frequency table: {output_path}")


def generate_wordcloud(
    freq: Counter[str],
    output_path: Path,
    font_path: Path,
    background_color: str,
    width: int,
    height: int,
    mask=None,
    title: str | None = None,
) -> None:
    if not freq:
        print(f"Skipped wordcloud (no tokens left after filtering): {output_path}")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    wc = WordCloud(
        font_path=str(font_path),
        background_color=background_color,
        width=width,
        height=height,
        max_words=len(freq),
        prefer_horizontal=0.95,
        collocations=False,
        mask=mask,
    )
    wc.generate_from_frequencies(dict(freq))

    plt.figure(figsize=(12, 7))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    if title:
        plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved wordcloud: {output_path}")


def slugify(value: str) -> str:
    value = re.sub(r"\s+", "_", str(value).strip())
    value = re.sub(r"[^0-9A-Za-z_\-\u4e00-\u9fff]", "", value)
    return value or "unknown"


def summarize_group(
    group_name: str,
    texts: Iterable[str],
    output_dir: Path,
    stopwords: set[str],
    min_token_length: int,
    min_frequency: int,
    top_k: int,
    font_path: Path,
    background_color: str,
    width: int,
    height: int,
    mask=None,
) -> Counter[str]:
    tokens = tokenize_texts(texts, stopwords=stopwords, min_token_length=min_token_length)
    freq = build_frequency(tokens, top_k=top_k, min_frequency=min_frequency)
    slug = slugify(group_name)

    save_frequency_csv(freq, output_dir / f"{slug}_top_tokens.csv")
    generate_wordcloud(
        freq=freq,
        output_path=output_dir / f"{slug}_wordcloud.png",
        font_path=font_path,
        background_color=background_color,
        width=width,
        height=height,
        mask=mask,
        title=group_name,
    )
    return freq


def main() -> None:
    args = parse_args()

    input_path = resolve_input_path(args.input)
    df = pd.read_csv(input_path)
    if df.empty:
        raise ValueError("Input dataset is empty.")

    text_column = detect_column(df.columns.tolist(), args.text_column, DEFAULT_TEXT_COLUMN_CANDIDATES, "text")
    label_column = None
    if args.label_column is not None:
        label_column = detect_column(df.columns.tolist(), args.label_column, DEFAULT_LABEL_COLUMN_CANDIDATES, "label")
    else:
        for candidate in DEFAULT_LABEL_COLUMN_CANDIDATES:
            if candidate in df.columns:
                label_column = candidate
                break

    df[text_column] = df[text_column].fillna("").astype(str).str.strip()
    df = df[df[text_column] != ""].copy()
    if df.empty:
        raise ValueError("No non-empty text rows available after cleaning input column.")

    stopwords = load_stopwords(args.stopwords_file)
    font_path = resolve_font_path(args.font_path)
    mask = load_mask(args.mask_image)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    print("=== Wordcloud Exploration Start ===")
    print(f"Input file    : {input_path}")
    print(f"Text column   : {text_column}")
    print(f"Label column  : {label_column or 'not found / skipped'}")
    print(f"Rows analyzed : {len(df)}")
    print(f"Output dir    : {args.output_dir}")
    print()

    overall_dir = args.output_dir / "overall"
    summarize_group(
        group_name="整體新聞標題詞雲",
        texts=df[text_column].tolist(),
        output_dir=overall_dir,
        stopwords=stopwords,
        min_token_length=args.min_token_length,
        min_frequency=args.min_frequency,
        top_k=args.top_k,
        font_path=font_path,
        background_color=args.background_color,
        width=args.width,
        height=args.height,
        mask=mask,
    )

    # Placeholder / first-pass class-wise exploration for judge-facing visuals.
    # When label quality is stable, you can directly use these per-class outputs
    # in the paper or pick representative classes for screenshots.
    if not args.no_classwise and label_column is not None:
        classwise_dir = args.output_dir / "by_class"
        counts = df[label_column].astype(str).value_counts()
        selected_labels = counts.index.tolist()[: args.max_per_class]

        summary_rows: list[dict[str, object]] = []
        for label in selected_labels:
            subset = df[df[label_column].astype(str) == str(label)]
            freq = summarize_group(
                group_name=f"類別詞雲：{label}",
                texts=subset[text_column].tolist(),
                output_dir=classwise_dir,
                stopwords=stopwords,
                min_token_length=args.min_token_length,
                min_frequency=args.min_frequency,
                top_k=args.top_k,
                font_path=font_path,
                background_color=args.background_color,
                width=args.width,
                height=args.height,
                mask=mask,
            )
            top_preview = "、".join(token for token, _ in freq.most_common(10))
            summary_rows.append(
                {
                    "label": label,
                    "samples": len(subset),
                    "unique_tokens": len(freq),
                    "top_tokens_preview": top_preview,
                }
            )

        if summary_rows:
            summary_df = pd.DataFrame(summary_rows)
            summary_path = classwise_dir / "classwise_summary.csv"
            summary_df.to_csv(summary_path, index=False, encoding="utf-8-sig")
            print(f"Saved class-wise summary: {summary_path}")
    elif not args.no_classwise:
        print("Label column not found, so class-wise placeholder outputs were skipped.")

    print("=== Wordcloud Exploration Finished ===")
    print("Suggested judge-facing usage:")
    print("1. Show the overall wordcloud as a quick data-understanding visual.")
    print("2. Pick 2-4 class-wise wordclouds to explain category differences.")
    print("3. Pair the images with top_tokens.csv tables for less subjective discussion.")


if __name__ == "__main__":
    main()
