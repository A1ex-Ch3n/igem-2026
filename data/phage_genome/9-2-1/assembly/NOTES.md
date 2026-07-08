# 9-2-1 Φ8 — assembly + annotation notes

First assembled phage genome of the project. Isolate **Φ8** propagated on host **9-2-1**
(vendor `3NKSC3`, reads back 2026-07-08). Pipeline: [`code/0708_phage_assembly/`](../../../../code/0708_phage_assembly/),
run on Laguna. **Host removal was redone from raw** (we did not trust the vendor's host-removed files).

## Headline result
The whole phage assembled as **one complete ~62.4 kb genome** with a **~77 bp Direct Terminal Repeat
(DTR)** — a clean, safe, novel **linear DTR podovirus** (T7/Autographiviridae-style). Our SPAdes contig
is 62,338 bp (one DTR copy trimmed + reverse-complemented + rotated); the PI group's assembly
(`PI_assembly/`, 62,416 bp) keeps the DTR at both ends and is the canonical reference. Confirmed by
direct comparison of the two assemblies (see Completeness below).

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
- **Completeness / topology — RESOLVED by comparing to the PI assembly:** the genome is complete with a
  **~77 bp Direct Terminal Repeat (DTR)**. The PI group's assembly (`PI_assembly/PI_Phage_Assembly_Version1.fa`,
  62,416 bp) has an **exact 77 bp prefix==suffix** — a real DTR — at both ends. Direct comparison
  ([`../../../code/0708_phage_assembly/compare_to_PI_assembly.py`](../../../code/0708_phage_assembly/compare_to_PI_assembly.py))
  confirms: **100% of our k-mers are in the PI assembly (same genome)**; the DTR is present in ours once
  (RC, at pos 17703); `62,416 − 77 = 62,339 ≈ our 62,338` → **our SPAdes run trimmed one DTR copy** and
  output the sequence **reverse-complemented + rotated** (why our raw ends looked different).
  A 77 bp DTR = **linear genome with Direct Terminal Repeats** (T7/Autographiviridae), fitting the
  podovirus morphology. My earlier read-only guesses (circular↔linear) were unreliable — the PI
  assembly settles it. See [`PI_assembly/README.md`](PI_assembly/README.md). *(Optional: PhageTerm on
  the full reads can formally classify DTR vs headful; CheckV for a completeness %.)*

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
- **Topology — RESOLVED:** linear genome with a ~77 bp DTR (confirmed against the PI assembly). Optional:
  PhageTerm on the full reads to formally classify the packaging (DTR vs headful); CheckV for a
  quantitative completeness % (DB download failed on Laguna — NERSC SSL drop — retry).
- **Adopt the PI assembly as canonical + re-annotate** — for submission/consistency, re-run pharokka on
  `PI_assembly/PI_Phage_Assembly_Version1.fa` (62,416 bp, DTR both ends, reference orientation) so the
  annotation coordinates match the PI reference. Our current pharokka/RBP coords are on the RC+rotated,
  DTR-trimmed contig (biologically valid, different frame).
- **Formal taxonomy** — terL phylogeny / VIRIDIC vs NCBI to place genus/family and confirm novelty.
- **Companion `9-6-2 Φ8`** — same 06/05 plaque batch, not yet sequenced.

---
*Log: 2026-07-08 — created after the first successful assembly+annotation run on Laguna.*
