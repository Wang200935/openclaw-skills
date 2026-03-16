# 紙本專題建置順序說明

這份 README 是給學生團隊內部用的執行順序表。

目標不是一開始就把所有東西做滿，而是照正確順序做，避免最常見的三種問題：
- 類別還沒定就先亂抓資料
- 資料還沒清乾淨就急著跑模型
- 模型有分數了，卻沒有過程證據可以給評審看

主題方向：**中文新聞標題分類研究**

---

## 一、總原則

整個專題請照這個原則走：

1. **先定研究問題，再定類別**
2. **先做資料流程，再做模型比較**
3. **先做 baseline，再做加強版**
4. **每完成一階段，就同步產出可展示證據**
5. **評審看的不是只有結果，而是完整過程**

一句話版本：

**不要先追最高分，先把完整研究流程做出來。**

---

## 二、建議整體執行順序

建議照下面 10 個階段執行。

1. 題目定稿
2. 類別與資料欄位定稿
3. 資料來源與 mapping 規則建立
4. 單站 crawler 完成
5. 多站資料蒐集完成
6. 資料清理與 clean dataset 完成
7. baseline 模型完成
8. 模型比較與評估完成
9. 圖表、流程圖、錯誤分析完成
10. 論文、簡報、評審展示包完成

---

## 三、分階段建置順序

下面是最實際的執行版本。每個階段都列出：
- 要做什麼
- 產出什麼
- 完成判準是什麼

---

## Phase 0：建立專案骨架

### 目標
先把資料夾架好，之後每個人做的東西才不會亂放。

### 要做的事
建立以下目錄：

```text
paper_project/
  paper/
  data/raw/
  data/interim/
  data/processed/
  src/collect/
  src/clean/
  src/train/
  src/viz/
  src/utils/
  configs/
  results/tables/
  results/figures/
  results/logs/
  diagrams/
  appendix/
```

### 這階段輸出
- 專案資料夾結構
- 路徑命名規則

### 完成判準
- 所有人知道檔案要放哪裡
- 不會再出現「圖表在某人桌面、資料在另一個資料夾」這種狀況

---

## Phase 1：題目、研究目的、研究問題定稿

### 目標
先把研究主軸鎖住，避免後面一直改題目。

### 建議題目
- `中文新聞標題分類研究`

### 要做的事
1. 寫出研究背景
2. 寫出研究動機
3. 寫出研究目的 3 到 6 點
4. 寫出研究問題 4 到 6 題
5. 決定為什麼研究對象是「標題」不是「全文」

### 這階段輸出
- 題目定稿
- 研究目的清單
- 研究問題清單
- 口頭報告開場稿草稿

### 完成判準
- 團隊每個人都能用 1 分鐘講清楚：你們到底在研究什麼
- 後續每個實驗都能對應到研究問題

---

## Phase 2：類別設計與欄位設計定稿

### 目標
先定好你們要分哪些類別，還有資料長什麼樣。

### 建議第一版類別
- 政治
- 社會
- 國際
- 生活

### 要做的事
1. 為每一類寫定義
2. 寫出容易混淆的邊界案例
3. 設計 raw dataset 欄位
4. 設計 clean dataset 欄位
5. 決定最終 `category_final` 的規格

### 建議 raw 欄位
```text
id,title,category_raw,category_final,source_site,source_section,publish_date,url,crawl_date,language,is_duplicate,keep,drop_reason,notes
```

### 建議 clean 欄位
```text
id,title,category_final,source_site,publish_date,url
```

### 這階段輸出
- `appendix/category_definition_table.md`
- `appendix/field_definition_table.md`
- `configs/label_rules.csv` 初稿

### 完成判準
- 看到一筆資料時，團隊成員大多能依相同規則判斷類別
- 類別不再反覆改動

---

## Phase 3：資料來源挑選與 mapping 規則建立

### 目標
不要一開始就抓很多站。先挑 2 到 4 個穩定來源。

### 建議策略
優先選：
- 分類清楚
- 列表頁穩定
- 標題、日期、連結可直接取得
- 不需要登入

### 要做的事
1. 選 2 到 4 個新聞來源
2. 每個來源挑對應分類頁
3. 建立 raw category 到 final category 的 mapping 表
4. 寫清楚哪些分類不收

### 這階段輸出
- `configs/sources.json`
- `data/processed/label_mapping.csv` 初稿
- `data/raw/README_raw_sources.md`

### 完成判準
- 每個來源都能回答：抓哪裡、抓哪些欄位、對應到哪個 final 類別

---

## Phase 4：先做單站 crawler，確認流程可跑

### 目標
先拿一個網站打通全流程，不要一口氣開 4 個站結果全部都壞。

### 要做的事
1. 寫第一支 crawler
2. 抓一小批資料
3. 確認欄位完整
4. 匯出 raw CSV
5. 記錄蒐集 log

### 建議檔案
- `src/collect/crawl_site_01.py`
- `src/collect/run_collection.py`

### 這階段輸出
- 至少 1 個 raw CSV
- 可運行的 crawler 程式
- collection log

### 完成判準
- 程式可重跑
- 產出的欄位符合先前欄位設計
- 團隊知道完整蒐集流程怎麼走

---

## Phase 5：擴充到多站蒐集，完成 raw data 池

### 目標
在流程已打通後，再擴到 2 到 4 個來源。

### 要做的事
1. 複製 crawler 架構到其他站
2. 逐站逐分類抓取資料
3. 每次蒐集都保留 raw CSV
4. 建立蒐集紀錄

### 建議資料量目標
- 最低：每類 300 筆
- 理想：每類 500 到 800 筆
- 全體：2000 筆上下很適合高中小論文

### 這階段輸出
- 多個 raw CSV
- 來源清單
- collection log 更新版

### 完成判準
- 每類至少有基本可用資料量
- 原始資料可追溯到來源站與日期

---

## Phase 6：資料清理、合併、去重、輸出 clean dataset

### 目標
這是整個專題最關鍵的地基。資料沒整理乾淨，後面分數再漂亮也不穩。

### 要做的事
1. 合併所有 raw CSV
2. 去除空白標題
3. 依 `url` 或 `title` 去重
4. 套用 label mapping
5. 過濾掉不適合資料
6. 抽樣人工檢查
7. 輸出 clean dataset

### 建議清理腳本
- `src/clean/merge_raw.py`
- `src/clean/deduplicate.py`
- `src/clean/normalize_labels.py`
- `src/clean/filter_titles.py`
- `src/clean/export_clean_csv.py`

### 這階段輸出
- `data/interim/merged_raw.csv`
- `data/interim/deduped.csv`
- `data/interim/labeled.csv`
- `data/processed/news_titles_clean.csv`
- `data/processed/label_mapping.csv`
- `data/processed/manual_audit_sample.csv`
- `results/logs/cleaning_log.md`

### 完成判準
- 有一份乾淨、可直接進模型的資料集
- 能說清楚每一步資料量怎麼變化
- 能拿給評審看資料品質控制流程

---

## Phase 7：先做 baseline，不要急著堆很多模型

### 目標
先確認資料真的能訓練出合理結果。

### 建議 baseline
- CountVectorizer + Multinomial Naive Bayes

### 要做的事
1. 資料切 train/test
2. 跑 baseline
3. 產出 Accuracy、Precision、Recall、Macro F1
4. 先看 confusion matrix

### 建議檔案
- `src/train/train_baseline.py`
- `src/train/evaluate_models.py`

### 這階段輸出
- 第一版 baseline 結果
- confusion matrix 初版
- class metrics 初版

### 完成判準
- 確認整個 training pipeline 是通的
- 確認資料不是完全不可分

---

## Phase 8：正式模型比較

### 目標
在 baseline 通了之後，再做有意義的比較。

### 建議最少比較組合
1. CountVectorizer + Multinomial Naive Bayes
2. TF-IDF + Multinomial Naive Bayes
3. TF-IDF + Logistic Regression
4. TF-IDF + Linear SVM

### 可選加強版
5. TF-IDF + Linear SVM + bigram
6. TF-IDF + Logistic Regression + bigram
7. 斷詞前後比較

### 要做的事
1. 固定同一組 train/test split
2. 用相同條件比較各模型
3. 產出總比較表
4. 選最佳模型

### 這階段輸出
- `results/tables/model_comparison.csv`
- `results/tables/class_metrics.csv`
- `results/figures/fig_model_comparison.png`
- `results/figures/fig_confusion_matrix_best.png`

### 完成判準
- 能回答哪一組方法最好
- 能回答為什麼不是只看 Accuracy

---

## Phase 9：視覺化、流程圖、錯誤分析

### 目標
把「研究理解力」做出來，這是評審很在意的部分。

### 要做的事
1. 畫資料分布圖
2. 畫模型比較圖
3. 畫最佳模型混淆矩陣
4. 整理 5 到 10 則錯誤案例
5. 畫 3 張流程圖

### 至少要有的圖
- 類別分布圖
- 模型比較圖
- confusion matrix

### 至少要有的流程圖
- 研究總流程圖
- 資料處理流程圖
- 模型比較流程圖

### 這階段輸出
- `results/figures/fig_dataset_distribution.png`
- `results/figures/fig_model_comparison.png`
- `results/figures/fig_confusion_matrix_best.png`
- `results/figures/fig_top_features.png`（可選）
- `results/tables/error_cases.csv`
- `diagrams/research_flow.md`
- `diagrams/data_pipeline.md`
- `diagrams/model_pipeline.md`

### 完成判準
- 評審可以直接從圖表看懂結果
- 你們不是只有數字，還有解釋能力

---

## Phase 10：論文撰寫與評審展示包整理

### 目標
把前面所有成果整合成「可評審」的最終成品。

### 要做的事
1. 寫正式論文
2. 寫摘要
3. 整理附錄
4. 整理評審展示包
5. 準備口頭報告腳本
6. 確定每張圖、每張表、每個檔案都能對應研究問題

### 論文章節建議
1. 緒論
2. 文獻探討
3. 研究方法
4. 研究結果與分析
5. 結論與建議

### 這階段輸出
- `paper/final_paper.pdf`
- `paper/final_paper.docx`
- `paper/abstract_zh.md`
- `appendix/category_definition_table.md`
- `appendix/field_definition_table.md`
- `appendix/judge_demo_script.md`

### 完成判準
- 論文、簡報、圖表、資料、程式四者一致
- 評審問到流程時，你們能立刻打開對應證據檔案

---

## 四、學生團隊實際分工建議

如果是 3 到 4 人小組，建議這樣分：

### 角色 A：資料蒐集負責
- sources.json
- crawler 撰寫
- raw CSV 管理
- collection log

### 角色 B：資料清理負責
- merge / dedup / label normalize
- clean dataset
- manual audit
- cleaning log

### 角色 C：模型與評估負責
- baseline
- model comparison
- metrics
- confusion matrix
- error cases

### 角色 D：論文與展示整合負責
- 流程圖
- 圖表排版
- 論文整合
- 口頭報告稿

如果只有 2 人，就改成：
- 1 人主抓資料與清理
- 1 人主抓模型與論文
- 但兩邊都要互相看懂彼此流程

---

## 五、最容易踩雷的錯誤順序

下面這些做法很常見，但不建議。

### 錯法 1：先跑很多模型，資料還沒整理好
後果：
- 分數不穩
- 結果不可解釋
- 評審一問資料流程就卡住

### 錯法 2：類別一直改
後果：
- 前面蒐集資料作廢
- mapping 表一直重做
- 後面論文寫不穩

### 錯法 3：只留最後 clean dataset，不留 raw data
後果：
- 評審問來源時拿不出證據
- 沒辦法回頭查問題

### 錯法 4：只有 Accuracy，沒有 Macro F1 和 confusion matrix
後果：
- 評審會覺得評估不完整

### 錯法 5：有圖表沒文字解釋
後果：
- 看起來像貼圖，不像研究分析

---

## 六、每一階段結束後要立即保存的東西

每完成一個階段，至少保存：

### 資料階段
- 原始 CSV
- clean CSV
- mapping 表
- log

### 模型階段
- 模型比較表
- class metrics 表
- confusion matrix 圖
- error cases 表

### 展示階段
- 流程圖
- 類別分布圖
- 簡報用圖片
- 論文草稿

原則很簡單：

**不要只保留最後結果，要保留中間證據。**

---

## 七、建議的最終時間順序

如果要做成比較穩的版本，建議時間順序如下：

### 第 1 週
- 題目定稿
- 類別定稿
- 欄位設計
- 來源挑選
- 單站 crawler 打通

### 第 2 週
- 多站蒐集
- raw data 整理
- 去重、label normalize
- clean dataset 完成

### 第 3 週
- baseline
- 正式模型比較
- 指標表與 confusion matrix

### 第 4 週
- 錯誤分析
- 視覺化
- 流程圖
- 論文初稿

### 第 5 週
- 論文修稿
- 簡報整理
- 評審展示包總檢查

---

## 八、最終交付前總檢查順序

真正要送出或報告前，請照這個順序最後檢查一次：

1. `paper/final_paper.pdf` 是否完成
2. `data/processed/news_titles_clean.csv` 是否完成
3. `data/processed/label_mapping.csv` 是否完成
4. `results/tables/model_comparison.csv` 是否完成
5. `results/figures/fig_model_comparison.png` 是否完成
6. `results/figures/fig_confusion_matrix_best.png` 是否完成
7. `results/tables/error_cases.csv` 是否完成
8. 3 張流程圖是否完成
9. 類別定義表與欄位定義表是否完成
10. 口頭報告時要展示的畫面是否都找得到

---

## 九、最核心的執行判準

如果團隊照這份順序做，到最後應該能達成這個狀態：

- 有資料
- 有程式
- 有流程
- 有比較
- 有圖表
- 有錯誤分析
- 有論文
- 有可展示證據

這樣評審看到的就不是一個「只有模型分數的作業」，而是一個完整的資訊科研究作品。

---

## 十、一句話版本的執行順序

如果要超精簡記住，就記這句：

**先定類別與資料規格，再蒐集與清理資料，再做 baseline 與模型比較，最後補圖表、錯誤分析、論文與評審展示包。**
