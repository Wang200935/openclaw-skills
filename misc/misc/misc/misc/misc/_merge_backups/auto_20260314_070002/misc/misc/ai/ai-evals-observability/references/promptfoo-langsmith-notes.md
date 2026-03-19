# Evals and observability notes

## Promptfoo-style use

Use for:
- prompt regression checks
- comparing prompt variants
- catching output drift after changes

## LangSmith-style use

Use for:
- tracing chain execution
- inspecting intermediate steps
- replaying failures
- comparing runs over time

## Practical local substitute

If those platforms are not installed, still preserve:
- input
- intermediate snapshots
- output
- repair action
- final verification

This gives you a minimal local trace system.
