"""
Reshape the Step-2 overlap into a table indexed by OUR receptors: for each of our ~144
receptor groups, which PharBP host strains carry a homolog (and at what identity).

Answers "each of our receptors is found on which PharBP host strains, in total".
Expands the per-genome overlap back to the PharBP host STRAINS (many strings share a genome).

Inputs (code/output/0703_phage_host_matrix/):
  host_receptor_overlap.tsv     our_rep, category, host_accession, host_organism, pct_identity, ...
  pharbp_pseudomonas_hosts.tsv  cleaned_name (host strain) -> ncbi_accession
  receptor_by_strain.tsv        our_rep -> which of our 5 isolates carry it
Output:
  receptor_host_presence.tsv    one row per our receptor; host-strain lists per identity tier
  receptor_host_presence.md     patterns (widely shared vs our-unique)

Thresholds: >=90% = essentially the same receptor; >=70% = same family, close; >=50% = homolog.
"""

import csv
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
OUR_STRAINS = ["9-6-2", "9-2-1", "10-10-2", "8-5-2", "8-10-2"]


def main():
    # genome accession -> list of PharBP host strains sharing it
    acc_hosts = defaultdict(list)
    with open(os.path.join(OUT, "pharbp_pseudomonas_hosts.tsv")) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["ncbi_accession"]:
                acc_hosts[row["ncbi_accession"]].append(row["cleaned_name"])

    # our receptor -> which of our isolates carry it (+ category)
    rep_meta = {}
    for row in csv.DictReader(open(os.path.join(OUT, "receptor_by_strain.tsv")), delimiter="\t"):
        ours = [s for s in OUR_STRAINS if row.get(s) == "1"]
        rep_meta[row["cluster_rep"]] = (row["category"], ours)

    # our receptor -> {host_strain: pct_identity} (best via the strain's genome)
    rep_hosts = defaultdict(dict)
    for row in csv.DictReader(open(os.path.join(OUT, "host_receptor_overlap.tsv")), delimiter="\t"):
        rep = row["our_rep"]
        pid = float(row["pct_identity"])
        for host in acc_hosts.get(row["host_accession"], []):
            if host not in rep_hosts[rep] or pid > rep_hosts[rep][host]:
                rep_hosts[rep][host] = pid

    def tier(pairs, lo, hi=101):
        return sorted((h for h, p in pairs.items() if lo <= p < hi), key=lambda h: -pairs[h])

    rows = []
    for rep, (cat, ours) in rep_meta.items():
        hp = rep_hosts.get(rep, {})
        ge90 = [h for h, p in hp.items() if p >= 90]
        ge70 = [h for h, p in hp.items() if p >= 70]
        ge50 = [h for h, p in hp.items() if p >= 50]
        best_host, max_id = ("", 0.0)
        if hp:
            best_host = max(hp, key=hp.get)
            max_id = hp[best_host]
        rows.append({
            "our_rep": rep, "category": cat, "n_our_isolates": len(ours),
            "our_isolates": ",".join(ours),
            "n_hoststrains_ge90": len(ge90), "n_hoststrains_ge70": len(ge70),
            "n_hoststrains_ge50": len(ge50), "max_identity": round(max_id, 1),
            "best_host": best_host,
            "hoststrains_ge90": "; ".join(sorted(ge90, key=lambda h: -hp[h])),
        })

    rows.sort(key=lambda r: (-r["n_hoststrains_ge90"], -r["max_identity"]))
    cols = ["our_rep", "category", "n_our_isolates", "our_isolates", "n_hoststrains_ge90",
            "n_hoststrains_ge70", "n_hoststrains_ge50", "max_identity", "best_host",
            "hoststrains_ge90"]
    with open(os.path.join(OUT, "receptor_host_presence.tsv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    # patterns
    n = len(rows)
    in_any90 = sum(1 for r in rows if r["n_hoststrains_ge90"])
    in_any50 = sum(1 for r in rows if r["n_hoststrains_ge50"])
    our_unique = [r for r in rows if r["n_hoststrains_ge50"] == 0]
    from collections import Counter
    uniq_cat = Counter(r["category"] for r in our_unique)

    with open(os.path.join(OUT, "receptor_host_presence.md"), "w") as fh:
        fh.write("# Our receptors — presence across PharBP host strains\n\n")
        fh.write(f"For each of our **{n}** receptor groups: which of the 54 PharBP Pseudomonas "
                 f"host strains carry a homolog. Tiers: >=90% (essentially same receptor), "
                 f">=70% (close), >=50% (homolog).\n\n")
        fh.write(f"- receptors present in >=1 host at **>=90%**: **{in_any90}/{n}**\n")
        fh.write(f"- receptors present in >=1 host at **>=50%**: **{in_any50}/{n}**\n")
        fh.write(f"- receptors found in **no** PharBP host (even >=50%) — potentially "
                 f"our-specific: **{len(our_unique)}** "
                 f"({', '.join(f'{k}={v}' for k, v in uniq_cat.most_common())})\n\n")
        fh.write("## Most widely shared receptors (top 15 by # host strains >=90%)\n\n")
        fh.write("| our_rep | category | host strains >=90% | max_id | best host |\n")
        fh.write("|---|---|---|---|---|\n")
        for r in rows[:15]:
            fh.write(f"| {r['our_rep']} | {r['category']} | {r['n_hoststrains_ge90']} | "
                     f"{r['max_identity']} | {r['best_host']} |\n")
        fh.write("\nFull table: `receptor_host_presence.tsv` (with the host-strain lists).\n")

    print(f"{n} receptors | {in_any90} in >=1 host @>=90% | {in_any50} @>=50% | "
          f"{len(our_unique)} our-specific")
    print("top shared receptors:")
    for r in rows[:6]:
        print(f"  {r['our_rep']:14} {r['category']:12} @>=90% on {r['n_hoststrains_ge90']:2} hosts "
              f"(max {r['max_identity']}) e.g. {r['best_host']}")


if __name__ == "__main__":
    main()
