# Creator Config — Backend Migrations TODO

> Generated 2026-05-28 from maquette spec validation against prod code (PrivateSessionsManageScreen.tsx,
> ChannelSetupScreen.tsx, sessions/settings.ts, packs/manage.ts, profiles table).
> Branch: `design/creator-config-may28` · Maquettes: `docs/design/creator-config-may28/maquettes/`

## Channel setup — schema deltas

Current code state (`channel-subscription.ts:set-price`) :
- `profiles.channel_price_cents` ✅
- `profiles.channel_description` ✅

To support the new maquette :

| Migration | Column / Table | Type | Default | Notes |
|---|---|---|---|---|
| 194-A | `profiles.channel_cover_url` | `text NULL` | `NULL` | S3 key for cover photo (390×312 recommended). Empty = no cover (fallback to brand placeholder). |
| 194-B | `channel_perks` | new table | n/a | `(id uuid PK, profile_id uuid FK, position int, label text NOT NULL, created_at timestamptz)` — ordered list, soft-delete via `deleted_at`. |
| 194-C | (drop) `profiles.channel_description` | n/a | n/a | Founder may28 13:15: tagline & description redundant with perks. Mark `_deprecated_channel_description` (NEVER drop columns with user data per CLAUDE.md), stop writing. |

**Lambda changes** : extend `payments/channel-subscription.ts` with new `set-cover` (presigned PUT) + `set-perks` (replaceAll) actions. Or split into `channel/cover.ts` + `channel/perks.ts` for cleaner routing.

---

## 1:1 setup — biggest delta

Current code state (`sessions/settings.ts`) :
- `creator.session_duration` single int (mins) ✅
- `creator.session_price_cents` single int ✅
- `creator.session_availability` `Record<weekday, TimeSlot[]>` ✅ (multi-slot already supported in DB!)
- `creator.session_subject_default` text ✅
- `DURATIONS = [30, 45, 60, 90]` hardcoded in `PrivateSessionsManageScreen.tsx:100`

Founder may28 13:10 decisions :
- Add `15min` → set becomes `[15, 30, 45, 60, 90]`
- Multi-duration with independent prices
- Multi-slot per day exposed in UI
- New "Dates fermées" section

| Migration | Column / Table | Type | Default | Notes |
|---|---|---|---|---|
| 195-A | `creator_session_offerings` | new table | n/a | `(id uuid PK, creator_id uuid FK, duration_min int NOT NULL, price_cents int NOT NULL, is_active boolean DEFAULT true, created_at timestamptz)` — unique `(creator_id, duration_min)`. Replaces single-duration fields. |
| 195-B | (deprecate) `creator.session_duration` + `creator.session_price_cents` | n/a | n/a | Backfill data into `creator_session_offerings` (one row at the current duration). Then mark `_deprecated_*`. |
| 195-C | `creator_closed_dates` | new table | n/a | `(id uuid PK, creator_id uuid FK, date date NOT NULL, end_date date NULL, label text NULL, created_at timestamptz)` — supports single days OR ranges (vacances 20–28 août). Label optional ("Fête nationale", "Vacances"). |
| 195-D | `PrivateSessionsManageScreen.tsx:100` | n/a | n/a | Change `DURATIONS = [15, 30, 45, 60, 90]`. |
| 195-E | `sessions/availability.ts` | n/a | n/a | Skip slots intersecting any row in `creator_closed_dates` (date or date range overlap). |

**Lambda changes** :
- `sessions/settings.ts` — extend `body` to accept `offerings: [{duration_min, price_cents, is_active}]` (replace strategy) + `closed_dates: [{date, end_date, label}]`.
- `sessions/availability.ts` — read `creator_session_offerings` per requested duration, filter `creator_closed_dates`.
- `creator_session_offerings` exposure : new GET endpoint `/v1/creators/:id/offerings` for the booking flow.

---

## Package setup — small deltas

Current code state (`packs/manage.ts`) :
- `packs.name` ✅
- `packs.description` ✅
- `packs.sessions_included` int ✅
- `packs.session_duration` int (mins) ✅
- `packs.validity_days` int ✅
- `packs.price_cents` int ✅
- `packs.savings_percent` int ✅ → can be used to derive promo price
- Separate `pack_offerings` table for services ⚠️ (not embedded in pack)

Maquette assumes :
- Pack title ✅
- Duration (free text "3 mois") — currently stored as `validity_days` int → UI should convert or store as string
- Services list (the "Inclus dans ce pack") → `pack_offerings` is the right home, but the editor UI doesn't yet inline-edit it
- Promo price + final price → `savings_percent` covers it (final = price, promo = price / (1 - savings/100))
- Badge → MISSING

| Migration | Column / Table | Type | Default | Notes |
|---|---|---|---|---|
| 196-A | `packs.badge` | `text NULL` | `NULL` | Optional badge text ("Best seller", "Nouveau", etc.). 32 chars max enforced server-side. |
| 196-B | (UX-only, no schema) | n/a | n/a | Inline editor for `pack_offerings` in the Package setup screen — currently the table exists, just not surfaced in this UI. |
| 196-C | (UX-only, no schema) | n/a | n/a | `validity_days` field rendered as "Durée : 3 mois / 12 semaines / 60 jours" — pick a unit picker (month/week/day) and store as days. |

**Lambda changes** :
- `packs/manage.ts` POST/PUT body accepts `badge: string \| null`.
- POST/PUT also accepts `offerings: [{position, label}]` for inline service editing.

---

## Total scope estimate

| Area | Migration count | Lambda changes | Mobile changes | Days |
|---|---|---|---|---|
| Channel | 3 | 1 file (+2 actions) | 1 screen (`ChannelSetupScreen.tsx`) | 2 |
| 1:1 | 5 | 2 files | 1 screen (`PrivateSessionsManageScreen.tsx`) | 3–4 |
| Package | 1 | 1 file | 1 screen (`PackEditorScreen.tsx`) | 1 |
| Popups (success + leave + slot-editor) | 0 | 0 | 1 shared component (`creator/SaveSheets.tsx` reusing `V2BottomSheet`) | 0.5 |
| Total | **9** | **3 files extended, ~+200 LoC** | **3 screens + 1 shared** | **~7 dev-days** |

## Open follow-ups for founder

1. **Cover photo aspect ratio + max size** : maquette assumes 5:4 + S3 presigned PUT. Decision : 4:3? Square? Max 5MB?
2. **Pack `validity_days` UX** : current free-text in maquette = "3 mois". Should we offer a unit picker (mois/semaines/jours)?
3. **Promo price computation** : show explicit `savings_percent` field, or `prix barré + prix final` and compute saving server-side?
4. **Channel currency display** : maquette shows `9,99 €`. Confirm EUR-default OR multi-currency at v1?

---

## Cross-surface impact (CLAUDE.md directive #10)

Areas to re-test after migrations land :
- Channel subscription flow (fan side) : new cover photo + perks list rendering on `ChannelView.tsx`
- 1:1 booking flow (fan side) : new offerings + closed-dates aware availability rendering
- Profile owner empty-state CTAs that point to these config screens
- Stripe subscription mappings (verify `channel_price_cents` still source of truth for the IAP tier mapping)
