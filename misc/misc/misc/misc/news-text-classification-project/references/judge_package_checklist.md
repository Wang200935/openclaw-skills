# 評審展示包檢查清單

本文件的目的，是確保評審看到的不是只有「最後模型分數」，而是能完整看到整個研究流程：資料從哪裡來、怎麼整理、怎麼建模、怎麼評估、模型錯在哪裡、你們做了哪些反思。

本專題題目方向：**中文新聞標題分類研究**

---

## 一、評審應該看到的最終展示結構

評審面前應至少能清楚看到以下 8 個區塊：

1. **研究題目與研究問題**
2. **資料來源與蒐集方式**
3. **資料欄位與清理流程**
4. **類別設計與標註規則**
5. **模型比較流程**
6. **量化結果與圖表**
7. **錯誤分析與限制**
8. **可重現的檔案結構與執行流程**

如果缺任何一塊，評審就容易覺得：
- 你們只是把資料丟進模型
- 過程不透明
- 研究可重現性不足
- 沒有真正理解結果

---

## 二、評審展示包建議檔案樹

以下是建議最終交付樹狀結構。評審不一定逐檔開，但你們自己一定要整理成這樣，口頭報告與書面論文才會穩。

```text
paper_project/
  README_build_order.md
  judge_package_checklist.md

  paper/
    final_paper.pdf
    final_paper.docx
    abstract_zh.md
    presentation_outline.md

  data/
    raw/
      README_raw_sources.md
      source_01_*.csv
      source_02_*.csv
    interim/
      merged_raw.csv
      deduped.csv
      labeled.csv
    processed/
      news_titles_clean.csv
      label_mapping.csv
      dataset_summary.csv
      manual_audit_sample.csv

  src/
    collect/
      crawl_site_01.py
      crawl_site_02.py
      run_collection.py
    clean/
      merge_raw.py
      deduplicate.py
      normalize_labels.py
      filter_titles.py
      export_clean_csv.py
    train/
      train_baseline.py
      train_compare_models.py
      evaluate_models.py
      error_analysis.py
    viz/
      make_dataset_figures.py
      make_model_figures.py
    utils/
      config.py
      io_utils.py
      paths.py

  configs/
    sources.json
    label_rules.csv
    experiment_plan.md

  results/
    tables/
      model_comparison.csv
      class_metrics.csv
      error_cases.csv
    figures/
      fig_dataset_distribution.png
      fig_pipeline_overview.png
      fig_model_comparison.png
      fig_confusion_matrix_best.png
      fig_top_features.png
    logs/
      collection_log.md
      cleaning_log.md
      training_log.md

  diagrams/
    research_flow.md
    data_pipeline.md
    model_pipeline.md
    mermaid/
      research_flow.mmd
      data_pipeline.mmd
      model_pipeline.mmd

  appendix/
    category_definition_table.md
    field_definition_table.md
    methodology_notes.md
    judge_demo_script.md
```

---

## 三、評審必看成果：每一項要讓他們看到什麼

下面這份是最重要的 judge-facing checklist。不是只有「檔案存在」就算完成，而是每個項目都要有**明確可展示輸出**。

### 1. 研究題目與研究問題

**評審應看到的輸出：**
- 題目：`中文新聞標題分類研究`
- 研究目的 3 到 6 點
- 研究問題 4 到 6 題
- 為什麼只做「標題」而不做全文的理由

**最低標準：**
- 能用 1 頁簡報或論文緒論清楚說明
- 研究問題必須和後面實驗結果一一對應

**建議檔案：**
- `paper/presentation_outline.md`
- `paper/abstract_zh.md`
- `paper/final_paper.pdf`

---

### 2. 資料來源與蒐集方式

**評審應看到的輸出：**
- 來源網站清單
- 每個來源抓哪個分類頁
- 為何選這些網站
- 蒐集欄位有哪些
- 是用程式蒐集，不是手動貼資料

**評審應看見的明確證據：**
- 原始 CSV 檔
- 爬蟲程式碼
- 蒐集紀錄 log
- 來源設定檔

**最低標準：**
- 至少 2 個來源網站
- 至少能展示 1 支實際可執行 crawler
- 能說明只抓標題、日期、分類、網址，不抓全文

**建議檔案：**
- `data/raw/README_raw_sources.md`
- `src/collect/*.py`
- `configs/sources.json`
- `results/logs/collection_log.md`

---

### 3. 資料欄位與資料表設計

**評審應看到的輸出：**
- 原始資料欄位表
- 清理後資料欄位表
- 每個欄位的定義

**原始資料至少應包含：**
- `id`
- `title`
- `category_raw`
- `category_final`
- `source_site`
- `publish_date`
- `url`
- `crawl_date`

**清理後資料至少應包含：**
- `id`
- `title`
- `category_final`
- `source_site`
- `publish_date`
- `url`

**評審應看見的明確證據：**
- `news_titles_clean.csv`
- `label_mapping.csv`
- 欄位定義表

**建議檔案：**
- `data/processed/news_titles_clean.csv`
- `data/processed/label_mapping.csv`
- `appendix/field_definition_table.md`

---

### 4. 類別設計與標註規則

**評審應看到的輸出：**
- 最終類別數
- 每一類的定義
- 邊界案例如何處理
- 原網站分類如何映射到最終類別

**建議第一版固定 4 類：**
- 政治
- 社會
- 國際
- 生活

**評審應看見的明確證據：**
- 類別定義表
- 映射表
- 抽樣人工檢查結果

**最低標準：**
- 有一份清楚的 `label_mapping.csv`
- 有一份類別定義表
- 每類至少抽樣檢查 30 筆左右

**建議檔案：**
- `appendix/category_definition_table.md`
- `data/processed/label_mapping.csv`
- `data/processed/manual_audit_sample.csv`

---

### 5. 資料清理與前處理流程

**評審應看到的輸出：**
- 合併 raw data 的流程
- 去重規則
- 異常資料刪除規則
- 類別標準化規則
- 最終 clean dataset 產出流程

**評審應看見的明確證據：**
- 合併前後筆數變化
- 去重前後筆數變化
- 清理規則說明
- 對應程式碼

**最低標準：**
- 能用流程圖說明資料怎麼從 raw 變成 processed
- 能列出至少 3 種刪除或過濾規則

**建議檔案：**
- `src/clean/*.py`
- `results/logs/cleaning_log.md`
- `diagrams/data_pipeline.md`
- `results/figures/fig_pipeline_overview.png`

---

### 6. 模型比較設計

**評審應看到的輸出：**
- 不是只跑一個模型
- 有 baseline
- 有特徵方法比較
- 有公平比較條件

**建議至少比較以下組合：**
- CountVectorizer + Multinomial Naive Bayes
- TF-IDF + Multinomial Naive Bayes
- TF-IDF + Logistic Regression
- TF-IDF + Linear SVM

**可再加分：**
- unigram vs unigram+bigram
- 是否斷詞的比較

**評審應看見的明確證據：**
- 實驗設計表
- 模型訓練程式
- 模型比較結果表

**建議檔案：**
- `configs/experiment_plan.md`
- `src/train/train_baseline.py`
- `src/train/train_compare_models.py`
- `results/tables/model_comparison.csv`

---

### 7. 評估指標與結果圖表

**評審應看到的輸出：**
- Accuracy
- Precision
- Recall
- Macro F1
- Confusion Matrix

**重點：**
評審要看到你們知道不能只看 Accuracy，因為新聞類別可能不平均，**Macro F1 是核心亮點之一**。

**至少要有的圖表：**
1. 類別分布圖
2. 模型比較圖
3. 最佳模型混淆矩陣

**建議再補：**
4. top features 圖
5. 清理前後筆數變化圖

**評審應看見的明確證據：**
- 指標表格
- 圖像檔
- 圖說文字

**建議檔案：**
- `results/tables/model_comparison.csv`
- `results/tables/class_metrics.csv`
- `results/figures/fig_dataset_distribution.png`
- `results/figures/fig_model_comparison.png`
- `results/figures/fig_confusion_matrix_best.png`
- `results/figures/fig_top_features.png`

---

### 8. 錯誤分析

**評審應看到的輸出：**
- 至少 5 到 10 則錯分案例
- 每則案例要寫：標題、真實類別、預測類別、誤判原因
- 要指出哪些類別最容易混淆

**評審想看的不是只有「模型會錯」，而是：**
- 為什麼錯
- 是標題太短、類別重疊、專有名詞問題，還是斷詞失敗
- 後續如何改進

**建議檔案：**
- `results/tables/error_cases.csv`
- `src/train/error_analysis.py`
- `paper/final_paper.pdf`

---

### 9. 研究限制與反思

**評審應看到的輸出：**
- 只用標題，沒有全文上下文
- 不同新聞網站分類標準不同
- 某些新聞天然跨類別
- 中文斷詞可能切錯
- 沒有納入大型深度學習模型

**最低標準：**
- 不能把限制寫成藉口
- 要寫成「誠實說明 + 後續改進方向」

**建議檔案：**
- `paper/final_paper.pdf`
- `appendix/methodology_notes.md`

---

### 10. 流程圖與口頭報告展示材料

**評審應看到的輸出：**
- 研究總流程圖
- 資料處理流程圖
- 模型訓練比較流程圖

**最低標準：**
- 至少 3 張流程圖
- 流程圖上的用詞要統一

**建議檔案：**
- `diagrams/research_flow.md`
- `diagrams/data_pipeline.md`
- `diagrams/model_pipeline.md`
- `results/figures/fig_pipeline_overview.png`
- `appendix/judge_demo_script.md`

---

## 四、評審展示時的「必出畫面」

下面是你們在簡報、口頭報告、檔案展示時，評審最好一定能看到的具體畫面。

### 必出畫面 1：研究流程總覽
評審要看到：
- 類別設計
- 資料蒐集
- 清理
- 特徵轉換
- 模型訓練
- 評估
- 錯誤分析

### 必出畫面 2：原始資料到乾淨資料的轉換
評審要看到：
- raw CSV 長什麼樣
- 去重與過濾後剩多少筆
- clean CSV 長什麼樣

### 必出畫面 3：類別分布圖
評審要看到：
- 每個類別各有多少資料
- 是否平衡

### 必出畫面 4：模型比較表
評審要看到：
- 至少 4 組方法
- 各自 Accuracy / Macro F1
- 哪一組最好

### 必出畫面 5：最佳模型混淆矩陣
評審要看到：
- 哪一類最容易分類
- 哪一類最容易混淆

### 必出畫面 6：錯誤案例分析表
評審要看到：
- 模型不是神
- 你們知道它錯在哪

### 必出畫面 7：可重現的檔案樹與程式碼
評審要看到：
- 你們真的做了資料蒐集與建模程式
- 不是只做成一份報告

---

## 五、最低完成標準 vs 加分標準

### 最低完成標準
如果時間很緊，至少要做到：
- 1 份 final paper
- 1 份 clean dataset
- 1 份 label mapping
- 2 個以上來源
- 4 組模型比較
- 3 張關鍵圖表
- 1 張 confusion matrix
- 5 則以上錯誤案例
- 3 張流程圖

### 加分標準
如果要讓評審更有感，可再補：
- unigram / bigram 比較
- 斷詞策略比較
- top features 視覺化
- 手動抽樣標註檢查表
- 研究展示腳本
- 可直接重跑的 `run_collection.py` 與 `train_compare_models.py`

---

## 六、交件前最後總檢查

交件或報告前，逐條確認：

- [ ] 題目、研究目的、研究問題已定稿
- [ ] 資料來源與蒐集方式能清楚說明
- [ ] raw / processed 資料已分開保存
- [ ] clean dataset 已產出
- [ ] label mapping 已完成
- [ ] 類別定義表已完成
- [ ] 清理流程與規則已寫清楚
- [ ] 至少完成 4 組模型比較
- [ ] 已產出 Accuracy / Precision / Recall / Macro F1
- [ ] 已產出最佳模型 confusion matrix
- [ ] 已完成至少 3 張關鍵圖表
- [ ] 已整理至少 5 則錯誤案例
- [ ] 已寫研究限制與改進方向
- [ ] 已整理完整檔案樹
- [ ] 已準備口頭報告時要展示的必出畫面

---

## 七、這份清單的核心判準

如果評審看完你們的內容後，能很自然回答下面這些問題，代表展示包是合格的：

- 你們的資料從哪裡來？
- 你們怎麼把不同網站的分類統整起來？
- 你們怎麼清理資料？
- 你們比較了哪些模型？
- 你們用什麼指標判斷模型好壞？
- 哪些類別最容易混淆？
- 你們知道模型為什麼會錯嗎？
- 如果下次重做，會怎麼改進？

如果這 8 題都能回答，評審通常就會覺得這不是只會套模型，而是一個完整、成熟、可展示的資訊專題。
