# Ancestral reconstruction + ZymCTRL scoring (from the PI)

Extracted from `documents/2026-10-18_prof_documents/SCRIPTS_DATA.zip`, received
2026-10-18. His code, not ours — do not edit in place; copy before modifying.

| File | What |
|---|---|
| `top1000_nr_activesite.fst` | Curated MUSCLE alignment, top 1000 nr hits to CDS_12, trimmed to the extant query's coverage |
| `top1000_nr_activesite-PhyML_tree_rooted` | PhyML tree (WAG, p-inv 0.1, 100 bootstraps), midpoint-rooted |
| `Ancestral_State_Reconstruction.ipynb` | IQ-TREE ASR along the CDS_12 → root path |
| `all_nodes.fa` | Reconstructed ancestral sequences, arbitrary node labels (1, 2, 38, 39, 40, 42, 267, 277, 281 = recent → ancestral) |
| `zymctrl_score.py`, `EC_Scoring.ipynb` | ZymCTRL perplexity per EC number; source of figure panel D |

Method text is in `documents/2026-10-18_pi_questionnaire_answers.md` (A1).
The three ancestral variants we ordered from Twist should be matched back to
these node labels — not yet done.
