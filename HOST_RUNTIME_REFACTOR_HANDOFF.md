# Host runtime refactor handoff

Date: 2026-08-28

Status: offline core accepted at `67ee6dee1748d03065ccb3d69ac92eb197dec531`;
bounded live seams hardened provider-free at
`cc78d3b4c7162c6d3615696defd68e9790ee04ea`; immutable locked model restored
and exact tokenizer behavior qualified provider-free at
`a7c7686977661dcd7adebc1da78a78aa2b423ff5`; one-call integrated live smoke
frozen and provider-free qualified at
`fbc1db052051b23cfb8667780eab0a9939dee11a`

Results: see `E84_HOST_RUNTIME_REFACTOR_RESULT.md`,
`E85_HOST_LIVE_HARDENING_RESULT.md`, and
`E86_HOST_LOCKED_ASSET_RESTORATION_RESULT.md`, and
`E87_HOST_LIVE_SMOKE_STAGE0.md`. The hardened path passes 11
adversarial tests, 18 combined host tests, lint, isolated type checking, exact
E83 replay, and a complete 282-test regression against the hash-verified full
model named by the frozen lock. No GPU/provider call occurred. Historical
runners remain frozen. The only selected GPU operation is the separately
authorized one-call E87 host smoke; it is not a behavioral experiment.

## Why the program is pausing

E83 exposed more than one off-by-one error. The apparatus has accumulated
separate implementations of the same lifecycle concepts across offline
preflight, live runners, task-specific wrappers, audits, and historical helper
modules. The Trellis offline path counted a newly acquired result as visible;
the live runner correctly required a later model invocation. Both paths were
well tested locally, but they were not executing one shared transition law.

This is a modularity failure. Adding another task or experimental treatment on
top of the current runner would compound uncertainty about whether a result is
about the agent system or the host apparatus.

The program therefore pauses GPU experimentation. The next work is an
apparatus review and refactor, not another memory, scaffold, trigger, or prompt
experiment.

## What E83 separated

### Host error

The host must not collapse:

```text
exact result acquired by host
pending result selected for a prospective prompt
result included in a completed model invocation
result currently resident in the model-facing packet
result externalized after prior delivery
```

E82's Stage 0 collapsed the second and third states. E83 preserved them and
correctly found six delivered sources plus two pending sources.

### Genuine model pacing

Qwen used a coherent depth-first strategy: it completed both halves of each
source pair before moving to the next pair. The system must not interpret slow
breadth acquisition as failure merely because an offline script expected one
large read per source.

Future trajectories should give the actor enough decisions to reveal whether
continued acquisition becomes cumulative work. The host should not demand a
particular acquisition speed or source count.

### Trigger mismatch

The frozen Trellis gate required breadth before common relief could deliver the
pending result that would increase breadth. This made activation depend on an
ordering assumption rather than the actor's actual paced trajectory.

Capacity relief is ordinary host infrastructure. It should not be conditional
on a semantic or source-count gate. A result is recorded as delivered only when
it appears in a completed model invocation.

## Corrected ownership split

### Host owns only mechanical execution

- exact custody of task, sources, results, candidates, effects, checks, and
  chronology;
- canonical object identity and exact content hashes;
- explicit result-delivery state;
- exact prompt construction and tokenizer accounting;
- response reserve and positive-savings pressure relief;
- prevention of duplicate exact bodies in one active packet;
- reversible externalization and exact reopen;
- candidate/effect/check version binding and currentness;
- call, token, latency, cache, and recurrence telemetry;
- durable pause/resume snapshots;
- hard resource ceilings and exact terminal dispositions.

The host does not decide which information is semantically important, whether
the actor should be finished, or whether repeated behavior is rational.

### Model owns task behavior

- what to read or reopen;
- whether to continue investigating;
- when and how to begin constructing;
- how to decompose and revise task work;
- when to check and repair;
- when to propose closure.

### Investigator owns checkpoint judgment

At frozen pauses, Codex reviews the literal transcript and decides whether the
unchanged trajectory is:

- progressing slowly but coherently;
- recovering necessary information;
- accumulating exact work;
- cycling without useful state change;
- blocked by the action interface;
- or blocked by host capacity/lifecycle behavior.

Continuation preserves the frozen policy. A desired policy change creates a
new experiment rather than repairing the live run.

## Minimal delivery state model

Every exact result should have one authoritative lifecycle represented by
events, not independently inferred booleans in several scripts.

```text
ACQUIRED
host has exact bytes; model has not seen them
    ↓
PENDING
exact result is scheduled for the next model-facing request
    ↓
DELIVERED_RESIDENT
a completed model invocation included the exact result; one body is resident
    ↓                    ↑
DELIVERED_EXTERNAL ── exact reopen
model saw it earlier; body is absent; exact handle remains
```

Currentness is separate from delivery. A delivered check can become stale
after a candidate mutation without becoming undelivered. A historical source
version can remain exactly recoverable without being current.

The event log must be able to replay this state exactly. Offline and live modes
must call the same transition functions.

## Deduplication law

The active packet is a set of exact bodies plus chronological control events,
not a bag that may contain repeated copies of the same body.

For the first refactor:

1. Canonical exact-body identity is content hash plus bound object/version and
   exact source span where applicable.
2. At most one copy of an identical exact body may be resident.
3. If the actor requests an identical resident object, record repeated demand
   and return a compact mechanical `already_resident` result; do not append the
   bytes again.
4. If the object was previously delivered but is external, exact reopen may
   restore one copy.
5. Pending and resident copies may not coexist as separate bodies.
6. Partial overlap is not automatically merged in v0. Only exact duplicate
   identity is deduplicated, avoiding hidden semantic or span-selection logic.

The deduplication result must remain visible as an ordinary action result so
the model knows what happened. It is mechanical feedback, not advice.

## Capacity lifecycle

```text
actor requests exact information
        ↓
host acquires and custodies it
        ↓
render next packet exactly
        ↓
if packet fits:
    schedule result as pending
if packet does not fit:
    apply deterministic strictly-positive relief
    stop immediately when the pending packet fits
        ↓
invoke model with the pending result
        ↓
record delivery only from that completed invocation
```

There is no source-count gate around ordinary relief. If no eligible mechanical
relief can admit the requested result while preserving the response reserve,
the runtime pauses with an exact capacity blocker for investigator review.

## Pacing and review tranches

The provisional operating defaults are:

- maximum 60 actor calls per trajectory;
- mandatory pause every 12 actor calls;
- one attempt per call and zero retries;
- earlier pause when no mechanical relief can admit a pending result;
- no automatic stop merely because the candidate is unchanged;
- no automatic semantic classification of a loop.

These numbers are review defaults, not yet frozen scientific constants. Twelve
calls is long enough to observe several acquisition/work transitions and short
enough to avoid another uncontrolled multi-hundred-thousand-token drift.

At each pause the host produces a review packet containing only mechanical and
literal evidence:

- all actor actions and exact results in order;
- new, repeated, resident, externalized, and reopened exact objects;
- pending versus delivered objects;
- prompt/completion tokens, cache reuse, latency, and relief events;
- candidate versions and mutations;
- effect delivery and check currentness;
- invalid/rejected actions;
- exact artifact diffs;
- recurrence counts such as identical actions and repeat reads;
- remaining call/token budgets;
- exact handles to full requests, responses, and result bodies.

Codex then adds a qualitative review, clearly separating transcript facts from
interpretation. If work is progressing, the same frozen trajectory may receive
another tranche authorization. If it is cycling or blocked, the run stops.

## Refactor architecture

The desired substrate is small and explicit:

```text
EVENT / CUSTODY STORE
exact immutable objects and chronological events
            ↓
DELIVERY STATE MACHINE
acquired / pending / delivered-resident / delivered-external
            ↓
PACKET COMPOSER
one exact body per identity; task/candidate/currentness bindings
            ↓
CAPACITY POLICY
real tokenizer; reserve; strictly-positive first-fit relief
            ↓
PROVIDER ADAPTER
one call, one attempt, exact request/response custody
            ↓
CHECKPOINT CONTROLLER
12-call pause, resource stop, resumable snapshot
```

Task-specific code should be declarative configuration and domain actions, not
global mutation of a historical runner.

## Required refactor review

Before editing, map every current owner of:

- result visibility and delivery;
- resident/external state;
- prompt composition;
- relief selection;
- activation gates;
- call budgeting;
- checkpoint/finalization;
- task-specific runner configuration;
- offline replay and live execution.

The review should identify duplicate implementations, hidden global mutation,
historical schema leakage, and code paths whose offline semantics differ from
live execution.

Known starting points in the current apparatus include:

- the large shared pressure-screen runner;
- task wrappers that overwrite shared module globals;
- separate Stage 0 simulations;
- activation snapshots that mix pending and delivered metadata;
- result-ledger visibility and residency booleans;
- task-specific audits that reimplement common replay logic;
- historical schema names reused by later tasks.

## Acceptance criteria before another GPU experiment

1. One delivery transition kernel is used by live runs, offline simulations,
   replay, and tests.
2. Replaying the E83 events reconstructs six delivered sources plus pending
   TRANSIT/COMMS exactly.
3. No task wrapper mutates global state in a historical runner.
4. Exact duplicate bodies cannot coexist in a rendered packet.
5. A repeated resident request produces a compact, auditable mechanical result.
6. Strictly-positive relief is common infrastructure with no semantic gate.
7. A run can stop after twelve calls, seal a review packet, and resume from the
   exact snapshot without rebuilding or altering history.
8. Offline and live paths render byte-identical packets from the same event
   fixture.
9. Provider failure, invalid action, capacity failure, and budget exhaustion
   each have exact non-overlapping terminal states.
10. Historical regression tests still pass, plus property/state-transition
    tests for the new kernel.
11. No GPU call is needed to establish any of these facts.

## Explicit non-goals

Do not add during the refactor:

- semantic notes or progress state;
- a new scaffold/digest experiment;
- model-managed eviction;
- automatic loop classification;
- relevance scoring;
- automatic phase discovery;
- learned memory policy;
- multi-agent orchestration;
- a product-wide universal memory abstraction.

The purpose is to make the host boring, exact, and reviewable.

## Return sequence

When work resumes:

1. review the apparatus module map and confirm the smallest cut line;
2. freeze the state/event invariants above;
3. implement the shared delivery and packet kernel behind tests;
4. migrate one provider-free fixture and E83 replay;
5. add exact deduplication;
6. add resumable twelve-call checkpoints;
7. migrate one thin live runner without global mutation;
8. run complete offline regression and inspect produced review packets;
9. update the program with the refactor result;
10. only then design the next long-horizon experiment.

No next GPU operation is selected or authorized.
