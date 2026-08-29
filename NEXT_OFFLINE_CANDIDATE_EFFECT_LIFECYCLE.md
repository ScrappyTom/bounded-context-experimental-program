# Next offline work — bounded candidate-effect lifecycle

Date: 2026-08-29

Status: completed at E97; no GPU/provider call occurred and no live successor
is selected or authorized. See
`E97_TRELLIS_CANDIDATE_EFFECT_LIFECYCLE_RESULT.md`.

## Trigger

E96 reached construction but could not begin verification. The current exact
candidate already contained six cumulative mutations, while six separate exact
candidate-effect bodies remained model-facing and were declared
non-relief-eligible. The next packet exceeded the prompt allowance with no
positive relief candidate.

## Goal

Make exact mutation uptake and currentness auditable without retaining every
historical effect beside the complete current candidate.

This is not an isolated compression benchmark. It repairs the complete
construction-to-verification interaction so the next whole-system trajectory
can reach effect uptake, current checking, repair, recheck, and readiness.

## Proposed ownership

The host preserves externally:

- every exact mutation request and effect;
- parent and resulting candidate hashes;
- result acquisition and delivery events;
- exact chronology and reopen handles; and
- whether a completed actor request actually exposed each effect.

E97 additionally showed that the causal assistant mutation action must share
the lifecycle. Its text can duplicate the exact current artifact just as the
effect body duplicates current candidate state. Applied action/effect pairs are
therefore bounded together after the same delivery and lineage proof.

The model-facing packet contains:

- the complete current candidate once;
- the newest pending effect exactly until a completed model invocation exposes
  it;
- a replaceable latest-effect/currentness projection after delivery;
- exact handles to older effects; and
- the current check status bound to the candidate hash.

Older delivered effect bodies may leave residency only after their resulting
candidate version is the current exact candidate and their delivery is recorded.
Externalization must never rewrite history or imply semantic uptake.

## Offline acceptance cases

1. A pending effect remains exact and non-droppable until a completed request
   contains it.
2. A failed or rejected provider call cannot mark the effect delivered.
3. After delivery, the latest effect becomes a replaceable currentness slot;
   older effects remain exact externally with handles.
4. The current candidate hash equals the delivered effect's resulting hash.
5. A later mutation makes an older check stale mechanically.
6. Check, repair, effect uptake, current recheck, and readiness remain reachable
   within the frozen Trellis envelope.
7. Replay and checkpoint hydration reproduce the same current candidate,
   latest-effect status, and external effect lineage.
8. No semantic scaffold change is introduced in the same apparatus revision.

## Stopping rule

Complete offline design, implementation, adversarial tests, exact E96 replay,
and a provider-free full lifecycle. Then stop for review. A live run requires a
new frozen commit and explicit authorization. Do not continue E96 from its
capacity-blocked checkpoint under a changed policy.

This stopping rule has been met. The authentic offline replay changes 21,023
tokens to 19,116 while retaining pending `RESULT-018` exactly; five focused and
303 full-repository tests pass. The route is closed at E97 pending selection of
a new whole-system live question.
