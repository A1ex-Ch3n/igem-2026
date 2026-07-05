# Why the ESMFold RBP × receptor matrix is not a usable binding readout

*Short note for Cesar. Figures: `code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png` (screen) and `control_validation.png` (control test).*

To go beyond the receptor-repertoire overlap, we tried to predict, for all 7,182 phage RBP ×
*Pseudomonas* receptor pairs, whether each RBP structurally docks onto each receptor. Because
AlphaFold2-multimer (MSA-server bottleneck) and Boltz-2 (GPU-driver incompatibility on our L40S
nodes) were not feasible at this scale, we used **ESMFold** — an MSA-free, single-sequence
structure predictor — folding each RBP+receptor as one complex and scoring the interface with a
PAE-derived pseudo-ipTM.

**The resulting scores do not represent binding.** Three independent lines of evidence show the
matrix is dominated by artifacts rather than interaction specificity:

1. **Scores are compressed and low.** Median pseudo-ipTM is 0.13 (sd 0.03); the maximum is 0.32.
   Genuine modeled protein–protein interfaces typically score 0.5–0.9. Almost every pair sits in a
   narrow band just above background.
2. **63% of the score variance is per-protein, not per-pair.** A simple additive model
   (RBP effect + receptor effect) explains most of the variation — i.e., a score mostly reflects
   how "confidently foldable" each protein is on its own, not whether *that* RBP binds *that*
   receptor. The specific pairing contributes little.
3. **The score tracks protein size, not binding.** Pseudo-ipTM correlates with complex length
   (r = +0.58), and the top-ranked "hits" are simply the smallest-RBP × smallest-receptor pairs
   (e.g. ~120 aa RBPs with a 248 aa receptor): the model packs two small domains together
   confidently whether or not they actually interact.

**Root cause (expected):** MSA-free folding of cross-kingdom pairs (phage protein × bacterial
protein) has no coevolutionary signal to locate a real interface; and the RBPs are homotrimers
whose true receptor-binding tip we did not model (we folded monomers). So the model defaults to
generic packing confidence, which is governed by size and foldability — exactly what we observe.

## Control test — why, how, and the result

**Why.** A screen is only meaningful if it can tell a real binder from a non-binder. Because the
matrix above looked suspicious, we tested the method against pairs with **known answers** before
trusting or discarding it.

**Hypothesis.**
- **H1 (method works):** if the pseudo-ipTM reflects real binding, documented binders should score
  *above* their scrambled/mismatched controls and above the screen background.
- **H0 (null):** the score reflects generic foldability/size, so real ≈ scrambled ≈ background.

**The three positive controls, and where they came from.** We took experimentally documented
phage RBP–receptor pairs from the literature, prioritizing ones with **solved co-structures**
(ground truth) plus one in **our own organism**; sequences pulled from UniProt/NCBI:

| Positive pair | Evidence | Note |
|---|---|---|
| T5 **pb5** × *E. coli* **FhuA** | cryo-EM co-structure, PDB **8A8C** (Degroux 2023) | gold standard |
| λ **gpJ** (C-terminal RBD) × *E. coli* **LamB** | co-structure, PDB **8XCJ** (2024) | gold standard |
| DEV **gp54** × *P. aeruginosa* **LptD** | genetics + AlphaFold, mBio 2026 | our organism |

For each positive we also folded a length-matched **scrambled** receptor (same residues, shuffled —
removes the size confound) and a **mismatched** receptor, through the *identical* ESMFold pipeline
(Figure: `control_validation.png`):

| positive pair | real | scrambled | mismatch | background |
|---|---|---|---|---|
| T5 pb5 × FhuA (PDB 8A8C) | 0.137 | **0.136** | 0.129 | median 0.127 |
| λ gpJ × LamB (PDB 8XCJ) | 0.112 | 0.102 | 0.129 | (sd 0.026) |
| DEV gp54 × LptD (*Pseudomonas*) | 0.159 | 0.129 | 0.112 | |

**Result — H0 supported, H1 rejected.** The known binders do **not** separate from scrambled/mismatched controls or from the screen
background — the gold-standard pair with a solved co-structure (pb5×FhuA) differs from its own
scrambled receptor by **0.001**. The mean real-vs-scrambled gap (+0.014) is smaller than the
background noise (sd 0.026). Crucially, the whole-complex **pTM** *does* collapse when the receptor
is scrambled (0.55→0.17, 0.49→0.24, 0.65→0.24) — so the model correctly detects the scramble is not
a real protein — yet the **interface score barely moves**, proving the pseudo-ipTM is not reading a
real interface. **Conclusion: this folding screen is not informative for phage RBP–receptor binding,
and we are not using it as evidence.**

The **receptor-repertoire overlap** analysis remains our primary, interpretable evidence for
candidate phage–host matches — the clue-level readout we agreed on — and does not depend on this
folding step.

---
*Log — 2026-07-05: final full matrix (6,358 OK + 824 SKIP = 7,182) + 9-fold control test both
complete and confirm the negative result. Figures: `rbp_receptor_iptm_heatmap.png` (screen),
`control_validation.png` (controls). Full method history in
`documents/2026-07-04_folding_tool_odyssey.md`; tool decision in
`documents/2026-07-04_folding_tool_recommendation.md` (§6 flagged exactly this failure mode).*
