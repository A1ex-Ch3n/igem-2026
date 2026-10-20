# CDS12_ANC_Node281 — reconstructed ancestral GH5, node 281 (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-GH5-ancN281` — reconstructed ancestral GH5 glycoside hydrolase (node 281) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa. From `registry_parts.ffn` |
| Source | **Computationally designed sequence — not found in nature.** Ancestral-state reconstruction at node 281 of a GH5 phylogeny built around CDS_0012 of bacteriophage 9-2-1 Φ8, by Prof. J. Espinoza. Reconstruction: the top 1000 NCBI nr hits to CDS_0012 were aligned with MUSCLE in SeaView and manually curated to the region covered by the extant query; the tree was built with PhyML (WAG, invariant-site proportion fixed at 0.1, 100 bootstrap replicates); ancestral states were inferred in IQ-TREE under the same WAG matrix with the tree midpoint-rooted. |
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

> **Tree position (resolved 2026-10-18).** The PI reconstructed every ancestral node on the path
> from CDS_0012 to the root. The labels are arbitrary identifiers, not depths, but their order is
> 1, 2, 38, 39, 40, 42, 267, 277, 281, running from the most recent ancestor to the most ancestral.
> Node 281 is therefore the deepest of our three, the closest to the root of the tree. Reconstruction order and sequence identity agree, so the three ancestral parts
> form a genuine depth series and not three arbitrary points.

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

The 10-10 gel alone could not distinguish no expression, insoluble product, and a dead column.

**Anti-His dot blot, 2026-10-19** (`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`;
measured in `code/1019_dotblot/`). Eleven samples spotted directly onto membrane and probed with
a single-step anti-His HRP conjugate. The positive control reached ~18x the negative control, so
the chemistry worked. A dot blot reports **the His tag, not size or activity**, and this one's
detection floor is high — every 1:10 dilution on the membrane fell to background — so absence of
signal here is weak evidence of absence.

**This part's flow-through (`e281 FT1`) was His-positive at 2.9x the negative control** — the
second strongest signal on the membrane. That settles the three-way ambiguity above: **the
protein was expressed and it did not bind the resin.** The failure is capture, not expression,
so the next move is the binding conditions — imidazole carried into the load, binding time,
resin choice — not another identical purification. An untransformed BL21(DE3) control lane is
still outstanding.

## characterisation

**First activity data, 2026-10-16 — essentially negative for this variant.**

**Spot test, 2026-10-16** (`code/1016_spot_test_result.ipynb`; figure and caption in
`code/output/1016_spot_test_result/`). Seven *Pseudomonas* strains were grown as double-layer
lawns (200 µL culture in 3 mL soft agar). Each plate received five 7 µL drops: phage Φ8 stock
(positive control), sterile 1× PBS (negative control), and the `e1`, `e40` and `e281`
preparations, each diluted 1:10 in that same sterile PBS. Spotted 12 Oct, read 16 Oct.

No drop produced a clear lysis zone, Φ8 included. The readout was colony growth inside the
drop: sterile PBS drops reproducibly developed discrete colonies (median 14 per drop), which is
the baseline for a liquid drop landing on these lawns. Against that baseline the medians were
**Φ8 0, `e1` 1, `e40` 10, `e281` 9**.

The crude `e281` lysate reduced colony counts only slightly, from a median of 14 to 9.

Every plate carried its own sterile-PBS drop, and that baseline varied between plates (7–17
colonies), so the comparable figure is **each drop as a percentage of the PBS drop on the same
plate**. On that scale the medians are **Φ8 0 %, `e1` 12 %, `e281` 53 %, `e40` 67 %**
(`spot_percent_of_pbs.tsv`). This variant sits at **53 %**, close to the
no-effect line.

**What this does and does not establish.**
- The `e281` preparation is a **crude lysate**, not purified protein, so the
  enzyme is not enriched in it. A weak effect here is **not** evidence that this variant is
  inactive; the experiment cannot tell a missing activity from a diluted one.
- Expression is now supported: the `e281` flow-through was His-positive on the 2026-10-19 blot.
  That does **not** rescue this result, because what was spotted here was the **1:10 crude
  lysate**, and every 1:10 dilution fell below that blot's detection floor. How much enzyme was
  in the drop remains unknown.
- By contrast the `e1` preparation, the only one that had been through a purification step,
  suppressed colonies almost completely in the same experiment (median 1). That difference
  tracks the preparation, not necessarily the sequence.
- The wild-type enzyme CDS12_WT was **not** spotted in this run, so the ancestor-versus-modern
  comparison the design asks for has not been made yet.
- One concentration, one plate per strain, colonies counted by automated image segmentation;
  no replicates and no statistics.
- No clearing means no halo, so this is not depolymerase activity in the classical sense.
- **Cannot be distinguished from CDS12_WT or the other two ancestors by SDS-PAGE** — all four
  are within 0.43 kDa (1.0 %). Identification needs sequencing or intact-mass MS.
- Note for anyone reading the `e1` result beside this one: that activity is **not yet
  attributed to the protein** either. `e1` tracks phage Φ8 strain by strain, so carry-over of
  infectious phage from the Φ8 stock remains the leading alternative, and a plaque assay of
  the preparation is the experiment that would settle it.
- Planned next: purify this variant, equalise protein against the others, and re-spot with an
  elution-buffer-only control and CDS12_WT on the same plate.

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
Both open items above were resolved on 2026-10-18 from the PI's handover — see
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md), A1.*

*Log — 2026-10-18: characterisation updated with the 2026-10-16 spot test
([`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)).
**This edit still has to be made on registry.igem.org** — the part page there was
transcribed from the earlier version of this draft.*
