# Guardian graph thinking

For service guardians, think in explicit state transitions:
- healthy
- unhealthy-detected
- diagnosing
- attempting-soft-recovery
- verifying
- attempting-stronger-recovery
- recovered
- escalated

This is a better fit than a free-form autonomous agent loop.
