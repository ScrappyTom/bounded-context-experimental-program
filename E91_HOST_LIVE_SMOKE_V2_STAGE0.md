# E91 — refactored host live smoke v2 Stage 0

Date: 2026-08-28

Apparatus commit: `3afd9e269abb437512ea961772b43f4a12ea0f30`

Run ID: `2026-08-28-host-refactor-live-smoke-v2`

Disposition: frozen and provider-free qualified; pending separate exact GPU
authorization.

V2 preserves the same one-call E83 host qualification while correcting the
exact projection boundary exposed by E90. It freezes, rather than tolerates:

- 21,401 live and offline tokens for the ordinary packet;
- 18,785 offline tokens for the relieved packet;
- 18,786 running-server tokens for the same relieved prompt bytes;
- deterministic `RESULT-001` externalization;
- pending `RESULT-007` delivery through completed call 8.

The running-server count is authoritative for live capacity. Any deviation
from either exact frozen projection stops before completion I/O.

The limits remain one model call, 30,000 serialized tokens, one attempt, zero
retries, and no automatic continuation. The v1 seal verifies, the 44-test host
suite passes, Ruff and mypy pass, direct E83 replay reproduces the frozen
offline geometry, and all 282 apparatus tests pass.

This remains a one-call apparatus qualification. It cannot establish model
utility, loop avoidance, or readiness for an unattended trajectory.
