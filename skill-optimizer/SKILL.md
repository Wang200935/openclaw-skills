---
name: skill-optimizer
description: Periodically scan all skills, classify and index them, detect duplicates, propose/perform merges with backup+archive, and update SKILL.md metadata to improve OpenClaw skill retrieval efficiency. Use for scheduled 12-hour skill optimization runs or manual skill-library maintenance.
---

# Skill Optimizer

## Purpose
Scan **all skills**, classify them, detect overlaps, build a fast retrieval index, and **merge duplicates** safely with full backup + archive. This skill is designed for **scheduled optimization runs every 12 hours** and for manual maintenance.

## Safety rules (non‑destructive default)
- Always **backup** before any merge.
- Default mode is **report‑only**. Use `--apply` to perform merges/archiving.
- When merging, **archive** the duplicate skill folder under `_archive/YYYY-MM/` (do not delete).

## How to run manually
```powershell
python <OPENCLAW_HOME>/skills/skill-optimizer/scripts/skill_optimizer.py --apply --deep-pass 2
```

## What it outputs
- **skills_index.json / skills_index.md** — searchable index
- **duplicates.json / merge_candidates.md** — duplicate/merge report
- **skills_memory.md** — condensed per‑skill memory summary (updated every run)
- **backups/** — full snapshots for rollback

## Scheduling (cron)
Use OpenClaw cron in an **isolated session**:
```powershell
openclaw cron add \
  --name "Skill optimizer" \
  --cron "0 4,16 * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "Use skill-optimizer skill to run scripts/skill_optimizer.py --apply --deep-pass 2" \
  --delivery none
```

## Merge policy (summary)
- Merge when name+description similarity is high and no conflicts.
- Prefer the most complete skill as primary.
- Archive the duplicate to `_archive/YYYY-MM/`.
- Update the index to map aliases → primary skill.
