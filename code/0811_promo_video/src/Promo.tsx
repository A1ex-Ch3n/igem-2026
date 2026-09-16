import React from "react";
import { AbsoluteFill, Audio, staticFile } from "remotion";
import { Beat } from "./components/Beat";
import { Credits } from "./components/Credits";
import {
  CloseScene,
  GapScene,
  HookScene,
  MethodScene,
  MlLoopScene,
  StakesScene,
  TeamScene,
  WetlabScene,
} from "./scenes";
import { theme } from "./theme";

/**
 * Do NOT add an iGEM intro — iGEM inserts its own after moderator approval,
 * and the 120 s limit excludes it.
 *
 * Narration is the ElevenLabs recording; timeline.ts is timed against it.
 * The file carries ~10 s of trailing silence after the last word at 1:44.9,
 * which the 1:53 composition simply runs past.
 */
export const Promo: React.FC = () => (
  <AbsoluteFill style={{ backgroundColor: theme.bg }}>
    <Audio src={staticFile("audio/narration.wav")} />
    <Beat id="hook">
      <HookScene />
    </Beat>
    <Beat id="stakes">
      <StakesScene />
    </Beat>
    <Beat id="gap">
      <GapScene />
    </Beat>
    <Beat id="team">
      <TeamScene />
    </Beat>
    <Beat id="method">
      <MethodScene />
    </Beat>
    <Beat id="wetlab">
      <WetlabScene />
    </Beat>
    <Beat id="mlloop">
      <MlLoopScene />
    </Beat>
    <Beat id="close">
      <CloseScene />
    </Beat>
    <Credits />
  </AbsoluteFill>
);
