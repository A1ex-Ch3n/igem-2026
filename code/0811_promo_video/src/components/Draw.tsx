import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { theme } from "../theme";

/**
 * A path that draws itself on.
 *
 * `pathLength={1}` normalises the geometry so one dash covers the whole path
 * regardless of its real length — the same `delay`/`speed` then reads the same
 * on a 40 px tick and a 1600 px genome track.
 */
export const DrawPath: React.FC<{
  d: string;
  delay?: number;
  speed?: number; // frames to complete
  stroke?: string;
  width?: number;
  dash?: string;
  opacity?: number;
  cap?: "butt" | "round";
}> = ({
  d,
  delay = 0,
  speed = 24,
  stroke = theme.stroke,
  width = theme.hair,
  dash,
  opacity = 1,
  cap = "round",
}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame - delay, [0, speed], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // A dashed line cannot also be used to reveal itself, so dashed paths just
  // fade instead of drawing.
  if (dash) {
    return (
      <path
        d={d}
        fill="none"
        stroke={stroke}
        strokeWidth={width}
        strokeDasharray={dash}
        opacity={p * opacity}
      />
    );
  }

  return (
    <path
      d={d}
      fill="none"
      stroke={stroke}
      strokeWidth={width}
      strokeLinecap={cap}
      strokeLinejoin="round"
      opacity={opacity}
      pathLength={1}
      strokeDasharray={1}
      strokeDashoffset={1 - p}
    />
  );
};

/**
 * A ring that fades in on schedule.
 *
 * Raw <circle> elements ignore the scene clock, so anything drawn that way
 * appears the instant its beat starts while everything around it is still
 * drawing on — which is exactly how the tree tips leaked into frame early.
 */
export const Dot: React.FC<{
  cx: number;
  cy: number;
  r: number;
  delay?: number;
  stroke?: string;
  width?: number;
  fade?: number;
}> = ({
  cx,
  cy,
  r,
  delay = 0,
  stroke = theme.stroke,
  width = 1.5,
  fade = 12,
}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame - delay, [0, fade], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <circle
      cx={cx}
      cy={cy}
      r={r}
      fill="none"
      stroke={stroke}
      strokeWidth={width}
      opacity={o}
    />
  );
};

/** Monospace annotation with a leader tick, blueprint-style. */
export const Note: React.FC<{
  x: number;
  y: number;
  text: string;
  delay?: number;
  anchor?: "start" | "middle" | "end";
  color?: string;
  size?: number;
}> = ({
  x,
  y,
  text,
  delay = 0,
  anchor = "start",
  color = theme.textDim,
  size = 24,
}) => {
  const frame = useCurrentFrame();
  const o = interpolate(frame - delay, [0, 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <text
      x={x}
      y={y}
      fill={color}
      opacity={o}
      textAnchor={anchor}
      fontFamily={theme.fontMono}
      fontSize={size}
      letterSpacing={1.2}
    >
      {text}
    </text>
  );
};
