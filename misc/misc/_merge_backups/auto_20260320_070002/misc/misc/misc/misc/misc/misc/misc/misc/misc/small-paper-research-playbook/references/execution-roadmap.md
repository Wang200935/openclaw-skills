# small-paper-research-playbook v2 執行路線圖

這份文件不是研究方法教學，而是把 `skill_upgrade_plan_v2.md` 變成可以真的照著做的落地順序。

目標：把目前偏精簡的 research-playbook，補成可操作的競賽級 planning layer。

## v2 目標

這個 skill 在整個小論文技能組裡，角色應該是：

- 幫使用者選對題目
- 提前排除弱題
- 先把資料、方法、驗證設計好
- 再把人導向 writer skill 寫作
- 需要 corpus 證據時，導向 high-school-info-essay-research

換句話說，這層不是負責把文章寫漂亮，而是負責避免一開始就走錯。

---

## 一、v2 核心文件地圖

## 已有文件
- `SKILL.md`
- `references/strong-vs-weak-patterns.md`
- `references/questionnaire-trap-warning.md`
- `references/public-text-data-sources.md`
- `references/nlp-topic-templates.md`
- `references/method-checklist.md`

## 本輪新增 / 擴充重點
- `references/nlp-public-text-playbook.md`
- `references/strong-vs-weak-competition-patterns-v2.md`
- `references/execution-roadmap.md`

## 下一輪建議新增
- `references/method-design-pack.md`
- `references/survey-risk-checklist.md`
- `references/system-validation-checklist.md`
- `references/corpus-reuse-guide.md`

---

## 二、先做什麼：分三階段

## Phase 1：先把最有槓桿的 planning 資產補齊

這一階段的重點不是文件數量，而是讓 agent 一進這個 skill，就能快速把題目導向對的軌道。

### 必做 1：擴充 NLP / 公開文字主線
- 新檔：`nlp-public-text-playbook.md`
- 目的：把「這方向不錯」變成「這題怎麼做」
- 完成標準：
  - 有資料來源選單
  - 有至少 5-6 個題型 archetypes
  - 有 baseline / 強化方法 / 指標 / 限制
  - 有安全範圍與縮題規則

### 必做 2：把強弱判斷從口號變成篩選表
- 新檔：`strong-vs-weak-competition-patterns-v2.md`
- 目的：讓 agent 能快速判斷題目是否值得做
- 完成標準：
  - 有強作品、弱作品、易高估、易低估四層
  - 能直接拿來批改題目草案
  - 內容明確吸收 `v2-deepening-notes.md` 的判斷框架

### 必做 3：給 skill 本身一個執行順序
- 新檔：`execution-roadmap.md`
- 目的：避免之後擴充時變成散亂檔案堆
- 完成標準：
  - 清楚定義 phase、優先順序、依賴關係
  - 說明 playbook 跟 writer / corpus skill 的銜接方式

---

## Phase 2：補決策分支

這個階段要解決的是：不是每個使用者都做 NLP 題。

### 建議新增 1：`method-design-pack.md`
把原本的 `method-checklist.md` 升級成真正的設計包。

至少要補：
- 資料合法性與可重現性
- label 定義
- train / test 切分
- baseline 選擇
- metric 對齊研究問題
- error analysis plan
- limitation 設計

### 建議新增 2：`survey-risk-checklist.md`
目的不是禁做問卷，而是防止問卷獨撐全場。

至少要補：
- 什麼情況下問卷可以做
- 什麼情況下問卷本身太弱
- 問卷題怎麼加上公開資料 / 系統驗證 / 比較設計

### 建議新增 3：`system-validation-checklist.md`
很多作品有原型，但驗證很弱。

至少要補：
- 功能測試
- 對照組 / baseline
- 失敗案例
- 使用者測試
- 效能、延遲、準確度、穩定性

---

## Phase 3：補跨 skill 銜接

這一階段要讓整個 skill stack 更像系統，不是單點參考文件。

### 建議新增：`corpus-reuse-guide.md`
讓使用者知道什麼時候從 playbook 切去 corpus skill。

要能回答：
- 哪些題型在 corpus 裡出現過很多次？
- 哪些題型已經過熱、容易撞題？
- 怎麼找「同類型但執行更好的」範例？
- 怎麼模仿結構，不複製題目？

---

## 三、SKILL.md 應怎麼升級

目前 `SKILL.md` 很短，方向對，但分支不夠明確。

## 建議新增的核心分流

### 1. 公開文字 / NLP 題
導向：
- `references/nlp-public-text-playbook.md`

### 2. 題目聽起來偏問卷或社會觀察
導向：
- `references/strong-vs-weak-competition-patterns-v2.md`
- 未來的 `references/survey-risk-checklist.md`

### 3. 有系統 / 原型 / app / 偵測器
導向：
- 未來的 `references/system-validation-checklist.md`
- `references/method-checklist.md` 或升級後的 `method-design-pack.md`

### 4. 想知道什麼題目比較有得獎相
導向：
- `references/strong-vs-weak-competition-patterns-v2.md`
- corpus skill

### 5. 已經定題，要開始寫
導向：
- `small-paper-writer`

---

## 四、推薦的實作順序

這裡的順序是按照「最能立刻提升實用度」排的。

## 第 1 批：已完成的三檔
1. `nlp-public-text-playbook.md`
2. `strong-vs-weak-competition-patterns-v2.md`
3. `execution-roadmap.md`

### 作用
- 直接補上 v2 裡最缺的 planning 核心
- 讓 agent 面對題目時，能先做分流與篩選
- 讓公開文字題有真正能執行的模板

## 第 2 批：立刻接續
4. `method-design-pack.md`
5. `survey-risk-checklist.md`
6. `system-validation-checklist.md`

### 作用
- 補齊非 NLP 題的設計支持
- 幫 prototype 題補驗證骨架
- 幫社會議題題補止血機制

## 第 3 批：跨 skill 整合
7. `corpus-reuse-guide.md`
8. 更新 `SKILL.md`

### 作用
- 讓 research-playbook 不會孤立運作
- 把 writer / corpus skill 串成明確路徑

---

## 五、每個檔案的完成標準

## `nlp-public-text-playbook.md`
完成標準：
- 能直接幫人把「我想做假訊息」收斂成研究設計
- 有資料來源、標註、baseline、評估、限制
- 不只列題目，而是能走完整流程

## `strong-vs-weak-competition-patterns-v2.md`
完成標準：
- 能拿來快速審題
- 能指出哪裡弱，不只是貼標籤說弱
- 能給出補強方向

## `method-design-pack.md`
完成標準：
- 不是問答清單而已，而是 decision support
- 能讓 agent 依研究類型挑方法

## `survey-risk-checklist.md`
完成標準：
- 明確指出問卷何時足夠、何時不夠
- 提供至少 4 種補強手段

## `system-validation-checklist.md`
完成標準：
- 能把「做出來了」提升成「證明它有效」
- 能覆蓋 app、網站、偵測器、IoT 原型

## `corpus-reuse-guide.md`
完成標準：
- 能讓使用者安全借鏡 corpus，而不是撞題或複製

---

## 六、和另外兩個 skill 的分工

## 跟 `small-paper-writer` 的分工

### 這個 skill 負責
- 題目是否值得做
- 研究設計是否站得住
- 資料與方法如何選
- 問卷 / NLP / prototype 哪條路比較合理

### writer skill 負責
- 章節怎麼寫
- 文獻探討怎麼組
- 引用怎麼整理
- 文風怎麼自然化
- 頁數怎麼壓

### 實務 handoff 時機
當使用者已經有：
- 題目
- 資料來源
- 方法
- 大致結果方向

就應轉去 writer skill。

## 跟 `high-school-info-essay-research` 的分工

### 這個 skill 負責
- 判斷怎樣的題目值得做
- 根據題型設計研究骨架

### corpus skill 負責
- 提供語料證據
- 找同類型例子
- 說明哪種作品常見、哪種容易撞題
- 幫忙找 imitation target

### 實務 handoff 時機
當使用者在問：
- 這題是不是太多人做？
- 有沒有得獎範例？
- 哪一類題比較有機會？

就應轉去 corpus skill。

---

## 七、建議的 agent 使用腳本

當 agent 套用這個 skill，可照下面順序：

1. 先判斷題目屬於哪一型
   - NLP / 公開文字
   - 問卷 / 社會觀察
   - 系統 / prototype
   - 演算法 / 比較

2. 先用 `strong-vs-weak-competition-patterns-v2.md` 做初篩
   - 是否太大
   - 是否只有問卷
   - 是否缺 baseline
   - 是否能量化

3. 如果是 NLP 題
   - 進 `nlp-public-text-playbook.md`
   - 直接幫對方收斂到資料 / 標籤 / baseline / 指標

4. 如果不是 NLP 題
   - 用 `method-checklist.md`
   - 之後切到更完整的 design / validation pack

5. 若需要例子或得獎趨勢
   - 轉 corpus skill

6. 若題目已定、要進入寫作
   - 轉 writer skill

---

## 八、最重要的設計原則

## 原則 1：SKILL.md 保持短，但分流要強
不要把所有內容塞回 SKILL.md。正確做法是：
- SKILL.md 只放 workflow 與 routing
- 具體內容放 references

## 原則 2：每份 reference 都要能被單獨讀懂
不能只寫成補充說明。每份 reference 都要像可以獨立拿來工作的手冊。

## 原則 3：少講抽象原則，多給決策規則
例如不要只說：
- 題目要聚焦

而要說：
- 樣本先做 500-5000
- 類別先做 2-5 類
- 一篇只做 1 個核心任務

## 原則 4：永遠把題目拉回證據鏈
任何題目都回到這六件事：
- 問題
- 資料
- 方法
- 比較
- 結果
- 限制

只要其中缺兩三項，通常就要提醒風險。

---

## 九、下一步最實際的行動

如果要繼續做 v2，建議照這個順序：

### 下一個最值得做的檔案
1. `method-design-pack.md`
2. `survey-risk-checklist.md`
3. `system-validation-checklist.md`
4. 更新 `SKILL.md`

### 更新 `SKILL.md` 時至少要改的點
- 加入分流
- 明確引用新的 v2 檔案
- 加一句：需要 corpus 例子時轉 `high-school-info-essay-research`
- 加一句：需要開始寫作時轉 `small-paper-writer`

---

## 十、最終判斷

如果 v2 只新增少數檔案，最有價值的就是：
- 一份能把公開文字題做成真的研究的 playbook
- 一份能快速判斷題目強弱的 competition pattern guide
- 一份能維持後續擴充順序的 roadmap

這三份補上後，這個 skill 就會從「有方向感的提醒」升級成「真的能幫人定題與避坑的 planning 工具」。