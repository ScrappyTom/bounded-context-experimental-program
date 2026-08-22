# Artifact-adjudication consistency audit

Date: 2026-08-22

Status: v1 hardening passed after the published H05 correction; zero
unresolved conflicts; zero GPU calls

## Purpose

Test whether identical candidate bytes acquired inconsistent artifact-quality
dispositions across the bounded-context program or its relevant older Qwen3.8
donor bank.

This is a consistency audit, not a new semantic grader. Agreement among prior
judgments does not prove that a rubric was complete or correct.

## Canonical identity

The v1 canonical comparison basis is:

```text
candidate/tree SHA-256
+ exact artifact file-hash manifest
+ authoritative task SHA-256
+ evaluation/rubric identity and hash-or-explicit-unavailability
+ exact evidence-manifest SHA-256
```

Candidate hash alone is insufficient. Identical bytes may legitimately receive
different measurements under different tasks or evaluators. Such differences
must remain explicit. Under one canonical basis, v1 compares the complete
quality class, score, criterion dispositions and findings, explicit closure
readiness, and blocking requirements. A difference in any of those fields is a
conflict. Across different evaluation bases, a divergent active judgment needs
an explicit typed relationship and explanation.

The exact task was reconstructed from the pinned actor request and locked as
2,076 UTF-8 bytes with SHA-256
`20a8a3cb2ea4718a0e287fd0f0b950b3b06b57a1fd9703d230be7335a6791936`.
The four governing evidence objects were reconstructed from pinned Git objects
and canonicalized into evidence-manifest SHA-256
`c2420d174e3827d9a72ef1dbda8f59aa023e4b80124adc9c0d040c34a17a230a`.
No separately materialized rubric hash existed in the donor lineage. V1 records
that absence as `not_separately_materialized`; it does not invent a hash.

## Current standalone program

The current standalone sequence contains one candidate/task family with a
substantive terminal-artifact adjudication:

- candidate ID
  `38893b4df5afc252a356ff5ab79a1dcda6330b7934a252a67d2759499eb4aac6`;
- file SHA-256
  `888c142abcad4c3bd9081960bdb18b7402be6415c03b456033ed3c7aed134d39`.

Four adjudication records were found:

| Record | Status | Disposition |
|---|---|---|
| Exact-construction reentry direct audit | active | strong partial: 10 met, 2 partial |
| Recurrent exact-state inherited audit | active | strong partial: 10 met, 2 partial |
| Original H05 coarse review | superseded | complete: 13/13 |
| H05 exact-hash reconciliation | active | strong partial: 10 met, 2 partial |

The original H05 13/13 record is retained rather than erased, but it is
mechanically inactive and points to the corrected adjudication through a typed
`superseded_due_to_coarser_coverage` relationship. Removing that relationship
causes a checker test to fail.

The three active strong-partial records are **one semantic judgment lineage**,
not three independent votes. The direct review is independent; the recurrent
record inherits it; and the H05 correction reconciles back to it. V1 assigns all
three the same semantic-independence group and reports one active independent
judgment group.

All four source commits, paths, and Git blob identities resolve exactly in their
standalone repositories.

Unchanged starting candidates in the capacity/residency experiments were
deliberately not graded as completed artifacts. They are not silently converted
into quality adjudications by this audit.

## Older Qwen3.8 bank

The read-only donor
`E:\research-state-integration-2026-08-18` was locked at commit
`b7e12ab21cec1ef8215e97dc9890924721651f1d`.

The checker enumerated and read JSON blobs directly from the pinned commit—not
from the checked-out working tree—and inspected machine records containing all
four fields:

- `terminal_candidate_id`;
- `terminal_passed_count`;
- `case_count`; and
- `task`.

Result:

- 150 pinned JSON files selected;
- 60 scored record occurrences;
- 22 unique candidate/task groups;
- every repeated candidate retained the same task-bound score;
- zero conflicting scores; and
- zero JSON parse failures in the selected record population.

This includes complete and incomplete candidates across Inventory Lots, Lease
Pool, Package Graph, Revision Store, Route Catalog, and Token Buckets task
families.

## Scope boundary

The audit covers:

- every substantive candidate-quality disposition in the current standalone
  bounded-context sequence;
- inherited and superseded judgments for its mutated navigation candidate; and
- the older donor's machine-scored terminal candidate records using the declared
  terminal-score shape.

It does not equate note, frontier, or source-digest expression grades with
terminal artifact readiness. It also does not ingest every free-form historical
sentence that happens to call an output “good” or “useful” without a candidate
identity and task-bound disposition. Zero conflicts means the selected records
agree under their declared bases; it does not prove that any rubric was complete
or any semantic judgment was correct.

## Governance result

Before any future artifact-quality claim or closure-utility score:

1. bind the exact candidate/tree identity and task version;
2. search the adjudication ledger and donor lineage;
3. hash the authoritative task, artifact file manifest, and evidence manifest;
4. record the evaluator/rubric hash, or explicitly record that it was not
   separately materialized;
5. record the full score, criterion dispositions, explicit closure readiness,
   and blocking requirements;
6. distinguish independent review from inheritance and reconciliation;
7. preserve prior judgments rather than overwrite them;
8. require an explained typed relationship for supersession or cross-basis
   divergence;
9. stop on any unexplained same-basis difference, not only a top-level class
   difference; and
10. freeze readiness before maintenance output or treated actor behavior.

The hardened checker is `tools/check_artifact_adjudications_v1.py`. Its locked
input is `ARTIFACT_ADJUDICATION_LEDGER_V1.json`; its exact result is
`ARTIFACT_ADJUDICATION_CONSISTENCY_RECEIPT_V1.json`. The v0 ledger, checker, and
receipt remain preserved as the first historical implementation.

This evaluation ledger is external governance. It is not automatically placed
in the actor prompt and is not authoritative world state. It governs later
investigator claims such as `ready`, `complete`, `improved`, or `useful
closure` by preserving exactly which evaluator reached which judgment under
which task and evidence basis.

## Disposition

After the H05 correction there are no unresolved consistency conflicts under
the hardened comparison. This does not reopen the blocked close-transfer
experiment and does not authorize a new GPU study. The next behavioral branch
remains unselected.
