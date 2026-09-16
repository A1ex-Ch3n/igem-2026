import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { GRID, H, W, theme } from "../theme";

/**
 * The blueprint ground: a dot grid that fades up at the start of a scene and
 * drifts a few pixels across it, so static frames never feel frozen.
 */
export const Grid: React.FC<{ drift?: number }> = ({ drift = 12 }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const dx = (frame / 60) * drift;

  return (
    <AbsoluteFill style={{ backgroundColor: theme.bg }}>
      <svg width={W} height={H} style={{ opacity }}>
        <defs>
          <pattern
            id="dots"
            width={GRID * 8}
            height={GRID * 8}
            patternUnits="userSpaceOnUse"
            patternTransform={`translate(${dx % (GRID * 8)} 0)`}
          >
            <circle cx={0} cy={0} r={1.1} fill={theme.gridDot} />
          </pattern>
          <pattern
            id="rules"
            width={GRID * 32}
            height={GRID * 32}
            patternUnits="userSpaceOnUse"
            patternTransform={`translate(${dx % (GRID * 32)} 0)`}
          >
            <path
              d={`M 0 0 L ${GRID * 32} 0 M 0 0 L 0 ${GRID * 32}`}
              stroke={theme.gridLine}
              strokeWidth={1}
              fill="none"
            />
          </pattern>
        </defs>
        <rect width={W} height={H} fill="url(#rules)" />
        <rect width={W} height={H} fill="url(#dots)" />
      </svg>
    </AbsoluteFill>
  );
};
