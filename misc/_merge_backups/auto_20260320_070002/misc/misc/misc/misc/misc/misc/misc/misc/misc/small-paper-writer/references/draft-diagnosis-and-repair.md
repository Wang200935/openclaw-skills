# Draft Diagnosis and Repair

Use this when a small-paper draft already exists but feels weak, generic, or unreliable. Read the draft by symptoms first, then repair the real problem instead of only paraphrasing surface wording.

The main rule is simple:

**Do not ask "How do I make this sound smarter?" Ask "What exactly is broken in the evidence, structure, or voice?"**

A believable revision usually comes from diagnosing the failure mode correctly.

---

## How to use this file

For each weak section:
1. identify the dominant symptom
2. check the diagnosis signs
3. confirm what the section is actually missing
4. apply the matching repair actions
5. rewrite with narrower, more concrete claims

If multiple symptoms appear together, fix them in this order:
1. evidence and claim mismatch
2. missing method detail
3. literature review detachment
4. generic wording
5. fake-academic tone

---

## 1. Failure mode: too generic

This is one of the most common weak-draft patterns. The paper sounds smooth, but after reading a paragraph, the judge still does not know what the team actually saw, used, collected, or found.

### Diagnosis signs
- the opening stays at trend level for too long
- many sentences could fit almost any topic if key nouns were swapped
- repeated phrases like 提升效率, 優化體驗, 重要性, 深遠影響, 創新應用
- claims mention benefits but not who benefits, in which step, or compared with what
- the draft has almost no counts, named tools, scenes, datasets, or concrete constraints
- motivation sounds like "society is changing rapidly" instead of a real trigger

### What is actually broken
Usually the paper is missing one or more of these:
- a real topic trigger
- exact nouns for the method or setting
- result details tied to actual observations
- limits that show the team understands scope

### Repair actions
- replace broad background with the actual trigger that started the topic
- replace abstract nouns with scene-specific nouns
- name the actual tool, platform, dataset, device, class, or environment
- after every benefit word, add: for whom, in which step, under what condition
- add one or two concrete limits so the prose stops sounding like promotion copy
- shorten trend background and move faster to the team's observed problem

### Rewrite moves
- Weak: 近年來人工智慧快速發展，對教育與社會帶來深遠影響。
- Better: 我們在資訊課接觸到影像辨識後，發現教學範例多半是在乾淨背景下測試，但校園實際場景的光線與背景差異較大，因此想進一步比較模型在真實拍攝條件下的表現。

- Weak: 本系統可提升效率並優化使用者體驗。
- Better: 本系統將常用查詢功能集中在同一頁面，能減少使用者來回切換頁面的次數，對校內資訊查找這類重複操作較有幫助。

### Fast self-check
If you can paste the paragraph into another topic with only noun replacement, it is still too generic.

---

## 2. Failure mode: literature review reads like pasted summaries

This is the "one source, one paragraph, one abstract" problem. The section may look full, but it does not help the paper make any decision.

### Diagnosis signs
- each paragraph starts with 作者或文獻指出 and then restates source content
- sources are introduced one by one with no grouping or comparison
- the literature section never says why those sources matter for this study
- there is no bridge sentence from literature to method
- the section reads like a reference report, not support for the paper's design
- after reading it, the judge still cannot tell why the team chose this variable, tool, or method

### What is actually broken
Usually the literature review is missing:
- thematic grouping
- comparison between sources
- a visible research gap
- a bridge from prior work to this study's design

### Repair actions
- regroup sources by theme, method, conclusion, or limitation
- cut repeated abstract-like summaries
- after each mini-group, add one sentence explaining what the group implies for this study
- add explicit bridge lines such as:
  - 綜合上述文獻可知______，因此本研究選擇______。
  - 由前述比較可知______較符合本研究需求，故後續方法採用______。
- end the literature review with a gap statement, not just a recap
- distinguish clearly between "others found" and "this study will do"

### Rewrite pattern
Instead of:
- source A summary
- source B summary
- source C summary

Use:
- first explain the concept category
- then compare 2 to 3 relevant approaches
- then state what limitation or gap remains
- then explain why your study focuses on one method, one variable, or one scenario

### Fast self-check
Ask: if I delete all citation names, would the section still show a logical comparison and lead naturally to the method? If not, it is still a pasted-summary review.

---

## 3. Failure mode: weak method section

A weak method section makes the whole paper feel untrustworthy, even when the topic is good. In student papers, method realism is one of the strongest authenticity signals.

### Diagnosis signs
- the section says "we used questionnaire / system development / analysis" but gives no workflow
- tools are unnamed or only described vaguely
- no sample size, image count, response count, split ratio, or test scope
- no explanation of how data were collected, labeled, compared, or evaluated
- the method sounds shorter and flatter than the introduction
- the reader cannot imagine repeating the study roughly from the description

### What is actually broken
Usually the draft is missing:
- procedural order
- concrete tool and dataset nouns
- quantities and scope
- evaluation criteria
- tested conditions and limitations

### Repair actions
- rewrite the method as steps: first, next, finally
- name the actual software, platform, hardware, model, form tool, or environment if known
- add quantities such as number of samples, number of respondents, date range, split ratio, or test rounds
- explain what was compared and by what standard
- state the testing condition, not only the task goal
- if the method is actually simple, write it honestly but specifically instead of trying to make it sound advanced

### Useful sentence patterns
- 本研究採用______法，研究流程分為以下幾個步驟。
- 首先，我們蒐集______；接著，使用______進行______；最後，以______作為比較依據。
- 問卷共回收______份，有效問卷為______份。
- 影像資料共______張，依______比例進行切分。
- 測試主要在______條件下進行，因此結果仍受______影響。

### Fast self-check
After reading the method, can a teacher roughly explain what the team actually did in order? If not, the section is still too weak.

---

## 4. Failure mode: overclaiming conclusion

This is when the conclusion sounds larger than the study. It usually happens when the team wants the ending to sound impressive, so the final claims outrun the data.

### Diagnosis signs
- words like 證明, 完全解決, 顯著改善, 最佳方法, 可全面推廣 appear without matching evidence
- questionnaire findings become claims about real behavior or social causation
- one-school or one-class results become statements about all students
- a small prototype becomes proof of real-world effectiveness
- conclusion paragraphs mention significance more than actual findings
- limitations are symbolic, vague, or tucked away in one sentence

### What is actually broken
Usually the evidence chain is broken:
- question -> data -> method -> result -> limitation -> claim

The draft jumps from local findings to big conclusions without respecting scope.

### Repair actions
- shrink the claim until it matches the data source and test scope
- replace causal language with descriptive or sample-bounded language when needed
- restate one real finding before any implication sentence
- add one explicit limit before the final value statement
- prefer "within this study" or "in this sample" wording when the scope is narrow
- end with a realistic next step instead of a victory speech

### Rewrite moves
- Overclaimed: 本研究證明短影音會嚴重降低學生的學習專注力。
- Better: 根據本研究問卷結果，多數受試者認為短影音使用與自身專注狀況有關，但本研究以自陳資料為主，無法直接證明實際學習表現下降。

- Overclaimed: 本研究顯示本模型為最佳方法。
- Better: 在本研究所使用的資料與評估方式下，該模型的表現相對較佳，但是否適用於其他資料情境仍需進一步測試。

### Fast self-check
Circle every strong conclusion verb. For each one, point to the exact evidence. If you cannot do that, the claim must become smaller.

---

## 5. Failure mode: questionnaire overreach

This is a special type of overclaim and appears very often in school papers. The draft treats a survey as if it proved real effects, causation, or population-wide truth.

### Diagnosis signs
- the paper uses self-reported answers to claim actual behavioral change
- respondents' perceptions are written as objective social facts
- convenience sampling is used, but conclusions refer to all teenagers or all students
- questionnaire data are used to justify policy-level claims
- terms like 影響、導致、改善 are used as if the survey directly measured them

### What a questionnaire can usually support
- attitudes
- preferences
- self-reported habits
- perceived influence
- differences inside this sample

### What a questionnaire usually cannot support by itself
- strong causation
- actual improvement in performance
- real-world intervention effectiveness
- nationwide or generation-wide claims
- certainty about policy necessity

### Repair actions
- change claims from factual proof to sample-based reporting
- add scope markers: 本研究樣本中, 受訪者認為, 問卷結果顯示, 受試者自述
- state the sampling limit clearly
- if the study needs stronger claims, move them into suggestion or future research, not conclusion fact
- separate "what respondents felt" from "what actually happened"

### Rewrite moves
- Overclaimed: 本研究顯示 ChatGPT 能大幅提升學生學習效率。
- Better: 在本研究樣本中，許多受訪者表示 ChatGPT 有助於節省查詢與整理資料的時間，但本研究主要測量使用感受，未直接檢驗成績或長期學習成效。

- Overclaimed: 本研究證明社群媒體會對青少年造成負面心理影響。
- Better: 問卷結果顯示，多數受訪者認為社群媒體使用與情緒或專注狀況有一定關聯，但本研究無法僅憑此資料直接證明心理影響的因果關係。

### Fast self-check
Replace every sentence that sounds like "the questionnaire proved" with "the respondents in this sample reported." If that changes the meaning too much, the original claim was too large.

---

## 6. Failure mode: demo-only system claims

This happens when a paper built something real, but the writing confuses "it runs" with "it has been validated thoroughly." The implementation may be real, yet the claim level is still too big.

### Diagnosis signs
- the paper has screenshots and interface descriptions but little evaluation
- a successful test example is treated as proof of practical deployment
- there is no baseline, error analysis, or failure-case discussion
- the result section focuses on completion of development more than measured performance
- conclusion uses phrases like 可廣泛應用, 可有效解決, 可直接導入 without field testing
- real testing conditions are not clearly described

### What a demo really shows
Usually it shows:
- the team completed implementation
- the workflow is feasible in tested conditions
- the idea can run at least at prototype level

It does not automatically show:
- robustness
- generalizability
- real-world adoption
- superiority over alternatives
- stable accuracy in complex environments

### Repair actions
- downgrade "effective solution" language to "initial feasibility" language
- describe the exact tested condition and scale
- add at least one failure case or unstable condition
- if no baseline exists, do not write as if performance leadership was proven
- separate implementation success from validation strength
- use practical potential wording instead of solved-problem wording

### Safer sentence patterns
- 本研究完成了______系統的初步建置。
- 在本次測試條件下，系統能完成______任務，顯示其具有一定可行性。
- 然而，若面對______情境，系統表現仍可能受影響。
- 因此，本研究成果較適合作為初步驗證，而非直接視為成熟應用。

### Rewrite move
- Overclaimed: 本系統可有效解決零售貨架管理問題。
- Better: 本研究建置的系統在團隊設定的測試環境下可辨識目標品項，顯示其作為貨架管理輔助工具具有初步可行性，但在不同光線、拍攝角度與較複雜場景下仍需進一步驗證。

### Fast self-check
Ask: did we prove that it works widely, or only that it worked here? Write the smaller answer.

---

## 7. Failure mode: fake-academic tone

This is the tone problem where the draft tries too hard to sound scholarly. It often makes the paper feel more synthetic, not more credible.

### Diagnosis signs
- lots of inflated words but little concrete content
- phrases sound like journal imitation rather than student reporting
- every paragraph ends with a polished claim about significance
- the draft avoids simple direct sentences even when they would be clearer
- the team disappears completely from the prose, making the paper sound detached and machine-flat
- limitations are framed defensively, like minor flaws in an otherwise groundbreaking study

### High-risk wording patterns
- 具有深遠影響
- 展現重大價值
- 具革命性意義
- 全面提升
- 顯著優化
- 本研究之學術貢獻極具參考價值

### What is actually broken
Usually the draft is trying to gain authority through tone instead of evidence. The problem is not "not academic enough." The problem is lack of grounded student-researcher voice.

### Repair actions
- replace inflated evaluative phrases with plain factual statements
- allow direct wording such as 我們發現, 本研究結果顯示, 在實作過程中
- vary rhythm: one technical sentence, one direct observation, one short limit sentence
- cut ceremonial transitions that add no meaning
- rewrite limitations as specific constraints, not ritual humility
- keep formal structure, but let the draft sound like a real team reporting work they actually did

### Rewrite moves
- Fake-academic: 本研究成果不僅具備重要學術價值，亦對相關領域之未來發展具有深遠啟發。
- Better: 本研究完成了______的初步分析／實作，結果可作為後續研究與改進的參考，但其適用範圍仍受樣本與測試條件限制。

- Fake-academic: 雖然本研究仍存在些微不足，然整體而言已充分展現高度應用潛力。
- Better: 雖然本研究已完成初步測試，但樣本數與測試場域仍有限，因此若要進一步討論實際應用，仍需補充更多情境驗證。

### Fast self-check
If a sentence sounds impressive but could survive even after deleting all results and method details, it is probably fake-academic filler.

---

## Combined repair patterns

In real drafts, these failure modes often appear together.

### Pattern A: generic opening + fake-academic tone
Fix by:
- cutting 30 to 50 percent of broad background
- inserting the real trigger earlier
- replacing praise words with observed problems and scoped purpose

### Pattern B: literature review summaries + weak method
Fix by:
- rewriting literature by theme
- adding bridge sentences that justify the chosen method
- expanding method with steps, tools, counts, and evaluation basis

### Pattern C: questionnaire overreach + overclaiming conclusion
Fix by:
- changing all strong causal claims to sample-based interpretation
- adding sampling limitations clearly
- rewriting conclusion to match self-reported evidence only

### Pattern D: demo-only system claims + fake-academic ending
Fix by:
- separating implementation success from effectiveness proof
- adding tested conditions and failure cases
- replacing grand closing rhetoric with feasibility + limit + future improvement

---

## One-pass diagnosis checklist

Before revising, mark Yes or No:
- Does the paper mention a real topic trigger?
- Does the literature review compare and bridge into method?
- Does the method include tools, steps, counts, and scope?
- Do the results describe actual observations before interpretation?
- Does the conclusion stay within the evidence chain?
- Does the questionnaire section avoid causal overreach?
- Does the system section avoid confusing demo with validation?
- Does the tone sound like a real student team rather than fake-academic imitation?

If 3 or more answers are No, do not do only sentence polishing. Rebuild the weak section structure first.

---

## Bottom line

The best repair is usually not a more advanced sentence.
It is a more honest one.

A strong small-paper draft sounds like this:
- the team had a real reason to study the topic
- the literature helped them choose a path
- the method shows what they actually did
- the results stay close to what they actually observed
- the conclusion is smaller than the ambition, but stronger than empty hype

That is what makes a student paper believable.