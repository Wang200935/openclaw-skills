---
name: news-text-classification-project
description: End-to-end implementation for the Chinese news-title classification high-school paper. Use when you need the full pipeline in this workspace (collection → mapping/cleaning → baseline training → metrics/plots → judge-facing materials), including the exact scripts and reference documents used in this project.
---

# News Text Classification Project

Use this skill to run the full implementation used in this workspace (paper_project), from collection to paper outputs.

## Quick start

1. Create or locate the project root (default: `paper_project/`).
2. Copy scripts from this skill into the project so relative paths resolve correctly:
   - Copy `skills/news-text-classification-project/scripts/*.py` → `paper_project/code/`
3. Follow the execution order in `references/run_order.md` and the build checklist in `references/README_build_order.md`.

## Core workflow (canonical order)

### 1) Data collection
- Edit `code/collect_news_titles.py` (TARGET_SITE + selectors) for each source.
- Run per source and save outputs under `data/raw/`.
- Use `code/collect_news_titles_alt.py` for alternative list-page patterns when needed.

### 2) Mapping → research dataset
- Update `references/label_mapping.csv` to match final categories.
- Build mapped dataset:
  - `python code/build_research_dataset.py data/raw/*.csv --mapping schemas/label_mapping.csv --output data/interim/research_dataset_mapped.csv`

### 3) Cleaning
- Clean and deduplicate:
  - `python code/clean_news_data.py data/interim/research_dataset_mapped.csv data/processed/news_titles_clean.csv --drop-unknown-labels`
- Use `references/data_cleaning_explainer.md` and `references/output_naming_rules.md` for checks.

### 4) Baseline training
- Train baseline models:
  - `python code/train_baseline.py --input data/processed/news_titles_clean.csv --output-dir outputs/baseline`
- Prepare plot inputs:
  - `python code/prepare_plot_inputs.py --input-dir outputs/baseline --output-dir results/metrics`

### 5) Visualization
- Generate figures:
  - `python code/plot_results.py --dataset data/processed/news_titles_clean.csv --output-dir results/figures`
- Optional exploratory visual:
  - `python code/explore_wordcloud.py`

### 6) Judge-facing materials
- Use `references/judge_package_checklist.md`, `references/demo_script.md`, and `references/diagram-plan.md` to assemble the final package.

## Scripts (copied into project `code/`)
- `collect_news_titles.py`: Single-site crawler template (fill selectors + pagination).
- `collect_news_titles_alt.py`: Alternative crawler pattern.
- `build_research_dataset.py`: Map raw labels to final categories; output mapped dataset.
- `clean_news_data.py`: Clean, normalize, dedupe, and export clean dataset.
- `train_baseline.py`: Baseline TF-IDF models + metrics/confusion matrices.
- `prepare_plot_inputs.py`: Convert training outputs into plotting-ready metrics.
- `plot_results.py`: Generate class distribution, model comparison, confusion matrix figures.
- `explore_wordcloud.py`: Optional word cloud exploration.
- `tokenizer_config.py`: Tokenization notes/config scaffold.

## References (read when needed)

### Project planning and order
- `references/README_build_order.md`
- `references/run_order.md`
- `references/paper_start_plan.md`

### Data, schema, and mapping
- `references/data_dictionary.md`
- `references/data_cleaning_explainer.md`
- `references/output_naming_rules.md`
- `references/news_schema.md`
- `references/label_mapping.csv`
- `references/source_selection.md`

### Modeling and evaluation
- `references/experiment_matrix.md`
- `references/baseline_hyperparameters.md`
- `references/tokenization_notes.md`
- `references/error_case_selection.md`

### Judge-facing package
- `references/judge_package_checklist.md`
- `references/demo_script.md`
- `references/literature_method_bridge.md`
- `references/diagram-plan.md`
- `references/visualization-plan.md`
