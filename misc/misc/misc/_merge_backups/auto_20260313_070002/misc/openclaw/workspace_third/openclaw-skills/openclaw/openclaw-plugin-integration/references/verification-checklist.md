# Verification checklist

A plugin is not considered working until all of these are true:
- gateway is healthy after restart
- plugin registration log appears
- plugin-specific config is reflected in registration output when possible
- plugin-specific CLI/tool command runs successfully
- plugin returns real data, not only a loaded status
