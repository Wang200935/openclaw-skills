---
name: codex-deep-search
description: Deep web research skill that combines Tavily Search, Serper.dev, lightweight page extraction, and OpenCode running a Codex-capable model to produce a researched, source-backed summary. Use when the user wants deeper research, cross-source synthesis, credibility checking, or a stronger answer than a quick search.
---

# Codex Deep Search

Use this skill for deeper research tasks where a normal quick web search is not enough.

## What it does

- Searches the web with **Tavily** and **Serper.dev**
- Merges and deduplicates results
- Fetches a handful of top pages
- Extracts lightweight readable text
- Builds a temporary research pack
- Calls **OpenCode** with `wangchatai/gpt-5.3-codex` to synthesize the answer
- Returns a source-backed markdown report

## Inputs

- `query`: required research question
- `max_results`: optional search breadth (default `8`)
- `fetch_pages`: optional number of pages to fetch (default `5`)
- `out`: optional output markdown file path

If `out` is omitted, the recommended wrapper `C:\Users\wang\.openclaw\scripts\deep-search.ps1` now writes the temporary report and pushes it into the private GitHub repo for deep-search reports instead of cluttering the desktop.

## Command

```powershell
python .\scripts\codex_deep_search.py --query "your research question"
```

Example:

```powershell
python .\scripts\codex_deep_search.py --query "What is Google Project Genie and how credible are the claims around it?"
```

## Notes

- Search priority follows user preference: **Tavily first, Serper second**.
- OpenCode synthesis is driven by the configured model `wangchatai/gpt-5.3-codex`.
- OpenCode config path is forced to `C:\Users\wang\.config\opencode\opencode.json`.
- If `out` is omitted, the script prints markdown to stdout.
