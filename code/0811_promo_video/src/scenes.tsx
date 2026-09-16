import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import cds from "./data/cds.json";
import { Dot, DrawPath, Note } from "./components/Draw";
import { GenomeTrack, ScaleBar, useWindow } from "./components/GenomeTrack";
import { Grid } from "./components/Grid";
import { Membrane, OAntigenField, project } from "./components/Membrane3D";
import { PHAGE_TIP_DROP, Phage } from "./components/Phage";
import { Label, Stage, Statement } from "./components/Type";
import { beatFrames } from "./timeline";
import { H, W, theme } from "./theme";

const dur = (id: string) => beatFrames(id).durationInFrames;

const Sheet: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg
    viewBox={`0 0 ${W} ${H}`}
    style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }}
  >
    {children}
  </svg>
);

/* ------------------------------------------------------------------ 0 hook */

export const HookScene: React.FC = () => (
  <AbsoluteFill>
    <Grid />
    <Sheet>
      {/* free virion: fibres still part-folded against the capsid */}
      <Phage x={1380} y={440} scale={1.3} delay={6} splay={1} />
      <Note
        x={1380}
        y={800}
        text="podovirus · 9-2-1 Φ8"
        delay={88}
        anchor="middle"
        size={22}
      />
    </Sheet>
    <Stage justify="center">
      <Label>Phagenomics · iGEM 2026</Label>
      <Statement size={88}>
        Phages are viruses
        <br />
        that hunt bacteria.
      </Statement>
      <Statement size={38} delay={44} color={theme.textDim}>
        They have been doing it for billions of years.
      </Statement>
    </Stage>
  </AbsoluteFill>
);

/* ---------------------------------------------------------------- 1 stakes */

/**
 * A field of bacteria with exactly one picked out: the strain actually making
 * someone sick. Nothing is struck through — the beat is that a phage has to hit
 * that one and usually cannot, so showing bacteria dying would invert the line
 * it sits under. Metaphor, not measurement: no axes, no numbers.
 */
export const StakesScene: React.FC = () => {
  const frame = useCurrentFrame();
  const cols = 22;
  const rows = 7;
  const TARGET = 74;
  const opts = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

  // a search pass across the field — the strain has to be found before it can
  // be treated, and only one of them is the one
  const sweepX = interpolate(frame, [90, 300], [-40, 780], opts);
  const targetCx = (TARGET % cols) * 34 + 8;

  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        <g transform="translate(1080 300)">
          <DrawPath
            d={`M ${sweepX} -34 L ${sweepX} ${rows * 46 + 22}`}
            delay={90}
            speed={10}
            stroke={theme.accentDim}
            width={1.4}
          />

          {Array.from({ length: cols * rows }).map((_, i) => {
            const cx = (i % cols) * 34;
            const cy = Math.floor(i / cols) * 46;
            const appear = interpolate(frame, [10 + i * 1.2, 26 + i * 1.2], [0, 1], opts);
            const isTarget = i === TARGET;
            const found = isTarget && sweepX > targetCx;
            return (
              <g key={i} opacity={appear}>
                <rect
                  x={cx}
                  y={cy}
                  width={16}
                  height={26}
                  rx={8}
                  fill="none"
                  stroke={found ? theme.accent : theme.strokeDim}
                  strokeWidth={found ? 2.4 : 1.5}
                />
              </g>
            );
          })}

          {/* ring and leader on the one that matters */}
          {(() => {
            const cx = (TARGET % cols) * 34 + 8;
            const cy = Math.floor(TARGET / cols) * 46 + 13;
            return (
              <g>
                <DrawPath
                  d={`M ${cx} ${cy - 34} A 34 34 0 1 1 ${cx - 0.01} ${cy - 34}`}
                  delay={300}
                  speed={26}
                  stroke={theme.accent}
                  width={1.5}
                />
                {/* leader exits below the field so it never crosses the grid */}
                <DrawPath
                  d={`M ${cx} ${cy + 34} L ${cx} 344`}
                  delay={326}
                  speed={12}
                  stroke={theme.accent}
                  width={1.2}
                />
                <Note
                  x={cx}
                  y={378}
                  text="this one"
                  delay={338}
                  anchor="middle"
                  color={theme.accent}
                  size={24}
                />
              </g>
            );
          })()}
        </g>
        <Note
          x={1080}
          y={740}
          text="schematic — not experimental data"
          delay={360}
          size={20}
        />
      </Sheet>
      <Stage justify="center">
        <Statement size={58}>Antibiotic resistance is rising.</Statement>
        <Statement size={58} delay={90} color={theme.accent}>
          Infections we could once cure
          <br />
          are becoming untreatable.
        </Statement>
        <Statement size={34} delay={280} color={theme.textDim}>
          Phages are one way to fight back —
          <br />
          but only if a phage can infect the exact
          <br />
          bacterium making someone sick.
        </Statement>
      </Stage>
    </AbsoluteFill>
  );
};

/* ------------------------------------------------------------------- 2 gap */

/**
 * Adsorption as our phage actually does it: the tail spike (CDS_0011) is a
 * β-helix depolymerase and the receptor is LPS O-antigen sugar, so the spikes
 * splay, cleave the sugar chains, and the particle settles onto the membrane.
 * Not a landing — an enzymatic descent.
 */
export const GapScene: React.FC = () => {
  const frame = useCurrentFrame();
  const total = dur("gap");
  const opts = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

  // near row sits below the frame edge so the membrane fills the bottom
  const ROWS = [380, 460, 560, 700, 900, 1200, 1700, 2600];
  const Z = 900; // the particle's depth

  const ground = project(0, 0, Z); // membrane under the particle
  const pScale = ground.s * 1.7;
  const tipDrop = PHAGE_TIP_DROP * pScale;
  const sugarTop = ground.y - 34 * ground.s;

  const phageY = interpolate(
    frame,
    [24, 170, 250, 330],
    [-160, sugarTop - tipDrop, sugarTop - tipDrop, ground.y - tipDrop],
    opts,
  );
  const splay = interpolate(frame, [150, 250], [0.15, 1], opts);
  const cleave = interpolate(frame, [240, 330], [0, 1], opts);
  const boxIn = interpolate(frame, [total - 240, total - 190], [0, 1], opts);

  return (
    <AbsoluteFill style={{ backgroundColor: theme.bg }}>
      <Sheet>
        {/* the membrane is the ground plane — no flat grid behind it, or the
            scene reads as two spaces at once */}
        <Membrane rows={ROWS} delay={8} />
        <OAntigenField
          rows={ROWS.slice(0, 6)}
          delay={20}
          cleaveAt={{ x: 0, z: Z, r: 300 }}
          cleaveProgress={cleave}
        />
        <Note
          x={40}
          y={1012}
          text="host cell surface · LPS O-antigen"
          delay={90}
          size={20}
        />

        <Phage
          x={ground.x}
          y={phageY}
          scale={pScale}
          delay={20}
          splay={splay}
        />

        {/* what the spike is doing, stated once */}
        <g opacity={interpolate(frame, [250, 290], [0, 1], opts)}>
          <Note
            x={1104}
            y={1024}
            text="β-helix depolymerase cleaves the O-antigen"
            delay={252}
            size={21}
            color={theme.accent}
          />
        </g>

        {/* callout, kept above the sugar layer where the ground is clean */}
        <g opacity={boxIn}>
          <DrawPath
            d={`M ${ground.x + 150} ${phageY - 40} L ${ground.x + 330} ${phageY - 150}`}
            delay={total - 230}
            speed={12}
            stroke={theme.accent}
            width={1.2}
          />
          <Note
            x={ground.x + 346}
            y={phageY - 168}
            text="which residues set the host range?"
            delay={total - 216}
            color={theme.accent}
            size={26}
          />
          <Note
            x={ground.x + 346}
            y={phageY - 130}
            text="we do not know yet"
            delay={total - 190}
            size={22}
          />
        </g>
      </Sheet>
      <Stage justify="flex-start">
        <Label>schematic — not experimental data</Label>
        <Statement size={50}>
          Host range is decided in the
          <br />
          first seconds of contact.
        </Statement>
      </Stage>
    </AbsoluteFill>
  );
};

/* ------------------------------------------------------------------ 3 team */

/** Deterministic scatter — Math.random would resample every frame and flicker. */
const rnd = (i: number) => {
  const x = Math.sin(i * 12.9898) * 43758.5453;
  return x - Math.floor(x);
};

/**
 * A plaque assay, played out: bacterial lawn fills the plate, phage lands, and
 * clearings open where it lysed the lawn. This is literally how the phages in
 * this project were isolated, so the beat shows the work rather than captioning
 * it.
 */
export const TeamScene: React.FC = () => {
  const frame = useCurrentFrame();
  const opts = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

  const CX = 1420;
  const CY = 520;
  const R = 250;

  const PLAQUES = [
    { x: -92, y: -54, r: 54 },
    { x: 66, y: 22, r: 68 },
    { x: -24, y: 128, r: 42 },
  ];

  const lawn = Array.from({ length: 260 }).map((_, i) => {
    const rr = R * 0.94 * Math.sqrt(rnd(i));
    const a = 2 * Math.PI * rnd(i + 977);
    return { x: rr * Math.cos(a), y: rr * Math.sin(a), i };
  });

  const grow = interpolate(frame, [150, 250], [0, 1], opts);

  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        <g transform={`translate(${CX} ${CY})`}>
          <DrawPath
            d={`M 0 ${-R} A ${R} ${R} 0 1 1 -0.01 ${-R}`}
            delay={10}
            speed={34}
            stroke={theme.strokeDim}
          />

          {lawn.map(({ x, y, i }) => {
            const appear = interpolate(frame, [24 + i * 0.35, 40 + i * 0.35], [0, 1], opts);
            const inPlaque = PLAQUES.some(
              (p) => Math.hypot(x - p.x, y - p.y) < p.r * grow,
            );
            return (
              <circle
                key={i}
                cx={x}
                cy={y}
                r={2.6}
                fill="none"
                stroke={theme.strokeDim}
                strokeWidth={1.2}
                opacity={appear * (inPlaque ? 0 : 0.9)}
              />
            );
          })}

          {PLAQUES.map((p, i) => (
            <circle
              key={i}
              cx={p.x}
              cy={p.y}
              r={p.r * grow}
              fill="none"
              stroke={theme.accent}
              strokeWidth={1.6}
              opacity={grow}
            />
          ))}

          <Note
            x={0}
            y={R + 52}
            text="plaque assay — each clearing is one phage"
            delay={256}
            anchor="middle"
            size={21}
          />
        </g>
      </Sheet>
      <Stage justify="center">
        <Label>Claremont, California</Label>
        <Statement size={88}>We are Phagenomics.</Statement>
        <Statement size={34} delay={70} color={theme.textDim}>
          We collected our phages from the water and soil around us,
          <br />
          along with the bacteria they infect — and sequenced them ourselves.
        </Statement>
      </Stage>
    </AbsoluteFill>
  );
};

/* ---------------------------------------------------------------- 4 method */

export const MethodScene: React.FC = () => (
  <AbsoluteFill>
    <Grid />
    <Sheet>
      {/* On the whole genome only the landmarks the eye can find at this scale.
          The tail genes are labelled in the zoom that follows. */}
      <GenomeTrack
        x={140}
        y={560}
        width={1640}
        delay={14}
        spread={70}
        only={["CDS_0011", "CDS_0017", "CDS_0020", "CDS_0078"]}
      />
      <ScaleBar
        x={140}
        y={700}
        width={1640}
        window={[0, cds.length]}
        bp={10000}
        delay={130}
      />
      <Note
        x={140}
        y={800}
        text={`9-2-1 Φ8 · ${cds.length.toLocaleString()} bp · ${cds.genes.length} CDS · our assembly, Pharokka annotation`}
        delay={150}
        size={22}
      />
    </Sheet>
    <Stage justify="flex-start">
      <Label>the genome we sequenced</Label>
      <Statement size={46}>
        We treat host range as an evolutionary question.
      </Statement>
    </Stage>
  </AbsoluteFill>
);

/* ---------------------------------------------------------------- 5 wetlab */

/**
 * Left: the window flies from the whole genome into the tail module, so the
 * tail spike the narration names is located in the real annotation.
 * Right: the construct we actually ordered — CDS_0011 residues 305-941 with an
 * N-terminal His6. Those numbers are real. The small tree beside it is marked
 * schematic, because no reconstructed tree has been published yet and an
 * unmarked one would read as a result we do not have.
 */
export const WetlabScene: React.FC = () => {
  // Fractions of the beat, not fixed frames: when the VO lands and this beat
  // changes length, the fly-in still finishes about a fifth of the way in.
  const total = dur("wetlab");
  const win = useWindow(
    [0, cds.length],
    cds.tailZoom as [number, number],
    Math.round(total * 0.02),
    Math.round(total * 0.18),
  );

  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        <GenomeTrack
          window={win}
          x={140}
          y={430}
          width={1640}
          delay={0}
          spread={30}
        />

        {/* construct bar */}
        <g transform="translate(140 640)">
          <Note x={0} y={-24} text="the construct we ordered" size={22} delay={130} />
          <DrawPath
            d="M 0 0 L 740 0 L 740 52 L 0 52 Z"
            delay={140}
            speed={26}
            stroke={theme.strokeDim}
          />
          <DrawPath
            d="M 236 0 L 740 0 L 740 52 L 236 52 Z"
            delay={160}
            speed={22}
            stroke={theme.accent}
            width={theme.hairBold}
          />
          <Note x={0} y={92} text="1" delay={180} size={20} />
          <Note x={236} y={92} text="305" delay={180} size={20} color={theme.accent} />
          <Note x={740} y={92} text="941 aa" delay={180} anchor="end" size={20} />
          <Note
            x={0}
            y={128}
            text="CDS_0011 tail spike · N-terminal His6"
            delay={196}
            size={20}
          />
        </g>

        {/* Schematic ancestral tree, drawn the way the analysis runs: today's
            sequences first, then merged backwards to the ancestor. Marked
            schematic — no reconstructed tree has been published yet, and an
            unmarked one would read as a result we do not have. */}
        <g transform="translate(1180 620)">
          <Note
            x={0}
            y={-40}
            text="ancestral reconstruction — schematic"
            size={20}
            delay={200}
            color={theme.strokeDim}
          />
          {[10, 70, 170, 230].map((y, i) => (
            <Dot
              key={y}
              cx={300}
              cy={y}
              r={7}
              delay={206 + i * 5}
              stroke={theme.stroke}
            />
          ))}
          <Note x={332} y={126} text="today" delay={214} size={20} />
          <DrawPath
            d="M 300 10 L 190 10 M 300 70 L 190 70 M 300 170 L 190 170 M 300 230 L 190 230"
            delay={228}
            speed={12}
          />
          <DrawPath d="M 190 10 L 190 70 M 190 170 L 190 230" delay={240} speed={10} />
          <DrawPath d="M 190 40 L 90 40 M 190 200 L 90 200" delay={250} speed={10} />
          <DrawPath d="M 90 40 L 90 200" delay={260} speed={10} />
          <DrawPath d="M 90 120 L 0 120" delay={270} speed={10} stroke={theme.accent} />
          <Dot cx={0} cy={120} r={9} delay={280} stroke={theme.accent} width={2.4} />
          <Note x={-16} y={172} text="ancestor" delay={286} anchor="end" size={20} color={theme.accent} />
        </g>
      </Sheet>
      <Stage justify="flex-start">
        <Label>tail / receptor-binding module</Label>
        <Statement size={42}>
          We build those ancestral proteins
          <br />
          and measure how tightly each one binds.
        </Statement>
      </Stage>
    </AbsoluteFill>
  );
};

/* ---------------------------------------------------------------- 6 mlloop */

export const MlLoopScene: React.FC = () => {
  const frame = useCurrentFrame();
  const opts = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
  const nodes = [
    ["ancestral", "sequences"],
    ["binding", "measurements"],
    ["model"],
    ["next", "design"],
  ];

  // a single measurement travelling the loop, so the diagram runs once on screen
  const tokenOn = frame > 78 && frame < 178;
  const forward = frame <= 140;
  const tx = forward
    ? interpolate(frame, [80, 140], [320, 1520], opts)
    : interpolate(frame, [140, 176], [1520, 320], opts);
  const back = interpolate(frame, [140, 176], [0, 1], opts);
  const ty = forward ? 560 : 668 + 4 * 172 * back * (1 - back);

  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        {nodes.map((lines, i) => {
          const x = 320 + i * 400;
          const r = 104;
          return (
            <g key={i}>
              <DrawPath
                d={`M ${x} ${560 - r} A ${r} ${r} 0 1 1 ${x - 0.01} ${560 - r}`}
                delay={i * 16}
                speed={26}
                stroke={i === 3 ? theme.accent : theme.stroke}
              />
              {lines.map((line, j) => (
                <Note
                  key={line}
                  x={x}
                  y={560 + (j - (lines.length - 1) / 2) * 28 + 8}
                  text={line}
                  delay={i * 16 + 18}
                  anchor="middle"
                  color={theme.text}
                  size={23}
                />
              ))}
              {i < 3 ? (
                <DrawPath
                  d={`M ${x + r + 14} 560 L ${x + 400 - r - 14} 560 M ${x + 400 - r - 32} 550 L ${x + 400 - r - 14} 560 L ${x + 400 - r - 32} 570`}
                  delay={i * 16 + 26}
                  speed={12}
                  stroke={theme.strokeDim}
                />
              ) : null}
            </g>
          );
        })}
        {/* feedback arc closing the loop */}
        <DrawPath
          d="M 1520 668 C 1520 840, 320 840, 320 668"
          delay={70}
          speed={40}
          stroke={theme.accent}
          width={1.5}
          dash="8 8"
        />
        {tokenOn ? (
          <circle cx={tx} cy={ty} r={9} fill={theme.accent} opacity={0.9} />
        ) : null}
        <Note
          x={920}
          y={906}
          text="each round narrows what to change next"
          delay={116}
          anchor="middle"
          size={22}
          color={theme.accent}
        />
      </Sheet>
      <Stage justify="flex-start">
        <Label>the loop</Label>
      </Stage>
    </AbsoluteFill>
  );
};

/* ----------------------------------------------------------------- 7 close */

export const CloseScene: React.FC = () => {
  const frame = useCurrentFrame();
  const marker = interpolate(frame, [40, 150, 230, 330], [1560, 300, 300, 1700], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        <DrawPath d="M 240 760 L 1720 760" delay={16} speed={30} />
        {[300, 640, 980, 1320, 1560].map((x, i) => (
          <g key={x}>
            <DrawPath
              d={`M ${x} 746 L ${x} 774`}
              delay={30 + i * 4}
              speed={8}
              stroke={theme.strokeDim}
            />
          </g>
        ))}
        <Note x={300} y={824} text="deep past" delay={60} anchor="middle" size={20} />
        <Note x={1560} y={824} text="today" delay={60} anchor="middle" size={20} />
        <Note x={1700} y={824} text="next" delay={240} anchor="middle" size={20} color={theme.accent} />
        <g transform={`translate(${marker} 760)`}>
          <circle r={12} fill="none" stroke={theme.accent} strokeWidth={3} />
          <circle r={26} fill="none" stroke={theme.accentDim} strokeWidth={1.2} />
        </g>
      </Sheet>
      <Stage justify="center">
        <Statement size={92}>This is a time machine.</Statement>
        <Statement size={36} delay={70} color={theme.textDim}>
          We go backward to find out what evolution learned,
          <br />
          and we run it forward to design the next generation of phages.
        </Statement>
      </Stage>
    </AbsoluteFill>
  );
};
