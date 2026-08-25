# E56 — Bluehaven batched-maintenance qualification result

Date: 2026-08-25

Status: separately authorized two-call gate complete, sealed, audited, and
pushed; qualification failed; B1 and the frozen B1/W1 continuation are closed

Standalone result:
[`qwen38-artifact-coupled-integration-scout-v0@9c0fdc5`](https://github.com/ScrappyTom/qwen38-artifact-coupled-integration-scout-v0/commit/9c0fdc537f26ff0a44f2cebc54c580cbd5f7b65d)

## Literal result

Both one-shot calls finished normally and remained below the 2,400-token body
limit:

| Case | Prompt | Completion | Body tokens | Admission |
|---|---:|---:|---:|---|
| initialize from S01–S06 | 11,238 | 1,058 | 1,057 | rejected |
| replace through S12 | 11,436 | 1,274 | 1,273 | accepted |

The initialization cited S07–S12 outside its exact S01–S06 allowlist. The
replacement case cited only allowed sources and passed. The run consumed two
calls and 25,006 serialized tokens, with one attempt per call, zero retries,
and clean runtime release. The independent audit passed while correctly
recording `qualification_passed: false`.

## The failure is semantic, not merely syntactic

Q1 did not merely list unopened handles as future work. It asserted substantive
claims under unseen sources. It attributed hospital and alternate-water
content to S07/S08, warning content to S10, and assay content to S09. More
diagnostically, it said S11 defined the 72-hour execution sequence and S12
defined independent-review blockers. Exact Bluehaven S11 is workforce; S12 is
mutual aid, vendors, routes, and cost authority.

The observed interaction is:

```text
complete R01–R12 replacement obligation
× only partial exact evidence
× task-level descriptions of every requirement
× similarly numbered R and S identifiers
→ fluent completion of missing semantic state with false source bindings
```

The frozen allowlist prevented those claims from becoming exact candidate
work. Relaxing it would destroy the distinction between task obligation and
observed evidence.

## What the accepted second case means

Q2 demonstrates that the runtime, Markdown carrier, 2,400-token bound, and
complete replacement operation are viable when the packet covers S01–S12.
The failure is therefore conditional on semantic maintenance being asked to
materialize a complete task state before its evidence basis is complete.

This is useful interaction evidence. Cadence cannot be selected only from
externalization count; it interacts with evidence maturity and the completeness
demanded of the persistent representation.

## Program disposition

E53 prospectively required both initialization and replacement expression to
pass before measured B1/W1 continuation. B1 fails that gate. The planned
comparison must not run.

No same-world prompt rewrite, token increase, allowlist relaxation, retry, or
delayed B1 trigger is authorized as a repair. A maturity-triggered semantic
policy would be a new whole configuration learned from this failure and needs
fresh prospective design. W1 remains unmeasured; running it alone would be a
descriptive trajectory rather than the frozen causal comparison.

The next high-value work is offline systems reconciliation across prior
maintenance trajectories: measure input evidence maturity, completeness
pressure, output source binding, admission, and downstream work. That audit
can determine whether partial-evidence semantic completion is recurrent before
the program chooses a fresh interaction scout.
