"""
Collect ColabFold ipTM for the 9-2-1 Φ8 binding screen + controls (local, no GPU).

Adapts code/0703_phage_host_matrix/fold/collect_results.py: walk a results dir
for each job's top-ranked score JSON (`*_scores_rank_001_*.json`), read ipTM /
pTM / max_pae, decode id (`<rbp>__<rec>`).

Two modes:
  screen  : write binding_matrix.csv (all pairs, sorted by ipTM desc)
  control : join a control_key.csv (id,class) and print/write the positive-vs-
            negative separation — the go/no-go gate for trusting the screen.

Usage:
  python collect_binding.py screen  <results_dir> [out.csv]
  python collect_binding.py control <results_dir> control_key.csv [out.csv]
"""

import csv
import json
import statistics
import sys
from pathlib import Path


def parse_results(results):
    rows = {}
    for f in sorted(Path(results).rglob("*_scores_rank_001_*.json")):
        parts = f.name.split("_scores_rank")[0].split("__")
        if len(parts) != 2:
            continue
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if d.get("iptm") is None:
            continue
        rows[(parts[0], parts[1])] = (d.get("iptm"), d.get("ptm"), d.get("max_pae"))
    return rows


def screen(results, out):
    rows = parse_results(results)
    ranked = sorted(rows.items(), key=lambda kv: kv[1][0], reverse=True)
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rbp_id", "rec_id", "iptm", "ptm", "max_pae"])
        for (rbp, rec), (iptm, ptm, pae) in ranked:
            w.writerow([rbp, rec, iptm, ptm, pae])
    print(f"parsed {len(rows)} pairs -> {out}")
    print("top 10 by ipTM:")
    for (rbp, rec), (iptm, *_ ) in ranked[:10]:
        print(f"  {rbp:10s} × {rec:14s} ipTM={iptm:.3f}")


def control(results, key_csv, out):
    rows = parse_results(results)
    cls = {}
    with open(key_csv) as fh:
        for r in csv.DictReader(fh):
            cls[tuple(r["id"].split("__"))] = r["class"]
    by = {}
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rbp_id", "rec_id", "class", "iptm", "ptm", "max_pae"])
        for k, (iptm, ptm, pae) in sorted(rows.items(), key=lambda kv: kv[1][0], reverse=True):
            c = cls.get(k, "unknown")
            by.setdefault(c, []).append(iptm)
            w.writerow([k[0], k[1], c, iptm, ptm, pae])
    print(f"parsed {len(rows)} control folds -> {out}")
    for c in ("positive", "scrambled", "mismatch", "unknown"):
        v = by.get(c, [])
        if v:
            print(f"  {c:10s} n={len(v)} ipTM mean={statistics.mean(v):.3f} "
                  f"min={min(v):.3f} max={max(v):.3f}")
    pos, neg = by.get("positive", []), by.get("scrambled", []) + by.get("mismatch", [])
    if pos and neg:
        gap = min(pos) - max(neg)
        verdict = ("SEPARATE — screen ipTM is trustworthy; use min(positive) as threshold"
                   if gap > 0 else
                   "OVERLAP — screen ipTM does NOT separate binders from non-binders; "
                   "treat the matrix as non-informative (as with the earlier MSA-free run)")
        print(f"\n  min(positive)={min(pos):.3f}  max(negative)={max(neg):.3f}  "
              f"gap={gap:+.3f}\n  VERDICT: {verdict}")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    mode = sys.argv[1]
    if mode == "screen":
        screen(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "binding_matrix.csv")
    elif mode == "control":
        control(sys.argv[2], sys.argv[3],
                sys.argv[4] if len(sys.argv) > 4 else "control_scores.csv")
    else:
        sys.exit("mode must be 'screen' or 'control'")


if __name__ == "__main__":
    main()
