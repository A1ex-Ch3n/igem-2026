# 1010 — Φ8-resistant picks vs parent (9-2-1 r1, 9-6-2 r1)

Compares Plasmidsaurus order **SBYK6W** (one Φ8-resistant pick per host, ONT, complete
genomes) against the June parent assemblies, then checks every difference against reads.
Everything is in [`resistant_vs_parent.ipynb`](resistant_vs_parent.ipynb).

```bash
conda activate igem2026          # + minimap2, samtools (bioconda)
bash code/1010_resistant_mutant_comparison/map_reads.sh   # ~15 min, writes BAMs
jupyter nbconvert --execute --inplace code/1010_resistant_mutant_comparison/resistant_vs_parent.ipynb
```

Inputs: `data/bacteria_genome/{9-2-1,9-6-2}/resistant_r1_SBYK6W/` (mutant assemblies + reads),
`data/bacteria_genome/9-2-1/reads/` (SRR39379361 from ENA), `data/phage_genome/9-2-1/3NKSC3_*`
(Illumina; the host-derived reads give 71× of the 9-2-1 parent). Outputs →
`code/output/1010_resistant_mutant_comparison/` (BAMs and fastq stay out of git).

## Result
- **9-6-2 r1: one confirmed mutation** — `4,643,730 T>C`, Stealth protein CR3
  (`OHPLIO_04215` / `PICBEH_04214`) **F126L**, in the 4.64–4.67 Mb capsule-type
  polysaccharide cluster. 263/264 mutant reads; 0/176 parent ONT, 0/60 parent Illumina.
- **9-2-1 r1: no confirmed mutation.**
- **O-antigen cassette and LPS core (waa): unchanged in both.**
- No structural change, no Φ8 sequence (not lysogens). Nearly all other assembly
  differences are ONT systematic errors (AF 0.3–0.5 in every ONT read set, 0 in Illumina).

⚠️ The picks were never phenotyped as resistant. See the notebook's UNDONE list.

---
*Log — 2026-10-10: created. Assembly alignment (minimap2 asm5), 5-way allele table,
read validation against ONT + Illumina parent reads, genome-wide pileup scan, cassette and
circos figures.*
