# E103 — Trellis repaired verification continuation result

Date: 2026-08-30

Apparatus freeze:
`97d84493ef72d271410ae590f6ead7e86c2b551a`

Apparatus result commit:
`13833edaed66634a2f8318d8f747b9f6acd66019`

Run ID:
`2026-08-30-trellis-e99-verification-lifecycle-continuation-v1`

## Outcome first

The authorized continuation made two normal actor calls and then stopped safely
on capacity. Qwen used the delivered current check to propose a bounded
authority/currentness repair, received a section-hash rejection, and repeated
the same semantic repair with the exact current hash. The second action was
admitted.

The accepted mutation did not improve the artifact. A previously glued heading
made the host's section span include the heat section; replacing that span
deleted the heat section, and another missing boundary glued the power heading.
The resulting candidate is structurally worse and remains `not_ready`.

The next pending effect could not be delivered: 21,318 prompt tokens were
required against a 20,992-token allowance. This was a 326-token gap with ten
actor calls and 298,937 serialized tokens still available.

## Literal accounting

- actor/provider calls: 2;
- maintenance calls: 0;
- serialized tokens: 39,865;
- retries: 0;
- final candidate:
  `d3a3d3691a254e8d463d98481977070d3e431180541ca5843a23b4c7d880041f`;
- pending undelivered effect: `RESULT-026`;
- terminal: `capacity_blocked`;
- run sealed and runtime released.

## What the transcript shows

Qwen was not looping. It performed a sensible check-to-repair transition and
used exact host feedback correctly. The substantive replacement retained
authority actors, current T9 bindings, historical T8 status, recheck and
rollback conditions, independent authorized acceptance, open findings, and an
explicit refusal to declare readiness.

The failure occurred where semantic work crossed the artifact mutation
boundary. `replace_artifact_section` assumed that the model would supply the
physical blank-line separator needed to protect the following Markdown
heading. It also treated a prior glued heading as ordinary section content.
That made a valid section-sized semantic action unsafe as an exact artifact
operation.

This is a host fault, not evidence that Qwen chose to discard heat controls.

## Evaluator reconciliation

The frozen evaluator reports:

- 871 words;
- 8 decision-source IDs;
- heading contract failed;
- T01 passed;
- T02–T08 failed;
- `not_ready`.

Its T08 regex contradicts its own written requirement. The written requirement
accepts "independent authorized acceptance," which the candidate contains; the
regex required acceptance to precede authorized/owner. A versioned prospective
correction makes T08 pass. T02–T07 and the structural, length, and breadth
criteria still fail, so the run remains a clear non-completion.

## Failure migration

E97 bounded old applied construction actions and effects. E103 reveals the
next residency pressure inside verification:

```text
current candidate
+ delivered phase effect
+ two check bodies
+ two rejection receipts
+ pending exact repair effect
→ next packet 326 tokens over allowance
```

The host knows which check is stale after candidate change, which rejection was
followed by an accepted action, which effect is still pending, and which phase
is current. It does not yet have a frozen verification-phase turnover policy
for those exact objects.

This is not permission for relevance-based eviction. It is a candidate for
mechanical lifecycle projection with exact custody and reopen preserved.

## Disposition

Local positives:

- check-driven targeted repair;
- exact rejection feedback uptake;
- no action loop or premature closure.

Local negatives:

- unsafe section-boundary transport;
- no net artifact-quality improvement;
- repaired effect never delivered;
- current recheck and closure not reached;
- verification chronology again exhausted model-facing capacity.

The sealed route is closed and must not resume from the corrupted candidate.
Prospective section-boundary and evaluator corrections are apparatus hardening,
not a regrading or rerun. The selected successor is the no-GPU verification-
residency reconciliation in
[NEXT_OFFLINE_VERIFICATION_RESIDENCY_RECONCILIATION.md](NEXT_OFFLINE_VERIFICATION_RESIDENCY_RECONCILIATION.md).
