/**
 * Single source of truth for beat timing.
 *
 * MEASURED, not planned: boundaries come from the recorded ElevenLabs narration
 * (8月12日(1).wav), aligned with faster-whisper word timestamps on 2026-08-12.
 * Each boundary sits inside the silence between paragraphs.
 *
 * The narration text below matches what is actually SPOKEN. Note the Team beat:
 * the recording says "isolated ... we sampled", which predates the later
 * "collected ... around us" rewrite. Captions must match the audio, so the
 * recording wins until that line is re-recorded.
 *
 * Per-cue caption timings live in src/data/cues.json — finer grained than these
 * beats, and what scripts/make_vtt.mjs emits.
 */

export const FPS = 30;

export type Beat = {
  id: string;
  start: number; // seconds
  end: number; // seconds
  text: string; // narration, verbatim
};

export const BEATS: Beat[] = [
  {
    id: "hook",
    start: 0,
    end: 5.9,
    text: "Phages are viruses that hunt bacteria. They have been doing it for billions of years.",
  },
  {
    id: "stakes",
    start: 5.9,
    end: 28.5,
    text: "That matters right now. Antibiotic resistance is rising, and infections we could once cure are becoming untreatable. Phages are one way to fight back, but only if a phage can infect the exact bacterium making someone sick. Most of the time, it cannot.",
  },
  {
    id: "gap",
    start: 28.5,
    end: 43.2,
    text: "That decision is made in the first seconds of contact, by the tail spike proteins that grip the bacterial surface. We do not know which parts of them set the host range, and we cannot yet aim a phage at a new host.",
  },
  {
    id: "team",
    start: 43.2,
    end: 56.9,
    // The recording predates the "collected ... around us" rewrite; this is what
    // the voice actually says, so it is what the captions carry.
    text: "We are Phagenomics, a team from Claremont, California. We isolated our phages from water and soil we sampled, along with the bacteria they infect, and sequenced them ourselves.",
  },
  {
    id: "method",
    start: 56.9,
    end: 72.3,
    text: "We treat host range as an evolutionary question. We take the receptor binding protein, the part that makes first contact, and reconstruct its ancestors, versions that existed long before the strains on our bench.",
  },
  {
    id: "wetlab",
    start: 72.3,
    end: 89.7,
    text: "We build those ancestral proteins in the lab and measure how tightly each one binds its target. Evolution already ran this experiment. The ancestral sequences are its notes, recording which changes opened a host range and which closed it.",
  },
  {
    id: "mlloop",
    start: 89.7,
    end: 95.0,
    text: "Those measurements train our model, and the model tells us what to change next.",
  },
  {
    id: "close",
    start: 95.0,
    end: 105.6,
    text: "So this is a time machine. We go backward to find out what evolution learned, and we run it forward to design the next generation of phages.",
  },
];

/** Credits card runs after the narration ends. iGEM requires >= 2 s on screen. */
export const CREDITS_START = 105.6;
export const TOTAL_SECONDS = 113; // hard cap is 120 — keep margin for the check

export const DURATION_IN_FRAMES = Math.round(TOTAL_SECONDS * FPS);

export const sec = (s: number) => Math.round(s * FPS);

export const beat = (id: string): Beat => {
  const b = BEATS.find((x) => x.id === id);
  if (!b) throw new Error(`unknown beat: ${id}`);
  return b;
};

export const beatFrames = (id: string) => {
  const b = beat(id);
  return { from: sec(b.start), durationInFrames: sec(b.end) - sec(b.start) };
};
