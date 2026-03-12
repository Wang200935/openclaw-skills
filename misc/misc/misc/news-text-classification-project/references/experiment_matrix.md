# Baseline Experiment Matrix

本文件用來定義第一批要先執行的比較實驗。
目標不是一開始追求最高分，而是先用可解釋、可重跑、可展示給評審的方式，建立 baseline 比較結果。

## 1. 第一批比較軸

### 特徵比較
- TF-IDF unigram (`ngram_range=(1,1)`)
- TF-IDF unigram+bigram (`ngram_range=(1,2)`)

### 分類器比較
- Multinomial Naive Bayes
- Logistic Regression

## 2. 建議先跑的 4 個 baseline 組合

| Run ID | Vectorizer | N-gram | Classifier | Purpose |
|---|---|---|---|---|
| EXP-01 | TF-IDF | unigram | Naive Bayes | 最基礎文字分類 baseline |
| EXP-02 | TF-IDF | unigram+bigram | Naive Bayes | 檢查加入 bigram 是否幫助 NB |
| EXP-03 | TF-IDF | unigram | Logistic Regression | 與 NB 比較線性分類器表現 |
| EXP-04 | TF-IDF | unigram+bigram | Logistic Regression | 檢查最佳化空間，作為第一輪較強 baseline |

## 3. 每個實驗預期要輸出的結果

每次 run 都應至少輸出以下內容，方便後續寫論文、做圖表、給評審看流程。

### 核心指標
- Accuracy
- Macro F1
- Precision / Recall（至少保留 macro average）
- 每類別 support

### 模型比較資料
- 各 run 的總表
- 每個 run 的 classification report
- 每個 run 的 confusion matrix
- 每個 run 的錯分案例

### 可展示證據
- 使用的資料集版本
- train / validation / test 切分設定
- 類別標籤清單
- 向量化設定與模型參數

## 4. 建議檔名規則

以下檔名規則先固定，之後做表格、圖表、附錄會比較整齊。

### 總表
- `results/tables/baseline_metrics_summary.csv`
  - 內容：4 個 baseline run 的 Accuracy、Macro F1、主要參數、備註

### 各 run 指標
- `results/logs/EXP-01_metrics.json`
- `results/logs/EXP-02_metrics.json`
- `results/logs/EXP-03_metrics.json`
- `results/logs/EXP-04_metrics.json`

### 各 run 分類報告
- `results/tables/EXP-01_classification_report.csv`
- `results/tables/EXP-02_classification_report.csv`
- `results/tables/EXP-03_classification_report.csv`
- `results/tables/EXP-04_classification_report.csv`

### 各 run 混淆矩陣
- `results/figures/EXP-01_confusion_matrix.png`
- `results/figures/EXP-02_confusion_matrix.png`
- `results/figures/EXP-03_confusion_matrix.png`
- `results/figures/EXP-04_confusion_matrix.png`

### 各 run 錯分案例
- `results/tables/EXP-01_error_cases.csv`
- `results/tables/EXP-02_error_cases.csv`
- `results/tables/EXP-03_error_cases.csv`
- `results/tables/EXP-04_error_cases.csv`

### 實驗設定快照
- `results/logs/EXP-01_config.json`
- `results/logs/EXP-02_config.json`
- `results/logs/EXP-03_config.json`
- `results/logs/EXP-04_config.json`

## 5. 建議 summary 表欄位

`baseline_metrics_summary.csv` 建議至少包含：

- `run_id`
- `vectorizer`
- `ngram_range`
- `classifier`
- `dataset_version`
- `accuracy`
- `macro_f1`
- `macro_precision`
- `macro_recall`
- `notes`

## 6. 第一輪比較想回答的問題

這 4 個 baseline 跑完後，至少可以回答下面幾個問題：

1. 在新聞標題分類上，TF-IDF 加入 bigram 是否比 unigram 更好？
2. 在同樣 TF-IDF 特徵下，Naive Bayes 和 Logistic Regression 哪個表現較好？
3. 哪個組合適合作為後續論文中的「baseline representative model」？
4. 哪些類別最容易混淆，適合進入第二輪錯誤分析？

## 7. 建議執行順序

為了快速拿到第一批結果，建議順序如下：

1. `EXP-01`：TF-IDF unigram + Naive Bayes
2. `EXP-03`：TF-IDF unigram + Logistic Regression
3. `EXP-02`：TF-IDF unigram+bigram + Naive Bayes
4. `EXP-04`：TF-IDF unigram+bigram + Logistic Regression

這樣可以先完成「同樣 unigram 下 NB vs LR」的第一層比較，再補上 bigram 的影響。

## 8. 後續可擴充方向

等第一輪完成後，再考慮第二輪擴充：
- CountVectorizer vs TF-IDF
- Logistic Regression vs Linear SVM
- 不同 `min_df` / `max_df` 參數
- class imbalance 處理
- 更完整的錯誤分析與代表案例整理
