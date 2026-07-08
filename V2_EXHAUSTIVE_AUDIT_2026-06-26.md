# V2 Exhaustive Audit — 2026-06-26 (branch nouss/ui3)

Founder-requested ultra-surgical audit: every screen, button, field, flow vs V2 maquette + functional completeness. READ-ONLY findings. 7 domain agents.

## STATUS
- ✅ Profile + Settings — done
- ✅ Creator-Pay / Channel — done
- ⏳ Auth+Onboarding · Feeds+Search+Xplorer · Messages+Notifs+Activities · Live+Sessions · Payments+Business+Mod — relaunched (first run killed by session limit)

---

## DOMAIN: Profile + Settings (28 files)
**Tally: Profile 8 FAITHFUL / 2 DIVERGENT · Settings 14 FAITHFUL / 4 DIVERGENT · 0 missing.**

### Real gaps (actionable)
- 🔴 EMOJI-as-icon (founder rule violation):
  - `ReportProblemScreen.tsx:58-63` — 6 problem tiles use 🐞🔥💳⚠️📊❓ instead of flat Ionicon tiles.
  - `NotificationSettingsScreen.tsx:281` — emoji 👊 on "smupsReceived" label suffix.
- 🟠 Visitor-path preview stubs (backend-blocked KAN-2400/2402):
  - `ProfileScreenV2.tsx:764` — 1:1 visitor subtitle hardcodes "4.9★ · 138 sessions" (fabricated).
  - `ProfileScreenV2.tsx:166-172` — hardcoded ONEONE_DURATIONS ($15/$28/$45/$69) + ONEONE_INCLUDED shown to visitors.
  - `ProfileScreenV2.tsx:146-213` — CHANNEL_HERO/CHANNEL_PERKS/CREATOR_PACKAGES consts (packs already render []; channel perks still preview).
- 🟠 `SecuritySettings:135` hardcoded "Google Authenticator" · `MyRatings:35-39` silent catch no retry · `PrescriptionPreferences:72` save local-only (backend gap).
### Confirmed GOOD
- Visitor channel price bug FIXED (server-sourced). @username compliant everywhere. All Settings rows wired to real routes. Settings icons = flat tinted Ionicons. 3 account types render correctly.

---

## DOMAIN: Creator-Pay / Channel (15 screens) — NOT done (founder was right)
**6 faithful · ~6 divergent · 3 orphan dead views · 2 maquette screens unimplemented.**

### 🔴 Dead code / orphan V2 views (built, tested, but NO screen mounts them)
1. `ChannelSubscriptionView` — orphan (real mounted one is `ChannelDetailView`). Latent @username render at :355-366 (not user-visible, orphan).
2. `PackagesOwnerView` — orphan. Packages-OWNER profile (creator_packages_owner_profile_v2: stats tiles + published-packs list + "Voir l'historique des ventes") NOT implemented — owner sees bare "Configurer vos packs" empty card. Blocked KAN-2400.
3. `PackageDetailView` — orphan dead component, no maquette, mounted by nothing.

### 🟠 Divergent layout vs maquette
4. Packages EDIT (`PackagesEditView`) — ships a reorder/delete list-manager; maquette `creator_packages_edit_v2` is a single-pack FORM (hero photo + Changer la photo + stat tiles + IDENTITÉ DU PACK + TARIF). Edit-form unimplemented; reorder dead-wired (KAN-2386).
5. Packages VISITOR list pane — faithful but fed `packages={[]}` → never renders (KAN-2400).
6. My Subscriptions — missing eyebrow + "N abonnements actifs" subtitle + bottom "Gérer" CTA; heavier card than compact maquette; stats summary card = dead code.
7. Fans List — V2 dropped the search bar (V1 had it), omits per-row verified marker + "Coach · 1.2K fans" role/fan-count subtitle.
8. ~~KYC Company — checklist vs 4-field form~~ → **NOT A GAP. CORRECT BY DESIGN (founder Jun 26): KYC/identity is DELEGATED TO STRIPE (Stripe Connect hosted onboarding). We have NO legal authority to collect KYC ourselves — building the maquette's 4-field form would be WRONG. The in-app screen is correctly a launcher/checklist → Stripe.**
9. ~~Payout — missing "En savoir plus"~~ → bank-detail onboarding is **Stripe Connect hosted (correct by design)**. Only the "En savoir plus" link is minor polish; the flow itself must stay a Stripe handoff.

### ⚠️ RULE (founder Jun 26): STRIPE-DELEGATED flows are NOT gaps
KYC, identity/document verification, bank/payout onboarding, and Verified-badge doc-capture go DIRECTLY through Stripe (Connect hosted). We don't have the authority/license to replicate them in-app. A maquette showing an in-app KYC/identity FORM is superseded by the Stripe handoff — do NOT "fix" these by building forms. In-app = a clean launcher + status only.
### Faithful
- Packages SETUP (add_service inline), Platform/Premium Plan, Manage Subscription (faithful superset), Packages purchase-detail (copy divergences only).
### Backend tickets referenced: KAN-2400/2386/2388/2389.

---
## DOMAIN: Auth + Onboarding (25 screens) — structurally complete BUT 7 P1 regressions
**9 FAITHFUL · 13 DIVERGENT · 3 PARTIAL · 0 missing.** All flag-gated (dark-shipped), no @username, account-gating correct.

### 🔴 P1 — functional regressions (V2 dropped a V1 input surface → user BLOCKED; MUST fix before flipping V2_UI on)
1. **CreatorOptional social links** — can't be entered in V2; `onEditSocial` (CreatorOptionalInfoScreen.tsx:184) is a no-op, no inline input/add/remove.
2. **BusinessInfo address autocomplete + geocoding LOST** (BusinessInfoScreen.tsx:271-306) — V1 Nominatim dropdown + locate + lat/long capture have no V2 slot; business coords silently dropped.
3. **BusinessCategory "Other"/custom unreachable in V2** (BusinessCategoryScreen.tsx:223-296) — custom TextInput never rendered; off-catalog businesses blocked.
4. **Profession "Other → custom text" dead-end** (ProfessionScreen.tsx:96-99) — selecting Other blocks Continue forever (no custom-input slot in V2 view).
5. **TellUs username + bio** = write-only dead state (v2Username/v2Bio never submitted, :175/:197) — also contradicts no-@username-in-onboarding. Remove or wire.
6. **FindFriends invite toggle = no-op** (FindFriendsScreen.tsx:37-41,80) — "✓ Invité" flips local state only, no SMS/server invite → misleads user. (Note: FindFriends now a Settings modal, not in onboarding flow.)
7. **EmailVerifPending X-close** dead (:182-206) + **Signup Content-Policy link** dead (:181, legal-sensitive → smuppy-legal).

### 🟠 P2 — emoji-as-icon, LIVE-rendered (founder-rule violations)
MFA 🛡⧉⚠↗ (MFAEnrollPrompt/QR/BackupCodes) · TellUs 📅⊕♂♀⚧ · Profession 8 emoji (:15-22) · CreatorInfo 📷✎ (:463/472) · text glyphs ✓ on BusinessCategory/Guidelines/Success/FindFriends.

### 🟠 P2 — copy/progress drift
ResetCode + VerifyCode step counters (2/4 vs 4/4) + dropped CooldownModal/setup-indicator · CreatorInfo/BusinessInfo titles · Profession hardcoded English (i18n gap) · missing field leading-icons (name-star/bio-doc/globe).

### P3 — confirm-intentional (founder yes/no): Welcome hero photo, Signup "Nom" field, Success/PasswordSuccess extra CTA.

## DOMAIN: Payments + Business + Moderation + Disputes + misc (28 screens)
**24/28 V2-wired faithful-or-intentional · 5 FLAG-OFF (M4 business) · 1 MISSING-V2 (WebView orphan).** 0 fabricated prices, 0 @username, directive #7 clean.

### 🔴 P1 — MONEY bug
- `DisputeDetailScreen.tsx:642,645,792,801` — amounts/refunds rendered WITHOUT `/100` (Center/Create divide by 100) → "2990.00" vs "29.90" on a refund surface. Pre-existing V1, replicated in V2. **FIX repo-wide (cents → /100).**

### 🔴 P1 — emoji-as-icon (live-rendered)
- `BusinessDashboardView.tsx:468` `settingsIcon ?? '⚙'` (prop typed string, screen passes none) · `SmuppyFormView.tsx:425` `icon="⚠"` hardcoded · `BlockedRegionView.tsx:267,294` 🌐/📍 fallback.

### 🟠 P1 — functional gaps / regressions when V2_UI=ON
- `ChannelMembersScreen:234-238` — V2 drops Banned tab + unban (creators can't unban fans).
- `SmupWalletScreen:310` "Envoyer" disabled (no wallet-send backend) + `:287` "Tous" misleading alias.
- `BusinessProfileScreen:226` owner "Modifier le profil" → opens website not edit route.
- `BusinessSubscriptionScreen:310,331-332,473,482,560` — hardcoded EN strings on V1 fallback path.

### 🟠 P1 — missing V2 wiring
- `WebViewScreen` — `WebViewView` built+faithful but ORPHANED (never imported). To ship: import + flag-gate + pass real WebView into webContentSlot + **re-apply isUrlAllowed/onShouldStartLoadWithRequest (security)** + Ionicon overrides.

### 🟠 i18n registration gap (verified)
3 namespaces have EN JSON but NOT imported in config.ts → FR-default fallback only: **v2CreatorWalletView, v2DisputeCenterView, v2BusinessSubscriptionView**.

### P2 — ticketed/deferred
SuggestSpot no-op onEditField · ActivePrescription no-op complete CTA during timer · AppealForm alreadyAppealed/summary stubs · BusinessBookingSuccess onAddToCalendar=Share (KAN-2398) · BookingHistory name join (KAN-2395) · Discovery text-search · BusinessProfile programme tab.

## DOMAIN: Live + Sessions (16) — all V2-gated, none missing
### 🔴 P0
- **WaitingRoom param mismatch** — callers pass flat `creatorId/Name/Avatar` (MySessions:122-127, SessionDetail:239-244) but WaitingRoom:52-54 reads nested `routeParams.creator` → host shows "Creator"/no avatar through join→PrivateCall(:298).
### 🔴 P1
- **Emoji-as-icon RENDERED in V2 LiveStreamingView** (🎙🔄📷🚫⏹👁✕, :398-562, screen passes no overrides). GoLive audience 🌐🔒💵 (:456/461/469).
- **ViewerLive paywall NOT wired** — view supports locked/onUnlock/lockPriceLabel (:211-227) but screen passes none → every viewer fully unlocked (maquette free-preview→subscribe absent).
- **ViewerLive V1 fabricated-price gift catalog** still in file ($2.99–$99.99, :1033-1039) — dead under V2 but delete (KAN-2409).
- **MySessions Book CTA** — bookSessionLabel without onBookSession (:280) = dead.
### 🟠 P2: LiveEnded missing star-rating + subscribe CTA · LiveEnded/SessionEnded Smups-send flag-gated (confirm vs KAN-2409) · GoLive missing magic-wand · glyphs lockIcon🔒/backIcon✕/🎉. i18n v2GoLiveIntroView/v2GoLiveView unregistered.
### ✅ CONFIRMED: GoLiveIntro Stripe-gate, GoLive PPV stepper, LiveStreaming camera-off+moderation, ViewerLive report/block, gift rail hidden, all session prices REAL.

## DOMAIN: Messages + Notifs + Activities
### 🔴 P0
- **ChatScreen V2 regression** (ChatScreen:861-892 + ChatView) — V2 drops: shared post/peak/profile bubbles (maquette shows a "Post de Sara" card that can't render), voice messages, long-press action menu (react/reply/delete/report/forward never opens), ChatInputArea (voice recorder UI + emoji picker + @mention + reply-preview + archived banner). Biggest single gap.
- **PersonalRunShare "Publier en Peak" gated OFF** (canPublishPeak=false, KAN-2405) — founder's #1 Run diff non-functional. (+V1 saveOnly mis-wired to publish :228-230.)
### 🔴 P1
- **@username LEAK in V2 MatchPageView** (:691/786/872/933; V1 uses displayName). ActivityGallery a11y "par @{{username}}".
- Emoji-as-icon: Run ■▶❚❚ (:238/247) · Records 🔥🏆 (:269/318) · CreateGroupChat 📷✓ (+dead photo picker) · ActivitySession 💬 · ActivityGallery 🗑 · FollowRequests ✓✕.
- PersonalRunTracking: NightRun/DayRun toggle not wired (OS-theme only); start/countdown dark-only (founder wants light obligatoire).
- Notifications: V2 drops post-thumbnail + follow-requests banner.
- i18n unregistered: v2MessagesView, v2ChatView, v2WeeklyStatsView.
### ✅ CreateActivity wizard = gold standard (event+group). SessionStats faithful. Directive #7 clean.

## DOMAIN: Feeds + Search + Xplorer
### 🔴 P1 — XPLORER (main gap): XplorerFeed is 100% V1; V2 XplorerSheetView (486L, built, i18n×4) ORPHANED. Missing the "Près de toi" nearby-results sheet entirely. Wiring needs: container V2 branch + MapMarker→XplorerResult adapter + **haversine distance calc (absent)** + nearby-sort + chip mapping + onSelectResult reuse + extend FeedHeaderV2 to Xplorer tab. **FOUNDER DIRECTIVE JUN 26: SIMPLIFY — remove create-activity FAB + create-spot FAB; keep ONLY run + search; make the search bar more useful+complete but simple.** (CreateActivity safe to remove — other entries exist. SuggestSpot has NO other entry → will be orphaned; founder to confirm drop-feature vs relocate.)
### 🔴 P1 — emoji/glyph icons render in prod (V2 defaults ON): FanFeed glyph fallbacks ♥♡➤★☆⋯▶✓ (FanFeed:824-866 omits icon-node props) · VideoRecorder 📷🎬 · Peaks 👁▶ (maquette-vs-rule, founder call).
### 🟠 Search divergences: Live-now rail never renders (v2Lives undefined, KAN-2410), suggested = rail vs 2-col grid, creator subtitle dropped, searchError not surfaced, ✕ glyph. FeedHeaderV2 icons swapped sides. CreateOptionsPopup 2 conflicting maquettes (pick canonical). SoundUsage "Utiliser ce son" CTA missing (ticket).
### ✅ Canonical PeakLiveCard112/CreatorCard144 shared feed/peaks/search. #7 clean. No @username (home/peaks/search). VibesFeed demoSofts + Peaks preview-on-empty = approved.

## ───────── MASTER FIX PLAN (prioritized) ─────────
**P0 (block V2 flip):** ChatScreen regression · WaitingRoom param · DisputeDetail /100 money · PersonalRunShare publish-Peak (KAN-2405 backend).
**P1-A EMOJI SWEEP (widest, mechanical, renders in prod):** Live/GoLive/FanFeed/VideoRecorder/Run/Records/CreateGroupChat/ActivitySession/ActivityGallery/FollowRequests/Peaks/ReportProblem/NotificationSettings/BusinessDashboard/SmuppyForm/BlockedRegion/MFA×3/TellUs/Profession/CreatorInfo → flat tinted Ionicon tiles.
**P1-B Xplorer wiring** (simplified per founder: map+run+search, no create FABs).
**P1-C Onboarding input-loss:** CreatorOptional social, BusinessInfo geocoding, BusinessCategory custom, Profession custom, TellUs fields, FindFriends invite.
**P1-D functional gaps:** ChannelMembers banned-tab, ViewerLive paywall, SmupWallet send, BusinessProfile edit→website, MySessions book CTA, @username V2 leaks (MatchPage), V1 fabricated-gift-catalog delete, WebView wire+security.
**P1-E i18n register 8 namespaces:** v2MessagesView/v2ChatView/v2WeeklyStatsView/v2GoLiveIntroView/v2GoLiveView/v2CreatorWalletView/v2DisputeCenterView/v2BusinessSubscriptionView.
**P1-F Creator-Pay:** mount/delete 3 orphan views, MySubs+FansList layout, PackagesOwner/Edit (backend KAN-2400/2386).
**Backend-blocked (tickets):** KAN-2400/2402/2404/2405/2386/2388/2389/2395/2398/2407/2409/2410.
**NOT gaps (Stripe-delegated):** KYC/Payout/Verified/Identity. Business booking flag-off = M4.

Auth/Onboarding · Feeds+Search+Xplorer (Xplorer KNOWN GAP: V1 flag=0, orphan XplorerSheetView) · Messages+Notifs+Activities · Live+Sessions · Payments+Business+Mod.

## EMERGING FIX BATCHES (once full audit in)
- A) Emoji→Ionicon sweep (ReportProblem, NotificationSettings + any others agents find).
- B) Mount orphan views / build missing Creator-Pay screens (PackagesOwner, PackagesEdit-form) where not backend-blocked.
- C) Wire Xplorer to XplorerSheetView.
- D) Divergent-layout fixes (MySubs, FansList) where not backend-blocked.
- E) Backend tickets for the rest (KAN-2400/2386/2388/2389 already exist).
