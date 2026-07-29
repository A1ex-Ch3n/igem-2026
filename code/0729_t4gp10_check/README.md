# 0729 — does CDS_0010 carry a T4gp10-like fragment?

Prof. Espinoza described our phage as resembling **group D** of
[Latka, Leiman, Drulis-Kawa & Briers 2019, *Front. Microbiol.* 10:2649](https://doi.org/10.3389/fmicb.2019.02649)
and asked for the assignment to be justified by synteny and similarity.

Group D in that paper is defined by its **first RBP lacking an enzymatic or
receptor-binding domain and carrying instead an N-terminal anchor that includes
a fragment of a T4gp10-like domain**, while the second tail fibre is a
full-featured RBP. Our `CDS_0010` (anchor, no template over its body) and
`CDS_0011` (anchor + β-helix depolymerase) look like that pair — so the
T4gp10-like fragment is the one part of the definition we can test directly.

**Answer: no T4gp10-like fragment is detectable in either protein.**
The group D reading has to rest on architecture and synteny, not on this marker.

## What was tested, and against what

Latka detected the similarity with **HHpred**, over gp10 **subdomains D2 and
D3** — their examples map to roughly gp10 res 61–256, i.e. the middle of the
protein, not its extreme N-terminus. HHpred is not available locally, so the
same claim was tested two other ways.

**Sequence.** `phmmer` with T4 gp10 (UniProt P10928) and gp9 (P10927) as queries
against all 80 canonical phage proteins, threshold deliberately relaxed to
E ≤ 10: **no hits at all**. Expected — remote baseplate homology is normally
invisible to sequence search, which is why Latka used a profile method.

**Structure.** `cealign` in PyMOL, which finds local structural correspondence
and works below the sequence twilight zone. Reference is **5iv5 chain AC**, in
which gp10 is modelled completely (602/602 residues, and 196/196 across D2/D3).

⚠️ Use 5iv5, not 5hx2. `5hx2` chain G resolves only **83 of the 196** D2/D3
residues, and a first pass against it produced apparently better numbers off
that partial model. The comparison is only meaningful against the fully
modelled chain.

## Results

RMSD is meaningless without the alignment length and without controls, so both
are reported and the panel is bracketed by a known-true and a known-false pair.

| Comparison | RMSD | aligned | matched region |
|:-----------------------------------|:------|:--------|:-----------------|
| **Positive control** — Calx-β 3US9 vs CDS_0010 anchor | **1.54 Å** | 88 res | CDS_0010 6–93 |
| **Positive control** — Calx-β 3US9 vs CDS_0011 anchor | **1.99 Å** | 96 res | CDS_0011 6–101 |
| gp10 D2/D3 vs CDS_0010 (full, 917 aa) | 6.88 Å | 96 res | CDS_0010 176–326 |
| gp10 D2/D3 vs CDS_0010 anchor (1–120) | 8.67 Å | 56 res | CDS_0010 6–74 |
| gp10 D2/D3 vs CDS_0011 anchor (1–120) | 5.61 Å | 64 res | CDS_0011 43–113 |
| gp10 full-length vs CDS_0010 (full) | 6.88 Å | 96 res | CDS_0010 176–326 |
| **Negative control** — gp10 D2/D3 vs CDS_0012 (GH5) | 6.72 Å | 64 res | CDS_0012 13–84 |
| **Negative control** — Calx-β 3US9 vs CDS_0012 (GH5) | 7.58 Å | 112 res | CDS_0012 3–139 |

The bands do not overlap. Real homology lands at **1.5–2.0 Å over 88–96
residues**; deliberate nonsense lands at **6.7–7.6 Å**. Every gp10 comparison
falls at **5.6–8.7 Å**, i.e. among the negative controls. The best of them
(6.88 Å over 96 res) is indistinguishable from the GH5 negative control
(6.72 Å over 64 res).

## What this does and does not settle

**Settled.** The anchors of CDS_0010 and CDS_0011 are genuinely **Calx-β** —
1.54 Å and 1.99 Å against a real Calx-β structure is not a marginal call. That
independently confirms the AF3 template assignment (3US9, 3RB5, 2KLT over res
4–104) and the earlier finding that the two proteins are paralogous fibres
sharing a virion-attachment module.

**Also settled.** Our anchors are **not** the anchor family Latka's group D
phages use. Theirs contain a T4gp10-like piece; ours are Calx-β. These are
different domain families doing the same job.

**Not settled.** This does not refute the group D assignment. Group D is defined
by an *architecture* — truncated first RBP, full-featured second — and that
architecture still holds: CDS_0010 has an anchor and no detectable enzymatic
domain, CDS_0011 has an anchor plus a β-helix depolymerase. What it means is
that the assignment must be argued **from architecture and synteny**, which is
exactly what the PI asked for, and cannot lean on the T4gp10 marker.

**Caveat on method.** `cealign` compares rigid bodies; HHpred compares
sequence profiles. A profile method can detect family relationships that a
structural superposition of a 917-aa multidomain protein against a 196-residue
fragment will miss. To match Latka's method exactly, run HHpred (or foldseek,
neither of which is available locally) before stating this negative in print.

Note also that Latka's phages are *Klebsiella* KP32 podoviruses and ours is a
*Pseudomonas* phage, so the whole comparison is by analogy — a different anchor
family across that distance is unsurprising.

## Run

```bash
conda activate igem2026
python code/0729_t4gp10_check/check_t4gp10_similarity.py
```

Fetches 5iv5 and 3US9 from the PDB; reads the PI's AF3 models from
`data/phage_genome/9-2-1/folds_espinoza/` (gitignored). Outputs in
`../output/0729_t4gp10_check/`.

⚠️ Only public reference structures are downloaded — **no phage sequence of ours
is sent anywhere.** All comparison is local.

---
*Log — 2026-07-29: created to answer item C5 from the 2026-07-29 PI
conversation. Result: no T4gp10-like fragment detectable in CDS_0010 or
CDS_0011 by sequence (phmmer, E ≤ 10, nothing) or structure (cealign, all
comparisons within the negative-control band). The Calx-β anchor assignment is
strongly confirmed as a by-product (1.54 Å / 88 res). First pass used 5hx2,
which resolves only 83/196 of D2/D3 — switched to 5iv5, which models gp10
completely, and the conclusion is unchanged.*
