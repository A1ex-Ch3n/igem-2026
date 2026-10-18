# CDS12_ANC_Node40 — reconstructed ancestral GH5, node 40 (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-GH5-ancN40` — reconstructed ancestral GH5 glycoside hydrolase (node 40) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa. From `registry_parts.ffn` |
| Source | **Computationally designed sequence — not found in nature.** Ancestral-state reconstruction at node 40 of a GH5 phylogeny built around CDS_0012 of bacteriophage 9-2-1 Φ8, by Prof. J. Espinoza. Reconstruction: the top 1000 NCBI nr hits to CDS_0012 were aligned with MUSCLE in SeaView and manually curated to the region covered by the extant query; the tree was built with PhyML (WAG, invariant-site proportion fixed at 0.1, 100 bootstrap replicates); ancestral states were inferred in IQ-TREE under the same WAG matrix with the tree midpoint-rooted. |
| Designed for | *Escherichia coli* (expression host) |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` N-terminal His6 leader |
| Team shorthand | `e40` |

**Functional description (design intent):** a reconstructed ancestor of the phage GH5
glycoside hydrolase, more distant from the modern enzyme than node 1, made to test whether an
ancestral enzyme has a **broader substrate range** than its modern descendant.

---

## design

**The hypothesis** is the same as for the other two ancestors: ancestral enzymes are repeatedly
found to be more promiscuous than their modern, specialised descendants, so an ancestral form
of our GH5 may cleave a surface polysaccharide the wild-type enzyme cannot — including on
phage-**resistant** hosts. The three nodes only make sense as a set; see the collection page.

**Where this sequence sits** (percent identity over the 361 aa mature insert):

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node40** | **52.6** | 61.8 | — | **87.3** |
| Node1 | 77.8 | — | 61.8 | 57.1 |
| Node281 | 51.0 | 57.1 | 87.3 | — |

This node is **far from the modern enzyme (52.6 %) but very close to Node281 (87.3 %)**. Node40
and Node281 therefore behave as a *pair*: a difference seen with both of them, and not with
Node1, is the pattern this design predicts most strongly. A difference seen with Node40 alone
would need explaining.

> **Tree position (resolved 2026-10-18).** The PI reconstructed every ancestral node on the path
> from CDS_0012 to the root. The labels are arbitrary identifiers, not depths, but their order is
> 1, 2, 38, 39, 40, 42, 267, 277, 281, running from the most recent ancestor to the most ancestral.
> Node 40 is therefore an intermediate node on that path. Reconstruction order and sequence identity agree, so the three ancestral parts
> form a genuine depth series and not three arbitrary points.

**Structure.** ESMFold v1, single sequence, no MSA, no template: **mean pLDDT 85.5**, 87.3 % of
residues above 70. Superposed on the ESMFold model of CDS12_WT it gives **0.50 Å** backbone
RMSD — the same GH5 TIM barrel, despite only ~52 % sequence identity. The lower pLDDT relative
to Node1 is concentrated in surface loops, which is where the reconstruction differs most.

The method is validated in the same way as for the other ancestors: wild-type CDS12_WT folded
with this single-sequence method superposes on Prof. Espinoza's AlphaFold3 model of the same
region at **0.28 Å over 2139 atoms**.

**Catalytic machinery is intact.** The GH5 acid/base glutamate sits in the conserved **NEP**
motif — `IGADLHNEPHG` at insert position 166 — with the conserved `SPHDY` block downstream.
Note the Tyr→His substitution immediately before the motif relative to Node1 and the wild type
(`…DLY NEP…` → `…DLH NEP…`), shared with Node281; it is adjacent to the catalytic residue and
is a sensible first thing to look at if the two distant ancestors behave alike.

**Relationship to the other parts.** A variant of **CDS12_WT**, the template-confirmed GH5 —
a **free, standalone enzyme**. Unrelated to the tail spike **CDS_0011** (depolymerase on
fold evidence only) and to **CDS_0010** (function unknown).

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience; order sheet filed
2026-09-10. *E. coli* BL21(DE3), kanamycin, IPTG induction at 16–20 °C.

⚠️ **`Codon Optimized: No`**, mammalian-like codon bias — the first suspect behind a missing
band; try Rosetta or BL21-CodonPlus.

**2026-09-15 SDS-PAGE**: this construct's lane on gel 1 was **effectively unloaded**, so that
experiment says nothing about it. No usable lane has been run since. In the project's
expression plan it is **batch 2**, behind CDS12_WT and `e1`.

## characterisation

**None.** No interpretable gel lane, no purification, no activity data.

- **Cannot be distinguished from CDS12_WT or the other two ancestors by SDS-PAGE** — all four
  are within 0.43 kDa (1.0 %). Identification needs sequencing or intact-mass MS.
- Planned readout: purify, then spot on sensitive and Φ8-resistant lawns beside the wild-type
  enzyme, with imidazole-vehicle and PBS controls.

## application

With Node281, the **far arm** of the ancestral panel: the pair that probes furthest from the
modern enzyme's specificity, and therefore the most likely of the three to act on a
polysaccharide the wild type cannot.

## discussion

**Limitations.** A reconstructed sequence is a hypothesis about a protein that no longer
exists. No expression, no activity, no interpretable gel lane yet. Non-optimised codon usage is
a live risk. The structural evidence is a single-sequence model: it shows the fold survived
reconstruction, not that the enzyme works.

**Comparison within the set.** Node40 and Node281 are 87.3 % identical to each other and ~52 %
to the wild type. Treating them as a pair is the honest reading of the panel, and it is also
what makes the experiment interpretable: two near-identical distant ancestors give an internal
replicate that Node1 does not have.

## attribution

- **Prof. J. Espinoza** — the GH5 phylogeny, the ancestral-state reconstruction and the choice
  of nodes. **The sequence of this part is his design, not the students'.**
- **Team students** — structural comparison of the variants, cloning, expression trials, gel
  densitometry.
- Every named author, including the PI, must opt in on registry.igem.org first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).
Both open items above were resolved on 2026-10-18 from the PI's handover — see
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md), A1.*
