# E94 — Trellis refactored-host first interaction checkpoint

Date: 2026-08-29

Freeze commit:
`381e44c9eb3c3c10a793903155c2482f5f8c570f`

Result commit:
`0626259773f1411272566caa1b4a00c83e70e606`

Run ID:
`2026-08-29-trellis-refactored-interaction-tranche-v0`

Disposition: both cells reached the mandatory twelve-actor-call checkpoint;
neither completed the task.

## Literal result

The sealed run used 24 actor calls, six maintenance calls, 30 provider calls,
and 379,972 serialized tokens with one attempt per call and zero retries.

Both configurations made exactly the same twelve actions: they read both halves
of each paired source in the frozen catalog order, from COUNCIL/CLIMATE through
LINEAGE/REVIEW. `RESULT-001` through `RESULT-011` crossed completed actor
invocations. Call 12 acquired `RESULT-012`, but no later call existed to deliver
it. Neither arm reopened evidence, repeated a read, produced an invalid action,
changed either artifact, checked, repaired, or submitted. Both candidates
remain the exact initial placeholder and are independently `not_ready`.

The mechanical host operated correctly. V0 externalized five old exact results
over four pressure events. V1 externalized seven over six pressure events. All
pending/delivered transitions, capacity relief, request bindings, checkpoints,
seals, and runtime releases verified.

## Treatment lifecycle

V1 used six successful maintenance calls. All proposed claims were grounded and
mechanically admitted; no transport or material-safety failure occurred. The
maintenance calls cost 31,578 serialized tokens. Twenty claims were admitted
over time, while ten remained in the final bounded register because later
chunks replaced earlier claims in the same source slot.

That replacement policy produced a real semantic lifecycle loss. High-value
COUNCIL/CLIMATE and GRID/WATER authority, threshold, capacity, pressure, and
reserve facts were later replaced by low-value tail-table rows from the second
chunk of the same sources. CLINIC/SHELTER key capacity facts were similarly
replaced. TRANSIT/COMMS retained useful later facts. The register was safe and
grounded, but its physical-chunk-triggered slot replacement was not equivalent
to preserving the most useful accumulated source meaning.

## System interpretation

The scaffold was active but did not change actor behavior before the first
checkpoint. That does not establish that it is useless. The actor was still
executing a strongly cued catalog-completion policy in both arms, and the final
catalog result had not yet entered either actor. There was no post-acquisition
decision in which the treatment could affect construction, reopen demand, or
verification.

V1 was more expensive at this boundary: 205,399 versus 174,573 serialized
tokens. Its actor prompt total was slightly lower, but it paid 31,578
maintenance tokens, lost 19,274 cached prompt tokens relative to V0, and
externalized two additional exact results. That cost purchased a grounded but
partly lossy semantic state and no observed behavioral divergence yet.

The supported conclusion is:

> During catalog traversal, the temporary provenance scaffold was mechanically
> safe and semantically active but added cost and exact-residency pressure
> without altering the actor's acquisition sequence. Its same-source
> replacement cadence discarded important early facts. Downstream construction
> utility remains untested because both cells stopped before the final source
> result was delivered.

The continuation may proceed only without changing the two configurations.
Repairing the register now would start a new experiment.

Detailed literal and qualitative custody remains in the apparatus repository's
`TRELLIS_REFACTORED_INTERACTION_TRANCHE_RESULT.md` and
`TRELLIS_REFACTORED_INTERACTION_QUALITATIVE_APPENDIX.md`.
