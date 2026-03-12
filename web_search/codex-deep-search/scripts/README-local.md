This machine now has OpenCode installed and configured globally.

OpenCode config path:
C:\Users\wang\AppData\Roaming\opencode\opencode.json

Configured provider:
- wangchatai (OpenAI-compatible)
- baseURL: https://wangchatai.dpdns.org/v1
- models:
  - wangchatai/gpt-5.4
  - wangchatai/gpt-5.3-codex

If you want the deep-search workflow to use OpenCode later, the next step is to wire this skill's script to call:
- opencode run ...
- or a project-local opencode.json override
instead of the current direct HTTP synthesis path.
