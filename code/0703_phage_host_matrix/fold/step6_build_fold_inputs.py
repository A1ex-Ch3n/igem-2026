"""
Step 6 — build ColabFold inputs for the RBP × receptor fold.

RBPs  : dereplicate the candidate RBP sequences into families (mmseqs, 90% id) -> probes.
Recept: our overlapped receptor groups (hit a candidate host >=90%), filtered to genuine
        surface receptors (drop efflux/LptD) -> panel.
Pairs : cartesian product family × receptor -> ColabFold CSV (id="RBP__REC",
        sequence="rbpseq:recseq"), plus a 6-pair smoke set.

Outputs (code/output/0703_phage_host_matrix/fold/):
  probes.fasta, probe_map.tsv, receptors_panel.fasta, receptor_map.tsv,
  all_pairs.csv, smoke.csv

Run: python code/0703_phage_host_matrix/fold/step6_build_fold_inputs.py
"""

import csv
import os
import shutil
import subprocess
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUTREF = os.path.join(HERE, "..", "..", "output", "0703_phage_host_matrix")
FOLD = os.path.join(OUTREF, "fold")
RECEP_FAA_DIR = os.path.join(HERE, "..", "..", "0623_metagenome_rbp", "out_receptor_fasta")
TMP = os.path.join(os.environ.get("CLAUDE_JOB_DIR", "/tmp"), "tmp", "fold_build")
MMSEQS = shutil.which("mmseqs") or "/opt/homebrew/bin/mmseqs"
DROP_CATEGORIES = {"TolC/efflux-OM", "LptD"}   # efflux pumps / LPS machinery aren't phage receptors
RBP_CLUSTER_ID = "0.90"


def read_fasta(path):
    name, buf = None, []
    with open(path) as fh:
        for line in fh:
            if line.startswith(">"):
                if name:
                    yield name, "".join(buf)
                name, buf = line[1:].rstrip("\n"), []
            else:
                buf.append(line.strip())
    if name:
        yield name, "".join(buf)


def wrap(seq):
    return "\n".join(seq[i:i + 60] for i in range(0, len(seq), 60))


def build_rbp_families():
    """Return (families, id_map) — families: rbp_id -> rep_seq; map: rbp_id -> metadata."""
    os.makedirs(TMP, exist_ok=True)
    # protein_id -> (phage, host, type); protein_id -> seq
    meta = {}
    for row in csv.DictReader(open(os.path.join(OUTREF, "candidate_rbps_table.tsv")), delimiter="\t"):
        meta[row["protein_id"]] = (row["phage"], row["organism"], row["rbp_type"])
    pid_seq, seq_pids = {}, defaultdict(list)
    for name, seq in read_fasta(os.path.join(OUTREF, "candidate_rbps.faa")):
        pid = name.split("|")[0]
        pid_seq[pid] = seq
        seq_pids[seq].append(pid)
    # unique sequences -> one representative protein_id each
    uniq = os.path.join(TMP, "rbp_uniq.faa")
    with open(uniq, "w") as fh:
        for seq, pids in seq_pids.items():
            fh.write(f">{pids[0]}\n{wrap(seq)}\n")
    # cluster unique reps into families
    pref = os.path.join(TMP, "rbpclust")
    subprocess.run([MMSEQS, "easy-cluster", uniq, pref, os.path.join(TMP, "mm"),
                    "--min-seq-id", RBP_CLUSTER_ID, "-c", "0.8", "-v", "1"], check=True)
    clusters = defaultdict(list)
    for line in open(pref + "_cluster.tsv"):
        rep, member = line.rstrip("\n").split("\t")
        clusters[rep].append(member)
    families, id_map = {}, {}
    for i, (rep, members) in enumerate(sorted(clusters.items(), key=lambda kv: -len(kv[1])), 1):
        rid = f"RBP{i:04d}"
        families[rid] = pid_seq[rep]
        # all original protein_ids covered by this family (members are unique-seq reps)
        orig = [p for m in members for p in seq_pids[pid_seq[m]]]
        phages = sorted({meta.get(p, ("", "", ""))[0] for p in orig})
        hosts = sorted({meta.get(p, ("", "", ""))[1] for p in orig})
        types = sorted({meta.get(p, ("", "", ""))[2] for p in orig})
        id_map[rid] = {"rep_protein_id": rep, "n_members": len(orig), "len": len(pid_seq[rep]),
                       "phages": "; ".join(phages), "hosts": "; ".join(hosts),
                       "types": ",".join(types)}
    return families, id_map


def build_receptor_panel():
    # overlapped receptor groups = our reps hitting a candidate host >=90%
    cand = ("putida", "taiwanensis", "plecoglossicida", "lactis", "grimontii", "gessardii")
    cand_accs = {row["ncbi_accession"] for row in
                 csv.DictReader(open(os.path.join(OUTREF, "pharbp_pseudomonas_hosts.tsv")), delimiter="\t")
                 if row["ncbi_accession"] and any(k in row["cleaned_name"].lower() for k in cand)}
    rep_hit = set()
    for row in csv.DictReader(open(os.path.join(OUTREF, "host_receptor_overlap.tsv")), delimiter="\t"):
        if row["host_accession"] in cand_accs and float(row["pct_identity"]) >= 90:
            rep_hit.add(row["our_rep"])
    # locus -> (category, product, seq, strain) from the 5 receptor faa
    info = {}
    for faa in sorted(f for f in os.listdir(RECEP_FAA_DIR) if f.endswith("_receptors.faa")):
        for name, seq in read_fasta(os.path.join(RECEP_FAA_DIR, faa)):
            locus = name.split()[0]
            cat = name.split("category=", 1)[1].split()[0] if "category=" in name else "?"
            prod = name.split("product=", 1)[1].strip() if "product=" in name else ""
            strain = name.split("strain=", 1)[1].split()[0] if "strain=" in name else "?"
            info[locus] = (cat, prod, seq, strain)
    # which of our strains carry each rep group (from receptor_by_strain)
    rep_strains = {row["cluster_rep"]: [s for s in ("9-6-2", "9-2-1", "10-10-2", "8-5-2", "8-10-2")
                                        if row.get(s) == "1"]
                   for row in csv.DictReader(open(os.path.join(OUTREF, "receptor_by_strain.tsv")),
                                             delimiter="\t")}
    panel, rmap = {}, {}
    kept = 0
    for locus in sorted(rep_hit):
        if locus not in info:
            continue
        cat, prod, seq, strain = info[locus]
        if cat in DROP_CATEGORIES:
            continue
        kept += 1
        rec_id = f"REC{kept:03d}"
        panel[rec_id] = seq
        rmap[rec_id] = {"locus_tag": locus, "category": cat, "product": prod,
                        "our_strains": ",".join(rep_strains.get(locus, []))}
    return panel, rmap


def main():
    os.makedirs(FOLD, exist_ok=True)
    families, fmap = build_rbp_families()
    panel, rmap = build_receptor_panel()
    print(f"RBP families: {len(families)}  |  receptor panel: {len(panel)} "
          f"(dropped {', '.join(DROP_CATEGORIES)})")

    with open(os.path.join(FOLD, "probes.fasta"), "w") as fh:
        for rid, seq in families.items():
            fh.write(f">{rid}\n{wrap(seq)}\n")
    with open(os.path.join(FOLD, "probe_map.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rbp_id", "rep_protein_id", "n_members", "len", "types", "phages", "hosts"])
        for rid, m in fmap.items():
            w.writerow([rid, m["rep_protein_id"], m["n_members"], m["len"], m["types"],
                        m["phages"], m["hosts"]])
    with open(os.path.join(FOLD, "receptors_panel.fasta"), "w") as fh:
        for rid, seq in panel.items():
            fh.write(f">{rid}\n{wrap(seq)}\n")
    with open(os.path.join(FOLD, "receptor_map.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rec_id", "locus_tag", "category", "our_strains", "product"])
        for rid, m in rmap.items():
            w.writerow([rid, m["locus_tag"], m["category"], m["our_strains"], m["product"]])

    # pairs: cartesian product
    pairs = []
    for rid, rseq in families.items():
        for cid, cseq in panel.items():
            pairs.append((f"{rid}__{cid}", f"{rseq}:{cseq}"))
    with open(os.path.join(FOLD, "all_pairs.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "sequence"]); w.writerows(pairs)
    # smoke: 6 diverse pairs (first 3 families × first 2 receptors)
    fam_ids = list(families)[:3]
    rec_ids = list(panel)[:2]
    smoke = [(f"{r}__{c}", f"{families[r]}:{panel[c]}") for r in fam_ids for c in rec_ids]
    with open(os.path.join(FOLD, "smoke.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["id", "sequence"]); w.writerows(smoke[:6])

    print(f"pairs: {len(pairs)} ({len(families)} × {len(panel)}) -> all_pairs.csv | smoke.csv: 6")
    print("receptor panel by category:")
    bycat = defaultdict(int)
    for m in rmap.values():
        bycat[m["category"]] += 1
    for c, n in sorted(bycat.items(), key=lambda x: -x[1]):
        print(f"  {c:16} {n}")


if __name__ == "__main__":
    main()
