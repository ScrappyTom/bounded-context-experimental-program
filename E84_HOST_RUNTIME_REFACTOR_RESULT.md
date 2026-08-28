# E84 — host runtime refactor result

Date: 2026-08-28

Apparatus implementation commit:
`a84f51ce1797cd00574fbc0f1f8d59945e8da2ff`

Apparatus acceptance commit:
`67ee6dee1748d03065ccb3d69ac92eb197dec531`

Disposition: apparatus fact; offline host refactor qualified; no behavioral or
GPU claim.

## Why this stage exists

E83 revealed that provider-free Stage 0 and live execution encoded different
rules for when a host-acquired result became model-visible. The same apparatus
family also spread delivery, residency, capacity, task configuration,
checkpointing, and replay across large runners, mutable task wrappers, Stage 0
simulations, and auditors.

E84 treats that as a systems blocker rather than patching the Trellis source
count. Historical runners and results remain frozen. A new contained
`host_refactor/` subproject implements the selected future path.

## What changed

The new host path has:

- one append-only event kernel for acquired, pending, delivered-resident, and
  delivered-external exact results;
- delivery committed only after a completed model invocation includes the
  pending result;
- immutable task/run configuration rather than mutation of another runner's
  globals;
- pure packet projection with one canonical exact body per bound
  object/version/span/payload;
- compact visible feedback when the actor requests an identical resident body;
- exact receipt substitution and reversible exact reopen;
- deterministic strictly-positive first-fit pressure relief independent of
  semantic or source-count activation gates;
- replaceable exact current-candidate state rather than repeated candidate
  copies;
- mechanically derived current/stale binding for the latest delivered check;
- one-shot provider request/response/failure custody;
- exact host and Trellis domain checkpoints, mechanical review packets, and
  resumable twelve-call tranches;
- a thin provider-capable tranche coordinator; and
- no host semantic relevance, loop, phase, readiness, or closure judgment.

## E83 replay

The shared event kernel reconstructs the sealed Trellis boundary as:

```text
delivered:
CLIMATE, CLINIC, COUNCIL, GRID, SHELTER, WATER

pending:
COMMS, TRANSIT
```

The pre-relief packet matches frozen live `FINAL_MESSAGES.json` and measures
21,401 tokens. Common first-fit relief selects RESULT-001 and produces a
feasible 18,785-token new-format packet. Completing one synthetic next
invocation moves TRANSIT/COMMS into delivered state, producing eight delivered
sources without pretending they were visible earlier.

## Verification

- focused refactor tests: 31 passed;
- complete apparatus suite: 266 passed;
- Ruff: passed;
- isolated type check of 11 new host modules: passed;
- randomized lifecycle replay properties: passed;
- GPU/model/provider calls: zero.

## What this supports

Supported:

- the selected future path has one replayable delivery law;
- offline replay and provider-capable execution use the same kernel and packet
  projection;
- exact duplicate bodies, current candidate replacement, check currentness,
  common relief, and checkpoint/resume are provider-free reachable;
- the E83 pending-versus-delivered correction is reproduced mechanically;
- long runs can pause for qualitative transcript review without a host loop
  classifier.

Not supported:

- improved model behavior or artifact quality;
- semantic continuity;
- any note, scaffold, digest, or residency-selection policy;
- adequacy of twelve/sixty calls for every task;
- live GPU robustness;
- product architecture promotion.

## Program consequence

The host modularity blocker is closed for offline experiment planning. New live
work must use the refactored path rather than the frozen global-mutating runner
family. A future experiment still requires a separately frozen launcher,
authorization, budgets, task/evaluator, and sealing plan.

The next research design should return to the actual interaction question:
whether evidence ingress, exact turnover, optional semantic persistence,
incremental exact work, effects, verification, repair, and closure become
cumulative under authentic model pacing. It should run in reviewable tranches,
with common relief always available and delivery counted only after completed
model exposure.

No GPU operation is selected.

