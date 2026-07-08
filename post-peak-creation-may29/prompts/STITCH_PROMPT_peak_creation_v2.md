# STITCH PROMPT — Smuppy V2 · Peak Creation Flow (single minimal editor + 2 popups × Light + Dark)

> Ready to copy-paste to Stitch. Mirrors the REAL code: CreatePeakScreen is a SINGLE minimal editor.
> AUTHORITATIVE source = `docs/features/PEAK_BEHAVIOR_CONTRACT.md` v3 §8 (2026-05-10).
> ⚠️ `docs/features/PEAKS.md §5` is STALE (describes a dead 3-screen flow + stickers/audio/PeakSync) — do NOT use it.
> KEEP = record/pick → trim, cover, sound on/off, caption, challenge toggle, submit + (v3) recording timer, speed presets, tone presets.
> KILLED (do NOT design) = stickers, text/location/mention overlays, smart-edit, draggable items, advanced panel, separate Edit/Preview screens, audience/feed-duration/save-to-gallery settings.

---

## Context

Design the **Peak creation flow** for **Smuppy** — a calm, premium fitness/wellness social app.
Peaks = short vertical 9:16 videos, ephemeral. Reference architecture = **Instagram Reels / TikTok** camera, but radically SIMPLIFIED to one calm editor screen.

iPhone 14 Pro frame · **393 × 852** · render in **Light AND Dark**.
This is a **full-bleed video / camera surface** — dark UI chrome over the footage in both modes, but the bottom control sheet follows Light/Dark theme.

---

## Brand identity (strict — do not deviate)

- **Font** : Plus Jakarta Sans only (400 / 500 / 600 / 700 / 800).
- **Primary mint** : `#26C1A4` solid. Dark-mode mint highlight : `#4EDCBE`.
- **Gradient (hero only)** : `linear-gradient(135deg, #11E3A3 0%, #00B3C7 100%)` — ONLY for the "Publier" CTA. Nothing else.
- **Over-footage chrome** : white icons + glass pills `rgba(0,0,0,.35) blur(20px)` so they read on any video.
- **Control sheet** : Light = `#FFFFFF`; Dark = pure `#000000` surface `#0A0A0C`. Section sub-text `#8B8B95` dark / `#5A6671` light.
- **Mint glow** on active controls (sound ON, challenge ON, record): `box-shadow: 0 0 16px rgba(38,193,164,.45)`.
- Radius : pills 999, sheet top corners 24, chips 12. Motion ≤ 220ms ease. **No bounce.**

---

## SCREEN 1a — Capture state (camera live)

Full-bleed camera viewfinder.

1. **Top overlay** (glass icons over footage):
   - Left : `close` ✕ glass button.
   - Right column (stacked 44×44 glass buttons) : `flip_camera_ios`, `bolt` (flash).
   - **Recording elapsed timer** : centered top, `MM:SS` glass pill (e.g. "00:07"), only while recording. **Pulses red `#FF453A`** when elapsed ≥ 90% of the picked duration.

2. **Right-edge duration selector** (vertical pill stack, glass): **6s · 10s · 15s · 60s** — default **10s** active = mint pill w/ glow. (Maps to DURATION_OPTIONS.)

3. **Speed preset (pre-record only)** : 3-pill segmented control just above the record button — **0.5× · 1× · 2×** (default 1×, selected = mint pill + glow). Uniform speed, locked once recording starts. (Capture-step control per contract §8.1 — NOT shown in the edit state.)

4. **Bottom controls**:
   - Center : large **record button** — white ring 76px, mint inner dot; tap = record, long-press = hold-to-record (min 3s), recording = morphs to a rounded-square + animated mint progress ring.
   - Left of record : `photo_library` glass button → "Importer" (gallery pick, video only, max 60s).

---

## SCREEN 1b — Edit state (after record/pick — SAME screen, controls swap in)

Footage now plays in a 9:16 preview. A calm control sheet replaces the camera controls. THIS is the canonical Peak editor — one screen, no navigation to a second editor.

1. **Top overlay** : `arrow_back` ✕ (discard, glass, opens Discard popup) · right : `music_note` "Son" glass chip.

2. **Trim bar** (TrimBar) : horizontal filmstrip of thumbnails near bottom of preview, two mint draggable handles (start/end), selected range highlighted mint, duration label center "0:14".

3. **Quick-tools row** (over footage, glass chips, horizontally scrollable):
   - `image` "Couverture" → opens cover-frame scrubber (filmstrip slider + "Définir la couverture" button captures current frame as thumbnail).
   - `volume_up` / `volume_off` "Son original" — toggle (mint when ON, glow). Default ON.
   - `tune` "Tons" → opens **TonePicker** : a row of **8** swatch presets (selected = mint ring) — **Aucun · Éclatant · Froid · Chaud · N&B · Fondu · Boost · Aurora**. Tones = ColorMatrix presets only, NOT filters/stickers. (Edit-step, pre-trim.)
   - `music_note` "Son" → opens Smuppy Sounds catalog (optional attach track).

   > Do NOT add a speed chip here — speed is a capture-step control (Screen 1a) only.

4. **Bottom control sheet** (theme-aware, top corners radius 24):
   - **Caption** : multi-line textarea, placeholder "Ajoute une légende…", 15px / 400, char counter "0 / 2200" bottom-right.
   - **Challenge row** : `emoji_events` (gold icon-chip 34×34) + "Lancer un défi" + sub "Tes fans pourront répondre avec leur propre Peak" + mint toggle (glow when ON). When ON, the caption doubles as the challenge title + an "Inviter des amis" link appears (opens TagFriendModal).
   - **Sticky CTA** : full-width **"Publier"** gradient pill 54px w/ drop-shadow. Above it a fade `linear-gradient(180deg, transparent, var(--surface))`.

> Post-publish behaviour (do NOT design a success screen here unless asked) : upload enqueues in background, a small mint **toast** "Peak en cours d'envoi…" appears, screen closes to feed. Optionally render this toast variant.

---

## Popups & sheets (V2 BottomSheet — slide up, scrim w/ blur, top corners radius 24)

- **Sounds sheet** : title "Sons Smuppy". Search field + scrollable list rows (waveform thumb + track name + artist sub + duration + play `play_arrow`). Selected row = mint check. (Opened by the `music_note` chip.)
- **Discard popup** : amber `warning` icon-chip + "Supprimer ce Peak ?" + "Ta vidéo et tes réglages seront perdus." + side-by-side CTAs : "Continuer l'édition" (ghost) + "Supprimer" (danger-red outline `#E53935`).

> No "Speed popup" — speed is an inline 3-pill segmented control on the capture screen (1a), not a sheet.

---

## Output

- **HTML files** : Screen 1a (capture) + Screen 1b (edit), each in Light + Dark = **4 files**.
- **2 sheet/popup variants** (Sounds sheet, Discard popup) rendered on top of the edit state.
- Optional : the "Peak en cours d'envoi…" toast variant.
- All strings in French (literals above are canonical).
- Over-footage chrome = white + glass-dark pills BOTH themes; control sheet follows theme.
- Toggles : iOS-style 46×28, mint w/ glow when ON. Max transition 220ms ease-out. No bounce.

## Why this matters

Peaks = Reels/TikTok canonical, but Smuppy deliberately stripped the editor to ONE calm screen (the code already killed stickers/overlays/smart-edit). The design MUST stay minimal — adding a multi-step editor or sticker tray would re-introduce dead UI the codebase already removed.
