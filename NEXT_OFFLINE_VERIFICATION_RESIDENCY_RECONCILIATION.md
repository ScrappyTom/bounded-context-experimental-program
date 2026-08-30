# Next offline work — verification residency reconciliation

Date: 2026-08-30

Status: selected no-GPU systems audit after E103. No live continuation is
authorized or eligible.

## Why this work exists

E103 reached a new failure boundary after one repair cycle. The host had enough
economic budget, Qwen was making coherent progress, and E97 had already bounded
construction mutation history. The next exact packet still exceeded allowance
because verification-specific observations and receipts accumulated beside the
complete current artifact and pending effect.

The same run also exposed two correctness faults at the artifact/evaluator
boundary. Those must be kept separate from the residency question.

## Governing question

> Which verification objects must remain exact-resident for the next decision,
> and which can be represented mechanically from exact lifecycle facts while
> remaining exactly custodied and reopenable?

This is not an eviction-ranking or prompt-tuning study. The host may use only
facts it can prove: phase identity; candidate and artifact hashes; result
delivery; check currentness; action disposition; candidate lineage; pending
versus delivered effect; and exact external handles.

The host may not infer that Qwen understood an observation, that a failed
criterion is unimportant, or that a semantic detail is safely forgotten.

## Work packages

### A. Preserve and harden mutation/evaluation correctness

1. Keep the frozen E103 run and evaluator unchanged.
2. Prospectively canonicalize section boundaries after bounded replacement.
3. Reject replacement when the selected span contains a glued hidden heading.
4. Keep the T08 correction versioned rather than rewriting the frozen evaluator.
5. Add exact regressions for all three conditions.

### B. Reconstruct the call-27 packet by system role

Produce a deterministic table for every model-facing entry: exact token cost,
lifecycle class, current binding, duplicate mechanical state, custody/reopen
path, and pending/active/stale/resolved/historical status.

Account separately for the current candidate, phase state, current and stale
checks, section-version rejections, accepted repair and pending effect, current
verification/effect slots, applied construction receipts, and base chronology.

### C. Test conservative lifecycle projections offline

Only projections justified by exact state may be tested. Candidate examples,
not preselected conclusions, are:

1. delivered check body → exact receipt after a later candidate mutation makes
   that check stale, while currentness retains hashes, failed IDs, readiness,
   and the raw handle;
2. resolved action rejection → hash-bound receipt after a later accepted action
   changes the candidate, while exact rejected response and receipt remain in
   custody;
3. delivered phase effect → compact phase receipt once replaceable current phase
   state is exposed;
4. pending candidate effect → remain exact until a completed model call includes
   it.

For each projection, compute the exact call-27 packet and show whether it fits.
Do not select a policy merely because it saves the needed 326 tokens.

### D. Provider-free lifecycle regression

If one conservative projection survives B/C, replay from an uncorrupted,
prospectively imported checkpoint under a new execution manifest. The fixture
must cover current check delivery, bounded repair, repair-effect delivery,
stale-check projection, new current check, and another repair or explicit
incomplete stop. It must demonstrate exact reopen of every projected body and
must not manufacture semantic uptake.

## Stop rules

Stop without a live runner if feasibility requires semantic relevance judgment,
the donor must preserve the glued-heading corruption, exact custody/reopen is
lost, a projection costs as much as its body, or the provider-free feedback
loop remains unreachable.

## Deliverables

- packet-role and token audit;
- prospective section/evaluator hardening receipt;
- zero-call lifecycle fixture if eligible;
- claim limits and explicit non-promotion;
- recommendation to freeze a new whole-lifecycle scout or stop.

No GPU use is part of this stage.
