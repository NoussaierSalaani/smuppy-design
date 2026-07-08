# Smuppy — App Store Screenshot Set (iOS)

Generated from the **validated V2 design** (mint two-tier: vivid `#54D6A6` dark / `#2FC9A2` light,
accent text `#6FE3BC` / `#0B7A62`, dark `#000` background). Built as HTML → rendered to PNG via
Chrome headless `--force-device-scale-factor=2` at window `645×1398` (= **1290×2796 @2x**).

**Key change vs previous set:** every media slot now shows a **real photo** (feed posts, avatars,
Peaks/Live thumbnails, profile cover + avatar, search creator avatars, live background, activity
cards, map). No more solid-color/gradient placeholder blocks. Theme = fitness / sport / running /
yoga / wellness / lifestyle.

- **Mode:** dark (primary)
- **Names:** display names only — **no `@username` anywhere** (per founder rule)
- **Imagery source:** **Unsplash** photo URLs (Unsplash License = free commercial use, no attribution
  required), embedded directly and rendered **ONLINE** (Chrome headless fetched remote images
  successfully — verified non-blank, 72k+ distinct colors in a test render).
- **No fabricated price:** the channel card shows "Abonnement chaîne" / "Contenu exclusif" with **no
  hardcoded amount** (price is creator-set/variable). Smups screen uses the in-app Smups currency
  (50 / 200 / 500 Smups), not euro/USD charged-price claims. Price sweep across all HTML = empty.
- **Apple-safe captions:** no superlatives, no Apple trademark misuse.
- **No app code touched, no git commit.**

## Files

| File | Caption (mint headline) | Real imagery | ASC size |
|------|-------------------------|--------------|----------|
| `01_home.png` | **Ton feed, tes fans** | **full `HomeFeedView`**: appbar (bell·wordmark·search) → **Fan·Vibes·Xplorer pills** (Fan active, icons — NOT a Fans/Vibes toggle) → "Peaks & Live" rail (LIVE + ▶views) → **"Suggestions pour toi" rail** (CreatorCard + Devenir fan) → "Ta tribu" post (avatar·name·verified·`Central Park · 2h`·caption w/ mint #hashtag·like·share·save) | 1290 × 2796 |
| `02_peaks.png` | **Peaks & lives en direct** | 2-col vertical-video thumbs (run/box/pilates/trail) + LIVE tags + viewer counts | 1290 × 2796 |
| `03_profile.png` | **Ta chaîne, ton contenu exclusif** | **`ProfileScreenV2`/ProfileShellView CENTERED owner layout**: cover (back · ⚙ gear) → **centered** avatar (mint ring) + name+verified + role line + bio w/ mint #hashtags → **Modifier** (wide) + message/share → **centered** stats (Fans·Posts·Peaks) → Lifestyle/Channel group tabs → **Posts·Peaks·Activités·Enregistrés** tab row → 3-col content grid | 1290 × 2796 |
| `04_search.png` | **Découvre créateurs, lieux & events** | live thumbnails row + suggested-creator avatars | 1290 × 2796 |
| `05_run.png` | **Cours, partage ton tracé en Peak** | immersive dark map bg + neon mint route + hero metric (5,24 km) | 1290 × 2796 |
| `06_create.png` | **Crée en quelques secondes** | `PostCreateMenuView` style-C sheet "Que veux-tu créer ?" — Post / Peak / Go Live rows over blurred real photo | 1290 × 2796 |
| `07_messages.png` | **Discute avec ta tribu** | 1:1 chat, real avatars + photo message | 1290 × 2796 |
| `08_live.png` | **Lives interactifs en direct** | `ViewerLiveStreamView`: full-bleed live (boxing) + creator photo + viewer count + LIVE + chat avatars + reactions (❤️·🔥·👊 Smups·share) | 1290 × 2796 |
| `09_activities.png` | **Organise & rejoins des activités** | activity cards (run/yoga photos) + map heatmap w/ mint pins + attendee faces | 1290 × 2796 |
| `10_smups.png` | **Soutiens tes créateurs** | `SmupWalletView`: "Wallet Smups" + balance **in Smups units (412, no euro)** + Acheter/Envoyer + creator target avatar + send amounts (50·200·500 Smups) | 1290 × 2796 |

## Layout

Each PNG = a marketing caption band (mint headline ~64px bold + grey sub-line) above an iPhone device
frame (notch + status bar). Home / Peaks / Search / Activities / Smups render the canonical V2 5-slot
bottom nav (Home · Peaks · FAB · Messages · Profile, profile slot = real avatar). Run / Create /
Messages / Live are full-bleed immersive states (no bottom nav, matching the maquettes).

## Imagery

All photos are **Unsplash** (`https://images.unsplash.com/photo-…?w=…&q=80`), Unsplash License =
free for commercial use, no attribution required. Varied people/scenes per card; avatars are portrait
crops. No identifiable brand logos, no competitor UI. 16 candidate photo IDs were batch-tested for
broken/removed images before use (0 fell back to placeholder grey).

## Regenerate

Source HTML lives in `_html/` (shared `_base.css`). To re-render any file (must be **online** so
Unsplash images load):

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cd docs/design/APP_STORE_SCREENSHOTS
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=645,1398 --default-background-color=000000ff --virtual-time-budget=15000 \
  --screenshot="$(pwd)/01_home.png" "file://$(pwd)/_html/01_home.html"
```

Contact sheet: open `index.html`.

## Verified dimensions

All ten confirmed `1290 × 2796` via `sips -g pixelWidth -g pixelHeight`. All ten confirmed
non-blank (real photo regions sampled, 500–12k distinct colors per region).
