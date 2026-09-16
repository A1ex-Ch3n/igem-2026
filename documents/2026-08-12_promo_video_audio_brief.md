# Promotion video — audio brief

Music and sound for `code/0811_promo_video`. Script and iGEM rules:
[`2026-08-11_promotional_script.md`](2026-08-11_promotional_script.md).

Total length **115 s**. Narration ends **1:48**; credits card 1:48–1:55.

---

## Where to generate it

| Source | Licence position | Note |
|---|---|---|
| **Artlist** (recommended) | Subscription licence — iGEM accepts "a stock platform licence permitting free reuse" | Already in play for the AI voiceover, so music + narration share one licence and one credit line. Confirm in the account that assets downloaded during the subscription stay licensed |
| **Suno / Udio** | Commercial use on **paid** tiers only; free tiers do not grant it | AI-generated, so iGEM also requires the tool be named in the end credits and on the Attributions Form |
| **ElevenLabs** (music / SFX) | Commercial use on paid plans | Useful if only short sound effects are needed |
| **Free Music Archive · Pixabay · Freesound** | CC0 / CC BY per track — **check each track**, not the site | Zero AI-licence questions; CC BY tracks still need creator + licence on the credits card |

Whatever the source: the licence must permit **both** cutting the material into an
edited work **and** publishing it. A `NoDerivatives` track cannot be used.

---

## Prompt

Paste as-is into a text-to-music tool.

```
Instrumental underscore for a 115-second science documentary about
bacteriophages. Sparse warm minimalism: felt piano, soft marimba, a low
sustained synth pad, faint granular texture. 72 BPM, 4/4, D minor resolving to
F major at the end. No vocals. No drums for the first 45 seconds; from 0:45 a
soft muted kick and light brushed percussion — no snare hits, no cymbal
crashes. No risers, no build to a drop, no cinematic braams, no orchestral
swell. Leave 200 Hz to 4 kHz open for a spoken voiceover: put the melodic
material above 4 kHz or below 200 Hz. Quiet and curious from 0:00 to 0:25;
slightly darker and more urgent from 0:25 to 0:45; steady forward motion from
0:45 to 1:30; one small lift at 1:36; resolved and calm by 1:48, then a
7-second tail that fades to silence.
```

Short version, for tools with a character limit:

```
Sparse instrumental science-documentary underscore. Felt piano, marimba, low
pad. 72 BPM, D minor. No vocals, no drums until halfway, no risers or drops.
Quiet and curious, mid-section slightly urgent, calm resolved ending. Leave the
midrange open for a voiceover.
```

Negative prompt, where the tool takes one:

```
vocals, lyrics, choir, spoken word, heavy drums, trap hi-hats, EDM drop, riser,
braam, orchestral crescendo, distorted bass, sound effects, applause, sidechain
pumping
```

---

## Structure map

The beats are the ones in `src/timeline.ts`. Ask for these dynamics, or edit the
generated track to land on them.

| Time | Beat | What the music does |
|---|---|---|
| 0:00–0:07 | Hook | single sustained pad, one piano note |
| 0:07–0:26 | Stakes — antibiotic resistance | pad darkens, low drone enters |
| 0:26–0:45 | Gap — adsorption | held tension, no percussion yet |
| 0:45–0:58 | Team | first pulse; warmth returns |
| 0:58–1:13 | Method — genome | steady arpeggio under the track drawing on |
| 1:13–1:30 | Wet lab | same pulse, add marimba |
| 1:30–1:36 | ML loop | brief acceleration, six seconds only |
| 1:36–1:48 | Close — time machine | one lift, then resolve to F major |
| 1:48–1:55 | Credits card | tail, fading to silence |

---

## Optional sound effects

The film is silent line-art, so it works with music alone. If effects are added,
keep them under −24 dB and generate them from the same platform so the credit
line stays single:

- soft pen-on-paper tick as shapes draw on (Hook, Method)
- one low settle when the particle reaches the membrane, ~0:39
- faint sub swell as the genome track populates, ~1:00

Do **not** add: whoosh transitions, impact hits, sci-fi beeps. They fight the
restraint of the visual system.

---

## Mix

- Bed around −22 LUFS under narration, −16 LUFS in the credits tail.
- No sidechain ducking — ride the level manually so the pad does not pump.
- Deliver the mixed audio as a single WAV; it goes to
  `code/0811_promo_video/public/audio/` and is wired into `Promo.tsx` with
  `<Audio src={staticFile("audio/…")} />`.

---

## Credits

Whatever is used goes on the end card as **title — creator — licence**, on
screen for at least 2 seconds, and onto the Attributions Form. If the track or
the voice is AI-generated, name the tool there too.

---

## Log

- 2026-08-12 written alongside the 3D phage revision
