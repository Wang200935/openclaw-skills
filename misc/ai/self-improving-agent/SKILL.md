---
name: self-improving-agent
description: Capture operational mistakes, repeated failures, and workflow lessons so future runs improve instead of repeating the same errors. Use when a task fails, a pattern keeps causing problems, a better method is discovered, or the agent should turn execution lessons into durable notes, checklists, or memory updates.
---

# Self-Improving Agent

Use this skill to turn mistakes into durable improvements.

## Core workflow

1. Detect the failure, friction, or lesson.
2. Classify it:
   - command failure
   - bad assumption
   - workflow mistake
   - tool mismatch
   - communication mistake
3. Record the minimal durable lesson in the right place.
4. Promote repeated lessons into:
   - memory
   - AGENTS.md
   - TOOLS.md
   - a skill reference
5. Prefer specific correction rules over vague reflections.

## Good lesson format

- What happened
- Why it failed
- What to do differently next time

## Do not

- Write private secrets into broad shared notes
- Create bloated postmortems for trivial mistakes
- Record lessons without an action rule
