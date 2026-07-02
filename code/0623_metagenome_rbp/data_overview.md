# 0623 Sequencing Data Overview

Inventory of the two sequencing datasets that feed the metagenome-RBP pipeline.
Everything here is read directly from the delivered files; **inferred** items are flagged.

Inputs:
- `data/bacteria_genome/` — host bacterial whole-genome sequencing (3 isolates)
- `data/metagenomes/` — environmental metagenome predicted proteins (2 samples)

Isolates are named by their **site name** — the trailing token of each result folder
(`..._sample_9_6_2` → site `9-6-2`). Every number below is reproduced in
[`data_overview.ipynb`](data_overview.ipynb), which parses the delivered files directly.

| Site | Result folder |
|---|---|
| `9-6-2` | `9-6-2/rerun_QB9Y48` |
| `9-2-1` | `9-2-1` |
| `10-10-2` | `10-10-2` |

---

## 1. Bacterial genomes — `data/bacteria_genome/`

Long-read (Oxford Nanopore) bacterial WGS delivered as **complete, circular, single-contig
genomes** with full Bakta annotation and QC. The output layout (ONT read stats + Flye-style
assembly graph + sourmash species ID + CheckM + circos + Bakta) is the signature of a
commercial ONT bacterial-genome service (**inferred**: Plasmidsaurus-style pipeline).

### Samples (3 isolates, 2 order IDs)

| Site | Order ID | Species (sourmash/GTDB) | Genome size | GC | Topology | CheckM compl. / contam. |
|---|---|---|---|---|---|---|
| `9-6-2` | QB9Y48 (**rerun**) | *Pseudomonas_E* sp013179515 | 6,178,775 bp | 62.4% | circular, 1 contig, fully resolved | 99.74% / 1.94% |
| `9-2-1` | XH254M, sample 1 | *Pseudomonas_E* sp013179515 | 6,178,779 bp | 62.4% | circular, 1 contig, fully resolved | 99.74% / 1.94% |
| `10-10-2` | XH254M, sample 3 | *Pseudomonas_E* sp013179515 | 5,933,216 bp | 62.6% | circular, 1 contig, fully resolved | 99.74% / 0.87% |

All three resolve to the same species, *Pseudomonas_E* sp013179515 (GTDB lineage
`d__Bacteria;p__Pseudomonadota;c__Gammaproteobacteria;o__Pseudomonadales;f__Pseudomonadaceae;g__Pseudomonas_E`),
query ANI ≈ 0.995–0.997.

> **Sites `9-6-2` and `9-2-1` have near-identical genomes** (size differs by 4 bp, identical
> GC, CDS 5448 vs 5449) despite the different site labels — `9-6-2` is the `_rerun_` assembly.
> They are very likely the same isolate (or clonal). **Site `10-10-2` is distinct** (~245 kb
> smaller). → so likely **2 unique strains across 3 assemblies.** See open question Q1.

### Read / assembly QC (`*_ont-stats.tsv`, `*_checkm-results.tsv`)

| Site | Total reads | Bases | Raw cov / final cov | Median read | Median Q | Read NG50 |
|---|---|---|---|---|---|---|
| `9-6-2` (rerun) | 107,609 | 435 Mb | 70.4× / 66.9× | 2,484 bp | Q24.2 | 51,165 |
| `9-2-1` | 354,501 | 1,935 Mb | 313.1× / 94.0× | 3,436 bp | Q25.8 | 66,805 |
| `10-10-2` | 128,866 | 522 Mb | 87.9× / 83.5× | 2,350 bp | Q24.2 | 54,751 |

CheckM lineage `g__Pseudomonas (UID4525)`; all near-complete, low contamination.

### Annotation (Bakta v1.12.0, DB v6.0 full)

| Site | CDSs | tRNA | rRNA | ncRNA | hypotheticals | pseudogenes | coding density |
|---|---|---|---|---|---|---|---|
| `9-6-2` | 5,448 | 74 | 22 | 42 | 232 | 11 | 89.6% |
| `9-2-1` | 5,449 | 74 | 22 | 42 | 233 | 11 | 89.6% |
| `10-10-2` | 5,267 | 73 | 22 | 50 | 177 | 10 | 89.7% |

No CRISPR arrays, no plasmids/oriV reported in any isolate.

### Files per sample

Top level of each `*_sample_*` folder:
- `*_reference.fasta` / `*_reference.gbk` — final polished genome (assembly + GenBank)
- `*_sourmash-genome-species.csv`, `*_sourmash-contigs-species.csv` — taxonomy (GTDB lineage, fraction, ANI)
- `*_checkm-results.tsv`, `*_checkm-plot.png` — completeness/contamination
- `*_ont-stats.tsv` — read-set stats (coverage, N-stats, Q)
- `*_ont-contigs.txt` / `.png` — assembly-graph summary
- `*_prepolished-assembly-info.yaml` — contig count, length, topology
- `*_circos.png`, `*_reads.png` — figures
- (XH254M_1 only) `*_sourmash-contigs-species.xlsx`

`annotation/` subfolder (Bakta output) per sample:
- `*_reference.faa` — **protein sequences** (CDS), Bakta locus tags (e.g. `PICBEH_00001`)
- `*_reference.ffn` — CDS nucleotide; `*_reference.fna` — full genome nucleotide
- `*_reference.gff3`, `.gbff`, `.embl`, `.json` — annotation in standard formats
- `*_reference.tsv` — **per-feature table**: `Sequence Id, Type, Start, Stop, Strand, Locus Tag, Gene, Product, DbXrefs` (DbXrefs include UniRef, KEGG, COG, EC, GO, RefSeq)
- `*_reference.hypotheticals.faa` / `.tsv` — hypothetical proteins only
- `*_reference.inference.tsv` — annotation evidence/source per feature
- `*_reference.png` / `.svg` — genome plot; `*_reference.log`
- Per-isolate `*_report.html` at the order-folder top level

**For the RBP pipeline, the actionable host files are the Bakta `*_reference.faa` (proteome)
and `*_reference.tsv` (annotated gene table)** — these give the host surface-protein /
receptor candidates per strain.

---

## 2. Metagenomes — `data/metagenomes/`

Two samples, each delivered as a **single `.faa` of predicted protein sequences** — no
nucleotide contigs, no taxonomy, no functional annotation.

| File | Predicted proteins | Source contigs | Size |
|---|---|---|---|
| `MG08.faa` | 706,108 | 608,062 | 176 MB |
| `MG09.faa` | 650,535 | 566,380 | 159 MB |

Header format (example):
```
>NODE_1_length_175154_cov_17.107334_1 # 1 # 429 # -1 # ID=1_1;partial=10;start_type=ATG;rbs_motif=None;rbs_spacer=None;gc_cont=0.688
```
This tells us:
- **Assembler = SPAdes/metaSPAdes** — `NODE_<n>_length_<L>_cov_<C>` is the SPAdes contig naming (**inferred** from header).
- **Gene caller = Prodigal** (metagenomic mode) — `# start # stop # strand # ID=...;partial=...;start_type=...;rbs_motif=...;gc_cont=...` is Prodigal's protein-FASTA header (**inferred**).
- Per protein we know: parent contig, contig length & k-mer coverage, gene coordinates, strand, whether the gene runs off the contig edge (`partial`), start codon, RBS motif, and GC.
- Contig lengths span ~286 bp to ~175 kb (MG08); most predicted proteins sit on short, low-coverage contigs typical of a fragmented metagenome.

These are the search space for mining phage RBP homologs (the 1,673-seq literature RBP DB
in `code/output/0619_literature_rbp_database/` → matches in MG08/MG09).

---

## 3. Open questions (resolve before building the search)

1. **Strain identity** — Are sites `9-6-2` and `9-2-1` the same isolate (rerun), giving
   **2 unique strains** total despite the two site labels? Which lab strains / binding-screen
   hosts do sites `9-6-2`, `9-2-1`, `10-10-2` correspond to?
2. **Metagenome provenance** — What sample / environment are MG08 and MG09 from, and how do
   they relate to the host isolates? (Same source material? Enrichment?)
3. **Only proteins for metagenomes** — Are nucleotide contigs / read sets available if needed
   (e.g. to recover full-length partial genes), or is the `.faa` the complete deliverable?
4. **Species resolution** — sourmash maps all isolates to one GTDB species at ANI ~0.995; is
   strain-level differentiation needed for host-specificity claims?

---

## Log
- 2026-06-23 — Initial overview of `bacteria_genome` (3 ONT isolates, Bakta) and `metagenomes` (MG08/MG09 Prodigal proteomes); counts read directly from files, assembler/gene-caller inferred from headers.
- 2026-06-23 — Switched isolate naming to site names (`9-6-2`, `9-2-1`, `10-10-2`); added `data_overview.ipynb` reproducing every figure from the delivered files.
