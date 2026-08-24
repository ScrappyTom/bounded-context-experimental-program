# E48 — Northstar transfer pressure-screen result

Date: 2026-08-24

Source:
[`ScrappyTom/qwen38-artifact-coupled-integration-scout-v0@454c605`](https://github.com/ScrappyTom/qwen38-artifact-coupled-integration-scout-v0/commit/454c605e896a48878673686864552af20f52c5b0)

Authorized freeze:
`40272d6cc0c5aa2eda7bb5df9394ff02d767829d`

Disposition: **LR/AF/NQ** — the run is exactly sealed and mechanically
reconciled, and it observed authentic pressure plus feasible positive relief.
It failed the prospectively frozen meaningful-acquisition threshold, so it
does not create the detached/coupled measured fork.

## Literal behavior

The actor made two valid `read_batch` decisions with one attempt per call and
zero retries:

- call 1 acquired S01–S03 as `RESULT-001`;
- call 2 acquired S04–S06 as pending `RESULT-002`.

`RESULT-001` crossed the second actor boundary. Adding `RESULT-002` to the
ordinary chronology would produce 25,705 prompt tokens against the 20,992-token
allowance, an overflow of 4,713 tokens. The candidate remained byte-identical,
no check or submission occurred, and `RESULT-002` remained undelivered.

A deterministic first-fit substitution of `RESULT-001`, with the pending
result protected, would reduce the packet to 14,654 tokens. Physical pressure
and relief feasibility are therefore real.

## Why the fork is ineligible

The frozen gate required at least four previously delivered source-observation
result objects. Only one delivered result object existed, although it contained
three sources. The second three-source batch created pressure immediately.
The runner correctly terminated as `pressure_boundary_ineligible`, and the
Stage 0 contract closes this task selection rather than allowing a retry or
post-outcome threshold change.

This exposes a system interaction missed by offline Stage 0:

```text
actor-selected batch ingress
        ×
large exact result bodies
        ×
result-object-count activation rule
        ↓
evidence throughput rises,
but pressure arrives before the planned semantic-work fork
```

Future qualification must prospectively align its meaningful-acquisition unit
with the ingress geometry it permits. That is not permission to retroactively
count this batch differently.

## Apparatus qualification

The sealed run, two provider attempts, exact requests/responses/results, token
recount, candidate identity, pending-result status, positive relief, runtime
release, and tree seal pass a separate post-run mechanical audit. The frozen
qualification auditor remains false, as it should for the ineligible endpoint.

One independent apparatus defect was found: the frozen runner omitted
`task_source_lock_sha256` from `SCREEN_RESULT.json` even though the frozen
auditor required it. The exact lock is still verified in `FREEZE_BINDING.json`.
Post-run code repairs the field for future screens without changing the sealed
result. The defect did not cause or cure the scientific ineligibility.

## Claim limit and route

Supported locally:

- authentic early pressure;
- positive mechanical relief feasibility;
- exact two-call acquisition behavior; and
- a batch-ingress/residency/activation interaction.

Not supported:

- artifact-coupling utility or harm;
- a D0/A1 causal comparison;
- semantic integration quality;
- measured continuation; or
- same-task retry.

No GPU successor is authorized. The next program action is an offline systems
reconciliation of activation semantics for a future fresh task, not a repaired
Northstar screen or a relaxation of this result.
