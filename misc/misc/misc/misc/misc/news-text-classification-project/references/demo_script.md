# 中文新聞標題分類研究：評審口頭展示腳本（第一版）

本文件是給現場口頭報告與檔案展示使用的短版 demo script。
目標不是把所有內容念完，而是讓評審在短時間內看到：

1. 題目是什麼
2. 資料從哪裡來
3. 類別怎麼定
4. 程式怎麼處理資料
5. 模型怎麼比較
6. 結果怎麼解讀
7. 整個流程是否可重現

建議展示時間：**5 到 8 分鐘**
建議原則：**一邊講、一邊開檔，不空講**

---

## 一、展示總策略

評審最想看到的不是只有最後模型分數，而是整個研究流程是否完整、清楚、可追溯。

所以 demo 順序建議固定為：

1. 研究題目與研究目的
2. 資料來源選擇
3. 類別與欄位設計
4. 蒐集程式
5. 清理程式
6. 訓練與評估程式
7. 流程圖
8. 圖表與結果
9. 錯誤分析與限制
10. 檔案結構與可重現性

一句話原則：

**先證明你們有方法，再證明你們有結果。**

---

## 二、展示前要先開好的視窗

建議報告前先把下列檔案或資料夾預先開好，避免現場找檔案浪費時間。

### 必開檔案
- `paper_project/README_build_order.md`
- `paper_project/source_selection.md`
- `paper_project/schemas/news_schema.md`
- `paper_project/schemas/label_mapping.csv`
- `paper_project/code/collect_news_titles.py`
- `paper_project/code/clean_news_data.py`
- `paper_project/code/train_baseline.py`
- `paper_project/code/plot_results.py`
- `paper_project/diagrams/workflow.mmd`
- `paper_project/diagrams/data_pipeline.mmd`
- `paper_project/diagrams/model_comparison.mmd`
- `paper_project/judge_package_checklist.md`

### 如果屆時已經有實際輸出，請另外先開
- `paper_project/data/raw/` 中的原始 CSV
- `paper_project/data/processed/news_titles_clean.csv`
- `paper_project/results/metrics_summary.csv` 或 `metrics_summary.json`
- `paper_project/results/...confusion_matrix...`
- `paper_project/results/figures/class_distribution.png`
- `paper_project/results/figures/model_comparison.png`
- `paper_project/results/figures/confusion_matrix.png`
- `paper_project/results/tables/error_cases.csv`

如果正式輸出還沒全部完成，就先以目前的規劃檔、schema、程式骨架、流程圖來展示「研究流程已被系統化設計」。

---

## 三、5 到 8 分鐘展示腳本

下面是建議的實際展示流程。每一步都包含：
- 要開什麼
- 要講什麼
- 這一步的重點是什麼

---

## Step 1：先講題目與研究核心

### 開啟檔案
- `paper_project/README_build_order.md`

### 畫面停留位置
- 標題
- 「主題方向：中文新聞標題分類研究」
- 總原則與建議執行順序

### 可直接講的版本
「我們的題目是中文新聞標題分類研究。這個專題不是只追求模型分數，而是希望完整展示一個文字分類研究的流程：從資料蒐集、資料清理、模型比較，到圖表、錯誤分析與評審展示，都能清楚呈現。」

### 這一步要讓評審看到的重點
- 題目明確
- 研究對象是「新聞標題」
- 這不是只做結果，而是完整研究流程

### 建議停留時間
- 30 到 45 秒

---

## Step 2：說明為什麼選這些資料來源

### 開啟檔案
- `paper_project/source_selection.md`

### 畫面停留位置
- 推薦來源 1：中央社 CNA
- 最終建議組合
- 蒐集限制與研究約束

### 可直接講的版本
「在資料來源上，我們沒有一開始就混很多站，而是先以分類較清楚、格式較穩定的來源當主資料集。像這份文件裡，我們先評估中央社等來源，考慮的是資料是否公開、類別是否清楚、欄位是否容易保留，以及流程能不能重現。」

### 補一句
「我們也刻意只抓標題、日期、分類、網址這些基本欄位，不抓全文，這樣研究焦點比較明確，也能降低資料處理複雜度。」

### 這一步要讓評審看到的重點
- 資料來源不是亂選的
- 有選站標準
- 有研究範圍與限制意識

### 建議停留時間
- 40 到 60 秒

---

## Step 3：展示類別設計與資料欄位設計

### 開啟檔案
- `paper_project/schemas/news_schema.md`
- `paper_project/schemas/label_mapping.csv`

### 畫面停留位置
- 四個最終類別定義
- 欄位定義
- raw_label 到 category_final 的 mapping

### 可直接講的版本
「這一段是我們研究的核心規格。首先，我們把最終類別固定成四類：政治、社會、國際、生活。因為不同新聞網站原本的分類很多，不適合直接拿來訓練，所以我們先制定一份 mapping 規則，把原始分類統一映射到研究使用的最終標籤。」

「另外，我們也先定義資料欄位，例如 title、category_raw、category_final、source、date、url。這樣後面無論是資料清理還是模型訓練，都有一致格式。」

### 如果時間夠，可補一句
「評審如果要看方法的嚴謹性，這份 schema 和 mapping 其實很關鍵，因為它決定了資料不是隨便貼進模型，而是先經過標準化設計。」

### 這一步要讓評審看到的重點
- 類別先定義，再收資料
- 有明確欄位設計
- 有映射規則，不是直接照搬網站分類

### 建議停留時間
- 45 到 60 秒

---

## Step 4：展示資料蒐集程式

### 開啟檔案
- `paper_project/code/collect_news_titles.py`

### 畫面停留位置
建議依序停在：
- 檔案最上方 docstring
- `CSV_COLUMNS`
- `SiteConfig`
- `TARGET_SITE`
- `extract_list_rows()` 的說明區

### 可直接講的版本
「這是我們的資料蒐集程式。它目前是第一版可重用 skeleton，重點不是說已經支援所有網站，而是把資料蒐集流程標準化。像這裡先固定輸出欄位，然後把網站設定、請求、欄位整理分開，這樣之後換來源時比較容易維護。」

「我們也刻意把它寫成可擴充的形式，例如網站設定和爬取邏輯分離，這樣可以先從單站驗證，再擴到多站。」

### 這一步要讓評審看到的重點
- 你們真的有寫蒐集程式
- 不是手動抄資料
- 程式結構有考慮後續擴充與重現

### 建議停留時間
- 40 到 50 秒

---

## Step 5：展示資料清理程式

### 開啟檔案
- `paper_project/code/clean_news_data.py`

### 畫面停留位置
建議停在：
- `DEFAULT_LABEL_ALIASES`
- `normalize_title()`
- `title_dedupe_key()`
- `clean_rows()`
- `main()` 輸出統計區

### 可直接講的版本
「這支程式負責把原始資料整理成可訓練的格式。像這裡可以看到，我們會檢查必要欄位、正規化標題、做標籤統一、去除重複資料，最後輸出乾淨版本的 CSV。」

「比起直接把資料丟進模型，我們更重視資料品質，所以這一步會留下讀入幾筆、保留幾筆、刪掉幾筆的統計，方便之後向評審說明資料是怎麼整理過來的。」

### 若現場已有 clean CSV，可接著打開
- `paper_project/data/processed/news_titles_clean.csv`

並補講：
「這就是清理後真正進模型的資料格式。」

### 這一步要讓評審看到的重點
- 有前處理流程
- 有去重與清理規則
- 有資料品質控制概念

### 建議停留時間
- 45 到 60 秒

---

## Step 6：展示 baseline 訓練與評估程式

### 開啟檔案
- `paper_project/code/train_baseline.py`

### 畫面停留位置
建議停在：
- 檔案最上方說明
- `build_models()`
- `evaluate_model()`
- `metadata` 與 `save_outputs()`
- 主程式印出 Accuracy、Macro F1 的區塊

### 可直接講的版本
「這支程式負責 baseline 訓練。它會先讀入資料，再切分 train/test，然後跑至少兩個基礎模型，例如 Naive Bayes 和 Logistic Regression，並輸出 Accuracy、Macro F1、classification report 和 confusion matrix。」

「我們特別強調 Macro F1，是因為新聞類別不一定完全平均，如果只看 Accuracy 會不夠完整。」

### 若屆時已有結果檔，請同步打開
- `paper_project/outputs/baseline/metrics_summary.csv`
- 或實際產出的 metrics JSON / confusion matrix CSV

### 可以補一句
「這樣評審不只看到程式，也可以看到程式實際輸出的指標檔案。」

### 這一步要讓評審看到的重點
- 有 baseline，不是只挑一個模型
- 有正式評估指標
- 有保存結果檔案，可追溯

### 建議停留時間
- 45 到 60 秒

---

## Step 7：展示圖表輸出程式

### 開啟檔案
- `paper_project/code/plot_results.py`

### 畫面停留位置
建議停在：
- `plot_class_distribution()`
- `plot_model_comparison()`
- `plot_confusion_matrix()`
- `main()` 中輸出的圖檔名稱

### 可直接講的版本
「這支程式把數值結果轉成評審更容易看的圖表，像是類別分布圖、模型比較圖，以及最佳模型的混淆矩陣。這樣在口頭報告時，不用只給一堆數字，而是能直接視覺化展示結果。」

### 若屆時已有圖片，直接展示
- `class_distribution.png`
- `model_comparison.png`
- `confusion_matrix.png`

### 這一步要讓評審看到的重點
- 有視覺化輸出
- 研究結果不是只有文字敘述
- 結果可直接進簡報或論文

### 建議停留時間
- 30 到 45 秒

---

## Step 8：展示三張流程圖

### 開啟檔案
- `paper_project/diagrams/workflow.mmd`
- `paper_project/diagrams/data_pipeline.mmd`
- `paper_project/diagrams/model_comparison.mmd`

### 建議展示順序
1. `workflow.mmd`
2. `data_pipeline.mmd`
3. `model_comparison.mmd`

### 可直接講的版本
「除了程式和資料，我們也把整個研究流程圖像化。第一張是整體研究流程，從研究目的、資料蒐集、前處理、特徵工程、模型訓練到結果分析。第二張是資料處理流程，讓評審看見 raw data 如何變成 clean dataset。第三張是模型比較流程，說明不同特徵與模型組合是怎麼被公平比較的。」

### 如果評審只願意看一張
優先展示：
- `workflow.mmd`

### 這一步要讓評審看到的重點
- 你們對流程有整體理解
- 方法是有架構的
- 不只是臨時拼湊程式

### 建議停留時間
- 45 到 60 秒

---

## Step 9：如果已有結果，展示輸出檔與圖表

### 優先展示項目
1. `news_titles_clean.csv`
2. `metrics_summary.csv`
3. `model_comparison.png`
4. `confusion_matrix.png`
5. `error_cases.csv`

### 可直接講的版本
「這裡是目前實驗輸出的結果。首先是 clean dataset，代表我們真正進模型的資料。接著是模型指標總表，可以比較不同方法的 Accuracy 和 Macro F1。再來是模型比較圖和混淆矩陣，幫助我們看出哪些類別最容易混淆。最後是錯分案例表，用來分析模型為什麼會判錯，而不是只停在分數本身。」

### 如果結果還沒全部完成，可改講
「目前我們已經把研究規格、資料流程、清理流程、訓練程式與圖表程式建立完成；正式結果會由這套流程產出，屆時可以直接補進這些固定位置的檔案。」

### 這一步要讓評審看到的重點
- 這個系統有實際輸出物
- 可從數字走到解釋
- 有錯誤分析，不只看準確率

### 建議停留時間
- 45 到 75 秒

---

## Step 10：最後用檢查清單收尾

### 開啟檔案
- `paper_project/judge_package_checklist.md`

### 畫面停留位置
- 八個展示區塊
- 必出畫面
- 交件前最後總檢查

### 可直接講的版本
「最後這份檢查清單是我們用來確認整個研究對評審是否完整可展示。也就是說，我們不只想做出模型，而是要確保題目、資料來源、欄位設計、清理流程、模型比較、圖表、錯誤分析與可重現檔案結構，全部都能被清楚呈現。」

### 收尾一句建議
「所以這個專題的核心不是只有分類結果，而是把中文新聞標題分類這件事，做成一套可重現、可檢查、可展示的研究流程。」

### 建議停留時間
- 30 到 45 秒

---

## 四、最短版 3 分鐘展示順序

如果評審時間非常短，只展示這 6 個畫面：

1. `README_build_order.md`
2. `source_selection.md`
3. `news_schema.md` + `label_mapping.csv`
4. `collect_news_titles.py` + `clean_news_data.py`
5. `train_baseline.py` + `plot_results.py`
6. `workflow.mmd` + 已產出的結果圖

### 3 分鐘版講法
- 第 1 分鐘：講題目、資料來源、類別設計
- 第 2 分鐘：講蒐集程式、清理程式、訓練程式
- 第 3 分鐘：講流程圖、結果圖、錯誤分析與總結

---

## 五、評審可能會問的問題與建議回答

### Q1：你們的資料從哪裡來？
建議回答：
「我們先選分類較清楚、公開可瀏覽、欄位容易保留的新聞來源，並保留標題、日期、分類與網址。不是手動整理，而是用程式蒐集並保存原始資料。」

### Q2：為什麼只做標題，不做全文？
建議回答：
「因為本研究的重點是標題分類。標題本身就濃縮了新聞主題，而且只用標題可以讓資料清理、標註與模型比較更聚焦，也更適合高中專題的研究規模。」

### Q3：不同網站分類不一樣，怎麼統一？
建議回答：
「我們先設計自己的最終研究類別，再用 mapping 表把網站原始分類映射到研究標籤，必要時再做人工抽查，所以不是直接照搬網站分類。」

### Q4：你們怎麼知道模型好不好？
建議回答：
「我們不只看 Accuracy，也看 Macro F1、Precision、Recall 和 confusion matrix，因為類別資料不一定平均，只看 Accuracy 會不夠完整。」

### Q5：如果模型判錯，你們有分析原因嗎？
建議回答：
「有，我們會整理錯分案例，看是因為標題太短、類別邊界重疊、詞語模糊，還是資料標註規則需要再修正。」

### Q6：你們怎麼證明這不是只做出一份報告？
建議回答：
「因為我們保留了資料規格、原始資料、清理程式、訓練程式、圖表程式和流程圖，整個研究流程是可重現、可檢查的。」

---

## 六、現場展示注意事項

### 1. 不要一開始就秀模型分數
先講研究問題、資料來源、類別設計，再進結果。

### 2. 不要一次開太多程式碼
每支程式只停在最能說明功能的地方，例如：
- 蒐集：欄位設計與站點設定
- 清理：去重與標籤統一
- 訓練：模型與指標輸出
- 圖表：三種圖的輸出函式

### 3. 每個畫面只講一個重點
不要邊開 schema 又講模型，又跳去資料來源。順序要穩。

### 4. 若正式結果尚未完整
不要硬說已完成全部。
可以誠實說：
「目前已完成研究規格、資料流程與程式架構，正式實驗結果會由這套流程穩定產出。」

### 5. 若已有實際結果
請一定展示：
- 一份 clean CSV
- 一張模型比較圖
- 一張 confusion matrix
- 一份錯誤案例表

這四個畫面最能讓評審感受到專題成熟度。

---

## 七、最後收束用一句話

可直接作為最後結尾：

**「我們這個專題的重點，不只是做出新聞分類模型，而是把中文新聞標題分類的整個研究流程，做成一套有資料、有程式、有圖表、有分析，而且可以向評審完整展示的方法。」**

---

## 八、目前版本定位

這是一份**第一版 oral demo script**，用途是先固定展示順序與必出畫面。
等後續實際資料集、圖表、metrics、錯誤分析表正式產出後，建議再做第二版更新，把下列具體檔名補進去：

- 實際 raw CSV 檔名
- 實際 clean dataset 檔名
- 實際 metrics summary 路徑
- 實際 confusion matrix 路徑
- 實際圖表檔名
- 實際 error_cases.csv 路徑

到第二版時，就可以把本文件從「展示腳本」升級成「現場逐頁口說稿」。
