# CDS11_WT — tail-spike β-helix depolymerase body (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-TSP-body` — tail-spike β-helix depolymerase body (CDS_0011 res 305–941) |
| Sequence | 1917 bp = `ATG` + CDS + stop → 638 aa. From `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8, a novel ~62 kb podovirus isolated from soil by this team; CDS_0011 of the PI's `UUAIURNK_` Pharokka annotation. Construct = res 305–941 of the full-length 941 aa protein |
| Designed for | *Escherichia coli* (expression host); source organism = phage 9-2-1 Φ8 |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` leader, and the designed `GGSGGGGS`-His6-`ENLYFQ`-`GGGGSGGGGS` purification linker — both described below |

**Functional description (design intent):** the trimeric β-helix body of a phage tail spike,
expressed on its own as a candidate polysaccharide depolymerase against the host's LPS
O-antigen.

---

## design

CDS_0011 is the **tail spike** of phage 9-2-1 Φ8 — a structural protein of the virion, and the
protein that makes contact with the host surface. Its 941 aa fold has three parts:

| Residues | Module | Confidence |
|---|---|---|
| 1–110 | Calx-β β-sandwich — the virion-attachment anchor | all four AF3 templates (3US9, 3EAD, 2FWU, 2KLT) map here |
| 111–300 | shaft | **AF3 cannot place it**: across five models it lands 41–52 Å apart |
| 301–941 | right-handed **β-helix / β-solenoid body** + receptor-binding region | rigid, pLDDT 88–94, models superpose at 0.44–0.99 Å |
| 921–941 | foldon — carries the trimer contacts, must stay in the construct | — |

**The construct is res 305–941**: the rock-solid body and the foldon, with the unplaceable
shaft and the anchor removed. That boundary came from superposing the PI's five AF3 models —
the body is self-trimerising and self-contained, everything N-terminal of ~301 is a floppy
appendage.

**What kind of enzyme this is, and how strong that claim is.** A right-handed β-helix is the
canonical fold of a phage **depolymerase** — an enzyme that cleaves the host's surface
polysaccharide rather than merely binding it. We call CDS_0011 a depolymerase **on fold
evidence alone**: AF3 has *no* template for res 111–941, and the β-helix was identified from
the sequence-offset period of its backbone hydrogen bonds (the method in our
[`phagecheck`](https://gitlab.igem.org) tool), not from a named homolog.

> **This is a different claim, with different evidence, from CDS_0012.** CDS_0012 is a
> template-confirmed GH5 glycoside hydrolase and is a **separate protein**, not a domain of
> this tail spike. Do not read "the tail spike contains a GH5" anywhere — we have no evidence
> for that. CDS_0011 = the virion-attached spike whose body is a β-helix depolymerase;
> CDS_0012 = the standalone GH5 enzyme.

**Relationship to CDS_0010.** The two fibers share the same N-terminal Calx-β
virion-attachment module: 42 % sequence identity over 107 aa, and superposing the two anchors
gives **RMSD 0.50 Å over 446 atoms**. They are paralogous fibers built on a common attachment
part.

**Tag and linker.** The plasmid we built adds pET-28a's N-terminal His6 leader plus a designed
`GGSGGGGS`-His6-`ENLYFQ` (TEV) linker, for Ni-NTA purification and tag removal. The insert ends
in its own stop codon, so the vector's C-terminal His6 is never translated — **despite the
construct filename, this protein has no C-terminal tag.** Neither the leader nor the linker is
part of the biological sequence, so neither is in the submitted part.

**Models:** AlphaFold3 Server trimer, pTM 0.66 / ipTM 0.64, mean pLDDT 90.3 inside the cloned
region. The low ipTM is not a bad interface — it is dragged down by the floppy N-terminal
appendage, and the inter-chain PAE minimum is ≈ 2 Å. The AF3 folds are **Prof. J. Espinoza's**
work (see *attribution* below).

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience, order of 2026-07-27.
Expression host *E. coli* BL21(DE3), kanamycin selection, IPTG induction at ~30 °C.

**Status: expression not yet demonstrated for this part.** Across three SDS-PAGE sessions
(2026-09-15, 09-29, 10-10) no band was seen at the expected 72.0 kDa; on 09-29 no undiluted
lane was run for this construct, so the absence is not yet interpretable. The
untransformed-BL21(DE3) control lane is still outstanding, so no band on these gels can be
assigned either way.

## characterisation

**None.** No confirmed expression (see *experiment*), no purified protein, and therefore no
activity assay.

The readout this part needs is a **spot assay on a host lawn**: a halo from purified protein
where the buffer control gives none would be direct evidence of depolymerase activity.
Controls fixed in advance: imidazole vehicle, PBS, a phage-positive spot, and the sensitive
parent strain from the same batch. A first spot test was run on 2026-10-16, but it covered only
the three ancestral GH5 variants — **this part was not in it**.

Until that assay exists, the depolymerase assignment for this part is a **structural
hypothesis, not a measured activity**.

## application

Intended as the **targeting and surface-stripping module** of a phage-derived antibacterial
toolkit against soil *Pseudomonas*. A free depolymerase strips the polysaccharide barrier
without requiring an infective virion, which is why the body is expressed separately from the
phage.

Context from the project: the three ANI-distinct host strains carry **three non-homologous
O-antigen cassettes in the same `ihfB`-flanked slot**, sharing only 4 of 45 ortholog clusters.
Since the receptor is that sugar, host range is predicted to track the cassette — untested, and
stated here as a prediction, not a result.

## discussion

**Limitations.**
- The depolymerase assignment is **fold-level**, with no named homolog and no template for
  res 111–941. It should be treated as a hypothesis until an activity assay exists.
- The cut at res 305 removes the virion anchor by design: this part cannot assemble into a
  virion, and is not meant to.
- 72 kDa of trimeric β-solenoid is a hard expression target; if it proves insoluble, refolding
  or a lower induction temperature are the next steps.

**For other teams.** The construct-boundary method is the reusable part: superpose several
predicted models, keep what is rigid across them, and cut where the models disagree. Here that
turned an ambiguous 941 aa protein into a self-contained 637 aa trimer.

## attribution

- **Prof. J. Espinoza** — the AlphaFold3 folds of CDS_0010/0011/0012 and the Pharokka
  annotation (`UUAIURNK_`) this numbering comes from; the construct-boundary request.
- **Team students** — phage isolation, sequencing and assembly; the domain-mapping analysis that
  set res 305–941; cloning, expression trials and gel analysis.
- Record these per author with the Registry's **Contribution Roles**. Every named author,
  including the PI, must opt in on registry.igem.org first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).*
