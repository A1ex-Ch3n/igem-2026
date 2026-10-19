# CDS12_WT — GH5 glycoside hydrolase (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-GH5` — phage GH5 glycoside hydrolase (CDS_0012 res 117–477) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa. From `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8, a novel ~62 kb podovirus isolated from soil by this team; CDS_0012 of the PI's `UUAIURNK_` Pharokka annotation. Construct = res 117–477 of the 477 aa protein |
| Designed for | *Escherichia coli* (expression host); source organism = phage 9-2-1 Φ8 |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` N-terminal His6 leader |

**Functional description (design intent):** a phage glycoside hydrolase family 5 (GH5) enzyme,
expressed as a free protein to degrade the host's surface polysaccharide.

---

## design

CDS_0012 is a **glycoside hydrolase family 5** enzyme: CAZy clan GH-A, a **(β/α)₈ TIM barrel**,
retaining mechanism, with the catalytic glutamates on the C-terminal face of the barrel. GH5
contains the classic bacterial endoglucanases, and in phage genomes GH5-like enzymes act as
**depolymerases** — they strip the capsule, EPS or O-antigen that stands between the phage and
the cell surface. Being a soluble enzyme rather than a virion component, it works without the
phage.

**This is the project's strongest structural call.** All four AlphaFold3 templates over
res 118–475 are GH5 endoglucanases — **1ECE** (with cellotetraose bound), **1VRX**, **4TUF**,
**2ZUM** — at pLDDT 95–98. AF3 monomer pTM 0.77; mean pLDDT **96.4** inside the cloned region,
98.9 % of those residues above 70.

> **CDS_0012 is a *separate protein*, not a domain of the tail spike.** When the question was
> posed as "the enzymatic domain within the tail spike", the confirmed glycoside hydrolase
> turned out to be this standalone protein. The tail spike, **CDS_0011**, is a different part:
> virion-attached, and a depolymerase on **fold evidence only** (β-helix, no template, no named
> homolog). Two different proteins, two different enzyme claims, two very different evidence
> grades. CDS_0010 is a third case again — **unknown function**.

**Construct boundary.** res 117–477 is essentially the whole TIM barrel; only a short
N-terminal extension is left out. The barrel is the catalytic unit, so the part is the enzyme.

**Catalytic machinery.** The GH5 acid/base glutamate sits in the conserved **NEP** motif —
`IGADLYNEPHL` at insert position 165 here — and the conserved `SPH(D/E)Y` block follows
downstream. Both are present. *Still to do: assign the second catalytic glutamate (the
nucleophile) by superposing on 1ECE rather than by motif matching.*

**Variants.** Three reconstructed ancestors of this enzyme (`CDS12_ANC_Node1 / _Node40 /
_Node281`) are submitted as separate parts and belong to the same collection. All three fold to
the same TIM barrel: superposed on this protein's model they give **0.28 / 0.50 / 0.52 Å**
backbone RMSD, well inside the 2 Å equivalence criterion, despite Node40 and Node281 sharing
only ~52 % sequence identity with it.

**Model validation.** Folding this sequence with **ESMFold** (single sequence, no MSA, no
template) and superposing on the AF3 model of the same region gives **0.28 Å over 2139 atoms** —
two independent methods agreeing, which is what licenses the use of ESMFold models for the
ancestral variants. The AF3 folds are **Prof. J. Espinoza's** work.

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience, order of 2026-07-27.
*E. coli* BL21(DE3), kanamycin, IPTG induction at 16–20 °C, 16 h.

SDS-PAGE on 2026-09-29 (`code/0929_gel_annotation.ipynb`): an **IPTG-dependent band at
40–43 kDa**, on the predicted 41.8 kDa, absent from the uninduced lane despite that lane
carrying more total protein. This is the project's first induction-dependent signal, and this
construct is first in the purification queue.

Not yet done: untransformed-BL21(DE3) control lane, anti-His western, Ni-NTA purification of
this construct.

## characterisation

**Preliminary and incomplete** — reported as such, per the Registry's note that inconclusive
results still have value.

- One induction-dependent band at the predicted mass (above). **Not** confirmed to be this
  protein: no western, no mass spectrometry, and the control lane that would exclude a host
  band is outstanding.
- No purified protein, therefore **no activity data**.
- Note for anyone reusing these parts: this protein and its three ancestral variants differ by
  at most 0.43 kDa (1.0 %) and **cannot be distinguished by SDS-PAGE**. Identity needs
  sequencing or intact-mass MS.
- **Not included in the 2026-10-16 spot test.** That run compared the three ancestral
  variants against phage Φ8 and a sterile-PBS control on seven *Pseudomonas* lawns
  (`code/1016_spot_test_result.ipynb`); the `e1` preparation suppressed colony growth inside
  the drop almost as completely as the phage. **This wild-type enzyme is the missing
  comparator** — without it on the same plate, no ancestor-versus-modern claim can be made.
  Putting CDS12_WT into that assay is the highest-value next experiment for this part.
- Planned readout: spot assay on a host lawn, halo versus imidazole-vehicle control.

## application

The **lysis/surface-stripping module** of a phage-derived antibacterial toolkit against soil
*Pseudomonas*. As a free enzyme it can be applied without an infective virion — the route we
are pursuing for phage-resistant hosts, where the ancestral variants are tested for a broader
substrate range than the modern enzyme.

## discussion

**Limitations.**
- The GH5 assignment is structural (templates + fold), not enzymatic: no substrate has been
  tested, and the natural substrate is assumed to be the host surface polysaccharide, not
  cellulose.
- Expression evidence is a single band at the right size; it is not yet an identification.
- The nucleophile has not been assigned structurally (see *design*).

**Comparisons.** Against the tail spike CDS_0011, this protein is the better-evidenced enzyme
but the weaker targeting module: the spike carries the host-recognition function and the
trimeric β-helix, while this one is a compact, soluble, monomeric barrel — easier to express,
purify and apply.

**Future directions.** Purify, confirm identity by western or MS, then assay against the
host's purified LPS and against resistant mutants, side by side with the three ancestors.

## attribution

- **Prof. J. Espinoza** — the AlphaFold3 folds, the Pharokka annotation (`UUAIURNK_`), and the
  GH5 phylogeny and ancestral-state reconstruction behind the three variant parts.
- **Team students** — phage isolation, sequencing and assembly; template and domain analysis;
  cloning, expression trials, gel densitometry.
- Record per author with the Registry's **Contribution Roles**; every author must opt in first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).*

*Log — 2026-10-18: characterisation updated with the 2026-10-16 spot test
([`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)).
**This edit still has to be made on registry.igem.org** — the part page there was
transcribed from the earlier version of this draft.*
