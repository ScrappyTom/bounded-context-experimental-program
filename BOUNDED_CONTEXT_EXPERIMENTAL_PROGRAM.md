# Experimental program for bounded context management

Date: 2026-08-21

Status: living research program; candidate mechanisms are not architecture

## Purpose

The current question is no longer whether enough old prompt material can be
removed to keep one local trajectory physically operable. That has been shown
on one task and model profile. The current question is:

> How can a bounded actor repeatedly preserve enough exact and semantic
> continuity to do useful work without rebuilding an indefinitely growing
> transcript?

The durable external system may preserve all authoritative bytes, versions,
events, effects, hashes, and bindings. Model-facing residency remains bounded.
Any sustainable candidate must therefore replace resident state, recompose a
bounded state, decompose work, or combine mechanisms that have independently
earned a role.

The research program does not choose that architecture in advance.

## Epistemic labels

Every program claim must carry one of these statuses:

- **AF — apparatus fact:** mechanically verified custody, capacity, delivery,
  effect, replay, or identity fact. It is not a behavioral advantage.
- **LR — local result:** observed behavior under a named task, world, model,
  treatment, and seed set. It does not automatically transfer.
- **CH — candidate hypothesis:** an interpretation earned strongly enough to
  justify a bounded test.
- **IN — inconclusive treatment:** a measured formulation was censored or
  underexposed before its planned behavioral comparison became evaluable.
- **UT — untested mechanism:** plausible design idea with no earned result.

“Supported” without one of these scopes is not sufficient for promotion.

## Current position

### Substrate and local results

- **AF:** exact external custody can preserve authoritative tasks, sources,
  candidates, observations, effects, chronology, hashes, and reopen handles
  while model-facing residency changes.
- **LR:** exact reopen handles were behaviorally usable; Qwen3.8 repeatedly
  requested and received demoted exact content.
- **LR:** pressure-triggered, minimum-necessary replacement of old exact-backed
  result bodies with receipts restored otherwise blocked result delivery in two
  seeds without changing the historical next decision.
- **LR:** the same oldest-first rule repeatedly maintained physical operability
  over 12 additional decisions per seed, but late behavior included substantial
  reopen churn and an exact period-three loop in one seed.
- **AF:** at those late endpoints, accumulated actions, receipts, errors, and
  access history prevented four task-declared documents from co-residing even
  after remaining old result bodies were minimized.
- **AF:** the same four documents and bounded target regions physically fit in a
  fresh exact packet.
- **LR:** chronology-free exact reentry produced one admitted, grounded mutation
  in two seeds. The other seed requested an omitted target region whose result
  could no longer fit. Both endpoints again reached result-delivery pressure.
- **LR:** recurrent chronology-free exact-state replacement carried both an
  inherited observation and an inherited candidate effect into new decisions,
  and recurrently carried at least one later result in each diagnostic case.
- **LR:** that exact-state representation was not a stable working state. The
  actor requested exact bytes already resident, and the single latest-update
  slot displaced recently delivered observations and effects.
- **IN:** an additive one-shot freeform-note treatment did not produce an
  evaluable three-call comparison. One note exhausted its frozen completion
  allowance mid-JSON; the one valid note was followed by a resident exact read
  whose result could not fit even after recomposition.

### Mechanisms insufficient alone on the tested trajectory

- **LR:** append-only chronology eventually became the dominant resident cost.
- **LR:** oldest-first eviction preserved capacity but not a stable working set.
- **LR:** one chronology-free reentry restored substantial headroom but did not
  preserve it through several ordinary action/result pairs.
- **LR:** 12 additional physically feasible decisions per seed did not produce
  mutation under recurrent oldest-first reduction.
- **LR:** exact current-state replacement alone did not make current residency
  behaviorally legible or preserve more than one exact recent update.
- **IN:** the tested additive one-shot note formulation did not establish a
  semantic-continuity benefit.

These are local boundaries, not universal impossibility results.

### Untested or unresolved

- **CH:** whether Qwen can reliably express a nonempty freeform note within a
  hard exact-token bound when JSON closure is removed as a failure amplifier;
- **CH:** whether a compact mechanical directory of current exact residency and
  region coverage reduces requests for bytes already present in the packet;
- **CH:** whether separate bounded latest-effect and latest-observation slots
  preserve exact causal continuity better than one replaceable update slot;
- **IN:** bounded model-authored working notes as behavioral continuity state;
- **UT:** specialized note compaction;
- **UT:** model-managed exact residency;
- **UT:** source-bound semantic digests;
- **UT:** deterministic chronology folding beyond exact-body replacement;
- **UT:** bounded semantic control/progress state; and
- **UT:** bounded phase decomposition with explicit recomposition review.

## Fundamental constraint

Any resident representation that only grows will eventually fail. Ordinary
chronology, receipts, notes, and digests all have this property if they are
merely appended. A sustainable mechanism must eventually:

1. **replace state** — rewrite a bounded representation;
2. **recompose state** — rebuild a bounded current state from exact custody; or
3. **decompose work** — split the task into bounded frames and reconcile them.

## Experimental axes

Every experiment must state three things independently.

### Representation

What remains model-visible?

Examples include an exact current-state projection, exact working-set slots,
compact receipts, a bounded note, source digests, a causal frontier, or a
progress record.

### Maintenance mode

What operation is performed?

Examples include ordinary task work, exact recomposition, note compaction,
source digestion, working-set selection, effect reconciliation, review, or
closure reconciliation.

### Trigger

Why does the operation happen now?

Prefer mechanically auditable triggers: prospective context overflow, a fixed
resident budget, note size, source-version change, candidate-hash change, or a
fixed reopen-churn threshold. “The model seems confused” and “construction
should start” are semantic triggers and require separate qualification.

## Experimental incumbent

Until another mechanism beats it, the incumbent is:

```text
exact external custody
+ ordinary chronology while it fits
+ minimum-necessary mechanical pressure response
+ exact reentry when history itself becomes the burden
```

Optional semantic state is not part of the incumbent.

## Immediate sequence

### Qualification Q1 — bounded-note expression

This is an apparatus qualification, not a claim that notes improve task work.
Reuse the two exact H02 maintenance histories and change only the expression
protocol:

```text
exact maintenance input
  -> same model and seed
  -> raw note text, no JSON wrapper
  -> generation allowance larger than the accepted note budget
  -> mechanically accept only nonempty output <=320 exact model tokens
```

Use one attempt, zero retries, no host truncation, and no actor continuation.
Record normal-stop rate, accepted bounded-note rate, exact token count, direct
factual/qualification audit, fabrication, cost, and cache behavior. A larger
generation allowance diagnoses closure separately; it does not relax the
320-token accepted-note bound.

### Experiment M1 — compact exact-workspace directory

The next behavioral experiment uses the two recurrent exact-state call-2
decision packets. They are different endpoint types, not replicate seeds, but
both historical actors requested `R033` while its exact bytes were already
resident.

Starting from each byte-exact packet, append one deterministic compact directory
derived only from the packet itself. It may identify current candidate/version,
resident object IDs, exact candidate line and region coverage, current latest
update, and the external-history handle. It must not summarize content, score
importance, claim sufficiency, recommend an action, or say not to reread.

The directory must fit within the tighter historical call-2 headroom while
preserving the frozen 4,096-token response reserve. Prefer <=128 exact model
tokens. The primary result is the first action's byte-level residency class,
not merely whether the action key changes. Novel acquisition, mutation,
submission, invalid action, and capacity remain separate outcomes.

The historical call-2 actions are immutable observed controls. One measured
call per case is sufficient for the primary contrast; any short continuation
must be separately frozen before outcomes are visible.

## Result-dependent routing

The program is adaptive rather than a fixed eight-experiment queue.

| Observed residual pressure | Next isolated candidate |
|---|---|
| A bounded freeform note cannot be expressed reliably | defer notes or separately test a constrained note-maintenance protocol |
| Exact resident bytes are requested despite explicit compact currentness | exact causal frontier or semantic continuity, selected by whether the requested bytes were resident or displaced |
| Compact currentness reduces resident rereads | recurrent compact-directory transfer before adding semantic state |
| A recently delivered effect/observation is displaced | bounded exact causal frontier |
| A legible exact workspace still has selection pressure | model-managed exact residency |
| A bounded note is reliable and exact residency is legible | fixed-total-budget substitutive note test |
| A useful note fills and replacement value is established | specialized note compaction |
| Stable evidence remains resident but acquisition continues without progress | bounded control/progress state |
| Repeated raw reopening dominates | model-managed residency or source-bound digest, chosen by the exact pressure |
| Mechanical event overhead remains dominant | chronology folding or exact causal frontier |
| No useful exact working set can fit | bounded decomposition and later integration audit |
| Recomposition is stable and task work progresses | close transfer before added mechanism |

No downstream branch is authorized merely because it appears in this table.

## Candidate mechanism families

### A. Deterministic exact-state recomposition

Mechanically materialize the authoritative task, current candidate/world,
selected exact objects, latest pending observation/effect, a short mechanically
explicit causal tail, and a full-history handle. Replace prior materialized
state rather than append it.

### B. Model-managed exact working set

Give the actor exact object identities, sizes, residency, and a hard workspace
budget plus `OPEN`, `PIN`, and `RELEASE`. The host owns bytes and enforcement;
the model owns only retention preference. This tests semantic residency
selection without semantic compression.

### C. Bounded model-authored working note

Use a versioned, lossy, non-authoritative replacement note with a hard token
budget. Begin only after an exact-recomposition control. Test freeform before
light structure; test a four-dimensional form only if simpler forms expose a
specific missing distinction.

### D. Source-bound semantic digest

Bind a lossy model-authored digest to one exact source identity and version,
retain an exact reopen handle, and invalidate it mechanically on source change.
Test only where repeated raw source reopening is an observed cost.

### E. Deterministic chronology folding

Normalize repeated access events, superseded versions, and candidate lineage
into current exact state plus exact history handles. This is mechanical
materialization, not semantic summarization.

### F. Exact causal frontier

Retain only events whose causal role is mechanically explicit: latest admitted
effect, unconsumed observation, current versions, unresolved rejection, and
current candidate identity. Do not infer semantic importance in the host.

### G. Bounded control/progress state

Let the model author current objective, completed work, unresolved discrepancy,
blockers, and next progress event. Test only after evidence residency is stable
enough that the state is not merely compensating for missing exact input.

### H. Bounded decomposition

Split work into fresh bounded frames when no useful global set fits. Require a
separate exact integration/review phase and score cross-part relationship loss,
not just local completion.

## Common experiment protocol

Each measured treatment must use an authentic frozen pressure boundary and
hold fixed task, exact world/candidate, model package, quantization, runtime,
template, sampler, reasoning setting, tools, hard context, response reserve,
one attempt, and zero retries unless one item is explicitly the treatment.

Record:

- exact pressure and capacity predicate;
- representation, mode, trigger, and owner;
- exact maintenance input and output;
- bytes/tokens replaced, retained, and externally reopenable;
- delivery boundaries for observations and effects;
- ordinary continuation behavior;
- exact candidate transitions;
- cache, latency, and token cost;
- direct terminal artifact review; and
- failure migration.

Capacity, orientation, acquisition, delivery, action onset, action admission,
effect, effect uptake, verification, artifact quality, closure, and cost remain
separate outcome classes.

## Shared metrics

- prompt tokens, response reserve, headroom, resident exact/semantic tokens;
- tokens replaced and added, recomposition count, and result/effect crossings;
- cached and uncached prompt tokens, prefill/generation/wall time;
- unique exact objects, reopens, repeat reopens, re-demotion, and turnover;
- novel acquisition, reacquisition, mutation, effect uptake, review,
  submission, and rejected actions;
- note/digest size and rewrites when applicable;
- stale claims, lost qualifications, unresolved-item and handle retention; and
- substantive mutation, source grounding, integration, repair, and closure.

## Interpretation rules

- A prompt fitting is not task success.
- Host acquisition is not model-visible delivery.
- An admitted effect is not model uptake of that effect.
- Reopening is not automatically failure; churn requires repeated lifecycle
  movement without commensurate progress.
- Maximum token removal is not the objective. Minimize resident cost subject to
  useful behavior, response reserve, and exact recovery.
- A two-case result over different endpoint types is not seed replication.

## Promotion rule

A mechanism earns an architecture role only after it demonstrates a recurring
positive effect, known trigger and preconditions, clear owner, bounded resident
cost, exact recovery, acceptable semantic and cache/latency cost, downstream
artifact or meaningful operability benefit, and a close transfer beyond one
exact trajectory.

Mechanisms may remain scope-specific. No general controller, universal
semantic graph, permanent four-dimensional prompt, host relevance scorer,
automatic phase classifier, learned eviction policy, summarization service, or
multi-agent system is authorized by this program.
