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

## What the ZymCTRL run actually returns — read this before quoting it

Checked 2026-10-20 against the stored outputs in `EC_Scoring.ipynb`.

**The EC classes are glycoside hydrolases, not carboxylases.** The notebook scores
against **23 distinct `3.2.1.x` targets** — the family CDS_0012 belongs to. The
PI's questionnaire answer A1 describes this as scoring *"carboxylase-likeness"*;
his code does not. The code is right and A1's wording is wrong, so do not repeat
the carboxylase phrasing anywhere public.

**The scan does not discriminate.** Across all 998 nodes:

| metric | observed | what `zymctrl_score.py` says it means |
|---|---|---|
| `ppl` | 15.808 – 18.271 | "< 1.75 is decent, < 1.5 is good" |
| `llr` | −0.058 – +0.081 | "the number that actually discriminates EC membership" |

A log-likelihood ratio of essentially zero everywhere means the target EC label
explains these sequences no better than the decoys. A1 reads a trend out of the
perplexity column — more ancestral nodes scoring lower, interpreted as more
canonical and therefore broader substrate range — but the spread is 2.5
perplexity units at a level the script itself calls poor, and `ppl` alone is
documented in that same script as confounded by length and by how well populated
the EC class was in training. A1's own closing caveat says the rest: reconstructed
ancestors are consensus-like by construction, which can move perplexity with no
functional signal behind it.

**How the wiki states it.** `/model` Track 5 reports the method, the numbers and
the non-result, and claims nothing about promiscuity from them. Keep it that way
unless someone re-runs this with a positive control — a set of sequences known to
belong to the target EC, scored the same way, to show the metric can separate
anything at all on this data.

---
*Log — 2026-10-20: numbers extracted from the notebook's stored outputs while
writing `/model` Track 5. Recorded because A1's description and the code disagree,
and because the result is a negative one that is easy to misread as a trend.*
