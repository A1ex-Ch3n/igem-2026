import { Config } from "@remotion/cli/config";

// iGEM requires .mp4, 1080p or 4K, landscape, <= 500 MB, <= 120 s.
Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.setCodec("h264");
// CRF 20 keeps a 115 s 1080p30 render far under the 500 MB cap.
Config.setCrf(20);
