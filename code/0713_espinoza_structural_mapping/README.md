# Prof. Cesar Espinoza — structural mapping of the 9-2-1 Φ8 virion (2026-07-13)

Provenance — **Prof. Cesar Espinoza's** work (shared 2026-07-13), kept distinct from our
`code/0712_phage_rbp_detect/` pipeline:

- `2026-07-13_espinoza_capsid_tube_foldseek.ipynb` — his Colab notebook (AlphaFold + foldseek → GP4)
- `pharokka_espinoza/` — **his** Pharokka run of the same genome (locus prefix `UUAIURNK_`; ours is `FHABPWTM_`)
- `cds_lookup.tsv` — sequence-verified prof↔our CDS map (80 rows; generated here)

## What the notebook does
He **structurally annotated the whole virion** (independent of Pharokka's sequence guesses):
AlphaFold-folded our phage proteins → **foldseek** matched them to a solved homologous podovirus,
**Ralstonia solanacearum phage GP4**, then colored matching chains in GP4 cryo-EM maps:

| GP4 PDB | what it is | GP4 components |
|---|---|---|
| **8H89** | GP4 head | major capsid gp2 + cement gp1, T=9 |
| **8JOV** | GP4 portal–tail complex | portal gp7, adaptors gp74/76/81/82 |
| **8JOU** | GP4 fibers | fiber-I / fiber-tail-adaptor gp77, gp80 |

## What the professor is expressing
1. **Converges with our conclusion:** RBP is a β-helix depolymerase → receptor is **LPS O-antigen (sugar)**
   → protein–protein docking can't work.
2. **A whole-virion structural map** (portal / major head / tube / fibers) — more reliable than Pharokka
   for structural proteins.
3. **RBP model = a sugar-enzyme cluster:** **CDS11 = RBP**, flanked by **CDS10 & CDS12 = glycosidase
   ("glycolytic") enzymes**; receptor-binding domain = **C-terminal ~550 aa of GP11**. (His numbers — reconciled below.)
4. **Open question:** do the glycosidases (CDS10/12) also **recognize** the sugar, or just **degrade** it?

## ✅ Numbering RECONCILED (sequence-verified)
His `UUAIURNK_` and our `FHABPWTM_` Pharokka runs are the **same phage** but the **genome is
reverse-oriented**, so the CDS numbering runs opposite. **77 / 80 CDS are byte-identical in sequence**
(just renumbered); in the tail region the map is `prof + our = 27` (before the tail spike) then `= 26`
(after). Only **3 CDS differ**, both from how the two runs split ORFs, not from any biological difference:

| type | prof | our | note |
|---|---|---|---|
| **tail spike split** | **CDS_0011** (941 aa, one ORF) | **CDS_0015 + CDS_0016** (547 + 402 aa, two ORFs) | our run split the tail spike into two; his kept it whole |
| genome-origin split | CDS_0001 + CDS_0080 | CDS_0026 (4193 aa) | circular-genome origin cut differently |

Full 80-row map: `cds_lookup.tsv`.

### His RBP cluster → our CDS (the important part)
| Prof (his model) | = Our CDS | Our 0712 fold finding | agree? |
|---|---|---|---|
| **CDS_0011 — RBP** | **CDS_0015 + CDS_0016** | both **β-helix depolymerase** (pLDDT 93 / 65) | ✅ **yes** |
| CDS_0010 — "glycosidase" | **CDS_0017** (tail protein, 917 aa) | we called it **α-rich / tail tube**, not β-helix | ⚠️ **needs check** |
| CDS_0012 — "glycosidase" | **CDS_0014** (hypothetical, 477 aa) | **α-rich**, not β-helix | ⚠️ **needs check** |
| (his "GP11 last 550 aa" = RBD) | ≈ our **CDS_0016** + C-term of 0015 | the C-terminal depolymerase/RBD | ✅ consistent |

Also note: our **CDS_0002** (a 3rd β-helix depolymerase, RBP-Detect-only) = **his CDS_0024** — a
separate depolymerase **outside** his tail cluster.

## The one thing to reconcile now
Numbering is solved — the remaining question is **biological**: his **CDS10/12 = our CDS_0017/CDS_0014**,
which he calls **glycosidases** but our simple H-bond-period test flagged as **α-rich (not β-helix)**.
That is not a contradiction (many glycoside hydrolases are α/β or TIM-barrel, not β-helix), but it needs
his evidence. **What to ask him for:** his **foldseek hit tables** (which PDB / glycoside-hydrolase family
each CDS matched) — that settles whether CDS_0017/0014 are truly sugar-active enzymes.

---
*Log — 2026-07-13: filed Prof. Espinoza's GP4 structural-mapping notebook + his Pharokka run. Numbering
reconciled by sequence (genome reversed; 77/80 identical; tail spike = his 1 ORF vs our 2). His RBP
CDS_0011 = our CDS_0015+0016 (β-helix depolymerase — we agree). His glycosidase calls (CDS10/12 = our
CDS_0017/0014) vs our α-rich reading: pending his foldseek output. UNDONE: get his foldseek tables.*
