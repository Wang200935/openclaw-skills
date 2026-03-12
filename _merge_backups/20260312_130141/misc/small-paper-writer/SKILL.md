---
name: small-paper-writer
description: Write or revise Taiwanese high-school small papers / research essays from outline to final draft. Use when the task is to turn a chosen topic and research plan into a structured paper, improve section writing, tighten literature review, fit likely school/contest formatting, humanize overly generic prose, reduce obvious AI-writing signals, or polish abstracts, conclusions, and references.
---

# Small Paper Writer

Turn an existing topic or research plan into a defensible, student-sounding small paper.

## Core workflow

1. Confirm the paper state first: topic ideation, outline, partial draft, or near-final revision.
2. If the topic, data source, or method is still unstable, stop full drafting and send the user back to `small-paper-research-playbook`.
3. When format rules are unknown, use a conservative default structure and follow `references/format-uncertainty-policy.md`.
4. Build or repair the paper in this order:
   - title
   - abstract
   - keywords
   - introduction / research motivation
   - literature review
   - method
   - findings / analysis
   - conclusion
   - references
5. Keep every section tied to actual evidence, method details, and realistic limitations.
6. Before delivery, run a humanization pass so the paper sounds like a real student team that actually did the work.

## Default structure

Use this default unless the user provides official rules:

- Title
- Abstract
- Keywords
- Introduction / research motivation
- Literature review
- Research method
- Findings / analysis
- Conclusion and suggestions
- References

## Non-negotiable writing rules

- Do not invent citations, page numbers, datasets, experiments, or results.
- Do not let the conclusion claim more than the evidence supports.
- Keep literature review separate from the paper's own findings.
- Prefer concrete nouns, measured observations, and named tools over inflated academic filler.
- Treat AI-rate reduction as a naturalization task, not a promise of bypassing detection.
- If the draft still lacks real method detail, missing sources, or fake-looking generalities, fix that root problem instead of only paraphrasing sentences.

## Routing guide: read only what is needed

### For structure and section drafting
Read `references/section-templates.md`.

### For format and page planning
Read:
- `references/format-guide.md`
- `references/format-pack.md`
- `references/page-budget.md`
- `references/format-uncertainty-policy.md` when rules are missing or unclear

### For literature review quality
Read `references/literature-review-guide.md`.

### For citation safety and reference cleanup
Read `references/citation-hygiene.md`.

### For making the prose less generic
Read:
- `references/anti-generic-writing.md`
- `references/writing-patterns-from-corpus.md`

### For human student voice and final authenticity pass
Read:
- `references/human-student-voice-checklist.md`
- `references/naturalization-rewrite.md`

### For stronger anti-AI-signal rewriting
Read only if the user explicitly wants lower detectability or the prose sounds obviously synthetic:
- `references/anti-ai-signal-hardening.md`
- `references/ai-rate-reduction-notes.md`

## Handoff rule

If the user is still choosing a topic, narrowing the research question, deciding whether a questionnaire-only design is too weak, or figuring out data/method/evaluation, switch to `small-paper-research-playbook` before writing full prose.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\misc\small-paper-writer\SKILL.md
---
---
name: small-paper-writer
description: Write or revise Taiwanese high-school small papers / research essays from outline to final draft. Use when the task is to turn a chosen topic and research plan into a structured paper, improve section writing, tighten literature review, fit likely school/contest formatting, humanize overly generic prose, reduce obvious AI-writing signals, or polish abstracts, conclusions, and references.
---

# Small Paper Writer

Turn an existing topic or research plan into a defensible, student-sounding small paper.

## Core workflow

1. Confirm the paper state first: topic ideation, outline, partial draft, or near-final revision.
2. If the topic, data source, or method is still unstable, stop full drafting and send the user back to `small-paper-research-playbook`.
3. When format rules are unknown, use a conservative default structure and follow `references/format-uncertainty-policy.md`.
4. Build or repair the paper in this order:
   - title
   - abstract
   - keywords
   - introduction / research motivation
   - literature review
   - method
   - findings / analysis
   - conclusion
   - references
5. Keep every section tied to actual evidence, method details, and realistic limitations.
6. Before delivery, run a humanization pass so the paper sounds like a real student team that actually did the work.

## Default structure

Use this default unless the user provides official rules:

- Title
- Abstract
- Keywords
- Introduction / research motivation
- Literature review
- Research method
- Findings / analysis
- Conclusion and suggestions
- References

## Non-negotiable writing rules

- Do not invent citations, page numbers, datasets, experiments, or results.
- Do not let the conclusion claim more than the evidence supports.
- Keep literature review separate from the paper's own findings.
- Prefer concrete nouns, measured observations, and named tools over inflated academic filler.
- Treat AI-rate reduction as a naturalization task, not a promise of bypassing detection.
- If the draft still lacks real method detail, missing sources, or fake-looking generalities, fix that root problem instead of only paraphrasing sentences.

## Routing guide: read only what is needed

### For structure and section drafting
Read `references/section-templates.md`.

### For format and page planning
Read:
- `references/format-guide.md`
- `references/format-pack.md`
- `references/page-budget.md`
- `references/format-uncertainty-policy.md` when rules are missing or unclear

### For literature review quality
Read `references/literature-review-guide.md`.

### For citation safety and reference cleanup
Read `references/citation-hygiene.md`.

### For making the prose less generic
Read:
- `references/anti-generic-writing.md`
- `references/writing-patterns-from-corpus.md`

### For human student voice and final authenticity pass
Read:
- `references/human-student-voice-checklist.md`
- `references/naturalization-rewrite.md`

### For stronger anti-AI-signal rewriting
Read only if the user explicitly wants lower detectability or the prose sounds obviously synthetic:
- `references/anti-ai-signal-hardening.md`
- `references/ai-rate-reduction-notes.md`

## Handoff rule

If the user is still choosing a topic, narrowing the research question, deciding whether a questionnaire-only design is too weak, or figuring out data/method/evaluation, switch to `small-paper-research-playbook` before writing full prose.

