---
name: youtube_to_md
description: Use when the user gives a YouTube lecture/talk URL and wants the slides (课件) reconstructed as Markdown, the transcript downloaded, and/or a detailed summary of what the speaker said — e.g. "把这个视频的课件整理成 md", "下载 transcript 并总结", "视频转笔记".
---

# youtube_to_md

Turn a recorded lecture into: `transcript.txt`, a slide-by-slide Markdown (original text + 中文 + speaker's verbal additions), a timeline summary, and clean slide images. The slides are recovered by **frame extraction from the video**, not OCR of a PDF.

## Workflow

1. **Setup** — `mkdir -p OUT_DIR`; check `yt-dlp`, `ffmpeg`, Pillow (`pip3 install yt-dlp` if missing; a "No supported JavaScript runtime" warning from yt-dlp is harmless).
2. **Run the pipeline** (download subs + 480p video, extract frames every 10 s, dedupe, build contact sheets):
   ```bash
   python3 scripts/yt_to_slides.py "URL" OUT_DIR --work SCRATCH/work --start 300
   ```
   Do **not** pass `--print` to yt-dlp elsewhere — it silently suppresses subtitle download.
3. **Read the transcript** (`OUT_DIR/transcript.txt`, ~100 k chars for 2 h) in 3 chunks with `sed -n`. Note section boundaries, Q&A, and things said but not on slides.
4. **Read every contact sheet** (`work/sheets/s_NN.jpg`, 6 frames each with timestamp). Record which frame shows which slide.
5. **Fill gaps**: if a slide range looks missing (dedupe drops slides shown <10 s, or the deck sat still while the speaker talked), re-extract that range at 1 fps and dedupe on the slide region only:
   ```bash
   ffmpeg -ss A -t (B-A) -i work/video.mp4 -vf fps=1 -q:v 3 work/gap/gA_%05d.jpg
   ```
   then crop to the slide area before diffing (presenter webcam + cursor otherwise defeat dedupe).
6. **Measure crop geometry once** — first check the frame size (`Image.open(frame).size`). Defaults in `export_slides.py` fit 854x480 frames with a Safari full-screen + bottom-right webcam layout. If the best stream was only 360p (640x360), scale every coordinate by 0.75: `--top 46 --bottom 330 --right 557 --overlay-x 491 --overlay-y 279 --navbar 19`. For a different layout, print row/column means to find the browser chrome top, Dock bottom, window right edge and the presenter-overlay box.
7. **Export slides**: write `mapping.txt` (`f_0077  08_agile_manifesto`), then
   ```bash
   python3 scripts/export_slides.py work/frames OUT_DIR/images mapping.txt
   ```
   Show the user 2–3 results (a dark slide, a light web page, an IDE screen) before writing docs.
8. **Write the docs** into OUT_DIR:
   - `01_课件整理_<topic>.md` — every slide in projection order: English original verbatim, `🇨🇳` translation, `💬 讲师补充` for verbal-only content; include any web pages / code the speaker walked through (templates, rubrics, starter code) as tables/code blocks; end with a 待办清单.
   - `02_讲课内容详细总结.md` — timeline sections (`### hh:mm–hh:mm 标题`) with Q&A, then a numbered 核心要点速览.
   - `README.md` index of files.
9. **Normalise auto-caption errors** in the docs (e.g. "G/gate"→Git, "spring"→sprint, "I/IGL/a"→Agile) and say so in the caveats.

## Quick reference

| Need | Command / rule |
|---|---|
| Frame → time | `start + (N-1)*interval` seconds |
| Only subs, no video | `yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en.*" --sub-format json3 -o "transcript.%(ext)s" URL` |
| List sub languages | `yt-dlp --list-subs URL` |
| Presenter overlay | fill with median colour sampled left of the box, don't crop the width (keeps slide right edge) |
| Light nav bar (Moodle/UNSW) | auto-trimmed when first rows are near-white (`--navbar 25`) |
| Big reads | transcript/sheets outputs >30 KB get persisted to a file — Read that file, don't re-run |

## Common mistakes

- Trusting the first dedupe pass: it keeps too many near-duplicates (presenter moves) *and* misses short slides — always scan sheets, then fill gaps.
- Row-wise colour fill for the overlay smears text on light pages → use one median colour per image.
- Forgetting the `--start` offset when converting frame numbers to timestamps.
- Writing summaries only from slides: the verbal Q&A (grading rules, deadlines, "why") is usually the most valuable part — it comes from the transcript.
- Reading the transcript with `Read` at 2000 lines: output is truncated; use `sed -n a,bp` in chunks.
