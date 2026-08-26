#!/usr/bin/env python3
"""
export_slides.py — crop chosen frames into clean slide images.

Usage:
  python3 export_slides.py FRAMES_DIR OUT_IMAGES_DIR MAPPING.txt
        [--top 62] [--bottom 440] [--right 743]
        [--overlay-x 655 --overlay-y 372]      # bottom-right webcam/presenter box; omit to disable
        [--navbar 25]                          # extra rows to trim when top strip is light (Moodle/UNSW nav)

MAPPING.txt: one "frame_stem  output_name" per line, e.g.
  f_0077   08_agile_manifesto
  # lines starting with # are ignored; frame_stem may be a path to any jpg

Removes: OS menu bar + browser tabs (--top), Dock (--bottom), area right of the
browser window (--right), presenter overlay (filled with median colour sampled
just left of it), and — only when the first rows are near-white — a site nav bar.
Coordinates default to an 854x480 frame; measure yours first (see SKILL.md).
"""
import argparse, os, sys
import numpy as np
from PIL import Image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("frames"); ap.add_argument("out"); ap.add_argument("mapping")
    ap.add_argument("--top", type=int, default=62)
    ap.add_argument("--bottom", type=int, default=440)
    ap.add_argument("--right", type=int, default=743)
    ap.add_argument("--overlay-x", type=int, default=655)
    ap.add_argument("--overlay-y", type=int, default=372)
    ap.add_argument("--no-overlay", action="store_true")
    ap.add_argument("--navbar", type=int, default=25)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    n = 0
    for line in open(a.mapping):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        stem, name = line.split()[:2]
        src = stem if stem.endswith(".jpg") else os.path.join(a.frames, stem + ".jpg")
        if not os.path.exists(src):
            print("MISSING", src); continue
        arr = np.array(Image.open(src).convert("RGB"))
        if not a.no_overlay:
            ox, oy = a.overlay_x, a.overlay_y
            col = np.median(arr[oy:a.bottom, ox - 40:ox - 4].reshape(-1, 3), axis=0)
            arr[oy:, ox:] = col
        im = Image.fromarray(arr).crop((0, a.top, a.right, a.bottom))
        g = np.array(im.convert("L"))
        if a.navbar and g[2:20, :].mean() > 235:   # light site nav bar present
            im = im.crop((0, a.navbar, im.width, im.height))
        im.save(os.path.join(a.out, name + ".jpg"), quality=88); n += 1
    print(f"exported {n} images to {a.out}")


if __name__ == "__main__":
    main()
