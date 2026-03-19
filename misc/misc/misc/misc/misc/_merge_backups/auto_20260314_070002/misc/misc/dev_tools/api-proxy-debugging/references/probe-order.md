# Probe order

1. root domain reachable?
2. `/models` reachable?
3. minimal `/chat/completions` request
4. minimal `/responses` request if supported
5. compare curl vs Python raw HTTP vs SDK

Do not debug application logic before route viability is confirmed.
