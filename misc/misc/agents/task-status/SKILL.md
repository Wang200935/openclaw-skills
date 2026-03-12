---
name: task-status
description: Track, summarize, and report progress for long-running multi-step tasks. Use when work spans multiple turns, background jobs, spawned subagents, or long scripts and the user wants clear status, milestone reporting, completion checks, blockers, or next-step summaries.
---

# Task Status

Use this skill to keep long-running work legible.

## Core workflow

1. Identify the active workstreams.
2. Separate completed, running, blocked, and next-up items.
3. Report milestones, not noise.
4. If the task crosses a meaningful node, note whether a backup or user update is due.
5. Prefer compact dashboards over verbose stream-of-consciousness logs.

## Reporting pattern

- Overall state
- Completed milestones
- In-progress items
- Blockers / risks
- Next actions

## Good use cases

- Background exec/process tasks
- Subagent orchestration
- Multi-file migrations
- Long research / coding / deployment loops
