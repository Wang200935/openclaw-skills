# Naturalization Rewrite

Use this when a draft is structurally correct but sounds too smooth, too broad, or too AI-generic. Rewrite toward a credible Taiwanese high-school student research voice.

## Goal
Make the text read like a real student project report:
- formal enough for a competition paper
- concrete enough to feel lived and built
- modest enough to match the evidence
- uneven enough to sound human, not template-generated

## Core shift
Do not try to sound more academic.
Try to sound more specific, more situated, and more honest.

Bad direction:
- bigger claims
- prettier transitions
- more abstract praise words

Better direction:
- clearer research trigger
- more exact tools, counts, scenes, and constraints
- direct link from literature to method
- conclusions that stop where the evidence stops

## Rewrite moves

### 1. Pull the opening closer to the student's real starting point
Compress world-scale background. Move the actual trigger earlier.

Too generic:
- 隨著人工智慧快速發展，科技已深刻影響各行各業。

Better:
- 我們在資訊課接觸到影像辨識後，發現它不只可以用在大型系統，也可能拿來處理校園中較單純的辨識問題，因此想進一步測試其實際效果。

Use triggers such as:
- class exposure
- club project
- family need
- campus observation
- news event
- repeated inconvenience in daily life

### 2. Replace abstract benefit words with a concrete scenario
Words like these are high risk unless immediately grounded:
- 提升效率
- 優化體驗
- 增加便利性
- 重要價值
- 深遠影響

Rewrite by naming:
- who benefits
- in what step
- what is reduced, improved, or detected
- under what condition

Bad:
- 本系統可提升管理效率。

Better:
- 本系統可減少管理者逐筆檢查資料的時間，尤其在每日需重複確認出缺勤紀錄時較為明顯。

### 3. Turn literature paragraphs into setup for your own choice
Do not end a literature paragraph with a floating summary.
End with why the study adopts, compares, or excludes something.

Weak:
- 由此可知，YOLO 是常見的物件偵測模型。

Better:
- 綜合上述文獻可知，YOLO 在即時偵測上具有速度優勢，因此本研究選擇它作為主要模型，並在校園單一情境下進行初步測試。

### 4. Keep the research purpose at the same scale as the method
If the method is small, keep the purpose small.
Do not write a huge purpose for a limited prototype.

Overstated:
- 探討人工智慧對教育產業之全面影響

Proportional:
- 比較兩種生成式 AI 工具在高中生英文摘要修訂上的實際差異

Safe verbs:
- 了解
- 探討
- 比較
- 分析
- 建立
- 設計
- 實作
- 驗證可行性

### 5. Add the details that only the real writer would know
Concrete details lower AI smell fast.

Useful details:
- tool names
- version names
- dataset size
- questionnaire count
- train/test split
- device limitations
- annotation platform
- failed attempts
- environmental interference

Example:
- 本研究以 312 張自行拍攝影像作為資料來源，其中 250 張作為訓練集，62 張作為測試集，並使用 Roboflow 完成標註。

### 6. Let the results sound measured, not triumphant
Student papers usually sound more credible when they report "usable" or "preliminary" results instead of grand success.

Prefer:
- 具有一定可行性
- 在特定情境下表現較穩定
- 能完成基本功能
- 與預期大致相符
- 仍受某些因素影響

Avoid:
- 證明了
- 徹底改變
- 顯著推動社會進步
- 具有革命性突破

### 7. Keep limitations visible
Limitations are not weakness padding. They are part of the student-paper voice.

Common realistic limits:
- sample size not large enough
- collection time too short
- lighting/background affected recognition
- free-platform restrictions
- hardware performance not enough
- only one school / one class / one scenario

Pattern:
- 雖然本研究已完成______，但仍受______限制，因此結果主要反映______情境下的初步觀察。

### 8. Allow sentence rhythm to vary
Do not make every paragraph equally polished.
A natural student draft often mixes:
- a longer explanatory sentence
- a short observation
- a practical constraint

This is good:
- a technical paragraph can be dense
- a limitation paragraph can be shorter
- a transition can be simple and direct

## Rewrite patterns

### Pattern A: background compression
Before:
- 近年來科技日新月異，數位化與智慧化浪潮席捲全球，並對教育、醫療、交通等領域產生深遠影響。

After:
- 近年來校園中也越來越常接觸到智慧化工具。我們在課堂與新聞中都看見相關應用，因此開始思考，這些工具是否也能處理我們觀察到的實際問題。

### Pattern B: purpose grounding
Before:
- 本研究旨在探討本系統之應用價值與未來發展潛力。

After:
- 本研究主要想了解此系統是否能在目前資料量有限的情況下完成基本辨識，並比較不同設定下的結果差異。

### Pattern C: literature-to-method bridge
Before:
- 根據相關研究可知，深度學習已廣泛應用於影像辨識。

After:
- 根據相關研究可知，深度學習在影像辨識上已有不少應用，因此本研究不再從傳統方法切入，而是直接比較較常見的模型設定在本研究資料上的表現。

### Pattern D: result moderation
Before:
- 實驗結果證明本系統具有高度準確性與實際推廣價值。

After:
- 依本次測試結果來看，本系統在單一場景下已有基本辨識能力，但在背景複雜或光線不穩時，結果仍容易受影響。

### Pattern E: honest conclusion
Before:
- 本研究成果可作為未來智慧社會發展的重要基礎。

After:
- 本研究完成了系統雛形與初步測試，能作為後續改良的起點，但若要實際應用，仍需擴充資料量並改善穩定度。

## Quick anti-generic checklist
Before finalizing, check whether the draft:
- starts from a real student trigger instead of a giant era statement
- names the exact object, tool, sample, or scene
- keeps each purpose matched to an actual method
- ends literature sections with a research decision
- reports results conservatively
- includes real limitations
- sounds like a student who did the work, not a narrator above the work

## Fast rewrite recipe
If a paragraph feels fake, do this in order:
1. delete one sentence of broad background
2. add one real scene or origin point
3. replace one abstract noun with a concrete object or action
4. add one method detail or constraint
5. soften one oversized claim
6. end with what this means for the paper, not for the whole world
