"""
Step 5: clean candidate-RBP table + a rough RBP x our-strain view.

"Candidate RBP" = any PharBP RBP whose host is a bacterium that shares >=1 of our receptors
at >=90% (the putida group + 3 marginal hosts). Source = PharBP (pulled in step4).

The RBP x strain relationship is HOST-level: an RBP relates to our strain S by how many
receptors its host shares with S (from Step 2/3). All RBPs of a host inherit that value,
so the heatmap shows host bands; the informative per-strain signal is that the 3 marginal
hosts share receptors only with 8-10-2 (capeferrum). RBP x specific receptor is the NEXT
step (fold on Laguna).

Outputs (code/output/0703_phage_host_matrix/):
  candidate_rbps_table.tsv      one row per RBP: phage, host, type, length, per-strain shared
  rbp_by_strain_heatmap.png     RBPs (grouped by host) x our 5 strains, colour = shared receptors
"""

import csv
import os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
STRAINS = ["9-6-2", "9-2-1", "10-10-2", "8-5-2", "8-10-2"]


def clean_parts(raw):
    for p in raw.replace(";", ",").split(","):
        p = " ".join(p.split()).strip()
        if p.lower().endswith(" and"):
            p = p[:-4].strip()
        if p.lower().startswith("pseudomonas"):
            yield p


def main():
    # shared[acc][strain] = # our receptors strain carries that hit this genome >=90%
    rep_strains = {}
    for row in csv.DictReader(open(os.path.join(OUT, "receptor_by_strain.tsv")), delimiter="\t"):
        rep_strains[row["cluster_rep"]] = {s for s in STRAINS if row.get(s) == "1"}
    rep_hits = defaultdict(set)
    for row in csv.DictReader(open(os.path.join(OUT, "host_receptor_overlap.tsv")), delimiter="\t"):
        if float(row["pct_identity"]) >= 90:
            rep_hits[row["our_rep"]].add(row["host_accession"])
    accs = {a for s in rep_hits.values() for a in s}
    shared = {a: {s: sum(1 for rep, ss in rep_strains.items() if s in ss and a in rep_hits.get(rep, ()))
                 for s in STRAINS} for a in accs}

    # cleaned host name -> accession + organism
    name_acc, acc_org = {}, {}
    for row in csv.DictReader(open(os.path.join(OUT, "pharbp_pseudomonas_hosts.tsv")), delimiter="\t"):
        if row["ncbi_accession"]:
            name_acc[row["cleaned_name"]] = row["ncbi_accession"]
            acc_org[row["ncbi_accession"]] = row["organism_name"] or row["cleaned_name"]

    def host_to_acc(raw):
        for p in clean_parts(raw):
            if p in name_acc:
                return name_acc[p]
        return ""

    # candidate RBPs
    rbps = list(csv.DictReader(open(os.path.join(OUT, "candidate_rbps_meta.tsv")), delimiter="\t"))
    seen_seq = set()
    for r in rbps:
        acc = host_to_acc(r["host"])
        r["accession"] = acc
        r["organism"] = acc_org.get(acc, "")
        ec = r["evidence_class"]
        r["rbp_type"] = ("TF+TSP" if ("TF" in ec and "TSP" in ec)
                         else "TSP" if "TSP" in ec else "TF" if "TF" in ec else "?")
        r["is_seq_rep"] = r["sequence_id"] not in seen_seq
        seen_seq.add(r["sequence_id"])
        for s in STRAINS:
            r[f"shared_{s}"] = shared.get(acc, {}).get(s, "")

    # ---- table ----
    cols = ["protein_id", "phage", "host", "accession", "organism", "rbp_type", "length",
            "is_seq_rep"] + [f"shared_{s}" for s in STRAINS]
    rbps.sort(key=lambda r: (-(r.get("shared_9-6-2") or 0) if isinstance(r.get("shared_9-6-2"), int)
                             else 0, r["host"], r["phage"]))
    with open(os.path.join(OUT, "candidate_rbps_table.tsv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rbps)

    # rows sorted so hosts form contiguous bands, most-shared host first
    order = sorted(rbps, key=lambda r: (-max((r[f"shared_{s}"] or 0) for s in STRAINS),
                                        r["organism"], r["phage"]))
    M = np.array([[(r[f"shared_{s}"] or 0) for s in STRAINS] for r in order], dtype=float)
    orgs = [r["organism"] or r["host"] for r in order]
    # host band boundaries + centred labels
    labels, bounds, prev, start = [], [], None, 0
    for i, o in enumerate(orgs + [None]):
        if o != prev and prev is not None:
            bounds.append(i)
            labels.append((prev, (start + i) / 2, i - start))
            start = i
        prev = o
    vmax = M.max()

    def sep_lines(ax, nrows):
        # clean white separators between every column, and between host bands
        for x in range(1, len(STRAINS)):
            ax.axvline(x - 0.5, color="white", lw=1.0)
        for b in bounds[:-1]:
            ax.axhline(b - 0.5, color="white", lw=1.4)
        for sp in ax.spines.values():
            sp.set_visible(True); sp.set_edgecolor("#cccccc")

    # ---- (1) SUMMARY: host-grouped bands, clean separators ----
    fig, ax = plt.subplots(figsize=(5.6, max(6, 0.022 * len(order))))
    im = ax.imshow(M, aspect="auto", cmap="Blues", vmin=0, vmax=vmax)
    ax.set_xticks(range(len(STRAINS))); ax.set_xticklabels(STRAINS, fontsize=9)
    ax.set_xlabel("our isolate", fontsize=9)
    ax.set_yticks([mid for _, mid, _ in labels])
    ax.set_yticklabels([f"{name}  ({n} RBP)" for name, _, n in labels], fontsize=7)
    sep_lines(ax, len(order))
    cbar = fig.colorbar(im, ax=ax, shrink=0.35)
    cbar.set_label("receptors shared ≥90% (host-level)", fontsize=8)
    ax.set_title(f"Candidate RBPs ({len(order)}) × our isolates — summary\n"
                 "colour = receptors that isolate shares with the RBP's host (≥90%)",
                 fontsize=9, pad=8)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, "rbp_by_strain_heatmap.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

    # ---- (2) DETAILED: one row per RBP, labelled by RBP id, clean cell borders ----
    n = len(order)
    fig, ax = plt.subplots(figsize=(6.0, max(8, 0.115 * n)))
    im = ax.imshow(M, aspect="auto", cmap="Blues", vmin=0, vmax=vmax)
    ax.set_xticks(range(len(STRAINS))); ax.set_xticklabels(STRAINS, fontsize=9)
    ax.set_xlabel("our isolate", fontsize=9)
    ax.set_yticks(range(n))
    ax.set_yticklabels([f"{r['protein_id'][:8]}  {r['phage'][:26]}  [{r['rbp_type']}]"
                        for r in order], fontsize=3.2)
    # thin border on every cell
    ax.set_xticks(np.arange(-0.5, len(STRAINS), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", lw=0.3)
    ax.tick_params(which="minor", length=0)
    for b in bounds[:-1]:
        ax.axhline(b - 0.5, color="#d33", lw=0.8)  # red host separators
    cbar = fig.colorbar(im, ax=ax, shrink=0.2)
    cbar.set_label("receptors shared ≥90%", fontsize=7)
    ax.set_title(f"Candidate RBPs (per RBP, n={n}) × our isolates — detailed\n"
                 "red lines separate hosts; label = protein_id | phage | type", fontsize=8, pad=8)
    plt.tight_layout()
    fig.savefig(os.path.join(OUT, "rbp_by_strain_detailed.png"), dpi=180, bbox_inches="tight")
    plt.close(fig)

    nseq = len(seen_seq)
    print(f"{len(rbps)} candidate RBPs | {nseq} unique sequences")
    print("per host:")
    byhost = defaultdict(int)
    for r in rbps:
        byhost[r["organism"] or r["host"]] += 1
    for h, n in sorted(byhost.items(), key=lambda x: -x[1]):
        print(f"  {h:36} {n} RBP")


if __name__ == "__main__":
    main()
