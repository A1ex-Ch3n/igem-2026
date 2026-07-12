# 0712 — RBP Detect on the 9-2-1 Φ8 phage genome + structure-prediction prep

Three parts:
1. **RBP Detect (local)** — run PhageRBPdetect v4 (ESM-2 t12 classifier) on the phage's
   80 PHANOTATE CDS and mark RBPs independently of the Pharokka annotation, then take the
   **union** of the two evidence sources.
2. **Structure prediction (Laguna)** — fold the union RBPs to confirm the tail-spike
   β-helix depolymerase fold + localize the RBD. Inputs in `fold_structure/`.
3. **Binding screen (Laguna)** — AF2-multimer (ColabFold, **real MSA**) of the 8 union RBPs ×
   15 receptor shortlist (120 pairs) + a 9-fold positive/negative control gate, ranked by ipTM.
   Inputs + run guide in `fold_binding/`. Top hit → refold on AlphaFold3 web.

## Run task 1
```bash
# model (~126 MB, gitignored) → code/0701_phagerbp_metagenome/model/RBPdetect_v4_ESMfine
python code/0701_phagerbp_metagenome/run_rbp_inference.py \
  --fasta data/phage_genome/9-2-1/assembly/pharokka_phage/phanotate.faa \
  --model-dir code/0701_phagerbp_metagenome/model/RBPdetect_v4_ESMfine \
  --out code/output/0712_phage_rbp_detect/predictions_9-2-1_phi8.csv --batch-size 16
python code/0701_phagerbp_metagenome/summarize_rbps.py \
  --out-dir code/output/0712_phage_rbp_detect \
  --sample 9-2-1_phi8 code/output/0712_phage_rbp_detect/predictions_9-2-1_phi8.csv \
    data/phage_genome/9-2-1/assembly/pharokka_phage/phanotate.faa
python code/0712_phage_rbp_detect/phage_rbp_union.py \
  --pred-csv code/output/0712_phage_rbp_detect/predictions_9-2-1_phi8.csv \
  --pharokka-tsv data/phage_genome/9-2-1/assembly/pharokka_phage/pharokka_cds_final_merged_output.tsv \
  --pharokka-curated-faa code/0708_rbp_analysis/seqs/rbps_all.faa \
  --phanotate-faa data/phage_genome/9-2-1/assembly/pharokka_phage/phanotate.faa \
  --out-dir code/output/0712_phage_rbp_detect
```

## Result (2026-07-12)
RBP Detect is **conservative**: only 2/80 CDS called RBP —
**CDS_0016** (tail spike 2, score 0.997; agrees with Pharokka) and **CDS_0002**
(650 aa, Pharokka "hypothetical"; a new detect-only candidate). It **missed** the
divergent tail spike 1 (0015) and tail fiber (0018) — expected for novel RBPs outside
the classifier's training families. Union with the Pharokka tail module (0014–0020) → **8 CDS**.

Outputs in `code/output/0712_phage_rbp_detect/`:
`predictions_9-2-1_phi8.csv`, `9-2-1_phi8_RBPs.{faa,tsv}` (detect-only),
`9-2-1_phi8_RBPs_union.faa` (**deliverable, 8 seqs**), `rbp_detect_vs_pharokka.tsv`.

---
*Log: 2026-07-12 — task 1 done locally (MPS, ~3 min). Task 2 fold inputs prepped; Laguna run + binding docking UNDONE.*
