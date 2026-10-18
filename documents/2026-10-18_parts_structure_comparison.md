# 2026-10-18 — The six expressed parts: 3D models and simulation comparison

Prepared for the iGEM **Parts** deliverable (Registry documentation + wiki). Covers the six
pET-28a(+) constructs we express, their predicted structures, and what the predictions do and
do not establish. Criteria and the winners we are modelling this on:
[`2026-10-18_igem_special_prize_benchmark.md`](2026-10-18_igem_special_prize_benchmark.md).

Code: [`code/1018_construct_structures/`](../code/1018_construct_structures/) ·
figures and tables: `code/output/1018_construct_structures/`.

---

## 1. The parts

| Part (team shorthand) | Protein | Residues of the parent | Insert | Mass (with leader) | pI |
|---|---|---|---|---|---|
| `CDS10_WT` | CDS_0010, unknown-function fiber | 105–917 | 813 aa | 91.63 kDa | 6.82 |
| `CDS11_WT` | CDS_0011 tail spike, β-helix depolymerase body | 305–941 | 667 aa | 72.02 kDa | 6.65 |
| `CDS12_WT` (the GH5) | CDS_0012, GH5 glycoside hydrolase | 117–477 | 361 aa | 41.84 kDa | 7.25 |
| `CDS12_ANC_Node1` (`e1`) | reconstructed ancestor of CDS_0012 | equivalent of 117–477 | 361 aa | 41.91 kDa | 6.34 |
| `CDS12_ANC_Node40` (`e40`) | reconstructed ancestor of CDS_0012 | " | 361 aa | 42.20 kDa | 5.30 |
| `CDS12_ANC_Node281` (`e281`) | reconstructed ancestor of CDS_0012 | " | 361 aa | 42.27 kDa | 5.82 |

All six carry pET-28a's `MGSSHHHHHHSSGLVPRGSHM` leader and are therefore **N-terminally
His6-tagged**, whatever the Twist filenames say. CDS_0011 additionally carries a
`GGSGGGGS`-His6-`ENLYFQ` (TEV) linker. Source genome numbering is Prof. Espinoza's
`UUAIURNK_` CDS index for 9-2-1 Φ8.

**Provenance that must be stated on every part page:** the GH5 phylogeny and the
ancestral-state reconstruction that produced Node1 / Node40 / Node281 are **Prof. Espinoza's
work, not the students'**. The reconstruction program and the node definitions are still
pending from him (asked in
[`2026-10-18_pi_contribution_questionnaire.md`](2026-10-18_pi_contribution_questionnaire.md)) —
until he answers, **do not describe the three nodes as "deep", "mid" or "shallow"**; we do not
know their positions on the tree.

## 2. How the models were made

| Tool | Input | Output | Used for |
|---|---|---|---|
| AlphaFold3 Server (Prof. Espinoza, 2026-07-14/15) | full-length CDS_0010 (917 aa), CDS_0011 ×3 (941 aa), CDS_0012 (477 aa); real MSA + PDB templates | 5 models each, pLDDT + PAE + pTM/ipTM | the three wild-type parts |
| ESMFold v1 (`facebook/esmfold_v1`, run locally, `fold_ancestors.py`) | single sequence, mature insert, leader stripped | 1 model, pLDDT in the B-factor column | the three ancestors, which have no AF3 job |
| PyMOL 3.1 (`render_constructs.py`) | the models above | cartoon renders, superpositions, Cα RMSD | figures and the WT-vs-ancestor comparison |
| Biopython `PairwiseAligner` (BLOSUM62, global) | mature inserts | pairwise % identity | `sequence_identity.csv` |

**Acceptance thresholds we report against** (following PHOENICS, the 2025 Best Part Collection
winner): a domain is called *modelled* at mean pLDDT ≥ 70 and *high-confidence* at ≥ 90;
structural equivalence between an ancestor and the wild type is called at backbone
RMSD < 2 Å over the aligned core.

**The two sources are not equivalent evidence.** AF3 had a real MSA and templates; ESMFold is
a single-sequence language-model fold with no MSA and no template. Ancestral panels are
therefore coloured by pLDDT rather than by domain, and no ancestral claim rests on the fold
alone.

## 3. Simulation comparison

From `code/output/1018_construct_structures/construct_comparison.csv`:

| Part | Model source | pTM | ipTM | mean pLDDT over the construct | fraction pLDDT ≥ 70 | % identity to CDS12_WT |
|---|---|---|---|---|---|---|
| `CDS10_WT` | AF3 monomer | 0.80 | — | **90.8** | 0.983 | 30.5¹ |
| `CDS11_WT` | AF3 trimer | 0.66 | 0.64 | **90.3** | 0.986 | 28.3¹ |
| `CDS12_WT` | AF3 monomer | 0.77 | — | **96.4** | 0.989 | 100 |
| `CDS12_ANC_Node1` | ESMFold | — | — | see `construct_comparison.csv` | " | **77.8** |
| `CDS12_ANC_Node40` | ESMFold | — | — | " | " | **52.6** |
| `CDS12_ANC_Node281` | ESMFold | — | — | " | " | **51.0** |

¹ cross-family identities (CDS_0010 / CDS_0011 vs the GH5) come from a forced global alignment
of unrelated proteins and are **alignment noise, not homology**. Only the CDS_0012-family
numbers are meaningful.

Three things the table says:

1. **The wild-type constructs are all high-confidence over exactly the region we cloned.**
   Mean pLDDT 90–96 and ≥ 98 % of residues above 70 inside the construct boundaries. The
   truncations were chosen to cut away the parts AF3 *cannot* place — for CDS_0011 the
   Calx-β anchor (res 1–110) and the shaft (111–300), which land 41–92 Å apart across the five
   AF3 models while the body (301–941) superposes at 0.44–0.99 Å RMSD.
2. **CDS_0011's low ipTM (0.64) is not a bad interface.** It is dragged down by that floppy
   appendage; the inter-chain PAE minimum is ≈ 2 Å. The trimer is real, and res 921–941 is a
   foldon that must stay in the construct — which it does (305–941).
3. **The ancestors are not evenly spaced around the wild type.** Node1 is 77.8 % identical to
   CDS12_WT, but Node40 and Node281 are only 52.6 % and 51.0 % identical to it while being
   **87.3 % identical to each other**. So the panel is really *wild type + one near relative +
   one distant sister pair*. Any host-range difference seen with e40 and e281 but not e1 is
   consistent with that structure; a difference seen with e1 alone would be harder to explain.

## 4. What the two protein families are, and why both are in the kit

### RBP — the receptor-binding protein (CDS_0011, and CDS_0010 alongside it)

A phage finds its host with **receptor-binding proteins**: tail fibers and tail spikes that sit
at the bottom of the virion and recognise one surface molecule on one host. RBP specificity is
what makes phage therapy narrow-spectrum — it is the targeting module, and swapping it is how
phage host range is engineered.

For 9-2-1 Φ8 the relevant facts we established:

- **CDS_0011 is the tail spike**: an N-terminal Calx-β β-sandwich (res 1–110) that anchors to
  the virion, a shaft, and a **right-handed β-helix / β-solenoid body (res 301–941)** that
  trimerises. A β-helix of that kind is the canonical fold of a **depolymerase** — an RBP that
  does not merely bind the host surface sugar but cleaves it.
- **CDS_0010 shares the same Calx-β anchor** (42 % identity over 107 aa) — a paralogous fiber
  using the same virion-attachment module. Its remaining ~800 aa have **no template at all**.
  The PI withdrew the glycosidase call for CDS_0010 on 2026-07-29; our part page must call it
  **unknown function**, which is also why it is the one construct we express purely to find out
  what it is.
- **The receptor is an LPS O-antigen sugar, not a protein.** That conclusion closed the
  RBP × OMP docking screen (retired: the controls failed twice, with two tools, and
  cross-kingdom pairs have no paired MSA). It is also why the three ANI-distinct host strains,
  which carry three non-homologous O-antigen cassettes in the same `ihfB`-flanked slot, are
  predicted not to be cross-infected — untested.
- The 2026-10-10 resistant-mutant sequencing supports a surface-sugar receptor: the 9-6-2 R1
  mutant's only confirmed change is **Stealth CR3 F126L** in the capsule-type cluster, with the
  O-antigen locus untouched.

### GH5 — glycoside hydrolase family 5 (CDS_0012 and its three ancestors)

**GH5** is a CAZy family of glycoside hydrolases: clan GH-A, a **(β/α)₈ TIM barrel**, retaining
mechanism, two catalytic glutamates on the C-terminal face of the barrel — an acid/base Glu in
the conserved **NEP** motif and a nucleophile further along the barrel. GH5 contains the
classic bacterial endoglucanases (cellulases), and in phage genomes GH5-like enzymes act as
**depolymerases**: they strip the polysaccharide barrier — capsule, EPS, O-antigen — that
stands between the phage and the cell surface, and they are the part of a phage that works as a
free enzyme, without the virion.

What we can say about ours:

- CDS_0012 is **template-confirmed** GH5: all four AF3 templates over res 118–475 are GH5
  endoglucanases (**1ECE** with cellotetraose bound, **1VRX**, **4TUF**, **2ZUM**), at
  pLDDT 95–98. It is the single best-supported structural call in the project.
- **It is a separate protein from the tail spike.** When the PI asked for "the enzymatic domain
  within the tail spike", the confirmed GH5 was CDS_0012, not a domain of CDS_0011. Our part
  pages must keep these distinct — one β-helix depolymerase (CDS_0011) and one TIM-barrel
  glycoside hydrolase (CDS_0012).
- **The NEP acid/base motif is conserved in all four variants** — `IGADLYNEPHL` in CDS12_WT
  (insert position 165) and `IGADL(Y/H)NEPH` in the three ancestors (position 166), with the
  downstream `SPH(D/E)Y` block likewise conserved. The catalytic machinery survived the
  reconstruction, which is the minimum precondition for the ancestors to be active enzymes.
  **UNDONE:** assign the second catalytic Glu (the nucleophile) by superposing each model on
  1ECE rather than by motif guessing.
- Why reconstruct ancestors at all: the hypothesis is that an **ancestral GH5 has a broader
  substrate range** than the modern, host-specialised enzyme, so an ancestor may clear a sugar
  coat that the wild-type enzyme cannot — including on phage-resistant mutants. That is the
  Track A × B experiment in
  [`2026-10-05_last_2_week_lab_planning.md`](2026-10-05_last_2_week_lab_planning.md): spot
  e1 / e40 / e281 / wild type on resistant lawns and look for a halo.

## 5. What the predictions do **not** show, and the state of the wet lab

Per the benchmark: a predicted structure in a winning Registry page always sits in the *design*
section, next to a wet-lab readout. Ours, honestly:

- **No construct has been confirmed to express yet.** 2026-09-15 gels were inconclusive;
  2026-09-29 gave one induction-dependent band at 40–43 kDa for `CDS12_WT` (on its predicted
  41.8 kDa) and an unassigned 45–50 kDa band for `e1`; 2026-10-10 Ni-NTA of `e281` **failed** —
  blank elutions, flow-through identical to the load.
- **The untransformed-BL21(DE3) control lane is still UNDONE after three gels.** Until it is
  run, no band can be assigned, and no part page may claim expression.
- The four CDS_0012-family proteins differ by at most 0.43 kDa (1.0 %) and **cannot be told
  apart by SDS-PAGE**; distinguishing them needs sequencing or intact-mass MS.
- Therefore every structure figure in this set is captioned as *prediction*, and the
  characterisation sections of the Registry pages stay empty until the control gel and the
  spot assay produce data.

---
*Log — 2026-10-18: created. AF3 numbers read from Prof. Espinoza's 2026-07-14/15 server jobs;
ESMFold models run locally the same day (slow on an 8 GB laptop — one 361 aa chain at a time).
Captions deliberately avoid any claim about where Node1/40/281 sit on the GH5 tree, pending the
PI's answer.*
