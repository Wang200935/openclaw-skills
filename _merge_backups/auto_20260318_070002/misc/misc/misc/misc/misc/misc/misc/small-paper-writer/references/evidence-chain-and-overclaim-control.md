# Evidence Chain and Overclaim Control

This guide is derived from the 404-paper corpus review, the chunk audits, and repeated judging patterns across the small-paper set.

The stable lesson is simple:

**The papers that look strongest are usually not the ones with the flashiest title. They are the ones whose claims stay proportional to their evidence.**

A small paper does not need to sound huge. It needs to sound believable.

---

## Core rule

Before writing any conclusion sentence, check whether your paper has this chain:

**question -> data -> method -> result -> limitation -> claim**

If one link is weak, the final claim must become smaller.

### Safe writing logic
- If you only have a questionnaire, write about **responses, tendencies, and perceptions**.
- If you have a prototype plus small testing, write about **feasibility, initial performance, and practical problems**.
- If you have a real dataset, clear method, comparison, and metrics, you can write about **measured effectiveness within this study's scope**.

### Dangerous writing logic
- big social topic -> small convenience sample -> sweeping conclusion
- simple demo -> “solves” a real-world problem
- one school / one class data -> conclusions about all students
- one model run -> claim that one method is “best” in general

---

## 1. What an evidence chain looks like in a student paper

A usable evidence chain usually includes:
- a specific problem
- a visible data source
- a method someone else could roughly repeat
- an observed result
- at least one limit or uncertainty
- a conclusion that does not go beyond those parts

### Strong example
- We collected 214 comments from a defined platform and time range.
- We labeled them by a stated rule.
- We compared model A and model B.
- Model A performed better on this dataset.
- However, slang and sarcasm still caused errors.
- Therefore, in this study, model A was more suitable for this task.

### Weak example
- We care about cyberbullying.
- We trained an AI model.
- The model performed well.
- Therefore, our system can effectively solve online bullying.

The second version jumps from a local result to a social solution. That is exactly the kind of overclaim that the corpus repeatedly exposed.

---

## 2. The most common overclaim patterns from the corpus

Across chunks, the same weak patterns kept showing up:

### A. Hot topic + questionnaire + oversized conclusion
Common topics:
- AI impact
- social media influence
- short-video addiction
- metaverse attitudes
- fraud awareness
- consumer behavior

Common problem:
- the paper measures opinions, but writes as if it proved real effects or causal mechanisms

### B. Tool implementation + little testing + “problem solved” language
Common topics:
- recognition systems
- recommendation systems
- educational apps
- security tools
- game systems
- helper bots

Common problem:
- the paper shows that something runs, but not that it works reliably in realistic conditions

### C. Trend summary + borrowed terminology + fake depth
Common problem:
- the draft uses words like AI, blockchain, RAG, cybersecurity, optimization, or deep learning, but the evidence is still just literature notes, screenshots, or concept explanation

### D. Nice result screenshot + no baseline
Common problem:
- the system output looks good, but there is no comparison, no error count, no before/after, and no explanation of failure cases

---

## 3. Keep claims proportional to evidence

Use the table below mentally when drafting.

### If your evidence is questionnaire only
You may claim:
- respondents' preferences
- respondents' attitudes
- self-reported habits
- perceived influence
- descriptive trends in this sample

You should avoid claiming:
- actual causation
- psychological harm as proven fact
- long-term social effects
- national or generation-wide conclusions
- policy certainty

### Safer wording
- According to the questionnaire results, most respondents believed...
- Within this sample, students tended to...
- The responses suggest that...
- This study found a perceived association between A and B.

### Dangerous wording
- This proves that...
- This shows A causes B.
- Modern teenagers are all...
- Society has already been seriously affected by...
- This phenomenon will definitely continue to worsen...

---

## 4. Questionnaire overreach: the exact trap to avoid

The corpus repeatedly showed that many weaker papers followed this line:

**big issue -> school survey -> broad social conclusion**

That is not automatically wrong, but it becomes weak when the paper forgets what the questionnaire can actually support.

## What a questionnaire can do well
- describe current awareness
- compare preferences between groups in your sample
- show how students report their own usage or opinions
- support a system paper with user feedback

## What a questionnaire usually cannot do by itself
- prove real behavioral change
- prove social harm or educational damage
- prove one tool truly improves learning outcomes
- prove one public policy is necessary
- represent all Taiwanese high-school students

## Rewrite pattern

### Overclaimed
This study proves that short-form video seriously reduces students' learning concentration.

### Better
Based on the questionnaire results, many respondents reported that they felt short-form video affected their concentration. However, because this study relied on self-reported data from a limited sample, it cannot directly prove actual learning decline.

### Overclaimed
This study shows that ChatGPT greatly improves student learning efficiency.

### Better
In this sample, many students reported that ChatGPT helped them save time during homework or concept checking. However, this study measured user perception rather than objective score improvement.

---

## 5. Demo-only overclaim: “we built it” is not the same as “it works”

This is another major pattern in the audits.

A lot of papers had:
- a visible interface
- a working app or model
- some screenshots
- one or two successful examples

But then the writing jumped to:
- high practicality
- strong effectiveness
- immediate real-world value
- broad future deployment claims

## What a demo actually proves
A demo usually proves:
- the team completed implementation
- the workflow is feasible at a basic level
- the system can run under tested conditions

## What a demo does not automatically prove
- stable accuracy
- robustness in real environments
- generalizability
- user adoption
- safety
- superiority over alternatives

## Better conclusion language for prototype papers
- The system was able to complete the target task under the tested conditions.
- The prototype showed initial feasibility for this scenario.
- In this small-scale test, the system could identify / classify / respond to...
- The implementation suggests practical potential, but further testing is needed.

## Dangerous conclusion language for prototype papers
- The system can be widely adopted.
- The system solves the problem effectively.
- The model is highly accurate in real-world settings.
- This can replace existing methods.

## Rewrite pattern

### Overclaimed
The inventory recognition system can effectively solve shelf management problems in retail stores.

### Better
The developed system could identify target items in the team's test environment and showed basic feasibility for inventory assistance. However, lighting changes, camera angle differences, and more complex store layouts were not fully tested in this study.

### Overclaimed
Our anti-fraud detection model can prevent online fraud.

### Better
On the dataset used in this study, the model showed some ability to distinguish suspicious cases. However, preventing real fraud would still require more diverse data, real-time testing, and analysis of false positives and false negatives.

---

## 6. The safest claim level for different study types

## A. Literature-heavy paper
Best claim level:
- organized understanding
- comparison of viewpoints
- clarified concepts
- identified possible risks or directions

Do not write as if literature review alone created new empirical proof.

## B. Questionnaire paper
Best claim level:
- sample-based description
- attitude comparison
- self-reported tendencies
- practical suggestions for the observed group

Do not write population-level or causal conclusions unless the design is unusually strong.

## C. Prototype / system paper
Best claim level:
- implementation completed
- workflow feasible
- tested under specific conditions
- has practical potential

Do not confuse “runs successfully” with “validated thoroughly.”

## D. Data-analysis / model-comparison paper
Best claim level:
- comparative performance on the stated dataset
- measurable strengths and weaknesses
- bounded interpretation of metrics

Still avoid writing “best method overall” unless your evaluation is much stronger than a normal student paper.

---

## 7. A quick claim-check before writing conclusions

For every important claim, ask:

1. **What exact evidence supports this sentence?**
2. **Is the evidence opinion, observation, or measured performance?**
3. **How wide is my sample or test scope?**
4. **Would a judge ask for a baseline, control group, or more cases?**
5. **Am I describing what happened, or quietly exaggerating what it means?**

If you cannot answer those questions clearly, shrink the claim.

---

## 8. Honest limitations do not weaken the paper

In the corpus, stronger papers often looked more trustworthy because they admitted limits clearly.

Judges usually know a high-school paper has limits.
What hurts more is pretending those limits do not exist.

## Good limitation topics
- sample size was limited
- respondents came mainly from one school or one grade
- questionnaire used convenience sampling
- test time was short
- images were collected under limited lighting conditions
- model had trouble with noisy, ambiguous, or rare cases
- labeled data may contain subjectivity
- the system was tested only in a simplified environment
- metrics were limited to this dataset
- user experience evaluation was preliminary

## Weak limitation style
- Due to limited time, there were some shortcomings.
- There are still many places for improvement in the future.

These lines are too empty.

## Better limitation style
- Because the questionnaire respondents were mainly from the same school, the results cannot represent all high-school students.
- Since the image data were collected under relatively stable lighting, the system may perform less consistently in more complex environments.
- This study focused on initial prototype completion and small-scale testing, so long-term usability and real-world stability were not fully verified.
- The labels in this study were manually defined by the team, so some subjective judgment may still affect the classification results.

---

## 9. Limitation sentences that still sound like real students

A good student voice is honest, specific, and not fake-professorial.

### Natural student-sounding patterns
- In this study, our sample size was still limited, so the results should be interpreted carefully.
- Because our test environment was relatively simple, the system's performance in real settings still needs further verification.
- We originally hoped to collect more data, but due to time and equipment limits, the current results are better understood as an initial test.
- Although the questionnaire showed a clear tendency, it mainly reflected respondents' self-reported perceptions rather than direct behavioral evidence.
- Our system could complete the task in most test cases, but some errors still appeared in more complex situations.

### Tone to avoid
- This research has groundbreaking significance but still has slight limitations.
- Although there are minor shortcomings, the overall contribution is extremely valuable.

That sounds defensive and inflated.

---

## 10. A practical conclusion formula that rarely goes wrong

When unsure, use this order:

1. say what you actually did
2. say what you actually found
3. say what the result means within this scope
4. state the limit
5. give a realistic next step

### Example formula
This study designed and tested a ______ system / analyzed ______ data / collected ______ questionnaires. The results showed that ______ under the conditions of this study. This suggests that ______ may have practical value for ______. However, because ______, the conclusion should be limited to this scope. In future work, the study could improve ______ by adding ______.

This structure keeps the paper grounded.

---

## 11. Fast rewrites for common overclaim sentences

### 1
Overclaimed: This study proves that AI education tools are highly effective.

Better: In this study, the tested tool showed some usefulness in the selected learning tasks, and many respondents gave positive feedback. However, the study did not directly measure long-term learning outcomes.

### 2
Overclaimed: This system can greatly reduce traffic accidents.

Better: The prototype was able to detect certain target conditions in the test setting, showing initial feasibility for traffic-safety assistance. Its actual effect on accident reduction was not verified in this study.

### 3
Overclaimed: This research shows that social media has serious negative effects on teenagers.

Better: The questionnaire results suggest that many respondents perceived social media as affecting their mood, concentration, or interaction patterns. However, these findings reflect self-reported perceptions within a limited sample.

### 4
Overclaimed: Our model is the best method.

Better: Among the methods compared in this study, our selected model performed better on the current dataset. Whether this advantage remains in other datasets still requires further testing.

### 5
Overclaimed: This project can be directly promoted to schools and society.

Better: This project shows preliminary practical potential, but broader application would still require larger-scale testing, user feedback, and environment-specific adjustment.

---

## 12. Final anti-overclaim checklist

Before submitting, check whether the draft accidentally does any of these:
- uses questionnaire data to claim causation
- uses a one-school sample to represent everyone
- uses a demo to claim real-world effectiveness
- uses one good example to hide failure cases
- says “improve efficiency” without explaining where and how
- says “high accuracy” without giving numbers or comparison
- says “practical value” without describing tested conditions
- writes a huge social conclusion after a very small method
- gives symbolic limitations instead of real ones

If yes, revise the claim downward.

---

## Final reminder

A believable small paper does not need to sound weak.
It just needs to sound exact.

In most school competitions, a modest but well-supported sentence is stronger than an ambitious sentence with no evidence behind it.

**Do not try to make the paper sound bigger than it is. Make it sound like a team that really did the work and understands what its evidence can and cannot say.**
