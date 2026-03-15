# Trace taxonomy

Capture at least:
- model_request
- model_response
- tool_call_requested
- tool_call_validated
- tool_execution_started
- tool_execution_finished
- tool_execution_failed
- approval_requested
- loop_terminated

Attach metadata:
- workflow name
- prompt version
- model version
- environment
- incident id or task id
