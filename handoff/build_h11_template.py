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
    ("soul", "First Corner. June has come to the corner for the first time, hands shaking. Marlo runs it fair. And he sells the rules before he sells anything."),
    ("alt",  "I \u2014 I was told this is where I ask. I ain't never done this before."),
    ("soul", "Then you listen first. On this corner, you ask plain, you pay plain, you leave plain."),
    ("alt",  "How much for a fifty? And don't play me \u2014 I counted it twice on the bus."),
    ("soul", "A fifty is a fifty. Price don't change 'cause you nervous."),
    ("soul", "You short five? No. You got it exact. See \u2014 you already better at this than you think."),
    ("alt",  "You counted it in front of me. Nobody ever counts it in front of me."),
    ("alt",  "What if \u2014 what if I need to come back? What if somebody sees me here?"),
    ("soul", "Don't make the corner carry your fear. There's your fifty. Wrapped clean. We good?"),
    ("alt",  "We good. Same time \u2014 if I need. Same price."),
]
VOICES = {"soul": VOICE, "alt": "avocado_v2:MAI_03"}
CAPS = [
    "FIRST CORNER. HER FIRST TIME.",
    "\"I AIN'T NEVER DONE THIS BEFORE.\"",
    "\"YOU ASK PLAIN, YOU PAY PLAIN, YOU LEAVE PLAIN.\"",
    "\"HOW MUCH FOR A FIFTY? DON'T PLAY ME.\"",
    "\"A FIFTY IS A FIFTY.\"",
    "\"YOU GOT IT EXACT.\"",
    "\"YOU COUNTED IT IN FRONT OF ME.\"",
    "\"WHAT IF SOMEBODY SEES ME HERE?\"",
    "\"DON'T MAKE THE CORNER CARRY YOUR FEAR.\"",
    "\"WE GOOD. SAME PRICE.\"",
]

# (Dray P,L,T,PLT, Carl P,L,T,PLT) — exact book states
STATES = [
    (58, 84, 16, "64.4",  42, 66, 28, "46"),
    (60, 88, 14, "67.6",  44, 69, 24, "49.6"),
    (64, 86, 15, "68",    41, 71, 26, "48.4"),
    (67, 91, 14, "71.6",  42, 76, 23, "52"),
    (65, 90, 17, "69.2",  40, 74, 27, "48.8"),
    (71, 92, 15, "73.2",  43, 78, 25, "52.4"),
]
STATE_LINE = [0, 1, 3, 5, 7, 8]  # state i active from line i (0-indexed)
CHIPS = [
    (2, "THE RULES BEFORE THE SALE"),
    (5, "COUNTED IN FRONT OF HER - LOVE BUILT"),
    (8, "THE HANDOFF - WRAPPED CLEAN"),
]
NAMES = [("MARLO", "81C784"), ("JUNE", "F48FB1")]

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
    ("THE HUSTLE", 64, (255, 210, 74), True),
    ("FIRST", 92, (255, 255, 255), True),
    ("CORNER", 92, (255, 255, 255), True),
    ("", 40, (255, 255, 255), False),
    ("OPENING SCORES", 52, (244, 114, 182), True),
    ("", 30, (255, 255, 255), False),
    ("MARLO", 58, (129, 199, 132), True),
    ("P 58 - L 84 - T 16", 54, (255, 255, 255), True),
    ("PLT 64.4", 84, (129, 199, 132), True),
    ("", 30, (255, 255, 255), False),
    ("JUNE", 58, (244, 143, 177), True),
    ("P 42 - L 66 - T 28", 54, (255, 255, 255), True),
    ("PLT 46", 84, (244, 143, 177), True),
    ("", 40, (255, 255, 255), False),
    ("Her first time. His corner, his rules.", 40, (220, 220, 220), False),
    ("BETTY PLUSH / 222 / PLT", 40, (244, 114, 182), True),
])
card(os.path.join(D, "card-final.png"), [
    ("FINAL SCORE", 84, (255, 255, 255), True),
    ("", 30, (255, 255, 255), False),
    ("MARLO", 58, (129, 199, 132), True),
    ("PLT 73.2", 96, (129, 199, 132), True),
    ("P 71 - L 92 - T 15", 50, (255, 255, 255), True),
    ("\u25c6\u25c6\u25c6 FAIR AND FIRM", 54, (129, 199, 132), True),
    ("", 30, (255, 255, 255), False),
    ("JUNE", 58, (244, 143, 177), True),
    ("PLT 52.4", 96, (244, 143, 177), True),
    ("P 43 - L 78 - T 25", 50, (255, 255, 255), True),
    ("\u25c6\u25c6 LEARNED THE RULES", 54, (244, 143, 177), True),
    ("", 40, (255, 255, 255), False),
    ("A corner with rules is a business.", 44, (220, 220, 220), False),
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
scene_span = {1: (CARD_OPEN, starts[2] + dur(mp3s[2]) + GAP),
              2: (starts[3], starts[5] + dur(mp3s[5]) + GAP),
              3: (starts[6], starts[8] + dur(mp3s[8]) + GAP)}
final_span = (starts[9], total)
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

src = {1: "media-generation-hustle-h11-anim1-0-f4bdc82b-7078-4c98-9d6c-0be24dd746dd.mp4",
       2: "media-generation-hustle-h11-anim2-0-453dab96-28cd-4eee-926f-cd2f4d1c9a27.mp4",
       3: "media-generation-hustle-h11-anim3-0-7a26851a-7fa0-41ab-8324-8d4273eff238.mp4"}
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

scene_end = starts[8] + dur(mp3s[8]) + GAP
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
out = os.path.join(FILES, "hustle-h11-first-corner.mp4")
run(["ffmpeg", "-y", "-v", "error", "-i", joined, "-i", aud, "-vf", vf,
     "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac",
     "-b:a", "160k", "-shortest", out])
print("DONE", out, round(dur(out), 2), "s")
