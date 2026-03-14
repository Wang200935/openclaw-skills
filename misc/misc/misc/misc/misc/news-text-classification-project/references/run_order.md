# paper_project 執行順序整合筆記

這份文件是把 **目前已經存在的腳本**，對齊到這個專題應該展示給評審看的執行順序。

核心主線只有一條：

**資料蒐集 -> 資料清理 -> baseline 訓練 / 模型比較 -> 圖表輸出 -> 評審展示包整理**

重點不是一開始追最高分，而是把每一階段的輸入、輸出、證據檔都留好。

---

## 1. 目前已存在的主要腳本

### Collection
- `code/collect_news_titles.py`
- `code/collect_news_titles_alt.py`

### Cleaning
- `code/clean_news_data.py`
- `code/tokenizer_config.py`（偏設定 / 輔助，不是主流程入口）

### Training
- `code/train_baseline.py`

### Plotting / analysis visuals
- `code/plot_results.py`
- `code/explore_wordcloud.py`（偏補充分析，不是主主線必要步驟）

### Judge-facing / support docs
- `README_build_order.md`
- `judge_package_checklist.md`
- `experiment_matrix.md`
- `demo_script.md`
- `diagrams/workflow.mmd`
- `diagrams/data_pipeline.mmd`
- `diagrams/model_comparison.mmd`
- `schemas/label_mapping.csv`
- `schemas/news_schema.md`

---

## 2. 建議主流程執行順序

## Step 0：先確認規格，不直接跑程式

先看的文件：
- `schemas/news_schema.md`
- `schemas/label_mapping.csv`
- `README_build_order.md`
- `judge_package_checklist.md`

目的：
- 先確認欄位規格
- 先確認最終類別怎麼定
- 先確認評審要看的證據有哪些

如果這一步沒先對齊，後面最常出現的問題就是：
- 抓到的欄位和清理 / 訓練腳本對不起來
- label 名稱不一致
- 產物有分數，但不適合給評審展示

---

## Step 1：資料蒐集 Collection

### 主要腳本
- 主用：`code/collect_news_titles.py`
- 備用 / 替代版本：`code/collect_news_titles_alt.py`

### 這一步在做什麼
從新聞網站列表頁抓：
- 標題
- 網址
- 日期
- 來源 / 分類頁等欄位

### 腳本定位
`collect_news_titles.py` 現在是 **第一版 crawler skeleton**，適合先打通：
- session / retry
- HTML 解析流程
- CSV schema
- 分頁結構

但它仍需要：
- 指定真實新聞來源
- 改 selector
- 確認 pagination

### 建議輸出
建議把 raw 輸出放到：
- `data/raw/*.csv`

雖然目前腳本內建輸出位置邏輯仍偏簡化，但專題展示上應該以 `data/raw/` 為正式 raw pool。

### 這一步完成標準
- 至少成功抓到 1 個來源的小批資料
- CSV 欄位和 schema 對得上
- 可以重跑
- 原始資料保留，不要直接覆蓋成 clean data

### 對後續的交棒
Step 1 的輸出要交給清理腳本處理。

---

## Step 2：資料清理 Cleaning

### 主要腳本
- `code/clean_news_data.py`

### 這一步在做什麼
把 raw CSV 整理成可訓練資料，至少包含：
- 標題文字清理
- label 正規化
- 缺值過濾
- 重複標題去除

### 目前腳本特性
`clean_news_data.py` 已經具備：
- required fields 檢查
- title normalization
- label alias mapping
- duplicate title 移除
- clean CSV 輸出

### 目前要注意的欄位對齊問題
這支清理腳本預設需要欄位：
- `title`
- `label`

但蒐集腳本目前輸出 schema 比較像：
- `title`
- `section`
- `source_site`
- `article_url`
- `published_at_*`

也就是說，正式串接前要先確認下面其中一種做法：

1. 在蒐集階段就產出 `label` 欄位
2. 或在 raw -> clean 中間加入 label mapping / 欄位轉換
3. 或修改 `clean_news_data.py`，讓它支援 `section -> label`

### 建議輸出
- `data/processed/news_titles_clean.csv`

如果要保留中介證據，也建議另外存：
- `data/interim/merged_raw.csv`
- `data/interim/deduped.csv`
- `data/interim/labeled.csv`

### 這一步完成標準
- 有一份乾淨且欄位穩定的 CSV
- 至少要有文本欄位 + 類別欄位
- 去重與丟棄規則可以說清楚
- 能統計清理前後筆數變化

### 對後續的交棒
Step 2 的 clean dataset 直接交給訓練腳本。

---

## Step 3：Baseline 訓練 / 模型比較 Training

### 主要腳本
- `code/train_baseline.py`

### 這一步在做什麼
先做第一版可解釋、可展示的 baseline，比模型前先確認 pipeline 是通的。

### 目前腳本能力
`train_baseline.py` 已經可以：
- 載入 CSV
- 自動偵測 text column / label column
- train/test split
- 跑兩個 baseline：
  - TF-IDF(char n-gram) + MultinomialNB
  - TF-IDF(char n-gram) + LogisticRegression
- 輸出：
  - accuracy
  - macro F1
  - confusion matrix
  - metrics json/csv

### 目前預期輸入
它會優先找：
- text 欄位候選：`clean_text`, `text`, `title`, `content`
- label 欄位候選：`label`, `category`, `class`

所以最穩的做法是讓 clean dataset 至少含有：
- `title` 或 `clean_text`
- `label`

### 建議輸出
依腳本目前預設，會輸出到：
- `outputs/baseline/`

但專題整體展示上，建議後續整理 / 複製到：
- `results/metrics/`
- `results/tables/`

至少要保留：
- `metrics_summary.csv`
- 各模型 metrics json
- confusion matrix csv

### 這一步完成標準
- 能成功跑完 train/test
- 至少產生 1 份 metrics summary
- 至少產生 1 個 confusion matrix
- 可以回答 baseline 現在大概有沒有可分性

### 對後續的交棒
Step 3 的 metrics / confusion matrix 交給繪圖腳本。

---

## Step 4：圖表輸出 Plotting

### 主要腳本
- `code/plot_results.py`

### 補充腳本
- `code/explore_wordcloud.py`

### 這一步在做什麼
把資料與模型結果轉成評審看得懂的圖表。

### `plot_results.py` 目前定位
這支腳本可以畫三大核心圖：
- 類別分布圖
- 模型比較圖
- confusion matrix

### 它目前預設會找的資料
- dataset：`data/processed/news_titles_clean.csv`
- metrics：`results/metrics/model_metrics.csv` 或 `json`
- confusion matrix：`results/metrics/best_model_confusion_matrix.csv` 或 `json`

### 這裡要注意的對齊點
`train_baseline.py` 目前預設輸出在 `outputs/baseline/`，
但 `plot_results.py` 預設會去 `results/metrics/` 找資料。

所以目前主流程若要順跑，必須做其中一種：

1. 訓練後把輸出整理到 `results/metrics/`
2. 或執行 `plot_results.py` 時用參數手動指定 metrics 路徑
3. 或之後統一修改輸出資料夾規格

### 建議正式圖表輸出
- `results/figures/class_distribution.png`
- `results/figures/model_comparison.png`
- `results/figures/confusion_matrix.png`
- `results/figures/confusion_matrix_normalized.png`（可選）

### `explore_wordcloud.py` 的定位
這比較像：
- 額外補充圖
- 報告或附錄用探索分析

不是主線必要品，但如果做得好，可以作為加分材料。

### 這一步完成標準
- 至少 3 張核心圖出來
- 圖表能和論文 / 簡報內容對上
- 圖檔命名穩定、可重複輸出

### 對後續的交棒
Step 4 的圖表和結果表，交給評審展示包整理。

---

## Step 5：評審展示包 Judge package outputs

### 主要依據文件
- `judge_package_checklist.md`
- `demo_script.md`
- `experiment_matrix.md`
- `README_build_order.md`

### 配套圖與圖解
- `diagrams/workflow.mmd`
- `diagrams/data_pipeline.mmd`
- `diagrams/model_comparison.mmd`

### 這一步在做什麼
把前面各階段輸出，整理成評審看得懂、問得到、打得開的成品。

### 評審包至少要能展示
1. 研究題目與研究問題
2. 原始資料來源
3. schema / label mapping
4. 清理流程
5. baseline 與模型比較
6. confusion matrix 與指標表
7. 錯誤分析 / 補充觀察
8. 可重現的檔案結構

### 建議最終整理的輸出區
- `data/raw/`
- `data/processed/`
- `results/metrics/`
- `results/figures/`
- `results/tables/`
- `diagrams/`
- `paper/`（之後放論文 / 摘要 / 簡報）

### 這一步完成標準
- 評審問「資料怎麼來」時，打得開 raw CSV 和 crawler
- 問「怎麼清理」時，打得開 clean script 和 clean dataset
- 問「模型怎麼比」時，打得開 metrics summary 和 confusion matrix
- 問「你們流程是什麼」時，打得開 mermaid / 流程圖 / demo script

---

## 3. 一條線版本：現有腳本對應順序

最實際的一條線可以寫成：

1. 先確認規格  
   - `schemas/news_schema.md`  
   - `schemas/label_mapping.csv`  
   - `judge_package_checklist.md`

2. 跑資料蒐集  
   - `code/collect_news_titles.py`  
   - 必要時改用 `code/collect_news_titles_alt.py`

3. 跑資料清理  
   - `code/clean_news_data.py`

4. 跑 baseline 訓練  
   - `code/train_baseline.py`

5. 跑圖表輸出  
   - `code/plot_results.py`

6. 補充探索圖 / 附加展示素材  
   - `code/explore_wordcloud.py`

7. 整理評審展示包  
   - `judge_package_checklist.md`  
   - `demo_script.md`  
   - `diagrams/*.mmd`

---

## 4. 目前整合上的關鍵缺口

目前腳本已經有雛形，但要真正串成完整流水線，最需要注意的是下面 3 件事。

### 缺口 1：collection -> cleaning 欄位還沒完全對齊
蒐集腳本偏 raw crawler schema，清理腳本偏 `title + label` 格式。

**要補的事：**
- 明確把 `section/category_raw` 映射成 `label`
- 或在中間加一個 build-dataset / mapping 步驟

### 缺口 2：training output -> plotting input 路徑不完全一致
- `train_baseline.py` 預設輸出：`outputs/baseline/`
- `plot_results.py` 預設讀取：`results/metrics/`

**要補的事：**
- 統一路徑規格，或用 CLI 參數明確指定

### 缺口 3：judge-facing 中介證據還需要持續累積
現在有流程文件，但真正要讓評審信服，還需要逐步補齊：
- raw sample
- clean sample
- metrics summary
- confusion matrix
- 錯分案例
- 研究流程圖對應說明

---

## 5. 建議的正式輸出節點

如果之後要把整條流程固定下來，建議每一階段至少固定產出這些東西：

### Collection outputs
- `data/raw/source_xxx.csv`
- `results/logs/collection_log.md`

### Cleaning outputs
- `data/interim/*.csv`
- `data/processed/news_titles_clean.csv`
- `results/logs/cleaning_log.md`

### Training outputs
- `results/metrics/model_metrics.csv`
- `results/metrics/model_metrics.json`
- `results/metrics/best_model_confusion_matrix.csv`

### Plotting outputs
- `results/figures/class_distribution.png`
- `results/figures/model_comparison.png`
- `results/figures/confusion_matrix.png`

### Judge package outputs
- `paper/` 內論文與摘要
- `diagrams/*.mmd`
- `demo_script.md`
- `judge_package_checklist.md`

---

## 6. 一句話版

**目前現有腳本的正確主順序是：**

`collect_news_titles.py` -> `clean_news_data.py` -> `train_baseline.py` -> `plot_results.py` -> `judge_package_checklist.md` / `demo_script.md` 整理展示包

備用或補充：
- `collect_news_titles_alt.py`：蒐集替代版
- `explore_wordcloud.py`：額外視覺化加分材料
- `tokenizer_config.py`：分詞 / 文字設定輔助模組

這樣整理後，整個專題就能清楚對應到評審想看的流程：

**蒐集 -> 清理 -> 訓練 -> 視覺化 -> 展示證據**
