# examples

Runnable examples, one per tool. `phagecheck` needs no downloaded data — its tests build their own
genomes and reads, and double as the worked example:

```bash
python -m pytest phagecheck/tests -q            # 11 tests, < 2 s
python -m phagecheck.dtr --help
python -m phagecheck.betahelix --help
```

To run `phagecheck.betahelix` on a real structure, point it at any predicted PDB:

```bash
python -m phagecheck.betahelix path/to/fold.pdb --out fold_calls.tsv
```

Examples for `olocus`, `gelquant` and `phageresist` land with those ports; each needs a small
fixture (a miniature annotation, a synthetic gel image, a 2 kb reference with one known variant)
rather than a copy of our project data.
