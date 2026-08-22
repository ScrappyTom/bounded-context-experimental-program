# Minimal earned policy v0

Date: 2026-08-22
Status: experimental incumbent for whole-method validation; not a promoted architecture

## Purpose

This document freezes the smallest coherent policy supported strongly enough to
serve as the treatment candidate in a fresh end-to-end comparison. It does not
claim that every component is independently sufficient or universally useful.

## Policy

### 1. Preserve exact external custody

Keep authoritative task/purpose, sources, world state, candidate versions,
actions, observations, effects, complete chronology, reopen handles, and
candidate-bound evaluation records outside the bounded model context.

Model-facing residency may change. External authoritative bytes do not.

### 2. Use ordinary chronology while healthy

Do not continuously rewrite a prompt that still admits the next exact result,
the frozen actor response reserve, and the protected control reserve. Ordinary
action/result chronology remains the default within a bounded phase.

### 3. Make capacity safety host-owned

Before every model or result-delivery boundary, compute the exact rendered
prompt under the locked tokenizer and template. Reserve separately:

- the ordinary response/action allowance; and
- enough control capacity to express and execute the mechanically declared
  pressure operation.

The model does not own hard-overflow prevention.

### 4. Apply minimum-necessary deterministic pressure relief

When a pending exact result would violate the frozen envelope, scan only
mechanically eligible result bodies that:

- were previously delivered across an actual model decision boundary;
- remain byte-exact in external custody;
- retain unchanged identity/version bindings; and
- can be reopened exactly through the ordinary action surface.

Replace the minimum mechanically selected amount needed to admit the pending
result while preserving both reserves. Use the proven deterministic selection
order until a whole-method failure shows that release identity dominates.

Do not ask the model to choose the amount of relief. Do not add host semantic
importance labels. Do not demote the newly pending result during its own
delivery.

### 5. Treat actor access as the demand signal

Exact reopening remains ordinary behavior. A reopen is a cost, not automatically
a failure. Track repeat reopen, demote→reopen interval, re-demotion, working-set
turnover, new acquisition, effects, and artifact progress.

The actor's actual request is stronger evidence of current demand than a
separate model role's prediction of what the actor will want next.

### 6. Reenter a bounded exact phase when chronology is the burden

If minimum-necessary exact-body relief cannot preserve the frozen reserves, or
a prospectively declared task/phase boundary is reached, start a fresh bounded
context constructed from external custody.

The first whole-method study must predeclare the phase rule. The fresh packet
may include only mechanically and contractually specified current state, such
as:

- authoritative task and current phase contract;
- exact current candidate/world and version;
- exact pending observation or effect;
- exact task-declared evidence for that phase;
- a bounded mechanically explicit causal tail when required for binding; and
- exact external-history and reopen handles.

Do not use post-outcome host relevance judgment to choose a successful packet.
Automatic semantic phase classification is not part of v0.

### 7. Keep optional semantic mechanisms out of the default policy

V0 contains no default:

- source digest;
- bounded working note;
- progress/frontier state;
- model-managed eviction;
- automatic semantic summary;
- host relevance scorer; or
- learned routing policy.

These mechanisms remain available only as later isolated responses to an exact
failure observed under v0. Their omission is not a universal negative claim.

### 8. Bind utility to independent evaluation

Before scoring closure, repair, or artifact benefit, bind the judgment to:

- exact candidate/tree and artifact file hashes;
- authoritative task hash;
- evaluator/rubric identity and hash or explicit unavailability;
- evidence-manifest hash;
- criterion-level findings;
- explicit `ready`, `not_ready`, or `not_adjudicated` state;
- blocking requirements; and
- independent, inherited, reconciled, or superseded provenance.

Submission, fewer calls, fewer reads, or lower token use do not establish useful
closure.

## Known limits

V0 does not solve semantic working-set selection. Oldest-first selection can
churn, exact reentry can change orientation, task-authored phase boundaries may
not transfer, and repeated reopening may still dominate. The policy earns a
whole-method test because its safety components work and its exclusions avoid
locally harmful or unevaluated defaults—not because its end-to-end benefit is
already known.

## Candidate whole-method comparison

Use fresh tasks rather than reusing the two navigation-pressure trajectories.
The initial task portfolio should contain:

- one large-document research/writing task; and
- one multi-file code task.

Use two frozen seeds per condition when task and runtime cost permit.

### Control

```text
ordinary chronology
+ exact external access
+ unchanged hard context/response envelope
+ stop when the next required packet cannot fit
```

### Treatment

```text
ordinary chronology while healthy
+ exact external custody
+ protected response/control reserves
+ minimum-necessary exact-backed pressure relief
+ exact reopen on demand
+ prospectively frozen bounded phase reentry
+ candidate-bound independent evaluation
```

Hold model, quantization, runtime, template, sampler, tools, action admission,
context, response reserve, task, world, attempts, and evaluator fixed.

### Primary outcomes

- independently adjudicated complete artifact quality;
- correct closure/readiness behavior; and
- admitted effect uptake into a later model decision.

### Secondary outcomes

- pressure events encountered and survived;
- results/effects crossing model boundaries;
- exact reopens and repeat-reopen churn;
- mutations, repairs, checks, and submissions;
- prompt, completion, cache, latency, and maintenance/reentry cost;
- phase count and failure migration; and
- direct transcript and artifact audit.

### Interpretation

This is intentionally a compound policy comparison. Its purpose is to determine
whether the earned components form a system worth pursuing, not to identify the
individual cause of every difference.

If treatment improves end-to-end quality/readiness and bounded operability on
fresh tasks, the policy becomes an architecture candidate requiring close
transfer and ablation. If it fails, select the next isolated experiment from
the first exact failure boundary that differs materially from already tested
episodes.

## Authorization state

No task bank, run schedule, call ceiling, or GPU use is authorized by this
document. Whole-method design begins with offline task/evaluator qualification.
