# Tool-calling runtime pattern

## Canonical loop

1. send conversation + tool schemas
2. inspect assistant response
3. if no tool call -> final answer
4. if tool call -> validate args
5. run tool under policy
6. wrap tool result in compact structured form
7. append tool result back to conversation
8. continue until success / stop condition / escalation

## Runtime responsibilities

- schema validation
- semantic validation
- authorization/policy checks
- timeout and retry limits
- loop detection
- logging/tracing

## Tool result shape

Prefer:
- ok: true/false
- summary
- data or error
- optional artifacts/paths

## Avoid

- raw giant logs in model context
- vague tool descriptions
- tools with overlapping responsibilities
- letting model define safety policy



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-sdk-openai-python\references\tool-calling-runtime.md
---
# Tool-calling runtime pattern

## Canonical loop

1. send conversation + tool schemas
2. inspect assistant response
3. if no tool call -> final answer
4. if tool call -> validate args
5. run tool under policy
6. wrap tool result in compact structured form
7. append tool result back to conversation
8. continue until success / stop condition / escalation

## Runtime responsibilities

- schema validation
- semantic validation
- authorization/policy checks
- timeout and retry limits
- loop detection
- logging/tracing

## Tool result shape

Prefer:
- ok: true/false
- summary
- data or error
- optional artifacts/paths

## Avoid

- raw giant logs in model context
- vague tool descriptions
- tools with overlapping responsibilities
- letting model define safety policy










