"""
Track A — pull all Pseudomonas-host RBPs recorded in PharBP (pharbp.ugent.be).

PharBP records RBP -> phage -> host bacterium (no receptor field). This exports the
subset whose host genus is Pseudomonas: the catalogued phage-RBP / host "pairs" most
relevant to our Pseudomonas isolates, with structures + evidence.

Uses the unauthenticated CSV export endpoint:
  GET /export/results/?host_genus=Pseudomonas&unique=1&download=csv
CSV columns: Protein ID, Protein Name, Type, Evidence Class(es), Evidence Type(s),
Evidence Probability(ies), Source, Source ID, Phage Name, Host Name(s), CDS ID

Writes the raw CSV + a summary.md (counts by host, evidence class, phage).

Usage:
  python pull_pseudomonas_rbps.py --out-dir ../output/0701_pharbp_query [--genus Pseudomonas]
"""

import argparse
import csv
import io
import os
from collections import Counter

import requests

BASE = "https://pharbp.ugent.be"

# named relatives closest to our hosts (P. putida group / Pseudomonas_E), for flagging
PUTIDA_GROUP = ("putida", "capeferrum", "protegens", "fluorescens", "monteilii", "mosselii",
                "plecoglossicida", "entomophila", "asplenii")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--genus", default="Pseudomonas")
    ap.add_argument("--unique", default="1", help="1 = one representative per identical sequence")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)

    url = f"{BASE}/export/results/"
    params = {"host_genus": args.genus, "unique": args.unique, "download": "csv"}
    print(f"GET {url} {params}")
    r = requests.get(url, params=params, timeout=180,
                     headers={"User-Agent": "iGEM6317-pharbp-client/1.0"})
    r.raise_for_status()
    csv_path = os.path.join(args.out_dir, f"{args.genus.lower()}_rbps.csv")
    with open(csv_path, "w") as fh:
        fh.write(r.text)

    rows = list(csv.DictReader(io.StringIO(r.text)))
    print(f"{len(rows)} RBP records written to {csv_path}")

    hosts = Counter(row["Host Name(s)"] for row in rows)
    phages = Counter(row["Phage Name"] for row in rows)
    classes = Counter(c.strip() for row in rows for c in row["Evidence Class(es)"].split(","))
    putida = [row for row in rows if any(k in row["Host Name(s)"].lower() for k in PUTIDA_GROUP)]

    md = os.path.join(args.out_dir, f"{args.genus.lower()}_rbps_summary.md")
    with open(md, "w") as fh:
        fh.write(f"# PharBP RBPs with host genus = {args.genus}\n\n")
        fh.write(f"Source: {url}?host_genus={args.genus}&unique={args.unique}&download=csv\n\n")
        fh.write(f"- **{len(rows)}** unique RBP records\n")
        fh.write(f"- **{len(phages)}** distinct phages\n")
        fh.write(f"- **{len(hosts)}** distinct host strains\n")
        fh.write(f"- class breakdown: " + ", ".join(f"{k}={v}" for k, v in classes.most_common()) + "\n")
        fh.write(f"- **{len(putida)}** records with a P. putida-group / non-aeruginosa host "
                 f"(closest to our isolates)\n\n")
        fh.write("## Records per host strain\n\n| host | n |\n|---|---|\n")
        for h, n in hosts.most_common():
            fh.write(f"| {h} | {n} |\n")
        fh.write("\n## P. putida-group host records (closest to our Pseudomonas_E isolates)\n\n")
        fh.write("| Protein ID | Phage | Host | Class |\n|---|---|---|---|\n")
        for row in putida:
            fh.write(f"| {row['Protein ID'][:12]}… | {row['Phage Name']} | "
                     f"{row['Host Name(s)']} | {row['Evidence Class(es)']} |\n")

    print(f"Summary -> {md}")
    print(f"  {len(rows)} RBPs | {len(phages)} phages | {len(hosts)} hosts | "
          f"{len(putida)} putida-group")


if __name__ == "__main__":
    main()
