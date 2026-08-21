# Bounded context experimental program

This repository is the cross-experiment planning and evidence ledger for a
sequence of standalone Qwen3.8 bounded-context studies. It does not contain a
runtime context manager and does not retroactively modify completed experiment
repositories.

The program asks:

> How can a bounded actor repeatedly maintain enough exact and semantic
> continuity to keep doing useful work without rebuilding an indefinitely
> growing transcript?

Start with [BOUNDED_CONTEXT_EXPERIMENTAL_PROGRAM.md](BOUNDED_CONTEXT_EXPERIMENTAL_PROGRAM.md).
Claim-level custody and promotion status are recorded in
[EVIDENCE_LEDGER.md](EVIDENCE_LEDGER.md).

Each measured experiment remains a separately frozen, auditable repository.
Adding a candidate mechanism here does not authorize or promote it.

Current route: frontier-interface tuning is closed after the final
closure-safe qualification failed 0/2 under its frozen complete-object gate.
The H08 two-case design also failed parity because type-separated observation
and effect slots change only the effect case. Its one-case diagnostic then
failed the exact capacity gate before inference: preserving both complete
updates produced 21,113 prompt tokens, 121 beyond the frozen allowance. A
post-hoc minimal deterministic label still missed by 23 tokens, so the result
was not merely verbose custody metadata. Zero GPU calls were made.
Host-selected exact-layout tuning is now closed at these
endpoints. Ongoing model-managed exact residency remains the next distinct
candidate branch, but no successor is active.
