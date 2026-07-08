# PI group's assembly of 9-2-1 Φ8 — and how it relates to ours

`PI_Phage_Assembly_Version1.fa` — the PI/professor group's assembly of the same phage (`>Version_1`).
Filed here for the record and as the **canonical complete genome** (it retains the terminal repeat).

## The two assemblies are the SAME genome
Verified by direct sequence comparison (`../../../../code/0708_phage_assembly/compare_to_PI_assembly.py`):
- **100.00%** of our assembly's 31-mers are found in the PI assembly → identical genome, no SNPs on our side.

## They differ in three ways (all explained)
| | PI (`Version_1`) | Ours (SPAdes `NODE_13`) |
|---|---|---|
| Length | **62,416 bp** | **62,338 bp** (= 62,416 − 78) |
| Terminal repeat | **77 bp DTR present at BOTH ends** | **trimmed** — one copy removed |
| Orientation | reference strand | **reverse-complemented** |
| Start point | (its own) | **rotated** — our start = PI internal pos, minus strand |

- **The ~77 bp Direct Terminal Repeat (DTR):** the PI sequence has an exact 77 bp prefix==suffix:
  `GGCTGCGCTCGACCACGACGTTTTGCGGCTTACCGCCTTTGACCTTCGGCACGGGCAGTTTCTTGCCCTGGCTGGCC`.
  Our SPAdes assembly **collapsed/removed one copy** of it (that's the 78 bp length difference), so ours
  has the DTR only once (present internally at ours position 17703, as reverse-complement). `62,416 − 77
  = 62,339 ≈ our 62,338` (within 1 bp) → ours = the PI genome with one DTR copy removed.
- **RC + rotation:** ours is the reverse-complement of the PI sequence, started at a different point —
  which is why a naive head-vs-tail comparison looked completely different. It's the same molecule.

## What this means biologically
A **~77 bp DTR** is the signature of a **linear genome with Direct Terminal Repeats** (T7 /
Autographiviridae-style packaging) — consistent with the short-tailed podovirus morphology. Earlier
read-only guesses (circular vs linear) were unreliable; **the PI assembly settles it: there is a real
77 bp terminal repeat.** (Formal packaging class — DTR vs headful — can be confirmed with PhageTerm on
the full reads, but the DTR itself is now established.)

## Which genome to use as THE reference
- **Canonical / archival / submission:** the PI `Version_1` (62,416 bp, DTR at both ends, reference
  orientation) — this is the complete, standard representation.
- **Our annotation (pharokka, RBP analysis) is on OUR coordinates** (62,338 bp, RC + rotated, DTR
  trimmed) — biologically valid (same genes) but a different coordinate frame/orientation. To put the
  annotation on the PI canonical coordinates, **re-run pharokka on `PI_Phage_Assembly_Version1.fa`**
  (cheap) — recommended before any external submission so coordinates match the PI reference.

---
*Log: 2026-07-08 — PI assembly received and compared. Confirms the ~77 bp DTR our SPAdes assembly had
trimmed; same genome, RC + rotated. See [`../NOTES.md`](../NOTES.md).*
