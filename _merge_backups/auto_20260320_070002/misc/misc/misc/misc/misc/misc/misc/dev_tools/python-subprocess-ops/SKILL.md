---
name: python_subprocess_ops
description: Safely run and supervise terminal commands from Python using subprocess for diagnostics, repair loops, and local automation. Use when building Python tools that must call CLIs, collect output, enforce timeouts, or recover services.
---

# Python subprocess Ops

Use this skill when Python must drive terminal commands.

## Good defaults

- Prefer `subprocess.run([...], shell=False, capture_output=True, text=True, timeout=...)`.
- Use explicit argument arrays, not shell strings, unless shell behavior is required.
- Capture stdout and stderr together for diagnostics.
- Treat timeout, return code, and stderr as first-class signals.
- Record command, exit code, and key output excerpt.

## For watchdog / repair tools

- Separate health checks from repair steps.
- Retry carefully, not infinitely.
- Verify after each repair step.
- Write machine-readable and human-readable logs.

## Read next when needed

- `references/checklist.md` for subprocess safety and supervision



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\dev_tools\python-subprocess-ops\SKILL.md
---
---
name: python_subprocess_ops
description: Safely run and supervise terminal commands from Python using subprocess for diagnostics, repair loops, and local automation. Use when building Python tools that must call CLIs, collect output, enforce timeouts, or recover services.
---

# Python subprocess Ops

Use this skill when Python must drive terminal commands.

## Good defaults

- Prefer `subprocess.run([...], shell=False, capture_output=True, text=True, timeout=...)`.
- Use explicit argument arrays, not shell strings, unless shell behavior is required.
- Capture stdout and stderr together for diagnostics.
- Treat timeout, return code, and stderr as first-class signals.
- Record command, exit code, and key output excerpt.

## For watchdog / repair tools

- Separate health checks from repair steps.
- Retry carefully, not infinitely.
- Verify after each repair step.
- Write machine-readable and human-readable logs.

## Read next when needed

- `references/checklist.md` for subprocess safety and supervision








