# Structure-predict the 9-2-1 Φ8 union RBPs on Laguna

Fold the **union RBP set** (RBP Detect ∪ Pharokka; 8 CDS) to confirm the tail-spike
**β-helix / β-solenoid depolymerase** fold and localize the variable RBD. **Structure
only — no RBP×receptor ipTM docking this round** (existing MSA-free screen's controls
don't separate; primary receptor is likely LPS O-antigen). Reuses the `localcolabfold`
install already on Laguna.

**Do NOT upload these novel phage sequences to the public MSA server → `--msa-mode single_sequence`.**

## Inputs
| File | Folds |
|---|---|
| `structures_monomers.csv` | 8 monomers (CDS 0002/0014/0015/0016/0017/0018/0019/0020) |
| `structures_trimers.csv` | 3 homotrimers (tail spikes 0015/0016 + tail fiber 0018) |

Rebuild with `python build_structure_inputs.py` after any change to the union FASTA.
Note: CDS_0017 is 917 aa (monomer ~decisive but slow single-seq); the 0015/0016 trimers
(~1.6k / 1.2k residues) are the key folds.

## Run (mirror the existing ColabFold array; path WITHOUT '@')
```bash
CF=/project/jespinoza_1541/$USER/localcolabfold/colabfold-conda
export PATH="$CF/bin:$PATH"; export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"
mkdir -p results
# one combined input (monomers + trimers):
cat structures_monomers.csv > structures.csv && tail -n +2 structures_trimers.csv >> structures.csv
colabfold_batch --num-models 1 --num-recycle 3 --msa-mode single_sequence structures.csv results/structures
```
Submit via OnDemand with the standard header
(`--account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 --cpus-per-task=8 --mem=40G --time=8:00:00`).
If the 0017 monomer or the trimers OOM, split them into a second run or drop `--num-recycle` to 1.

## Collect + interpret
```bash
python collect_structures.py --results results/structures \
  --out ../../output/0712_phage_rbp_detect/structure/structure_summary.tsv
```
- **Tailspike (0015/0016) trimer = right-handed β-helix + surface groove** → depolymerase →
  **primary receptor = LPS O-antigen** (host locus OHPLIO_01274–01298). The variable
  C-terminal block (lower per-fifth pLDDT) marks the RBD.
- New RBP-Detect-only candidate **CDS_0002** (650 aa, Pharokka "hypothetical") — check whether
  it folds into an RBP-like fold or is a classifier false positive.
- Full reasoning: [`../../0708_rbp_analysis/RBP_variable_region_analysis.md`](../../0708_rbp_analysis/RBP_variable_region_analysis.md).

## Backup if single-seq fold quality is poor
- ESMFold (already installed: `code/0703_phage_host_matrix/fold/esmfold/`) — native single-sequence, good on β-helices; or
- build a local MSA (jackhmmer/mmseqs vs a local DB) and re-fold with MSA.

---
*Log: 2026-07-12 — structure-only fold prep for the union RBP set; binding ipTM docking deferred (UNDONE).*
