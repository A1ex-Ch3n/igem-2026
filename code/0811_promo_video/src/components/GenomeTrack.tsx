import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import cds from "../data/cds.json";
import { theme } from "../theme";
import { DrawPath, Note } from "./Draw";

type Gene = {
  cds: string;
  s: number;
  e: number;
  strand: number;
  category: string;
  label: string | null;
};

const GENES = cds.genes as Gene[];

/**
 * The real 80-CDS annotation of 9-2-1 Φ8, drawn as stroke arrows.
 *
 * PHROG category colour is deliberately collapsed here: the printed figure uses
 * nine category colours, which at 1080p over a few seconds reads as confetti.
 * On screen the track carries one distinction the narration actually makes —
 * the tail module, and the tail spike inside it.
 */
export const GenomeTrack: React.FC<{
  /** bp window; defaults to the whole genome */
  window?: [number, number];
  x: number;
  y: number;
  width: number;
  height?: number;
  /** frame at which genes start appearing */
  delay?: number;
  /** frames over which the whole track populates */
  spread?: number;
  showLabels?: boolean;
  /** restrict labels to these CDS ids; omit to label every gene that has one */
  only?: string[];
}> = ({
  window: win = [0, cds.length],
  x,
  y,
  width,
  height = 30,
  delay = 0,
  spread = 40,
  showLabels = true,
  only,
}) => {
  const [ws, we] = win;
  const span = we - ws;
  const px = (bp: number) => x + ((bp - ws) / span) * width;

  const visible = GENES.filter((g) => g.e > ws && g.s < we);
  const h = height / 2;

  const labelled = visible.filter(
    (g) => g.label && showLabels && (!only || only.includes(g.cds)),
  );

  // Stack labels into rows so neighbouring genes never overprint each other.
  // Monospace at `size` is close enough to 0.62 em per character to pack on.
  const rowRight: number[] = [];
  const rowOf = new Map<string, number>();
  for (const g of labelled) {
    const size = g.cds === cds.star ? 26 : 21;
    const half = ((g.label as string).length * size * 0.62) / 2;
    const cx = (px(g.s) + px(g.e)) / 2;
    let r = 0;
    while (r < 4 && cx - half < (rowRight[r] ?? -Infinity) + 24) r++;
    rowRight[r] = cx + half;
    rowOf.set(g.cds, r);
  }

  return (
    <g>
      {/* baseline */}
      <DrawPath
        d={`M ${x} ${y} L ${x + width} ${y}`}
        delay={delay}
        speed={30}
        stroke={theme.strokeFaint}
        width={1}
      />

      {visible.map((g, i) => {
        const isStar = g.cds === cds.star;
        const isTail = g.category === "tail";
        const gx0 = px(Math.max(g.s, ws));
        const gx1 = px(Math.min(g.e, we));
        const w = Math.max(gx1 - gx0, 3);
        const head = Math.min(14, w * 0.45);

        const d =
          g.strand >= 0
            ? `M ${gx0} ${y - h} L ${gx0 + w - head} ${y - h} L ${gx0 + w} ${y} L ${gx0 + w - head} ${y + h} L ${gx0} ${y + h} Z`
            : `M ${gx0 + w} ${y - h} L ${gx0 + head} ${y - h} L ${gx0} ${y} L ${gx0 + head} ${y + h} L ${gx0 + w} ${y + h} Z`;

        return (
          <DrawPath
            key={g.cds}
            d={d}
            delay={delay + (i / Math.max(visible.length - 1, 1)) * spread}
            speed={14}
            stroke={
              isStar ? theme.accent : isTail ? theme.stroke : theme.strokeDim
            }
            width={isStar ? theme.hairBold : theme.hair}
            cap="butt"
          />
        );
      })}

      {labelled.map((g, i) => {
        const cx = (px(g.s) + px(g.e)) / 2;
        const up = (rowOf.get(g.cds) ?? 0) + 1;
        const ly = y - h - 30 * up - 14;
        const isStar = g.cds === cds.star;
        const d0 = delay + spread + 6 + i * 5;
        return (
          <g key={g.cds}>
            <DrawPath
              d={`M ${cx} ${y - h - 6} L ${cx} ${ly + 8}`}
              delay={d0}
              speed={10}
              stroke={isStar ? theme.accent : theme.strokeDim}
              width={1}
            />
            <Note
              x={cx}
              y={ly}
              text={g.label ?? ""}
              delay={d0 + 4}
              anchor="middle"
              color={isStar ? theme.accent : theme.textDim}
              size={isStar ? 26 : 21}
            />
          </g>
        );
      })}
    </g>
  );
};

/** Scale bar with a bp figure — keeps the track honest about its extent. */
export const ScaleBar: React.FC<{
  x: number;
  y: number;
  width: number;
  window: [number, number];
  bp: number;
  delay?: number;
}> = ({ x, y, width, window: win, bp, delay = 0 }) => {
  const w = (bp / (win[1] - win[0])) * width;
  const label = bp >= 1000 ? `${bp / 1000} kb` : `${bp} bp`;
  return (
    <g>
      <DrawPath
        d={`M ${x} ${y} L ${x + w} ${y} M ${x} ${y - 6} L ${x} ${y + 6} M ${x + w} ${y - 6} L ${x + w} ${y + 6}`}
        delay={delay}
        speed={12}
        stroke={theme.strokeDim}
        width={1}
      />
      <Note x={x + w + 14} y={y + 8} text={label} delay={delay + 6} size={20} />
    </g>
  );
};

/** Interpolates a bp window — used to fly from whole genome into the tail module. */
export const useWindow = (
  from: [number, number],
  to: [number, number],
  startFrame: number,
  frames: number,
): [number, number] => {
  const frame = useCurrentFrame();
  const opts = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
  return [
    interpolate(frame, [startFrame, startFrame + frames], [from[0], to[0]], opts),
    interpolate(frame, [startFrame, startFrame + frames], [from[1], to[1]], opts),
  ];
};
