"""Map our FHABPWTM_ phage CDS numbering onto the PI's UUAIURNK_ numbering.

Both files are Pharokka annotations of the same 9-2-1 Phi8 assembly. Most CDS are
byte-identical at the protein level, so they are matched on the translation; the
few that differ are places where one run split an ORF the other called whole, and
those are resolved by looking for each unmatched protein inside the other's.
"""
import csv
from pathlib import Path

from Bio import SeqIO

ROOT = Path(__file__).resolve().parents[2]
OURS = ROOT / "data/phage_genome/9-2-1/assembly/pharokka_phage/pharokka.gbk"
PROF = ROOT / "code/0713_espinoza_structural_mapping/pharokka_espinoza/pharokka.gbk"
OUT = ROOT / "code/output/1024_cds_numbering_map"


def load(path):
    out = []
    for rec in SeqIO.parse(path, "genbank"):
        for feat in rec.features:
            if feat.type != "CDS":
                continue
            out.append(
                {
                    "tag": feat.qualifiers["locus_tag"][0],
                    "start": int(feat.location.start) + 1,
                    "end": int(feat.location.end),
                    "aa": feat.qualifiers.get("translation", [""])[0],
                    "product": feat.qualifiers.get("product", [""])[0],
                }
            )
    return out


def contained_in(needle, haystack):
    """Return (tag, first_residue, last_residue) for an exact containment, else None."""
    for cds in haystack:
        idx = cds["aa"].find(needle["aa"])
        if idx >= 0 and len(needle["aa"]) < len(cds["aa"]):
            return cds["tag"], idx + 1, idx + len(needle["aa"])
    return None


def overlapping_prefix(needle, haystack, seed=30):
    """Resolve a CDS whose start agrees with one of the PI's ORFs but whose end does not."""
    for cds in haystack:
        idx = cds["aa"].find(needle["aa"][:seed])
        if idx < 0:
            continue
        shared = 0
        while (
            shared < len(needle["aa"])
            and idx + shared < len(cds["aa"])
            and needle["aa"][shared] == cds["aa"][idx + shared]
        ):
            shared += 1
        if shared >= seed:
            return cds["tag"], idx + 1, idx + shared, shared
    return None


def main():
    ours, prof = load(OURS), load(PROF)
    prof_by_aa = {c["aa"]: c for c in prof}

    rows = []
    for cds in ours:
        hit = prof_by_aa.get(cds["aa"])
        if hit:
            rows.append(
                {
                    "ours": cds["tag"],
                    "prof": hit["tag"],
                    "relation": "identical protein",
                    "prof_residues": f"1-{len(hit['aa'])}",
                    "aa_len": len(cds["aa"]),
                    "our_product": cds["product"],
                    "prof_product": hit["product"],
                }
            )
            continue
        part = contained_in(cds, prof)
        if part:
            tag, first, last = part
            rows.append(
                {
                    "ours": cds["tag"],
                    "prof": tag,
                    "relation": "our CDS is part of the PI's longer ORF",
                    "prof_residues": f"{first}-{last}",
                    "aa_len": len(cds["aa"]),
                    "our_product": cds["product"],
                    "prof_product": next(c["product"] for c in prof if c["tag"] == tag),
                }
            )
            continue
        partial = overlapping_prefix(cds, prof)
        if partial:
            tag, first, last, shared = partial
            rows.append(
                {
                    "ours": cds["tag"],
                    "prof": tag,
                    "relation": (
                        f"our CDS covers the PI's ORF from its start and runs "
                        f"{len(cds['aa']) - shared} aa past its end"
                    ),
                    "prof_residues": f"{first}-{last}",
                    "aa_len": len(cds["aa"]),
                    "our_product": cds["product"],
                    "prof_product": next(c["product"] for c in prof if c["tag"] == tag),
                }
            )
            continue
        pieces = [c for c in prof if c["aa"] and c["aa"] in cds["aa"]]
        rows.append(
            {
                "ours": cds["tag"],
                "prof": "+".join(c["tag"] for c in pieces),
                "relation": "the PI's annotation splits this ORF" if pieces else "unresolved",
                "prof_residues": "",
                "aa_len": len(cds["aa"]),
                "our_product": cds["product"],
                "prof_product": "; ".join(c["product"] for c in pieces),
            }
        )

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "cds_numbering_map.tsv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    identical = sum(r["relation"] == "identical protein" for r in rows)
    print(f"{len(ours)} CDS ours, {len(prof)} CDS the PI's; {identical} identical proteins")
    print("\nEverything that is not a one-to-one identity:")
    for row in rows:
        if row["relation"] != "identical protein":
            print(f"  {row['ours']} ({row['aa_len']} aa) -> {row['prof']} "
                  f"res {row['prof_residues'] or '-'} | {row['relation']}")
    print("\nThe two CDS cited in 2026-07-13_why_protein_protein_binding_fails:")
    for row in rows:
        if row["ours"].endswith(("CDS_0002", "CDS_0016")):
            print(f"  {row['ours']} -> {row['prof']} res {row['prof_residues']} "
                  f"({row['prof_product']})")


if __name__ == "__main__":
    main()
