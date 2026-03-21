---
name: ai_guardian_builder
description: Build local AI guardian tools that monitor a service, diagnose failures, run terminal-based recovery steps, and expose an operator UI. Use when creating watchdogs, service guardians, repair loops, or AI-assisted local operations panels for OpenClaw or similar systems.
---

# AI Guardian Builder

Use this skill when building a local guardian/ops agent.

## Core architecture

1. Health monitor loop
2. Snapshot collection
3. Diagnosis stage
4. Recovery stage
5. Verification stage
6. Operator-visible UI and logs

## Hard rules

- Never hide actions; show what was checked and what command was run.
- Separate diagnosis from repair.
- Verify after every repair attempt.
- Keep logs structured and human-readable.
- If remote AI is unavailable, degrade gracefully to local diagnostics instead of failing closed.

## Preferred local stack

- Python for process control and orchestration
- subprocess for terminal actions
- lightweight local web UI for visibility
- markdown or JSON reports for incident history

## Recovery pattern

observe -> snapshot -> diagnose -> start -> verify -> stop/start -> verify -> report

## Read next when needed

- `references/ui.md`
- `references/recovery.md`
- `references/degrade-gracefully.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-guardian-builder\SKILL.md
---
---
name: ai_guardian_builder
description: Build local AI guardian tools that monitor a service, diagnose failures, run terminal-based recovery steps, and expose an operator UI. Use when creating watchdogs, service guardians, repair loops, or AI-assisted local operations panels for OpenClaw or similar systems.
---

# AI Guardian Builder

Use this skill when building a local guardian/ops agent.

## Core architecture

1. Health monitor loop
2. Snapshot collection
3. Diagnosis stage
4. Recovery stage
5. Verification stage
6. Operator-visible UI and logs

## Hard rules

- Never hide actions; show what was checked and what command was run.
- Separate diagnosis from repair.
- Verify after every repair attempt.
- Keep logs structured and human-readable.
- If remote AI is unavailable, degrade gracefully to local diagnostics instead of failing closed.

## Preferred local stack

- Python for process control and orchestration
- subprocess for terminal actions
- lightweight local web UI for visibility
- markdown or JSON reports for incident history

## Recovery pattern

observe -> snapshot -> diagnose -> start -> verify -> stop/start -> verify -> report

## Read next when needed

- `references/ui.md`
- `references/recovery.md`
- `references/degrade-gracefully.md`









