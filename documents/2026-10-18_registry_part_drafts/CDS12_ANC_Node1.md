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

> **Registry "Functional Description" field — closing sentence, updated 2026-10-19.**
> The live field on `registry.igem.org/parts/bba-26twex42` ends *"Expression has not been
> confirmed; see the documentation entries."* That is now out of date. Replace with:
>
> > Anti-His dot blot on 2026-10-19 gave a positive signal for this construct's induced lysate,
> > at 2.4x the negative control; the product has not been assigned by size. See the
> > documentation entries.

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

**Anti-His dot blot, 2026-10-19** (`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`;
measured in `code/1019_dotblot/`). Eleven samples spotted directly onto membrane and probed with
a single-step anti-His HRP conjugate; the positive control reached ~18x the negative control.
**The `e1` rough lysate was His-positive at 2.4x the negative control**, the third strongest
signal on the membrane. A dot blot reports **the His tag, not size**, so this supports
expression of a tagged product but does not distinguish full-length protein from a truncation
or from free tag — and so does not by itself assign the unexplained 45-50 kDa band.

## characterisation

**First activity data, 2026-10-16 — a positive but preliminary signal.**

**Spot test, 2026-10-16** (`code/1016_spot_test_result.ipynb`; figure and caption in
`code/output/1016_spot_test_result/`). Seven *Pseudomonas* strains were grown as double-layer
lawns (200 µL culture in 3 mL soft agar). Each plate received five 7 µL drops: phage Φ8 stock
(positive control), sterile 1× PBS (negative control), and the `e1`, `e40` and `e281`
preparations, each diluted 1:10 in that same sterile PBS. Spotted 12 Oct, read 16 Oct.

No drop produced a clear lysis zone, Φ8 included. The readout was colony growth inside the
drop: sterile PBS drops reproducibly developed discrete colonies (median 14 per drop), which is
the baseline for a liquid drop landing on these lawns. Against that baseline the medians were
**Φ8 0, `e1` 1, `e40` 10, `e281` 9**.

The `e1` drops suppressed colony growth almost completely, as did the phage, on six of the
seven strains. The `e1` drop was 90 % the same sterile PBS, so the difference comes from the
`e1` preparation itself.

Every plate carried its own sterile-PBS drop, and that baseline varied between plates (7–17
colonies), so the comparable figure is **each drop as a percentage of the PBS drop on the same
plate**. On that scale the medians are **Φ8 0 %, `e1` 12 %, `e281` 53 %, `e40` 67 %**
(`spot_percent_of_pbs.tsv`).


**What this does and does not establish.**
- It is the first evidence that the `e1` preparation carries an activity against *Pseudomonas*,
  and the strongest signal of the three ancestral variants.
- It does **not** identify the active agent as this protein. Expression now has positive
  evidence — the `e1` rough lysate was His-positive at 2.4x on the 2026-10-19 blot — but a His
  tag in the lysate does not make this protein the active species, and the elution buffer the
  preparation sits in (imidazole) was not spotted on its own.
- **The largest remaining confound is phage carried over from the Φ8 stock.** Across the seven
  strains `e1` tracks the phage almost exactly — both fall below 40 % on six strains, and the
  single strain where the phage failed (9-1-1, at 157 %) is also the one where `e1` failed
  (114 %). An infectious contaminant would produce precisely that agreement. **The deciding
  experiment is a plaque assay of the `e1` preparation itself on a 9-2-1 lawn**; it has not
  been done. Suppression in this assay does not require infection either — Φ8 cleared colonies
  on two of the three strains it cannot plaque — so the fact that `e1` works on non-hosts does
  *not* resolve this.
- The wild-type enzyme CDS12_WT was **not** spotted in this run, so the ancestor-versus-modern
  comparison the design asks for has not been made yet.
- One concentration, one plate per strain, colonies counted by automated image segmentation;
  no replicates and no statistics.
- No clearing means no halo, so this is not depolymerase activity in the classical sense.
- **Cannot be distinguished from CDS12_WT or the other two ancestors by SDS-PAGE** — all four
  are within 0.43 kDa (1.0 %). Identification needs sequencing or intact-mass MS.
- Planned next, in order: (1) plaque assay of the `e1` preparation on a 9-2-1 lawn, (2) an
  elution-buffer-only drop, (3) a dilution series of `e1`, (4) the same plate run with
  CDS12_WT alongside. Full reasoning in `code/output/1016_spot_test_result/figure_caption.md`.

## application

The **broad-spectrum arm** of a phage-derived antibacterial toolkit: an enzyme that may clear
surface polysaccharides the modern enzyme cannot, for use against hosts that have escaped the
phage by changing their sugar. Reusable by any team that wants an ancestral-enzyme variant of a
phage depolymerase to compare against a modern one.

## discussion

**Limitations.**
- A reconstructed sequence is a **hypothesis about a protein that no longer exists**; it is not
  evidence about any real ancestral phage.
- Expression is supported by anti-His signal (2026-10-19), but the product has never been
  assigned by size: the 45-50 kDa band remains unexplained, and a dot blot cannot tell
  full-length protein from a truncation or from free tag.
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

*Log — 2026-10-18: characterisation updated with the 2026-10-16 spot test
([`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)).
**This edit still has to be made on registry.igem.org** — the part page there was
transcribed from the earlier version of this draft.*
