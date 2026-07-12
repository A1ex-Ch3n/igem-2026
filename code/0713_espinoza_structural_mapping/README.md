# Prof. Cesar Espinoza — structural mapping of the 9-2-1 Φ8 virion (2026-07-13)

Provenance: **Prof. Cesar Espinoza's** Colab notebook (shared 2026-07-13), saved here as
`2026-07-13_espinoza_capsid_tube_foldseek.ipynb`. This is **his** work, kept distinct from our
Pharokka/RBP-Detect pipeline (`code/0712_phage_rbp_detect/`).

## What the notebook does / 教授在做什麼
He **structurally annotated the whole virion**, independently of Pharokka's sequence annotation:
AlphaFold-folded our phage proteins → **foldseek** matched them to a solved homologous podovirus,
**Ralstonia solanacearum phage GP4**, then colored the matching chains in the GP4 cryo-EM maps:

| GP4 PDB | what it is | GP4 components |
|---|---|---|
| **8H89** | GP4 head | major capsid gp2 (×540) + cement gp1 (×540), T=9 |
| **8JOV** | GP4 portal–tail complex | portal gp7, adaptors gp74/gp76/gp81/gp82 |
| **8JOU** | GP4 fibers | fiber-I / fiber-tail-adaptor gp77, gp80 |

(GP4 = a short-tailed podovirus with "three types of tail fibers" — our phage is also a podovirus,
so it is a good structural template.)

## What the professor is expressing / 教授想表達的重點
1. **He converges with our conclusion:** the RBP is a β-helix depolymerase → receptor is **LPS
   O-antigen (a sugar)** → protein–protein docking can't work. (He agreed in chat.)
2. **He has a whole-virion structural map** (portal / major head / structural-tube / fibers), which is
   more reliable than Pharokka's sequence guesses for the *structural* proteins.
3. **His RBP model is a sugar-enzyme cluster:** **CDS11 = the RBP**, flanked by **CDS10 & CDS12 =
   glycosidase ("glycolytic") enzymes**; the receptor-binding domain = **the C-terminal ~550 aa of
   GP11**. (These are *his* gene numbers — see numbering caveat below.)
4. **Open question he raised:** do the glycosidase domains (CDS10/12) also **recognize** (bind
   specifically) the sugar, or just **degrade / "chew away"** it non-specifically? → determines whether
   specificity/host-range lives in those domains.
5. His suggested next step (matches Alex's): foldseek known depolymerases on PDB, then look for the same
   fold in our metagenome / bacterial genomes.

## ⚠️ CDS numbering does NOT line up between us / 編號對不起來
His CDS numbers and our Pharokka `FHABPWTM_CDS_####` numbers are **not the same and not a fixed
offset** — almost certainly because of a **different genome origin/orientation or a different
gene-caller**. Examples:

| Protein (by function) | **Our** Pharokka CDS | **Prof's** label |
|---|---|---|
| Portal protein | CDS_0006 (742 aa) | "CDS_020" |
| Major head / capsid | CDS_0009 (368 aa) | "CDS_017" |
| Virion structural | CDS_0010 / 0013 / 0020 | "CDS_016" |
| (portal→head offset) | +3 (0006→0009) | −3 (020→017) |

→ the offset is not even the same sign, so **we cannot map his numbers to ours from the numbers
alone.** A reliable look-up needs sequences/coordinates (see below).

## Tentative look-up table (by FUNCTION, not sequence — treat as a hypothesis)
Our annotation is the backbone; prof's assignment overlaid where the function/GP4-component matches.

| Our CDS (Pharokka) | aa | Our function | Our structure finding (0712) | Prof's likely label / role | GP4 analog |
|---|---|---|---|---|---|
| CDS_0006 | 742 | portal protein | — | "CDS_020" portal | gp7 |
| CDS_0009 | 368 | major head protein | — | "CDS_017" major head | gp2 |
| CDS_0010 | 158 | virion structural | — | structural / "CDS_016"? | gp1/cement |
| CDS_0012 | 232 | structural protein | — | structural | adaptor? |
| CDS_0013 | 201 | virion structural | — | "CDS_013" structural | adaptor |
| CDS_0014 | 477 | hypothetical | α-rich | "CDS_014" structural | adaptor/tail |
| **CDS_0015** | 547 | **tail spike** | **β-helix depolymerase** | **RBP? ("CDS11", C-term ~550aa RBD)** | fiber |
| **CDS_0016** | 402 | **tail spike** | **β-helix depolymerase** | **glycosidase? ("CDS10/12")** | fiber |
| CDS_0017 | 917 | tail protein | α-rich (tail tube) | tail tube | tail |
| CDS_0018 | 118 | tail fiber | small β | fiber tip | fiber |
| **CDS_0002** | 650 | hypothetical | **β-helix depolymerase** | (a 3rd depolymerase?) | — |

**The one that matters most is unresolved:** is the prof's **CDS11 RBP** the same protein as our
**CDS_0015** (547 aa ≈ his "C-terminal 550 aa") or our **CDS_0016**? And are his glycosidases CDS10/12
the same as our CDS_0015/0016/0002 β-helices, or additional proteins? Numbers can't tell us.

## What we need from the professor to finalize / 需要教授提供什麼
1. **His protein FASTA** for the phage (the sequences he folded) — then we sequence-align to our
   `phanotate.faa` and the mapping becomes exact (this is the real answer).
2. **or his gene table / GFF** (CDS start–stop coordinates) — align by genome position.
3. **His foldseek output** (which PDB/depolymerase each CDS hit) — to compare with our fold analysis.
4. Clarify: did he re-call genes himself, and against which genome orientation (pre- or post-dnaapler reorientation)?

---
*Log — 2026-07-13: filed Prof. Espinoza's GP4-based structural-mapping notebook; his model
(RBP=CDS11 + glycosidase cluster CDS10/12, RBD=GP11 C-term 550aa) converges with our depolymerase→LPS
conclusion. CDS numbering between us does NOT align — reconciliation UNDONE pending his FASTA/GFF.*
