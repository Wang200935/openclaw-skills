# Baseline Hyperparameters

這份文件用來固定第一輪 baseline 實驗的保守型超參數設定。
目標不是一開始就追最高分，而是先建立一組：
- 容易解釋
- 容易重跑
- 適合展示給評審
- 能和後續改良版本清楚比較

本文件對應目前第一輪的 4 個 baseline：
- EXP-01: TF-IDF unigram + Multinomial Naive Bayes
- EXP-02: TF-IDF unigram+bigram + Multinomial Naive Bayes
- EXP-03: TF-IDF unigram + Logistic Regression
- EXP-04: TF-IDF unigram+bigram + Logistic Regression

---

## 1. 設定原則

### 原則 A：先保守，不過度調參
第一輪 baseline 應避免大量 grid search，否則會讓研究流程變得複雜，也不利於說明「基準模型」的概念。

### 原則 B：先確保可重現
所有會影響結果波動的設定應盡量固定，例如：
- random_state
- train/validation/test split
- class label order
- vectorizer 參數

### 原則 C：先讓模型穩定收斂
由於新聞標題屬於短文本，特徵稀疏很常見，因此第一輪設定以穩定、常見、教科書級配置為主。

---

## 2. TF-IDF Vectorizer 建議基準設定

> 適用於 EXP-01 ~ EXP-04。

### 共用基準

```python
TfidfVectorizer(
    analyzer="word",
    lowercase=False,
    token_pattern=None,
    tokenizer=custom_tokenizer_or_split,
    preprocessor=None,
    strip_accents=None,
    use_idf=True,
    smooth_idf=True,
    sublinear_tf=True,
    norm="l2",
    min_df=2,
    max_df=0.95,
    max_features=20000,
)
```

### 參數說明

- `analyzer="word"`
  - 若前面已做 jieba 斷詞並輸出空白分隔字串，第一輪先用 word-level TF-IDF，最容易解釋。

- `lowercase=False`
  - 中文資料通常不需要強制轉小寫；若資料中混有英文縮寫（AI、NBA、ETF），保留原貌比較安全。

- `token_pattern=None`
  - 若搭配自訂 tokenizer 或已預先斷詞字串，建議關掉預設 token pattern，避免和中文斷詞流程互相干擾。

- `use_idf=True`
  - TF-IDF 的核心設定，保留。

- `smooth_idf=True`
  - 避免極端低頻詞導致 idf 不穩，屬於穩健型預設。

- `sublinear_tf=True`
  - 用 `1 + log(tf)` 壓低詞頻過大的影響，對新聞標題這類短文本通常是保守而合理的設定。

- `norm="l2"`
  - 線性模型常見標準配置。

- `min_df=2`
  - 至少出現 2 次才保留，可先去除只出現一次的極端稀疏噪音詞。
  - 對小型資料集來說比 `min_df=3` 更保守，不會太早刪掉資訊。

- `max_df=0.95`
  - 過度高頻詞可能對分類幫助有限，先排除在 95% 文件中都出現的詞。

- `max_features=20000`
  - 第一輪先限制特徵上限，降低記憶體與運算負擔，也方便模型比較。
  - 若資料量仍小，可視情況改成 `10000`；若資料量擴大，可再放寬。

---

## 3. TF-IDF 的 n-gram 設定

### EXP-01 / EXP-03
```python
ngram_range=(1, 1)
```
- unigram 作為最基本 baseline。
- 優點是特徵簡單、可解釋性高、計算快。

### EXP-02 / EXP-04
```python
ngram_range=(1, 2)
```
- 在 unigram 基礎上加入 bigram。
- 用來檢查像「台積電 擴產」「立法院 三讀」這類雙詞搭配是否有額外幫助。
- 第一輪不建議直接上 trigram，因為短文本容易太稀疏。

---

## 4. Multinomial Naive Bayes 建議基準設定

### 建議設定

```python
MultinomialNB(
    alpha=1.0,
    fit_prior=True,
)
```

### 參數說明

- `alpha=1.0`
  - 使用 Laplace smoothing，這是非常經典也保守的 baseline 設定。
  - 對短文本與稀疏特徵來說，先用 `1.0` 很合理。
  - 若之後要第二輪微調，可再比較 `0.1 / 0.5 / 1.0`。

- `fit_prior=True`
  - 讓模型使用資料中的類別先驗分布。
  - 如果資料類別略不平衡，這通常比硬設平均先驗更符合真實情況。

### 為什麼 NB 適合當第一輪 baseline
- 訓練快
- 容易解釋
- 對文字分類是經典基準
- 很適合和 Logistic Regression 做第一輪比較

---

## 5. Logistic Regression 建議基準設定

### 建議設定

```python
LogisticRegression(
    C=1.0,
    penalty="l2",
    solver="liblinear",
    max_iter=1000,
    class_weight=None,
    random_state=42,
)
```

### 參數說明

- `C=1.0`
  - 標準保守值，先不要太強或太弱正則化。
  - 第二輪若要微調，可比較 `0.5 / 1.0 / 2.0`。

- `penalty="l2"`
  - 最常見、最穩定的線性分類器正則化方式。

- `solver="liblinear"`
  - 對中小型文字分類資料常見且穩定。
  - 若之後資料量變大、類別更多，也可考慮 `lbfgs` 或 `saga`，但 baseline 先用 `liblinear` 即可。

- `max_iter=1000`
  - 比預設值更保守，避免因特徵稀疏導致尚未收斂。

- `class_weight=None`
  - 第一輪 baseline 先不做人為平衡修正，保留最自然的模型表現。
  - 若後續確認類別不平衡明顯，再比較 `class_weight="balanced"`。

- `random_state=42`
  - 固定隨機性，方便重跑與論文記錄。

### 為什麼 LR 適合當第一輪 baseline
- 是文字分類中非常常見的強基準
- 比 Naive Bayes 更能學到特徵權重差異
- 容易搭配 TF-IDF 使用
- 係數可拿來做後續關鍵詞解釋

---

## 6. 第一輪不建議先動的參數

為了保持 baseline 的單純性，第一輪先不要優先搜尋以下參數：

- TF-IDF `max_features` 的大範圍搜索
- TF-IDF `min_df` / `max_df` 的密集 grid search
- NB 的大量 `alpha` 搜尋
- LR 的大量 `C` 搜尋
- class_weight 調整
- 過度複雜的 stopword 組合
- trigram 或更高階 n-gram

原因很簡單：

**baseline 的任務是建立比較基準，不是一次把最佳模型找完。**

---

## 7. 建議搭配的資料切分與訓練設定

雖然這不是模型超參數本身，但建議一起固定：

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)
```

### 理由
- `test_size=0.2`：保留 20% 做測試，屬於常見設定。
- `random_state=42`：方便重現。
- `stratify=y`：確保各類別在切分後分布不要偏掉。

如果資料量允許，正式報告還可補：
- 5-fold cross-validation

這也和評估規劃一致，能讓結果更穩健。

---

## 8. 建議記錄格式

每次訓練都應把下列設定一併存進 config 檔或 metrics 檔：

```json
{
  "vectorizer": "tfidf",
  "ngram_range": [1, 2],
  "min_df": 2,
  "max_df": 0.95,
  "max_features": 20000,
  "use_idf": true,
  "smooth_idf": true,
  "sublinear_tf": true,
  "classifier": "logistic_regression",
  "C": 1.0,
  "penalty": "l2",
  "solver": "liblinear",
  "max_iter": 1000,
  "class_weight": null,
  "random_state": 42
}
```

這樣之後做：
- 實驗對照表
- 論文方法章節
- 附錄實驗設定

都會輕鬆很多。

---

## 9. 第一輪 baseline 建議總表

| Run ID | Vectorizer | ngram_range | Classifier | Key hyperparameters |
|---|---|---|---|---|
| EXP-01 | TF-IDF | (1,1) | MultinomialNB | `min_df=2`, `max_df=0.95`, `max_features=20000`, `alpha=1.0` |
| EXP-02 | TF-IDF | (1,2) | MultinomialNB | `min_df=2`, `max_df=0.95`, `max_features=20000`, `alpha=1.0` |
| EXP-03 | TF-IDF | (1,1) | LogisticRegression | `min_df=2`, `max_df=0.95`, `max_features=20000`, `C=1.0`, `solver=liblinear`, `max_iter=1000` |
| EXP-04 | TF-IDF | (1,2) | LogisticRegression | `min_df=2`, `max_df=0.95`, `max_features=20000`, `C=1.0`, `solver=liblinear`, `max_iter=1000` |

---

## 10. 第二輪可微調方向

等第一輪 baseline 跑完後，再考慮以下小幅調整：

### TF-IDF
- `min_df`: 1 / 2 / 3
- `max_df`: 0.9 / 0.95 / 1.0
- `max_features`: 10000 / 20000 / None
- `ngram_range`: (1,1) / (1,2)

### Naive Bayes
- `alpha`: 0.1 / 0.5 / 1.0

### Logistic Regression
- `C`: 0.5 / 1.0 / 2.0
- `class_weight`: None / balanced
- `solver`: liblinear / lbfgs

但這些都應該放在 baseline 完成之後。

---

## 11. 一句話結論

第一輪 baseline 建議使用：
- **TF-IDF**：`min_df=2`, `max_df=0.95`, `max_features=20000`, `sublinear_tf=True`
- **MultinomialNB**：`alpha=1.0`
- **LogisticRegression**：`C=1.0`, `penalty='l2'`, `solver='liblinear'`, `max_iter=1000`, `random_state=42`

這組設定夠保守、夠穩、夠容易說明，很適合作為本研究第一批正式 baseline。