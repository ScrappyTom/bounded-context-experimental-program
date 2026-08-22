# Artifact-adjudication consistency audit

Date: 2026-08-22

Status: passed after the published H05 correction; zero unresolved conflicts;
zero GPU calls

## Purpose

Test whether identical candidate bytes acquired inconsistent artifact-quality
dispositions across the bounded-context program or its relevant older Qwen3.8
donor bank.

This is a consistency audit, not a new semantic grader. Agreement among prior
judgments does not prove that a rubric was complete or correct.

## Canonical identity

An adjudication is keyed by:

```text
candidate/tree identity
+ exact file hashes where available
+ authoritative task family/version
+ evaluation/rubric identity
+ declared evidence coverage
```

Candidate hash alone is insufficient. Identical bytes may legitimately receive
different measurements under different tasks or evaluators. Such differences
must remain explicit. An unexplained quality upgrade for the same candidate and
task is a conflict.

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
mechanically inactive and points to the corrected adjudication. Reactivating it
causes the checker test to fail.

All four source commits, paths, and Git blob identities resolve exactly in their
standalone repositories.

Unchanged starting candidates in the capacity/residency experiments were
deliberately not graded as completed artifacts. They are not silently converted
into quality adjudications by this audit.

## Older Qwen3.8 bank

The read-only donor
`E:\research-state-integration-2026-08-18` was locked at commit
`b7e12ab21cec1ef8215e97dc9890924721651f1d`.

The checker recursively inspected machine records containing all four fields:

- `terminal_candidate_id`;
- `terminal_passed_count`;
- `case_count`; and
- `task`.

Result:

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
identity and task-bound disposition.

## Governance result

Before any future artifact-quality claim or closure-utility score:

1. bind the exact candidate/tree identity and task version;
2. search the adjudication ledger and donor lineage;
3. record the evaluator/rubric and evidence coverage;
4. preserve prior judgments rather than overwrite them;
5. require explicit supersession for a corrected judgment;
6. stop on an unexplained active conflict; and
7. freeze readiness before maintenance output or treated actor behavior.

The checker is `tools/check_artifact_adjudications.py`. The locked inputs are
`ARTIFACT_ADJUDICATION_LEDGER.json`; the exact result is
`ARTIFACT_ADJUDICATION_CONSISTENCY_RECEIPT.json`.

## Disposition

After the H05 correction there are no unresolved consistency conflicts. This
does not reopen the blocked close-transfer experiment and does not authorize a
new GPU study. The next behavioral branch remains unselected.
