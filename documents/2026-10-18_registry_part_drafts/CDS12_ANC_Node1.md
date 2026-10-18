# CDS12_ANC_Node1 — reconstructed ancestral GH5, node 1 (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-GH5-ancN1` — reconstructed ancestral GH5 glycoside hydrolase (node 1) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa. From `registry_parts.ffn` |
| Source | **Computationally designed sequence — not found in nature.** Ancestral-state reconstruction at node 1 of a GH5 phylogeny built around CDS_0012 of bacteriophage 9-2-1 Φ8, by Prof. J. Espinoza. Reconstruction: the top 1000 NCBI nr hits to CDS_0012 were aligned with MUSCLE in SeaView and manually curated to the region covered by the extant query; the tree was built with PhyML (WAG, invariant-site proportion fixed at 0.1, 100 bootstrap replicates); ancestral states were inferred in IQ-TREE under the same WAG matrix with the tree midpoint-rooted. |
| Designed for | *Escherichia coli* (expression host) |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` N-terminal His6 leader |
| Team shorthand | `e1` |

**Functional description (design intent):** a reconstructed ancestor of the phage GH5
glycoside hydrolase, made to test whether an ancestral enzyme has a **broader substrate range**
than the modern, host-specialised one.

---

## design

**The hypothesis.** Modern phage depolymerases are specialists: each is tuned to the surface
sugar of its own host, which is also why phage therapy fails against a host that changes that
sugar. Reconstructed ancestors of enzyme families are repeatedly found to be more
**promiscuous** than their modern descendants. So an ancestral form of our GH5 may cleave a
polysaccharide the wild-type enzyme cannot — including on phage-**resistant** mutants. These
three ancestors (`_Node1`, `_Node40`, `_Node281`) are that test, and they only make sense as a
set: see the collection page.

**Where this sequence sits relative to the others** (percent identity over the 361 aa mature
insert, `sequence_identity.csv`):

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node1** | **77.8** | — | 61.8 | 57.1 |
| Node40 | 52.6 | 61.8 | — | 87.3 |
| Node281 | 51.0 | 57.1 | 87.3 | — |

Node1 is **the closest of the three to the modern enzyme** (77.8 %). Node40 and Node281 are far
more distant from it (~52 %) while being 87.3 % identical to each other. The panel is therefore
*wild type + one near relative + one distant sister pair*, not three evenly spaced points.

> **Tree position (resolved 2026-10-18).** The PI reconstructed every ancestral node on the path
> from CDS_0012 to the root. The labels are arbitrary identifiers, not depths, but their order is
> 1, 2, 38, 39, 40, 42, 267, 277, 281, running from the most recent ancestor to the most ancestral.
> Node 1 is therefore the most recent of the reconstructed ancestors on that path. Reconstruction order and sequence identity agree, so the three ancestral parts
> form a genuine depth series and not three arbitrary points.

**Structure.** ESMFold v1, single sequence, no MSA, no template: **mean pLDDT 90.0**, 95.8 % of
residues above 70 — the most confident of the three ancestral models. Superposed on the ESMFold
model of CDS12_WT it gives **0.28 Å** backbone RMSD, far inside the 2 Å equivalence criterion.
The reconstruction changed the surface, not the fold.

That method is itself validated here: folding the wild type with the same single-sequence
method and superposing it on Prof. Espinoza's AlphaFold3 model of the same region gives
**0.28 Å over 2139 atoms**, so these ancestral models are not single-sequence artefacts.

**Catalytic machinery is intact.** The GH5 acid/base glutamate sits in the conserved **NEP**
motif — `IGADLYNEPHQ` at insert position 166 — with the conserved `SPHEY` block downstream.
Same fold, same catalytic residues, different surface: the structural precondition for an
active enzyme with altered specificity.

**Relationship to the other parts.** This is a variant of **CDS12_WT**, the template-confirmed
GH5 — a **free, standalone enzyme**. It is *not* related to the tail spike CDS_0011, whose
depolymerase assignment is fold-level only, and not to CDS_0010, whose function is unknown.

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience; order sheet filed
2026-09-10. *E. coli* BL21(DE3), kanamycin, IPTG induction at 16–20 °C.

⚠️ **`Codon Optimized: No`**, and the insert uses mammalian-like codon bias (`CCC`/`GGG`/`GCC`-
heavy) rather than *E. coli* bias. This is the first thing to suspect behind a missing band;
Rosetta or BL21-CodonPlus is the obvious next host.

**2026-09-29 SDS-PAGE** (`code/0929_gel_annotation.ipynb`): a strong, clean band at
**45–50 kDa in all four lanes, induced and uninduced alike**, 7–19 % above the predicted
41.9 kDa. **Unassigned.** It cannot simply be the product, because CDS12_WT — the same
predicted mass — runs on prediction in the same experiment. A host protein is equally
consistent with the data, and the untransformed-BL21(DE3) control lane that would settle it is
still outstanding.

## characterisation

**None yet, and the one candidate band is explicitly not claimed as this protein.**

- Expression unconfirmed (see *experiment*).
- **This part cannot be told apart from CDS12_WT or the other two ancestors by SDS-PAGE** —
  all four are within 0.43 kDa (1.0 %) of each other. Identification needs sequencing or
  intact-mass MS.
- Planned readout: purify, then spot on lawns of the sensitive host **and** of the Φ8-resistant
  mutants, beside wild-type enzyme, imidazole-vehicle and PBS controls. A halo from the
  ancestor where the wild type gives none is the result the whole design is aimed at.

## application

The **broad-spectrum arm** of a phage-derived antibacterial toolkit: an enzyme that may clear
surface polysaccharides the modern enzyme cannot, for use against hosts that have escaped the
phage by changing their sugar. Reusable by any team that wants an ancestral-enzyme variant of a
phage depolymerase to compare against a modern one.

## discussion

**Limitations.**
- A reconstructed sequence is a **hypothesis about a protein that no longer exists**; it is not
  evidence about any real ancestral phage.
- No expression confirmed, no activity data, and the one observed band is unassigned.
- The non-optimised, mammalian-biased codon usage is a live expression risk.
- The structural evidence is a single-sequence model; it says the fold survived reconstruction,
  not that the enzyme works.

**Comparison within the set.** Being 77.8 % identical to the wild type, this node is the
conservative test: if even *this* ancestor behaves differently from CDS12_WT, the effect is
unlikely to be a sequence-distance artefact. Node40 and Node281 probe much further out.

## attribution

- **Prof. J. Espinoza** — the GH5 phylogeny, the ancestral-state reconstruction, and the choice
  of nodes. **The sequence of this part is his design, not the students'**, and the Contribution
  Roles must say so.
- **Team students** — the structural comparison of the variants, cloning, expression trials,
  gel densitometry.
- Every named author, including the PI, must opt in on registry.igem.org first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).
Both open items above were resolved on 2026-10-18 from the PI's handover — see
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md), A1.*
