# Anti-AI Signal Hardening

Use this when a draft sounds too generic, too even, or too detached from the actual work. The goal is not to "beat detectors." The goal is to make genuine human authorship visible through specific evidence, honest limits, and natural student-researcher judgment.

## Core rule
- Do not falsify sources, data, process, or authorship.
- Do not add fake personal stories or fake implementation details.
- Do not promise that any wording change will bypass AI detection.
- Rewrite toward truth, specificity, and evidential fit.

## What usually creates AI-like signals
- background sections that stay broad and world-scale for too long
- literature review that reads like stacked encyclopedia summaries
- repeated abstract benefit words: 提升效率, 優化體驗, 重要價值, 深遠影響
- paragraphs with identical cadence and overly smooth transitions
- conclusions that praise significance without returning to actual findings
- claims that sound larger than the method, sample, or prototype can support

## Ethical hardening moves

### 1. Replace generic background with the actual trigger
Prefer the real reason the topic started:
- class exposure
- campus observation
- family need
- specific news case
- a technical problem encountered during practice

Better pattern:
- 先交代具體情境
- 再說觀察到的問題
- 最後導向研究目的

Example shift:
- Weak: 隨著人工智慧快速發展，相關技術已深刻影響社會各層面。
- Better: 我們在資訊課接觸到影像辨識後，發現校園場景中的辨識條件和教學範例差很多，例如光線與背景都更不穩定，因此想進一步測試它在實際情境下的可行性。

### 2. Ground every abstract benefit in a concrete scene
If the draft says a system improves something, specify:
- for whom
- in which step
- compared with what
- under what condition

Example shift:
- Weak: 本系統可提升效率並優化使用體驗。
- Better: 本系統可減少使用者在查詢校內資訊時重複切換頁面的次數，讓常用功能集中在同一介面完成。

### 3. Make literature review serve later decisions
Do not let literature review become detached background filling.
After defining or citing a concept, add a bridge sentence such as:
- 綜合上述文獻可知______，因此本研究選擇______。
- 由前述比較可知______較符合本研究的場域限制，故後續方法採用______。

A good literature paragraph should help explain:
- why this method was chosen
- why this variable matters
- why this scope is reasonable

### 4. Show method reality with exact nouns
Name the actual things touched in the project:
- software and platform names
- model versions
- device types
- dataset counts
- questionnaire counts
- train/test split
- workflow order
- restricted conditions

Strong authenticity signals:
- Python, Colab, VS Code, Roboflow, Arduino, Unity
- 120 張影像、84 份問卷、7:3 切分
- 在教室走廊與室內白光環境下測試

If a detail is unknown, do not invent it. Either verify it or keep the wording general but honest.

### 5. Vary sentence rhythm without becoming messy
Human student writing is usually not perfectly symmetrical.
Use a mix of:
- medium explanatory sentences
- short conclusion sentences
- one denser technical sentence when needed

Good pattern:
- describe the step
- note one observed effect
- add a short limit sentence

Avoid:
- every sentence having the same length
- every paragraph ending with the same style of summary
- repeated transitions like 此外、另外、再者 in every paragraph

### 6. Keep calibrated judgment, not flat neutrality or overclaiming
Prefer moderate claims:
- 具有一定可行性
- 在本次測試下表現較佳
- 可作為初步參考
- 仍需進一步驗證

Avoid inflated claims:
- 證明了重大價值
- 完全解決問題
- 具有革命性意義

Match claim strength to evidence strength.

### 7. Preserve student-researcher voice
The target voice is formal but still recognizably written by a real student team.
Safe voice markers:
- 我們發現
- 本組在實作過程中觀察到
- 本研究進一步比較後發現
- 透過本次研究，我們更了解______

Do not overdo first person, but do not sterilize the draft so much that it sounds machine-flat.

### 8. Admit real limitations
Concrete limitations often make the writing more credible than polished self-praise.
Useful categories:
- sample size small
- collection period short
- one-class or one-school scope only
- lighting / angle / background interference
- hardware limits
- free-tool or platform restrictions
- unstable model performance in more complex scenes

Good pattern:
- state what worked
- state the specific limit
- state one realistic future improvement

Example:
- 本研究完成了初步系統建置，結果顯示其在單一場域中具有一定可行性，但受限於測試樣本數與光線條件，結果仍可能隨場景改變而波動。

### 9. Keep conclusions narrower than the evidence
A conclusion should answer the stated purposes, not expand into a speech.
Check:
- Did the result section really support this sentence?
- Is the conclusion broader than the sample or method allows?
- Does the ending mention actual findings rather than only importance?

## Fast manual rewrite checklist
Before final delivery, check whether the draft has:
- a real topic trigger instead of a giant generic opening
- bounded purposes that match the method
- literature paragraphs with method-bridge sentences
- exact method nouns and counts where available
- result-first reporting before interpretation
- 1 to 3 concrete limitations
- fewer abstract praise words and more scene-based wording
- some natural variation in sentence and paragraph length
- a formal but still human student voice
- no fake citations, fake details, or false authorship framing

## Safe process note
If authorship might be questioned, keep:
- outline notes
- source collection notes
- intermediate drafts
- revision traces showing how evidence and wording evolved

These records support genuine authorship. They are better than trying to game detectors.

## Bottom line
The strongest way to reduce AI-like signals is not concealment. It is to write like someone who actually did the work:
- specific about why the topic was chosen
- concrete about what was done
- careful about what the evidence can support
- honest about what remains limited
- clean about citation and authorship