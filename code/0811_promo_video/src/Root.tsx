import { Composition } from "remotion";
import { Promo } from "./Promo";
import { THUMB_VARIANTS, Thumbnail } from "./Thumbnail";
import { DURATION_IN_FRAMES, FPS } from "./timeline";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Promo"
        component={Promo}
        durationInFrames={DURATION_IN_FRAMES}
        fps={FPS}
        width={1920}
        height={1080}
      />
      {/* One composition per thumbnail candidate. They are static — the reveal
          animations all run from delay 0 — so any frame renders the finished
          image; scripts/thumbnails.sh grabs frame 60 to be safe. */}
      {THUMB_VARIANTS.map((v) => (
        <Composition
          key={v}
          id={`Thumb-${v}`}
          component={Thumbnail}
          defaultProps={{ variant: v }}
          durationInFrames={90}
          fps={FPS}
          width={1920}
          height={1080}
        />
      ))}
    </>
  );
};
