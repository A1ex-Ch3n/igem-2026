# CDS10_WT — unknown-function virion fiber (draft part page)

| Field | Value |
|---|---|
| Part type / role | CDS (`SO:0000316`), **basic part** |
| Title | `Phi8-Fiber10` — virion fiber of unknown function (CDS_0010 res 105–917) |
| Sequence | 2445 bp = `ATG` + CDS + stop → 814 aa. From `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8, a novel ~62 kb podovirus isolated from soil by this team; CDS_0010 of the PI's `UUAIURNK_` Pharokka annotation. Construct = res 105–917 of the 917 aa protein |
| Designed for | *Escherichia coli* (expression host); source organism = phage 9-2-1 Φ8 |
| Not included in the sequence | pET-28a's `MGSSHHHHHHSSGLVPRGSHM` N-terminal His6 leader |

**Functional description (design intent):** a virion fiber paralogous to the tail spike,
expressed in order to **determine what it does** — the function is genuinely unknown and this
part is submitted as such.

---

## design

CDS_0010 sits in the tail module of phage 9-2-1 Φ8 and shares its N-terminal **Calx-β
anchor** with the tail spike CDS_0011: 42 % sequence identity over 107 aa, and superposing the
two anchors gives **RMSD 0.50 Å over 446 atoms** (0.96 Å by CE over 88 residues). The two are
**paralogous fibers built on a common virion-attachment module** — that relationship is the
best-supported thing we can say about this protein.

Everything else about it is open:

- Its remaining ~800 residues have **no structural template at all**. The only hit anywhere in
  the chain is a weak IspD match over res 361–456.
- The AF3 model is confident as a *shape* — pTM 0.80, mean pLDDT 90.8 inside the cloned
  region, 98.3 % of those residues above 70 — but confidence in a fold is not a function.

> **This part is deliberately *not* called a glycosidase.** An early annotation suggested one;
> our template analysis never supported it, and the PI withdrew the call on 2026-07-29. The
> honest statement is **unknown function**. We cloned and expressed it for exactly that reason:
> the function of a tail-module protein with no structural template can only be settled
> experimentally.
>
> Keep the three wild-type parts distinct: **CDS_0010 = unknown function**; **CDS_0011** = the
> virion-attached tail spike, a depolymerase on **fold evidence only** (β-helix, no template,
> no named homolog); **CDS_0012** = the template-confirmed **GH5 glycoside hydrolase**, a
> separate, free protein. Three proteins, three different claims, three different evidence
> grades.

**Construct boundary.** res 105–917 cuts just inside the Calx-β anchor (res 1–110), keeping the
large uncharacterised region intact. The anchor is what attaches the fiber to the virion, so
removing most of it gives a soluble protein rather than an assembly component.

**Model:** AlphaFold3 Server monomer, by **Prof. J. Espinoza**.

## experiment

Cloned into **pET-28a(+)** (NdeI/XhoI), synthesised by Twist Bioscience, order of 2026-07-27.
*E. coli* BL21(DE3), kanamycin, IPTG induction at ~30 °C.

**Status: not yet attempted in earnest.** This construct is **batch 3** in the project's
expression plan, behind CDS12_WT and the ancestral variants; at 91.6 kDa it is also the hardest
of the six to express. No gel to date carries an interpretable lane for it.

## characterisation

**None.** No expression, no purification, no activity data. Submitted as a sequence-and-
structure contribution with an explicitly open function.

## application

Two uses, both honest about the state of knowledge:

1. **A functional-characterisation target.** The protein is in hand as a plasmid; any team with
   a *Pseudomonas* host and a surface-polysaccharide assay could test it.
2. **A source of the Calx-β anchor module.** The shared anchor (res 1–110, 42 % identical to the
   tail spike's) is a candidate attachment part for chimeric-fiber work — the module that two
   different fibers of this phage both use.

## discussion

**Limitations.** Function unknown; ~800 aa without a template; the model is confident in shape
only. Expression untested, and 91.6 kDa is a hard target.

**Why submit a part whose function is unknown?** Because the sequence and the structural
relationship are real results, and because the Registry explicitly values negative and
inconclusive documentation. A phage fiber that shares its anchor with a characterised tail
spike, and whose remaining 800 residues match nothing in the PDB, is exactly the kind of entry
another team may one day recognise — and the alternative, labelling it a glycosidase on no
evidence, is how the earlier annotation went wrong.

**Future directions.** Express at low temperature; if soluble, test against the host's purified
LPS alongside CDS_0012; in parallel, search for remote homologs as structure databases grow.

## attribution

- **Prof. J. Espinoza** — the AlphaFold3 fold and the Pharokka annotation (`UUAIURNK_`); also
  the 2026-07-29 withdrawal of the glycosidase call, which this page follows.
- **Team students** — phage isolation, sequencing and assembly; the template and anchor-homology
  analysis; cloning.
- Record per author with the Registry's **Contribution Roles**; every author must opt in first.

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).*
