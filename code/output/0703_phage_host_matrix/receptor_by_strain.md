# Receptor repertoire of our 5 sequenced isolates

Reference table for the phage–host receptor matrix. 441 receptor proteins clustered (mmseqs, 90% id / 80% cov) into **144 receptor groups** across 5 isolates.

Isolates: **9-6-2 / 9-2-1 / 10-10-2 / 8-5-2** are *Pseudomonas_E* sp013179515 (the first three are ~identical strain); **8-10-2** is *P. capeferrum*.

- receptor groups present in **all 5** isolates (core): **43**
- groups found **only in 8-10-2** (capeferrum-specific): **46**

## Receptor count per strain, by class

| class | 9-6-2 | 9-2-1 | 10-10-2 | 8-5-2 | 8-10-2 |
|---|---|---|---|---|---|
| porin | 29 | 29 | 26 | 26 | 28 |
| TBDR | 23 | 23 | 22 | 22 | 22 |
| TolC/efflux-OM | 12 | 12 | 13 | 13 | 14 |
| other-OM | 9 | 9 | 9 | 9 | 12 |
| OmpA | 5 | 5 | 6 | 6 | 6 |
| usher | 3 | 3 | 3 | 3 | 1 |
| Tsx | 2 | 2 | 2 | 2 | 1 |
| FadL | 2 | 2 | 1 | 1 | 2 |
| Omp-porin | 1 | 1 | 1 | 1 | 2 |
| LptD | 1 | 1 | 1 | 1 | 1 |
| flagellin | 1 | 1 | 1 | 1 | 1 |
| pilin | 1 | 1 | 1 | 1 | 1 |
| **total** | **89** | **89** | **86** | **86** | **91** |

## Notes
- Full presence matrix (one row per receptor group): `receptor_by_strain.tsv`.
- The 4 sp013179515 isolates share nearly the same repertoire; 8-10-2 (capeferrum) is the genuinely distinct reference.
- Clustering at 90% id groups orthologs; lower identity paralogs stay separate.
