"""Render every animated clip to mp4.

    python code/1025_presentation_deck/render_movies.py            # all of them
    python code/1025_presentation_deck/render_movies.py tree reads-filter

Clips land in code/output/1025_presentation_deck/movies/ and a poster PNG of
each one's final state in .../posters/. build_deck.py embeds both.
"""
import sys
from concurrent.futures import ProcessPoolExecutor

import mov_adsorption
import mov_bench
import mov_method
import motion

SCENES = {}
for mod in (mov_adsorption, mov_method, mov_bench):
    SCENES.update(mod.SCENES)


def one(name):
    draw, keys = SCENES[name]
    r = motion.render(name, draw, keys, quiet=True)
    return name, r["seconds"], r["path"].stat().st_size


def main(names):
    bad = [n for n in names if n not in SCENES]
    if bad:
        raise SystemExit(f"unknown scene(s): {', '.join(bad)}")
    total = 0.0
    with ProcessPoolExecutor() as pool:
        for name, secs, size in pool.map(one, names):
            total += secs
            print(f"{name:28s} {secs:5.1f}s  {size / 1e6:5.2f} MB")
    print(f"\n{len(names)} clips, {total / 60:.1f} min of motion")


if __name__ == "__main__":
    main(sys.argv[1:] or list(SCENES))
