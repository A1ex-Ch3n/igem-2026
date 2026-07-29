# 0727 — O-antigen (O-PS) locus comparison across our isolates

Prof. Espinoza asked for "bioinformatics tools capable of predicting the
O-polysaccharide (O-PS) type from bacterial genome sequences, compared across
our three isolates."

**Short answer: no such tool applies to our bacteria.** Every in-silico O-PS
typer is species-bound, and ours is none of the supported species. So this
directory answers the question the other way — by pulling the O-antigen locus
out of each genome and comparing the loci directly.

## Two things to know before reading the numbers

**1. "Three isolates" is really three *strains* out of five isolates.**
`data/bacteria_genome/` holds five: `8-5-2`, `8-10-2`, `9-2-1`, `9-6-2`,
`10-10-2`. Per [`code/0627_unique_strain_table.ipynb`](../0627_unique_strain_table.ipynb)
they collapse to three ANI-distinct strains, and that is what is compared here:

| strain group | isolates | species (GTDB) |
|---|---|---|
| Strain 1 | 8-5-2, 10-10-2 | *Pseudomonas_E* sp013179515 |
| Strain 2 | 9-2-1, 9-6-2 | *Pseudomonas_E* sp013179515 |
| Strain 3 | 8-10-2 | *P. capeferrum* (~87% ANI to the others) |

⚠️ Which three the PI meant is **not confirmed** — this is our inference.
Note also that [`documents/2026-06-27_MRA_Pseudomonas.docx`](../../documents/2026-06-27_MRA_Pseudomonas.docx)
covers only the four *sp013179515* isolates and **excludes 8-10-2**, so the MRA
says "two strains" while this analysis says three. Different scope, not a
contradiction.

**2. Why no existing tool works.**

| tool | scope | why it does not apply |
|---|---|---|
| PAst / PAst2.0 | *P. aeruginosa* OSA clusters O1–O20 | ours are ~80% ANI to PAO1 — a different species |
| Kaptive (all versions) | *Klebsiella*, *A. baumannii*, third-party *V. parahaemolyticus* | no *Pseudomonas* database exists |

There is no reference O-serotype scheme for *Pseudomonas_E* sp013179515, so
**no serotype name can be assigned to any of our strains.** The deliverable is
"the locus architecture differs", not "Strain 1 is O-type X".

## Method

The locus is a variable cassette dropped into a conserved slot, so extraction
is anchored on the **flanks**, not on coordinates. In all five genomes the
upstream flank reads:

```
30S ribosomal protein S1 → integration host factor subunit β (ihfB)
    → Lipopolysaccharide assembly protein A → MBL fold metallo-hydrolase
```

`ihfB` (= *himD*) is the canonical upstream flank of the *Pseudomonas* OSA
cluster in the literature, so the anchor is not arbitrary. The cassette starts
immediately after the MBL hydrolase and runs until the polysaccharide gene
block ends (gap-tolerant; see `GAP` in the script).

Orthology is decided **by sequence, not by product string** — Bakta gives
unrelated glycosyltransferases identical labels, so MMseqs2 clustering
(≥30% identity, ≥50% coverage) does the calling.

```bash
conda activate igem2026
python code/0727_o_antigen_comparison/extract_o_antigen_loci.py
python code/0727_o_antigen_comparison/compare_loci.py
python code/0727_o_antigen_comparison/plot_loci.py
```

## Results

**The three strains carry three different O-antigen cassettes in the same slot.**

| strain group | locus tags | genes | span |
|---|---|---|---|
| Strain 2 | `OHPLIO_01276–01298` / `PICBEH_01275–01297` | 23 | 26.5 kb |
| Strain 1 | `PEMOGA_01378–01392` / `BPBBIK_01378–01392` | 15 | 17.0 kb |
| Strain 3 | `NEEDOG_01333–01357` | 25 | 38.2 kb |

**The clone pairs are the internal control, and they pass.** 9-2-1 vs 9-6-2 —
all 23 genes hit at **100.0%** mean identity, on identical coordinates
(1,409,400–1,435,896). 8-5-2 vs 10-10-2 — all 15 at **100.0%**. This matters:
the argument is that ANI saturates while accessory loci diverge, so we could
not simply *assume* the clone pairs match — it had to be measured.

**Across strain groups the cassettes barely correspond:**

| comparison | genes with a best hit | mean identity | median |
|---|---|---|---|
| Strain 2 ↔ Strain 1 | 9 of 23 | 71.9% | 67.4% |
| Strain 2 ↔ Strain 3 | 10 of 23 | 54.7% | 49.4% |
| Strain 1 ↔ Strain 3 | 6 of 15 | 63.5% | 61.7% |

⚠️ These are **best-hit-per-query in one direction, not reciprocal best hits**,
and they use a looser cutoff (20% identity / 40% coverage) than the clustering
below (30% / 50%). The two sets of counts are therefore **not** meant to
reconcile — a gene can have a weak best hit without joining an ortholog cluster.

Of **45 ortholog clusters** (30% id / 50% cov) across 101 cassette proteins,
only **4** are shared by all three strains — UDP-glucose 4-epimerase, a GT-family-4 transferase, a
CapD-like protein, and an SDR oxidoreductase. All generic sugar chemistry; none
of it assembly machinery. Strains 1 and 2 additionally share the dTDP-rhamnose
trio (`rfbA/rfbB/rfbD`) and the chain-length regulator — the latter despite
Bakta labelling them differently in each strain, which is exactly why orthology
was called by sequence.

Distinctive to each: **Strain 2** carries a UDP-GlcNAc → 2,3-diacetamido-uronic
acid route (`wbpA/wbpB/wbpD`-type), a DegT aminotransferase, `wzx`, a
repeat-unit polymerase (`wzy`), `wbuB`, and an acetamidino modification module
(amidotransferase + HisH + AglZ/HisF2). **Strain 1** carries `wbpL`, `epsG`,
`capD` and four glycosyltransferases, with none of Strain 2's amino-uronic
route. **Strain 3** carries an O-antigen ligase, a separate polymerase, a
D-glucuronyl C5-epimerase, UDP-ManNAc dehydrogenase, and one 6.7 kb ORF
(`NEEDOG_01355`).

The dTDP-rhamnose pathway is arranged differently but is **complete in all
three strains**. Strains 1 and 2 carry `rfbA/rfbB/rfbD` at the end of the
cassette, with `rmlC` (dTDP-4-dehydrorhamnose 3,5-epimerase) elsewhere in the
genome (`OHPLIO_00244`, `BPBBIK_00248`). Strain 3 instead carries the whole
four-gene operon *outside* the cassette (`NEEDOG_00269–00272`, `rmlC` included)
and keeps only a lone `rfbD` inside it.

![O-antigen locus comparison](../output/0727_o_antigen_comparison/o_antigen_loci_comparison.png)

## What this predicts — and what it does not

9-2-1 Φ8's tail spike is a β-helix depolymerase, so its receptor is the host
LPS O-antigen sugar rather than a protein
([`code/0712_phage_rbp_detect/`](../0712_phage_rbp_detect/)). The phage was
isolated on Strain 2 and, per `data/assays/`, has **only ever been tested
against Strain 2** (9-2-1 and 9-6-2).

So this is a **prediction, not an explanation**: if the depolymerase reads
Strain 2's O-antigen, 9-2-1 Φ8 should **fail to plaque on Strain 1 (8-5-2,
10-10-2) and Strain 3 (8-10-2)**. One spot assay tests it. Either outcome is
publishable — a match confirms the mechanism; a miss points at the second
depolymerase (`CDS_0024`, flagged by RBP Detect and missed by Pharokka), which
would then be the more interesting result.

Do **not** state that the O-antigen difference explains observed host range.
No cross-strain plaque data exists yet.

## Limitations

- Assignments are Bakta **product strings**, not experimentally determined
  structures. No sugar composition is claimed.
- `EpsG family protein` and `Polysaccharide biosynthesis protein` (Strain 1)
  are the usual labels for Wzy- and Wzx-family proteins, but Bakta assigns them
  no Pfam/InterPro domain here (UniRef50 only). They are left **unassigned** in
  the figure rather than coloured as machinery we have not confirmed. Strain 1
  therefore *appears* to lack a flippase and polymerase; that is most likely an
  annotation-label artifact, not a real absence.
- The Strain 3 cassette boundary is set by the gene-content rule; its
  downstream flank (`Competence protein ComEA`) differs from strains 1 and 2
  (`Beta-ketoacyl synthase`), as expected for a different species.

## UNDONE

- **Spot assay** — 9-2-1 Φ8 against 8-5-2 / 10-10-2 / 8-10-2. Tests the prediction above.
- **Confirm Wzx/Wzy family assignment** for `BPBBIK_01380` / `BPBBIK_01384`
  (and their 8-5-2 twins) with InterProScan or Pfam HMMs — not available locally.
- **Confirm with the PI which three** he meant, before this goes in a figure legend.
- Sugar-composition work (LPS extraction / MS) if the O-antigen claim needs to
  go beyond gene content.

---
*Log — 2026-07-27: created. Anchor-based extraction of the O-antigen cassette
from all five isolates; MMseqs orthology; three-way comparison figure. Result:
three ANI-distinct strains carry three non-homologous cassettes in the same
`ihfB`-flanked slot, only 4/45 ortholog clusters core, both clone pairs 100%
identical as internal controls. Established that no off-the-shelf O-PS typer
(PAst, Kaptive) covers* Pseudomonas_E *sp013179515. Host-range prediction
recorded as untested. Strain 3 cassette boundary resolved (`NEEDOG_01333–01357`,
contiguous — the apparent gap is a single 6.7 kb ORF). Corrected a first-pass
claim that strains 1 and 2 lack* rmlC *— all five genomes carry it, just outside
the cassette; the rhamnose pathway is complete everywhere.*
