# iGEM 2026 Project Promotion Video — Phagenomics

Remotion project for the 2 minute promotion video. Script and iGEM rules live in
`documents/2026-08-11_promotional_script.md`.

## Run

```
npm install
npm run studio                 # live preview at localhost:3000
npm run render                 # -> out/promo.mp4  (1920x1080, h264, ~115 s)
node scripts/make_vtt.mjs --retimed > out/captions.vtt
```

`ffmpeg` is bundled with Remotion for rendering; the separate Homebrew `ffmpeg`
is only needed for the container checks below.

## Where things are

| What | Where |
|---|---|
| Beat timing + narration (single source of truth) | `src/timeline.ts` |
| Scene visuals | `src/scenes.tsx` |
| Design tokens | `src/theme.ts` |
| Credits card (team, assets, licences, AI tools) | `src/components/Credits.tsx` |
| Real CDS coordinates of 9-2-1 Φ8 | `src/data/cds.json` (regenerate: `python scripts/export_cds.py`) |
| Voiceover audio | `public/audio/` (gitignored) |

## Visual system

Blueprint line-art: dark ground, a visible 8 px grid, 1.5 px strokes, no fills.
Every shape draws itself on via `DrawPath` (normalised `pathLength`, so a 40 px
tick and a 1600 px genome track reveal at the same rate).

Nothing on screen is sourced from a third party — every frame is drawn in code,
which is why the credits card currently lists no external assets. If an icon set
is ever added (Servier Medical Art, BioIcons, SciDraw), it must be listed there
and on the Attributions Form, per icon licence.

The genome track is not a picture of a figure: `scripts/export_cds.py` pulls the
real 80-CDS Pharokka annotation into JSON and `GenomeTrack.tsx` draws it as SVG,
so it can zoom, re-window and animate while staying our own data.

## Order of work

1. Record the English VO first. Nothing can be timed without it.
2. Measure the real beat boundaries and write them into `src/timeline.ts`.
3. Build scenes, preview in studio.
4. Render, then generate `captions.vtt` from the same `timeline.ts`.

Doing 4 before 2 guarantees the captions drift out of sync with the picture.

## iGEM constraints baked in

- 115 s total against a machine-enforced 120 s cap.
- 1920x1080 landscape, `.mp4`, well under the 500 MB limit at CRF 20.
- No self-made iGEM intro — iGEM inserts its own after approval.
- Captions ship as a separate `.vtt`, never burned in.
- On-screen figures are the team's own analysis output, so no third-party
  licence applies and nothing can be mistaken for invented results.

## Checks before upload

```
ffprobe -v error -show_entries format=duration,size:stream=width,height out/promo.mp4
python3 -c "print(open('out/promo.mp4','rb').read(12)[4:12].decode())"   # want: ftypisom
```

`ftypisom` is the brand iGEM's uploader accepts. If a file is ever rejected,
repackage with `ffmpeg -i in.mp4 -c copy fixed.mp4`.

### What is in `out/` (gitignored, on disk only)

| File | Brand | Size | Note |
|---|---|---|---|
| `promo_morandi.mp4` / `promo_morandi_final.mp4` | `ftypisom` | 1920x1080, 115.05 s | the Remotion render; identical bytes |
| `ClaremontCA.mp4` | **`ftypqt`** | 3840x2160, 115.80 s | the 4K team export — **this brand is what iGEM's uploader rejects** |
| `ClaremontCA_fixed.mp4` | `ftypisom` | 3840x2160, 115.82 s | the `-c copy` repackage of the above — **this is the file to upload** |
