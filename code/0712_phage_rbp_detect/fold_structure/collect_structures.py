"""
Collect ColabFold structure-prediction results for the 9-2-1 Phi8 union RBPs.

Run AFTER folding on Laguna. Point --results at the ColabFold output dir
(the one holding `*_scores_rank_001_*.json` + `*_relaxed/unrelaxed_rank_001_*.pdb`).
Writes a per-structure summary TSV: mean pLDDT (fold confidence), pTM, and a
coarse N->C per-fifth pLDDT profile (a conserved high-pLDDT N-terminal stalk
with a lower/variable C-terminal block is the tail-spike RBD signature).

  python collect_structures.py --results /path/to/results/structures \
      --out code/output/0712_phage_rbp_detect/structure/structure_summary.tsv
"""

import argparse
import glob
import json
import os
import statistics


def per_fifth(plddt):
    n = len(plddt)
    if n == 0:
        return ["NA"] * 5
    step = n / 5.0
    out = []
    for i in range(5):
        a, b = int(round(i * step)), int(round((i + 1) * step))
        seg = plddt[a:b] if b > a else plddt[a:a + 1]
        out.append(f"{statistics.mean(seg):.1f}" if seg else "NA")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, help="ColabFold output dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    rows = []
    for jf in sorted(glob.glob(os.path.join(args.results, "*_scores_rank_001_*.json"))):
        with open(jf) as fh:
            d = json.load(fh)
        # id = filename up to "_scores_rank"
        base = os.path.basename(jf)
        name = base.split("_scores_rank")[0]
        plddt = d.get("plddt", [])
        mean_plddt = statistics.mean(plddt) if plddt else float("nan")
        ptm = d.get("ptm", "NA")
        iptm = d.get("iptm", "NA")  # present for multimer (trimer) jobs
        rows.append([name, len(plddt), f"{mean_plddt:.1f}", ptm, iptm, *per_fifth(plddt)])

    with open(args.out, "w") as fh:
        fh.write("structure\tn_res\tmean_plddt\tptm\tiptm\t"
                 "plddt_1\tplddt_2\tplddt_3\tplddt_4\tplddt_5\n")
        for r in sorted(rows, key=lambda x: x[0]):
            fh.write("\t".join(str(x) for x in r) + "\n")

    print(f"Wrote {args.out} ({len(rows)} structures)")
    for r in sorted(rows, key=lambda x: x[0]):
        print(f"  {r[0]:34s} n={r[1]:>4} plddt={r[2]} ptm={r[3]} iptm={r[4]}")


if __name__ == "__main__":
    main()
