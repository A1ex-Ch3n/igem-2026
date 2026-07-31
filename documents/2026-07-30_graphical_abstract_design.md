# Graphical abstract — design spec (item 2)

Design for the PI's item 2, *"a graphical abstract that summarizes the overall
project"* (2026-07-27 email). Brainstormed and locked with Alex on 2026-07-30.
This is the **design + the list of what must be confirmed before it can be
built** — the figure is not built yet (three inputs are pending, see §6).

> Ambiguities surfaced up front: the project's results are characterisation-heavy,
> but a graphical abstract needs an *engineering thesis*. That thesis (below) is
> forward-looking — most of the central pipeline is **proposed / in progress**, not
> demonstrated. The honesty scheme (§4) exists so the figure cannot be misread as
> finished work.

## 1. Thesis (the one message)

**Programmable, sugar-specific phages: read the O-antigen, retarget which bacteria
the phage kills.** An engineering-platform story — not "we characterised a phage".
Structure/mechanism-informed, in deliberate contrast to Phagos's genome-only
host-range prediction (`2026-07-30_phagos_company_research.md`).

## 2. Audience / venue

**One master, wide, reflowable → export three crops:** iGEM wiki hero (wide),
manuscript graphical abstract (≈1:1 or portrait), presentation slide (16:9).
Design the logic once; the master must degrade gracefully (wide = one row;
square = two rows). Must read at phone width and in greyscale.

## 3. Layout — Approach A, horizontal DBTL pipeline (left → right)

```
Zone 0  ── title strip: the one-line thesis ────────────────────────────────
┌── Zone 1: FOUNDATION (✅ solid) ──┐  ┌─ Zone 2: ENGINEERING LOOP (proposed) ─┐  ┌ Zone 3: OUTPUT ┐
│ novel ~62 kb Pseudomonas podo-    │  │  Learn  →  Test   →   Build            │  │ platform:      │
│ virus 9-2-1 Φ8                    │  │  GH5     in trans     modular          │  │ seq → predict  │
│ tail spike CDS_0011 = β-helix     │  │  ancestral  challenge  depolymerase    │  │ which sugar    │
│ DEPOLYMERASE                      │  │  tree      (affinity   swap            │  │ → retarget     │
│ receptor = strain-specific        │  │  → rules)   readout)   (host-range     │  │                │
│ O-ANTIGEN sugar (not a protein)   │  │                        on demand)      │  │ programmable   │
│ 3 strains × 3 non-homologous      │  │                                        │  │ precision      │
│ O-antigen cassettes (one ihfB     │  │                                        │  │ antibacterial  │
│ slot) → why one phage can't kill  │  │                                        │  │ platform       │
│ all, and why it's a handle        │  │                                        │  │                │
│ (aux) 2nd depolymerase CDS_0024   │  │                                        │  │                │
└───────────────────────────────────┘  └────────────────────────────────────────┘  └────────────────┘
```

- **Reading direction:** left→right narrative. Wide venue = this single row;
  square venue = Zone 1 top, Zones 2–3 bottom.
- **Zone 1** is the confirmed ground truth; **Zone 2** is the DBTL engineering
  loop (Learn→Test→Build); **Zone 3** is the deliverable — the *platform/method*
  itself (design rules + prediction), with modular swap as its ultimate use.

## 4. Honesty scheme (non-negotiable)

A single legend, applied throughout:

- **Solid outline / full colour = done, has data.**
- **Dashed outline / faded = in progress or proposed.**

| Element | Status | Rendering |
|---|---|---|
| podovirus genome, β-helix depolymerase, O-antigen receptor, 3 cassettes, CDS_0024 | ✅ has data | **solid** |
| recombinant proteins CDS_0011 / CDS_0012 | ordered, not expressed | half-dashed |
| host-range assay | run 2026-07-04, **data not in hand** | half-dashed |
| GH5 ancestral tree (Learn) | PI building it | half-dashed |
| in-trans challenge (Test), modular swap (Build), prediction platform (Output) | proposed / concept | **dashed** |

Application framing (Zone 3): **species-agnostic** "programmable precision
antibacterial platform", *demonstrated on environmental Pseudomonas*. **Do not
imply clinical use** — the isolates are *Pseudomonas_E* sp013179515 and
*P. capeferrum*, not clinical *P. aeruginosa*.

## 5. Style

- Reuse the synthesis figures' colour language where it exists: tail spike /
  depolymerase in the red-accent already used for CDS_0011; O-antigen cassette in
  the red used on the bacterial maps. Keep a small, restrained palette (≤5
  colours) that survives greyscale.
- Baby blue as a secondary accent (Alex's chosen 3D-print colour — a light thread
  tying the abstract to the physical tail-spike prints).
- Icons over photos; one sugar-chain glyph reused everywhere for "O-antigen".
- **Build as editable vector (SVG).** This is a designed schematic, not a
  data-driven plot, so it is *not* a matplotlib figure — hand-authored or
  scripted SVG that stays editable for the reflow crops. Tool chosen at build time
  (Inkscape / drawsvg / hand SVG).

## 6. What must be confirmed before building (the ask)

**Locked (2026-07-30 with Alex):** thesis · layout A · the Learn→Test→Build flow ·
deliverable = platform/method · venue = master→export · application = species-
agnostic platform.

**Still pending — mostly from the PI:**

1. **Host-range readout** — awaiting the PI's 2026-07-04 notebook. Decides whether
   the "one phage can't kill all" panel can show real data or stays a prediction.
2. **GH5 ancestral tree output** — the PI is building it; needed to draw the *Learn*
   panel concretely.
3. **In-trans experimental design** — needed to draw the *Test* panel concretely.
4. (minor) confirm the exact one-line thesis wording with the PI.

Until 1–3 land, the central loop stays schematic/dashed. The figure can be drafted
now with placeholders and finalised as each input arrives.

## 7. Tooling — how it gets built (filtered by "Claude can iterate")

Selection filter (Alex's): the tool must let Claude help **execute *and* iterate**,
not just hand back a one-shot image.

| Tool | Claude can drive it? | Medium fit | Verdict |
|---|---|---|---|
| **Claude-authored SVG** (drawsvg to write, cairosvg to rasterise so Claude can *see* and correct its own output) | ✅ full loop — write → render → view → edit | vector, reflowable, wiki + manuscript ready | **primary** |
| **HTML + inline SVG as a claude.ai Artifact** | ✅ authors + republishes; you watch it update live at one URL | same SVG, live shareable preview | **complement** (your live view) |
| **PaperBanana** (`paperbanana.me` — the one Alex used; text→figure, five-agent, **exports editable SVG**) | ⚠️ no — web GUI, Claude can't drive it | fast, pretty first pass | **optional seeder**: generate a draft there → export SVG → Claude refines it |
| **matplotlib** (already installed) | ✅ but wrong medium | data plots, not designed illustration | fallback only |
| **BioRender / Inkscape / Canva** | ❌ GUI, Claude can't drive (fails the filter) | best icon libraries if *you* build it by hand | not for a Claude-driven loop |

**Recommendation:** primary = **Claude-authored SVG** (`drawsvg` + `cairosvg` for
self-check — one `python -m pip install drawsvg cairosvg`, the only setup),
complemented by an **HTML/SVG Artifact** so Alex gets a live preview. PaperBanana
is a useful *seeder* only because it exports editable SVG that Claude can then take
over — Claude cannot iterate inside it.

---
*Log — 2026-07-30: brainstormed with Alex. Locked thesis (engineering host-range
platform), Layout A (horizontal DBTL), the GH5-Learn → in-trans-Test →
modular-swap-Build flow, platform/method as the deliverable, master→export venue,
and a species-agnostic application framing (not clinical — environmental
Pseudomonas). Honesty scheme fixed (solid = done, dashed = proposed). Figure not
built: three inputs pending, all from the PI (host-range readout, GH5 tree,
in-trans design). Feeds §1 item 2 of the results synthesis.*
