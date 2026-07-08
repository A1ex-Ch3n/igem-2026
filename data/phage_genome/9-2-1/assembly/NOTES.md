# 9-2-1 Φ8 — assembly + annotation notes

First assembled phage genome of the project. Isolate **Φ8** propagated on host **9-2-1**
(vendor `3NKSC3`, reads back 2026-07-08). Pipeline: [`code/0708_phage_assembly/`](../../../../code/0708_phage_assembly/),
run on Laguna. **Host removal was redone from raw** (we did not trust the vendor's host-removed files).

## Headline result
The whole phage assembled as **one complete 62,338 bp contig** (no gaps, full module set) — a clean,
safe, novel phage. **Read coverage indicates a circular genome** (uniform, no linear-DTR spike);
PhageTerm on the full reads will confirm the exact packaging (see Completeness below).

## Read processing (our own, from raw)
| Step | Number |
|---|---|
| Raw pairs | 9,933,775 |
| After fastp trim | 9,805,539 pairs |
| Aligned concordantly to 9-2-1 host | 14.34% (overall alignment 15.17%) |
| **Kept as non-host** | **85.66% = 8,399,296 pairs** |
| Subsampled for assembly (seqtk) | 600,000 pairs |
| Read-back rate onto assembly | **98.44%** |

- **Our host fraction ~15% vs the vendor's 1.9%** — an ~8× gap. The vendor's `hostremoved` files
  leave substantial host in; redoing it against this strain's own genome was the right call.

## Assembly (SPAdes `--isolate`, from 600k subsampled pairs)
- 235 contigs ≥1 kb; 113 ≥10 kb. **But only one is the phage.**
- **`NODE_13`: 62,338 bp, coverage 1014×** — vs every other contig at 3–6×. The 200× coverage gap
  makes the phage unambiguous. The other 234 contigs (incl. some 100–158 kb but only 3–5×) are
  low-coverage background — the un-purified lysate's environmental / residual-host DNA.
- The phage was ~1/3 of the non-host reads; the rest is that background. (This plaque was **not**
  re-isolated to single-phage purity — rounds 2 & 3 were `UNDONE` — but the target phage still
  dominates cleanly by coverage.)

## Annotation (pharokka v1.10)
- **62,338 bp, GC 62%, 80 CDS, 96.3% coding density**, 2 tRNAs, 0 CRISPRs.
- Functional modules (PHROGs): head & packaging 11 (portal, terminase), tail 4 (tail spike ×2,
  tail fiber, tail protein), DNA/RNA/nucleotide metabolism 9, transcription regulation 3,
  moron/host-takeover 3, lysis 1, **integration & excision 2**, unknown 45.
- **Completeness / topology — read coverage points to CIRCULAR:** the genome is **one contig,
  62,338 bp, 0 gaps**, full module set + reorientable terminase (dnaapler → terL start, phrog hit 97.7%
  cov / 64.7% id) + 96% coding density → **complete genome**. For topology we ran a k-mer read-coverage
  check ([`../../../code/0708_phage_assembly/check_terminal_redundancy.py`](../../../code/0708_phage_assembly/check_terminal_redundancy.py),
  300k reads): coverage is **uniform (~357×, max/median 1.63×) across the whole genome including both
  ends, with no ~2× spike**. That is the **circular** signature and argues *against* a T7-style linear
  Direct Terminal Repeat (a real short DTR, collapsed by the assembler, would show a sharp ~2× coverage
  spike over the repeat — absent here). No terminal redundancy in the contig sequence either.
- **Reconciling the PI group's reported ~70 bp terminal repeat:** most consistent with a
  **circularization overlap** (the redundant sequence an assembler keeps at the circular join, ~ its
  k-mer length ≈70 bp) — i.e. it *confirms circular*, and our SPAdes contig simply has that overlap
  trimmed (clean 62,338 bp, 0 terminal redundancy). It is unlikely to be a biological linear DTR given
  the flat coverage. **To settle packaging definitively:** run **PhageTerm** on the full reads (Laguna)
  — it classifies DTR vs cos vs pac/headful vs circular from read-end distributions and gives the exact
  repeat — and confirm which tool/method gave the PI group's 70 bp. Plus CheckV for a completeness %.
  (All UNDONE — see below.)

## Three things that matter for the project
1. **Temperate phage.** The `integration & excision` genes (integrase/excisionase) mean it can
   lysogenize. If the goal is a therapeutic phage, temperate lifestyle is a caveat (lysogeny +
   transduction risk) — may need engineering to lytic, or picking a virulent phage instead.
2. **Safe.** VFDB virulence factors = 0, CARD AMR genes = 0. Carries no virulence or resistance genes.
3. **Carries RBPs.** tail spike (`CDS_0015`/`0016`) and tail fiber (`CDS_0018`) are the
   receptor-binding proteins that set host specificity — the experimental counterpart to the
   computational binding screen. See [[project_phage_receptor_binding_screen]].

## Novelty
mash vs INPHARED: **`no_inphared_mash_hit`** (no known phage within mash distance 0.2) → relatively
**novel**. Formal classification/novelty still to do: terL phylogeny or whole-genome comparison
(VIRIDIC / NCBI). The terL hit to a phrog terminase at only 64.7% identity is consistent with novelty.

## Files here
- `phage_genome.fasta` — the 62 kb phage contig (as assembled).
- `pharokka_phage/pharokka_dnaapler_reoriented.fasta` — **use this as the reference genome** (reoriented to terL start).
- `pharokka_phage/pharokka.gbk` / `.gff` — full annotation.
- `pharokka_phage/pharokka_cds_final_merged_output.tsv` — per-CDS functions.
- `contigs_min1kb.fasta` / `contig_summary.txt` — the full 235-contig assembly (phage + background).
- `bowtie2_host.log`, `readback.log`, `fastp.html` — QC.

## UNDONE
- **CheckV completeness + circularity** — CheckV DB download failed on Laguna (NERSC SSL drop); retry
  for a quantitative completeness %. Also confirm circularity from the SPAdes assembly graph /
  terminal-repeat structure (the contig has no exact terminal redundancy, so "circular" is inferred,
  not proven). Evidence above indicates a complete genome; circularity is likely but unconfirmed.
- **Formal taxonomy** — terL phylogeny / VIRIDIC vs NCBI to place genus/family and confirm novelty.
- **Companion `9-6-2 Φ8`** — same 06/05 plaque batch, not yet sequenced.

---
*Log: 2026-07-08 — created after the first successful assembly+annotation run on Laguna.*
