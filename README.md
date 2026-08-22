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

Current route: host-selected exact-layout and frontier-schema tuning are
closed at the tested endpoints. The first passive model-managed exact-residency
formulation also failed to qualify an ongoing policy: Qwen made no residency
action in two calls, reread exact bytes already resident, and the compact state
announcing its later pending result was itself 45 tokens over the frozen
allowance. The model never saw that pending state, so this is not a FIFO
comparison or a general disproof of model-managed residency.

The next distinct candidate is source-bound semantic digestion at seed 42's
first literal repeat-reopen boundary. The program now also treats protected
management/control headroom as a host-owned apparatus invariant. Digest
production must qualify in one bounded plain-text maintenance call before any
actor utility test.
