# Stick-Figure Series — Character System (LOCKED)

**Date:** 2026-11-07
**Series:** PLT book series explainer videos, Craig Jones & Lakeema Jones — 60–90 s, vertical 1080×1920
**Source of truth for the base figure:** pilot `../pilot-mistake-one-75s.mp4` (Book 1, Mistake One) and production plan `../stick-figure-production-plan.md` §5.
**Rule:** the pilot's figure never changes. New figures are built ON it — same skeleton, same head, same line weight — and are told apart by line colour + one prop + one floating symbol. Never add a new accent colour, never redraw the skeleton.

## 0. The pilot lock — starts EVERY image prompt, verbatim

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head.

On-screen labels (MISTAKE 1, THE TAX, etc.) are added in CapCut, NEVER baked into the image. The only baked-in text allowed anywhere in the series is **"PLT"** on the host's pink book prop and **"222"** on the host's badge, plus **"$"** on Profit's coin.

## 1. Shared geometric spec (for the motion/animation builder — reproduce programmatically)

Canvas: **1080 × 1920 px**, white background `#FFFFFF`, figure centred at x = 540.
All measurements below are in px on that canvas. The script that draws Tax and both host variants exactly to this spec is `draw-characters.py` in this folder — re-run it, don't eyeball it.

| Part | Spec |
|---|---|
| Head | Circle, centre (540, 560), radius 190, stroke 16 px, no fill |
| Eyes | Two solid dots, centres (470, 530) and (610, 530), radius 13–16 px |
| Smile (Host / Profit / Love) | Arc, bounding box (470, 560)–(610, 700), 15°–165°, stroke 16 px |
| Mouth (Tax only) | Flat horizontal line (490, 650)–(590, 650), stroke 14 px — Tax never smiles |
| Torso | Straight line (540, 750) → (540, 1150), stroke 16 px |
| Arms | From shoulder (540, 800), stroke 16 px; Host/Profit/Love: angled out/up or holding prop; Tax: drooping down (slumped shoulders) |
| Legs | From hip (540, 1150) to (430, 1650) and (650, 1650), stroke 16 px |
| Feet | Horizontal tick 90 px at each ankle: (430, 1650)→(340, 1650) and (650, 1650)→(740, 1650) |
| Figure height | Head top (y≈370) to feet (y≈1650) ≈ 1,280 px; head diameter (380 px) ≈ 30% of figure height — the big round head IS the recognition cue |
| Line weight | 16 px at 1080 wide (≈1.5% of frame width). Scale proportionally if rendering at another size. |
| Face | Dot eyes + smile/flat mouth only. No nose, no hair (except a figure's locked accessory), no ears. |

### Colour palette (exact hex — no substitutes)

| Colour | Hex | Used by |
|---|---|---|
| Black (line) | `#000000` | Host body lines |
| Hot pink (Betty Plush accent) | `#FF2E88` | Host accessories, book, badge, shoes, tutu, jacket, cap |
| Gold | `#FFB800` | Profit — entire figure + coin + star |
| Red | `#E8112D` | Love — entire figure + hearts |
| Slate grey | `#4A4A4A` | Tax — entire figure + clock + weight + hourglass |
| White | `#FFFFFF` | Background, head fill, "PLT"/"222" lettering |

### At-a-glance test
In a small vertical frame the four must read instantly: **black + pink = Host · all-gold = Profit · all-red = Love · all-grey, slumped = Tax.** If two figures could be confused at thumbnail size, the image has failed — re-roll it.

---

## 2. THE HOST — "YOU"

**File:** `host-base.webp`
**When to use:** every episode, every scene. The host is the "you" in every story — the person making the mistake, learning the correction, holding the book at the takeaway. If a scene has one figure, it is the host.

**Locked description (verbatim prompt text — reuse in every future prompt):**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. THE HOST: the same black stick figure, with a small hot pink bow on the side of the round head, hot pink sneakers, and holding a small hot pink book with the letters PLT on its cover in white. A tiny hot pink badge reading 222 pinned on the chest.

**Locked identifiers (never change, never drop):**
- Black line body, round head, dot eyes, smile.
- Hot pink bow, top-right of head.
- Hot pink book, "PLT" in white — carried in the hand, prominent in the final takeaway scene of every episode (pilot §4, scene 7).
- Hot pink round badge reading "222" on the chest.
- Hot pink shoes.
- Everything else about the host may change per episode (outfit variants below) — these five marks may not.

**Geometric spec:** shared skeleton (§1), line colour `#000000`. Bow: two pink triangles + centre dot at the top-right of the head (≈640–760, 330–430). Book: pink rectangle ≈140 × 220 px at the hand, black outline 8 px, "PLT" white bold ≈52 pt. Badge: pink circle diameter 80 px at chest (≈500–580, 830–910), "222" white bold ≈34 pt. Shoes: pink filled ovals ≈140 × 60 px at the feet.

**Check result (2026-11-07):** PASS — matches the pilot's proportions, line weight and round head; bow, PLT book, 222 badge and pink shoes all present; no extra text.

### 2a. Host outfit variant — PINK TUTU

**File:** `host-tutu.png` (drawn programmatically to the §1 spec — see `draw-characters.py`)
**Locked description:**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. THE HOST IN PINK TUTU: the same black stick figure with the hot pink bow, hot pink badge reading 222, and hot pink book with PLT on its cover, wearing a flared hot pink tutu skirt at the waist and hot pink shoes.

**Spec:** tutu = flared pink fan at the waist (y≈1080–1300), widest ≈420 px, black outline 8 px. All five host identifiers stay on. Use for celebratory / Betty Plush fashion episodes; rotate with the other looks, never the same outfit in every image.

### 2b. Host outfit variant — STREET LOOK

**File:** `host-street.png` (drawn programmatically to the §1 spec — see `draw-characters.py`)
**Locked description:**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. THE HOST IN STREET LOOK: the same black stick figure with the hot pink badge reading 222 and hot pink book with PLT on its cover, wearing a hot pink baseball cap with brim, a hot pink bomber jacket with a black zip line down the centre, and hot pink shoes.

**Spec:** cap = pink dome over the top half of the head + rectangular brim to the right (≈620–820, 520–560) + centre button dot. Jacket = pink rounded rectangle over the torso (470–610, 760–1160), black outline 8 px, black centre zip line. All host identifiers stay on except the bow (replaced by the cap — the one allowed swap). Use for street / confident / everyday-decision episodes.

**Future outfit variants (same rule):** change ONLY the outfit layer (cap/jacket/tutu/hoodie/etc., pink + black, Betty Plush world). Never change the skeleton, head, line weight, or the PLT book + 222 badge. One new outfit per episode at most; rotate, don't repeat.

---

## 3. PROFIT — locked

**File:** `profit.webp`
**When to use:** whenever the narration names Profit, or shows what is gained — money, skill, time leverage, reputation, network, freedom, peace, identity (the 8 forms of Profit, pilot §4 scene 5). Profit appears, holds up the coin, and leaves. Never appears as a black figure — gold is the whole point.

**Locked colour/prop:** **gold `#FFB800` + large gold coin with "$" + gold star.**
**Locked description (verbatim prompt text):**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. PROFIT: the same stick figure proportions and round head, but drawn entirely in solid gold yellow lines (#FFB800) instead of black, holding up a large shiny gold coin with a dollar sign on it in one hand, a small five-pointed gold star floating above the round head.

**Geometric spec:** shared skeleton (§1), ALL lines `#FFB800` (head, torso, arms, legs, face). Coin: gold filled circle, diameter ≈ 0.9 × head diameter, held high in the raised hand, "$" in darker gold/brown centred on it. Star: five-pointed outline star, ≈120 px, floating above the head, gold. Smile: yes — Profit is the upbeat one. No pink anywhere on Profit.

**Check result (2026-11-07):** PASS — gold figure, coin with "$" held high, star above head, same head/proportions as pilot.

---

## 4. LOVE — locked

**File:** `love.webp`
**When to use:** whenever the narration names Love, or shows what is felt/kept — relationships, peace, belonging, who you are becoming. Love holds the heart against the chest. Never appears as a black or pink figure — red is the whole point (red also keeps Love distinct from the host's hot pink).

**Locked colour/prop:** **red `#E8112D` + large solid red heart held to the chest + small red heart above the head.**
**Locked description (verbatim prompt text):**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. LOVE: the same stick figure proportions and round head, but drawn entirely in solid bright red lines (#E8112D) instead of black, holding a large solid red heart with both hands against the chest, a small red heart floating above the round head.

**Geometric spec:** shared skeleton (§1), ALL lines `#E8112D`. Big heart: solid red, ≈ head-width or slightly wider, centred on the chest, arms wrapped around it. Small heart: solid red, ≈120 px, floating above the head. Smile: yes — warmest smile of the four. No pink anywhere on Love; the heart is red, not pink, so it never reads as the host's accent.

**Check result (2026-11-07):** PASS — red figure, big heart held to chest, small heart above head, same head/proportions as pilot. (The big heart covers the torso — that is the design, not a flaw.)

---

## 5. TAX — locked

**File:** `tax.png` (canonical — drawn programmatically to the §1 spec)
**When to use:** whenever the narration names Tax, or shows what a choice costs — time, stress, opportunity, relationship, health, integrity (the 6 forms of Tax, pilot §4 scene 5). Tax arrives, the weight drops, the clock ticks. Tax is the only figure that never smiles.

**Locked colour/prop:** **slate grey `#4A4A4A` + round grey clock + heavy grey iron weight + grey hourglass.**
**Locked description (verbatim prompt text):**

> Simple black stick figure, round head, thin black line body, white background, flat 2D cartoon style, no shading, no text in the image. One accent color only: hot pink (#FF2E88) for objects that matter. The figure is the same in every scene: same proportions, same line weight, same round head. TAX: the same stick figure proportions and round head, but drawn entirely in solid dark slate grey lines (#4A4A4A) instead of black, holding a round grey clock with black hands in one hand, a heavy grey iron weight hanging from the other hand, a small grey hourglass floating above the round head. Tax has a flat straight mouth, never a smile, and slightly slumped shoulders.

**Geometric spec:** shared skeleton (§1), ALL lines `#4A4A4A`. Clock: grey-rimmed circle, diameter ≈240 px, in the left hand, hands at 12 and ~4. Weight: solid grey kettlebell/iron weight, ≈190 px diameter, hanging from the right hand by its handle. Hourglass: grey outline, ≈220 px tall, floating above the head, grey sand in both bulbs. Mouth: flat line (§1) — never a smile. Shoulders/arms droop downward. **No pink anywhere on Tax — pink props are a fail (see drift note below).**

**Check result / drift note (2026-11-07):** the first AI-generated Tax (`tax-v1-pink-props-DRIFT.webp`, kept in this folder as evidence, NOT canonical) came back with the figure correctly grey but all three props rendered in hot pink, plus a smile — that breaks the lock, because pink props make Tax read as the host. It was re-drawn programmatically as `tax.png` with all-grey props, flat mouth and slumped shoulders: PASS. Do not use the v1 file in any episode. If a future AI re-roll ever puts pink on Tax again, reject it on sight — Tax is grey, end to end.

---

## 6. How to use the cast in an episode

- **Host = the "you"** in every story; in every scene unless the beat is purely about one of the three.
- **Profit / Love / Tax appear only when the narration names them** (or shows their thing: a gain, a feeling, a cost). They enter, do their one action (coin up / heart held / weight dropped), and leave. They never carry the story alone.
- **Pilot mapping (Book 1, Mistake One):** scene 1–2 host + Profit's coin (green "$" in the pilot is the scene prop, not Profit himself); scene 3 Tax (clock/heart/shield cracking — Tax's clock + weight); scene 4 host at the equation; scene 5 Profit + Love + Tax together around the balance scale; scene 6 host, correction; scene 7 host with the PLT book.
- **Never put two figures in the same colour.** If Profit and Love share a frame, gold vs red does the work — no labels needed.
- **New figures:** do not invent a fourth PLT figure. Anything else in a scene (boss, friend, crowd) is a plain black pilot figure with NO pink bow/book/badge — the host's marks are what make the host the host.

## 7. Files in this folder

| File | Figure | Status |
|---|---|---|
| `host-base.webp` | Host (base) | PASS, AI-generated, checked full-size |
| `host-tutu.png` | Host — pink tutu variant | PASS, programmatic to §1 spec, checked full-size |
| `host-street.png` | Host — street variant | PASS, programmatic to §1 spec, checked full-size (cap fixed after first draw) |
| `profit.webp` | Profit | PASS, AI-generated, checked full-size |
| `love.webp` | Love | PASS, AI-generated, checked full-size |
| `tax.png` | Tax (canonical) | PASS, programmatic to §1 spec, checked full-size |
| `tax-v1-pink-props-DRIFT.webp` | Tax v1 — REJECTED | Pink props + smile; kept as drift evidence only, do not use |
| `draw-characters.py` | Builder script for Tax + host variants | Re-run to reproduce exactly |
| `characters.md` | This file | — |

## 8. Verification (2026-11-07)

- Read `../stick-figure-production-plan.md` §5 (character lock) and §4 (pilot scenes) first; extracted a frame from `../pilot-mistake-one-75s.mp4` and used it as the visual reference for all four AI generations.
- Every image above was opened and checked at full size before being kept: same round head, same proportions, same line weight as the pilot; no baked-in text except "PLT", "222", and "$" as allowed.
- One drift found and fixed in this pass: Tax v1 pink props (re-drawn, not re-rolled through the AI tool, to guarantee the grey lock). One minor flaw noted and kept: the hourglass on `tax.png` slightly overlaps the top of Tax's head; the "222" on the tutu variant's badge slightly overflows its circle — both cosmetic, neither breaks recognition.
- $0 spent. Nothing published or uploaded. Soul Economy repo / live site untouched.
