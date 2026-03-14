# B 題建置狀態板

## 專案
- 題目方向：中文新聞標題分類研究
- 目標：完成可展示給評審的完整研究流程，涵蓋資料蒐集、前處理、建模、評估、視覺化、錯誤分析與流程說明。

## 整體狀態
- 目前階段：規劃文件已完成，第一批實作骨架已啟動
- 狀態判定：進行中

## 已完成文件
### 規劃 / 研究設計
- `analysis/paper_news_data_plan.md`
- `analysis/paper_news_detailed_outline.md`
- `analysis/paper_news_diagrams.md`

### 能力 / 專案支援
- `skills/news-text-classification-project/` 已建立，用於支援此題目的端到端工作流程

## 規劃中的主要檔案 / 產出
### 資料層
- `paper_project/data/raw/`：原始新聞標題資料
- `paper_project/data/interim/`：清理後中介資料
- `paper_project/data/processed/`：最終訓練資料集
- `paper_project/data/label_mapping.csv`：網站分類對應到研究類別的映射表
- `paper_project/data/dataset_schema.md`：欄位定義與資料說明

### 程式層
- `paper_project/src/collect_news.py`：新聞標題蒐集主程式
- `paper_project/src/clean_titles.py`：文字清理與資料整理
- `paper_project/src/build_dataset.py`：整併資料與切分資料集
- `paper_project/src/train_baselines.py`：baseline 模型訓練
- `paper_project/src/evaluate_models.py`：模型評估與輸出指標
- `paper_project/src/error_analysis.py`：錯誤案例整理
- `paper_project/src/visualize_results.py`：圖表輸出

### 輸出層
- `paper_project/results/metrics_summary.csv`
- `paper_project/results/confusion_matrix.*`
- `paper_project/results/model_comparison.*`
- `paper_project/results/error_cases.csv`
- `paper_project/docs/method_flow.md`
- `paper_project/docs/experiment_log.md`

## 已完成里程碑
- 已選定 B 題方向
- 已確認簡化題名方向為「中文新聞標題分類研究」
- 已完成資料來源與蒐集策略規劃
- 已完成評審導向的詳細論文大綱
- 已完成流程圖設計稿
- 已建立專用技能支援此研究題目
- 已啟動第一批實作工作：
  - 新聞蒐集 skeleton
  - schema / label mapping
  - cleaning pipeline
  - baseline training script skeleton

## 目前阻塞 / 風險
- `paper_project/` 目錄先前尚未建立，現已補建，但實作檔案尚未落地
- 第一批程式骨架目前屬於「已啟動但未驗收完成」狀態
- 新聞網站實際可抓取性、分類一致性與反爬限制仍需在實作階段驗證
- 最終研究類別數（4 類或擴充）仍需依實際資料品質確認
- 尚未看到實際資料樣本、訓練結果與評估圖表，因此結果章節仍屬待實作

## 下一步
1. 在 `paper_project/` 內建立正式資料夾結構
2. 落地第一批 Python 腳本骨架
3. 先對 1 到 2 個新聞來源做小規模抓取驗證
4. 確認 label mapping 與最終研究類別設計
5. 產出第一版乾淨資料集 CSV
6. 跑 baseline（CountVectorizer / TF-IDF × NB / LR / Linear SVM）
7. 輸出 Accuracy、Macro F1、Confusion Matrix 與錯分案例
8. 將實驗結果回填到論文章節與圖表素材

## 建議回報口徑
- 已完成：研究規劃三件套（資料計畫、論文大綱、流程圖）
- 進行中：資料管線與 baseline 程式骨架
- 待確認：資料來源穩定性、類別映射、首版資料集品質
- 下一個可回報里程碑：成功抓到首批資料並跑出第一版 baseline 指標
