# Recovery guardrails

## Minimum protections

- consecutive-failure threshold before incident opens
- cooldown after each recovery attempt
- restart budget per incident and per time window
- pause mode
- maintenance mode
- escalated mode when auto-recovery is no longer safe

## Preferred recovery policy

1. observe unhealthy state repeatedly
2. open incident
3. collect snapshot
4. diagnose
5. run one bounded recovery action
6. verify
7. wait through cooldown
8. escalate only after limited retries

## Avoid

- multiple strong actions in one loop iteration
- infinite retries
- treating a temporary green state as final proof of stability



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-guardian-lessons\references\recovery-guards.md
---
# Recovery guardrails

## Minimum protections

- consecutive-failure threshold before incident opens
- cooldown after each recovery attempt
- restart budget per incident and per time window
- pause mode
- maintenance mode
- escalated mode when auto-recovery is no longer safe

## Preferred recovery policy

1. observe unhealthy state repeatedly
2. open incident
3. collect snapshot
4. diagnose
5. run one bounded recovery action
6. verify
7. wait through cooldown
8. escalate only after limited retries

## Avoid

- multiple strong actions in one loop iteration
- infinite retries
- treating a temporary green state as final proof of stability




