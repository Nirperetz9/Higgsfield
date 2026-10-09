#!/usr/bin/env bash
# Film finishing pass for MiniMax clips: softens the "AI sharpness", adds halation,
# 35mm-style grain, optional LUT, 24fps. Usage:
#   ./film_finish.sh input.mp4 output.mp4 [LUT.cube|none] [scope]
# "scope" as 4th arg adds 2.39:1 letterbox bars (Hollywood widescreen).
# Default LUT is none, because the keyframes were already graded with the LUT
# (the video inherits it). Pass LANA_WarmPrint35_60.cube only if a clip drifted.
set -euo pipefail
IN="$1"; OUT="$2"; LUT="${3:-none}"; SCOPE="${4:-}"
BARS=""
[ "$SCOPE" = "scope" ] && BARS=",drawbox=x=0:y=0:w=iw:h=(ih-iw/2.39)/2:color=black:t=fill,drawbox=x=0:y=ih-(ih-iw/2.39)/2:w=iw:h=(ih-iw/2.39)/2:color=black:t=fill"
LUTF=""
[ "$LUT" != "none" ] && LUTF="lut3d='${LUT}',"
ffmpeg -y -i "$IN" -filter_complex "
[0:v]${LUTF}format=gbrp,split=3[base][soft][glow];
[soft]gblur=sigma=0.9[softb];
[base][softb]blend=all_mode=normal:all_opacity=0.55[softened];
[glow]curves=all='0/0 0.70/0 1/0.9',gblur=sigma=14,colorchannelmixer=rr=1.0:gg=0.35:bb=0.12[halo];
[softened][halo]blend=all_mode=screen:all_opacity=0.22[haloed];
[haloed]noise=alls=7:allf=t+u,eq=saturation=0.97,fps=24${BARS},format=yuv420p[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -crf 16 -preset slow -c:a copy "$OUT"
