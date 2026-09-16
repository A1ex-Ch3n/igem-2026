import React from "react";
import { AbsoluteFill } from "remotion";
import cds from "./data/cds.json";
import { DrawPath, Note } from "./components/Draw";
import { GenomeTrack } from "./components/GenomeTrack";
import { Grid } from "./components/Grid";
import { Membrane, OAntigenField, project } from "./components/Membrane3D";
import { PHAGE_TIP_DROP, Phage } from "./components/Phage";
import { H, SAFE_MARGIN, W, theme } from "./theme";

/**
 * Thumbnail candidates.
 *
 * A thumbnail is seen small and alone, so these are composed rather than grabbed
 * from the film: one subject, few words, and the title carried by the image
 * instead of by narration. iGEM's only stated constraint is an image under 4 MB.
 *
 * Every variant is drawn by the same components as the video, so nothing here
 * is a separate asset to license or keep in sync.
 */

export type ThumbVariant =
  | "hero"
  | "adsorption"
  | "genome"
  | "type"
  | "timemachine";

const TITLE = "Rebuilding the ancestors of a phage tail spike";

const Sheet: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <svg
    viewBox={`0 0 ${W} ${H}`}
    style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }}
  >
    {children}
  </svg>
);

const Tag: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div
    style={{
      fontFamily: theme.fontMono,
      fontSize: 30,
      letterSpacing: 3.4,
      textTransform: "uppercase",
      color: theme.accent,
    }}
  >
    {children}
  </div>
);

const Head: React.FC<{ size?: number; children: React.ReactNode }> = ({
  size = 92,
  children,
}) => (
  <div
    style={{
      fontFamily: theme.fontDisplay,
      fontSize: size,
      fontWeight: 600,
      letterSpacing: -1.6,
      lineHeight: 1.1,
      color: theme.text,
    }}
  >
    {children}
  </div>
);

const Stack: React.FC<{
  children: React.ReactNode;
  width?: number;
  align?: "flex-start" | "center";
}> = ({ children, width = 1050, align = "flex-start" }) => (
  <div
    style={{
      position: "absolute",
      inset: SAFE_MARGIN,
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: align,
      gap: 30,
      width,
      textAlign: align === "center" ? "center" : "left",
    }}
  >
    {children}
  </div>
);

export const Thumbnail: React.FC<{ variant: ThumbVariant }> = ({ variant }) => {
  if (variant === "adsorption") {
    const ROWS = [380, 460, 560, 700, 900, 1200, 1700, 2600];
    const Z = 900;
    const ground = project(0, 0, Z);
    const pScale = ground.s * 2.1;
    return (
      <AbsoluteFill style={{ backgroundColor: theme.bg }}>
        <Sheet>
          <Membrane rows={ROWS} delay={0} />
          <OAntigenField
            rows={ROWS.slice(0, 6)}
            delay={0}
            cleaveAt={{ x: 0, z: Z, r: 300 }}
            cleaveProgress={1}
          />
          <Phage
            x={ground.x}
            y={ground.y - PHAGE_TIP_DROP * pScale}
            scale={pScale}
            delay={0}
            splay={1}
          />
        </Sheet>
        <Stack width={880}>
          <Tag>Phagenomics · iGEM 2026</Tag>
          <Head size={72}>
            Host range is decided
            <br />
            in the first seconds
            <br />
            of contact.
          </Head>
        </Stack>
      </AbsoluteFill>
    );
  }

  if (variant === "genome") {
    return (
      <AbsoluteFill>
        <Grid />
        <Sheet>
          <GenomeTrack
            x={140}
            y={700}
            width={1640}
            height={40}
            delay={0}
            spread={0}
            only={["CDS_0011"]}
          />
          <Note
            x={140}
            y={840}
            text={`9-2-1 Φ8 · ${cds.length.toLocaleString()} bp · ${cds.genes.length} CDS · our own assembly`}
            delay={0}
            size={26}
          />
        </Sheet>
        <Stack width={1500}>
          <Tag>Phagenomics · iGEM 2026</Tag>
          <Head size={80}>
            One protein decides
            <br />
            which bacteria a phage can kill.
          </Head>
        </Stack>
      </AbsoluteFill>
    );
  }

  if (variant === "type") {
    return (
      <AbsoluteFill>
        <Grid />
        <Sheet>
          <Phage x={1560} y={620} scale={0.95} delay={0} splay={1} />
        </Sheet>
        <Stack width={1180}>
          <Tag>Phagenomics · iGEM 2026</Tag>
          <Head size={86}>{TITLE}</Head>
          <div
            style={{
              fontFamily: theme.fontMono,
              fontSize: 28,
              color: theme.textDim,
              letterSpacing: 0.6,
            }}
          >
            Claremont, California
          </div>
        </Stack>
      </AbsoluteFill>
    );
  }

  if (variant === "timemachine") {
    return (
      <AbsoluteFill>
        <Grid />
        <Sheet>
          <DrawPath d="M 240 800 L 1720 800" delay={0} speed={1} />
          {[300, 640, 980, 1320, 1560].map((x) => (
            <DrawPath
              key={x}
              d={`M ${x} 786 L ${x} 814`}
              delay={0}
              speed={1}
              stroke={theme.strokeDim}
            />
          ))}
          <Note x={300} y={864} text="deep past" delay={0} anchor="middle" size={24} />
          <Note x={1560} y={864} text="today" delay={0} anchor="middle" size={24} />
          <g transform="translate(760 800)">
            <circle r={16} fill="none" stroke={theme.accent} strokeWidth={4} />
            <circle r={34} fill="none" stroke={theme.accentDim} strokeWidth={1.6} />
          </g>
          <Phage x={1500} y={330} scale={0.62} delay={0} splay={1} />
        </Sheet>
        <Stack width={1200}>
          <Tag>Phagenomics · iGEM 2026</Tag>
          <Head size={112}>This is a time machine.</Head>
          <div
            style={{
              fontFamily: theme.fontDisplay,
              fontSize: 36,
              color: theme.textDim,
            }}
          >
            Reconstructing the ancestors of a phage tail spike.
          </div>
        </Stack>
      </AbsoluteFill>
    );
  }

  // hero
  return (
    <AbsoluteFill>
      <Grid />
      <Sheet>
        <Phage x={1420} y={520} scale={1.75} delay={0} splay={1} />
        <Note
          x={1420}
          y={930}
          text="podovirus · 9-2-1 Φ8"
          delay={0}
          anchor="middle"
          size={26}
        />
      </Sheet>
      <Stack width={1000}>
        <Tag>Phagenomics · iGEM 2026</Tag>
        <Head size={96}>
          Phages are viruses
          <br />
          that hunt bacteria.
        </Head>
        <div
          style={{
            fontFamily: theme.fontDisplay,
            fontSize: 36,
            color: theme.textDim,
          }}
        >
          We are learning to aim them.
        </div>
      </Stack>
    </AbsoluteFill>
  );
};

export const THUMB_VARIANTS: ThumbVariant[] = [
  "hero",
  "adsorption",
  "genome",
  "type",
  "timemachine",
];
