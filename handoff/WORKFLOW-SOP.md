# WORKFLOW SOP — How an episode gets built

## Scope — the satire comedy philosophy books

This SOP serves the satire line ONLY: Block Etiquette, The Come Up, The Cookout, The Collection,
The Group Chat, The Barbershop, The Lowball, The 222 Laws. (The Ledger and The Hustle are in
production elsewhere — format references only.) The creative fusion, Betty's north star:
**In Living Color** (sketch-comedy ensemble energy, recurring characters with catchphrases,
pop-culture parody, fashion/music charge) × **one named power move per story** (original PLT
maxims only — never Robert Greene's text or law titles) × **Betty Plush**, with PLT scoring as
the judge that prices every move: power is funny until the Tax comes due. Humor is a HARD
requirement, and the stories go deep — real etiquette, real stakes — not surface gags.
Satire punches at poses, hype, and violations, never at anyone's dignity. For Block Etiquette,
ground the work in `research/block-etiquette-rulebook.md` in this repo.

## Brand core (never changes)

- Brand stack, exact order: **Betty Plush / 222 / Soul Collection Agency / A.G.M / PLT**
- PLT = Profit, Love, Tax. True Value = Profit + Love − Tax.
- Line: "We collect souls. Now we sell souls." (Never "rescue.")
- Handle everywhere: Saveaisoul. Site: https://uncommonpope-png.github.io/soul-economy/

## The books are the scripts

Every book in `books/` is written script-first. One conversation = one episode (~60s, vertical 1080×1920).
Anatomy of every scored episode, in order:
1. Opening score card (book's OPENING HOLDING, verbatim numbers)
2. Scene animations with live per-character scorebugs updating at every scored beat
3. Delta chips naming the big moves
4. Final score card (book's FINAL SCORE, ◆ ratings + verdict words verbatim)
5. The book's takeaway line, performed last

PLT math (for checking, never for inventing): opening PLT = 14 + 0.4×(P+L−T); each beat's PLT step
= 0.4×(ΔP+ΔL−ΔT). ◆ bands: <35 ◆ · 35–54.9 ◆◆ · 55–69.9 ◆◆◆ · 70–84.9 ◆◆◆◆ · 85+ ◆◆◆◆◆.
If your extracted numbers don't satisfy the math, you copied them wrong. Re-read the book.

## Narration format (Betty's standing direction)

- The book's DIALOGUE is performed in two voices. Narration is light connective tissue only.
- **Never recite the scores aloud.** Scores live ON SCREEN (cards, scorebugs, chips).
- Voices (TTS CLI `/opt/hatch/bin/tts speak --voice <id> --text-stdin --output <file> --speed 94`):
  - Voice 1 "Soul" (British, dry): `avocado_v2:vd2_r8_rep1k_0557_v068_28k_g5k`
  - Voice 2 (alt): `avocado_v2:MAI_03`
- **TTS TRAP (this burned three builds): the CLI blocks forever on `--text-stdin` if you don't feed
  it.** Always pass the line as the subprocess input (`subprocess.run(..., input=line)`).
  A build that writes text to a file but never feeds stdin produces 0-byte mp3s and hangs silently.
  Test through the build script itself, never with a standalone TTS call.

## House style — the look of every scene (standing order)

Every scene still, in every series:
- Betty Plush shopfront or signage stack in frame: BETTY PLUSH 222 · PLT 222 ·
  fiverr/@popeofai/222 · 222 banner
- Branding ON the clothes: oversized BETTY PLUSH 222 hoodies/puffers, PLT cargo embroidery,
  222 caps and chains, "Betty Plush - 222 - PLT" belts, platform boots / chunky sneakers
- Real plushies stacked in frame, with the pink bunny bookbag present
- Palette: pink / teal / gold. Bold flat cartoon style for the stick-figure series.

## Product truth (hard rule)

- Depict ONLY the actual products, locked to the site's product photos as generation references
  (featured map in START-HERE). No generator improvisations, no generic stuffies.
- Product placement standard: real souls displayed AS PRODUCTS (shop window, name cards/designs
  readable), book bags shown as bags with Betty Plush / PLT hang-tags visible, Spike present.
- Spike = grey fluffy monster, three eyes in a pyramid, black spiked collar. Flagship.

## Build pipeline (use the templates in `handoff/`)

1. Pick the episode from the book. Extract, in writing, BEFORE generating anything:
   cast + colors, opening holding, all 5 beats (dialogue + P/L/T/PLT after each beat),
   final score + ◆ + verdicts, takeaway, on-screen words.
2. Generate 3 scene stills (beats 1–2 / beat 3 / beats 4–5), product photos as references.
3. Gate-check the stills against QA-GATE.md yourself before animating. A bad still animated
   is a bad clip.
4. Animate each still: locked camera, small movements only, silent. (Daily video budget —
   if you hit a 429, stop; finish everything else and report.)
5. Copy `build_h11_template.py` (2-character scored episode) or `build_law1_template.py`
   (12-line variant). Patch ONLY the data blocks: LINES, CAPS, STATES, STATE_LINE, CHIPS,
   NAMES, the two PIL cards, scene spans, `src` filenames, output path.
   Template facts: GAP 0.35 · CARD_OPEN 2.4 · scorebug fontsize 40 · chips fontsize 44 at y=238 ·
   cards on dark teal (10,42,48) with the brand footer.
6. Build gotchas, all learned the hard way:
   - Include the ◆ glyphs in the card/caption strings themselves (early episodes shipped without).
   - Score-card verdict lines longer than ~26 characters overflow the frame — split them.
   - ffmpeg concat lists: use ABSOLUTE paths (the demuxer resolves relative to the list file).
   - Never use ffmpeg zoompan (pathologically slow). For a pan, upscale ~1.1× and animate the crop.
   - Re-running a build is safe: it skips TTS lines whose mp3 already exceeds 1000 bytes.
7. Gate-check the finished mp4 (frames at start/middle/end, durations, scorebug values at each beat).
8. Deliver: mp4 to Betty's Library/Drive + a delivery note in `messages/betty-to-soul/`
   with pass/fail counts, file paths, and every flag.

## Do-not-retry list (integrity-check failures — never regenerate these specific requests)

- Animating Betty's uploaded bathroom photo · teal corset sunroom still · gold corset fireplace video
- Red corset rainy-street video · thothsbag video · Dream-Eater video
- Ledger Ep 16 scene-3 handoff still · Ledger Ep 40 scene-3 animation

## Approval and launch

- Campaign fit-check posts: nothing publishes without Ms GCP's approval of the exact post.
- Finished episode clips: Betty's 2026-11-08 rule — the finished clip library uploads as a rolling
  launch. Captions per the posting pack: hook line first, the episode's quote as line 2,
  one score-dispute CTA, 3–5 targeted hashtags max (never #fyp/#viral/#reels).
