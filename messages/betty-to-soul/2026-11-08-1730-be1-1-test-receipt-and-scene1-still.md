From: Betty (Seshat)
To: Soul
Date: 2026-11-08 17:30 CST
Subject: TEST-TASK receipt — BE1.1 "The Stoop Rules" state table + scene 1 still
Needs reply by: Test pass/fail review — no further build until this passes

# TEST-TASK — receipt (Step 1) + one scene still (Step 2)

Note on a concurrent receipt: while this file was being pushed, a parallel receipt landed — `messages/betty-to-soul/2026-11-08-1740-test-task-receipt-be1-1.md`, commit 63f58efc. Its state table agrees exactly with the table below (checked line by line). This file is NOT a second competing receipt: it is the same test, plus the Step 2 still and its QA checks, which the 1740 receipt said "follows separately". First push attempt of this file failed with "failed to update reference" because the head moved to 63f58efc during the push; this is the retry against that head.

Lane: SATIRE COMEDY PHILOSOPHY books only — Block Etiquette, The Come Up, The Cookout, The Collection, The Group Chat, The Barbershop, The Lowball, The 222 Laws. The Ledger and The Hustle were not touched; they are format references only.

## 1. Handoff files read, in order

1. `handoff/START-HERE.md`
2. `handoff/CURRENT-WORKFLOW.md`
3. `handoff/WORKFLOW-SOP.md`
4. `handoff/QA-GATE.md`
5. `handoff/TEST-TASK.md`

Source for BE1.1, read after the handoff: `books/BLOCK-ETIQUETTE-full-episode-book.md` (BE1.1 "The Stoop Rules").
Storyboard read before generating the still: `storyboards/block-etiquette-ep1-stoop-rules.md`.

## 1b. Environment check — actual results, not claims

- Can you generate images? YES — proven in this run. One still generated: `media-generation-be1-1-scene1-still-0-f8c5893b-07ea-4d60-a202-722d57e0d43e.webp`, 1152x2048, 674,120 bytes, local path `~/workspace/soul-line-test/media-generation-be1-1-scene1-still-0-f8c5893b-07ea-4d60-a202-722d57e0d43e.webp`.
- Can you generate video? NOT TESTED in this run — the video tool (`media.generate_video`) is present in the pipeline, but TEST-TASK Step 3 forbids animating, so no video generation was attempted. No daily-limit / 429 error was encountered, because no video was attempted.
- Can you run `/opt/hatch/bin/tts`? YES — binary present and `--help` runs. No synthesis was run in this test (TTS is a full-build step, not a test step).
- Can you run `ffmpeg`? YES — `/usr/bin/ffmpeg`, version 8.1.2, verified with `ffmpeg -version`.
- Can you write files back to this repo? YES via the GitHub MCP connector (approval-gated `push_files`); NO via `gh` CLI — `gh auth status` reports "You are not logged into any GitHub hosts". First push attempt of this file failed only because a concurrent commit moved the head mid-push (see note above); retry is against head 63f58efc. If this file is in the repo, the write succeeded.

## 2. BE1.1 "The Stoop Rules" — FULL state table, copied from the book

Cast (per TEST-TASK anchors): UNCLE LEDGER = green, cream tailored suit, pink BETTY PLUSH 222 shirt, gold 222 chain, voice 1. TREY = orange, oversized BETTY PLUSH 222 puffer, layered chains, voice 2. MS. VERDICT passes through in Beat 4 (magenta, big pink bow, pink bunny bookbag).

### OPENING HOLDING
- UNCLE LEDGER — P 72 · L 88 · T 14 │ PLT 72.4
- TREY — P 48 · L 52 · T 34 │ PLT 40.4

### Beat 1 — OPENING
- UNCLE LEDGER: P 72 (—) L 86 (-2) T 17 (+3) │ PLT 70.4 ▼
- TREY: P 50 (+2) L 49 (-3) T 38 (+4) │ PLT 38.4 ▼

### Beat 2 — SMALL TAX
- UNCLE LEDGER: P 74 (+2) L 86 (—) T 18 (+1) │ PLT 70.8 ▲
- TREY: P 48 (-2) L 45 (-4) T 41 (+3) │ PLT 34.8 ▼

### Beat 3 — BOUNDARY SET
- UNCLE LEDGER: P 78 (+4) L 88 (+2) T 16 (-2) │ PLT 74.0 ▲
- TREY: P 45 (-3) L 43 (-2) T 43 (+2) │ PLT 32.0 ▼

### Beat 4 — LOVE BUILT
- UNCLE LEDGER: P 79 (+1) L 92 (+4) T 14 (-2) │ PLT 76.8 ▲
- TREY: P 47 (+2) L 49 (+6) T 39 (-4) │ PLT 36.8 ▲

### Beat 5 — HOLDING
- UNCLE LEDGER: P 81 (+2) L 95 (+3) T 13 (-1) │ PLT 79.2 ▲
- TREY: P 51 (+4) L 54 (+5) T 36 (-3) │ PLT 41.6 ▲

### FINAL SCORE
- UNCLE LEDGER — PLT 79.2 · P 81 · L 95 · T 13 — ◆◆◆◆ "KEPT THE BOOK OPEN"
- TREY — PLT 41.6 · P 51 · L 54 · T 36 — ◆◆ "FIRST LESSON, PAID IN FULL"

### PLT math check (WORKFLOW-SOP: opening = 14 + 0.4×(P+L−T); steps = 0.4×(ΔP+ΔL−ΔT))
All 12 lines check out. Examples: opening Ledger 14 + 0.4×(72+88−14) = 14 + 58.4 = 72.4; opening Trey 14 + 0.4×(48+52−34) = 14 + 26.4 = 40.4; Beat 5 Ledger 14 + 0.4×(81+95−13) = 14 + 65.2 = 79.2; Beat 5 Trey 14 + 0.4×(51+54−36) = 14 + 27.6 = 41.6. ◆ bands check: 79.2 = ◆◆◆◆ (70–84.9); 41.6 = ◆◆ (35–54.9).

On-screen words (book): THAT STEP HAS HELD MY NEWSPAPER · SHE DESERVED A GOOD MORNING IN SURROUND SOUND · MUSIC THAT NEEDS THE WHOLE BLOCK'S PERMISSION · GOOD MORNING, MS. VERDICT · RESPECT IS THE TUITION

## 3. Takeaway line, verbatim

"The stoop is a classroom with one chair — respect is the tuition, and everybody pays it in the open."

## Step 2 — One scene still: BE1.1 scene 1 (Beat 1)

Still: Trey posted up in Ledger's top-step seat, speaker blasting, music notes in the air; Uncle Ledger coming out of his own door behind him, arms folded; Ms. Verdict watching from the next stoop, pink bunny bookbag beside her. Full house style, storyboard Frames 1–2.

Local file: `~/workspace/soul-line-test/media-generation-be1-1-scene1-still-0-f8c5893b-07ea-4d60-a202-722d57e0d43e.webp` (1152x2048, 9:16). The repo push tool accepts text only, so the still itself is delivered in chat / Betty's Library with this note, not as a binary in this repo file — that is a delivery limitation, flagged here, not hidden.

### My own QA-GATE still checks
- [x] House style present: signage stack readable — BETTY PLUSH 222, PLT 222 poster, fiverr / @popeofai / 222 board. Branding on the clothes — Trey's BETTY PLUSH 222 puffer, Ledger's pink 222 shirt and gold 222 chain. Real plushies in frame.
- [x] Products match the site photos in design/colors, with readable name cards: Spike (grey, three eyes, spiked collar), Pink Drip Bunny, Pixel Bunny, Bat Plush, Patchwork Plush. Pink bunny bookbag shown as a bag with Betty Plush / PLT hang-tags visible.
- [x] Spike, when present, is grey with three eyes and a spiked collar.
- [x] Characters match assigned colors/outfits: Ledger green / cream suit, Trey orange / oversized puffer / layered chains / limited sneakers, Ms. Verdict magenta / big pink bow.
- [~] Full figures in frame, nothing important cropped — mostly. See flags below.

### Flags — travelling with the work
1. Boombox at the left edge is partly cropped (left side cut off).
2. Ms. Verdict's ponytail touches / is tight to the right edge; her figure is otherwise fully in frame.
3. The "BETTY PLUSH 22" banner across the shopfront is partly obscured by Trey's foot — the final "2" is cut.
4. Generator added a top title line "BE1.1 Beat 1 — 'The Stoop Rules'" that was not in the prompt — extra on-screen text, not a book line.
5. Trey is wearing headphones, which are not in the book — a small generator addition; the book's speaker is present as the boombox.
6. Still dimensions are 1152x2048 (9:16), not 1080x1920 — correct ratio, not the exact episode frame size.
7. Ms. Verdict appears in this Beat 1 still per the approved storyboard Frame 1 (watching from the next stoop); in the book she passes through in Beat 4. That is storyboard, not book, staging — flagged so it is not mistaken for a book change.
8. No video was generated, no TTS was run, no episode was built — per TEST-TASK Step 3. Nothing here is described as finished beyond one still + paper.

## Step 3 — Stop

No animation, no episode build, no BE1.2, no other book started. Awaiting test pass/fail review.
