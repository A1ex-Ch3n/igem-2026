#!/usr/bin/env python3
"""
Stage 2a — turn the pairs manifest + sequences into ColabFold inputs.

ColabFold complex format: a CSV with columns `id,sequence`, where sequence joins the
two chains with ':'. The `id` becomes the job name (and output filename prefix), so we
encode the pair into it:  id = "<strain>__<phage_id>__<receptor_id>".

Tier-1 = monomer RBP × monomer receptor  ->  sequence = "<RBP>:<RECEPTOR>".

Outputs (under binding_screen/colabfold_input/):
  <strain>.csv     all pairs for that strain (id,sequence)
  all_pairs.csv    every pair (for a single big array)
  smoke.csv        a tiny subset (N pairs) for the end-to-end smoke test
"""
import csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest/pairs_36x60.csv"
PROBES = ROOT / "phage_probes/probes.fasta"
OUTDIR = ROOT / "colabfold_input"
SMOKE_N = 6  # pairs in the smoke test

def read_fasta(path):
    d, name, seq = {}, None, []
    for line in open(path):
        if line.startswith(">"):
            if name: d[name] = "".join(seq)
            name = line[1:].split()[0]; seq = []
        else:
            seq.append(line.strip())
    if name: d[name] = "".join(seq)
    return d

def main():
    OUTDIR.mkdir(exist_ok=True)
    probe_seq = read_fasta(PROBES)
    rec_seq = {}
    for strain in ("10-10-2", "9-2-1", "9-6-2"):
        for locus, s in read_fasta(ROOT / f"receptors_panel/{strain}_receptors.fasta").items():
            rec_seq[(strain, locus)] = s

    rows_by_strain, all_rows = {}, []
    missing = 0
    for r in csv.DictReader(open(MANIFEST)):
        strain, ph, rec = r["strain"], r["phage_id"], r["receptor_id"]
        if ph not in probe_seq or (strain, rec) not in rec_seq:
            missing += 1; continue
        jid = f"{strain}__{ph}__{rec}"
        seq = f"{probe_seq[ph]}:{rec_seq[(strain, rec)]}"
        rows_by_strain.setdefault(strain, []).append((jid, seq))
        all_rows.append((jid, seq))

    def write_csv(path, rows):
        with open(path, "w", newline="") as fh:
            w = csv.writer(fh); w.writerow(["id", "sequence"]); w.writerows(rows)

    for strain, rows in rows_by_strain.items():
        write_csv(OUTDIR / f"{strain}.csv", rows)
        print(f"  {strain}: {len(rows)} pairs -> colabfold_input/{strain}.csv")
    write_csv(OUTDIR / "all_pairs.csv", all_rows)
    # smoke: 2 pairs from each strain
    smoke = []
    for strain, rows in rows_by_strain.items():
        smoke.extend(rows[:2])
    write_csv(OUTDIR / "smoke.csv", smoke[:SMOKE_N])
    print(f"  all_pairs.csv: {len(all_rows)} pairs | smoke.csv: {len(smoke[:SMOKE_N])} pairs")
    if missing:
        print(f"  WARNING: {missing} manifest rows had no matching sequence (skipped)")

if __name__ == "__main__":
    main()
