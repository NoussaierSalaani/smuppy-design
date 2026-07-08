# Session Handover — V2 RN Implementation + Payments + Run + Map (Jun 3-5)

> Read this FIRST to resume. Branch `design/creator-config-may28` (NOT pushed — founder owns `git push`). Companion: memory `project_v2_rn_coverage_roadmap_jun3.md` (the campaign tracker) + `project_v2_rn_foundation_jun3.md` + `project_payments_v2_maquettes_jun3.md`.

## Goal
Founder: **"tous les UI ont leur RN code"** — implement EVERY screen in React Native (V2 design). This is a MULTI-SESSION campaign (~90 screens remain). One session ≠ all of it.

## ✅ DONE this session (RN, committed, tsc 0 / lint 0 / ~530 V2 tests green)

### 17 component/screen commits on `design/creator-config-may28`
```
c5055d9fa ActivityRing + StatTile          a968a4494 BottomNav
812ae4294 CreatorCard + PeakLiveCard       949eed1c2 ProfileHeader
04b1d265e ListRow + Banner                 358122f02 PlanCard
666bb02d6 PayoutOnboardingView             e49903cb0 PremiumPlanView
0dde67d76 VerifiedBadgeView+PaymentGateSheet  5142dbcbf PremiumSuccessView+KycCompanyView
0ed40b9c7 map filter (NightRun/DayRun)      47b73379f NightRun pitch 55°
f59806c4e NeonRoads (teal road glow)        868c29bad RunStartView+RunCountdownView
e39d146ea run fast-flow wiring (Option A)   6b3b05f31 tracking StatTile
06a63c241 share StatTile
```
- **Atoms** `src/components/v2/`: ActivityRing, StatTile, BottomNav, CreatorCard, PeakLiveCard, ProfileHeader, ListRow, Banner, PlanCard (+ pre-existing Avatar/Button/Card/Input/TabBar/Toast/BottomSheet/EmptyState).
- **Payment composed screens** (presentational, need container+nav): PayoutOnboardingView, PremiumPlanView, VerifiedBadgeView, PaymentGateSheet, PremiumSuccessView, KycCompanyView.
- **Map**: `src/theme/v2/mapStyle.ts` (style URLs + route glow + pitch) + `src/components/v2/map/NeonRoads.tsx` (teal road glow via runtime LineLayer — only public `pk.` token available, no Studio upload). Wired into `PersonalRunTrackingScreen` + `XplorerMapView`.
- **Run feature V2 END-TO-END**: `RunStartView`+`RunCountdownView` + fast-flow wiring (controller `beginCountdown`/`cancelCountdown`, phase-driven `PersonalRunTrackingScreen`, FAB `reset()`→idle) + tracking/share StatsCard→StatTile. Flow: Xplorer FAB → DÉPART → 3·2·1 → tracking(NightRun map) → share.

## 🔲 REMAINING (~90 screens) — prioritized
1. **P0 payment nav wiring**: container (paymentsApi/useIAPCheckout) + MainNavigator + types (3-file rule) for the 6 payment views; replace V1 UpgradeToPro/PlatformSubscription/IdentityVerification (consolidate, don't parallel — directive #8).
2. **Feeds** (home/FanFeed/VibesFeed/Search/Xplorer/Peaks-Live), **Profiles** (ProfileHeader + sub-tabs, 8 variants), **Creator config** (channel/1:1/packages), **Onboarding**, **Settings** (25 items→ListRow), **Auth**, **Post/Peak creation**, **Run records/history/detail**.

## 🔑 KEY DECISIONS (locked this session)
- **Prices** (real, `src/config/iap-products.ts`): Pro Creator $99.99/mo, Pro Business $49/mo, Verified badge $14.99/mo add-on (INDEPENDENT of premium — `is_premium ⊥ is_verified`). Channel tiers $4.99–19.99.
- **1 plan per account type** (no side-by-side picker — mirrors `PlatformSubscriptionScreen.tsx:124`).
- **business_type = `company`** for pro_business KYC (individual for personal/pro_creator). Founder said backend already done.
- **Currency = USD `$` everywhere** (converted 83 € → $ in maquettes).
- **Payout banner = STATE of existing channel screen**, NOT a new screen (dedupّed `channel_payout_banner`).
- **Map**: NightRun(dark)/DayRun(light) "filter"; full neon-grid needs a custom Mapbox Studio style (needs an `sk.` styles:write token — only `pk.` available) → approximated via NeonRoads runtime layer.
- **HARD RULE**: never push to `main`/origin; founder owns push. Commit only on the feature branch.

## 🎨 Maquettes (design source) — survive /tmp loss
- **Builders** (Python → HTML, persisted in repo): `docs/design/master-audit-may30/scripts/builders/build_*.py` (synced Jun 5: payments_v2, run_v2, creator_config_v2, feeds_v5, profiles_v5, p1_v2, p2_v2). Working copies in `/tmp/smuppy-v2-recovery/maquettes/` (regenerable).
- **Galleries** (persisted): `docs/design/master-audit-may30/galleries/payments_gallery.html` + `run_gallery.html`.
- **Serve to visualize**: `cd /tmp/smuppy-v2-recovery && python3 -m http.server 8765 --bind 127.0.0.1` → `http://127.0.0.1:8765/maquettes/payments_v2/_png/` (payment PNGs) + `…/run_png/` (run iframes, live — they hang headless Chrome capture but render in a real browser).
- **Regen a builder**: `cd /tmp/smuppy-v2-recovery/maquettes && python3 build_<x>.py`.

## 🔒 LOCKED PATTERN for every new RN piece
1. `src/components/v2/<Name>/<Name>.tsx` + `index.ts`; `useV2Theme()`; `memo`+`displayName='V2X'`; required `accessibilityLabel`; icons as nodes (lib-agnostic).
2. Colocated test `src/__tests__/components/v2/<Name>.test.tsx`, `@jest-environment jsdom`, mock react-native + reanimated + expo-haptics + expo-linear-gradient as passthrough.
3. Screen restyle: V1 component → V2 atom, KEEP existing testIDs (E2E), don't recreate existing screens.
4. Gate per commit: `npm run typecheck` 0 + `npx eslint <files>` 0 + jest green + gitleaks.
5. `V2ThemeProvider` is at `App.js:425` (root) + V2_FONTS loaded → V2 atoms work live. Can't Chrome-screenshot RN → maquette PNGs/iframes are the visual; real RN preview = `expo start`.

## ▶️ Resume
Open the roadmap memory, pick the next P0/feature, build/restyle per the locked pattern, commit each piece. Founder wants continuous progress — cover a chunk per session toward 100%.
