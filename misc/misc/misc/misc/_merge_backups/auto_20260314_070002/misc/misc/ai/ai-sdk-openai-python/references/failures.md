# Failure guide

- 1010: Cloudflare/browser signature denial. Suspect WAF or anti-bot rules.
- 502/504: upstream unavailable, reverse proxy misroute, or backend timeout.
- 403 with valid key: route policy, IP restriction, or product mismatch.
- If root domain responds but `/v1/...` fails, suspect API path/proxy configuration.
