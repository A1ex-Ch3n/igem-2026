"""
Foundation table for the phage–host receptor matrix task.

Builds a receptor x strain PRESENCE table for our 5 sequenced isolates: cluster the
441 receptor proteins (from 0623 out_receptor_fasta) across strains, so each row is
one receptor (an ortholog group) and each column is a strain, marking whether that
strain carries it. Also writes a Markdown summary of each strain's receptor repertoire.

Why re-cluster: the existing 0623 reps only covered 3 of the 5 strains. We redo it
across all 5 here so the reference is complete and its provenance is clear.

Clustering: mmseqs easy-cluster at 90% identity / 80% coverage (ortholog-level).

Inputs : ../0623_metagenome_rbp/out_receptor_fasta/<strain>_receptors.faa  (headers:
         >LOCUS strain=<s> category=<class> product=<...>)
Outputs: output/0703_phage_host_matrix/receptor_by_strain.tsv
         output/0703_phage_host_matrix/receptor_by_strain.md
Usage  : python build_receptor_by_strain.py
"""

import glob
import os
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
FAA_DIR = os.path.join(HERE, "..", "0623_metagenome_rbp", "out_receptor_fasta")
OUT_DIR = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
TMP = os.environ.get("CLAUDE_JOB_DIR", "/tmp")
TMP = os.path.join(TMP, "tmp") if os.path.isdir(os.path.join(TMP, "tmp")) else "/tmp"

# 4 isolates are Pseudomonas_E sp013179515 (9-6-2/9-2-1/10-10-2 ~identical strain,
# plus 8-5-2); 8-10-2 is P. capeferrum. Ordered to show the group vs the outlier.
STRAINS = ["9-6-2", "9-2-1", "10-10-2", "8-5-2", "8-10-2"]


def parse_headers():
    """locus_tag -> (strain, category, product); also write a combined fasta."""
    meta = {}
    combined = os.path.join(OUT_DIR, "_all_receptors.faa")
    with open(combined, "w") as out:
        for faa in sorted(glob.glob(os.path.join(FAA_DIR, "*_receptors.faa"))):
            with open(faa) as fh:
                keep = False
                for line in fh:
                    if line.startswith(">"):
                        h = line[1:].strip()
                        locus = h.split()[0]
                        # strain= and category= are single tokens; product= runs to EOL
                        strain = cat = "?"
                        prod = ""
                        if "strain=" in h:
                            strain = h.split("strain=", 1)[1].split()[0]
                        if "category=" in h:
                            cat = h.split("category=", 1)[1].split()[0]
                        if "product=" in h:
                            prod = h.split("product=", 1)[1].strip()
                        meta[locus] = (strain, cat, prod)
                        out.write(f">{locus}\n")
                        keep = True
                    elif keep:
                        out.write(line)
    return combined, meta


def cluster(combined):
    """Run mmseqs easy-cluster, return rep -> [members]."""
    prefix = os.path.join(OUT_DIR, "clust")
    cmd = ["mmseqs", "easy-cluster", combined, prefix, os.path.join(TMP, "mmseqs_recep"),
           "--min-seq-id", "0.9", "-c", "0.8", "--cov-mode", "0", "-v", "1"]
    subprocess.run(cmd, check=True)
    clusters = defaultdict(list)
    with open(prefix + "_cluster.tsv") as fh:
        for line in fh:
            rep, member = line.rstrip("\n").split("\t")
            clusters[rep].append(member)
    return clusters


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    combined, meta = parse_headers()
    print(f"parsed {len(meta)} receptors across {len({m[0] for m in meta.values()})} strains")
    clusters = cluster(combined)
    print(f"{len(clusters)} receptor clusters")

    rows = []
    for rep, members in clusters.items():
        strains_present = {meta[m][0] for m in members}
        # representative category/product = the rep's (fall back to any member)
        cat = meta[rep][1]
        prod = meta[rep][2] or next((meta[m][2] for m in members if meta[m][2]), "")
        rows.append((rep, cat, prod, strains_present, len(members)))

    # sort: most widespread first, then category
    rows.sort(key=lambda r: (-len(r[3]), r[1]))

    tsv = os.path.join(OUT_DIR, "receptor_by_strain.tsv")
    with open(tsv, "w") as fh:
        fh.write("cluster_rep\tcategory\tn_strains\t" + "\t".join(STRAINS) + "\tproduct\n")
        for rep, cat, prod, present, _ in rows:
            cells = "\t".join("1" if s in present else "0" for s in STRAINS)
            fh.write(f"{rep}\t{cat}\t{len(present)}\t{cells}\t{prod}\n")
    print(f"wrote {tsv}")

    # ---- markdown summary ----
    per_strain_cat = {s: defaultdict(int) for s in STRAINS}
    for locus, (s, cat, _) in meta.items():
        per_strain_cat[s][cat] += 1
    cats = sorted({c for d in per_strain_cat.values() for c in d}, key=lambda c: -sum(
        per_strain_cat[s][c] for s in STRAINS))
    core = sum(1 for r in rows if len(r[3]) == 5)
    capeferrum_only = sum(1 for r in rows if r[3] == {"8-10-2"})

    md = os.path.join(OUT_DIR, "receptor_by_strain.md")
    with open(md, "w") as fh:
        fh.write("# Receptor repertoire of our 5 sequenced isolates\n\n")
        fh.write(f"Reference table for the phage–host receptor matrix. {len(meta)} receptor "
                 f"proteins clustered (mmseqs, 90% id / 80% cov) into **{len(rows)} receptor "
                 f"groups** across 5 isolates.\n\n")
        fh.write("Isolates: **9-6-2 / 9-2-1 / 10-10-2 / 8-5-2** are *Pseudomonas_E* sp013179515 "
                 "(the first three are ~identical strain); **8-10-2** is *P. capeferrum*.\n\n")
        fh.write(f"- receptor groups present in **all 5** isolates (core): **{core}**\n")
        fh.write(f"- groups found **only in 8-10-2** (capeferrum-specific): **{capeferrum_only}**\n\n")
        fh.write("## Receptor count per strain, by class\n\n")
        fh.write("| class | " + " | ".join(STRAINS) + " |\n")
        fh.write("|---|" + "---|" * len(STRAINS) + "\n")
        for c in cats:
            fh.write(f"| {c} | " + " | ".join(str(per_strain_cat[s][c]) for s in STRAINS) + " |\n")
        fh.write("| **total** | " + " | ".join(
            f"**{sum(per_strain_cat[s].values())}**" for s in STRAINS) + " |\n\n")
        fh.write("## Notes\n")
        fh.write("- Full presence matrix (one row per receptor group): `receptor_by_strain.tsv`.\n")
        fh.write("- The 4 sp013179515 isolates share nearly the same repertoire; 8-10-2 "
                 "(capeferrum) is the genuinely distinct reference.\n")
        fh.write("- Clustering at 90% id groups orthologs; lower identity paralogs stay separate.\n")
    print(f"wrote {md}")


if __name__ == "__main__":
    main()
