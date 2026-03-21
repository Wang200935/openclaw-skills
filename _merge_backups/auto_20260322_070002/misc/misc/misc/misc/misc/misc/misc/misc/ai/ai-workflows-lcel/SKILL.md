---
name: ai_workflows_lcel
description: Design or reason about LangChain Expression Language style pipelines where input flows through transforms, models, tools, custom APIs, and outputs in a standard chain. Use when building chained AI workflows, wrappers around custom APIs, or structured prompt-to-output pipelines.
---

# LCEL-style Workflows

Use this skill when composing reusable AI pipelines.

## Core model

Think in stages:
- input
- prompt shaping / transforms
- model or external API call
- post-processing
- output

## Good defaults

- Keep each stage inspectable.
- Prefer explicit data contracts between stages.
- Make external API boundaries easy to stub or swap.
- Separate prompt construction from transport code.
- Log intermediate values for diagnosis, but avoid leaking secrets.

## Use cases

- input -> prompt -> custom API -> parser -> UI
- file -> chunk -> retrieve -> synthesize
- status snapshot -> diagnose -> action plan -> terminal action

## Read next when needed

- `references/patterns.md` for chain patterns



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-workflows-lcel\SKILL.md
---
---
name: ai_workflows_lcel
description: Design or reason about LangChain Expression Language style pipelines where input flows through transforms, models, tools, custom APIs, and outputs in a standard chain. Use when building chained AI workflows, wrappers around custom APIs, or structured prompt-to-output pipelines.
---

# LCEL-style Workflows

Use this skill when composing reusable AI pipelines.

## Core model

Think in stages:
- input
- prompt shaping / transforms
- model or external API call
- post-processing
- output

## Good defaults

- Keep each stage inspectable.
- Prefer explicit data contracts between stages.
- Make external API boundaries easy to stub or swap.
- Separate prompt construction from transport code.
- Log intermediate values for diagnosis, but avoid leaking secrets.

## Use cases

- input -> prompt -> custom API -> parser -> UI
- file -> chunk -> retrieve -> synthesize
- status snapshot -> diagnose -> action plan -> terminal action

## Read next when needed

- `references/patterns.md` for chain patterns









