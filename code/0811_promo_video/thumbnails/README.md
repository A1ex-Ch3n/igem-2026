# Thumbnail candidates

Frames pulled from the final 4K cut (`ClaremontCA_fixed.mp4`), so whichever is
chosen matches the film exactly — nothing here is a separate asset to license or
keep in sync.

| File | Source time | What it shows |
|---|---|---|
| `01_hero_phage.png` | 0:03 | The virion and the opening line — clearest "what is this about" |
| `02_resistance.png` | 0:22 | The stakes, and the one strain that matters |
| `03_adsorption.png` | 0:40 | The particle on the membrane, spikes engaged |
| `04_genome.png` | 1:02 | Our own annotation, tail spike picked out |
| `05_time_machine.png` | 1:40 | The closing idea, type-led |

3840×2160 PNG, 0.5–1.8 MB each. iGEM's only stated limit for the video thumbnail
is 4 MB.

Add or replace a candidate:

```
ffmpeg -ss <seconds> -i ../../../ClaremontCA_fixed.mp4 -frames:v 1 out.png
```

`src/Thumbnail.tsx` also holds purpose-built thumbnail compositions — composed
rather than grabbed, with the real title set as a lockup. Render them with
`node scripts/thumbnails.mjs` once the Chrome that Remotion drives launches
again; it currently hangs on startup, which is an environment problem, not a
code one (the binary runs, but never opens its debugging port).
