/**
 * A very small software renderer, so every part of an object goes through the
 * same pipeline instead of each piece being drawn its own way.
 *
 * Build polygons in local space → transform → cull back faces → sort by depth →
 * fill with a lambert term and stroke the edge. Because capsid facets, tail
 * tube, nozzle and spikes are all polygons in one list, they shade under one
 * light and occlude each other for free.
 */

export type V3 = [number, number, number];

export type Poly = {
  /** local-space vertices, wound counter-clockwise seen from outside */
  pts: V3[];
  /** which material tints this face */
  mat: "capsid" | "tail" | "spike";
  /** stable id so a reveal can stagger deterministically */
  key: string;
  /** closed surfaces cull; open strips (rare) do not */
  cull?: boolean;
};

export const rotY = ([x, y, z]: V3, a: number): V3 => {
  const c = Math.cos(a);
  const s = Math.sin(a);
  return [x * c + z * s, y, -x * s + z * c];
};

export const rotX = ([x, y, z]: V3, a: number): V3 => {
  const c = Math.cos(a);
  const s = Math.sin(a);
  return [x, y * c - z * s, y * s + z * c];
};

const sub = (a: V3, b: V3): V3 => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];

const cross = (a: V3, b: V3): V3 => [
  a[1] * b[2] - a[2] * b[1],
  a[2] * b[0] - a[0] * b[2],
  a[0] * b[1] - a[1] * b[0],
];

const norm = (a: V3): V3 => {
  const m = Math.hypot(a[0], a[1], a[2]) || 1;
  return [a[0] / m, a[1] / m, a[2] / m];
};

const dot = (a: V3, b: V3) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

/** Key light: upper left, slightly toward the viewer. */
const LIGHT = norm([-0.35, 0.62, 0.7]);

const hex = (h: string): [number, number, number] => [
  parseInt(h.slice(1, 3), 16),
  parseInt(h.slice(3, 5), 16),
  parseInt(h.slice(5, 7), 16),
];

const toHex = (c: [number, number, number]) =>
  "#" +
  c
    .map((v) => Math.max(0, Math.min(255, Math.round(v))).toString(16).padStart(2, "0"))
    .join("");

export const mix = (a: string, b: string, t: number) => {
  const A = hex(a);
  const B = hex(b);
  return toHex([
    A[0] + (B[0] - A[0]) * t,
    A[1] + (B[1] - A[1]) * t,
    A[2] + (B[2] - A[2]) * t,
  ]);
};

export type Drawn = {
  key: string;
  d: string;
  fill: string;
  stroke: string;
  depth: number;
  order: number;
};

/**
 * Transform, cull and depth-sort. Returns polygons back-to-front, each already
 * shaded — the caller only has to emit <path>.
 *
 * Screen space flips y (SVG grows downward); +z is toward the viewer, so a face
 * is visible when its normal has a positive z.
 */
export const renderMesh = (
  polys: Poly[],
  opts: {
    ry: number;
    rx: number;
    tint: Record<Poly["mat"], [string, string]>;
    /** how dark an unlit face gets: 0 = black, 1 = flat */
    ambient?: number;
  },
): Drawn[] => {
  const { ry, rx, tint, ambient = 0.3 } = opts;
  const out: Drawn[] = [];

  polys.forEach((p, i) => {
    const world = p.pts.map((v) => rotX(rotY(v, ry), rx));
    const n = norm(cross(sub(world[1], world[0]), sub(world[2], world[0])));

    if (p.cull !== false && n[2] <= 0.02) return;

    const lambert = Math.max(0, dot(n, LIGHT));
    const t = ambient + (1 - ambient) * lambert;
    const [lo, hi] = tint[p.mat];
    const fill = mix(lo, hi, t);

    const depth =
      world.reduce((acc, v) => acc + v[2], 0) / world.length;

    const d =
      world
        .map(
          (v, k) =>
            `${k === 0 ? "M" : "L"} ${v[0].toFixed(2)} ${(-v[1]).toFixed(2)}`,
        )
        .join(" ") + " Z";

    out.push({
      key: p.key,
      d,
      fill,
      // a facet edge one step darker than its own fill keeps the faceting
      // readable without a separate outline pass
      stroke: mix(lo, hi, Math.max(0, t - 0.35)),
      depth,
      order: i,
    });
  });

  return out.sort((a, b) => a.depth - b.depth);
};

export type Op =
  | { kind: "fill"; d: string; key: string }
  | { kind: "edge"; d: string; mat: Poly["mat"]; key: string };

/**
 * Hidden-line rendering: the same mesh, drawn as outlines.
 *
 * Each visible face is filled with the page colour — invisible, but it occludes
 * whatever was drawn behind it — and then only its *contour* edges are stroked.
 * An edge is contour if it is a silhouette (one neighbouring face faces away)
 * or, for materials that ask for it, a crease sharp enough to read as a facet.
 *
 * That is what gives the tail and the spikes volume without turning them into a
 * bundle of lines: they contribute a silhouette, not their every seam. The
 * capsid asks for creases, so it keeps its icosahedral faceting.
 */
export const renderOutline = (
  polys: Poly[],
  opts: {
    ry: number;
    rx: number;
    /** per material: show crease edges, and above what normal-angle */
    crease: Record<Poly["mat"], number | false>;
  },
): Op[] => {
  const { ry, rx, crease } = opts;

  const world = polys.map((p) => p.pts.map((v) => rotX(rotY(v, ry), rx)));
  const normals = world.map((w) =>
    norm(cross(sub(w[1], w[0]), sub(w[2], w[0]))),
  );
  const front = normals.map((n) => n[2] > 0.02);
  const depth = world.map((w) => w.reduce((a, v) => a + v[2], 0) / w.length);

  // Adjacency is built on the *local* coordinates so it is stable frame to
  // frame regardless of rotation.
  const vkey = (v: V3) =>
    `${v[0].toFixed(2)},${v[1].toFixed(2)},${v[2].toFixed(2)}`;
  const edgeFaces = new Map<string, number[]>();
  polys.forEach((p, fi) => {
    p.pts.forEach((v, i) => {
      const w = p.pts[(i + 1) % p.pts.length];
      const a = vkey(v);
      const b = vkey(w);
      const k = a < b ? `${a}|${b}` : `${b}|${a}`;
      const list = edgeFaces.get(k);
      if (list) list.push(fi);
      else edgeFaces.set(k, [fi]);
    });
  });

  const order = polys
    .map((_, i) => i)
    .filter((i) => front[i])
    .sort((a, b) => depth[a] - depth[b]);

  const pt = (v: V3) => `${v[0].toFixed(2)} ${(-v[1]).toFixed(2)}`;
  const ops: Op[] = [];

  for (const fi of order) {
    const w = world[fi];
    ops.push({
      kind: "fill",
      key: `f${polys[fi].key}`,
      d: w.map((v, i) => `${i === 0 ? "M" : "L"} ${pt(v)}`).join(" ") + " Z",
    });

    polys[fi].pts.forEach((v, i) => {
      const nextI = (i + 1) % polys[fi].pts.length;
      const a = vkey(v);
      const b = vkey(polys[fi].pts[nextI]);
      const k = a < b ? `${a}|${b}` : `${b}|${a}`;
      const adj = edgeFaces.get(k) ?? [];
      const other = adj.find((x) => x !== fi);

      let draw = false;
      if (other === undefined) {
        draw = true; // open boundary
      } else if (!front[other]) {
        draw = true; // silhouette
      } else {
        const th = crease[polys[fi].mat];
        if (th !== false) {
          const cosA = dot(normals[fi], normals[other]);
          const ang = (Math.acos(Math.max(-1, Math.min(1, cosA))) * 180) / Math.PI;
          // draw a shared crease once, from whichever face is nearer
          draw = ang > th && depth[fi] >= depth[other];
        }
      }

      if (draw) {
        ops.push({
          kind: "edge",
          mat: polys[fi].mat,
          key: `e${polys[fi].key}_${i}`,
          d: `M ${pt(w[i])} L ${pt(w[nextI])}`,
        });
      }
    });
  }

  return ops;
};

/* ---------------------------------------------------------------- builders */

const PHI = (1 + Math.sqrt(5)) / 2;

const ICO_V: V3[] = [
  [0, 1, PHI], [0, -1, PHI], [0, 1, -PHI], [0, -1, -PHI],
  [1, PHI, 0], [-1, PHI, 0], [1, -PHI, 0], [-1, -PHI, 0],
  [PHI, 0, 1], [-PHI, 0, 1], [PHI, 0, -1], [-PHI, 0, -1],
];

/** The 20 faces: every triple whose three edges are all one edge-length. */
const ICO_F: [number, number, number][] = (() => {
  const d2 = (a: V3, b: V3) =>
    (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2;
  const faces: [number, number, number][] = [];
  for (let i = 0; i < 12; i++)
    for (let j = i + 1; j < 12; j++)
      for (let k = j + 1; k < 12; k++) {
        if (
          Math.abs(d2(ICO_V[i], ICO_V[j]) - 4) < 1e-6 &&
          Math.abs(d2(ICO_V[j], ICO_V[k]) - 4) < 1e-6 &&
          Math.abs(d2(ICO_V[i], ICO_V[k]) - 4) < 1e-6
        )
          faces.push([i, j, k]);
      }
  return faces;
})();

/** Icosahedral capsid of the given circumradius, centred on the origin. */
export const capsidPolys = (r: number): Poly[] => {
  const k = r / Math.hypot(1, PHI);
  return ICO_F.map(([a, b, c], i) => {
    const tri: V3[] = [ICO_V[a], ICO_V[b], ICO_V[c]].map(
      (v) => [v[0] * k, v[1] * k, v[2] * k] as V3,
    );
    // wind so the normal points away from the centre
    const n = cross(sub(tri[1], tri[0]), sub(tri[2], tri[0]));
    const centroid: V3 = [
      (tri[0][0] + tri[1][0] + tri[2][0]) / 3,
      (tri[0][1] + tri[1][1] + tri[2][1]) / 3,
      (tri[0][2] + tri[1][2] + tri[2][2]) / 3,
    ];
    const pts = dot(n, centroid) > 0 ? tri : [tri[0], tri[2], tri[1]];
    return { pts, mat: "capsid" as const, key: `cap${i}` };
  });
};

/**
 * A surface of revolution through a profile of (radius, height) pairs — one
 * builder covers the tail tube and the nozzle cone, so they cannot drift apart.
 */
export const lathePolys = (
  profile: { r: number; y: number }[],
  mat: Poly["mat"],
  keyPrefix: string,
  seg = 18,
): Poly[] => {
  const out: Poly[] = [];

  // caps, so the surface is closed and the outline pass sees no open boundary
  const disc = (p: { r: number; y: number }, flip: boolean): V3[] => {
    const ring = Array.from({ length: seg }, (_, j) => {
      const t = (j / seg) * Math.PI * 2;
      return [p.r * Math.cos(t), p.y, p.r * Math.sin(t)] as V3;
    });
    return flip ? ring.reverse() : ring;
  };
  out.push({ pts: disc(profile[0], true), mat, key: `${keyPrefix}capA` });
  out.push({
    pts: disc(profile[profile.length - 1], false),
    mat,
    key: `${keyPrefix}capB`,
  });

  for (let i = 0; i < profile.length - 1; i++) {
    const a = profile[i];
    const b = profile[i + 1];
    for (let j = 0; j < seg; j++) {
      const t0 = (j / seg) * Math.PI * 2;
      const t1 = ((j + 1) / seg) * Math.PI * 2;
      out.push({
        pts: [
          [a.r * Math.cos(t0), a.y, a.r * Math.sin(t0)],
          [a.r * Math.cos(t1), a.y, a.r * Math.sin(t1)],
          [b.r * Math.cos(t1), b.y, b.r * Math.sin(t1)],
          [b.r * Math.cos(t0), b.y, b.r * Math.sin(t0)],
        ],
        mat,
        key: `${keyPrefix}${i}_${j}`,
      });
    }
  }
  return out;
};

/**
 * A tapered tube swept along a polyline — the tail spikes, so they are solid
 * geometry that occludes and is occluded, not strokes floating over the model.
 */
export const tubePolys = (
  path: V3[],
  radii: number[],
  mat: Poly["mat"],
  keyPrefix: string,
  seg = 6,
): Poly[] => {
  const out: Poly[] = [];

  // One ring per path point, built once and shared by both neighbouring
  // segments. Building a ring per segment would duplicate the vertices at each
  // joint, and the outline pass would then see two open boundaries there and
  // draw a seam across the middle of the tube.
  const rings: V3[][] = path.map((p, i) => {
    const prev = i > 0 ? norm(sub(p, path[i - 1])) : null;
    const next = i < path.length - 1 ? norm(sub(path[i + 1], p)) : null;
    const axis = norm(
      prev && next
        ? [prev[0] + next[0], prev[1] + next[1], prev[2] + next[2]]
        : (next ?? prev)!,
    );
    // a single global reference keeps the frame from twisting along the path
    const ref: V3 = Math.abs(axis[1]) < 0.9 ? [0, 1, 0] : [1, 0, 0];
    const u = norm(cross(axis, ref));
    const v = norm(cross(axis, u));
    const r = radii[i];

    return Array.from({ length: seg }, (_, j) => {
      const a = (j / seg) * Math.PI * 2;
      return [
        p[0] + r * (u[0] * Math.cos(a) + v[0] * Math.sin(a)),
        p[1] + r * (u[1] * Math.cos(a) + v[1] * Math.sin(a)),
        p[2] + r * (u[2] * Math.cos(a) + v[2] * Math.sin(a)),
      ] as V3;
    });
  });

  for (let i = 0; i < rings.length - 1; i++) {
    for (let j = 0; j < seg; j++) {
      const k = (j + 1) % seg;
      out.push({
        pts: [rings[i][j], rings[i][k], rings[i + 1][k], rings[i + 1][j]],
        mat,
        key: `${keyPrefix}${i}_${j}`,
      });
    }
  }

  // cap both ends so the tube is a closed solid and has no open boundary to
  // outline
  out.push({ pts: [...rings[0]].reverse(), mat, key: `${keyPrefix}capA` });
  out.push({ pts: rings[rings.length - 1], mat, key: `${keyPrefix}capB` });

  return out;
};
