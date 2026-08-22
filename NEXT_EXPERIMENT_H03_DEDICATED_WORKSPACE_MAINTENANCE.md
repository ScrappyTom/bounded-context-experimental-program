# H03 successor: dedicated exact-workspace maintenance mode

Date: 2026-08-22  
Status: completed; sealed local negative for one-shot selection utility

## Research question

At an authentic pending-result pressure boundary, can Qwen3.8 make a feasible
exact-residency selection when workspace maintenance is the only permitted
operation, and does the resulting ordinary actor packet preserve useful task
continuation?

This is not another passive directory. It is not a semantic memory, digest,
progress note, or general context manager.

## Conditions

### K — mechanical incumbent

Reuse the sealed `oldest_fit_receipts_v0` cells from
`qwen38-context-reduction-pressure-boundary-v0` at commit
`ab0e21b201d04521a43f83c223a364bca35a7b86`.

The host scans exact-backed result messages oldest-first and replaces the
minimum number needed to deliver the pending result. Existing measured actor
responses are controls; do not spend GPU calls recreating byte-identical
requests.

### M — dedicated maintenance selection

From the same exact historical decision state and accepted pending result:

1. append the exact historical assistant read action;
2. add one mechanical maintenance message containing the pending result's
   identity/size, ordinary capacity deficit, and eligible result-message
   catalog;
3. restrict output to one `release_result_ids` array;
4. validate the selection and exact rendered capacity;
5. replace selected bodies with the same deterministic exact receipts;
6. append the exact pending result;
7. omit maintenance call chronology from the actor packet; and
8. make one ordinary actor call unless its request is byte-identical to an
   already measured incumbent request.

No host semantic relevance label, summary, readiness statement, progress cue,
or recommendation is allowed.

## Protected control plane

- Context: 25,088 tokens.
- Ordinary response reserve: 4,096 tokens.
- Maintenance response allowance: 512 tokens.
- Manager prompt/headroom:
  - seed 42: 21,792 / +2,784;
  - seed 314159: 20,713 / +3,863.

The smaller maintenance allowance is mode-specific and frozen. It cannot leak
into ordinary actor calls. The host remains responsible for hard-overflow
safety.

## Primary outcomes

Report separately per seed:

1. `valid_feasible_selection`;
2. `pending_result_delivered`;
3. `ordinary_next_decision_preserved` against the measured incumbent action;
4. selected result IDs and exact net headroom; and
5. whether the ordinary actor immediately requests a released object.

Exact incumbent next actions are:

- seed 42: `read_region R030`;
- seed 314159: `read_region R032`.

A mutation is not forced and is not required for interface qualification. If
one occurs, audit its literal effect and artifact quality separately.

## Call authorization ceiling

- Two maintenance calls, one per seed.
- Up to two ordinary actor calls, only for novel rendered requests.
- Maximum four new model calls.
- One attempt, zero retries.
- Stop a cell on invalid/insufficient selection, exact-capacity failure,
  parser/admission failure, or apparatus invariant failure.

## Interpretation

- Valid selection + preserved actor decision in both seeds: dedicated
  maintenance is a viable selection surface at these boundaries, not proof it
  beats the mechanical incumbent over time.
- Valid selection + released-object request: the model's chosen working set is
  locally unstable.
- Valid selection + different useful task action: descriptive lead requiring
  direct audit; do not post-hoc broaden equivalence.
- Invalid or insufficient selection: model selection failed even after control
  reachability was solved.
- Byte-identical incumbent selection: reuse the sealed actor response; the new
  evidence is selection convergence, not another actor sample.

## Frozen forecast

- 35%: feasible selections and incumbent next decisions preserved in both cells;
- 30%: feasible selection, but one or both actor decisions shift toward released
  or other exact information;
- 15%: at least one invalid, insufficient, or over-aggressive selection;
- 10%: manager exactly reproduces an incumbent release set in at least one cell;
- 5%: at least one actor mutates or otherwise makes stronger task progress;
- 5%: apparatus or action-serialization issue dominates.

## Approval gate

Implement and qualify the standalone apparatus first. Then present exact source
locks, manager/actor packet counts, fake-model results, schedule, maximum call
cost, and this forecast. Do not launch measured inference without explicit user
authorization for the frozen commit.

## Completed disposition

The standalone apparatus was frozen at
`a2a4284a6f3b1d4044e6b22333a20c97065b3600` and the authorized four-call run is
sealed at
[`44bade979d0ba1f1a2df3f2c919146c29d4c6868`](https://github.com/ScrappyTom/qwen38-dedicated-workspace-maintenance-v0/commit/44bade979d0ba1f1a2df3f2c919146c29d4c6868).

Both manager outputs were valid and made the pending result model-visible.
They released 6,527 and 6,956 prompt tokens for deficits of 394 and 1,045;
both ordinary actors immediately requested the same released source and 0/2
preserved the incumbent next decision. The experiment solved reachability, not
selection utility. No prompt-tuning successor is selected.
