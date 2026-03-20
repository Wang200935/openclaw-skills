# OpenAI / OpenAI-compatible Python patterns

## 1. Raw HTTP first

Use a tiny raw HTTP probe before blaming SDKs.

Check in this order:
- root domain reachable?
- `/models` reachable?
- `/chat/completions` reachable?
- `/responses` reachable?

Record:
- exact URL
- method
- headers shape
- status code
- response excerpt

## 2. OpenAI-compatible caveats

Do not assume every proxy supports:
- `/responses`
- tool calling
- streaming
- the same auth header behavior
- the same model ids as upstream OpenAI

## 3. Failure mapping

- `1010`: anti-bot / browser signature denial
- `403`: auth, IP policy, route policy, or WAF decision
- `404`: wrong route or unsupported product surface
- `502/504`: upstream/proxy problem, not usually prompt/model logic

## 4. Practical diagnosis order

1. Test with `curl`
2. Test with Python `urllib`/`requests`
3. Compare with a known-working client
4. Only then switch to SDK abstraction

## 5. For production wrappers

Wrap API calls behind one adapter that controls:
- base URL
- auth header
- endpoint path
- timeout
- retry policy
- logging
- streaming mode



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\ai\ai-sdk-openai-python\references\sdk-patterns.md
---
# OpenAI / OpenAI-compatible Python patterns

## 1. Raw HTTP first

Use a tiny raw HTTP probe before blaming SDKs.

Check in this order:
- root domain reachable?
- `/models` reachable?
- `/chat/completions` reachable?
- `/responses` reachable?

Record:
- exact URL
- method
- headers shape
- status code
- response excerpt

## 2. OpenAI-compatible caveats

Do not assume every proxy supports:
- `/responses`
- tool calling
- streaming
- the same auth header behavior
- the same model ids as upstream OpenAI

## 3. Failure mapping

- `1010`: anti-bot / browser signature denial
- `403`: auth, IP policy, route policy, or WAF decision
- `404`: wrong route or unsupported product surface
- `502/504`: upstream/proxy problem, not usually prompt/model logic

## 4. Practical diagnosis order

1. Test with `curl`
2. Test with Python `urllib`/`requests`
3. Compare with a known-working client
4. Only then switch to SDK abstraction

## 5. For production wrappers

Wrap API calls behind one adapter that controls:
- base URL
- auth header
- endpoint path
- timeout
- retry policy
- logging
- streaming mode









