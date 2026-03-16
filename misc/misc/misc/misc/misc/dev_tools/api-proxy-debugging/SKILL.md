---
name: api_proxy_debugging
description: Diagnose OpenAI-compatible API proxies, custom base URLs, Cloudflare/WAF interference, endpoint mismatches, and request-shape bugs. Use when an LLM API works in some tools but fails in your own code or scripts.
---

# API Proxy Debugging

Use this skill when a custom LLM endpoint behaves inconsistently across clients.

## Core lessons

1. Confirm whether the problem is auth, path, client fingerprint, or upstream instability.
2. Probe routes directly before integrating them into a larger app.
3. Test with the same API key across multiple request styles.
4. Compare raw HTTP, curl, and Python client behavior.
5. Record exact response codes and body excerpts.

## Known pitfall class

Cloudflare or WAF can block default Python client signatures even when:
- the key is valid
- the route exists
- the same request works from curl or a browser-like client

## Read next when needed

- `references/probe-order.md`
- `references/cloudflare-lessons.md`
- `references/request-shape-matrix.md`



---
MERGED_FROM_BACKUP: C:\Users\wang\.openclaw\skills\dev_tools\api-proxy-debugging\SKILL.md
---
---
name: api_proxy_debugging
description: Diagnose OpenAI-compatible API proxies, custom base URLs, Cloudflare/WAF interference, endpoint mismatches, and request-shape bugs. Use when an LLM API works in some tools but fails in your own code or scripts.
---

# API Proxy Debugging

Use this skill when a custom LLM endpoint behaves inconsistently across clients.

## Core lessons

1. Confirm whether the problem is auth, path, client fingerprint, or upstream instability.
2. Probe routes directly before integrating them into a larger app.
3. Test with the same API key across multiple request styles.
4. Compare raw HTTP, curl, and Python client behavior.
5. Record exact response codes and body excerpts.

## Known pitfall class

Cloudflare or WAF can block default Python client signatures even when:
- the key is valid
- the route exists
- the same request works from curl or a browser-like client

## Read next when needed

- `references/probe-order.md`
- `references/cloudflare-lessons.md`
- `references/request-shape-matrix.md`






