# Dedicated workspace-maintenance eligibility audit

Date: 2026-08-22  
Status: eligible offline; zero chat completions

## Question

Can the two authentic result-delivery pressure boundaries support a separate
maintenance-only model view with guaranteed control headroom, multiple real
residency choices, and an unchanged 4,096-token ordinary response reserve?

## Donor

- Repository: `E:\qwen38-context-reduction-pressure-boundary-v0`
- Commit: `ab0e21b201d04521a43f83c223a364bca35a7b86`
- Cells: `s42-s1` and `s314159-s1`
- Incumbent: measured `oldest_fit_receipts_v0`

The donor is preferable to the passive-residency endpoint. Its pending results
are novel accepted observations that historically could not cross a model
boundary. The passive endpoint's pending `R031` duplicated bytes already
resident in its candidate suffix.

## Proposed maintenance view

The manager sees the exact historical decision packet, the exact accepted read
action, a mechanical pending-result identity/size receipt, and a catalog of
eligible exact-backed historical result messages. No result body is summarized
and the pending result is never eligible for release.

The only output is:

```json
{"release_result_ids":["RESULT_..."]}
```

The maintenance call has a 512-token response allowance. The following
ordinary actor call retains the frozen 4,096-token reserve. Maintenance
chronology will remain external to the actor packet, so the behavioral
treatment is the selected residency set rather than a fresh model-authored cue.

## Exact capacity result

| Cell | Historical post-result prompt | Deficit | Manager prompt | Manager headroom | Eligible results | Feasible single releases | Incumbent releases |
|---|---:|---:|---:|---:|---:|---:|---|
| s42-s1 | 21,386 | 394 | 21,792 | 2,784 | 8 | 7 | indices 5, 7 |
| s314159-s1 | 22,037 | 1,045 | 20,713 | 3,863 | 6 | 3 | indices 5, 7 |

Counts use the exact parent template and tokenizer through a CPU-only
tokenization endpoint. It made 16 template calls and 16 tokenization calls,
zero chat completions, and was stopped after the audit. Port 18092 closed.

Selection is nontrivial in both cells: several distinct single-object releases
can make the ordinary post-result packet fit. This is therefore not a disguised
host decision with only one feasible answer.

## Eligibility disposition

Eligible for standalone preflight.

The measured experiment must still prove:

- exact donor materialization and request reconstruction;
- strict maintenance-only schema execution with fake-model probes;
- exact receipt substitution and ordinary post-result rendering for arbitrary
  selected sets;
- no manager output or maintenance chronology entering the actor packet;
- byte reuse rather than a duplicate actor call when the selected packet equals
  an existing measured incumbent request;
- unchanged ordinary task, tools, model, sampler, context, and reserve; and
- one attempt, zero retries, and a maximum of four new model calls.

This audit establishes capacity and nontrivial choice only. It does not show
that Qwen can make a valid selection or that its selection improves behavior.
