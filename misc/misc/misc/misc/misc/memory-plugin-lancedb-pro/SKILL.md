---
name: memory_plugin_lancedb_pro
description: Install and configure the third-party OpenClaw memory-lancedb-pro plugin with Jina embeddings/reranker, set plugin load paths and memory slot selection, and verify that LanceDB memory commands actually work. Use when enabling advanced LanceDB memory in OpenClaw.
---

# memory-lancedb-pro Integration

Use this skill when setting up the `memory-lancedb-pro` plugin.

## Core lessons

- The plugin can appear installed but still fail unless required config schema fields are present.
- The important required path is `plugins.entries.memory-lancedb-pro.config.embedding`.
- After installation, verify with plugin-specific functionality such as `openclaw memory-pro stats` and `openclaw memory-pro list`, not only `plugins list`.
- If service environment variables are inconvenient or unreliable, direct config values can be the faster path to a working deployment.

## Minimum config areas

- `plugins.allow`
- `plugins.load.paths`
- `plugins.entries.memory-lancedb-pro.enabled`
- `plugins.entries.memory-lancedb-pro.config.embedding`
- `plugins.entries.memory-lancedb-pro.config.retrieval`
- `plugins.slots.memory = "memory-lancedb-pro"`

## Verification target

A good install shows all of these:
- plugin registered in gateway logs
- LanceDB path visible
- embedding model visible
- `memory-pro stats` returns counts and retrieval mode
- `memory-pro list` returns actual memories

## Read next when needed

- `references/jina-config.md`
- `references/real-verification.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\misc\memory-plugin-lancedb-pro\SKILL.md
---
---
name: memory_plugin_lancedb_pro
description: Install and configure the third-party OpenClaw memory-lancedb-pro plugin with Jina embeddings/reranker, set plugin load paths and memory slot selection, and verify that LanceDB memory commands actually work. Use when enabling advanced LanceDB memory in OpenClaw.
---

# memory-lancedb-pro Integration

Use this skill when setting up the `memory-lancedb-pro` plugin.

## Core lessons

- The plugin can appear installed but still fail unless required config schema fields are present.
- The important required path is `plugins.entries.memory-lancedb-pro.config.embedding`.
- After installation, verify with plugin-specific functionality such as `openclaw memory-pro stats` and `openclaw memory-pro list`, not only `plugins list`.
- If service environment variables are inconvenient or unreliable, direct config values can be the faster path to a working deployment.

## Minimum config areas

- `plugins.allow`
- `plugins.load.paths`
- `plugins.entries.memory-lancedb-pro.enabled`
- `plugins.entries.memory-lancedb-pro.config.embedding`
- `plugins.entries.memory-lancedb-pro.config.retrieval`
- `plugins.slots.memory = "memory-lancedb-pro"`

## Verification target

A good install shows all of these:
- plugin registered in gateway logs
- LanceDB path visible
- embedding model visible
- `memory-pro stats` returns counts and retrieval mode
- `memory-pro list` returns actual memories

## Read next when needed

- `references/jina-config.md`
- `references/real-verification.md`





