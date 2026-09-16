import React from "react";
import { interpolate, useCurrentFrame } from "remotion";
import { theme } from "../theme";
import {
  Poly,
  V3,
  capsidPolys,
  lathePolys,
  renderOutline,
  tubePolys,
} from "./mesh";

/**
 * 9-2-1 Φ8 as one line-drawn solid.
 *
 * It is a podovirus: our own synteny analysis puts the virion module in the
 * canonical podovirus order — portal (CDS_0020) → major capsid (0017) →
 * head/tail adaptor (0016/0014/0013) → tail spike (0011) → tail (0010) → tail
 * fibre (0009) → ejection protein (0008) (code/0730_synteny_group_d/). So the
 * tail is SHORT and non-contractile. A long contractile tail would be a
 * myovirus — someone else's phage.
 *
 * Capsid facets, tail tube, nozzle cone and the six spikes are one mesh. It is
 * rendered as outlines with hidden-line removal (see renderOutline): faces are
 * filled with the page colour purely to occlude, and only contour edges are
 * stroked. No shading, no fills you can see — but the spikes are real swept
 * tubes, so they carry volume instead of being a few strokes.
 *
 * The model does not spin. A fixed three-quarter view reads as a considered
 * object; a rotating wireframe reads as a toy.
 */

const TILT = 0.34;
const YAW = 0.62;

export const Phage: React.FC<{
  x: number;
  y: number;
  scale?: number;
  delay?: number;
  /** 0 = spikes folded against the capsid, 1 = extended for adsorption */
  splay?: number;
  /** optional slow drift; 0 keeps the fixed three-quarter view */
  spin?: number;
}> = ({ x, y, scale = 1, delay = 0, splay = 1, spin = 0 }) => {
  const frame = useCurrentFrame();
  const s = (n: number) => n * scale;

  const R = s(92);
  const yHead = -R * 0.86;
  const yTube = yHead - s(30);
  const yNozzleTop = yTube - s(6);
  const yNozzle = yNozzleTop - s(26);

  const polys: Poly[] = [
    ...capsidPolys(R),
    ...lathePolys(
      [
        { r: s(19), y: yHead },
        { r: s(19), y: yTube },
        { r: s(30), y: yNozzleTop },
        { r: s(22), y: yNozzle },
      ],
      "tail",
      "tail",
      20,
    ),
  ];

  for (let i = 0; i < 6; i++) {
    const a = (i / 6) * Math.PI * 2;
    const cos = Math.cos(a);
    const sin = Math.sin(a);

    const rHinge = s(20);
    const rKnee = interpolate(splay, [0, 1], [s(26), s(46)]);
    const yKnee = interpolate(splay, [0, 1], [yNozzle + s(46), yNozzle - s(34)]);
    const rTip = interpolate(splay, [0, 1], [s(30), s(60)]);
    const yTip = interpolate(splay, [0, 1], [yNozzle + s(96), yNozzle - s(62)]);

    const path: V3[] = [
      [rHinge * cos, yNozzle, rHinge * sin],
      [rKnee * cos, yKnee, rKnee * sin],
      [rTip * cos, yTip, rTip * sin],
    ];

    // 10 sides: enough that adjacent facets stay below the crease threshold, so
    // a spike reads as one smooth volume rather than a bundle of seams
    polys.push(
      ...tubePolys(path, [s(8), s(5), s(2.6)], "spike", `sp${i}_`, 10),
    );
  }

  const ops = renderOutline(polys, {
    ry: YAW + frame * spin,
    rx: TILT,
    crease: {
      capsid: 25, // keep the icosahedral faceting
      tail: false, // silhouette only
      spike: false, // silhouette only
    },
  });

  const lw = Math.max(0.6, Math.min(2, scale));
  const inkFor = { capsid: theme.cool, tail: theme.stroke, spike: theme.accent };
  const widthFor = { capsid: 1.5, tail: 1.5, spike: 1.9 };

  // total edges, so the reveal spreads across the object rather than per-face
  const edgeCount = ops.filter((o) => o.kind === "edge").length || 1;
  let seen = 0;

  return (
    <g transform={`translate(${x} ${y})`}>
      {ops.map((op) => {
        if (op.kind === "fill") {
          return (
            <path key={op.key} d={op.d} fill={theme.bg} stroke="none" />
          );
        }
        const t = seen++ / edgeCount;
        const p = interpolate(
          frame - delay - t * 26,
          [0, 9],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
        );
        return (
          <path
            key={op.key}
            d={op.d}
            fill="none"
            stroke={inkFor[op.mat]}
            strokeWidth={widthFor[op.mat] * lw}
            strokeLinecap="round"
            pathLength={1}
            strokeDasharray={1}
            strokeDashoffset={1 - p}
          />
        );
      })}
    </g>
  );
};

/** Total drop from the capsid centre to the splayed spike tips, in local units. */
export const PHAGE_TIP_DROP = 92 * 0.86 + 30 + 6 + 26 + 62;
