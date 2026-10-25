# CDS numbering map — our annotation onto the PI's

`map_cds.py` matches the two Pharokka annotations of the same 9-2-1 Φ8 assembly and
writes `code/output/1024_cds_numbering_map/cds_numbering_map.tsv`.

- ours: `data/phage_genome/9-2-1/assembly/pharokka_phage/pharokka.gbk` — `FHABPWTM_` tags
- the PI's: `code/0713_espinoza_structural_mapping/pharokka_espinoza/pharokka.gbk` — `UUAIURNK_` tags

Both call 80 CDS and 77 of them are identical at the protein level. The three that
differ are ORF-boundary disagreements, not different genes:

| ours | the PI's | relation |
|---|---|---|
| `CDS_0015` (547 aa) | `CDS_0011` res 1–530 | our call starts with his ORF and runs 17 aa past its end |
| `CDS_0016` (402 aa) | `CDS_0011` res 540–941 | our call is the C-terminal part of his ORF |
| `CDS_0026` (4193 aa) | `CDS_0001` + `CDS_0080` | his annotation splits this ORF across the two ends of his assembly |

So **our `CDS_0015` and `CDS_0016` are the two halves of the PI's single 941 aa tail
spike, `CDS_0011`**, which our Pharokka run split in two and his called whole. The
β-helix depolymerase identified in `documents/2026-07-13_why_protein_protein_binding_fails.qmd`
as `CDS_0016` is therefore **`CDS_0011` residues 540–941**, and it sits entirely inside
the fragment ordered from Twist (`CDS_0011` res 305–941).

The other cited protein, our `CDS_0002`, is a clean one-to-one match to `CDS_0024`
(650 aa) and is still annotated only as a hypothetical protein in both runs, so the
claim that the fold found a depolymerase the annotation had missed still holds.

`CDS_0026` is worth a second look on its own: an ORF that is whole in our assembly and
split between the first and last genes of the PI's is the signature of the two
assemblies being linearised at different points. That bears on the unresolved topology
question in `documents/2026-10-18_genome_topology_conflict.md` and is **not** settled here.

Run with the `igem2026` env: `python code/1024_cds_numbering_map/map_cds.py`
