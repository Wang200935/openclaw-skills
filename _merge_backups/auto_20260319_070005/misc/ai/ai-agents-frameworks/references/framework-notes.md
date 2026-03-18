# Agent framework notes

## LangGraph-style thinking

Represent long-lived workflows as explicit state transitions.
Good for:
- observe -> diagnose -> repair loops
- retries with bounded transitions
- persistent state and resumability

## CrewAI-style thinking

Represent specialized roles with clear task boundaries.
Good for:
- researcher
- operator
- evaluator
- reporter

## Tool calling

Prefer explicit tool schemas and visible action logs.
For ops tasks, keep the executor deterministic when possible.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-agents-frameworks\references\framework-notes.md
---
# Agent framework notes

## LangGraph-style thinking

Represent long-lived workflows as explicit state transitions.
Good for:
- observe -> diagnose -> repair loops
- retries with bounded transitions
- persistent state and resumability

## CrewAI-style thinking

Represent specialized roles with clear task boundaries.
Good for:
- researcher
- operator
- evaluator
- reporter

## Tool calling

Prefer explicit tool schemas and visible action logs.
For ops tasks, keep the executor deterministic when possible.


