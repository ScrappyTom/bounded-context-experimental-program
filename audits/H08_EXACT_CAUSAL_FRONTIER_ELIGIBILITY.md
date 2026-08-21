# H08 exact causal-frontier eligibility audit

Date: 2026-08-21

Status: **planned two-case treatment ineligible; no GPU call made**

## Proposed rule

The proposed H08 treatment would replace one generic `latest_update` slot with
two exact replaceable slots:

- `latest_observation`; and
- `latest_effect`.

An observation would replace only the observation slot; an effect would replace
only the effect slot. The intended two-case test required the same rule to
preserve the displaced update in both donor histories.

## Read-only donor

Repository:
`E:\qwen38-recurrent-exact-state-recomposition-v0`

Commit:
`c22cff99a0a1111215940c478db50e5762f1c5d3`

Audited donor files:

| Path | SHA-256 |
|---|---|
| `DIRECT_TRANSCRIPT_AUDIT.md` | `89da090339d8edb08c223740cfd4d8e83fb0c243b4cb7cf56e528dabb33496bb` |
| observation `CELL_RESULT.json` | `9518afa2e9cab94007c2923417e0e00695b627929aa76c03f0232c7e3aa724c1` |
| effect `CELL_RESULT.json` | `50d091f2d013c192f3c0ef50034831e2248a0eeecd29c8c0f01273ccf58c71ef` |
| observation `recompositions/after-call-02.json` | `fa266d420dbb5ae6434bd0d18d7bbd44fdf2a3d514c424fb1a06a13cfd440095` |
| effect `recompositions/after-call-02.json` | `4dfc885fa5e6d0039e9d4276b18d58e70cd41a6672d7bed9173f067ad1a3978e` |

## Exact classification

### Observation case

Initial reentry update:

- type: `accepted_observation`;
- update SHA-256:
  `3c5f15b96aae08c8666d6bb4a1e51e10eb9169a0e37e60a759bf1b03e4282b43`;
- content: inherited exact R030 result.

After call 2, recomposition replaced it with:

- type: `accepted_observation`;
- update SHA-256:
  `12a19a70f28994d3690009c5d6b6be2f4d377f78e9fcac47cfa04ed9cb73b79a`;
- content: exact R033 result;
- recomposed prompt/headroom: 19,023 / +1,969.

The later R030 reacquisition therefore followed
`accepted_observation → accepted_observation` displacement. Separate one-deep
observation/effect slots would still replace R030 with R033. H08 would not
change this case.

### Effect case

Initial reentry update:

- type: `admitted_candidate_effect`;
- update SHA-256:
  `490422fb8536197ceec05f8b5bfd5c82aba28fc026453487a6ab3418ed02348a`;
- content: exact accepted patch/effect receipt.

After call 2, recomposition replaced it with:

- type: `accepted_observation`;
- update SHA-256:
  `d3d7da126c00dff655fd918648a5ef624afb8e62ed4cb001f2045e0b8efe9e8b`;
- content: exact R033 result;
- recomposed prompt/headroom: 19,790 / +1,202.

This is `admitted_candidate_effect → accepted_observation` displacement.
Separate observation/effect slots would preserve the patch receipt here.

## Eligibility result

The two histories do not instantiate the same causal contrast:

| Case | Displacement | Two type slots preserve prior update? |
|---|---|---|
| observation | observation → observation | no |
| effect | effect → observation | yes |

Running both as if they were matched would mix a no-op representation in one
case with an active treatment in the other. A behavioral difference could not
be interpreted as transfer of one mechanism.

The predeclared parity gate therefore fails. No renderer, model request, GPU
call, or result claim was created.

## Genuine next design fork

The evidence leaves three materially different choices:

1. run the cross-type two-slot intervention on the effect case only, accepting
   a one-trajectory descriptive scope;
2. design a deeper fixed exact causal tail that can preserve multiple
   same-type observations as well as effects, with depth and admission rules
   justified before capacity preflight; or
3. move to model-managed exact residency, letting the actor choose among exact
   objects under a hard budget.

These are not interchangeable. Choice 2 is the closest mechanical successor,
but selecting a depth solely to retain R030 after seeing this trajectory risks
post-hoc fitting. No successor is authorized by this audit alone.
