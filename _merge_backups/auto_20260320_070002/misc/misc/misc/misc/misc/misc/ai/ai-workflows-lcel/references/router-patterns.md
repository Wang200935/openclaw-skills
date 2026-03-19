# Router patterns

## Classifier -> branch

Use LCEL-style routing when the flow is mostly tree-shaped and stateless.
Example:
- classify request
- map to branch
- execute narrow chain
- parse result

## Validation/repair pattern

- generate structured output
- validate against schema
- if invalid, run one bounded repair pass
- stop instead of infinite self-fixing loops



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-workflows-lcel\references\router-patterns.md
---
# Router patterns

## Classifier -> branch

Use LCEL-style routing when the flow is mostly tree-shaped and stateless.
Example:
- classify request
- map to branch
- execute narrow chain
- parse result

## Validation/repair pattern

- generate structured output
- validate against schema
- if invalid, run one bounded repair pass
- stop instead of infinite self-fixing loops







