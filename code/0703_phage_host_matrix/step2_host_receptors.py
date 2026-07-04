"""
Step 2 of the phage-host receptor matrix: download the Step-1 host genomes, mine their
receptor repertoires, and compute the receptor overlap vs our isolates' receptors.

For the 43 distinct NCBI assemblies resolved in Step 1, download proteomes (datasets CLI),
function-filter to receptor proteins (reusing 0623 receptor_fasta.classify), then mmseqs-
search OUR 144 receptor-cluster reps against each host's receptors. Output the host x
our-receptor identity matrix + a per-host overlap summary (which hosts share our receptors,
at what identity) joined with PharBP RBP/phage counts.

Reuses: code/0623_metagenome_rbp/receptor_fasta.py `classify()`, and the download/filter/
search pattern from receptor_ncbi_search.py. Local, no GPU.

Run: python code/0703_phage_host_matrix/step2_host_receptors.py
"""

import csv
import glob
import importlib.util
import json
import os
import shutil
import subprocess
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
HOSTS_TSV = os.path.join(OUT_DIR, "pharbp_pseudomonas_hosts.tsv")
RECEPTOR_BY_STRAIN = os.path.join(OUT_DIR, "receptor_by_strain.tsv")
OUR_FAA_DIR = os.path.join(HERE, "..", "0623_metagenome_rbp", "out_receptor_fasta")
RF_PATH = os.path.join(HERE, "..", "0623_metagenome_rbp", "receptor_fasta.py")

WORK = os.path.join(os.environ.get("CLAUDE_JOB_DIR", "/tmp"), "tmp", "host_genomes")
DATASETS = shutil.which("datasets") or "/opt/anaconda3/bin/datasets"
MMSEQS = shutil.which("mmseqs") or "/opt/homebrew/bin/mmseqs"
TARGET_MINL, TARGET_MAXL = 80, 2000  # same length gate as 0623


def sh(cmd, **kw):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **kw)


def load_classifier():
    spec = importlib.util.spec_from_file_location("rf", RF_PATH)
    rf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rf)
    return rf


def read_fasta(path):
    name, buf = None, []
    with open(path) as fh:
        for line in fh:
            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(buf)
                name, buf = line[1:].rstrip("\n"), []
            else:
                buf.append(line.strip())
    if name is not None:
        yield name, "".join(buf)


def download_hosts(accs):
    os.makedirs(WORK, exist_ok=True)
    data = os.path.join(WORK, "ncbi_dataset", "data")
    have = {a for a in accs if os.path.exists(os.path.join(data, a, "protein.faa"))}
    missing = [a for a in accs if a not in have]
    if missing:
        print(f"downloading {len(missing)} genome proteomes via datasets...")
        zf = os.path.join(WORK, "hosts.zip")
        sh([DATASETS, "download", "genome", "accession", *missing,
            "--include", "protein", "--filename", zf])
        sh(["unzip", "-q", "-o", zf, "-d", WORK])
    faas = {}
    for a in accs:
        p = os.path.join(data, a, "protein.faa")
        if os.path.exists(p):
            faas[a] = p
    print(f"proteomes available: {len(faas)}/{len(accs)}")
    return faas


def mine_host_receptors(faas, rf):
    """Write host_receptors.faa (>acc|pid) + return per-acc {category: count}."""
    out_faa = os.path.join(WORK, "host_receptors.faa")
    counts = defaultdict(Counter)
    with open(out_faa, "w") as out:
        for acc, path in faas.items():
            for name, seq in read_fasta(path):
                if not (TARGET_MINL <= len(seq) <= TARGET_MAXL):
                    continue
                toks = name.split(None, 1)
                pid, desc = toks[0], (toks[1] if len(toks) > 1 else "")
                is_rec, cat = rf.classify(desc, set())
                if is_rec:
                    out.write(f">{acc}|{pid}\n")
                    for i in range(0, len(seq), 60):
                        out.write(seq[i:i + 60] + "\n")
                    counts[acc][cat] += 1
    print(f"host receptors mined: {sum(sum(c.values()) for c in counts.values())} "
          f"across {len(counts)} genomes")
    return out_faa, counts


def build_our_query():
    """our_receptor_reps.faa from the 144 receptor_by_strain cluster reps; return rep->category."""
    seqs = {}
    for faa in glob.glob(os.path.join(OUR_FAA_DIR, "*_receptors.faa")):
        for name, s in read_fasta(faa):
            seqs[name.split()[0]] = s
    rep_cat = {}
    with open(RECEPTOR_BY_STRAIN) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rep_cat[row["cluster_rep"]] = row["category"]
    q = os.path.join(WORK, "our_receptor_reps.faa")
    with open(q, "w") as out:
        for rep in rep_cat:
            if rep in seqs:
                out.write(f">{rep}\n")
                for i in range(0, len(seqs[rep]), 60):
                    out.write(seqs[rep][i:i + 60] + "\n")
    print(f"our query reps: {len(rep_cat)} ({sum(1 for r in rep_cat if r in seqs)} with seq)")
    return q, rep_cat


def search(query, target):
    m8 = os.path.join(WORK, "hits.m8")
    sh([MMSEQS, "easy-search", query, target, m8, os.path.join(WORK, "mmtmp"),
        "--format-output", "query,target,fident,pident,alnlen,qcov,tcov,evalue,bits",
        "-s", "5.7", "--max-seqs", "1000", "-v", "1"])
    return m8


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    rf = load_classifier()

    # host accession -> representative organism + list of host strings (from Step 1)
    acc_org = {}
    host_rows = []
    with open(HOSTS_TSV) as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            host_rows.append(row)
            acc = row["ncbi_accession"]
            if acc and acc not in acc_org:
                acc_org[acc] = row["organism_name"] or row["cleaned_name"]
    accs = sorted(acc_org)
    print(f"{len(host_rows)} host strings -> {len(accs)} distinct genomes")

    faas = download_hosts(accs)
    host_faa, counts = mine_host_receptors(faas, rf)
    query, rep_cat = build_our_query()
    m8 = search(query, host_faa)

    # best pident per (our_rep, acc)
    best = defaultdict(dict)  # rep -> acc -> (pid, qcov)
    for line in open(m8):
        f = line.rstrip("\n").split("\t")
        rep, target = f[0], f[1]
        pid, qcov = round(float(f[2]) * 100, 1), round(float(f[5]) * 100, 1)
        acc = target.split("|")[0]
        if acc not in best[rep] or pid > best[rep][acc][0]:
            best[rep][acc] = (pid, qcov)

    reps = list(rep_cat)
    accs_present = [a for a in accs if a in faas]

    # --- main matrix: our receptor (row) x host genome (col) = best pident ---
    with open(os.path.join(OUT_DIR, "host_overlap_matrix.tsv"), "w") as out:
        out.write("our_rep\tcategory\t" + "\t".join(acc_org[a] for a in accs_present) + "\n")
        for rep in reps:
            cells = "\t".join(str(best[rep].get(a, ("",))[0]) for a in accs_present)
            out.write(f"{rep}\t{rep_cat[rep]}\t{cells}\n")

    # --- long form ---
    with open(os.path.join(OUT_DIR, "host_receptor_overlap.tsv"), "w") as out:
        out.write("our_rep\tcategory\thost_accession\thost_organism\tpct_identity\tquery_cov\n")
        for rep in reps:
            for a in accs_present:
                if a in best[rep]:
                    pid, qcov = best[rep][a]
                    out.write(f"{rep}\t{rep_cat[rep]}\t{a}\t{acc_org[a]}\t{pid}\t{qcov}\n")

    # --- per-accession overlap stats ---
    acc_stats = {}
    for a in accs_present:
        pids = [best[rep][a][0] for rep in reps if a in best[rep]]
        acc_stats[a] = {
            "n_ge50": sum(1 for p in pids if p >= 50),
            "n_ge90": sum(1 for p in pids if p >= 90),
            "max_id": max(pids) if pids else 0,
            "mean_id": round(sum(pids) / len(pids), 1) if pids else 0,
            "n_receptors": sum(counts[a].values()),
        }

    # --- per-host summary (expand back to the 54 host strings) + PharBP counts ---
    PUTIDA = ("putida", "capeferrum", "protegens", "fluorescens", "monteilii", "mosselii",
              "plecoglossicida", "entomophila", "asplenii", "taiwanensis", "alloputida",
              "hunanensis", "fortuita", "chlororaphis")
    summ = []
    for row in host_rows:
        a = row["ncbi_accession"]
        st = acc_stats.get(a)
        if not st:
            continue
        summ.append({
            "host": row["cleaned_name"], "accession": a, "organism": acc_org.get(a, ""),
            "n_ge90": st["n_ge90"], "n_ge50": st["n_ge50"], "max_id": st["max_id"],
            "mean_id": st["mean_id"], "host_n_receptors": st["n_receptors"],
            "n_pharbp_rbp": row["n_pharbp_rbp"], "n_phages": row["n_phages"],
            "near": any(k in row["cleaned_name"].lower() for k in PUTIDA),
        })
    summ.sort(key=lambda x: (-x["n_ge90"], -x["max_id"]))

    scols = ["host", "accession", "organism", "n_ge90", "n_ge50", "max_id", "mean_id",
             "host_n_receptors", "n_pharbp_rbp", "n_phages"]
    with open(os.path.join(OUT_DIR, "host_overlap_summary.tsv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=scols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(summ)

    with open(os.path.join(OUT_DIR, "host_receptor_counts.tsv"), "w") as fh:
        cats = sorted({c for a in counts for c in counts[a]})
        fh.write("accession\torganism\ttotal\t" + "\t".join(cats) + "\n")
        for a in accs_present:
            fh.write(f"{a}\t{acc_org[a]}\t{sum(counts[a].values())}\t"
                     + "\t".join(str(counts[a].get(c, 0)) for c in cats) + "\n")

    # --- markdown summary ---
    with open(os.path.join(OUT_DIR, "host_overlap_summary.md"), "w") as fh:
        fh.write("# Host x our-receptor overlap (Step 2)\n\n")
        fh.write(f"Our **{len(reps)}** receptor-cluster reps vs receptors mined from "
                 f"**{len(accs_present)}** PharBP host genomes (mmseqs). Cell = best % identity.\n\n")
        fh.write("Overlap = shared receptor family (presence + homology) — a **clue** to host "
                 "range, not proof (phages read variable surface loops).\n\n")
        fh.write("## Hosts ranked by receptors shared with us (>=90% identity)\n\n")
        fh.write("| host | organism | shared>=90 | shared>=50 | max_id | PharBP RBP | phages | near-rel |\n")
        fh.write("|---|---|---|---|---|---|---|---|\n")
        for s in summ[:30]:
            fh.write(f"| {s['host']} | {s['organism']} | {s['n_ge90']} | {s['n_ge50']} | "
                     f"{s['max_id']} | {s['n_pharbp_rbp']} | {s['n_phages']} | "
                     f"{'★' if s['near'] else ''} |\n")
        fh.write("\nFull matrix: `host_overlap_matrix.tsv` · long form: `host_receptor_overlap.tsv` "
                 "· host repertoires: `host_receptor_counts.tsv`.\n")

    print(f"\nmatrix: {len(reps)} receptors x {len(accs_present)} genomes")
    print("top hosts by shared>=90:")
    for s in summ[:8]:
        print(f"  {s['host']:38} shared>=90={s['n_ge90']:3} max_id={s['max_id']:5} "
              f"phages={s['n_phages']}")


if __name__ == "__main__":
    main()
