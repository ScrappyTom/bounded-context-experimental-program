# E88 — refactored host live smoke v0 result

Date: 2026-08-28

Apparatus commit: `fbc1db052051b23cfb8667780eab0a9939dee11a`

Run ID: `2026-08-28-host-refactor-live-smoke-v0`

Disposition: sealed pre-provider environmental stop; zero model calls.

The external authorization and exact selected-asset verification passed. The
fresh-runtime gate then found an already running `llama-server` and stopped
before provider I/O. Read-only inspection established that this was an active
Franken Agent compaction job on port 18084, not a leaked process from the host
refactor. It occupied nearly all VRAM and was not terminated or altered.

The v0 tree is sealed with SHA-256
`cee41353d20a360aea2dd7ff920eaa2d261eb4cf994c66b370818df3784316dd`.
It contains the authorization, freeze binding, exact asset verification,
failure, finalization, and seal records. Provider attempts, model calls, and
retries were all zero.

This is not host-path or model evidence. It is a resource-contention stop. The
v0 run ID is closed. The unchanged one-call design is frozen as v1 at apparatus
commit `a92577d64612a6a5f7c623e02de89eb527b47017` after the other job released
the GPU.
