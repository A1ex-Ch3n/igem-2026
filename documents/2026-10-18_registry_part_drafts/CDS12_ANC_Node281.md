# CDS12_ANC_Node281 — reconstructed ancestral GH5, node 281 (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-GH5-ancN281` — reconstructed ancestral GH5 glycoside hydrolase (node 281) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa. From `registry_parts.ffn` |
| Source | **Computationally designed sequence — not found in nature.** Ancestral-state reconstruction at node 281 of a GH5 phylogeny built around CDS_0012 of bacteriophage 9-2-1 Φ8, by Prof. J. Espinoza. ⬜ **UNDONE: name the reconstruction program, the alignment and the tree before submitting.** |
| Designed for | *Escherichia coli* (expression host) |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` N-terminal His6 leader |
| Team shorthand | `e281` |

**Functional description (design intent):** a reconstructed ancestor of the phage GH5
glycoside hydrolase, the most distant of our three from the modern enzyme, made to test
whether an ancestral enzyme has a **broader substrate range** than its modern descendant.

---

## design

**The hypothesis** is shared across the three ancestors: ancestral enzymes tend to be more
promiscuous than their modern specialised descendants, so an ancestral GH5 may cleave surface
polysaccharides the wild-type enzyme cannot — including on phage-**resistant** hosts. The
three nodes are designed as a set; see the collection page.

**Where this sequence sits** (percent identity over the 361 aa mature insert):

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node281** | **51.0** | 57.1 | **87.3** | — |
| Node1 | 77.8 | — | 61.8 | 57.1 |
| Node40 | 52.6 | 61.8 | — | 87.3 |

**The most distant of the three from the modern enzyme (51.0 %)**, and 87.3 % identical to
Node40. The two behave as a pair, which gives the panel an internal replicate at the far end.

> ⬜ **UNDONE — do not describe this node by tree depth** ("shallow", "recent", "closest to the
> extant clade") until the PI tells us where node 281 sits on his tree. Only the identities
> above are ours to state.

**Structure.** ESMFold v1, single sequence, no MSA, no template: **mean pLDDT 85.8**, 88.1 % of
residues above 70. Superposed on the ESMFold model of CDS12_WT it gives **0.52 Å** backbone
RMSD. Half the sequence has changed and the GH5 TIM barrel is unmoved; the differences are in
surface loops, which is also where the model's confidence is lowest.

Method validation, as for the others: wild-type CDS12_WT folded with the same single-sequence
method superposes on Prof. Espinoza's AlphaFold3 model of the same region at **0.28 Å over
2139 atoms**.

**Catalytic machinery is intact.** The acid/base glutamate sits in the conserved **NEP** motif
— `IGADLHNEPHG` at insert position 166 — with the conserved `SPHDY` block downstream. It
shares the Tyr→His substitution immediately before the motif with Node40, a difference from
both Node1 and the wild type and an obvious first thing to test if these two distant ancestors
behave alike.

**Relationship to the other parts.** A variant of **CDS12_WT**, the template-confirmed GH5 —
a **free, standalone enzyme**. Unrelated to the tail spike **CDS_0011** (depolymerase on
fold evidence only) and to **CDS_0010** (function unknown).

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience; order sheet filed
2026-09-10. *E. coli* BL21(DE3), kanamycin, IPTG induction at 16–20 °C.

⚠️ **`Codon Optimized: No`**, mammalian-like codon bias — the first suspect behind a missing
band; try Rosetta or BL21-CodonPlus.

This is the only construct we have attempted to purify, and **the purification failed**
(2026-10-10, `code/1010_gel_annotation.ipynb`):

- Ni-NTA **elutions E1 and E2 were blank gel** — peak prominence 0.011 against a measured 0.020
  noise floor, lane totals inside the never-loaded range.
- **Flow-through was indistinguishable from the load**: the same 40–44 kDa band in both.
  Nothing bound the resin, so that band — close to the predicted 42.3 kDa — behaves like a host
  protein, not like a His6-tagged construct.
- The crude 2026-09-29 gel had already shown no band at 42.3 kDa for this construct.

The result cannot distinguish between no expression, insoluble product, and a dead column. The
documented next step is **not** to purify again, but to run crude ±IPTG beside an untransformed
BL21(DE3) lane, or an anti-His western.

## characterisation

**None, and one documented negative result** (the failed purification above), reported because
the Registry states that negative and inconclusive results are still valuable.

- **Cannot be distinguished from CDS12_WT or the other ancestors by SDS-PAGE** — all four are
  within 0.43 kDa (1.0 %). Identification needs sequencing or intact-mass MS.
- Planned readout: establish expression first, then spot on sensitive and Φ8-resistant lawns
  beside the wild-type enzyme, with imidazole-vehicle and PBS controls.

## application

With Node40, the **far arm** of the ancestral panel — the pair furthest from the modern
enzyme's specificity, and the most likely of the three to act where the wild type cannot.

## discussion

**Limitations.** A reconstructed sequence is a hypothesis about a protein that no longer
exists. Expression is unconfirmed and one purification attempt failed outright. Non-optimised
codon usage is a live risk. The structural evidence is a single-sequence model.

**What the failed purification does and does not say.** It does not say the protein is absent —
no control lane has yet excluded that the construct simply is not being expressed, and no
insoluble-pellet lane was run. Anyone reusing this part should prove the protein exists in
crude lysate before committing a column to it, and should keep the pellet as its own lane.

**Comparison within the set.** Being the most diverged (51.0 % to the wild type), this node is
the strongest test of the promiscuity hypothesis and the most likely to misfold or express
poorly. Its near-twin Node40 is the control for both of those risks.

## attribution

- **Prof. J. Espinoza** — the GH5 phylogeny, the ancestral-state reconstruction and the choice
  of nodes. **The sequence of this part is his design, not the students'.**
- **Team students** — structural comparison of the variants, cloning, expression trials,
  Ni-NTA attempt, gel densitometry.
- Every named author, including the PI, must opt in on registry.igem.org first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).
Two UNDONE items above must be resolved with the PI before this part leaves Draft.*
