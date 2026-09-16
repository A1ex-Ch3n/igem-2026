import React from "react";
import { DrawPath } from "./Draw";
import { theme } from "../theme";

/**
 * A perspective ground plane for the adsorption scene.
 *
 * The capsid is a real rotating icosahedron, so standing it on a flat 2D rule
 * reads wrong — one object in depth inside a diagram with none. This puts the
 * whole scene in the same space: the membrane recedes to a horizon, the sugar
 * chains shrink with distance, and the particle scales with its own depth.
 *
 * Pinhole camera looking down the +z axis from height CAM_H above the plane.
 * A world point (x, y, z), y measured up from the membrane, lands at
 *   sx = CX + x·f/z,  sy = HORIZON + (CAM_H − y)·f/z,  scale = f/z
 */
export const CAM = {
  f: 900,
  camH: 260,
  cx: 960,
  horizon: 380,
} as const;

export const project = (x: number, y: number, z: number) => {
  const s = CAM.f / z;
  return {
    x: CAM.cx + x * s,
    y: CAM.horizon + (CAM.camH - y) * s,
    s,
  };
};

/** Rows of constant depth, plus rails converging to the vanishing point. */
export const Membrane: React.FC<{
  rows: number[];
  halfWidth?: number;
  railStep?: number;
  delay?: number;
}> = ({ rows, halfWidth = 2400, railStep = 480, delay = 0 }) => {
  // offset by half a step so no rail runs straight through the particle at x=0
  const rails: number[] = [];
  for (let x = -halfWidth + railStep / 2; x <= halfWidth; x += railStep)
    rails.push(x);
  const zNear = rows[0];
  const zFar = rows[rows.length - 1];

  return (
    <g>
      {rows.map((z, i) => {
        const a = project(-halfWidth, 0, z);
        const b = project(halfWidth, 0, z);
        return (
          <DrawPath
            key={`r${z}`}
            d={`M ${a.x} ${a.y} L ${b.x} ${b.y}`}
            delay={delay + i * 3}
            speed={26}
            stroke={i === 0 ? theme.strokeDim : theme.strokeFaint}
            width={i === 0 ? 1.6 : 1}
          />
        );
      })}
      {rails.map((x, i) => {
        const a = project(x, 0, zNear);
        const b = project(x, 0, zFar);
        return (
          <DrawPath
            key={`c${x}`}
            d={`M ${a.x} ${a.y} L ${b.x} ${b.y}`}
            delay={delay + 6 + i}
            speed={22}
            stroke={theme.strokeFaint}
            width={1}
          />
        );
      })}
    </g>
  );
};

/**
 * LPS O-antigen standing off the membrane. Our tail spike (CDS_0011) is a
 * β-helix depolymerase and the receptor is this sugar, not a surface protein —
 * adsorption is the spike cleaving these chains.
 *
 * `cleaveAt` is a world-space circle; chains inside it shorten as
 * `cleaveProgress` runs 0 → 1.
 */
export const OAntigenField: React.FC<{
  rows: number[];
  halfWidth?: number;
  step?: number;
  height?: number;
  delay?: number;
  cleaveAt?: { x: number; z: number; r: number };
  cleaveProgress?: number;
}> = ({
  rows,
  halfWidth = 1500,
  step = 105,
  height = 34,
  delay = 0,
  cleaveAt,
  cleaveProgress = 0,
}) => {
  const chains: { x: number; z: number }[] = [];
  for (const z of rows) {
    for (let x = -halfWidth; x <= halfWidth; x += step) chains.push({ x, z });
  }

  return (
    <g>
      {chains.map(({ x, z }, i) => {
        const cut =
          cleaveAt &&
          Math.hypot(x - cleaveAt.x, z - cleaveAt.z) < cleaveAt.r;
        const h = cut ? height * (1 - 0.82 * cleaveProgress) : height;

        // three kinks so it reads as polysaccharide rather than a bristle
        const p0 = project(x, 0, z);
        const p1 = project(x + 7, h * 0.34, z);
        const p2 = project(x - 7, h * 0.67, z);
        const p3 = project(x, h, z);

        return (
          <DrawPath
            key={i}
            d={`M ${p0.x} ${p0.y} L ${p1.x} ${p1.y} L ${p2.x} ${p2.y} L ${p3.x} ${p3.y}`}
            delay={delay + (i % 17) * 1.2}
            speed={10}
            stroke={cut ? theme.accentDim : theme.strokeDim}
            width={Math.max(0.7, 1.2 * p0.s)}
            opacity={Math.min(0.9, 0.2 + p0.s * 0.45)}
          />
        );
      })}
    </g>
  );
};
