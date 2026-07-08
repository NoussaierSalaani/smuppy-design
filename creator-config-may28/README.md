# Creator Config — design package (2026-05-28)

Branch : `design/creator-config-may28` · isolated from `main` and from Hamza's work.

## What's in here

| File | Purpose |
|---|---|
| `maquettes/build_creator_config_v2.py` | Python generator for the 6 HTML maquettes (3 screens × light/dark). Pure stdlib, run `python3` to regenerate. |
| `maquettes/harmonized/creator_{screen}_v2_{light,dark}/code.html` | Generated HTML maquettes (each 18–28 KB, single file, no external assets except Google Fonts + Material Symbols). |
| `maquettes/index.html` | iPhone-frame preview grid that loads all 6 maquettes in iframes. Open in any browser. |
| `prompts/STITCH_PROMPT_creator_config_v2.md` | Single merged Stitch prompt ready to copy-paste — contains full spec for all 3 screens + 3 popups. |
| `MIGRATIONS_TODO.md` | Backend deltas required to ship the maquettes (9 migrations, ~7 dev-days). |
| `_verify/*.png` | Reference screenshots at 480×900 (Chrome bug workaround for ≤393px viewport). |
| `README.md` | This file. |

## How to preview locally

```bash
cd /tmp/smuppy-v2-recovery        # or wherever maquettes/index.html lives
python3 -m http.server 8765 --bind 127.0.0.1
open http://127.0.0.1:8765/maquettes/   # opens the iPhone-frame grid
```

Append `#success` / `#leave` / `#slot-editor` to any maquette URL to open the corresponding bottom-sheet popup. Example :

```
http://127.0.0.1:8765/maquettes/harmonized/creator_1on1_setup_v2_dark/code.html#slot-editor
```

## Scope decisions taken in this session (2026-05-28)

| Topic | Decision |
|---|---|
| Bottom nav on subscreens | **Removed** — back-arrow only (V2 brand-rules #10). |
| Channel free trial | **Removed** — founder lock since Apr 29 ("pas d'essai gratuit pour pas de complexité"). |
| Channel identity (name + tagline rows) | **Removed** — profile display name auto-used; hero shows it as preview only. |
| 1:1 duration set | **5 durations [15, 30, 45, 60, 90]** — adds 15min to existing code set, no removals. |
| 1:1 pricing | **Multi-duration, per-duration price** (replaces single-duration field). Migration `creator_session_offerings`. |
| 1:1 availability | **Multi-slot per day** (UI exposes the multi-slot DB capability that already exists in `sessions/settings.ts`). |
| 1:1 closed dates | **New section "Dates fermées"** + new table `creator_closed_dates`. |
| Save flow | **Success bottom sheet** (V2 BottomSheet, mint check icon, "Voir ma chaîne" + "Fermer"). |
| Back with unsaved | **Confirm-leave bottom sheet** (amber warn, "Continuer la config" ghost + "Quitter quand même" danger). |
| Tap day to edit slots | **Slot-editor bottom sheet** (per-slot delete, "+ Ajouter une plage", "Fermer ce jour" danger CTA). |

## Open questions for founder (in MIGRATIONS_TODO.md)

1. Cover photo aspect / max size
2. Pack duration unit picker (mois/semaines/jours)
3. Promo price : explicit savings % field or compute server-side ?
4. Currency : EUR-only V1 or multi-currency ?

## Status

- ✅ All 3 screens designed (light + dark)
- ✅ All 3 popups designed (success + leave + slot-editor)
- ✅ Stitch prompt finalized + single-file ready to paste
- ✅ Backend migration spec written
- ⏳ Founder visual validation in real browser pending
- ⏳ Engineering kickoff (migrations 194 / 195 / 196) pending
