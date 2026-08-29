# E87 — refactored host live-smoke Stage 0

Date: 2026-08-28

Apparatus commit:
`fbc1db052051b23cfb8667780eab0a9939dee11a`

Run ID: `2026-08-28-host-refactor-live-smoke-v0`

Disposition: frozen and provider-free qualified; one live GPU/model call is
eligible only after separate exact authorization bound to the apparatus commit.

## Why this stage exists

E84–E86 established that the refactored host and exact restored model reproduce
the historical E83 pressure geometry offline. They did not establish that the
same refactored path can start the frozen CUDA runtime, send an exact
pressure-relieved request, receive one real model response, and preserve every
delivery, action, checkpoint, custody, release, and seal transition.

E87 freezes the smallest integrated live qualification that can answer that
apparatus question without pretending one model response is a behavioral
experiment.

## Exact starting boundary

The run resumes E83 after seven completed historical actor calls:

- six source domains are already delivered;
- `RESULT-007`, containing COMMS and TRANSIT, is pending;
- the ordinary packet is 21,401 tokens against a 20,992-token prompt limit;
- deterministic first-fit relief externalizes only `RESULT-001`;
- the treated packet is 18,785 tokens and feasible.

One new model invocation is allowed. A completed call 8 must include and deliver
`RESULT-007`. The model's chosen action may be accepted or rejected normally;
semantic usefulness is not a qualification condition.

## Integrated gates

The launcher requires:

1. clean apparatus commit and external authorization receipt;
2. exact model, CUDA server, and tokenizer executable hashes;
3. a complete hash inventory of the CUDA server bundle;
4. a fresh hidden server with the frozen alias/build, 25,088-token context,
   66/66 GPU offload, and PID visible on the GPU;
5. exact 21,401 / `RESULT-001` / 18,785 pressure preflight;
6. a verified parent checkpoint for the seven historical calls;
7. exactly one provider attempt and one completed invocation;
8. `RESULT-007` bound to and delivered through call 8;
9. raw HTTP and host-provider custody;
10. new checkpoint, mechanical review, clean runtime release, and sealed tree.

## Frozen resource contract

- maximum new model calls: 1
- maximum serialized tokens: 30,000
- attempts per call: 1
- retries: 0
- automatic continuation: prohibited

## Offline verification

- selected runtime assets: exact hash verification passed;
- runtime bundle: complete file-hash inventory recorded;
- direct E83 replay: passed;
- focused refactored-host tests: 44 passed;
- live-smoke tests: 2 passed;
- Ruff: passed;
- mypy over 13 host modules: passed;
- full apparatus regression: 282 passed in 329.53 seconds;
- GPU/provider calls: 0.

The offline qualification caught and repaired three integration defects before
freeze: missing parent-checkpoint binding, use of a review-only invocation
projection instead of the authoritative event log, and an incorrect raw HTTP
custody filename.

## Claim limit

A future pass would establish only that one pressure-relieved live invocation
can cross the refactored host correctly. It would not establish useful model
behavior, improved information management, loop prevention, or readiness for
an unattended long run.

## Exact authorization shape

The external authorization receipt must bind:

```text
authorized: true
authorized_freeze_commit: fbc1db052051b23cfb8667780eab0a9939dee11a
authorized_scopes: [host_refactor_live_smoke_v0]
authorized_run_id: 2026-08-28-host-refactor-live-smoke-v0
maximum_model_calls: 1
maximum_serialized_tokens: 30000
attempts_per_call: 1
retries: 0
```

No GPU call is made by this Stage 0 record.
