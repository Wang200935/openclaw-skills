---
name: ai_guardian_lessons
description: Build or repair local AI guardian/watchdog systems for OpenClaw or similar services without repeating common mistakes. Use when creating service guardians, recovery loops, monitoring consoles, or AI-assisted local operations tools.
---

# AI Guardian Lessons

Use this skill when building a local guardian that watches a service, diagnoses failures, repairs safely, and exposes a human-visible control panel.

## Core lessons

1. Do not ship local-only heuristics as if remote AI were already integrated.
2. Prefer remote-AI-first with local fallback, not remote-AI-only.
3. Stop crash loops before making diagnosis smarter.
4. Separate diagnosis, action, and verification visibly.
5. Treat operator visibility as a first-class feature, not polish.

## Required architecture

- health monitor
- bounded recovery policy
- incident state
- cooldown / restart budget
- pause / maintenance modes
- report output
- operator UI

## Hard rules

- Never run unbounded `start -> stop -> start` loops.
- Every recovery step needs a verification gate.
- Keep incident state outside transient conversation text.
- If remote AI fails, degrade to local heuristics and keep operating.
- Do not call the system finished because one recovery succeeded once.

## Read next when needed

- `references/recovery-guards.md`
- `references/ui-lessons.md`
- `references/remote-ai-integration.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-guardian-lessons\SKILL.md
---
---
name: ai_guardian_lessons
description: Build or repair local AI guardian/watchdog systems for OpenClaw or similar services without repeating common mistakes. Use when creating service guardians, recovery loops, monitoring consoles, or AI-assisted local operations tools.
---

# AI Guardian Lessons

Use this skill when building a local guardian that watches a service, diagnoses failures, repairs safely, and exposes a human-visible control panel.

## Core lessons

1. Do not ship local-only heuristics as if remote AI were already integrated.
2. Prefer remote-AI-first with local fallback, not remote-AI-only.
3. Stop crash loops before making diagnosis smarter.
4. Separate diagnosis, action, and verification visibly.
5. Treat operator visibility as a first-class feature, not polish.

## Required architecture

- health monitor
- bounded recovery policy
- incident state
- cooldown / restart budget
- pause / maintenance modes
- report output
- operator UI

## Hard rules

- Never run unbounded `start -> stop -> start` loops.
- Every recovery step needs a verification gate.
- Keep incident state outside transient conversation text.
- If remote AI fails, degrade to local heuristics and keep operating.
- Do not call the system finished because one recovery succeeded once.

## Read next when needed

- `references/recovery-guards.md`
- `references/ui-lessons.md`
- `references/remote-ai-integration.md`











