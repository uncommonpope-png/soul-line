# START HERE — Betty Plush Episode Workflow Handoff

You are a Muse agent taking over episode production for the Betty Plush / Soul Economy books.
This pack is the workflow. Not a summary — the actual operating files.

## YOUR LANE — the satire comedy philosophy books ONLY

Block Etiquette · The Come Up · The Cookout · The Collection · The Group Chat ·
The Barbershop · The Lowball · The 222 Laws.
These fuse In Living Color sketch-comedy energy (ensemble, recurring characters, catchphrases)
with one named power move per story, judged by PLT scoring. Humor is a hard requirement.
**The Ledger and The Hustle are ALREADY IN PRODUCTION elsewhere — do not touch them,
do not reassign them.** They exist in this repo as format references only.

Read these files in this order:

1. `handoff/START-HERE.md` (this file)
2. `handoff/CURRENT-WORKFLOW.md` — how the newest work was actually made, the Law 1 worked
   example, your production queue, and the status board. **When older files conflict with
   this one, this one wins.**
3. `handoff/WORKFLOW-SOP.md` — the full pipeline, step by step
4. `handoff/QA-GATE.md` — the pass/fail checklist every deliverable is graded against
5. `handoff/TEST-TASK.md` — your first assignment. Do ONLY this until it passes review.

Also in this repo, already pushed:
- `books/` — all ten episode books (Ledger Vol One, The Hustle, The Come Up, Block Etiquette,
  The Cookout, The Collection, The Group Chat, The Barbershop, The Lowball, The 222 Laws).
  Every conversation in them is written as a performable script: dialogue, 5 scored beats,
  on-screen words, score-after, takeaway.
- `product-refs/betty-plush-catalog.json` — the full product catalog (ground truth for products).
- `ledger-episode-index.md`, `ledger-stitch-plan.md` — series index and scoring-on-screen spec.
- `storyboards/block-etiquette-ep1-stoop-rules.md` — the approved storyboard + product-placement
  standard for Block Etiquette Ep 1, your first episode.
- `research/block-etiquette-rulebook.md` — the deep etiquette research rulebook: ground your
  Block Etiquette stories and gags in it (real rules, real social costs, comedy angles).
- `messages/soul-to-betty/2026-11-08-1255-full-directive-for-prophet.md` — brand, cast colors,
  and Hustle H1.1's exact state track. Read it as a FORMAT worked example only — the Hustle
  assignment in it is not yours.
- `handoff/build_h11_template.py` and `handoff/build_law1_template.py` — the two PROVEN episode
  build scripts. Copy one, patch its data blocks. Do not write a new builder from scratch.

## The one rule above all rules

**Prove, don't describe.** Never reply "understood." Your first reply is a RECEIPT
(see TEST-TASK.md) and your proof is a deliverable graded against QA-GATE.md.
Words about the workflow earn nothing. A correct state table and one good scene earn the next task.

## Where things live

- Books + this pack: this repo (`uncommonpope-png/soul-line`).
- Finished clips: Google Drive folder "The Ledger — Volume One (all 62 clips + full movie)"
  and Betty's Library.
- Product photos (the ONLY legal product references):
  `https://uncommonpope-png.github.io/soul-economy/featured/bp-NNN.jpg` and the catalog JSON above.
  Featured map: bp-378 Drippy · bp-382 Mendie · bp-384 Denim Patch · bp-388 Ember Stripe ·
  bp-394 Pixel Heart · bp-398 Bell Paws · bp-405 Nightwing Dawn · bp-407 Listen.
- Your deliverables and reports go in `messages/betty-to-soul/` in this repo, one file per message,
  filename `YYYY-MM-DD-HHMM-short-subject.md`, header: From / To / Date / Subject / Needs reply by.
  **Flags travel with the work, never hidden** — every defect, substitution, or failed generation
  is named in the delivery note.

## Hard stops

- Scores are ONLY ever the book's own numbers. Never invent or "smooth" a score.
- Never invent a soul name, product, price, or quote. Prices: keychain $100 · plushie $400 ·
  purse $800 ($1,000 flagship) · book bag $650 · Full Set $1,950 ($2,150 flagship).
- Betty Plush is an ADULT collectible plush brand. Monsters are never bears. Never children's-toy framing.
- Video generation has a daily account budget. On a 429 / daily-limit error: STOP, do not retry,
  do not schedule retries. Report and do stills/paperwork instead.
- Max 6 video generations per work session batch.
