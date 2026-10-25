"""Turn the deck's drawings into real movement.

A scene is one function, `draw(ax, s)`, where `s` is a dictionary of numbers:
positions, widths, opacities. A timeline is a list of keyframes — a time in
seconds and the values that hold at that time — and anything not named in a
keyframe carries forward from the one before. The engine evaluates the state at
every video frame, redraws the scene, and pipes the pixels straight into ffmpeg.

So nothing here cross-fades between finished pictures. The picture itself is a
function of time: the phage descends, the channel opens, the pointer extends.

    python code/1025_presentation_deck/render_movies.py
"""
import math
import shutil
import subprocess
from pathlib import Path

import numpy as np

from anim_style import PAPER, canvas

ROOT = Path(__file__).resolve().parents[2]
MOVIES = ROOT / "code/output/1025_presentation_deck/movies"
POSTERS = ROOT / "code/output/1025_presentation_deck/posters"

FPS = 30
W_IN, H_IN, DPI = 12.8, 6.0, 150          # 1920 x 900, even on both axes


# --------------------------------------------------------------------------- #
# easing
# --------------------------------------------------------------------------- #

def smooth(t):
    """Ease in and out — the default, because linear motion reads as mechanical."""
    return t * t * (3 - 2 * t)


def out(t):
    """Fast then settling: for something arriving."""
    return 1 - (1 - t) ** 3


def inout_back(t):
    """A slight overshoot, for something snapping into place."""
    c = 1.70158
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2


LINEAR = lambda t: t

EASES = {"smooth": smooth, "out": out, "back": inout_back, "linear": LINEAR}


# --------------------------------------------------------------------------- #
# timeline
# --------------------------------------------------------------------------- #

class Timeline:
    """Keyframes of a flat numeric state, with carry-forward and per-key easing.

    keys = [(seconds, {"phage_y": 47, "lbl": 0}), ...]
    """

    def __init__(self, keys, ease="smooth"):
        self.ease = EASES[ease] if isinstance(ease, str) else ease
        self.keys = []
        state = {}
        for t, patch in keys:
            state = dict(state)
            state.update(patch)
            self.keys.append((float(t), state))
        if not self.keys:
            raise ValueError("a timeline needs at least one keyframe")
        self.duration = self.keys[-1][0]

    def at(self, t):
        if t <= self.keys[0][0]:
            return dict(self.keys[0][1])
        if t >= self.duration:
            return dict(self.keys[-1][1])
        for i in range(len(self.keys) - 1):
            t0, s0 = self.keys[i]
            t1, s1 = self.keys[i + 1]
            if t0 <= t <= t1:
                f = self.ease(0.0 if t1 == t0 else (t - t0) / (t1 - t0))
                out_state = dict(s1)
                for k, v1 in s1.items():
                    v0 = s0.get(k, v1)
                    if isinstance(v0, (int, float)) and isinstance(v1, (int, float)):
                        out_state[k] = v0 + (v1 - v0) * f
                return out_state
        return dict(self.keys[-1][1])


# --------------------------------------------------------------------------- #
# rendering
# --------------------------------------------------------------------------- #

def _encode_args(path, w, h):
    return ["ffmpeg", "-y", "-loglevel", "error",
            "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{w}x{h}",
            "-r", str(FPS), "-i", "-",
            "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "20",
            "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.0",
            "-movflags", "+faststart", str(path)]


def render(name, draw, keys, ease="smooth", tail=1.2, xlim=(0, 124), ylim=(0, 52),
           quiet=False):
    """Render one scene to mp4, plus a poster PNG of its final state.

    `tail` holds the last frame so the clip does not cut the moment it lands.
    """
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not on PATH")
    MOVIES.mkdir(parents=True, exist_ok=True)
    POSTERS.mkdir(parents=True, exist_ok=True)

    tl = Timeline(keys, ease=ease)
    total = tl.duration + tail
    n = int(round(total * FPS))

    fig, ax = canvas(W_IN, H_IN, xlim, ylim, dpi=DPI)
    fig.canvas.draw()
    w, h = fig.canvas.get_width_height()

    path = MOVIES / f"{name}.mp4"
    proc = subprocess.Popen(_encode_args(path, w, h), stdin=subprocess.PIPE)
    try:
        for i in range(n):
            t = i / FPS
            ax.clear()
            ax.set_xlim(*xlim)
            ax.set_ylim(*ylim)
            ax.axis("off")
            draw(ax, tl.at(t))
            fig.canvas.draw()
            proc.stdin.write(np.asarray(fig.canvas.buffer_rgba()).tobytes())
        proc.stdin.close()
    finally:
        rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"ffmpeg failed on {name} (exit {rc})")

    # poster: the state the clip ends on, which is what a static export shows
    ax.clear()
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    draw(ax, tl.at(tl.duration))
    fig.savefig(POSTERS / f"{name}.png", facecolor=PAPER)
    import matplotlib.pyplot as plt
    plt.close(fig)

    if not quiet:
        print(f"{name}.mp4  {total:5.1f}s  {n:4d} frames  "
              f"{path.stat().st_size / 1e6:.2f} MB")
    return {"name": name, "path": path, "seconds": total,
            "poster": POSTERS / f"{name}.png"}


def fan(seq, t, step=0.14, span=0.5):
    """Opacity for item i of a sequence appearing one after another.

    `t` is 0..1 for the whole group; returns a list of alphas.
    """
    alphas = []
    for i in range(seq):
        a = (t - i * step) / span
        alphas.append(min(1.0, max(0.0, a)))
    return alphas


def pulse(t, period=1.6, depth=0.25):
    """A gentle breathing multiplier, for something that should feel alive."""
    return 1.0 - depth * 0.5 * (1 - math.cos(2 * math.pi * t / period))
