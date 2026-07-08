# STITCH PROMPT — Smuppy V2 · Post Creation Flow (2 screens + 4 popups × Light + Dark)

> Ready to copy-paste to Stitch. Mirrors the REAL code flow:
> CreatePostScreen → AddPostDetailsScreen → PostSuccessScreen (+ Visibility / Location / Tag / Vibes modals).

---

## Context

Design the **post creation flow** for **Smuppy** — a calm, premium fitness/wellness social app.
Reference architecture = **Instagram Feed** composer (pick media → caption + options → publish), restyled to Smuppy's calm wellness aesthetic.

iPhone 14 Pro frame · **393 × 852** · render each screen in **Light AND Dark**.
Vibe : Calm + Headspace + lululemon. Airy, never flashy.

---

## Brand identity (strict — do not deviate)

- **Font** : Plus Jakarta Sans only (weights 400 / 500 / 600 / 700 / 800).
- **Primary mint** : `#26C1A4` solid (95% of UI). Dark-mode mint highlight : `#4EDCBE`.
- **Gradient (hero only, 5–8% of UI)** : `linear-gradient(135deg, #11E3A3 0%, #00B3C7 100%)` — ONLY for the publish CTA + success popup primary button. NEVER on body fills.
- **Dark mode background** = pure `#000000`. Never navy. Surface `#0A0A0C`, container `#14141A`, text `#F1F4F6`, sub `#8B8B95`, outline `#26262E`.
- **Light mode** = page `#FFFFFF`, container `#F5F7F8`, text `#0F1419`, sub `#5A6671`, outline `#CFD6DA`.
- **Section labels** : 11px, weight 700, letter-spacing 0.10em, UPPERCASE, color `#94A3B8` (light) / `#6B6B75` (dark).
- **Mint glow** on active controls / selected media / primary CTA : `box-shadow: 0 0 16px rgba(38,193,164,.45)`.
- **Radius** : cards 16, media 20, pills 999. **Motion** : max 220ms ease `cubic-bezier(.4,0,.2,1)`. **No bounce, ever.**

---

## SCREEN 1 — Pick media (CreatePostScreen)

Full-bleed media-picker, Instagram-composer layout.

1. **Topbar** (fixed, 56px, glass `backdrop-filter:blur(20px) saturate(180%)`):
   - Left : `close` ✕ (40×40).
   - Center : title "Nouvelle publication" (16px / 700).
   - Right : **"Suivant"** text button (mint `#26C1A4`, 14px / 700) — disabled/40%-opacity until ≥1 media selected.

2. **Live preview** (top, full-width, height ≈ 295px, bg container):
   - Shows the currently-selected media (image fill). Multi-select badge bottom-right "1/10".
   - If a video : small `play_circle` overlay + duration chip "0:14" bottom-left.

3. **Gallery toolbar** row under preview:
   - Left : "Pellicule ▾" dropdown chip (album selector).
   - Right : `photo_camera` glass icon button (opens camera) + a `layers` multi-select toggle (mint when active).

4. **Gallery grid** : 3 columns, 4px gap, square cells, fills rest of screen.
   - Selected cells : mint 2px ring + numbered badge (1, 2, 3…) top-right, max **10**.
   - Each video cell : tiny duration chip bottom-right.

> Note : Pro/Premium creators see an extra **"Vibes"** entry point (mint sparkle chip in the toolbar) → opens the Vibes popup (below). Free users do not.

---

## SCREEN 2 — Post details (AddPostDetailsScreen)

Scrollable form, calm card layout.

1. **Topbar** : `arrow_back` (left) · title "Détails" (center) · **"Publier"** mint text button (right, 14px / 700).

2. **Author + caption block** (top card, radius 16):
   - Row : 40×40 round avatar + display name "Sarah Coach" (15px / 700).
   - Multi-line `textarea`, placeholder "Écris une légende…", min 3 rows, 15px / 400.
   - Bottom-right char counter "0 / 2200" (sub color).

3. **Section — OPTIONS** (UPPERCASE label + card with hairline-divided rows). Each row = tinted icon-chip (34×34, radius 11, hue@10%) + label + current value + chevron-right:
   - `public` (mint) — "Qui peut voir" — value "Tout le monde" → opens **Visibility popup**.
   - `location_on` (blue) — "Lieu" — value "Ajouter un lieu" (sub when empty / text when set) → opens **Location popup**.
   - `person_add` (purple) — "Identifier des personnes" — value "Ajouter" / "3 personnes" → opens **Tag popup**.

4. **Helper note** (sub, 12px) : "Ta publication apparaît dans le feed de tes fans selon ta visibilité."

---

## SCREEN 3 — Success (PostSuccessScreen)

Centered, calm:
- Mint `check_circle` icon (64px) with glow.
- "Publication en ligne 🎉" (20px / 800).
- "Tes fans peuvent maintenant la voir." (14px / 500, sub).
- Stacked CTAs : **"Voir ma publication"** (gradient pill, 54px) + **"Créer une autre"** (ghost).

---

## 4 bottom-sheet popups (V2 BottomSheet — slide up, scrim w/ blur, top corners radius 24)

- **Visibility popup** : title "Qui peut voir cette publication". Selectable rows w/ radio + icon-chip + description sub-line (selected = mint check + mint-tinted bg). Real options (canonical, from `usePostForm.ts`):
  - `globe-outline` **Public** — "Tout le monde peut voir cette publication" (default).
  - `people-outline` **Réservé aux fans** — "Seuls tes fans peuvent la voir".
  - `lock-closed-outline` **Privé** — "Toi seul peux la voir".
  - `star-outline` **Abonnés payants** — "Seuls les abonnés payants de ta chaîne" — **shown only for pro_creator with a channel** (4th conditional row).
- **Location popup** : search field `search` "Rechercher un lieu" + list of nearby place rows (`place` icon + name + city sub). Tapping a row selects + closes.
- **Tag popup** : search field "Rechercher des personnes" + list rows (avatar + name + username sub + add `+` button that turns into mint check when added). Selected count chip at top.
- **Vibes popup** (Pro only) : title "Publier en Vibes ?" + short explainer "Les Vibes sont des posts éphémères mis en avant 24 h." + mint toggle + "Continuer" CTA.

---

## Output

- **6 HTML files** : Screen 1 + Screen 2 + Screen 3, each in Light + Dark.
- **4 popup variants** rendered on top of Screen 2 (Visibility, Location, Tag, Vibes).
- All strings in French (literals above are canonical).
- Inputs : 15px / 400. Icon-chips : 34×34 radius 11, hue@10% bg. Toggles : iOS-style 46×28, mint w/ glow when ON.
- Max transition 220ms ease-out. No bouncy animation.

## Why this matters

Post is the core creation loop (Instagram Feed canonical). Calm composer, never cluttered. The 2-screen split (pick → details) + option-row pattern mirrors Instagram while staying inside Smuppy's wellness DS.
