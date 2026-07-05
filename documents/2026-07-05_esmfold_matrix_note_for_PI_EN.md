# Why the ESMFold RBP × receptor matrix is not a usable binding readout

*Short note for Cesar. Figure: `code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap_partial.png`.*

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

**What we are doing about it.** We are running positive/negative controls (known phage
RBP–receptor pairs pushed through the identical pipeline) to formally confirm that the method
cannot separate real binders from background at this resolution. In the meantime, the
**receptor-repertoire overlap** analysis remains our primary, interpretable evidence for candidate
phage–host matches — the clue-level readout we agreed on — and does not depend on this folding step.

---
*Log — 2026-07-05: diagnostic on the partial ESMFold matrix (4,386 of 7,182 folds). Full method
history in `documents/2026-07-04_folding_tool_odyssey.md`; tool decision in
`documents/2026-07-04_folding_tool_recommendation.md` (§6 flagged exactly this failure mode).*
