# E97 — bounded candidate causal-history offline qualification

Date: 2026-08-29

Source:
`ScrappyTom/qwen38-artifact-coupled-integration-scout-v0@15b7f57e1042194d3cdf859b2650a213c8a93a77`

## Result

The E96 host failure had two coupled sources of redundant model-facing state:

1. delivered mutation-effect bodies remained beside the complete exact current
   candidate; and
2. the assistant mutation actions could themselves contain large copies of the
   artifact already represented by that candidate.

E97 implements one guarded lifecycle for that causal pair. An old mutation
action/effect pair may become compact model-facing receipts only after the
effect has crossed a completed invocation and its exact before/after lineage
ends at the exact current candidate. The original action, effect, hashes, and
event order remain in append-only external custody. The pending effect and its
causal action remain exact. The host exposes a replaceable mechanical
current-effect object and explicitly does not infer semantic uptake.

## Authentic E96 replay

The sealed E96 V1 checkpoint contains six candidate effects:

- delivered-resident: `RESULT-013` through `RESULT-017`;
- pending: `RESULT-018`.

The future policy compacts only the five delivered action/effect pairs and
leaves `RESULT-018` exact. All exact effect hashes are preserved. Under the
same locked offline tokenizer, the pre-terminal packet changes from 21,023 to
19,116 tokens against a 20,992-token allowance, leaving 1,876 tokens of
headroom.

The historical live result remains 21,041 tokens and `capacity_blocked`. E97
does not retry, continue, or regrade E96. Because the core host files changed,
their execution-manifest hash changed too; current-head hydration correctly
refuses to claim identity with the old execution package. Exact historical
continuation remains bound to the E96 result commit.

## What this solves

It solves a specific lifecycle problem:

```text
exact current candidate
+ old delivered mutation actions
+ old delivered mutation effects
-> mechanically redundant active causal history

exact delivery + exact lineage proof
-> compact applied-action receipt
+ compact applied-effect receipt
+ exact external custody
+ one bounded current-effect object
```

It keeps the newest undelivered causal update available for a real model call,
while preventing every older applied mutation from retaining full prompt
residency indefinitely.

## What this does not solve

The policy operates only after delivery. A newly emitted complete-document
mutation and its pending effect must still fit together for one later model
call. E97 therefore does not eliminate the response/action transport boundary
or justify monolithic artifact replacement. Incremental task-artifact actions
remain part of the viable whole-system geometry.

It also does not prove that Qwen noticed an effect, used the current candidate
correctly, verified the artifact, repaired it, or closed appropriately. The
provider-free end-to-end fixture proves only that the host path can traverse
mutation, delivery, compaction, check, repair, recheck, and closure without
violating custody.

## Verification

- 5 focused lifecycle/audit tests passed;
- Ruff passed;
- mypy passed over 16 host modules;
- all 303 apparatus repository tests passed in 422.95 seconds;
- GPU/provider calls: zero.

## Program disposition

E97 closes the selected offline E96 lifecycle repair. The mechanical substrate
now has a bounded applied-candidate causal-history operation in addition to
ordinary source relief. This is not live agent-utility evidence and does not
select an automatic E96 continuation or another GPU run.

The next research decision should return to a whole configuration. Any live
successor must prospectively combine incremental artifact actions, exact
delivery/currentness, bounded applied causal history, current checking, repair,
and review checkpoints. A separate frozen package and explicit authorization
would be required.
