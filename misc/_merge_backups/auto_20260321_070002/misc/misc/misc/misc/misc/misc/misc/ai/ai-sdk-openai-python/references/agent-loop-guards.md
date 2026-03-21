# Agent loop guardrails

Every tool-enabled loop should define:
- success condition
- max loop turns
- max tool calls
- timeout budget
- duplicate-action detector
- escalation-to-human condition

For risky actions:
- require approval before destructive or irreversible steps
- keep world state separate from conversation state when possible



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-sdk-openai-python\references\agent-loop-guards.md
---
# Agent loop guardrails

Every tool-enabled loop should define:
- success condition
- max loop turns
- max tool calls
- timeout budget
- duplicate-action detector
- escalation-to-human condition

For risky actions:
- require approval before destructive or irreversible steps
- keep world state separate from conversation state when possible








