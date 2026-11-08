#!/usr/bin/env python3
"""Ledger Ep 2 'The Short Bag' WITH in-video scoring (same system as Ep 1).
Narration: Soul's British voice, own words. Scores: the book's exact states."""
import subprocess, os
from PIL import Image, ImageDraw, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
FILES = os.path.expanduser("~/workspace/goals/betty-plush-tiktok-campaign/files")
VOICE = "avocado_v2:vd2_r8_rep1k_0557_v068_28k_g5k"
TTS = "/opt/hatch/bin/tts"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
GAP = 0.35
CARD_OPEN = 2.4

# NEW FORMAT (Betty, 2026-11-07): dialogue-forward. The book's own conversation,
# performed in two voices; narration is only connective tissue and never recites
# the scores — the bugs show them moving. (voice_key, text) per line.
LINES = [
    ("soul", "What? It's a step. Steps are for sitting. This whole block is steps."),
    ("alt",  "That step has heard forty years of good mornings, baby. You just sat on all of them."),
    ("alt",  "You speak, the stoop knows your name. You don't speak, the stoop knows your type."),
    ("soul", "It's one morning. You acting like I skipped a mortgage payment."),
    ("soul", "...Morning, Mr. Ledger."),
    ("alt",  "Well. The steps taught him faster than I did."),
    ("soul", "Morning, Miss Earline. Morning, Dee. Morning \u2014 man, there's a lot of y'all."),
    ("alt",  "Every one of them would feed you now. That's what the word buys."),
    ("soul", "I'll sit down here till I earn the top."),
    ("alt",  "Boy, you greeted the whole row. Sit up here. You paid."),
    ("alt",  "One word opened every door on this row. Speak first \u2014 the sitting takes care of itself."),
    ("alt",  "A hello is the rent on any stoop \u2014 pay it gladly and the whole block is your living room."),
]
VOICES = {"soul": VOICE, "alt": "avocado_v2:MAI_03"}
CAPS = [
    "\"STEPS ARE FOR SITTING.\"",
    "\"YOU SAT ON FORTY YEARS OF GOOD MORNINGS.\"",
    "\"YOU DON'T SPEAK, THE STOOP KNOWS YOUR TYPE.\"",
    "\"IT'S ONE MORNING.\"",
    "\"...MORNING, MR. LEDGER.\"",
    "\"THE STEPS TAUGHT HIM FASTER THAN I DID.\"",
    "\"MORNING, MISS EARLINE. MORNING, DEE.\"",
    "\"EVERY ONE OF THEM WOULD FEED YOU NOW.\"",
    "\"I'LL SIT DOWN HERE TILL I EARN THE TOP.\"",
    "\"SIT UP HERE. YOU PAID.\"",
    "ONE WORD OPENED EVERY DOOR ON THIS ROW.",
    "A HELLO IS THE RENT ON ANY STOOP.",
]

# (Dray P,L,T,PLT, Carl P,L,T,PLT) — exact book states
STATES = [
    (34, 48, 44, "29.2",  66, 88, 18, "68.4"),
    (32, 44, 49, "24.8",  66, 87, 20, "67.2"),
    (32, 42, 52, "22.8",  68, 90, 19, "69.6"),
    (33, 47, 48, "26.8",  69, 94, 17, "72.4"),
    (36, 53, 45, "31.6",  71, 97, 16, "74.8"),
    (40, 59, 41, "37.2",  73, 101, 14, "78.0"),
]
STATE_LINE = [0, 2, 4, 6, 8, 10]  # state i active from line i (0-indexed)
CHIPS = [
    (1, "HE SAT BEFORE HE SPOKE"),
    (5, "ONE WORD \u2014 HIS TAX FALLS"),
    (9, "YOU PAID \u2014 TOP STEP EARNED"),
]
NAMES = [("TREY", "FFA726"), ("MS. VERDICT", "F48FB1")]

def run(cmd, input_text=None):
    r = subprocess.run(cmd, capture_output=True, text=True, input=input_text)
    if r.returncode != 0:
        raise SystemExit(f"FAILED {cmd[0]}: {r.stderr[-600:]}")
    return r

def dur(p):
    r = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p])
    return float(r.stdout.strip())

FD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
def card(path, rows):
    img = Image.new("RGB", (1080, 1920), (10, 42, 48))
    dr = ImageDraw.Draw(img)
    y = 240
    for text, size, color, bold in rows:
        f = ImageFont.truetype(FD if bold else FR, size)
        dr.text((540, y), text, font=f, fill=color, anchor="ma")
        y += int(size * 1.55)
    img.save(path)

card(os.path.join(D, "card-open.png"), [
    ("THE 222 LAWS", 64, (255, 210, 74), True),
    ("LAW 1", 92, (255, 255, 255), True),
    ("SPEAK FIRST, SIT SECOND", 62, (255, 255, 255), True),
    ("", 40, (255, 255, 255), False),
    ("OPENING SCORES", 52, (244, 114, 182), True),
    ("", 30, (255, 255, 255), False),
    ("TREY", 58, (255, 167, 38), True),
    ("P 34 - L 48 - T 44", 54, (255, 255, 255), True),
    ("PLT 29.2", 84, (255, 167, 38), True),
    ("", 30, (255, 255, 255), False),
    ("MS. VERDICT", 58, (244, 143, 177), True),
    ("P 66 - L 88 - T 18", 54, (255, 255, 255), True),
    ("PLT 68.4", 84, (244, 143, 177), True),
    ("", 40, (255, 255, 255), False),
    ("A hello is the rent on any stoop.", 40, (220, 220, 220), False),
    ("BETTY PLUSH / 222 / PLT", 40, (244, 114, 182), True),
])
card(os.path.join(D, "card-final.png"), [
    ("FINAL SCORE", 84, (255, 255, 255), True),
    ("", 30, (255, 255, 255), False),
    ("TREY", 58, (255, 167, 38), True),
    ("PLT 37.2", 96, (255, 167, 38), True),
    ("P 40 - L 59 - T 41", 50, (255, 255, 255), True),
    ("\u25c6\u25c6 PAID THE TOLL", 54, (255, 167, 38), True),
    ("", 30, (255, 255, 255), False),
    ("MS. VERDICT", 58, (244, 143, 177), True),
    ("PLT 78.0", 96, (244, 143, 177), True),
    ("P 73 - L 101 - T 14", 50, (255, 255, 255), True),
    ("\u25c6\u25c6\u25c6\u25c6 THE STOOP APPROVES", 54, (244, 143, 177), True),
    ("", 40, (255, 255, 255), False),
    ("One word opened every door on this row.", 44, (220, 220, 220), False),
    ("BETTY PLUSH / 222 / PLT", 40, (244, 114, 182), True),
])

mp3s = []
for i, (vk, line) in enumerate(LINES, 1):
    p = os.path.join(D, f"line{i:02d}.mp3")
    if not (os.path.exists(p) and os.path.getsize(p) > 1000):
        run([TTS, "speak", "--voice", VOICES[vk], "--text-stdin",
             "--output", p, "--speed", "94"], input_text=line)
    mp3s.append(p)

starts, t = [], CARD_OPEN
for p in mp3s:
    starts.append(t)
    t += dur(p) + GAP
total = t + 0.6
scene_span = {1: (CARD_OPEN, starts[3] + dur(mp3s[3]) + GAP),
              2: (starts[4], starts[5] + dur(mp3s[5]) + GAP),
              3: (starts[6], starts[9] + dur(mp3s[9]) + GAP)}
final_span = (starts[10], total)
print("total", round(total, 2))

def ts(s):
    h = int(s // 3600); m = int(s % 3600 // 60); sec = s % 60
    return f"{h}:{m:02d}:{sec:05.2f}"
ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "",
       "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
       "Style: Cap,Arial,58,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,0,2,60,60,150,1",
       "", "[Events]",
       "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i, cap in enumerate(CAPS):
    s = starts[i] + 0.05; e = starts[i] + dur(mp3s[i]) - 0.03
    ass.append(f"Dialogue: 0,{ts(s)},{ts(e)},Cap,,0,0,0,,{cap}")
open(os.path.join(D, "subs.ass"), "w").write("\n".join(ass))

import glob as _glob
def _anim(n):
    hits = sorted(_glob.glob(os.path.join(D, f"media-generation-law1-anim{n}-*.mp4")))
    return os.path.basename(hits[0]) if hits else None
src = {1: _anim(1), 2: _anim(2), 3: _anim(3)}
if any(v is None for v in src.values()):
    print("PREP READY: cards + TTS + subs done; scene animations not generated yet.")
    raise SystemExit(0)
segs = []
def still_seg(img, length, name):
    out = os.path.join(D, name)
    run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-i", img, "-t", str(length),
         "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-an", out])
    return out
segs.append(still_seg(os.path.join(D, "card-open.png"), CARD_OPEN, "seg0.mp4"))
for s in (1, 2, 3):
    a, b = scene_span[s]; length = b - a
    out = os.path.join(D, f"seg{s}.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-stream_loop", "-1", "-i", os.path.join(D, src[s]),
         "-t", str(length), "-vf",
         "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-an", out])
    segs.append(out)
fa, fb = final_span
segs.append(still_seg(os.path.join(D, "card-final.png"), fb - fa, "seg4.mp4"))
with open(os.path.join(D, "concat.txt"), "w") as f:
    for s in segs:
        f.write(f"file '{s}'\n")
joined = os.path.join(D, "joined.mp4")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i",
     os.path.join(D, "concat.txt"), "-c", "copy", joined])

sil = os.path.join(D, "sil.mp3")
run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
     "-t", str(GAP), sil])
sil_open = os.path.join(D, "sil_open.mp3")
run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
     "-t", str(CARD_OPEN), sil_open])
order = [sil_open]
for p in mp3s:
    order += [p, sil]
with open(os.path.join(D, "aconcat.txt"), "w") as f:
    for p in order:
        f.write(f"file '{p}'\n")
aud = os.path.join(D, "audio.mp3")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i",
     os.path.join(D, "aconcat.txt"), "-c:a", "libmp3lame", "-q:a", "3", aud])

scene_end = starts[9] + dur(mp3s[9]) + GAP
filters = []
def bug(state_idx, a, b):
    dp, dl, dt, dplt, tp, tl, tt, tplt = STATES[state_idx]
    for (who, color), align_right, vals in (
        (NAMES[0], False, (dp, dl, dt, dplt)),
        (NAMES[1], True, (tp, tl, tt, tplt))):
        txt = f"{who}  PLT {vals[3]}\nP {vals[0]}  L {vals[1]}  T {vals[2]}"
        tf = os.path.join(D, f"bug_{who}_{state_idx}.txt")
        open(tf, "w").write(txt)
        xexpr = "w-tw-28" if align_right else "28"
        filters.append(
            f"drawtext=fontfile={FONT}:textfile={tf}:fontsize=40:fontcolor={color}"
            f":box=1:boxcolor=black@0.62:boxborderw=14:x={xexpr}:y=28"
            f":line_spacing=6:enable='between(t,{a:.2f},{b:.2f})'")
for i, li in enumerate(STATE_LINE):
    a = CARD_OPEN if i == 0 else starts[li]
    b = scene_end if i == len(STATE_LINE) - 1 else starts[STATE_LINE[i + 1]]
    bug(i, a, b)
for li, text in CHIPS:
    tf = os.path.join(D, f"chip_{li}.txt")
    open(tf, "w").write(text)
    a = starts[li]
    filters.append(
        f"drawtext=fontfile={FONT}:textfile={tf}:fontsize=44:fontcolor=white"
        f":box=1:boxcolor=black@0.66:boxborderw=14:x=(w-tw)/2:y=238"
        f":enable='between(t,{a:.2f},{a + 1.5:.2f})'")
vf = ",".join(filters) + f",subtitles={os.path.join(D, 'subs.ass')}"
out = os.path.join(FILES, "222-laws-001-speak-first-sit-second.mp4")
run(["ffmpeg", "-y", "-v", "error", "-i", joined, "-i", aud, "-vf", vf,
     "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac",
     "-b:a", "160k", "-shortest", out])
print("DONE", out, round(dur(out), 2), "s")
