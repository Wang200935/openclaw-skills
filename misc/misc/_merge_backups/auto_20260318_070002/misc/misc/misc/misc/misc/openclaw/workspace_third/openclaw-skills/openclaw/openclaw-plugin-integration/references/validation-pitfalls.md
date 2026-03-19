# Validation pitfalls

Common mistake:
- plugin appears installed but gateway refuses to load because required config schema fields are missing

Example class:
- `plugins.entries.<id>.config.embedding` required before enablement

Treat schema errors as a signal to finish config before restart.



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\openclaw\openclaw-plugin-integration\references\validation-pitfalls.md
---
# Validation pitfalls

Common mistake:
- plugin appears installed but gateway refuses to load because required config schema fields are missing

Example class:
- `plugins.entries.<id>.config.embedding` required before enablement

Treat schema errors as a signal to finish config before restart.






