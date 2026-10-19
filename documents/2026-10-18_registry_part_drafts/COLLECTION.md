# Collection page — Phage Φ8 surface-polysaccharide toolkit (draft)

The six parts as one set. Paste this into the Registry collection page.
Chinese version: [`COLLECTION_zh.md`](COLLECTION_zh.md).

---

## Title

**Phage 9-2-1 Φ8 surface-polysaccharide toolkit: three virion proteins and an ancestral series
of their glycoside hydrolase**

## Summary

Six basic parts from a single soil phage, **9-2-1 Φ8**, isolated and sequenced by our team from
a *Pseudomonas* host. Three are the phage's own virion proteins, taken straight from the
genome. Three are reconstructed ancestors of one of them. Together they are a set for one
question: **can an ancestral enzyme act on bacterial surface sugars that its modern descendant
cannot reach?**

| Part | Registry ID | What it is | Evidence grade |
|---|---|---|---|
| CDS12_WT | `BBa_267WQM51` | GH5 glycoside hydrolase, a free standalone enzyme | template-confirmed |
| CDS11_WT | `BBa_26DKNAEC` | tail-spike β-helix depolymerase body | fold-level only |
| CDS10_WT | `BBa_269KJB8G` | virion fiber | function unknown |
| CDS12_ANC_Node1 | `BBa_26TWEX42` | reconstructed ancestor of CDS12, nearest | computational design |
| CDS12_ANC_Node40 | `BBa_26EK89VW` | reconstructed ancestor, deeper | computational design |
| CDS12_ANC_Node281 | `BBa_26LHLSLW` | reconstructed ancestor, deepest of the three | computational design |

## Why these six belong together

**The problem.** Phage therapy fails when a host changes the surface sugar the phage binds.
The phage's depolymerases are specialists, each tuned to one host's polysaccharide. That
specificity is the useful property and the failure mode at once.

**The hypothesis.** Reconstructed ancestors of enzyme families are repeatedly found to be more
**promiscuous** than their modern descendants. If that holds for a phage depolymerase, an
ancestral form of it may cleave polysaccharides the modern enzyme cannot — including those of
hosts that have escaped the phage.

**The design.** CDS12_WT is the modern enzyme; the three ancestral nodes are reconstructions
along the path from it to the root of its GH5 phylogeny. CDS11_WT and CDS10_WT are the other
two surface-contacting proteins from the same virion, included because the question is about
the phage's whole surface-recognition apparatus, not one enzyme in isolation.

**The panel is not evenly spaced,** and that is deliberate. Over the 361 aa mature insert,
Node1 is **77.8 %** identical to CDS12_WT, while Node40 and Node281 are **52.6 %** and
**51.0 %** to the wild type but **87.3 %** to each other. So the set is *wild type + one near
relative + one distant sister pair*. Node1 is the conservative test: if even that ancestor
behaves differently, the effect is unlikely to be an artefact of sequence distance.

## What is established

- **All three ancestors fold to the same GH5 TIM barrel as the wild type.** ESMFold v1,
  single sequence: backbone RMSD 0.28 / 0.50 / 0.52 Å for Node1 / Node40 / Node281 against the
  CDS12_WT model, all far inside the 2 Å equivalence criterion. The reconstruction changed the
  surface, not the fold.
- **That modelling method is itself validated here.** Folding the wild type the same way and
  superposing it on Prof. Espinoza's AlphaFold3 model of the same region gives **0.28 Å over
  2139 atoms**, so the ancestral models are not single-sequence artefacts.
- **Catalytic machinery is intact in all three** — the GH5 acid/base glutamate sits in the
  conserved NEP motif with the conserved SPHEY block downstream.
- **CDS10_WT and CDS11_WT share an N-terminal Calx-β anchor** (42 % identity over 107 aa,
  anchors superposing at 0.50 Å over 446 atoms): paralogous fibers on a common
  virion-attachment module.

## What is not established

Stated plainly, because it is most of what a reuser needs to know:

- **No expression is confirmed for any of the six parts.** Three SDS-PAGE sessions produced one
  induction-dependent band at the predicted mass for CDS12_WT and one unassigned band for
  `e1`; the untransformed-BL21(DE3) control lane that would settle either is still outstanding.
- **The four CDS_0012-family proteins cannot be told apart by SDS-PAGE** — all within 0.43 kDa
  (1.0 %) of each other. Identification needs sequencing or intact-mass MS.
- **One activity result exists and it is unattributed.** In a spot test on 2026-10-16, the
  `e1` preparation suppressed colony growth inside the drop to a median of 12 % of the
  same-plate sterile-PBS control, against 0 % for phage Φ8 and 53–67 % for the crude `e40` and
  `e281` lysates. But `e1` tracks the phage strain by strain, including their shared failure on
  one strain, so **carry-over of infectious phage from the Φ8 stock is still the leading
  alternative explanation**. A plaque assay of the preparation itself is the experiment that
  would settle it, and it has not been run.
- **No ancestor-versus-modern comparison has been made.** CDS12_WT was not in that spot test.
- **The inserts are not codon-optimised** and carry mammalian-like codon bias, which is the
  first thing to suspect behind a missing band. Rosetta or BL21-CodonPlus is the obvious next
  host.

## How to reuse this collection

The set is designed to be taken as a whole or in two halves.

- **For a phage-therapy project:** CDS12_WT plus the three ancestors is a ready-made
  modern-versus-ancestral panel for any depolymerase activity assay. The fold and catalytic
  residues are checked; what is missing is expression and activity, so the panel is a starting
  point rather than a result.
- **For an ancestral-sequence-reconstruction project:** the three nodes are a worked example
  with the full method recorded — top 1000 NCBI nr hits, MUSCLE in SeaView, manual curation,
  PhyML (WAG, p-inv 0.1, 100 bootstraps), ancestral states in IQ-TREE, midpoint-rooted — plus
  the structural validation of the resulting sequences.
- **For a phage-biology project:** CDS10_WT and CDS11_WT are two surface proteins from a novel
  62 kb phage, one with a fold-level depolymerase assignment and one genuinely unassigned.

All six are expression constructs cloned into **pET-28a(+)** via NdeI/XhoI, for
*E. coli* BL21(DE3). **The vector's N-terminal His6 leader is not part of any of these parts'
sequences**, and no part carries a C-terminal tag.

## Attribution

The GH5 phylogeny, the ancestral-state reconstruction and the choice of nodes are
**Prof. J. Espinoza's work**, not the students'. The three ancestral sequences are his design.
The students contributed the phage isolation and sequencing, the structural comparison of the
variants, the cloning and expression trials, the gel densitometry, and the spot test.
Every named author, including the PI, must opt in on registry.igem.org before being credited.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/` and
`code/output/1016_spot_test_result/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).*
