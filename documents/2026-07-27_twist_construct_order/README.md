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

## Open question for the PI

`CDS10_WT_NOTAG` was ordered on the basis that CDS_0010 is a glycosidase, but our
template analysis does not support that — the body has one weak IspD hit and
~460 aa with no template at all. One of the three sponsored constructs is
therefore a bet. Worth asking him for his evidence before the protein work
starts.

---
*Log — 2026-07-29: filed. Moved here from a loose `new mails/` directory at the
repo root and renamed to the `YYYY-MM-DD_slug` convention. Construct contents
verified by translating each plasmid; the filename/sequence mismatch and the
resolved cut site are recorded above.*
