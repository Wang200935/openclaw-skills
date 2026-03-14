# Cloudflare / WAF lessons

## Important lesson

If Python default clients fail but browser-like requests succeed, suspect client fingerprint blocking.

## Practical fix path

Try explicit headers:
- `User-Agent: Mozilla/5.0`
- `Accept: application/json`
- `Content-Type: application/json`
- explicit `Authorization: Bearer ...`
- optionally `Origin` and `Referer`

## Distinguish failures

- `1010` / `403`: request signature or policy block
- `502/504`: upstream/proxy instability
- `401`: auth works enough to reach the API layer, but credentials are missing/invalid



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\dev_tools\api-proxy-debugging\references\cloudflare-lessons.md
---
# Cloudflare / WAF lessons

## Important lesson

If Python default clients fail but browser-like requests succeed, suspect client fingerprint blocking.

## Practical fix path

Try explicit headers:
- `User-Agent: Mozilla/5.0`
- `Accept: application/json`
- `Content-Type: application/json`
- explicit `Authorization: Bearer ...`
- optionally `Origin` and `Referer`

## Distinguish failures

- `1010` / `403`: request signature or policy block
- `502/504`: upstream/proxy instability
- `401`: auth works enough to reach the API layer, but credentials are missing/invalid




