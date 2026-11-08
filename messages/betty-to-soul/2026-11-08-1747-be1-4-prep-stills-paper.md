From: Betty (Seshat)
To: Soul
Date: 2026-11-08 17:47 CST
Subject: BE1.4 "The Stoop Sweep" — prep done: paper + 3 stills + TTS + build script, NO VIDEO YET
Needs reply by: Next video round / duration decision (see flag 1) — no assembly until then

# BE1.4 prep — Pope's parallel-production order (2026-11-08 ~17:41 CST)

Pope ordered multiple episodes at a time. BE1.1 + BE1.2 are the full-episode (video) builds this round and are using the whole video budget (6 videos). BE1.4 was prepped alongside so it is ready to animate next round.

**NO VIDEO was generated in this round — zero video calls.** This note is paper + stills + TTS + build script only. The final mp4 is NOT assembled and nothing here is described as finished.

Lane: satire comedy philosophy books only. The Ledger and The Hustle were not touched.

## Files read, in order
- handoff/WORKFLOW-SOP.md, handoff/QA-GATE.md, handoff/CURRENT-WORKFLOW.md
- books/BLOCK-ETIQUETTE-full-episode-book.md — BE1.4 section only
- storyboards/block-etiquette-ep1-stoop-rules.md (cast locks / house style)
- handoff/build_h11_template.py — copied and patched, not rewritten

## BE1.4 "The Stoop Sweep" — FULL state table, copied from the book

Cast: UNCLE LEDGER (the elder, broom already in hand) · DEE (young neighbor, whose stoop night left evidence). No Trey in this episode.

### OPENING HOLDING
- UNCLE LEDGER — P 74 · L 86 · T 14 │ PLT 72.4
- DEE — P 52 · L 56 · T 32 │ PLT 44.4

### Beat 1 — OPENING
- UNCLE LEDGER: P 74 (—) L 85 (-1) T 16 (+2) │ PLT 71.2 ▼
- DEE: P 52 (—) L 54 (-2) T 35 (+3) │ PLT 42.4 ▼

### Beat 2 — SMALL TAX
- UNCLE LEDGER: P 75 (+1) L 84 (-1) T 17 (+1) │ PLT 70.8 ▼
- DEE: P 50 (-2) L 51 (-3) T 38 (+3) │ PLT 39.2 ▼

### Beat 3 — PROFIT DIP
- UNCLE LEDGER: P 74 (-1) L 84 (—) T 19 (+2) │ PLT 69.6 ▼
- DEE: P 48 (-2) L 49 (-2) T 40 (+2) │ PLT 36.8 ▼

### Beat 4 — LOVE BUILT
- UNCLE LEDGER: P 75 (+1) L 88 (+4) T 17 (-2) │ PLT 72.4 ▲
- DEE: P 51 (+3) L 55 (+6) T 36 (-4) │ PLT 42.0 ▲

### Beat 5 — HOLDING
- UNCLE LEDGER: P 77 (+2) L 91 (+3) T 16 (-1) │ PLT 74.8 ▲
- DEE: P 55 (+4) L 59 (+4) T 33 (-3) │ PLT 46.4 ▲

### FINAL SCORE
- UNCLE LEDGER — PLT 74.8 · P 77 · L 91 · T 16 — ◆◆◆◆ "THE STANDARD, DEMONSTRATED"
- DEE — PLT 46.4 · P 55 · L 59 · T 33 — ◆◆ "SWEEP BEFORE YOU'RE ASKED"

### PLT math check (14 + 0.4×(P+L−T))
All 12 lines check out. Examples: opening Ledger 14 + 0.4×(74+86−14) = 72.4; opening Dee 14 + 0.4×(52+56−32) = 44.4; Beat 5 Ledger 14 + 0.4×(77+91−16) = 74.8; Beat 5 Dee 14 + 0.4×(55+59−33) = 46.4. ◆ bands check: 74.8 = ◆◆◆◆ (70–84.9); 46.4 = ◆◆ (35–54.9).

On-screen words (book): CUPS DON'T LIE · THAT LINE IS SAYING A LOT · I DECLINE THE CONTRACT · CLEANER THAN YOURS. ON PURPOSE. · WELCOME TO THE HOUR

## Takeaway line, verbatim

"Your front is your first sentence — the block reads it before you say a word."

## Voices
- UNCLE LEDGER — voice 1 (avocado_v2:vd2_r8_rep1k_0557_v068_28k_g5k)
- DEE — voice 2 (avocado_v2:MAI_03)
- No scores are recited aloud; scores live on screen only. Line 01 is a one-line narration intro in voice 1 (template pattern); lines 02–21 are the book's 20 dialogue lines in order; line 22 is the takeaway, spoken last.

## Stills — 3 generated, gate-checked (work dir ~/workspace/soul-line-test/be1-4/)
- Scene 1 (Beats 1–2): media-generation-be1-4-scene1-still-0-0d3e21ad-5f99-4474-9056-7725e8b1a814.webp — Ledger sweeping his clean stoop, Dee on her messy stoop, cups/wrappers, Spike bookbag by the rail
- Scene 2 (Beat 3): media-generation-be1-4-scene2-still-0-64facb41-d0f5-4e3e-848f-b393a6b523a7.webp — Dee offering the $20, Ledger declining with hand raised, holding the broom
- Scene 3 (Beats 4–5): media-generation-be1-4-scene3-still-0-6f7dbebe-7f35-445a-b95b-ff095ca75e67.webp — golden hour, Dee sweeping proudly, Ledger smiling with broom on shoulder, two clean stoops
- All 3 are 1152x2048 (9:16). House style present in all 3: signage stack (BETTY PLUSH 222 / PLT 222 / fiverr/@popeofai/222), branding on the clothes, real plushies with readable name cards, Spike grey three-eyed spiked collar, pink bunny bookbag with Betty Plush / PLT tags, full bodies head to feet.

## TTS / cards / captions — done via the build script
- line01.mp3–line22.mp3: 22/22, all >1000 bytes (13K–77K), no 0-byte lines.
- card-open.png, card-final.png: 1080x1920, checked visually — numbers exact, no overflow, verdict lines split ("◆◆◆◆ THE STANDARD, / DEMONSTRATED" and "◆◆ SWEEP BEFORE / YOU'RE ASKED").
- subs.ass: 22 captions, one per line.
- build_be14.py: patched copy of build_h11_template.py (patch script patch_build.py in the same dir). Data blocks only, plus line-index spans for 22 lines and a `--prep-only` stop. `python3 build_be14.py --prep-only` redoes TTS/cards/subs; full run assembles be1-4-the-stoop-sweep.mp4.
- Full work-dir inventory + next steps: README.md in ~/workspace/soul-line-test/be1-4/

## Flags — travelling with the work
1. **DURATION — decision needed before assembly.** Estimated episode length from the prep run: **123.84 s**, nearly double the QA-GATE build-gate target of roughly 55–70 s. Cause: BE1.4 has 20 dialogue lines + intro + takeaway (22 lines); at TTS speed 94 the lines run 1.6–9.7 s each. I did NOT cut any book dialogue to force the target. Options: (a) accept a ~124 s episode, (b) split into two parts, or (c) raise TTS speed / trim the intro (saves only ~10 s). The script as written will produce the ~124 s episode if run as-is.
2. **Scene 1 window cards carry INVENTED PRICES** (Spike $22, Drip Bunny $18, Pixel Bunny $16, Bat Plush $14, Patchwork $20) — generator invention, NOT the book/catalog prices ($100 keychain / $400 plushie / $800 purse / $650 book bag). Do not read them as real prices; scenes 2 and 3 have no prices on their cards.
3. **Generator-added title banners and footer** on all 3 stills ("Block Etiquette BE1.4 • Beats 1-2/3/4-5 'The Stoop Sweep'" at top; scene 1 footer "KEEP IT TIGHT. CLEAN YOUR STOOP. • RESPECT YOUR BLOCK •") — not in the prompts, extra on-screen text.
4. **Ledger's shirt in scene 3 reads "B222Y PLUSH 222"** — garbled "BETTY". Scene 1 doormat reads "LEGDER" (misspelled). Scene 2's fiverr board reads "fiverr" correctly.
5. **Ledger wears glasses and a grey beard/ponytail in all 3 stills** — not in the cast lock (lock: tall green figure, cream suit, pink shirt, gold chain, white sneakers). Consistent across the three stills, but an addition.
6. **DEE HAS NO CAST LOCK in the book or storyboard** (no color, outfit, or voice assigned). Her look (curly puff, coral BETTY PLUSH 222 hoodie, teal cargo pants, chunky sneakers) and her scorebug color (amber FFB74D) are my assignments for this prep, not book canon — confirm or change before the final build.
7. **Scene 2 staging drift:** Ledger holds the broom and raises a hand, but is not visibly handing the broom to Dee as the book's Beat 3 says ("Here — the broom knows the way, and now so do your hands").
8. **Scene 3 still shows dirt/debris at Dee's broom** — sweeping in progress, fine for Beat 4, slightly off for Beat 5's "two clean stoops" holding shot.
9. **Stills are 1152x2048, not 1080x1920** — correct 9:16 ratio, not the exact episode frame size (the build script scales/crops to 1080x1920).
10. **Long caption risk:** caption line 13 ("I AM NOT FOR HIRE") is a shortened form of the spoken line "I am not for hire against your own education" — the full line would overflow the caption at fontsize 58; flagged, not hidden.
11. **No video generated, no mp4 assembled** — by design this round (video budget with BE1.1/BE1.2). Do not mistake this prep for a finished episode.

## Exact next step (next video round)
1. Animate the 3 stills (locked camera, small movements only, silent), save as be1-4-scene1-anim.mp4 / be1-4-scene2-anim.mp4 / be1-4-scene3-anim.mp4 in ~/workspace/soul-line-test/be1-4/
2. Run `python3 build_be14.py` (no flag) in that dir — assembles be1-4-the-stoop-sweep.mp4
3. Gate-check the finished mp4 against QA-GATE.md (frames, scorebug values per beat, final card, duration decision in flag 1) before delivering
4. Do NOT start BE1.5 / BE2.1 or any other episode from this prep.
