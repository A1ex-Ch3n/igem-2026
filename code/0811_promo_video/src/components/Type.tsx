import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { SAFE_MARGIN, theme } from "../theme";

/** Big statement line. Rises and fades in over `delay` frames. */
export const Statement: React.FC<{
  children: React.ReactNode;
  delay?: number;
  size?: number;
  align?: "left" | "center";
  color?: string;
}> = ({ children, delay = 0, size = 76, align = "left", color = theme.text }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame - delay, [0, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        fontFamily: theme.fontDisplay,
        fontSize: size,
        lineHeight: 1.18,
        fontWeight: 600,
        letterSpacing: -1.2,
        color,
        textAlign: align,
        opacity: t,
        transform: `translateY(${(1 - t) * 22}px)`,
      }}
    >
      {children}
    </div>
  );
};

/** Small monospace label — used for figure provenance and section tags. */
export const Label: React.FC<{
  children: React.ReactNode;
  delay?: number;
}> = ({ children, delay = 0 }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame - delay, [0, 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        fontFamily: theme.fontMono,
        fontSize: 24,
        letterSpacing: 2.4,
        textTransform: "uppercase",
        color: theme.accent,
        opacity: t,
      }}
    >
      {children}
    </div>
  );
};

/** Standard scene frame: safe margins, vertical stack, left aligned. */
export const Stage: React.FC<{
  children: React.ReactNode;
  justify?: React.CSSProperties["justifyContent"];
  align?: React.CSSProperties["alignItems"];
  gap?: number;
}> = ({ children, justify = "center", align = "flex-start", gap = 28 }) => (
  <div
    style={{
      position: "absolute",
      inset: SAFE_MARGIN,
      display: "flex",
      flexDirection: "column",
      justifyContent: justify,
      alignItems: align,
      gap,
    }}
  >
    {children}
  </div>
);
