# E92 — refactored host live smoke v2 result

Date: 2026-08-29

Freeze commit: `3afd9e269abb437512ea961772b43f4a12ea0f30`

Result commit: `eddb5d6f8095a931701642542d94face46b7057b`

Run ID: `2026-08-28-host-refactor-live-smoke-v2`

Disposition: qualified and stopped at the mandatory checkpoint after exactly
one model call, one attempt, and zero retries.

All exact asset and runtime gates passed. Deterministic `RESULT-001` relief
produced the frozen 18,786-token live prompt. The completed invocation delivered
pending `RESULT-007` on call 8. Qwen then returned a valid batch read for
TRANSIT 61–94 and COMMS 61–94. The host admitted it, acquired exact
`RESULT-008`, and correctly left that new result pending for a later completed
invocation.

The call used 18,786 prompt and 74 completion tokens, totaling 18,860
serialized tokens. There were no failed invocations, reopens, repeat demands,
repeated responses, or candidate changes. The checkpoint, mechanical review,
request/response custody, result lifecycle, run seal, and server release all
verify. The run seal SHA-256 is
`2eb130f3ed5d1cea7c399bbf018c7b15e618624b20f31e8eec421ac9cda021d3`.

Qualitatively, the action continues Qwen's prior depth-first source-pair pacing:
after receiving the first TRANSIT/COMMS ranges, it requested their remaining
ranges. This is coherent acquisition and establishes that the refactored live
path connects exact pressure relief, pending-result delivery, model action,
new-result acquisition, and checkpointing correctly. It does not establish
task integration, artifact progress, loop resistance, verification, readiness,
or closure.

The v2 smoke is closed. No continuation or behavioral experiment is selected
or authorized by this apparatus result.
