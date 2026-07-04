# Our receptors — presence across PharBP host strains

For each of our **144** receptor groups: which of the **54 PharBP host name strings** carry a homolog. Tiers: >=90% (essentially same receptor), >=70% (close), >=50% (homolog).

> **Counts are at the 54 host-*strain* level, not the 43 distinct genomes.** Several PharBP names share one genome (e.g. 8 aeruginosa names -> PAO1), so a receptor in that genome is counted once per name. This inflates aeruginosa's >=50 counts; negligible for the P. putida group (~1 name : 1 genome).

- receptors present in >=1 host at **>=90%**: **76/144**
- receptors present in >=1 host at **>=50%**: **131/144**
- receptors found in **no** PharBP host (even >=50%) — potentially our-specific: **13** (porin=7, other-OM=4, usher=1, pilin=1)

## Most widely shared receptors (top 15 by # host strains >=90%)

| our_rep | category | host strains >=90% | max_id | best host |
|---|---|---|---|---|
| NEEDOG_04082 | other-OM | 7 | 98.7 | Pseudomonas putida |
| BPBBIK_04940 | TolC/efflux-OM | 6 | 98.1 | Pseudomonas putida KT2440 |
| BPBBIK_01078 | OmpA | 6 | 97.7 | Pseudomonas putida |
| BPBBIK_04393 | porin | 6 | 97.6 | Pseudomonas putida KT2440 |
| BPBBIK_04429 | TolC/efflux-OM | 6 | 97.5 | Pseudomonas putida KT2440 |
| BPBBIK_00770 | other-OM | 6 | 97.5 | Pseudomonas putida |
| BPBBIK_00985 | porin | 6 | 97.5 | Pseudomonas putida |
| BPBBIK_00251 | porin | 6 | 97.4 | Pseudomonas putida KT2440 |
| BPBBIK_02459 | porin | 6 | 97.1 | Pseudomonas putida KT2440 |
| BPBBIK_04368 | porin | 6 | 96.1 | Pseudomonas putida |
| BPBBIK_02609 | TolC/efflux-OM | 6 | 95.9 | Pseudomonas putida |
| BPBBIK_04430 | porin | 6 | 95.6 | Pseudomonas putida |
| BPBBIK_01607 | Tsx | 6 | 95.4 | Pseudomonas putida S12 |
| BPBBIK_00881 | TBDR | 6 | 95.3 | Pseudomonas putida |
| NEEDOG_00167 | TolC/efflux-OM | 6 | 95.2 | Pseudomonas putida S12 |

Full table: `receptor_host_presence.tsv` (with the host-strain lists).
