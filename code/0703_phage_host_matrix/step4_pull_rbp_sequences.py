"""
Step 4a of the RBP x receptor layer: pull the candidate RBP sequences from PharBP.

Candidates = RBPs whose host is a P. putida-group bacterium that shares receptors with us
at >=90% (putida / KT2440 / S12 / NBRC / taiwanensis / plecoglossicida). These are the
phage RBPs worth folding against our receptors.

PharBP has no bulk-sequence export, so we pull per protein via the JSON API:
  export(host=Pseudomonas) -> filter to candidate hosts -> protein_hex_id
  GET /api/protein/<hex>/structure/  -> sequences[0].sequence_id (+ phage/host)
  GET /api/sequence/<sequence_id>/basic/ -> amino-acid sequence
Writes candidate_rbps.faa (>protein_hex|phage|host|class) + candidate_rbps_meta.tsv.
Resumable: skips proteins already in the meta TSV.

Run: python code/0703_phage_host_matrix/step4_pull_rbp_sequences.py
"""

import csv
import io
import os
import time

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
BASE = "https://pharbp.ugent.be"
# hosts that share >=1 of our receptors at >=90% (from shared_receptors_by_strain):
# the substantive putida group + 3 marginal hosts (1 shared receptor, with 8-10-2 only).
CAND_KEYS = ("putida", "taiwanensis", "plecoglossicida", "lactis", "grimontii", "gessardii")
S = requests.Session()
S.headers["User-Agent"] = "iGEM6317-pharbp-client/1.0"


def get_json(url):
    try:
        r = S.get(url, timeout=45)
        if r.status_code == 200:
            return r.json()
    except (requests.RequestException, ValueError):
        pass
    return None


def main():
    os.makedirs(OUT, exist_ok=True)
    print("fetching candidate RBP records (host=Pseudomonas -> putida group)...")
    r = S.get(f"{BASE}/export/results/", params={"host": "Pseudomonas", "download": "csv"}, timeout=180)
    r.raise_for_status()
    rows = list(csv.reader(io.StringIO(r.text)))[1:]
    cand = []
    for row in rows:
        if len(row) > 9 and row[9].lower().startswith("pseudomonas") \
                and any(k in row[9].lower() for k in CAND_KEYS):
            cand.append({"protein_id": row[0], "evidence_class": row[3],
                         "phage": row[8], "host": row[9]})
    print(f"{len(cand)} candidate RBP records")

    meta_path = os.path.join(OUT, "candidate_rbps_meta.tsv")
    faa_path = os.path.join(OUT, "candidate_rbps.faa")
    done = set()
    if os.path.exists(meta_path):
        for row in csv.DictReader(open(meta_path), delimiter="\t"):
            done.add(row["protein_id"])
        print(f"resuming: {len(done)} already pulled")

    seq_cache = {}
    new = not os.path.exists(meta_path) or os.path.getsize(meta_path) == 0
    mfh = open(meta_path, "a", newline="")
    mw = csv.writer(mfh, delimiter="\t")
    if new:
        mw.writerow(["protein_id", "sequence_id", "length", "phage", "host", "evidence_class"])
    ffh = open(faa_path, "a")

    pulled = 0
    for i, c in enumerate(cand):
        if c["protein_id"] in done:
            continue
        prot = get_json(f"{BASE}/api/protein/{c['protein_id']}/structure/")
        time.sleep(0.15)
        if not prot or not prot.get("sequences"):
            continue
        seqid = prot["sequences"][0].get("sequence_id")
        if not seqid:
            continue
        if seqid not in seq_cache:
            sb = get_json(f"{BASE}/api/sequence/{seqid}/basic/")
            time.sleep(0.15)
            seq_cache[seqid] = (sb or {}).get("sequence", "")
        seq = seq_cache[seqid]
        if not seq:
            continue
        mw.writerow([c["protein_id"], seqid, len(seq), c["phage"], c["host"], c["evidence_class"]])
        ffh.write(f">{c['protein_id']}|{c['phage']}|{c['host']}|{c['evidence_class']}\n")
        for j in range(0, len(seq), 60):
            ffh.write(seq[j:j + 60] + "\n")
        mfh.flush(); ffh.flush()
        pulled += 1
        if pulled % 40 == 0:
            print(f"  pulled {pulled} ({len(seq_cache)} unique sequences)...", flush=True)

    mfh.close(); ffh.close()
    print(f"done. pulled {pulled} RBPs | {len(seq_cache)} unique sequences -> {faa_path}")


if __name__ == "__main__":
    main()
