---
name: ai_agents_frameworks
description: Reason about multi-step agent systems, tool use, orchestration, and control loops using concepts from LangGraph, CrewAI, tool-calling examples, and agent courses. Use when building AI agents that plan, call tools, manage state, or coordinate subtasks.
---

# Agent Framework Patterns

Use this skill for agentic systems.

## Core rules

- Keep control loops explicit.
- Make tool boundaries auditable.
- Separate planner state from executor state.
- Add guardrails around destructive actions.
- Prefer deterministic repair flows over free-form autonomy for ops tasks.

## Common pattern

observe -> diagnose -> decide -> act -> verify

## For ops agents

- Log every action.
- Require confirmation for dangerous steps unless already authorized.
- Make retries bounded and visible.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-agents-frameworks\SKILL.md
---
---
name: ai_agents_frameworks
description: Reason about multi-step agent systems, tool use, orchestration, and control loops using concepts from LangGraph, CrewAI, tool-calling examples, and agent courses. Use when building AI agents that plan, call tools, manage state, or coordinate subtasks.
---

# Agent Framework Patterns

Use this skill for agentic systems.

## Core rules

- Keep control loops explicit.
- Make tool boundaries auditable.
- Separate planner state from executor state.
- Add guardrails around destructive actions.
- Prefer deterministic repair flows over free-form autonomy for ops tasks.

## Common pattern

observe -> diagnose -> decide -> act -> verify

## For ops agents

- Log every action.
- Require confirmation for dangerous steps unless already authorized.
- Make retries bounded and visible.









