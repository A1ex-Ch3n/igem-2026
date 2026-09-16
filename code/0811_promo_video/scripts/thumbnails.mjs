#!/usr/bin/env node
/**
 * Render every thumbnail candidate into thumbnails/.
 *
 * One bundle for all of them — invoking `remotion still` per variant re-bundles
 * the project each time, which is most of the wall clock.
 *
 *   node scripts/thumbnails.mjs
 *
 * iGEM's only stated limit for the video thumbnail is 4 MB; these land far under.
 */
import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const VARIANTS = ["hero", "adsorption", "genome", "type", "timemachine"];

const serveUrl = await bundle({ entryPoint: path.join(root, "src/index.ts") });

for (const v of VARIANTS) {
  const id = `Thumb-${v}`;
  const composition = await selectComposition({ serveUrl, id });
  const output = path.join(root, "thumbnails", `${v}.png`);
  await renderStill({ composition, serveUrl, output, frame: 60, overwrite: true });
  console.log(`wrote thumbnails/${v}.png`);
}
