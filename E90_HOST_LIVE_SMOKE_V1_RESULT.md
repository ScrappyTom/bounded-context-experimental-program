# E90 — refactored host live smoke v1 result

Date: 2026-08-28

Apparatus commit: `a92577d64612a6a5f7c623e02de89eb527b47017`

Run ID: `2026-08-28-host-refactor-live-smoke-v1`

Disposition: sealed before provider I/O; zero model calls, zero provider
attempts, and zero retries.

The selected model/runtime assets and all live server gates passed: exact model
alias and build, 25,088-token context, 66/66 GPU offload, and the server PID on
the GPU. The running server reproduced the ordinary packet at exactly 21,401
tokens. After deterministic `RESULT-001` externalization it counted 18,786
tokens, one more than the frozen exact offline projection of 18,785. The
exact-equality gate stopped before completion I/O and released the server.

Two additional fresh-server diagnostics reproduced the split. Offline and
live paths rendered identical 49,518-byte prompts with SHA-256
`fdc87d49f9b66200343f38af6beb5ceeabc6367162126b58efb97fc875a88bcf695`.
The ordinary packet's 21,401 token IDs were identical. The relieved paths first
diverged at token index 2,580 and later reconverged. This rules out different
messages, model bytes, receipt selection, or a simple extra BOS token.

The correction is not a tolerance. E91 freezes the two exact projections
separately: 18,785 for offline qualification and 18,786 for the authoritative
running-server capacity gate. Both select the same `RESULT-001` relief and are
well below the 20,992-token prompt limit.

The v1 run tree is sealed with SHA-256
`5dfbc9bc52f3f220602097ff4f4ed5572e45e74f17be6c0e0e91dbfc9d29602f`.
This result adds runtime/apparatus evidence only and no model behavior.
