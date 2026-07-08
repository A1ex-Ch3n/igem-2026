# Phage sequencing reads

Raw phage sequencing reads, one subfolder per host site. Reads are gitignored
(`data/phage_genome/**/*.fastq.gz`) — kept on disk, not in the repo.

Storage / provenance context: [`../dna_extraction_inventory.md`](../dna_extraction_inventory.md).
Assembly pipeline (runs on Laguna): [`../../code/0708_phage_assembly/`](../../code/0708_phage_assembly/).

---

## `9-2-1/` — Φ8 on host 9-2-1 (vendor `3NKSC3`), back 2026-07-08

Phage isolate **Φ8**, plaque-picked and propagated on host **9-2-1**, then whole-genome
sequenced. First phage genome data of the project. **Reads only — the vendor delivered no
QC report, no assembly, and no genome-size estimate.**

**Platform.** Illumina **NovaSeq X Plus** (instrument `LH01080`, flowcell `23MFHLLT3`,
lane 1, dual-index `GAGGTTAGAC+GCAATACATT`), **2×151 bp** paired-end, 2-color chemistry with
binned quality (most bases Q41 — high quality).

**Files.**

| File | Read pairs | Notes |
|---|---:|---|
| `3NKSC3_1_9_2_1_ph8_R1.fastq.gz` | 9,933,775 | raw, uniform 151 bp, untrimmed |
| `3NKSC3_1_9_2_1_ph8_R2.fastq.gz` | 9,933,775 | raw mate |
| `3NKSC3_1_9_2_1_ph8_hostremoved_R1.fastq.gz` | 9,743,410 | vendor host-removed + lightly trimmed |
| `3NKSC3_1_9_2_1_ph8_hostremoved_R2.fastq.gz` | 9,743,410 | vendor host-removed mate |

- **Raw yield:** ~3.00 Gbp (9.93M pairs × 2 × 151 bp).
- **Vendor host removal:** only **190,365 pairs (1.9%)** dropped as host. We do **not** assemble
  these files — we redo host removal ourselves from raw against our own 9-2-1 reference, and use
  this 1.9% only as a cross-check. Host-removed headers are reformatted (index stripped) and reads
  are already length-trimmed, so they differ from raw by more than host content.

**Two caveats that shape assembly.**
1. **Extreme overcoverage.** ~2.9 Gbp of phage-enriched reads against any plausible phage genome
   (40–250 kb) is **~11,000×–73,000×**. That degrades SPAdes, so coverage is normalized to ~100×
   (`bbnorm`) before assembly.
2. **Single-phage origin not confirmed.** Re-isolation rounds 2 & 3 were never done (`UNDONE` in
   [`../../scheme/20260604_confirmed_scheme_CLAUDE.md`](../../scheme/20260604_confirmed_scheme_CLAUDE.md)),
   so this pick may contain >1 phage. Assembly inspects **all** contigs rather than assuming one genome.

**Host reference** (decontamination target, from the matched bacterial genome):
`../bacteria_genome/9-2-1/XH254M_1_sample_1_1_reference.fasta` — *Pseudomonas_E* sp013179515
(P. putida group).

**Assembly + annotation (done 2026-07-08)** — see [`9-2-1/assembly/NOTES.md`](9-2-1/assembly/NOTES.md).
A single **62,338 bp, circular, novel phage genome** (SPAdes `NODE_13`, cov 1014× vs 3–6× background;
read-back 98.44%). pharokka: 80 CDS, GC 62%, 96.3% coding density, complete structural modules
(portal/terminase/tail spike+fiber), **temperate** (integrase present), **safe** (0 virulence, 0 AMR),
**novel** (no INPHARED mash hit). Our own host removal found **~15% host vs the vendor's 1.9%**.
Reference genome to use: `9-2-1/assembly/pharokka_phage/pharokka_dnaapler_reoriented.fasta`.

**Not yet in hand:** the companion `9-6-2 Φ8` pick (same 06/05 plaque batch) has not come back.

---

*Log: 2026-07-08 — created. Filed the `3NKSC3` delivery under `9-2-1/`; recorded platform, read
counts, host-removal delta, and the coverage / single-phage caveats from direct inspection of the
FASTQs.*
