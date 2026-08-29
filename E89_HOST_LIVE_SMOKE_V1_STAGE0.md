# E89 — refactored host live smoke v1 Stage 0

Date: 2026-08-28

Apparatus commit: `a92577d64612a6a5f7c623e02de89eb527b47017`

Run ID: `2026-08-28-host-refactor-live-smoke-v1`

Disposition: completed by E90. The authorized run stopped before provider I/O
on a stable exact offline/live tokenizer-projection difference.

V1 preserves the E87 one-call design without changing host behavior. It exists
because v0 is a sealed no-retry run ID after E88's pre-provider environmental
stop.

The other GPU job has now ended and released the device. The latest observed
GPU state after release was about 603 MiB used, 15,450 MiB free, and 1 percent
utilization. This observation is not a substitute for the launcher's fresh
runtime gate.

The frozen limits remain:

- at most one model call;
- at most 30,000 serialized tokens;
- one attempt;
- zero retries;
- no automatic continuation.

The exact boundary remains 21,401 ordinary tokens, deterministic
`RESULT-001` externalization, 18,785 treated tokens, and pending `RESULT-007`
delivery on completed call 8. Forty-four host tests, Ruff, mypy over thirteen
host modules, and the direct replay pass after the v1 identity change.

This remains an apparatus qualification rather than behavioral evidence. See
`E90_HOST_LIVE_SMOKE_V1_RESULT.md` for the sealed result and diagnosis.
