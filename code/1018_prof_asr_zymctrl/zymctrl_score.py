#!/usr/bin/env python
"""
Score protein sequences against a target EC number with ZymCTRL.

Two numbers per sequence:
  ppl        - perplexity under the target EC. Lower = the sequence looks more
               like what ZymCTRL would write for that label. <1.75 is decent,
               <1.5 is good (per the model card).
  llr        - log-likelihood ratio: mean NLL under the best decoy EC minus
               mean NLL under the target EC. POSITIVE and large = the target
               label explains the sequence better than the alternatives.
               This is the number that actually discriminates EC membership;
               ppl alone is confounded by length and by how well-populated
               the EC class was in training.

Usage:
    python zymctrl_score.py --fasta candidates.fasta --ec 3.5.5.1
    python zymctrl_score.py --fasta candidates.fasta --ec 3.5.5.1 \
        --decoys 1.1.1.1 2.7.1.1 3.1.1.3 4.2.1.1 5.3.1.1 6.1.1.1

Requires: torch, transformers. GPU strongly recommended but CPU works.
"""

import argparse
import math

import torch
from transformers import AutoTokenizer, GPT2LMHeadModel

MODEL_ID = "AI4PD/ZymCTRL"
MAX_LEN = 1024
VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")

# A spread of one decoy per top-level EC class. Swap these for ECs that are
# actually plausible confusions for your target - a decoy panel drawn from the
# same class (e.g. other 3.5.x.x hydrolases) is a much harder, more meaningful
# test than one drawn from across the whole tree.
DEFAULT_DECOYS = ["1.1.1.1", "2.7.1.1", "3.1.1.3", "4.2.1.1", "5.3.1.1", "6.1.1.1"]


def read_fasta(path):
    """Yield (header, sequence) pairs."""
    name, buf = None, []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(buf)
                name, buf = line[1:].split()[0], []
            else:
                buf.append(line)
    if name is not None:
        yield name, "".join(buf)


def clean(seq):
    """Uppercase and drop anything that isn't a canonical residue."""
    return "".join(c for c in seq.upper() if c in VALID_AA)


@torch.no_grad()
def mean_nll(model, tokenizer, ec, seq, device):
    """
    Mean negative log-likelihood per residue token, conditioned on the EC tag.

    The EC control tokens are masked out of the loss so that the score reflects
    only how well the label explains the RESIDUES. Without this mask you are
    partly scoring the label's own prior frequency, which makes numbers
    incomparable across different ECs.
    """
    prompt = f"{ec}<sep><start>"
    full = f"{prompt}{seq}<end><|endoftext|>"

    ids = tokenizer(full, return_tensors="pt").input_ids.to(device)
    if ids.shape[1] > MAX_LEN:
        return None  # too long for the model's context; see note below

    n_prompt = len(tokenizer(prompt).input_ids)
    labels = ids.clone()
    labels[:, :n_prompt] = -100  # ignore the control tag in the loss

    return model(ids, labels=labels).loss.item()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fasta", required=True, help="candidate sequences")
    ap.add_argument("--ec", required=True, help="target EC, e.g. 3.5.5.1")
    ap.add_argument("--decoys", nargs="*", default=DEFAULT_DECOYS,
                    help="background ECs for the likelihood ratio")
    ap.add_argument("--model", default=MODEL_ID)
    ap.add_argument("--out", default="scores.tsv")
    args = ap.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"loading {args.model} on {device}")
    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = GPT2LMHeadModel.from_pretrained(args.model).to(device).eval()

    decoys = [d for d in args.decoys if d != args.ec]
    rows = []

    for name, raw in read_fasta(args.fasta):
        seq = clean(raw)
        if not seq:
            print(f"  skipping {name}: no valid residues")
            continue

        nll_target = mean_nll(model, tokenizer, args.ec, seq, device)
        if nll_target is None:
            print(f"  skipping {name}: {len(seq)} aa exceeds the 1024-token context")
            continue

        decoy_nlls = {d: mean_nll(model, tokenizer, d, seq, device) for d in decoys}
        decoy_nlls = {k: v for k, v in decoy_nlls.items() if v is not None}
        best_decoy = min(decoy_nlls, key=decoy_nlls.get)

        rows.append({
            "name": name,
            "length": len(seq),
            "ppl": math.exp(nll_target),
            "llr": decoy_nlls[best_decoy] - nll_target,
            "best_decoy": best_decoy,
        })
        print(f"  {name}: ppl={rows[-1]['ppl']:.3f} llr={rows[-1]['llr']:+.3f} "
              f"(closest decoy {best_decoy})")

    # Rank by discrimination first, then by absolute fit.
    rows.sort(key=lambda r: (-r["llr"], r["ppl"]))

    with open(args.out, "w") as fh:
        fh.write("name\tlength\tppl\tllr\tbest_decoy\n")
        for r in rows:
            fh.write(f"{r['name']}\t{r['length']}\t{r['ppl']:.4f}\t"
                     f"{r['llr']:.4f}\t{r['best_decoy']}\n")

    print(f"\nwrote {len(rows)} scored sequences to {args.out}")


if __name__ == "__main__":
    main()
