---
name: ai_sdk_openai_python
description: Build or debug Python integrations against OpenAI-compatible APIs, including chat/completions, responses, tool calling, streaming, auth headers, and endpoint probing. Use when wiring Python code to an LLM API or diagnosing why a Python client cannot reach a model endpoint.
---

# OpenAI Python / OpenAI-compatible API

Use this skill for Python clients talking to OpenAI-style endpoints.

## Core workflow

1. Confirm base URL, auth header, and endpoint path.
2. Probe lightweight routes first (`/models`, then a minimal text generation request).
3. Distinguish auth problems from proxy/WAF/upstream failures.
4. Prefer small reproducible Python scripts over large frameworks during diagnosis.
5. Record exact request path, headers shape, status code, and response body excerpt.

## Diagnose by failure class

- `401/403`: auth, policy, IP/WAF, or route restrictions.
- `404`: wrong path or product mismatch.
- `429`: rate limiting or quota.
- `5xx`: upstream/proxy instability.
- Cloudflare 1010: browser/request signature denied.
- Cloudflare 502/504: upstream unavailable or proxy path broken.

## Minimal patterns

- Start with raw HTTP if SDK behavior is unclear.
- Use SDK only after raw request format is confirmed.
- For OpenAI-compatible proxies, do not assume `/responses` is supported.
- Try both `/chat/completions` and `/models` when diagnosing.

## What to report

Always summarize:
- what route was tested
- what status code came back
- whether the issue is local code, auth, or upstream/proxy

## Read next when needed

- For deeper request/response patterns: `references/patterns.md`
- For failure interpretation: `references/failures.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-sdk-openai-python\SKILL.md
---
---
name: ai_sdk_openai_python
description: Build or debug Python integrations against OpenAI-compatible APIs, including chat/completions, responses, tool calling, streaming, auth headers, and endpoint probing. Use when wiring Python code to an LLM API or diagnosing why a Python client cannot reach a model endpoint.
---

# OpenAI Python / OpenAI-compatible API

Use this skill for Python clients talking to OpenAI-style endpoints.

## Core workflow

1. Confirm base URL, auth header, and endpoint path.
2. Probe lightweight routes first (`/models`, then a minimal text generation request).
3. Distinguish auth problems from proxy/WAF/upstream failures.
4. Prefer small reproducible Python scripts over large frameworks during diagnosis.
5. Record exact request path, headers shape, status code, and response body excerpt.

## Diagnose by failure class

- `401/403`: auth, policy, IP/WAF, or route restrictions.
- `404`: wrong path or product mismatch.
- `429`: rate limiting or quota.
- `5xx`: upstream/proxy instability.
- Cloudflare 1010: browser/request signature denied.
- Cloudflare 502/504: upstream unavailable or proxy path broken.

## Minimal patterns

- Start with raw HTTP if SDK behavior is unclear.
- Use SDK only after raw request format is confirmed.
- For OpenAI-compatible proxies, do not assume `/responses` is supported.
- Try both `/chat/completions` and `/models` when diagnosing.

## What to report

Always summarize:
- what route was tested
- what status code came back
- whether the issue is local code, auth, or upstream/proxy

## Read next when needed

- For deeper request/response patterns: `references/patterns.md`
- For failure interpretation: `references/failures.md`






