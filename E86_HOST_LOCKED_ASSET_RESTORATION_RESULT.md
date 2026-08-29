# E86 — host locked-asset restoration and exact qualification

Date: 2026-08-28

Apparatus commit:
`a7c7686977661dcd7adebc1da78a78aa2b423ff5`

Disposition: exact provider-free host qualification passed; no behavioral,
utility, or GPU claim.

## Why this stage exists

E85 finished the bounded live-seam hardening but found that the tokenizer-only
sparse GGUF named by the historical lock was no longer present. A different
Qwen3.8 model supported provisional regression, but correctly could not satisfy
the frozen identity gate.

Archive review showed that the sparse projection had originally been created
by copying the pinned model download while that download was still in progress
and then extending the copy sparsely. Its hash bound an accidental transient
snapshot. It was not a deterministic artifact that could be fetched again from
the immutable repository revision.

## Durable correction

The immutable full model was downloaded from the exact repository and revision
already recorded by every relevant model lock:

```text
repository: AtomicChat/Qwen3.8-27B-GGUF
revision: ca10ebceb1887be9d33b838770a36b39d75a8a4c
path: E:\AI_Models\AtomicChat__Qwen3.8-27B-GGUF__ca10ebceb188\Qwen3.8-27B-AD-IQ2_S.gguf
bytes: 11,141,912,032
SHA-256: d416fa422c9035605c778f60d90a94b288c38b4f9ec2126b58ef938ce8d5f716
```

The offline tokenizer now resolves only a hash-verified asset already named by
the frozen lock. It prefers the historical sparse projection when present and
exact; otherwise it uses the exact full model. A present but mismatched file is
never accepted.

This changes no historical model lock, sealed output, expected packet, or task
fixture. It removes an accidental dependency on a transient convenience file.

## Verification

| Evidence | Result |
|---|---:|
| Asset-resolution tests | 3 passed |
| Direct E83 ordinary packet | 21,401 tokens |
| First-fit relief | `RESULT-001` |
| Direct E83 treated packet | 18,785 tokens, feasible |
| Full repository regression | 280 passed in 299.79 s |
| Injected compatible model | none |
| GPU/provider calls | 0 |

## Program consequence

The refactored host is no longer blocked on tokenizer identity and is exactly
qualified at the provider-free boundary. The full locked model is also present
at the path required by the frozen CUDA server profile.

This is apparatus readiness, not evidence about Qwen behavior or an
information-management mechanism. A live experiment or GPU qualification must
still be selected, frozen, and authorized separately.
