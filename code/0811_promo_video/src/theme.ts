/**
 * Line-art system, two palettes.
 *
 * Everything on screen is a stroke over a visible grid. No fills, no
 * photographic imagery — which is also what keeps the film clear of iGEM's rule
 * against invented imagery that could be mistaken for real experimental
 * results: line-art reads as a diagram, never as a photograph.
 *
 * `morandi` is drawn from the team logo: sage plate, coral lettering, pale blue
 * capsid, olive leaf. `blueprint` is the dark technical variant.
 *
 * Switch with PALETTE below — every scene reads the same token names.
 */

const blueprint = {
  bg: "#0a1420",
  gridDot: "#16283a",
  gridLine: "#101f2d",

  stroke: "#4fd1c5",
  strokeDim: "#2b5f66",
  strokeFaint: "#1d3b45",

  cool: "#7ea8c9", // capsid / structural
  capsidLo: "#12293c", // shaded facet
  capsidHi: "#5f9dc4", // lit facet
  tailLo: "#0f2530",
  tailHi: "#3f8f88",
  spikeLo: "#7a2e21",
  spikeHi: "#f08a72",
  text: "#dcecef",
  textDim: "#7f9aa3",
  accent: "#e0533d",
  accentDim: "#8c3527",
} as const;

const morandi = {
  bg: "#EAEDE4", // the logo plate, lightened for a full frame
  gridDot: "#D2DACA",
  gridLine: "#E0E5D9",

  stroke: "#6E8478", // sage ink — deep enough to survive video compression
  strokeDim: "#9BAA9A",
  strokeFaint: "#C4CCBE",

  cool: "#8FA9C4", // logo capsid blue
  capsidLo: "#7E9BB8", // shaded facet
  capsidHi: "#DCE7F0", // lit facet — the logo's pale blue
  tailLo: "#7E9184",
  tailHi: "#CBD5C8",
  spikeLo: "#B36A46",
  spikeHi: "#F0B294",
  text: "#3F4A42",
  textDim: "#78857A",
  accent: "#DE8A61", // logo coral
  accentDim: "#C4A38F",
} as const;

export const PALETTE: "morandi" | "blueprint" = "morandi";

const palette = PALETTE === "morandi" ? morandi : blueprint;

export const theme = {
  ...palette,
  fontDisplay:
    '"Helvetica Neue", Helvetica, "Inter", "SF Pro Display", Arial, sans-serif',
  fontMono: '"SF Mono", "JetBrains Mono", Menlo, monospace',
  hair: 1.5,
  hairBold: 3,
} as const;

export const GRID = 8;
export const SAFE_MARGIN = 96;
export const W = 1920;
export const H = 1080;
