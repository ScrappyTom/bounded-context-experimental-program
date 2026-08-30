# Project pause handoff — 2026-08-30

Status: deliberately paused by the project owner after E107 Stage 0. No live
run is authorized. The GPU/model server is not part of an active tranche.

This document is the restart-oriented summary of where the bounded-context
program has been, what it has actually learned, where the evidence remains
weak, and what was prepared next. It complements the detailed
[full experiment sequence](FULL_EXPERIMENT_SEQUENCE_WRITEUP.md), the current
[program reconciliation](PROGRAM_RECONCILIATION.md), and the governing
[systems frame](SYSTEMS_INFORMATION_ECONOMICS.md).

## Executive summary

The program began by asking whether a bounded model could keep enough exact and
semantic continuity to do useful work without carrying an indefinitely growing
transcript. It did not discover one universally good memory object, context
layout, summary, or cache policy.

It discovered a more useful division of responsibility:

1. The host can reliably preserve exact reality, account for capacity, deliver
   results exactly once, externalize and reopen exact objects, and make the
   smallest frozen mechanical intervention needed to keep another decision
   possible.
2. Those mechanisms create *opportunity* for useful cognition. They do not make
   the model use that opportunity well.
3. Semantic representations are not passive memory. They change acquisition,
   construction, stopping, and closure behavior. Their value and risk depend on
   when they are used and what other state is present.
4. The most promising durable model-facing state is the exact, versioned,
   incrementally editable task artifact itself. Temporary provenance-bound
   semantic scaffolding can help convert dispersed evidence into that artifact,
   but it has not earned permanent residency or readiness authority.
5. As one bottleneck is removed, failure moves: capacity to acquisition,
   acquisition to integration, integration to action transport, construction to
   effect uptake, and effect uptake to verification, repair, and closure.

The current architecture hypothesis is therefore a phase-dependent lifecycle,
not a context format:

```text
exact external custody
        ↓
host-owned pressure and delivery safety
        ↓
temporary provenance-bound semantic scaffold
during acquisition and early construction
        ↓
exact incremental task artifact
        ↓
bounded applied-action/effect and current-verification state
        ↓
check → repair → current recheck → correct closure
```

The complete lifecycle has **not** yet produced a high-quality, correctly
closed live task. That is the principal unresolved claim.

## Where we have been

### 1. Exact custody and physical operability

The first major branch separated context loss from information loss. Exact
source bodies, actions, observations, effects, candidates, versions, and full
chronology can remain externally custodied even when they are not resident in
the model prompt. Hash-bound handles and receipts make them exactly reopenable.

Deterministic pressure relief repeatedly restored prompt feasibility. A frozen
scan order externalizes eligible, already-delivered exact bodies and stops as
soon as the pending packet fits. Real tokenizer accounting, response reserve,
and protected control capacity prevent the recovery operation itself from
becoming unreachable.

This is the strongest result in the program. Its limit is equally important:
keeping another decision physically possible does not create useful progress.
Long trajectories sometimes stayed alive while doing nothing but acquiring or
reacquiring information.

### 2. Exact layout and residency selection

The program tested oldest-first demotion, recurrent relief, static exact working
sets, chronology-free reentry, recurrent exact recomposition, residency
directories, focus relocation, passive `OPEN`/`PIN`/`RELEASE` controls, and a
dedicated model-management turn.

These studies showed that recoverability, residency, behavioral accessibility,
and working-set adequacy are different properties. A directory did not stop
resident rereads. Moving requested bytes often moved demand to complementary
bytes. Passive controls did not activate before the control interface became
unreachable. Dedicated maintenance made selection reachable, but Qwen released
far more than required and the ordinary actor immediately requested the same
released source.

The route was therefore closed as a default architecture direction. The host
owns capacity safety and the amount of relief. Ordinary actor reads are the
best local demand signal observed so far. Open-ended model-cache-manager prompt
tuning is not owed.

### 3. Semantic representations

Several distinct semantic functions were tested rather than treating all
semantic state as one kind of memory.

- A bounded frontier showed encouraging prose continuity and exact handle
  copying, but the strict structured-output carrier did not qualify. Schema and
  grammar tuning was closed.
- A source digest was grounded and behaviorally active, but it redirected the
  actor first to a related audit and then back to the original source. It added
  production, carrier, recovery, and decision cost without progress. At that
  boundary it was a complement to exact evidence, not a substitute.
- A bounded progress state changed a redundant reread into submission. Exact
  candidate-bound adjudication later showed that the artifact had known
  defects. The intervention therefore had high control leverage but negative
  utility: it induced false closure.
- Global semantic replacement could encourage construction but also preserved
  stale or incorrect relationships and bundled too many jobs into one rewrite.
- Source-local representations avoided some global rewrite costs, but early
  carriers either forbade ordinary cross-source references or required the
  model to copy physical source lines byte-for-byte. Those were transport
  failures, not general semantic failures.
- Host-materialized exact anchors plus provenance-local claims finally allowed
  bounded grounded semantic residue to operate inside a complete pressured
  trajectory. Partial claim admission and unchanged-state fallback let the
  actor continue when some claims were invalid or unaffordable.

The durable lesson is that locality should constrain mutation scope and
authority, not erase relationships. The host should materialize exact
provenance; the model should select and express meaning. Semantic state must
remain non-authoritative for readiness and closure.

### 4. Information economics and interaction-first work

The project reoriented after recognizing that the value of information is
non-stationary and configuration-dependent. More information can reveal more
demand rather than satisfy it. A small semantic package can cost several times
its payload after provenance, message framing, and serialization. Fresh reentry
can reduce prompt length while destroying prefix-cache reuse and causal
continuity.

This changed the unit of study from an isolated component to a complete system
trajectory. The important variables now include:

- evidence ingress and acquisition bandwidth;
- exact residency and recovery;
- semantic relationship formation;
- work-product externalization;
- action and response transport;
- candidate/effect uptake;
- current verification and repair;
- readiness and closure;
- total calls, tokens, cache behavior, and failure migration.

The project no longer treats fewer reads, fewer calls, successful submission,
or a packet fitting as sufficient evidence of value. Artifact quality and
correct readiness must be independently, candidate-bound adjudicated.

### 5. Exact artifacts as external cognition

The ingress/work, artifact-coupling, Cedar, Solace, and Trellis studies produced
the clearest system-level signal.

Direct-exact arms often acquired broadly but delayed construction. In Solace,
the direct arm formed substantial fourteen-source understanding and produced
two broad decision drafts, but both monolithic JSON actions exhausted the
4,096-token response allowance and neither became an admitted artifact.

The coupled arm combined temporary grounded semantic residue, an exact evidence
ledger, section-sized action affordances, and a growing exact artifact. It began
construction earlier, admitted incremental mutations, and consolidated them
into a substantial decision. The result remained incomplete, but cognition had
crossed the action boundary and become durable, inspectable work.

Trellis later repeated the regime change. Its direct arm delivered the catalog
and then reread the entire catalog in the same order. The scaffolded/artifact
arm immediately wrote an evidence ledger and multiple decision sections without
raw-source rereads.

These are compound-configuration results. They do not prove that a register
alone caused understanding. They support a stronger and more practical claim:
temporary semantic scaffolding plus exact incremental work and bounded action
transport can change a trajectory from reacquisition to cumulative
construction.

They also exposed the main weakness. Same-source scaffold replacement selected
later table rows over stronger governing relations. Important authority,
threshold, capacity, duration, and gate information disappeared from the
model-facing scaffold and then from the durable artifact. Exact persistence can
capitalize semantic mistakes as efficiently as it preserves good work.

### 6. Construction-to-verification lifecycle

Once construction succeeded, full mutation actions and their exact effects sat
beside the complete current artifact and exhausted prompt capacity before
verification. The host now compacts only causally proven, delivered mutations
whose resulting state is exactly embodied in the current candidate. Full
actions and effects remain externally custodied and reopenable; pending effects
remain exact.

Later runs exposed and repaired additional host faults:

- phase guidance and action schema could disagree;
- rejected large responses could remain fully resident;
- section boundaries could be corrupted by glued headings;
- delivered check bodies could duplicate the replaceable current-verification
  state.

These failures motivated a modular host refactor with explicit event state,
request/delivery binding, current candidate and verification slots, pressure
planning, checkpoints, and seals. Provider-free regression and a live smoke
qualified one complete pressured request/delivery/action/acquisition/checkpoint
slice against the real Qwen runtime.

The host is now credible common infrastructure, not the active scientific
question. It is live-qualified only for the paths actually exercised; long-run
mutation, check, repair, and closure robustness remain empirical questions.

### 7. The clean prospective Trellis route

Historical donor-derived verification runs were informative but contaminated by
old candidate corruption and repaired apparatus state. They were closed rather
than repeatedly patched.

E105 created a clean prospective whole-lifecycle route. E106 ran its first live
tranche. Across 12 actor and six maintenance calls, Qwen completed a coherent,
non-recurrent traversal of all twelve source pairs. Every actor response was a
valid read action. Six relief events kept the trajectory operable. There were
no reopens, repeated reads, mutations, checks, or submissions.

The last source result was acquired after the twelfth actor call and remains
pending. Therefore the checkpoint is not evidence of construction failure. It
is exactly one completed provider invocation before the first true post-catalog
decision in which the complete evidence sweep has crossed the model boundary.

The semantic pathway also operated cleanly. Twenty grounded claims entered over
time, but replacement left ten current claims and reproduced the known
selection losses. The scaffold became visible partway through acquisition and
did not alter the disciplined catalog plan.

## What we have learned

### Claims with the strongest support

1. **Exact external custody is foundational.** Loss of residency need not mean
   loss of information, identity, version, or auditability.
2. **The host should own mechanical safety.** Token accounting, delivery state,
   reserve protection, currentness, exact reopen, and the amount of pressure
   relief are mechanically knowable responsibilities.
3. **Ordinary actor behavior is a better demand signal than advance
   self-prediction.** Model-authored residency selection was locally unstable
   across modes.
4. **Full chronology belongs in external custody, not permanent prompt
   residency.** Resident chronology must have a lifecycle under a fixed window.
5. **Semantic state is an intervention in action policy.** It can redirect
   acquisition, accelerate construction, or cause premature closure.
6. **The exact incremental artifact is the best current candidate for durable
   model-facing work state.** It is versioned, revisable, auditable, and can
   preserve integration after raw evidence leaves residency.
7. **Action transport is part of cognitive capability.** Prompt capacity alone
   is insufficient; response budget, action granularity, serialization, and
   admission determine whether formed understanding becomes executable work.
8. **Checks and effects require exact version/currentness bindings.** Historical
   observations may remain true records while being stale for the current
   candidate.
9. **Evaluation is a separate custody layer.** Exact execution can coexist with
   a wrong semantic judgment. Readiness and utility claims require frozen,
   candidate/task/rubric/evidence-bound adjudication and explicit
   supersession.
10. **The system, not the component, is the research unit.** Useful completion
    is limited by the narrowest of acquisition, integration, residency,
    decision bandwidth, work externalization, effect uptake, verification, and
    closure.

### Routes closed or strongly deprioritized

- More static exact-layout, focus-position, or directory variants at the same
  boundaries.
- More strict JSON/schema/frontier carrier tuning.
- Passive or open-ended model-owned eviction as the default safety policy.
- Generic always-on source digestion.
- Generic progress state or model-authored readiness control.
- Scheduled fresh reentry at low prompt occupancy.
- Complete-global semantic replacement during acquisition.
- More receipt-field or host-mechanism tuning without a concrete new live
  failure.

These are routing decisions, not universal impossibility claims. Reopening one
requires a new failure boundary that the completed studies do not already
explain.

### Important unresolved questions

- Can the clean integrated system progress from complete evidence delivery into
  admitted incremental construction?
- Can its lossy scaffold support rather than corrupt cross-source work?
- Can the exact artifact absorb enough meaning that the scaffold can later be
  demoted?
- Can the actor receive its latest effect, enter current verification, identify
  real semantic defects, repair them, recheck the changed candidate, and stop
  correctly?
- Can these effects transfer to a fresh world and more than one seed/model?
- Can prompt-facing applied-history receipts eventually be folded without
  harming orientation if a trajectory becomes much longer?

No completed study yet supports promoting the provisional lifecycle as a
general architecture.

## Where we are now

### Last measured state: E106

- Run: `2026-08-30-trellis-clean-whole-lifecycle-v0`
- Apparatus result commit:
  `fa67aecdf833b72f282a03819a3fbc35e263c320`
- Actor calls: 12
- Maintenance calls: 6
- Provider calls: 18
- Serialized tokens: 205,399
- Candidate: unchanged initial stub
- Candidate SHA-256:
  `e7a12171c6523e8881fddf7cdcd0cba3e99f97ff7ef1db9770f7295a596db0ba`
- Readiness: `not_ready`
- Source state: results 1–7 externalized, 8–11 resident, 12 pending
- Current scaffold: ten admitted source-bound facts, with known selection loss
- Terminal: qualified mandatory checkpoint, not task completion

The detailed result is [E106](E106_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CHECKPOINT_RESULT.md).

### Prepared but unauthorized: E107

E107 freezes an unchanged continuation from the exact E106 checkpoint:

- Apparatus freeze commit:
  `d62a7594e4703453bd990e1e7df06daf3422c04c`
- Selected maximum: 12 additional actor calls, six maintenance calls, 18
  provider calls, and 400,000 serialized tokens
- Mandatory review at the tranche end or any earlier terminal
- One attempt per call, zero retries
- No scaffold repair, policy change, or donor substitution

Provider-free qualification preserves the actual lossy scaffold, delivers the
pending final source, and proves mechanical reachability through later
lifecycle actions. It is not behavioral evidence. E107 has **not** received GPU
authorization and must not run merely because it is prepared.

See [E107](E107_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CONTINUATION_STAGE0.md).

### Repository state at pause

- Program repository branch:
  `codex/bounded-context-experimental-program-v0`
- Program state before this handoff commit:
  `a295f0b0d528ecfaaaf1fff7408c29afdb04aa9d`
- Apparatus repository:
  `E:\qwen38-artifact-coupled-integration-scout-v0`
- Apparatus frozen E107 state:
  `d62a7594e4703453bd990e1e7df06daf3422c04c`
- No live tranche is authorized.
- No automatic continuation is permitted.

## Where we are going

When work resumes, the highest-information next operation is the already-frozen
E107 continuation, not a new mechanism or a repaired scaffold. It observes the
first clean post-catalog decision under the system that actually produced the
E106 state.

The continuation should answer, in order:

1. Does delivery of the final pending result move the actor from acquisition to
   construction, or does it reacquire evidence?
2. If it constructs, does it use bounded incremental artifact actions that can
   cross the response/admission boundary?
3. Which scaffold facts enter the artifact, and which known selection losses
   become visible omissions or errors?
4. Does each admitted mutation effect cross a later model boundary and remain
   correctly bound to the current candidate?
5. Does the actor initiate a current check, repair real defects, recheck the
   changed candidate, and reach a correct readiness disposition?
6. Where does the next bottleneck migrate?

The continuation must not be interpreted as a referendum on one register. It
tests the complete configuration over time.

If E107 produces useful, correctly verified progress, the next step is
fresh-world transfer before component ablation or architecture promotion. If it
fails, the next study should be chosen from the first genuinely new failure
boundary in the transcript. It should not default back to the catalog of notes,
digests, layouts, managers, receipt schemas, or prompt variants.

## Restart checklist

1. Read this handoff, E106, E107, and the current program reconciliation.
2. Confirm both Git repositories are clean and at the commits named above.
3. Confirm the exact model/runtime asset lock and live tokenizer projection are
   available.
4. Confirm the E106 sealed parent checkpoint and pending `RESULT-012` resolve
   exactly.
5. Re-run only the frozen provider-free preflight required by E107; do not
   change policy or semantic state.
6. Obtain new, exact commit-bound GPU authorization from the project owner.
7. Run the frozen continuation with one attempt per call and zero retries.
8. Stop at the mandatory checkpoint or any earlier terminal, release the GPU,
   and perform transcript-level qualitative review before selecting anything
   else.
9. Reconcile artifact quality and readiness against the external evaluation
   ledger before calling submission, fewer calls, or lower token use a success.

## Reading map

- Detailed history: [FULL_EXPERIMENT_SEQUENCE_WRITEUP.md](FULL_EXPERIMENT_SEQUENCE_WRITEUP.md)
- Current synthesis: [PROGRAM_RECONCILIATION.md](PROGRAM_RECONCILIATION.md)
- Governing economics: [SYSTEMS_INFORMATION_ECONOMICS.md](SYSTEMS_INFORMATION_ECONOMICS.md)
- Interaction contract: [SYSTEM_INTERACTION_EXPLORATION.md](SYSTEM_INTERACTION_EXPLORATION.md)
- Roadmap and stopping rules: [STRUCTURED_EXPLORATION_ROADMAP.md](STRUCTURED_EXPLORATION_ROADMAP.md)
- Claim-level evidence: [EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md)
- Host refactor handoff: [HOST_RUNTIME_REFACTOR_HANDOFF.md](HOST_RUNTIME_REFACTOR_HANDOFF.md)
- Last live checkpoint: [E106](E106_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CHECKPOINT_RESULT.md)
- Frozen continuation: [E107](E107_TRELLIS_CLEAN_WHOLE_LIFECYCLE_CONTINUATION_STAGE0.md)

## Pause disposition

The project is paused in a safe, reproducible state. The scientific boundary is
clear, the next operation is frozen but unauthorized, and there is no need to
reconstruct the program from chat history. Resume from E106/E107 only after a
fresh deliberate decision to restart.
