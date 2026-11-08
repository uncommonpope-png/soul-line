From: Betty (Seshat)
To: Soul
Date: 2026-11-08 17:48 CST
Subject: BE1.3 prep — "Speak When You Pass": paper + 3 stills + TTS + cards + build script, NO VIDEO YET
Needs reply by: Next-round animation — no assembly until the duration flag below is decided

# BE1.3 PREP — paper + stills + voices + cards, video NOT generated

Pope's order (live call, 2026-11-08 ~17:41 CST): work on multiple episodes at a time. BE1.1 and BE1.2 are being built in parallel by sibling agents and are using the whole video budget (6 videos) for this round. This prep does everything EXCEPT video generation, so BE1.3 is ready to animate in the next round.

**No video was generated in this round. Zero media.generate_video calls. No final mp4 exists.**

## 1. Files read
- handoff/WORKFLOW-SOP.md, handoff/QA-GATE.md, handoff/CURRENT-WORKFLOW.md
- books/BLOCK-ETIQUETTE-full-episode-book.md — BE1.3 section only
- storyboards/block-etiquette-ep1-stoop-rules.md (cast locks / house style)
- handoff/build_h11_template.py — copied, data blocks patched only

Lane: satire comedy philosophy books only. The Ledger and The Hustle were not touched.

## 2. BE1.3 "Speak When You Pass" — FULL state table, copied from the book

Cast (book): BIG FRAME — gentle giant, clean tee, tailored cargos, heavy gold chain, soft voice · TREY — orange, oversized BETTY PLUSH 222 puffer, layered chains, limited sneakers, headphones on, eyes down. Elders in Beat 4, by name: Mrs. Abernathy, Mr. Otis (sharp hat), Miss Dee.

### OPENING HOLDING
- BIG FRAME — P 66 · L 84 · T 18 │ PLT 66.8
- TREY — P 46 · L 50 · T 36 │ PLT 38.0

### Beat 1 — OPENING
- BIG FRAME: P 66 (—) L 82 (-2) T 20 (+2) │ PLT 65.2 ▼
- TREY: P 46 (—) L 47 (-3) T 39 (+3) │ PLT 35.6 ▼

### Beat 2 — SMALL TAX
- BIG FRAME: P 65 (-1) L 79 (-3) T 22 (+2) │ PLT 62.8 ▼
- TREY: P 44 (-2) L 43 (-4) T 43 (+4) │ PLT 31.6 ▼

### Beat 3 — LOVE DIP
- BIG FRAME: P 65 (—) L 77 (-2) T 23 (+1) │ PLT 61.6 ▼
- TREY: P 41 (-3) L 40 (-3) T 46 (+3) │ PLT 28.0 ▼

### Beat 4 — LOVE BUILT
- BIG FRAME: P 66 (+1) L 82 (+5) T 21 (-2) │ PLT 64.8 ▲
- TREY: P 44 (+3) L 46 (+6) T 42 (-4) │ PLT 33.2 ▲

### Beat 5 — HOLDING
- BIG FRAME: P 68 (+2) L 85 (+3) T 20 (-1) │ PLT 67.2 ▲
- TREY: P 48 (+4) L 50 (+4) T 39 (-3) │ PLT 37.6 ▲

### FINAL SCORE
- BIG FRAME — PLT 67.2 · P 68 · L 85 · T 20 — ◆◆◆ "SEEN, ON PURPOSE"
- TREY — PLT 37.6 · P 48 · L 50 · T 39 — ◆◆ "LEARNED TO LOOK UP"

### PLT math check (14 + 0.4×(P+L−T))
All 12 lines check out, e.g. opening Frame 14 + 0.4×(66+84−18) = 66.8; opening Trey 14 + 0.4×(46+50−36) = 38.0; Beat 5 Frame 14 + 0.4×(68+85−20) = 67.2; Beat 5 Trey 14 + 0.4×(48+50−39) = 37.6. ◆ bands: 67.2 = ◆◆◆ (55–69.9); 37.6 = ◆◆ (35–54.9).

On-screen words (book): LIKE I WAS FURNITURE WITH A PULSE · A STOPPED GIANT IS A WHOLE ANNOUNCEMENT · THAT IS THE PROBLEM, NOT THE EXCUSE · YOU ARE THE ONE WHO JUST ARRIVED · THAT NOD IS A DIPLOMA

## 3. Takeaway line, verbatim

"Speaking when you pass costs nothing and buys everything — the block runs on being seen."

## 4. What is done — work dir ~/workspace/soul-line-test/be1-3/

- `build_be13_template.py` — template copy, patched data blocks only: 24 performed lines (book's 22 dialogue lines verbatim + a short scene-setting opener + the takeaway as the last line), CAPS (24), STATES (6, book-exact), STATE_LINE [0, 6, 11, 15, 19, 23], CHIPS (line 5 "FURNITURE WITH A PULSE" · line 10 "A STOPPED GIANT" · line 18 "YOU JUST ARRIVED"), NAMES [("BIG FRAME", "4DD0E1"), ("TREY", "FFA726")], both PIL cards, scene spans, src placeholders, output path `block-etiquette-be1-3-speak-when-you-pass.mp4` in the work dir. One required index update, noted in the script: `scene_end` uses line 22 (last dialogue line) instead of line 8 — index only, logic unchanged, because the script has 24 lines instead of 10.
- `card-open.png`, `card-final.png` — 1080×1920, checked visually: opening numbers exact, finals exact, ◆◆◆ / ◆◆ correct, verdict lines fit, takeaway split over 3 lines, brand footer present.
- `line01.mp3` … `line24.mp3` — all 24 TTS lines via the build script (stdin fed per line, per the TTS trap note), every one >1000 bytes (smallest 8.3 KB). Speech total ≈ 107.5 s.
- `subs.ass` — 24 caption lines matching LINES/CAPS.
- `seg0.mp4` — ffmpeg still segment of the opening card (2.4 s), produced by the script before it stopped. It is NOT a generated video.
- `README.md` — full work-dir record, including the next-step list below.

## 5. Stills (1152×2048, 9:16) — QA still-check results

- Scene 1 (Beats 1–2): `media-generation-be1-3-scene1-0-3c354ee5-02bf-4246-931f-56fa793e68c2.webp`
- Scene 2 (Beat 3): `media-generation-be1-3-scene2-0-6242f0fc-4ef0-4555-acf7-005bf9522a9c.webp`
- Scene 3 (Beats 4–5) PRIMARY v2: `media-generation-be1-3-scene3-v2-0-5dfd6336-19d8-4db8-b3ff-77be2f587815.webp`
- Scene 3 v1 (alternate, superseded): `media-generation-be1-3-scene3-0-98d7a689-0786-48e2-9eae-fec8a92986a1.webp`

QA gate, all three: signage stack readable (BETTY PLUSH 222 / PLT 222 / fiverr/@popeofai/222) · branding on the clothes · real plushies in frame with readable name cards · Spike grey with three eyes and a spiked collar (see flag 5) · characters match cast · full figures (see flag 4).

## 6. Flags — travelling with the work

1. **DURATION — decision needed before assembly.** The build script reports **total 118.85 s** (2.4 s card + ~107.5 s speech + 24×0.35 s gaps + 0.6 s) — nearly double the SOP's ~55–70 s episode target. Cause: BE1.3 has 22 dialogue lines (vs 10 in the H11 template / 12 in Law 1). I did NOT cut any book dialogue. Options: (a) accept a ~2-minute episode, (b) trim to key lines per beat (Law 1 pattern), (c) raise TTS speed above 94. Do not assemble-and-ship a 119 s episode as if it passed the 55–70 s gate.
2. **Scene 3 v1 — invented elder names (superseded).** Its speech bubble reads "Ms. LENA! • Mr. CAL! • AZIZA!" — those names are invented and contradict the book's Mrs. Abernathy / Mr. Otis / Miss Dee. That is why v2 (no bubble, no names) is primary. V1 is kept only as an alternate; do not animate v1 without removing the bubble.
3. **Generator-added title text on all three stills.** Scenes 1–2 carry a top title banner ("Block Etiquette BE1.3 • Beat 1-2 / Beat 3: 'Speak When You Pass'"); scene 2 also has a bottom ribbon "STOP. HOLD. SPEAK WHEN YOU PASS" — a paraphrase, not a book line. These are baked into the stills and will appear in the animated scenes unless cropped.
4. **Scene 3 v2 tradeoffs.** Big Frame is cropped at the right edge (shoulder/arm past the frame) and Trey's puffer has no BETTY PLUSH 222 text (v1 has the branding and full figures, but the wrong-names bubble). V2 was chosen because a false name is a worse defect than missing jacket text.
5. **Spike's eyes differ between stills.** Scene 1, scene 2 and scene 3 v1: three eyes, spiked collar, correct. Scene 3 v2: Spike shows two visible eyes (third eye not visible). Flagged for the animator.
6. **Continuity drift.** Frame's cargos are khaki in scenes 1–2, green in scene 3 v1, khaki again in v2. Frame's gold chain gains a pendant in scenes 2–3 (scene 1 has none). Scene 2 poster says "PLT 222 PLUSH • TOYS • LIMITED DROP" — the word TOYS is generator drift (adult collectible, never toy framing). Scene 1 background adds "Elm St" and "CAFFE GRANDE" signs — invented background signage, minor.
7. **Voice + colour choices NOT in the book (flagged, changeable).** Big Frame has no book-assigned voice or scorebug colour. I put him on voice 1 (avocado_v2:vd2_r8_rep1k_0557_v068_28k_g5k) with scorebug teal 4DD0E1 (RGB 77,208,225); Trey stays on voice 2 (avocado_v2:MAI_03) with orange FFA726 (matching the sibling BE builds). The opener and takeaway are also voice 1, as in the H11 template. Big Frame's skin tone in the stills is natural (not a colour-coded figure like Ledger green / Trey orange / Verdict magenta) — the book gives him no colour lock, and his look is consistent across all three stills.
8. **Script stop point is by design, not a defect.** The build script ran through cards + TTS + subs and stopped with `FAILED ffmpeg: Error opening input file .../be1-3-scene1-anim.mp4` — the first animation file does not exist yet. No final mp4, no joined.mp4, no audio.mp3 (audio concat happens after the video segments in the script). Re-running the script is safe: it skips TTS lines already >1000 bytes.

## 7. Next step (next round, exact)

1. Animate the 3 stills (locked camera, small movements only, silent) and save in `~/workspace/soul-line-test/be1-3/` as exactly: `be1-3-scene1-anim.mp4`, `be1-3-scene2-anim.mp4`, `be1-3-scene3-anim.mp4` (scene 3 = v2 primary).
2. Run `python3 build_be13_template.py` in that dir. It writes `block-etiquette-be1-3-speak-when-you-pass.mp4` there.
3. Gate-check the finished mp4 against QA-GATE.md (frames, scorebug values per beat, final card, duration — see flag 1), then deliver with a delivery note.

## 8. What was NOT done

- Zero video generation. No animation, no assembly, no final mp4.
- BE1.4 not started. The Ledger / The Hustle not touched. Sibling work dirs (be1-1/, be1-2/, be1-4/) not touched.
