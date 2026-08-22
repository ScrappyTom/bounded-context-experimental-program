# S3 plan — deliberately lossy source-digest utility

Date: 2026-08-21

Status: selected for standalone implementation and offline preflight; no GPU
execution authorized by this document

## Proposed repository

- Repository: `ScrappyTom/qwen38-lossy-source-digest-utility-v0`
- Local folder: `E:\qwen38-lossy-source-digest-utility-v0`
- Branch: `codex/qwen38-lossy-source-digest-utility-v0`

## Research question

At an authentic boundary where Qwen3.8 historically reopened an unchanged
8,063-byte exact source, does adding a small, explicitly lossy,
non-authoritative, source-bound digest alter useful short-horizon actor behavior
without material semantic degradation, while preserving exact reopen?

This tests a semantic cache in a layered system. It does not test whether the
digest is an exact substitute for the source.

## Frozen donors

### Historical actor boundary

Repository: `ScrappyTom/qwen38-recurrent-context-reduction-horizon-v0`

Pinned result commit: `f52642ec85efdc8f7196515503a0312af7c38d78`

Use seed 314159:

- source first read at horizon call 9;
- identical repeat reopen at call 12;
- unchanged candidate identity;
- exact call-12 request, response, action, projection, candidate, receipts, and
  action executor state;
- historical prompt: 19,686 tokens;
- frozen response reserve: 4,096 tokens;
- historical headroom: 1,306 tokens; and
- historical first action: exact `repo_read` of the selected source.

### Semantic derivative

Repository: `ScrappyTom/qwen38-source-digest-actor-utility-v0`

Pinned result commit: `d9336f5681ecffb8d322802c01ebaf8bb480f750`

Use the exact digest bytes from:

`runs/2026-08-21-sealed-source-digest-stage-a-s314159-v0/cells/01-digest-source-navigation-results-s314159/response/DIGEST_RECEIPT.json`

Bind its exact digest bytes, 218-token receipt, token-ID hash, source path,
source commit, Git blob, source-content hash, provider-response hash, and run
seal. Do not regenerate or edit it.

## Known semantic-loss vector

Preserved:

- both source-study episodes exhausted 32 calls;
- no exact atlas document was read;
- no submission occurred;
- missing cumulative navigation state caused orientation loops;
- the result did not establish a model selection/construction inability;
- navigation observations had active-work-surface value;
- downstream selection, sufficiency, stopping, and construction remained
  unresolved; and
- semantic memory/digests/action bases/forced construction were not promoted.

Omitted:

- the source-study candidate remained unchanged; and
- no source-study check ran.

Fabricated, contradicted, or materially reversed: none found in the sealed
direct audit.

This loss vector is visible in experiment custody and downstream auditing. Do
not add the omitted facts to the model as compensating host prose.

## Control and treatment

### Historical control

No new control inference is required. The byte-exact donor call-12 packet and
response are the baseline:

```text
source body nonresident
+ exact reopen receipt
-> actor reopens the source immediately
```

Do not describe the historical response as randomized simultaneous control.
It is an exact within-trajectory historical comparison.

### Treatment

Start from the exact historical call-12 request. Preserve every existing byte
and capability, then add one canonical block containing:

```text
SOURCE-BOUND SEMANTIC DIGEST
source identity/version/hash
digest identity/hash
lossy_non_authoritative: true
exact_reopen_available: true
<exact frozen digest bytes>
```

Do not add semantic advice, progress state, completeness claims, source
importance, action recommendations, omitted endpoint facts, or another digest.
The known-loss record remains investigator-visible and must not be shown to the
actor as compensating semantic content.

## Hard preflight gates

Before a measured call, prove:

1. both donor commits and all imported objects are byte-exact;
2. call 12 literally repeats call 9's exact source action on an unchanged
   candidate;
3. the digest bytes/hash/token receipt and source binding match the sealed run;
4. the digest is marked lossy and non-authoritative;
5. exact reopen remains unchanged and executable;
6. the treatment differs from control only by the canonical digest block;
7. the treated first request fits with the unchanged 4,096-token response
   reserve;
8. the maximum legal first response fits;
9. result execution/delivery and the inherited minimum-necessary pressure rule
   are deterministic;
10. enough protected control headroom exists for every authorized continuation
    branch;
11. no donor file changes;
12. fresh-process rendering and replay are deterministic; and
13. maximum actor calls are exactly three, with one attempt and zero retries.

Any identity, binding, capacity, exact-reopen, control-reachability, or replay
failure stops the study before GPU inference.

## Measured continuation

### Decision 1 — primary

Run the treated actor once.

If it requests the same exact source, classify
`immediate_same_source_raw_reopen` and stop the cell. Do not spend additional
calls to make an immediate substitution failure look productive.

If it requests another valid action, execute it through the inherited exact
executor and deliver its result under the frozen minimum-necessary pressure
rule.

### Decisions 2–3 — conditional feedback horizon

Only after a different valid first action, allow at most two further ordinary
actor decisions. Stop earlier at:

- same-source raw reopen;
- admitted submission;
- context/control invariant failure;
- result that cannot be delivered under the frozen rule;
- apparatus/model integrity failure; or
- the three-call ceiling.

Do not force mutation, check, submission, or source reopening.

## Outcomes

Primary classification:

- immediate same-source reopen; or
- different valid first action.

Secondary trajectory classes:

- delayed same-source reopen;
- healthy exact recovery after a precision-sensitive action;
- different duplicate acquisition;
- novel acquisition;
- mutation/effect uptake;
- submission;
- semantic error plausibly related to a known or newly identified digest loss;
- no reopen and no useful progress; or
- capacity/apparatus endpoint.

Avoiding reopen is not itself success. A positive local utility lead requires a
different valid action without material semantic degradation. A later reopen
may be appropriate recovery rather than failure.

## Information-economic accounting

Report separately:

- digest production: 6,902 prompt tokens, 219 completion tokens, 16,070 ms;
- digest resident tokens and wrapper tokens by treated call;
- control and treatment prompt/completion/cache/latency;
- exact source result tokens and bytes when reopened;
- raw source deliveries avoided or delayed;
- maintenance/recomposition tokens and substitutions;
- calls spent on productive work versus recovery;
- candidate/artifact changes and repair cost; and
- total serialized tokens through the terminal measured decision.

Use the exact tokenizer to calculate how many avoided source deliveries would
be required to repay digest production under token accounting. Report latency
and cache effects separately; do not invent a single scalar exchange rate.

## Direct audit

Read every measured turn and compare against:

- exact historical call-12 behavior;
- exact source content;
- known digest loss record;
- current candidate/world state; and
- any terminal mutation or artifact.

Record whether the actor relied on a false inference, merely chose a different
read, appropriately reopened for precision, or made actual task progress.

## Frozen forecast for implementation

- 35%: immediate same-source raw reopen;
- 25%: different first acquisition followed by delayed same-source reopen;
- 20%: different acquisition with no same-source reopen and no mutation within
  three calls;
- 10%: mutation, submission, or other substantive action without material
  semantic error;
- 5%: semantic misuse or quality degradation plausibly related to digest loss;
- 5%: capacity, control, or apparatus integrity endpoint.

Freeze or revise this forecast only before measured outcomes and only from
exact offline capacity/custody evidence.

## Claim limit and stop rule

This one selected, already observed digest creates a descriptive local utility
test. It cannot establish production reliability, transfer, general source
digestion, or a complete context policy.

After replay, direct audit, cost accounting, result publication, and program
ledger update: stop. Select no automatic successor and make no further GPU
calls.
