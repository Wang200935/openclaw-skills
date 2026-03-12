# 輸出檔案命名規範

本文件用來統一 `paper_project/` 內各類輸出檔案的命名方式，避免後續出現：
- 同一種成果每個人命名不同
- 看不出檔案是 raw、clean 還是 metrics
- 不知道某張圖屬於哪個實驗 run
- 圖表、JSON、CSV、log、流程圖彼此對不起來

這份規範的目標很簡單：

**看到檔名，就知道它是什麼、來自哪一階段、對應哪個資料版本或實驗 run。**

---

## 一、總原則

所有輸出檔名都盡量遵守以下原則：

1. **全部使用小寫英文字母**
2. **單字之間用底線 `_` 連接**
3. **不要用空白、中文、括號、全形符號**
4. **同一類檔案固定欄位順序**，不要今天 `run_id` 放前面、明天放後面
5. **有版本就寫版本，有日期就寫日期，有 run_id 就寫 run_id**
6. **中間產物與最終產物分開命名**，不要混在一起
7. **圖檔、表格、JSON、log 要能互相對應**

---

## 二、建議命名骨架

依輸出類型不同，採用下列骨架。

### 1. 資料檔

```text
{stage}_{subject}_{source_or_scope}_{version_or_date}.{ext}
```

### 2. 實驗輸出檔

```text
{run_id}_{artifact}_{dataset_version}.{ext}
```

### 3. 通用彙總檔

```text
{subject}_{artifact}_summary.{ext}
```

### 4. 圖表檔

```text
fig_{subject}_{detail}_{version_or_run_id}.{ext}
```

### 5. 日誌檔

```text
{stage}_{artifact}_log_{date_or_run_id}.{ext}
```

### 6. 流程圖 / 結構圖

```text
{subject}_{diagram_type}.{ext}
```

---

## 三、固定欄位與常用代碼

為了讓命名一致，下面幾個欄位請固定使用。

### 1. stage（階段）
- `raw`：原始蒐集資料
- `interim`：中介清理資料
- `processed`：最終可建模資料
- `results`：模型與評估結果
- `fig`：圖表輸出
- `log`：紀錄檔
- `diagram`：流程圖或架構圖

### 2. subject（主題）
- `news_titles`：新聞標題主資料集
- `label_mapping`：標籤映射表
- `dataset`：資料集摘要或總覽
- `baseline`：baseline 實驗集合
- `model_comparison`：模型比較
- `class_metrics`：各類別指標
- `confusion_matrix`：混淆矩陣
- `error_cases`：錯分案例
- `pipeline`：資料流程
- `workflow`：研究流程

### 3. source_or_scope（來源或範圍）
- 單一來源網站：用固定短碼，例如 `cna`、`pts`、`setn`
- 多來源整併：用 `all_sources`
- 單一類別：可用 `politics`、`society`、`international`、`lifestyle`
- 全部類別：用 `all_classes`

### 4. version_or_date（版本或日期）
二選一或兩者並用：
- 版本：`v1`、`v2`、`v3`
- 日期：`20260310`
- 若同時需要，建議：`v1_20260310`

### 5. run_id（實驗編號）
固定使用：
- `exp_01`
- `exp_02`
- `exp_03`
- `exp_04`

不要混用 `EXP-01`、`exp01`、`run1`、`baseline_a`。

**本專案正式檔名一律建議使用：`exp_01` 這種格式。**

---

## 四、資料輸出命名規則

## 4.1 Raw CSV

### 規則

```text
raw_news_titles_{source}_{date}.csv
```

### 用途
原始蒐集檔，保留網站抓下來的標題、原分類、日期、網址等欄位。

### 範例
- `raw_news_titles_cna_20260310.csv`
- `raw_news_titles_pts_20260310.csv`
- `raw_news_titles_setn_20260310.csv`

### 補充規則
1. 一個來源一天一個主檔，最清楚
2. 如果同一天分批抓，可加批次碼：
   - `raw_news_titles_cna_20260310_batch01.csv`
   - `raw_news_titles_cna_20260310_batch02.csv`
3. 不要命名成：
   - `cna_news.csv`
   - `新聞資料最新版.csv`
   - `raw_final_v2.csv`

---

## 4.2 Clean / Interim CSV

中介資料與最終 clean 資料要分開。

### A. 中介資料

```text
interim_news_titles_{step}_{version}.csv
```

### 建議 step 名稱
- `merged`
- `deduped`
- `labeled`
- `filtered`
- `audited`

### 範例
- `interim_news_titles_merged_v1.csv`
- `interim_news_titles_deduped_v1.csv`
- `interim_news_titles_labeled_v1.csv`
- `interim_news_titles_filtered_v1.csv`

### B. 最終 clean 資料

```text
processed_news_titles_clean_{version}.csv
```

### 範例
- `processed_news_titles_clean_v1.csv`
- `processed_news_titles_clean_v2.csv`

### 建議搭配檔
- `processed_dataset_summary_v1.csv`
- `processed_manual_audit_sample_v1.csv`

---

## 4.3 Label mapping / schema 類資料

### Label mapping CSV

```text
processed_label_mapping_{version}.csv
```

範例：
- `processed_label_mapping_v1.csv`

### Dataset summary CSV

```text
processed_dataset_summary_{version}.csv
```

範例：
- `processed_dataset_summary_v1.csv`

### 欄位或 schema 文件

```text
news_schema.md
```

或如果之後需要版本化：

```text
news_schema_v1.md
```

如果 schema 已穩定、不常變動，保留 `news_schema.md` 即可。

---

## 五、Metrics 輸出命名規則

Metrics 分成兩層：
1. **單一 run 的細節輸出**
2. **全部 run 的總表輸出**

---

## 5.1 單一 run 的 metrics JSON

### 規則

```text
{run_id}_metrics_{dataset_version}.json
```

### 範例
- `exp_01_metrics_v1.json`
- `exp_02_metrics_v1.json`
- `exp_03_metrics_v1.json`

### 用途
保存單次實驗的整體指標，例如：
- accuracy
- macro_f1
- macro_precision
- macro_recall
- support
- train/test size
- vectorizer setting
- model parameter

---

## 5.2 單一 run 的 classification report CSV

### 規則

```text
{run_id}_class_metrics_{dataset_version}.csv
```

### 範例
- `exp_01_class_metrics_v1.csv`
- `exp_02_class_metrics_v1.csv`

### 用途
保存每個類別的 precision / recall / f1-score / support。

---

## 5.3 全部 run 的 metrics summary CSV

### 規則

```text
baseline_metrics_summary_{dataset_version}.csv
```

或如果不是 baseline，而是更廣泛比較：

```text
model_comparison_summary_{dataset_version}.csv
```

### 範例
- `baseline_metrics_summary_v1.csv`
- `model_comparison_summary_v2.csv`

### 建議
如果目前主要是 baseline 第一輪比較，優先用：
- `baseline_metrics_summary_v1.csv`

如果後面進入正式比較與擴充實驗，再用：
- `model_comparison_summary_v2.csv`

---

## 5.4 配置快照 JSON

### 規則

```text
{run_id}_config_{dataset_version}.json
```

### 範例
- `exp_01_config_v1.json`
- `exp_04_config_v1.json`

### 用途
保存該 run 的：
- vectorizer
- ngram_range
- classifier
- random_state
- split ratio
- preprocessing option

---

## 六、Confusion Matrix 命名規則

混淆矩陣至少要能分辨：
- 屬於哪個 run
- 對應哪個資料版本
- 是圖檔還是表格

## 6.1 圖檔版

### 規則

```text
fig_confusion_matrix_{run_id}_{dataset_version}.png
```

### 範例
- `fig_confusion_matrix_exp_01_v1.png`
- `fig_confusion_matrix_exp_04_v1.png`

## 6.2 CSV 表格版（可選）

### 規則

```text
{run_id}_confusion_matrix_{dataset_version}.csv
```

### 範例
- `exp_01_confusion_matrix_v1.csv`
- `exp_04_confusion_matrix_v1.csv`

## 6.3 最佳模型專用檔

如果要做論文或簡報固定引用的最佳模型圖，可額外保留一份別名：

```text
fig_confusion_matrix_best_v1.png
```

注意：
- `best` 是展示用途別名
- 真正可追溯的主檔仍應保留 `run_id`

也就是說，最好同時保留：
- `fig_confusion_matrix_exp_04_v1.png`
- `fig_confusion_matrix_best_v1.png`

---

## 七、Plots / 圖表命名規則

所有圖表統一以 `fig_` 開頭。

### 規則

```text
fig_{subject}_{detail}_{version_or_run_id}.png
```

如果同時需要 run_id 與版本：

```text
fig_{subject}_{detail}_{run_id}_{dataset_version}.png
```

---

## 7.1 資料分布圖

### 範例
- `fig_dataset_class_distribution_v1.png`
- `fig_dataset_source_distribution_v1.png`
- `fig_dataset_cleaning_counts_v1.png`

---

## 7.2 模型比較圖

### 範例
- `fig_model_comparison_accuracy_v1.png`
- `fig_model_comparison_macro_f1_v1.png`
- `fig_model_comparison_overview_v1.png`

---

## 7.3 特徵或解釋型圖表

### 範例
- `fig_top_features_exp_04_v1.png`
- `fig_error_case_examples_exp_04_v1.png`
- `fig_token_length_distribution_v1.png`

---

## 7.4 流程概觀圖（若輸出成圖片）

### 範例
- `fig_pipeline_overview_v1.png`
- `fig_workflow_research_overview_v1.png`

---

## 八、Logs 命名規則

Logs 重點是看得出它記錄哪一階段、哪一天，必要時看得出對應哪個 run。

## 8.1 資料蒐集 log

### 規則

```text
collection_log_{date}.md
```

### 範例
- `collection_log_20260310.md`
- `collection_log_20260311.md`

如果想維持單一滾動文件，也可以保留：
- `collection_log.md`

但如果過程會很多，**我比較建議逐日版本化**。

---

## 8.2 清理流程 log

### 規則

```text
cleaning_log_{date}.md
```

### 範例
- `cleaning_log_20260310.md`

若是由程式輸出的機器 log，也可使用：

```text
cleaning_log_{dataset_version}.txt
```

例如：
- `cleaning_log_v1.txt`

---

## 8.3 訓練 log

### 規則

```text
training_log_{run_id}_{dataset_version}.txt
```

### 範例
- `training_log_exp_01_v1.txt`
- `training_log_exp_04_v1.txt`

### 補充
如果是一輪多個 run 的總 log，也可以用：
- `training_log_baseline_v1.txt`

---

## 8.4 錯誤 / 例外 log

### 規則

```text
error_log_{stage}_{date}.txt
```

### 範例
- `error_log_collection_20260310.txt`
- `error_log_training_20260310.txt`

---

## 九、Diagrams 命名規則

流程圖、架構圖、比較圖的源文件命名要簡單穩定，不要加太多噪音。

## 9.1 Mermaid 原始檔

### 規則

```text
{subject}_{diagram_type}.mmd
```

### 範例
- `workflow_overview.mmd`
- `data_pipeline.mmd`
- `model_comparison.mmd`
- `research_flow.mmd`

如果要更貼近目前專案內容，也可使用：
- `workflow.mmd`
- `data_pipeline.mmd`
- `model_comparison.mmd`

目前 `paper_project/diagrams/` 既有檔名已算合理，可延續使用。

---

## 9.2 圖說或說明文件

### 規則

```text
{subject}_{diagram_type}.md
```

### 範例
- `research_flow.md`
- `data_pipeline.md`
- `model_pipeline.md`

---

## 9.3 匯出的圖像檔

### 規則

```text
fig_{subject}_{diagram_type}_{version}.png
```

### 範例
- `fig_research_flow_v1.png`
- `fig_data_pipeline_v1.png`
- `fig_model_pipeline_v1.png`

---

## 十、推薦的資料夾對應

為了讓命名和目錄一致，建議如下放置：

### data/raw/
- `raw_news_titles_cna_20260310.csv`
- `raw_news_titles_pts_20260310.csv`

### data/interim/
- `interim_news_titles_merged_v1.csv`
- `interim_news_titles_deduped_v1.csv`
- `interim_news_titles_labeled_v1.csv`

### data/processed/
- `processed_news_titles_clean_v1.csv`
- `processed_label_mapping_v1.csv`
- `processed_dataset_summary_v1.csv`
- `processed_manual_audit_sample_v1.csv`

### results/tables/
- `baseline_metrics_summary_v1.csv`
- `model_comparison_summary_v1.csv`
- `exp_01_class_metrics_v1.csv`
- `exp_01_confusion_matrix_v1.csv`
- `exp_01_error_cases_v1.csv`

### results/figures/
- `fig_confusion_matrix_exp_01_v1.png`
- `fig_model_comparison_macro_f1_v1.png`
- `fig_dataset_class_distribution_v1.png`
- `fig_top_features_exp_04_v1.png`

### results/logs/
- `collection_log_20260310.md`
- `cleaning_log_20260310.md`
- `training_log_exp_01_v1.txt`
- `exp_01_metrics_v1.json`
- `exp_01_config_v1.json`

### diagrams/
- `workflow.mmd`
- `data_pipeline.mmd`
- `model_comparison.mmd`
- `research_flow.md`
- `data_pipeline.md`
- `model_pipeline.md`

---

## 十一、推薦的最小一致集合

如果現在不想一次搞太複雜，至少先把下面這批命名固定住。

## 11.1 資料層
- `raw_news_titles_{source}_{date}.csv`
- `interim_news_titles_merged_v1.csv`
- `interim_news_titles_deduped_v1.csv`
- `processed_news_titles_clean_v1.csv`
- `processed_label_mapping_v1.csv`

## 11.2 實驗層
- `exp_01_metrics_v1.json`
- `exp_01_class_metrics_v1.csv`
- `exp_01_confusion_matrix_v1.csv`
- `exp_01_error_cases_v1.csv`
- `exp_01_config_v1.json`

## 11.3 圖表層
- `fig_confusion_matrix_exp_01_v1.png`
- `fig_model_comparison_macro_f1_v1.png`
- `fig_dataset_class_distribution_v1.png`

## 11.4 日誌層
- `collection_log_20260310.md`
- `cleaning_log_20260310.md`
- `training_log_exp_01_v1.txt`

## 11.5 圖解層
- `workflow.mmd`
- `data_pipeline.mmd`
- `model_comparison.mmd`

---

## 十二、不建議的命名方式

下面這些命名方式要避免：

### 問題 1：語意不清
- `final.csv`
- `new_data.csv`
- `result2.csv`
- `latest_metrics.json`

### 問題 2：版本混亂
- `exp1.json`
- `EXP-1.json`
- `run01_result.csv`
- `lr_bigram_new_final.csv`

### 問題 3：圖檔對不上實驗
- `confusion_matrix.png`
- `comparison.png`
- `plot_final_final.png`

### 問題 4：同一專案混用不同格式
- 一部分用 `exp_01`
- 一部分用 `EXP-01`
- 一部分用 `run1`

這會讓後續論文附錄、圖表引用、程式自動讀檔都變麻煩。

---

## 十三、最終建議：本專案直接採用的標準

如果要一句話定版，我建議本專案直接採用下面這組標準：

### 資料
- `raw_news_titles_{source}_{date}.csv`
- `interim_news_titles_{step}_{version}.csv`
- `processed_news_titles_clean_{version}.csv`
- `processed_label_mapping_{version}.csv`

### 指標
- `{run_id}_metrics_{dataset_version}.json`
- `{run_id}_class_metrics_{dataset_version}.csv`
- `baseline_metrics_summary_{dataset_version}.csv`

### 混淆矩陣
- `{run_id}_confusion_matrix_{dataset_version}.csv`
- `fig_confusion_matrix_{run_id}_{dataset_version}.png`

### 圖表
- `fig_{subject}_{detail}_{version_or_run_id}.png`

### 日誌
- `collection_log_{date}.md`
- `cleaning_log_{date}.md`
- `training_log_{run_id}_{dataset_version}.txt`

### 圖解
- `{subject}_{diagram_type}.mmd`
- `{subject}_{diagram_type}.md`

---

## 十四、附：快速對照表

| 類型 | 規則 | 範例 |
|---|---|---|
| Raw CSV | `raw_news_titles_{source}_{date}.csv` | `raw_news_titles_cna_20260310.csv` |
| Interim CSV | `interim_news_titles_{step}_{version}.csv` | `interim_news_titles_deduped_v1.csv` |
| Clean CSV | `processed_news_titles_clean_{version}.csv` | `processed_news_titles_clean_v1.csv` |
| Label mapping | `processed_label_mapping_{version}.csv` | `processed_label_mapping_v1.csv` |
| Metrics JSON | `{run_id}_metrics_{dataset_version}.json` | `exp_01_metrics_v1.json` |
| Metrics CSV | `{run_id}_class_metrics_{dataset_version}.csv` | `exp_01_class_metrics_v1.csv` |
| Summary CSV | `baseline_metrics_summary_{dataset_version}.csv` | `baseline_metrics_summary_v1.csv` |
| Confusion CSV | `{run_id}_confusion_matrix_{dataset_version}.csv` | `exp_01_confusion_matrix_v1.csv` |
| Confusion plot | `fig_confusion_matrix_{run_id}_{dataset_version}.png` | `fig_confusion_matrix_exp_01_v1.png` |
| Plot | `fig_{subject}_{detail}_{version_or_run_id}.png` | `fig_model_comparison_macro_f1_v1.png` |
| Log | `{stage}_log_{date}.md` | `collection_log_20260310.md` |
| Training log | `training_log_{run_id}_{dataset_version}.txt` | `training_log_exp_01_v1.txt` |
| Diagram | `{subject}_{diagram_type}.mmd` | `data_pipeline.mmd` |

---

## 十五、執行建議

接下來如果要把這份規範真正用起來，建議這樣做：

1. 先把 `run_id` 格式正式統一為 `exp_01`、`exp_02` 這種形式
2. 新產出的 CSV / JSON / PNG 全部依這份規範命名
3. 若現有程式會自動輸出檔案，之後在訓練腳本與繪圖腳本中直接把這套規則寫死
4. 論文、簡報、附錄引用圖表時，也優先引用這些正式檔名

這樣後面做評審展示、整理附錄、重跑實驗、交叉核對結果時，會省很多麻煩。