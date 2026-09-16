# 2026-09-10 — Twist construct order, second set (CDS_0012 ancestral variants)

Three reconstructed-ancestor variants of CDS_0012, all in **pET-28a(+)** with the
same NdeI/XhoI architecture as the first set
([`../2026-07-27_twist_construct_order/`](../2026-07-27_twist_construct_order/)).

> **The 2026-09-10 in the folder name is the date this was filed, not the order
> date.** Only Twist's design sheet was on hand; no order email accompanied it.
> Correct the date if the order correspondence turns up.

## Contents

| File | What |
|---|---|
| `constructs/iGEM-design_Second_Set.csv` | Twist's design/order sheet — insert + full construct sequence for all three |

No `.gb` files were supplied for this set; the CSV's `Construct sequence` column
is the only sequence source.

## What is in the three plasmids

| Name | Insert | Construct | Complexity | Codon optimised |
|---|---|---|---|---|
| `CDS12_ANC_Node1` | 1086 bp | 6378 bp | Low | No |
| `CDS12_ANC_Node40` | 1086 bp | 6378 bp | Low | No |
| `CDS12_ANC_Node281` | 1086 bp | 6378 bp | Low | No |

Identical architecture to `CDS12_WT_NOTAG` from the first set — same 1086 bp
insert length, same 6378 bp construct. All four therefore express a **382 aa**
protein and are **indistinguishable by SDS-PAGE**; see
[`../../code/0910_construct_protein_mw.ipynb`](../../code/0910_construct_protein_mw.ipynb).

Like the first set, all three inherit pET-28a's `MGSSHHHHHHSSGLVPRGSHM` leader,
so they are **N-terminally His6-tagged** despite carrying no tag in their name.
The insert ends in its own stop codon, so the vector's C-terminal His6 is never
translated.

⚠️ `Codon Optimized: No` — and the inserts use mammalian-like codon bias
(`CCC`/`GGG`/`GCC`-heavy), not *E. coli*. This is the first thing to suspect if a
band is missing from an expression gel.

---
*Log — 2026-09-10: filed. `iGEM-design_second_set.csv` moved here from a loose file
at the repo root and renamed to match the first set's `iGEM-design_First_Set.csv`.
Construct contents verified by translating the CSV's `Construct sequence` column;
protein masses computed in `code/0910_construct_protein_mw.ipynb`. Order date
unknown — see the note above.*
