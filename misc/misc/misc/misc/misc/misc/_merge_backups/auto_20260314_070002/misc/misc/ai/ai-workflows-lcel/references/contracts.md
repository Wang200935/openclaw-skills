# Data contracts for chained workflows

When building chains, define each stage with:
- input schema
- output schema
- failure modes
- timeout budget
- logging surface

Example operator flow:
- health snapshot -> diagnosis text -> recovery plan -> terminal action -> verification result

Make it possible to rerun each stage independently.
