# E104 — Verification-residency reconciliation

Date: 2026-08-30

Status: complete no-GPU apparatus and systems audit. No live operation is
authorized.

Apparatus result:
[`b548a4d`](https://github.com/ScrappyTom/qwen38-artifact-coupled-integration-scout-v0/commit/b548a4d)

## What E103 was carrying

The blocked call-27 packet was not simply “the artifact plus one pending
effect.” It carried the latest complete check projection twice:

- in delivered `RESULT-024`; and
- in the replaceable `current_verification_frame`.

The older delivered `RESULT-021` check also remained resident. Their exact
marginal costs were approximately 899 and 912 offline tokens. The historical
live deficit was only 326 tokens. The pending `RESULT-026` effect cost about
1,264 marginal tokens and was not eligible for turnover.

## Earned prospective rule

The host may replace a delivered check body with an exact receipt only after
the current verification state binds:

- result ID and exact result SHA;
- evaluated candidate SHA;
- exact check-projection SHA;
- complete check findings with mechanical current/stale fields; and
- exact reopen authority.

This uses no relevance judgment and asserts no semantic uptake. It is a
replaceable-current-state rule: exact current verification carries the active
diagnostic; exact external custody carries the raw historical object.

At the exact E103 boundary, adding these bindings and turning over
`RESULT-021` and `RESULT-024` projects a 20,548-token packet, 444 tokens below
the 20,992-token offline allowance. Applying the historical 17-token
live/offline difference still leaves 427 projected tokens. `RESULT-026`
remains an exact pending body, and both checks remain exactly reopenable.

## What was deliberately not changed

The audit did not compact phase effects, resolved action rejections, the
current artifact, or the pending candidate effect. Check turnover alone
restored projected feasibility and had the strongest exact duplication proof.

The plan's donor-derived fixture stop rule also fired. Exact uncorrupted
version-007 artifact bytes exist, but there is no sealed checkpoint at that
state. The next sealed checkpoint is version 008 and already contains the
glued-heading corruption. No checkpoint was invented by mixing earlier
artifact bytes with later event/domain state.

A separate provider-free non-donor fixture completed failing check, repair,
passing recheck, and submission with exact check turnover and reopen. All 328
repository tests and Ruff pass. This qualifies mechanics, not live Qwen
behavior.

## Program meaning

E104 strengthens the phase-dependent lifecycle hypothesis:

```text
exact current artifact
+ exact pending effect
+ replaceable current verification state
+ reopenable historical check receipts
```

is a more coherent verification packet than retaining every complete check
beside the current verification state.

It does not show that Qwen will remain oriented, repair correctly, recheck, or
close correctly after live turnover. E103 remains sealed and cannot resume
under this prospective policy.

## Next decision

Do not run another receipt or schema micro-study. The next live evidence, if
selected after offline Stage 0, should be a new prospectively frozen
whole-lifecycle execution under the corrected section transport and E104 host.
It should start from a clean declared initial state, checkpoint frequently, and
continue through construction, effect delivery, current check, bounded repair,
recheck, and correct closure or explicit incomplete stop.

No GPU run is selected by E104.
