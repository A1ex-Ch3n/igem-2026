# 0708 — 9-2-1 Φ8 RBP variable-region analysis

Characterize the receptor-binding proteins (RBPs) of the assembled phage **9-2-1 Φ8**: find the
**variable region** (receptor-binding domain) and build a hypothesis for **how it binds the receptor
on host 9-2-1**. Follow-on to the assembly in [`../../data/phage_genome/9-2-1/assembly/`](../../data/phage_genome/9-2-1/assembly/).

**Read this first:** [`RBP_variable_region_analysis.md`](RBP_variable_region_analysis.md) — the full
answer + evidence + confidence flags + morning runbook.

## What's here
| Path | What |
|---|---|
| `RBP_variable_region_analysis.md` | the writeup (start here) |
| `seqs/` | extracted RBP + tail-module protein sequences (CDS_0014–0020) |
| `fold/` | Laguna folding inputs — RBP structures + real-RBP × receptor binding screen ([`fold/README_RUN.md`](fold/README_RUN.md)) |

## One-paragraph result
Short-tailed podovirus; RBPs are 2 tailspikes (CDS_0015/0016) + a large tail protein (0017) + a small
tail fiber (0018). Each has a **conserved N-terminal virion-attachment domain and a variable C-terminal
receptor-binding domain** (the "variable region"). The tailspikes have β-helix-depolymerase composition,
so the **primary receptor is most likely the host LPS O-antigen** (9-2-1 has a full rhamnose O-antigen
locus) — bound and cleaved by the tailspike RBD; an OMP/TBDR protein receptor (esp. for the tail fiber)
is the secondary hypothesis. Confirm by folding the RBPs on Laguna (β-helix + groove = depolymerase).

**Note:** all sequence analysis was done locally; the novel phage sequences were **not** sent to any
external service. Structure prediction is deferred to Laguna.

---
*Log: 2026-07-08 — created overnight.*
