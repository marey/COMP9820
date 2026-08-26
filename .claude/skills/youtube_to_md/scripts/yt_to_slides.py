#!/usr/bin/env python3
"""
yt_to_slides.py — YouTube lecture -> transcript + de-duplicated slide frames + contact sheets.

Usage:
  python3 yt_to_slides.py URL OUT_DIR [--work WORK_DIR] [--video existing.mp4]
                          [--start SEC] [--interval SEC] [--height 480] [--langs "en,en-orig"]

Steps (each idempotent; skips what already exists):
  1. subtitles  -> OUT_DIR/transcript.en.json3 + OUT_DIR/transcript.txt  ([hh:mm:ss] text)
  2. video      -> WORK_DIR/video.mp4 (<= --height p, default 480p)
  3. frames     -> WORK_DIR/frames/f_NNNN.jpg every --interval s (default 10), starting at --start
  4. dedupe     -> near-identical consecutive frames removed (whole-frame 4% threshold)
  5. sheets     -> WORK_DIR/sheets/s_NN.jpg  2x3 labelled contact sheets (filename + timestamp)

Then: view the sheets, pick frames, and run export_slides.py.
Timestamp of frame f_NNNN = start + (NNNN-1)*interval seconds.
Dependencies: yt-dlp, ffmpeg, Pillow.
"""
import argparse, glob, json, os, re, subprocess, sys
from PIL import Image, ImageChops, ImageDraw


def sh(cmd, **kw):
    print("+", " ".join(cmd), flush=True)
    return subprocess.run(cmd, check=True, **kw)


def ts(sec):
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def step_subtitles(url, out, langs):
    txt = os.path.join(out, "transcript.txt")
    if os.path.exists(txt):
        print("transcript exists, skip"); return
    sh(["yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
        "--sub-langs", langs, "--sub-format", "json3/vtt",
        "-o", os.path.join(out, "transcript.%(ext)s"), url])
    # prefer transcript.en.json3 over transcript.en-orig.json3 (same content)
    cands = sorted(glob.glob(os.path.join(out, "transcript.*.json3")), key=len)
    if not cands:
        sys.exit("no json3 subtitles downloaded")
    keep = cands[0]
    for c in cands[1:]:
        os.remove(c)  # en-orig etc. are duplicates of en
    d = json.load(open(keep))
    lines = []
    for ev in d.get("events", []):
        if "segs" not in ev:
            continue
        t = ev["tStartMs"] // 1000
        s = "".join(x.get("utf8", "") for x in ev["segs"]).replace("\n", " ").strip()
        if s:
            lines.append(f"[{ts(t)}] {s}")
    open(txt, "w").write("\n".join(lines))
    print(f"transcript: {len(lines)} lines")


def step_video(url, work, height, video):
    if video:
        return video
    dst = os.path.join(work, "video.mp4")
    if os.path.exists(dst):
        print("video exists, skip"); return dst
    sh(["yt-dlp", "-f", f"bv*[height<={height}]/b[height<={height}]/worst", "--no-playlist",
        "-o", os.path.join(work, "video.%(ext)s"), url])
    got = glob.glob(os.path.join(work, "video.*"))
    if not got:
        sys.exit("video download failed")
    if got[0] != dst:
        os.rename(got[0], dst)
    return dst


def step_frames(video, work, start, interval):
    fdir = os.path.join(work, "frames")
    if os.path.isdir(fdir) and glob.glob(os.path.join(fdir, "*.jpg")):
        print("frames exist, skip"); return fdir
    os.makedirs(fdir, exist_ok=True)
    sh(["ffmpeg", "-loglevel", "error", "-ss", str(start), "-i", video,
        "-vf", f"fps=1/{interval}", "-q:v", "3", os.path.join(fdir, "f_%04d.jpg")])
    files = sorted(glob.glob(os.path.join(fdir, "*.jpg")))
    prev = None; kept = 0
    for f in files:
        im = Image.open(f).convert("L").resize((64, 36))
        if prev is not None:
            n = sum(ImageChops.difference(im, prev).histogram()[25:])
            if n < 64 * 36 * 0.04:
                os.remove(f); continue
        kept += 1; prev = im
    print(f"frames: {len(files)} extracted, {kept} kept after dedupe")
    return fdir


def step_sheets(fdir, work, start, interval):
    sdir = os.path.join(work, "sheets")
    os.makedirs(sdir, exist_ok=True)
    for old in glob.glob(os.path.join(sdir, "*.jpg")):
        os.remove(old)
    files = sorted(glob.glob(os.path.join(fdir, "*.jpg")))
    W, H, cols, rows = 640, 360, 2, 3
    per = cols * rows
    for s in range(0, len(files), per):
        sheet = Image.new("RGB", (W * cols, (H + 20) * rows), "white")
        d = ImageDraw.Draw(sheet)
        for i, f in enumerate(files[s:s + per]):
            n = int(re.search(r"f_(\d+)", f).group(1))
            t = start + (n - 1) * interval
            x, y = (i % cols) * W, (i // cols) * (H + 20)
            sheet.paste(Image.open(f).resize((W, H)), (x, y + 20))
            d.text((x + 4, y + 4), f"{os.path.basename(f)}  {ts(t)}", fill="black")
        sheet.save(os.path.join(sdir, f"s_{s // per:02d}.jpg"), quality=80)
    print(f"sheets: {len(glob.glob(os.path.join(sdir, '*.jpg')))} in {sdir}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("out")
    ap.add_argument("--work", default=None)
    ap.add_argument("--video", default=None)
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--interval", type=int, default=10)
    ap.add_argument("--height", type=int, default=480)
    ap.add_argument("--langs", default="en,en-orig,en.*")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    work = a.work or os.path.join(a.out, "_work")
    os.makedirs(work, exist_ok=True)
    step_subtitles(a.url, a.out, a.langs)
    video = step_video(a.url, work, a.height, a.video)
    fdir = step_frames(video, work, a.start, a.interval)
    step_sheets(fdir, work, a.start, a.interval)
    print("DONE. Next: read sheets, choose frames, run export_slides.py")


if __name__ == "__main__":
    main()
