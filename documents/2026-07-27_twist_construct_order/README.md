# 2026-07-27 — Prof. Espinoza's construct order to Twist

The first three plasmids of the project, ordered under the iGEM sponsorship.
Filed here as received; nothing in `constructs/` has been edited.

## Contents

| File | What |
|---|---|
| `2026-07-24_twist_sponsorship_enquiry.pdf` | the PI asks Twist whether the constructs can ship as frozen glycerol stocks; Twist (Xueer Jiang) replies 07-25 that they can, as a paid add-on not covered by the sponsorship |
| `2026-07-27_twist_order_email.pdf` | the actual order, sent 2026-07-27 09:11 — rush order + glycerol stocks, three constructs attached |
| `constructs/*.gb` | the three plasmids as sent, all in **pET-28a(+)** |
| `constructs/iGEM-design_First_Set.csv` | Twist's design/order sheet |

Numbering throughout is the PI's canonical `UUAIURNK_` index — see
[`../../code/0713_espinoza_structural_mapping/cds_lookup.tsv`](../../code/0713_espinoza_structural_mapping/cds_lookup.tsv).

## What is actually in the three plasmids

Each `.gb` was translated from the vector's T7 start to verify what will be
expressed. The result does **not** match the filenames:

| File | Actual insert | Actual tag |
|---|---|---|
| `CDS11_WT_CTERM_HIS6TAG.gb` | CDS_0011 **res 305–941** | **N-terminal**, two His6 — **no C-terminal His6** |
| `CDS10_WT_NOTAG.gb` | CDS_0010 res 105–917 | N-terminal His6 (**not** untagged) |
| `CDS12_WT_NOTAG.gb` | CDS_0012 res 117–477 | N-terminal His6 (**not** untagged) |

All three inherit pET-28a's `MGSSHHHHHHSSGLVPRGSHM` leader, which is why the two
"NOTAG" constructs are in fact tagged. CDS_0011 additionally carries a designed
`GGSGGGGS`–His6–`ENLYFQ` (TEV) cassette at its N-terminus, and its insert **ends
in its own stop codon**, so the vector's C-terminal His6 downstream is never
translated.

⚠️ **The filenames are wrong, not the sequences.** Residues 305–941 is
essentially the "clean self-contained β-helix body" option from
[`../../code/0716_espinoza_fiber_construct/`](../../code/0716_espinoza_fiber_construct/),
and an N-terminal tag is what that analysis recommended — res 921–941 is a
trimerization foldon that should be left intact. So the biology is right; only
the naming is misleading. **Do not design downstream experiments (e.g. a
C-terminal-tag detection step) from the filenames.**

This also **closes the 0716 open question** about where to cut CDS_0011: the PI's
two earlier statements disagreed by 280 residues ("bases" vs residues, and 111 vs
391). He went with 305.

### Accurate descriptive names (for our records)

The `.gb` files **keep their as-sent filenames** for provenance (that is what was
ordered from Twist). These are aliases for internal use:

| As-sent filename | Accurate name |
|---|---|
| `CDS11_WT_CTERM_HIS6TAG.gb` | `CDS11_305-941_NTERM_His6` |
| `CDS10_WT_NOTAG.gb` | `CDS10_105-917_NTERM_His6` |
| `CDS12_WT_NOTAG.gb` | `CDS12_117-477_NTERM_His6` |

The PI **confirmed on 2026-07-29** that all three use N-terminal tags and that he
wants **no C-terminal tag on any construct** — so the sequences are right and only
the filenames mislead.

## CDS_0010 — resolved (2026-07-29)

`CDS10_WT_NOTAG` was ordered on the basis that CDS_0010 is a glycosidase, but our
template analysis did not support that — the body has one weak IspD hit and
~460 aa with no template at all. **On 2026-07-29 the PI withdrew the glycosidase
call:** he confirmed he does not know what CDS_0010 is and is expressing it for
functional characterization. It is now an **unknown protein**. Expressing the
construct is still worthwhile — it may let us characterize the protein — but no
glycosidase function should be assumed downstream.

## Expressed protein masses

Computed from sequence in [`../../code/0910_construct_protein_mw.ipynb`](../../code/0910_construct_protein_mw.ipynb):
**CDS10 91.63 kDa** (834 aa), **CDS11 72.02 kDa** (688 aa), **CDS12 41.84 kDa** (382 aa),
each including the 21 aa vector leader. The three ancestral CDS_0012 variants of the
second set ([`../2026-09-10_twist_construct_order_second_set/`](../2026-09-10_twist_construct_order_second_set/))
are all within 0.43 kDa of CDS12_WT and **cannot be separated from it by SDS-PAGE**.

---
*Log — 2026-07-29: filed. Moved here from a loose `new mails/` directory at the
repo root and renamed to the `YYYY-MM-DD_slug` convention. Construct contents
verified by translating each plasmid; the filename/sequence mismatch and the
resolved cut site are recorded above.*
*Log — 2026-07-30: after the 2026-07-29 PI conversation (`../2026-07-29_pi_conversation/`).
C1 — the PI withdrew the CDS_0010 glycosidase call; "Open question for the PI"
rewritten as "CDS_0010 — resolved". C2 — the PI confirmed all-N-terminal / no
C-terminal tag; `.gb` filenames kept as-sent for provenance, accurate-name aliases
added, and the no-C-terminal-tag-detection note above reaffirmed.*
*Log — 2026-09-10: added the expressed-mass section; an independent re-translation in
`code/0910_construct_protein_mw.ipynb` reproduced the residue ranges and the N-terminal-tag
finding recorded above. A second Twist order was filed at
`../2026-09-10_twist_construct_order_second_set/`.*
