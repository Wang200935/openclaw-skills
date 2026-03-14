# Windows subprocess notes

- Prefer explicit executable paths when PATH lookup is unreliable.
- `shell=False` remains the safe default.
- On Windows, `.cmd` wrappers may behave differently from direct binaries.
- Capture both stdout and stderr because many CLIs print important diagnostics to stderr even on partial success.
- Do not kill the process that is running your current supervision command by accident.
- Be careful with reserved PowerShell variables like `$PID`.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\dev_tools\python-subprocess-ops\references\windows-notes.md
---
# Windows subprocess notes

- Prefer explicit executable paths when PATH lookup is unreliable.
- `shell=False` remains the safe default.
- On Windows, `.cmd` wrappers may behave differently from direct binaries.
- Capture both stdout and stderr because many CLIs print important diagnostics to stderr even on partial success.
- Do not kill the process that is running your current supervision command by accident.
- Be careful with reserved PowerShell variables like `$PID`.




