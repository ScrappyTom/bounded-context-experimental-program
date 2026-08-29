# E95 — Trellis unchanged interaction continuation Stage 0

Date: 2026-08-29

Parent result commit:
`0626259773f1411272566caa1b4a00c83e70e606`

Apparatus freeze commit:
`18e17806e906d57943ab9b7461def708084d69b1`

Disposition: offline qualified and frozen in the apparatus repository; live GPU
continuation not authorized.

E94 stopped one invocation before the first complete-catalog decision.
`RESULT-012` exists exactly but remains pending in both cells. The highest-value
next observation is therefore not a redesigned scaffold. It is the unchanged
systems' transition from acquisition into construction, reopen, or continued
reading after that pending result becomes model-visible.

The continuation resumes both exact sealed checkpoints and preserves all prior
policy, prompt, action, budget, evaluator, scaffold, and replacement rules. It
cannot repair E94's discovered semantic loss without starting a new experiment.
Provider-free tests verify exact hydration and the complete common
candidate/check/repair/recheck/closure path from action 13 onward.

Frozen additional limits are 24 actor calls, six maintenance calls, 30 provider
calls, and 520,028 serialized tokens, with one attempt per call and zero
retries. V0 runs before V1, each in a fresh model-server process. Each cell
pauses after 24 cumulative completed actor calls or an earlier terminal/resource
condition. No third tranche is automatic.

GPU execution requires a separate authorization quoting the apparatus commit
above.
