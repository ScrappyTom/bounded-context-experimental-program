# E77 — cross-run causal-continuity audit and repair-contract preflight

Date: 2026-08-27

Standalone result commit:
`2e276cb69106de263516aa4828d30cec0e25e365` in
`ScrappyTom/qwen38-artifact-coupled-integration-scout-v0`

Model calls: 0

## Scope

The deterministic audit reconstructs 157 sealed actor calls in ten cells across
four independent worlds: Architecture, Cedar, Solace, and Orchard. It retains
same-world arms as controls without treating them as independent replication.

## Cross-world result

Action-transport failure followed by functional non-progress recurrence appears
in three independent worlds:

* Architecture D0 repeated the same exact rejected `no_effect` section update
  on consecutive calls;
* Solace W0 repeated unadmitted full-document construction at the response/JSON
  boundary; and
* Orchard P1 followed an unresolved non-unique repair with four byte-identical
  exact reads and no candidate change.

Rejected mutation recurrence specifically appears in Architecture and Orchard.
Cedar contains neither action rejection nor exact consecutive recurrence, and
Solace's admitted patch/check loops provide a positive repair control.

The evidence supports one mechanical lifecycle law:

> A rejected mutation remains active while the candidate is unchanged. A later
> observation must not erase the rejection merely because it is newer.

It does not establish that actor-visible causal state changes behavior.

## Implemented bounded contract

The standalone package implements `bounded-verification-causal-frame-v0` as a
host-derived projection of exact ledger facts:

* current candidate;
* compact current check identity and currency;
* latest attempt and outcome;
* latest unresolved rejection until candidate change;
* latest delivered update and candidate effect;
* repeated exact-action count within the current candidate epoch; and
* exact history handle.

The maximum rendered frame over all audited endpoints is 1,297 tokenizer tokens.
It contains no semantic advice, repair selection, readiness assertion, or
automatic recurrence intervention.

The package also implements a common repair action bound to:

* current candidate SHA-256;
* current artifact SHA-256;
* one unique section heading;
* expected exact section SHA-256; and
* complete replacement section bytes.

Against the exact Orchard P1 candidate, a 461-token repair is admitted;
candidate- and section-version mismatches reject without mutation; an admitted
effect clears the prior rejection epoch; and a provider-free current recheck
fits in a 983-token causal frame. The fixture remains not ready.

## Systems meaning

The active unit remains the complete verification lifecycle:

```text
exact artifact
× current check
× repair transport
× unresolved rejection continuity
× recurrence
× effect uptake
× current recheck
× readiness and closure
```

The repair correction must be common to future configurations. Otherwise a
treatment could win merely because it received a usable mutation surface.

## Disposition

| Claim | Status |
|---|---|
| Cross-world action-transport/causal boundary | supported |
| Rejected mutation recurrence beyond Orchard | supported in two independent worlds |
| Bounded exact causal projection | provider-free feasible |
| Uniquely bound section repair | provider-free feasible |
| Actor utility | untested |
| Minimality or sufficiency of frame | untested |
| Readiness or closure benefit | untested |
| Orchard extension | closed |

The cross-world gate selects a fresh whole-system offline Stage 0. No fresh task
or runner is frozen, and no GPU operation is authorized.
