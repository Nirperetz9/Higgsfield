#!/usr/bin/env bash
# Applies the LUT to every keyframe PNG/JPG in a folder before uploading to MiniMax.
#   ./grade_keyframes.sh ./keyframes ./keyframes_graded [LUT.cube]
set -euo pipefail
IN="$1"; OUT="$2"; LUT="${3:-$(dirname "$0")/../luts/LANA_WarmPrint35_full.cube}"
mkdir -p "$OUT"
for f in "$IN"/*.{png,jpg,jpeg}; do
  [ -e "$f" ] || continue
  ffmpeg -loglevel error -y -i "$f" -vf "lut3d='$LUT'" "$OUT/$(basename "${f%.*}").png"
  echo "graded $(basename "$f")"
done
