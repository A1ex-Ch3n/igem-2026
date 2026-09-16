#!/usr/bin/env node
/**
 * Emit captions.vtt from the measured cue table.
 *
 * iGEM requires captions as a SEPARATE .vtt file — never burned into the
 * picture — and warns that auto-generated captions contain errors, so these are
 * built from `src/data/cues.json`: timings measured off the recorded narration
 * with faster-whisper word timestamps, text taken from the script (the
 * transcriber's own words are not trusted).
 *
 *   node scripts/make_vtt.mjs > out/captions.vtt
 *
 * Paste the result into the VTT validator tab on teams.igem.org before upload.
 */
import { readFileSync } from "node:fs";

const data = JSON.parse(
  readFileSync(new URL("../src/data/cues.json", import.meta.url), "utf8"),
);

const stamp = (s) => {
  const h = String(Math.floor(s / 3600)).padStart(2, "0");
  const m = String(Math.floor((s % 3600) / 60)).padStart(2, "0");
  const sec = String(Math.floor(s % 60)).padStart(2, "0");
  const ms = String(Math.round((s % 1) * 1000)).padStart(3, "0");
  return `${h}:${m}:${sec}.${ms}`;
};

const cues = data.cues;
const problems = [];
cues.forEach((c, i) => {
  if (c.e <= c.s) problems.push(`cue ${i + 1}: end is not after start`);
  if (i > 0 && c.s < cues[i - 1].e)
    problems.push(`cue ${i + 1}: overlaps the previous cue`);
  if (c.t.length > 80) problems.push(`cue ${i + 1}: ${c.t.length} chars`);
});
if (problems.length) {
  console.error(problems.join("\n"));
  process.exit(1);
}

const lines = ["WEBVTT", ""];
for (const c of cues) lines.push(`${stamp(c.s)} --> ${stamp(c.e)}`, c.t, "");
process.stdout.write(lines.join("\n"));
