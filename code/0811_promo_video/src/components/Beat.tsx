import React from "react";
import { AbsoluteFill, Sequence, interpolate, useCurrentFrame } from "remotion";
import { beatFrames } from "../timeline";
import { theme } from "../theme";

const FADE = 12; // frames of cross-fade at each edge

/**
 * Wraps one narration beat. Handles its own fade so scenes only describe
 * what they show, never when. Timing comes from timeline.ts.
 */
export const Beat: React.FC<{
  id: string;
  children: React.ReactNode;
}> = ({ id, children }) => {
  const { from, durationInFrames } = beatFrames(id);
  return (
    <Sequence from={from} durationInFrames={durationInFrames} name={id}>
      <Fader durationInFrames={durationInFrames}>{children}</Fader>
    </Sequence>
  );
};

const Fader: React.FC<{
  durationInFrames: number;
  children: React.ReactNode;
}> = ({ durationInFrames, children }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(
    frame,
    [0, FADE, durationInFrames - FADE, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );
  return (
    <AbsoluteFill style={{ opacity, backgroundColor: theme.bg }}>
      {children}
    </AbsoluteFill>
  );
};
