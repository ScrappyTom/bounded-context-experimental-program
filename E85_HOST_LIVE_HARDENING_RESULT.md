# E85 — host live-seam hardening result

Date: 2026-08-28

Historical checkpoint note: E86 subsequently resolved the asset blocker below
by restoring the immutable full model already named by the frozen lock. See
`E86_HOST_LOCKED_ASSET_RESTORATION_RESULT.md`.

Apparatus commit:
`cc78d3b4c7162c6d3615696defd68e9790ee04ea`

Disposition: provider-free apparatus hardening accepted; exact locked-asset
qualification blocked; no behavioral, utility, or GPU claim.

## Why this stage exists

External review found that E84's offline architectural refactor did not yet
close several seams that matter in live execution. In particular, the host
could compose one packet and send another transformed request, expected action
rejection was terminal, Trellis reopen bypassed the native lifecycle,
reopenable IDs were inferred from receipts, finish reasons were ignored, and
checkpoint/review evidence did not fully bind execution or tranche lineage.

E85 is a bounded hardening pass over those seams. It does not add a semantic
mechanism, choose an experiment, alter historical runners, or call a model.

## Implemented corrections

- The exact final provider messages must equal the composed packet messages.
- Each attempted request binds packet and manifest hashes, exact pending result
  IDs, current exact state versions, final request hash, completion reserve,
  and an execution-manifest hash.
- Delivery and completed state exposure commit only from that verified request
  after provider success.
- A provider failure preserves attempted request binding but commits no
  completed exposure.
- An unacceptable finish reason is preserved exactly, produces nonterminal
  response rejection, and cannot execute a task action.
- Expected parse/action/domain rejection is an exact scheduled observation and
  does not terminate the trajectory.
- Unexpected adapter failure remains a distinct terminal apparatus failure.
- Trellis `reopen_exact` moves the original delivered-external result through
  the kernel; it creates no duplicate legacy result.
- Advertised reopen capability is derived only from projected lifecycle state.
- Prompt allowance is context window minus frozen response reserve, and the
  total serialized budget is checked before a provider attempt.
- Resumed tranches verify the complete parent checkpoint and bind its hash.
- Mechanical review now contains request bindings, finish reasons, raw custody
  paths, provider usage/timing, action disposition, exact candidate transitions
  and diffs, recurrence telemetry, and separate attempt/completion/failure
  counts.

The implementation also caught and fixed one replay issue during testing:
wall-clock provider duration initially entered the authoritative event log and
made uninterrupted and resumed histories differ. Timing is now nonauthoritative
custody/review telemetry.

## Verification

| Evidence | Result |
|---|---:|
| Adversarial live-hardening tests | 11 passed |
| Combined checkpoint/live/hardening tests | 18 passed |
| Ruff | passed |
| mypy | passed, 12 host modules |
| Full regression with compatible Qwen3.8 tokenizer | 277 passed in 307.51 s |
| GPU/provider calls | 0 |

## Exact asset blocker

The tokenizer projection frozen in the model lock was found missing after the
power outage:

```text
E:\AI_Models\AtomicChat__Qwen3.8-27B-GGUF__ca10ebceb188\Qwen3.8-27B-AD-IQ2_S.tokenizer-projection.gguf
SHA-256: 7047272e809b62b5c68b6427a349cba78b2f45109de04350d48f0338db68eef3
```

The locked tokenizer executable is still present and matches its recorded
hash. A different local Qwen3.8 GGUF reproduced the E83 token-count/relief
assertion and supported the full regression when injected only inside the test
process. That is useful compatibility evidence, but it is not the frozen asset
and does not satisfy exact qualification.

No lock, sealed result, historical runner, or runtime path was changed to hide
the blocker.

## Program consequence

The refactor is code-qualified provider-free and should remain the only
candidate path for future experiment design. It is not yet exactly live-
qualified. The next eligible operation is restoration of the exact tokenizer
projection, SHA-256 verification, then direct E83 replay and full provider-free
regression on the locked asset. That restoration does not authorize GPU use.
