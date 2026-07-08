# STITCH PROMPT — Smuppy V2 · Creator Config Screens (3 screens × Light + Dark)

> Final merged prompt — generated 2026-05-28 after founder validation loop.
> Ready to copy-paste to Stitch.

---

## Context

Design 3 mobile config screens for **Smuppy** — a calm, premium fitness/wellness social app.
Audience : pro_creator ($99.99/mo) configuring their monetization tools.

iPhone 14 Pro frame · **393 × 852** · render each in **Light AND Dark**.
Vibe : Calm + Headspace + lululemon. Wellness, airy, never flashy.

---

## Brand identity (strict — do not deviate)

- **Font** : Plus Jakarta Sans only (weights 400 / 500 / 600 / 700 / 800).
- **Primary mint** : `#26C1A4` solid (95% of UI). Dark-mode mint highlight : `#4EDCBE`.
- **Gradient (hero only, 5–8% of UI)** : `linear-gradient(135deg, #11E3A3 0%, #00B3C7 100%)` — for the sticky CTA pill and success popup primary button. NEVER on body fills.
- **Dark mode background** = pure `#000000`. Never navy.
- **Light mode background** = `#F6F8FA` (page), `#FFFFFF` (cards).
- **Section labels** : 11px, weight 700, letter-spacing 0.10em, UPPERCASE, color `#94A3B8` (light) / `#6B6B75` (dark).
- **Subtle mint glow** on every active control (toggle ON, primary CTA) : `box-shadow: 0 0 16px rgba(38,193,164,.45)`.

---

## Universal layout (apply to all 3 screens)

1. **Topbar** (fixed, 56px, glass blur `backdrop-filter:blur(20px) saturate(180%)`) :
   - Left : `arrow_back` chevron (40 × 40 button)
   - Center : screen title (16px / 700)
   - Right : empty 40 × 40 spacer (centers title)
   - **NO bottom navigation** — these are subscreens per V2 rule #10.

2. **Sections** :
   - UPPERCASE label + rounded card (radius 18, light shadow).
   - Card contains rows separated by hairline dividers.
   - Each row : tinted icon chip (34×34, radius 11, `bg = hue @ 10%`) + label (+ optional sublabel) + control on the right.

3. **Sticky CTA** (fixed bottom, full-width pill 54px, gradient mint, drop-shadow) :
   - Above CTA, a `linear-gradient(180deg, transparent, var(--page) 50%)` fades the content behind.

4. **3 bottom-sheet popups** (V2 BottomSheet style — slide up from bottom, scrim w/ blur, radius 24/24/0/0 top corners) :
   - **Success popup** : opens after Save. Mint check icon w/ glow · "Chaîne publiée 🎉" · "Tes fans peuvent maintenant s'abonner." · 2 stacked CTAs ("Voir ma chaîne" primary, "Fermer" ghost).
   - **Confirm-leave popup** : opens if user taps back with unsaved edits. Amber warn icon · "Quitter sans enregistrer ?" · "Tes modifications ne seront pas conservées." · 2 side-by-side CTAs ("Continuer la config" ghost, "Quitter quand même" danger-red outline).
   - **Slot-editor popup** (1:1 setup only) : opens when creator taps a day row. "Lundi · plages d'ouverture" · 2 slot rows (09:00 – 12:00 + 14:00 – 19:00, each with delete trash icon) · "+ Ajouter une plage" mint dashed CTA · "Fermer ce jour" (danger) + "Enregistrer" (primary).

---

## SCREEN 1 — Channel setup

**Hero** (preview-only, no editable text overlay) :
- Tappable cover-photo card, full width, aspect-ratio 5/4, radius 24.
- Top-right glass badge with `photo_camera` icon + "Changer la couverture".
- Bottom-left overlay : pill "APERÇU" (10px UPPERCASE) + `<profile display name>` (22px / 800) + "Ton nom de profil sera utilisé automatiquement" (13px / 500).

**Section — Abonnement mensuel**
- Row : `euro` icon (mint) — "Prix mensuel" + sublabel "Prix vu par tes fans · TVA incluse" — input `9,99 €` (mint-tinted).

**Section — Avantages abonnés**
- Benefit rows (mint `check_circle` filled icon + text + ✕ remove):
  - "Accès à tous les lives"
  - "Posts réservés aux abonnés"
  - "Réductions sur les sessions 1:1"
- Add row: `+ Ajouter un avantage` (mint, dashed top).

**Helper note** : "Commission Smuppy **20–40%** sur les abonnements, dégressive selon la taille de ta communauté."

**Sticky CTA** : **Publier la chaîne**.

> **Removed vs prior versions** : channel name + tagline rows (founder may28 13:15 : "on peut aussi supprimer le tagline et le nom de la chaîne" → profile display name covers it). Free trial toggle (founder lock since Apr 29).

---

## SCREEN 2 — 1:1 setup (the richest screen)

**Hero compact** (mint-tinted gradient card) :
- 48 × 48 icon chip : `video_camera_front` (mint, FILL 1) + mint glow.
- Title "Sessions 1:1 en vidéo" + sub "Coaching direct via Agora · facturation auto".

**Section — Durées proposées** (5 rows, fixed set)
- `15 min` · ACTIF · `15 €` · toggle ON
- `30 min` · ACTIF · `28 €` · toggle ON
- `45 min` · INACTIF · `—` · toggle OFF
- `60 min` · ACTIF · `45 €` · toggle ON
- `90 min` · ACTIF · `69 €` · toggle ON

**Section — Disponibilités · plages multiples**
- 7 day-rows (Lun → Dim), each = `event` icon chip (mint) + day name + slots summary on right + chevron.
- Lun : "09:00 – 12:00 · 14:00 – 19:00" (multi-slot example)
- Mar : "09:00 – 19:00"
- Mer : "10:00 – 17:00"
- Jeu : "09:00 – 12:00 · 14:00 – 19:00"
- Ven : "09:00 – 16:00"
- Sam : "10:00 – 14:00"
- Dim : `do_not_disturb_on` icon (gray) + "Fermé" pill
- Tap any day → opens the **slot-editor bottom sheet** (see popup spec above).

**Section — Dates fermées · vacances · jours fériés**
- Flex-wrap grid of gold-tinted chips :
  - "14 juillet · Fête nationale" + ✕
  - "15 août · Assomption" + ✕
  - "20 – 28 août · Vacances" + ✕
- Add row: `+ Ajouter une date fermée` (mint, dashed top).

**Section — Sujet par défaut · optionnel** (collapsed-style)
- Padded textarea 2 rows, placeholder "Ex. Revue de programme et objectifs du mois…"
- Char counter "0 / 240".

**Helper note** : "Vidéo en direct via Agora · commission Smuppy **20%** sur chaque session."

**Sticky CTA** : **Enregistrer**.

---

## SCREEN 3 — Package setup

**Hero compact** :
- Icon : `inventory_2` mint FILL 1
- Title : "Packs de coaching" + sub "Tu remplis chaque pack avec tes propres services"

**Section — Tes packs publiés**
- One existing pack row :
  - 48 × 48 thumb with pastel-coral gradient (`#FFB4A2 → #FFCFD2`) and white `rocket_launch` icon
  - Name : **Kickstart** + sub "1 mois · 149 € · 24 abonnés actifs" + chevron-right.

**Section — Nouveau pack** (editor)
- Row : `edit_note` (purple) — "Titre du pack" — `Transformation`.
- Row : `timer` (blue) — "Durée" — `3 mois` (free text).
- Subsection header "INCLUS DANS CE PACK" (separator + UPPERCASE label).
- 3 benefit rows (mint check + text + ✕):
  - "2 sessions 1:1 / semaine"
  - "Plan nutrition personnalisé"
  - "Support WhatsApp quotidien"
- Add row: `+ Ajouter un service` (mint).
- Separator + price block:
  - Row : `strikethrough_s` (slate) — "Prix barré (promo)" — `320 €`.
  - Row : `euro` (mint) — "Prix final" — `269 €` (mint-tinted).
  - Row : `workspace_premium` (gold) — "Badge (optionnel)" — `Best seller`.

**Helper note** : "Tu remplis chaque pack avec **tes propres services**. Commission Smuppy **20%** sur chaque vente."

**Sticky CTA** : **Enregistrer le pack**.

---

## Output

- **6 HTML files** for the 3 screens (light + dark).
- **3 popup variants** rendered on top of each screen (success, leave, slot-editor for 1:1 only).
- All in French (string literals above are canonical).
- No bouncy animations. Max transition 220ms ease-out.
- Inputs : 13px / 600, border 1px, radius 10, right-aligned value.
- Toggles : iOS-style 46×28 track, white knob, mint when ON with glow `0 0 16px rgba(38,193,164,.45)`.

---

## Why this matters

Monetization core of pro_creator $99.99/mo. Calm, never flashy. Architecture mirrors Cal.com / Mindbody / Patreon : one config screen per feature, reachable from Settings → CREATOR section, no parallel routes.

Multi-slot per day + closed-dates picker mirrors Mindbody's professional-tier scheduling — addresses the founder's flagged gap "comment le créateur peut supprimer des heures de la journée ou des jours fériés".
