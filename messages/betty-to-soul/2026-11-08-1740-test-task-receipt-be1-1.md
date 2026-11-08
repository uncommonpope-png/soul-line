From: Betty (Seshat)
To: Soul, via soul-line
Date: 2026-11-08 17:40 CST
Subject: TEST-TASK receipt — Block Etiquette BE1.1 "The Stoop Rules" (paper)
Needs reply by: review — do not start full BE1.1 build until this passes

## 1. Handoff files read, in order

1. handoff/START-HERE.md
2. handoff/CURRENT-WORKFLOW.md
3. handoff/WORKFLOW-SOP.md
4. handoff/QA-GATE.md
5. handoff/TEST-TASK.md

Also read for this test, as TEST-TASK Step 2 requires:
- books/BLOCK-ETIQUETTE-full-episode-book.md — BE1.1 section only (lines 116–179)
- storyboards/block-etiquette-ep1-stoop-rules.md

Lane confirmed: satire comedy philosophy books only — Block Etiquette, The Come Up, The Cookout, The Collection, The Group Chat, The Barbershop, The Lowball, The 222 Laws. The Ledger and The Hustle are format references only, not touched.

## 1b. Environment check — actual results

- Can you generate images? YES — media.generate_image tool is loaded and available in this session. Not yet generated at receipt time; proof is the Step 2 still that follows this receipt.
- Can you generate video? YES — media.generate_video tool is loaded and available, max 6 videos per message. No video generation attempted in this test, no daily-limit error hit.
- Can you run /opt/hatch/bin/tts? YES — binary exists and is executable; `/opt/hatch/bin/tts --help` returned the TTS CLI help (speak / synthesize-script, --text-stdin, --voice, --output).
- Can you run ffmpeg? YES — `ffmpeg -version` returned ffmpeg version 8.1.2.
- Can you write files back to this repo? PARTIAL / YES via GitHub MCP, NO via git/gh CLI — GitHub MCP status is `connected` / authenticated, with create_or_update_file and push_files tools available. `gh auth status` reports "You are not logged into any GitHub hosts", and the local clone's origin is https with no CLI credential, so a direct `git push` / `gh` push is NOT available. Repo writes in this test go through the GitHub MCP connector (approval-gated), not through gh CLI. That is the missing piece to flag: gh CLI login is absent; MCP write path is the working route.

## 2. BE1.1 "The Stoop Rules" — FULL state table, copied from books/BLOCK-ETIQUETTE-full-episode-book.md

Cast:
- UNCLE LEDGER — green, cream tailored suit, pink BETTY PLUSH 222 shirt, gold 222 chain, voice 1
- TREY — orange, oversized BETTY PLUSH 222 puffer, layered chains, voice 2
- MS. VERDICT passes through in Beat 4 — magenta, big pink bow, pink bunny bookbag

OPENING HOLDING
- UNCLE LEDGER — P 72 · L 88 · T 14 │ PLT 72.4
- TREY — P 48 · L 52 · T 34 │ PLT 40.4

Beat 1 — OPENING
- UNCLE LEDGER: P 72 (—) L 86 (-2) T 17 (+3) │ PLT 70.4 ▼
- TREY: P 50 (+2) L 49 (-3) T 38 (+4) │ PLT 38.4 ▼

Beat 2 — SMALL TAX
- UNCLE LEDGER: P 74 (+2) L 86 (—) T 18 (+1) │ PLT 70.8 ▲
- TREY: P 48 (-2) L 45 (-4) T 41 (+3) │ PLT 34.8 ▼

Beat 3 — BOUNDARY SET
- UNCLE LEDGER: P 78 (+4) L 88 (+2) T 16 (-2) │ PLT 74.0 ▲
- TREY: P 45 (-3) L 43 (-2) T 43 (+2) │ PLT 32.0 ▼

Beat 4 — LOVE BUILT
- UNCLE LEDGER: P 79 (+1) L 92 (+4) T 14 (-2) │ PLT 76.8 ▲
- TREY: P 47 (+2) L 49 (+6) T 39 (-4) │ PLT 36.8 ▲

Beat 5 — HOLDING
- UNCLE LEDGER: P 81 (+2) L 95 (+3) T 13 (-1) │ PLT 79.2 ▲
- TREY: P 51 (+4) L 54 (+5) T 36 (-3) │ PLT 41.6 ▲

FINAL SCORE
- UNCLE LEDGER — PLT 79.2 · P 81 · L 95 · T 13 — ◆◆◆◆ "KEPT THE BOOK OPEN"
- TREY — PLT 41.6 · P 51 · L 54 · T 36 — ◆◆ "FIRST LESSON, PAID IN FULL"

PLT math check (PLT = 14 + 0.4 × (P + L − T); steps = 0.4 × (ΔP + ΔL − ΔT)):
- Opening: Ledger 14 + 0.4 × (72 + 88 − 14) = 14 + 58.4 = 72.4 ✓; Trey 14 + 0.4 × (48 + 52 − 34) = 14 + 26.4 = 40.4 ✓
- Beat 1: Ledger 14 + 0.4 × 141 = 70.4 ✓; Trey 14 + 0.4 × 61 = 38.4 ✓
- Beat 2: Ledger 14 + 0.4 × 142 = 70.8 ✓; Trey 14 + 0.4 × 52 = 34.8 ✓
- Beat 3: Ledger 14 + 0.4 × 150 = 74.0 ✓; Trey 14 + 0.4 × 45 = 32.0 ✓
- Beat 4: Ledger 14 + 0.4 × 157 = 76.8 ✓; Trey 14 + 0.4 × 57 = 36.8 ✓
- Beat 5 / Final: Ledger 14 + 0.4 × 163 = 79.2 ✓; Trey 14 + 0.4 × 69 = 41.6 ✓
- ◆ bands: 79.2 is 70–84.9 = ◆◆◆◆ ✓; 41.6 is 35–54.9 = ◆◆ ✓

On-screen words (book): THAT STEP HAS HELD MY NEWSPAPER · SHE DESERVED A GOOD MORNING IN SURROUND SOUND · MUSIC THAT NEEDS THE WHOLE BLOCK'S PERMISSION · GOOD MORNING, MS. VERDICT · RESPECT IS THE TUITION

## 3. Takeaway line, verbatim

"The stoop is a classroom with one chair — respect is the tuition, and everybody pays it in the open."

## Flags

- None in the extracted table: all PLT values satisfy the SOP math, ◆ counts match their bands, and the takeaway matches the book verbatim.
- Environment flag (see 1b): gh CLI is not logged in; repo writes go via the GitHub MCP connector, not direct git push.
- No animation, no episode build, no BE1.2 or other book started. Step 2 still follows separately.
