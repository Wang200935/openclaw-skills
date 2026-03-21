---
name: openclaw_plugin_integration
description: Install, configure, validate, and troubleshoot OpenClaw plugins safely, especially third-party extensions with config schemas, plugin slots, extra load paths, and gateway restarts. Use when integrating external plugins into OpenClaw.
---

# OpenClaw Plugin Integration

Use this skill when adding or repairing OpenClaw plugins.

## Core workflow

1. Inspect plugin docs and schema before install.
2. Identify required config fields before enabling the plugin.
3. Install the plugin into a trusted extensions path.
4. Add explicit `plugins.allow`, `plugins.load.paths`, `plugins.entries.<id>`, and slot selection if needed.
5. Restart gateway only after config is complete.
6. Verify with both plugin load signals and real functional commands.

## Hard rules

- Do not enable a plugin before required config exists.
- Treat plugin schema validation errors as install blockers, not minor warnings.
- Verify real functionality, not just plugin registration.
- Avoid relying on service environment variables when direct config is more reliable for the current deployment.

## Read next when needed

- `references/install-order.md`
- `references/validation-pitfalls.md`
- `references/verification-checklist.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\openclaw\openclaw-plugin-integration\SKILL.md
---
---
name: openclaw_plugin_integration
description: Install, configure, validate, and troubleshoot OpenClaw plugins safely, especially third-party extensions with config schemas, plugin slots, extra load paths, and gateway restarts. Use when integrating external plugins into OpenClaw.
---

# OpenClaw Plugin Integration

Use this skill when adding or repairing OpenClaw plugins.

## Core workflow

1. Inspect plugin docs and schema before install.
2. Identify required config fields before enabling the plugin.
3. Install the plugin into a trusted extensions path.
4. Add explicit `plugins.allow`, `plugins.load.paths`, `plugins.entries.<id>`, and slot selection if needed.
5. Restart gateway only after config is complete.
6. Verify with both plugin load signals and real functional commands.

## Hard rules

- Do not enable a plugin before required config exists.
- Treat plugin schema validation errors as install blockers, not minor warnings.
- Verify real functionality, not just plugin registration.
- Avoid relying on service environment variables when direct config is more reliable for the current deployment.

## Read next when needed

- `references/install-order.md`
- `references/validation-pitfalls.md`
- `references/verification-checklist.md`










