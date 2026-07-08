# V2 UI Library — Handover to Hamza (wiring guide)

> Companion to `TRACKER.md` (status) + `docs/prompts/V2_UI_CREATION_MASTER_PROMPT.md` (contract).
> **What you get:** ~108 presentational-pure V2 components (views + atoms + panes + sheets), each
> hardened to a ready-to-implement standard — i18n strings-via-props (×4 locales), fixtures per state,
> WCAG AA both themes, a11y role+label+state, 100% func/branch-reachable coverage, review-loop 0/0.
> **Phase-2 BUILD is COMPLETE** (69 views over 14 waves + keystone ProfileShellView, all on PR #367).
> Browse them all in the dev gallery: `src/components/v2/__gallery__/` (`V2Gallery`, dev-flag, 111 entries).
> **Your job:** wire each into its screen (data hooks, navigation, API, i18n `t()`) WITHOUT
> touching the presentation. The components never import nav/api/store/`useTranslation` — you bring
> those at the edge. Branch: `design/creator-config-may28`.

---

## 0. The universal wiring pattern (every component)

A V2 component is `props in → JSX out`. To wire one:

1. **Read its fixtures** — `src/components/v2/<Name>/__fixtures__/<Name>.fixtures.ts` is the exact
   prop shape per state (happy / loading / empty / error / role-variants). Your container builds the
   same object from real data.
2. **Bring the data** — call the existing V1 controller/hook/API for that screen (listed per-group
   below) and map its result onto the fixture shape.
3. **Bring i18n** — every user-facing string is a REQUIRED (or optional-defaulted) string prop.
   - Register the component's namespace once: in `src/i18n/config.ts`, import the 4 locale JSONs
     (`src/i18n/locales/{fr,en,es,pt-BR}/v2<Name>.json`) and add to each `resources.<lng>` block +
     the `ns: [...]` array. (Most namespaces are NOT yet registered — registration is deliberately
     deferred to you, the wiring step.) The atoms/views document the exact keys.
   - Then pass `t('v2<Name>:<key>')` for each string prop. For templates with `{{token}}` use
     `t('v2<Name>:<key>', { token: value })`.
   - **i18n brace rule (L-2026-06-05):** a namespace's placeholder brace style MUST match its
     component's substitution mechanism. Components that self-substitute use `.replace('{{x}}')`
     (double-brace) — the run-flow, profile-panes & PeaksLive use SINGLE-brace `.replace('{x}')`;
     match the locale to the component. Most are double-brace/i18next.
4. **Bring nav + analytics** — each component exposes one callback prop per user action
   (`onSubmit`, `onSelectX`, `onBack`, …). Wire navigation + analytics (PostHog/Branch) there.
5. **Preserve testIDs** — pass the same `testID` prefix the V1 screen used (the components derive
   `${testID}-child` ids that match V1, so Maestro E2E keeps working). Per-component notes call out
   the exact V1 ids.
6. **Replace, don't parallel (directive #8/#22):** when a V2 view supersedes a V1 screen, delete the
   old screen body in the SAME commit (CREATE + nav-rewire + DELETE old + grep-zero + tsc-0).

**Do NOT** add a parallel implementation, re-style inside the component, or hardcode a string —
that breaks the single-source contract.

> **Complete component lookup:** `WIRING_INDEX.md` lists ALL 167 wireable components with their
> i18n namespace + fixture path — your one-stop table for "which view, which namespace, which prop shape".

### Worked example — wiring `EditInterestsScreen` end-to-end (copy this shape for every screen)

**Step 1 — register the namespace** (once, `src/i18n/config.ts`):
```ts
import v2EditInterestsViewFr from './locales/fr/v2EditInterestsView.json';
// …en/es/pt-BR…
resources.fr.v2EditInterestsView = v2EditInterestsViewFr;   // + en/es/pt-BR
// add 'v2EditInterestsView' to the ns array
```

**Step 2 — the screen file** (`src/screens/settings/EditInterestsScreen.tsx`) becomes a thin wiring shell:
```tsx
import { useTranslation } from 'react-i18next';
import { useNavigation } from '@react-navigation/native';
import { EditInterestsView } from '../../components/v2/EditInterestsView';
import { useSelectionList } from '../../hooks/useSelectionList'; // the EXISTING V1 controller
import { ALL_INTERESTS } from '../../config/interests';

export default function EditInterestsScreen() {
  const { t } = useTranslation('v2EditInterestsView');
  const nav = useNavigation();
  // 1) DATA — reuse the V1 controller untouched
  const { selected, hasChanges, isSaving, toggle, handleSave } = useSelectionList({ profileKey: 'interests', userKey: 'interests' });
  // 2) map config → the fixture shape (field names already match → no remap)
  const categories = ALL_INTERESTS.map((c) => ({ id: c.category, label: t(`cat_${c.category}`), hue: c.color, interests: c.items }));
  return (
    <EditInterestsView
      title={t('title')}
      categories={categories}
      selectedNames={selected}
      hasChanges={hasChanges}
      isSaving={isSaving}
      onToggle={toggle}                                   // 3) callbacks
      onSave={async () => { await handleSave(); nav.goBack(); }}
      onBack={() => nav.goBack()}
      saveLabel={t('save')}
      backTestID="interests-back-button"                  // 4) preserve V1 testIDs (Maestro)
      saveTestID="interests-save-button"
    />
  );
}
```
**Step 3 — delete the old V1 render body in the SAME commit** (the controller `useSelectionList` stays;
only the old JSX/styles go). `npx tsc --noEmit` 0 + `grep -rn "old-testid" src/` zero. Done.

That's the entire loop. Every screen is this shape — open its fixture for the exact props, the
per-group notes (§1-1d) for the V1 source + traps, `WIRING_INDEX.md` for the namespace.

---

## 1. Per-group wiring

### Payments (7) — `PayoutOnboardingView, PremiumPlanView, VerifiedBadgeView, PaymentGateSheet, PremiumSuccessView, KycCompanyView` (+ `PlanCard` atom)
- Reference container to imitate: `src/screens/payments/PlatformSubscriptionScreen.tsx`,
  `IdentityVerificationScreen.tsx`, `CreatorWalletScreen.tsx`.
- Data hooks: `paymentsApi`, `useIAPCheckout`, Stripe Connect status, `iap-products.ts` (real prices
  $99.99 pro_creator / $49 pro_business / $14.99 verified add-on). **`is_premium ⊥ is_verified`** — two
  independent flags; one plan per account type (NOT a side-by-side picker).
- Loading props (`subscribeLoading`/`verifyLoading`/`start/refresh/withdrawLoading`) are the
  presentational half of the double-submit guard (directive #18) — drive them from the in-flight
  mutation; the server idempotency key is still required.
- **pro_business → company KYC** (`KycCompanyView`): `connect.ts:190` needs a backend branch for the
  company entity (NOT done — see memory `project_payments_v2_maquettes_jun3`).
- V1 parity: PlatformSubscription/IdentityVerification ship **0 testIDs + 0 analytics** — add the
  analytics call-sites yourself on the callback props.

### Run / Activities (5) — `RunStartView, RunCountdownView, RunDetailView, RunHistoryView, RunRecordsView`
- **Already wired** into `src/screens/activities/PersonalRunTrackingScreen.tsx` (idle→RunStartView,
  countdown→RunCountdownView) + `src/i18n/config.ts` registers `v2RunStartView`/`v2RunCountdownView`.
  The run flow is i18n-complete ×4. Detail/History/Records still need container wiring (SessionStats /
  WeeklyStats / PersonalRecords hooks + ActivityRing).
- Run overlays use constant `#fff/#000` inks ON PURPOSE (full-screen over a dark map, theme-independent).

### Settings (5) — `SettingsListView, EditProfileView, NotificationSettingsView, PrivacySettingsView, SecuritySettingsView` (+ `ListRow`, `StatTile`, `Banner` atoms)
- Reference: `src/screens/settings/{Settings,EditProfile,NotificationSettings,PrivacySettings,SecuritySettings}Screen.tsx`.
- Toggle rows: the View renders the switch; you wire `onToggle(next)` to the prefs mutation. The
  OFF-knob is state-dependent for WCAG — don't override the knob color.
- `SettingsListView` composes `ListRow`; pass `item.testID` to reproduce V1 row ids
  (`menu-item-profile`, `logout-button`, `delete-account-button`, …).

### Profile (6) — `ProfileHeader, ProfileChannelPane, ProfileOneOnOnePane, ProfilePackagesPane, ProfileProgrammePane, ProfileActivitiesPane`
- Reference: `src/screens/profile/ProfileScreen.tsx` + the channel/1:1/packages/programme/activities tabs.
- `useProfileController` is the data source (note: it had a 4-source consistency issue per the May-25
  audit — wire ONE controller per directive #8). 5 role views: owner/visitor/fan/private/business.
- ProfileHeader stat row callbacks open fans/posts/peaks lists.

### Feeds (5) — `VibesFeedView, SearchView, XplorerSheetView, PeaksLiveView, LivePreviewView` (+ `CreatorCard`, `PeakLiveCard` atoms)
- Reference: `src/screens/home/VibesFeed.tsx`, `search/SearchScreen.tsx`, `home/XplorerFeed*`,
  `peaks/PeaksFeedScreen.tsx`.
- **PERF — these are virtualized.** VibesFeedView + PeaksLiveView use `FlatList numColumns=2`,
  XplorerSheetView uses `FlatList`, all with a named memoized renderItem + `onEndReached`. Wire your
  pagination to `onEndReached` + `onRefresh`. SearchView's 4 discovery rails are bounded `.map` (the
  unbounded typed-query RESULTS list from V1 is a SEPARATE surface, not in this restyle).
- **⚠️ Crash-class guard (L-2026-06-05):** renderItem context flows through a closure, NOT FlatList
  `extraData` (reading `info.extraData` is `undefined` in real RN → crash). Keep it that way if you
  extend a list.
- CreatorCard requires `ctaA11yLabel` + `isFan` — already wired in VibesFeed/Search.

### Onboarding (7) — `OnboardingAccountTypeView, …Interests, …Expertise, …Profession, …FindFriends, …Guidelines, …BusinessCategory`
- Reference: `src/screens/onboarding/*Screen.tsx`. Selectable chips/cards expose
  `accessibilityState={{selected/checked}}` — drive selection from your wizard state.
- `OnboardingFindFriendsView` contacts list is virtualized (FlatList). Account types: 3 real
  (personal / pro_creator / pro_business).

### Auth (6) — `AuthWelcomeView, AuthLoginView, AuthSignupView, AuthForgotPasswordView, AuthVerifyCodeView, AuthNewPasswordView`
- Reference: `src/screens/auth/*Screen.tsx` (Cognito: email + Apple + Google).
- **Security baked in:** password fields default `secureTextEntry`; the visibility toggle flips it +
  reflects `accessibilityState.checked`; no password value is ever rendered as plain text. Wire the
  toggle to a local `secure` state. Async submit CTAs take a `loading` prop (double-submit guard).
- VerifyCode is OTP (number-pad). Error props are caller-provided strings — never pass a raw
  exception (no internal leak). The shared `Input` atom now announces field errors to screen readers
  (role=alert + live region) — every Input consumer inherits this.

### Atoms (5 this batch + the pre-existing Button/Card/Input/Avatar/TabBar/Toast/BottomSheet/EmptyState)
- `ActivityRing` (progressbar+value, clamp/NaN-safe), `StatTile` (metric tile, accent value=primary
  AA, single-read a11y), `BottomNav` (tabs role=tab+state), `ListRow` (cell, 56pt, destructive AA),
  `PlanCard` (subscription card, tag AA). All data-driven; pass labels/values as already-translated data.

---

## 1b. NEW views built 2026-06-06 (autonomous night) — +32 components → 77 V2 namespaces

Same universal wiring pattern (§0). Each is presentational-pure (props in / JSX out, strings-via-props,
`memo`, `useV2Theme`), has a per-view i18n namespace `v2<Name>.json` ×4 locales (register in `config.ts`
at wire-time), `__fixtures__/<Name>.fixtures.ts` (a mock per state — use them as your prop shape), and a
test suite proving WCAG AA both themes + a11y + ≥44pt tap targets. **5 atom-level conventions are now
enforced across ALL V2 (verified by the review-loop — keep them when you wire):** (a) a glyph `*Icon`
prop rendered in a `<Text>` is typed `string`, a real icon node goes in a `<View>` slot; (b) every tap
target is a `Pressable`/`onPress` (never `onTouchEnd`), ≥44pt via native `minWidth/minHeight`; (c) i18n
`{{x}}` placeholders are substituted in-component (pass the template, not a pre-resolved string); (d) any
danger/destructive ink is a `getContrastRatio` direct pick (never a luminance threshold); (e) money CTAs
take a `*Loading` prop (double-submit guard) and flip to a non-money action once subscribed/purchased
(no double-charge). The `BottomSheet` atom gained `dismissible?: boolean` (default true) — pass `false`
for non-cancellable surfaces (payment-in-progress). `Banner.icon` is now string-or-node safe.

- **Auth-rest (6)** — `AuthCheckEmailView, AuthEmailVerificationPendingView, AuthPasswordSuccessView, AuthMfaEnrollPromptView, AuthMfaEnrollQrView, AuthMfaEnrollBackupCodesView`. Ref `src/screens/auth/*`. MFA: the TOTP secret + backup codes are caller-supplied props (never hardcoded); QR is a caller node slot; no real codes in fixtures. Success screens: hero check is a node slot, title `role=header`.
- **Onboarding-rest (5)** — `OnboardingTellUsView` (name/username-availability/dob/bio), `OnboardingBusinessInfoView`, `OnboardingCreatorInfoView`, `OnboardingCreatorOptionalView` (skippable), `OnboardingSuccessView`. Ref `src/screens/onboarding/*`. Username-availability is a prop-driven state machine (idle/checking/available/taken/invalid) — wire your debounce + API to drive `usernameStatus`.
- **Home (1)** — `HomeFeedView` (TikTok-For-You canonical). Vertical posts = `FlatList` with a named memoized renderItem closing over context (NEVER `info.extraData`); peaks/creator rails = horizontal `FlatList`. Wire your feed controller to the canonical single-cache (directive #8); pass `posts/peaks/suggestions` arrays + `onRefresh/loading/error`.
- **Post/Peak create (5)** — `PostCreateMenuView` (BottomSheet chooser), `PostGalleryView` (media-pick grid `FlatList numColumns`, selection-order badges), `PostComposeDetailsView` (caption/audience/location/tags — **NO comments**, directive #7), `PostSuccessView`, `PeakCameraView` (full-bleed chrome; `cameraSlot` = your camera node; all controls native ≥44pt Pressables, no Button atom). Caption counter uses `{{count}}`/`{{max}}` substitution.
- **Popups (10)** — compose `BottomSheet`: `LeaveSheet` (discard, danger CTA), `AddTextSheet` (overlay caption), `ChannelPricePickerSheet`, `IapConfirmSheet` (purchase, double-submit), `PaymentLoadingSheet` (`dismissible={false}` — only `visible=false` on payment-resolve closes it), `FlowSuccessSheet`, `DatePickerSheet` (7-col day grid, caller computes the month → pass `days[{id,label,available,selected}]` + `confirmDisabled`), `AddDateSheet` (delegates calendar via `onPickDate`; `addDisabled ?? !hasDate`), `SlotEditorSheet` (2-step destructive delete), `BookObjectiveSheet`. (`popup_success` = use `FlowSuccessSheet`.)
- **Creator-config views (5)** — `ChannelDetailView` (fan; `subscribed` prop flips Subscribe→Manage, no re-charge), `PackageDetailView` (fan; `purchased` prop; `{{price}}` substitution), `ChannelOwnerView` (owner stats; empty/draft states), `PackagesOwnerView` (owner list + `onEditPackage(id)`), `PackagesEditView` (editable packs; per-row delete = 2-step confirm sheet, `onDeletePack(id)` by id not index). Money CTAs use the gradient Button (see §4 gradient note).

---

## 1c. NEW views built 2026-06-06/07 (autonomous campaign waves 7–14) — +31 components → 108 V2 namespaces

Same universal wiring pattern (§0) + the 5 enforced conventions in §1b, plus a **6th now enforced
repo-wide: dark-mode detection uses the canonical `t.mode`/`t.isDark` from `useV2Theme()` — NEVER a
surface-string heuristic** (`t.colors.surface !== '#FFFFFF'` is fragile and was eliminated everywhere).
Each view is presentational-pure, has its `v2<Name>.json` ×4 (register in `config.ts` at wire-time),
`__fixtures__` per state, and a review-loop-0/0 test suite (WCAG read-from-render both themes + a11y +
≥44pt). **DS-FILL views mirror the V1 screen's data field names 1:1** so you wire without remapping —
the per-view note names the V1 source.

- **Sessions (5, wave-7)** — `MySessionsView, BookSessionView, SessionPaymentView, PrivateCallView, SessionEndedView`. Ref `src/screens/**` session/booking + Agora call screens. Mindbody/Calendly booking grammar; PrivateCall over-video chrome uses constant inks on the dark call surface. Money: SessionPayment double-submit-guarded.
- **Live + Wallet (5, wave-8)** — `GoLiveView, LiveStreamingView, LiveEndedView` (Twitch/TikTok-Live arch; over-video scrim+textShadow; `connectionState` drives an `accessibilityLiveRegion` per directive #19 — wire the Agora connection state to it) + `CreatorWalletView, SmupWalletView` (Twitch-Bits/Meta-Pay; cash-out + IAP top-up both double-submit-guarded + money-never-by-color-alone; balance card white-on-`primaryDeep` 6.47:1).
- **Business / Identity / Subscription (4, wave-9)** — `BusinessDiscoveryView` (Mindbody discovery, virtualized `FlatList`), `BusinessBookingView` (4-step Calendly), `IdentityVerificationView` (personal Stripe Identity KYC — distinct from `KycCompanyView` company KYC; render-only, no real doc data), `PlatformSubscriptionView` (Settings→Premium **management** — distinct from `PremiumPlanView` upsell; `isSubscribed` flips Subscribe→Manage, no re-charge).
- **Profile SHELL (1, wave-10) — KEYSTONE** — `ProfileShellView`: ONE parametric view for all 10 maquette combos (composes `ProfileHeader` + the profile panes + `BottomNav`). Props = `viewerRole` (owner/visitor/fan/private) + `tabs` (you build the per-account translated set) + `activeTabId/onSelectTab` + `activePane` (you pass the matching pane node). **Privacy invariant enforced IN the shell**: `ownerOnlyTabIds` (default `['saved']`) is stripped for non-owners regardless of the `tabs` you pass — you can't accidentally leak Saved to a visitor. `private` role renders the locked gate. Canonical "Become a fan" (never "Follow").
- **Messaging (4, wave-11)** — `MessagesView` (inbox `FlatList`), `ChatView` (DM thread, **inverted** `FlatList`; sent/received/sending/failed/day-separator states), `NewMessageView` (recipient picker), `CreateGroupChatView` (group setup). WhatsApp-canonical. Data shapes mirror V1 `Conversation`/`Message`(`isMe=sender_id===currentUserId`)/`Profile`. **DM chat is NOT a post comment** — directive #7 does not apply here. Online dots are per-mode greens (≥3:1).
- **Settings DS-fill (5, wave-12)** — `DataExportView` (GDPR), `MutedUsersView`, `BlockedUsersView` (lists = `FlatList`; unmute/unblock are RESTORATIVE → adaptive-primary outline, NOT danger-styled), `PasswordManagerView` (**all 3 fields `secureTextEntry`**; the show/hide toggle + field label sit in a header row above the `Input`, label rendered once), `TermsPoliciesView`. Ref `src/screens/settings/*`.
- **Media / Peaks DS-fill (3, wave-13)** — `VideoRecorderView` (post capture chrome; `cameraSlot` = your Expo camera node; the recording timer/progress VALUE arrives as a prop — the **wiring layer owns the interval**, the view runs no effect), `CreatePeakView` (minimal Peak editor §8: trim/cover/sound/caption/challenge/audience/publish; `previewSlot` = your `<Video>`; caption `{{count}}/{{max}}`), `SoundUsageView` (sound attribution + peaks-using-it `FlatList`; the challenge state is folded INTO the card `accessibilityLabel`). Do NOT import expo-camera/av/media-library — they're caller slots.
- **Tail DS-fill (4, wave-14)** — `ChannelSubscriptionView` (fan subscribe; `isSubscribed` removes the charge CTA — no re-charge; restore-purchases + iOS manage-subscriptions links), `ChannelMembersView` (owner subscriber `FlatList`; per-row remove/ban danger-direct-pick, `acting` disables both controls), `PostDetailView` (**DISPLAY-ONLY, NO comments — directive #7**; media slot + author + caption + like/share/save + like count only; over-media constant inks), `WebViewView` (namespace `v2WebView`; `webContentSlot` = your `<WebView>` — do NOT import react-native-webview; nav chrome over constant-dark base; progressbar role+value).

## 1d. 100%-APP extension — waves 15-24 (autonomous campaign, 2026-06-06/07) → 164 V2 namespaces / 145 views

Same universal wiring pattern (§0) + all conventions, plus a **7th bug class now enforced repo-wide:
`label-on-non-accessible-View`** — a RN `<View>` carrying `accessibilityLabel` MUST also carry
`accessible` or VoiceOver/TalkBack DROP the label (`accessibilityRole` alone does NOT promote a View).
**Its INVERSE is equally enforced**: a View that CONTAINS a focusable child (Pressable/Button/Switch/
TextInput) must NOT be `accessible` — that collapses the child out of the AT tree. The rule is
conditional: *labeled leaf* → `accessible`; *container with a focusable child* → role-only, no
`accessible` (carry the label on an inner Text, or leave children natural). Every wave-15-24 view test
asserts this both ways.

- **Activities / Sessions (waves 15-19)** — `ActivityDetailView, ActivitySessionView, ActivityAttendeesView, ActivityLeaderboardView, ActivityRatingsView, CreateActivityV2View, ActivityGalleryView, MatchPageView, PeerRatingView, PlayerCareerCardView` (Strava arch); `SessionDetailView, SessionBookedView, WaitingRoomView, PrivateSessionsManageView, BookingHistoryView` (Calendly/Mindbody); `PackPurchaseView, PackPurchaseSuccessView, BusinessBookingSuccessView, CreatorOfferingsView` (Twitch/Meta-Pay). Social: `FansListView, FollowRequestsView, PostLikersView, NotificationsView, HashtagFeedView`. All money CTAs double-submit-guarded; lists virtualized.
- **Business-suite (5, wave-20)** — `BusinessDashboardView, BusinessProfileView, BusinessSubscriptionView, BusinessSubscriptionSuccessView, CreatorEarningsView`. Meta Business Suite + Twitch creator. **`StatTile` atom gained `valueColor`/`labelColor` overrides** — pass `#FFFFFF`/`rgba(255,255,255,0.85)` when a tile sits on the constant `primaryDeep` balance card (CreatorEarnings + CreatorWallet hero tiles); the default adaptive inks fail AA on a constant bg. Subscribe gated by `isSubscribed` (no re-charge); `PlanRow` list memoized.
- **Disputes / Moderation (7, wave-21)** — `CreateDisputeView, DisputeCenterView, DisputeDetailView, AppealFormView, AccountBannedView, AccountSuspendedView, BlockedRegionView`. Meta Transparency Center + Stripe dispute-center. Trust-&-safety tone: status conveyed by WORD + dot (never color-alone); **never surface internal moderation reasoning beyond the strings you pass**. `AppealFormView` has `statementMinLength` (default 10, V1 parity — wire your min). DisputeDetail timeline is a bounded `.map` (V1 parity), NOT a paginated list.
- **Health-pro (4, wave-22)** — `PrescriptionsView, ActivePrescriptionView, PrescriptionPreferencesView, CoachJournalView`. "Prescriptions" = wellness MISSIONS (movement/mindfulness/…), NOT medical. `PrescriptionPreferences` option groups are GENERIC over the id union (`OptionGroupSection<TId>`) — pass your narrow union, get type-safe `onSelect`. ActivePrescription progressbar ALWAYS announces a value (falls back to `{pct}%`).
- **Live-secondary + subs (5, wave-23)** — `ViewerLiveStreamView` (audience side — distinct from broadcaster `LiveStreamingView`; **live chat is ALLOWED**, it's Agora not a post comment; over-video scrim inks; LIVE badge per-mode red `#D81F32`), `GoLiveIntroView` (feature/trial gate — distinct from `GoLiveView` setup), `ManageSubscriptionView` (Apple 3.1.2 transparency — lists all active subs, **filters `canceled` out** to avoid a cancel-of-canceled mutation; cancel routes to StoreKit, never an in-app charge), `UpgradeToProView` (ONE-WAY Personal→Pro — irreversibility note + terminal no-recharge), `MySubscriptionsView` (business subs list; cancel/reactivate gated by server `canCancel`/`canReactivate`).
- **Settings-edit + misc (11, wave-24)** — `EditExpertiseView, EditInterestsView, EditBusinessCategoryView` (settings multi-select; Save gated by `hasChanges` — distinct from the `Onboarding*` step variants), `MyRatingsSettingsView`, `PlayerAbilitiesView` (ability rating rows; the editable visibility `Switch` is an independent AT sibling of the accessible summary block — do not wrap it), `ResetCodeView` (6-digit Cognito OTP; the grid is role-only so each cell stays focusable; no secret logging), `SpotDetailView` (map/route caller SLOTs + reviews `FlatList`), `SuggestSpotView` (5-step wizard; caller controls `step`), `SmuppyFormView` (configurable member-intake; photo + signature are caller SLOTs — keep them non-focusable so the `accessible` slot wrapper doesn't collapse them), `PeakViewerView` (immersive single-peak player; video SLOT + over-video action rail; **NO comments — directive #7**), `HelpView` (FAQ list + contact-support). **`PlatformSubscriptionSuccess` was NOT built — use the existing `PremiumSuccessView`.**

---

## 2. Known traps & device-bug mapping (KAN-2131→2143)

The V2 views are presentation only — the device bugs you filed live in the V1 CONTROLLERS you will
wire. Each affected screen carries a "fix controller required" note so nothing surprises you:

| Bug (Jira) | Surface | What to fix in the controller you wire |
|---|---|---|
| KAN-2131 (P0) | Live gate | "déjà abonné" but access blocked — fix the entitlement check before mounting LivePreviewView |
| KAN-2140 (P0) | Activities | `useProfileEventsGroups` hardcodes `my-activities` → activity visible in ALL profiles; fix before wiring ProfileActivitiesPane |
| KAN-2137 / 2128 | (related) | see ticket |
| KAN-2141 / 2142 | Peaks chip | chip state — fix before wiring PeaksLiveView chips |
| KAN-2143 | Messages nav | nav bug — relevant when you build the Messages DS-fill view (Phase 4) |
| like race / fan flicker | feeds | optimistic-UI controller; wire VibesFeed/Search to the canonical single-cache controller (directive #8) |

(Full ticket text + repro: memory `project_jira_device_bugs_jun03`.)

## 3. OTA-rollback plan for risky waves
Payments, live/sessions, and auth are the high-risk surfaces. When you ship them:
- Feature-flag the V2 screen (PostHog) so you can flip back to V1 instantly without a new build.
- The presentation is OTA-able; any NEW native permission must already be in `Info.plist`
  (cannot be added via OTA — see CLAUDE.md launch rules).

## 4. Open follow-ups (NOT blocking; founder/token-owner decisions)
- ✅ **RESOLVED — gradient primary-CTA WCAG AA** (`a0783eaa6`, founder-delegated). Deepened the mint
  gradient `#41AD96/#2C95A0 → #1A7D68/#157082` (same mint→teal hue, darker value → white 5.03:1/5.72:1
  AA) + the gradient Button now inks a CONSTANT white (`GRADIENT_INK`), not the theme-adaptive onPrimary.
  One `tokens.ts` change cleared every gradient CTA. Tests are now AA guards + revert-proofs. Nothing to
  wire — it's a token; your gradient CTAs are AA out of the box.
- i18n namespace auto-registration: 77 `v2*` namespaces have locale files; most aren't yet in
  `config.ts` resources/ns (register-on-wire). Consider a glob auto-loader.
- `BottomSheet.backdropA11yHint` atom default is an English literal with no i18n key (same
  untranslated-a11y-default class fixed in AddDateSheet) — make it a threaded prop in a separate atom pass.
- ✅ **Dev gallery BUILT + COMPLETE** — `src/components/v2/__gallery__/` (`V2Gallery` screen +
  `galleryRegistry`, **167 entries** × fixtures × theme — every fixture-bearing view from all waves,
  gated `if(!__DEV__) return null`). NOT wired into prod nav — mount it behind a dev menu to eyeball
  every component × state. Theme caveat: it follows the OS appearance; the in-screen toggle restyles the
  gallery frame.
- 🟡 **DEFERRED — shared-atom a11y (own dedicated PR, NOT in the view waves)**: two shared atoms carry the
  `label-on-non-accessible-View` class internally — `Banner` (root `<View>` has `accessibilityRole="alert"`
  + label but no `accessible`, and its inner Texts aren't AT-hidden → the composed `alert` is dropped, it
  reads as two plain texts) and `ListRow` (non-pressable branch, label on a non-accessible View). Lower
  severity (content still reads via the inner Texts; only the `alert`/composed-label is lost). The fix
  changes a shared-atom a11y contract that **16+ consumer test files assert against**, so it must land in
  its OWN PR (per "1 PR = 1 purpose") where every consumer test updates atomically — do NOT fold it into a
  view-wiring PR. Banner fix shape: move `accessible`+role+label onto the inner `texts` View (NOT the root,
  which holds the optional action Pressable) + hide the inner Texts; ListRow non-pressable branch: add
  `accessible` to the row View.

## 5. Build status & your remaining work
**🎉 100%-APP V2 COVERAGE COMPLETE** — **145 V2 view dirs / 164 `v2*` namespaces** across the whole app
(maquette scope 69 views over 14 waves + ProfileShellView keystone, + the 100%-app extension waves 15-24).
Every wave passed a 3-lens review-loop to 0 P0/P1 (min 2 rounds, no cap). On PR #367 (clean fast-forward,
zero conflict with your `main` work, `main` untouched). The dev gallery (167 entries) is built. **7 bug
classes are eliminated repo-wide and self-propagate**: icon-node-in-Text · placeholder-leak ·
onTouchEnd-tap-target · false-green-wcag-test · money-double-submit · surface-string-isDark ·
**label-on-non-accessible-View + its inverse** (see §1d).

**Your remaining work is WIRING, not building.** For each screen: register the `v2<Name>` namespace in
`config.ts`, map the V1 controller data onto the fixture shape (field names already mirror V1 1:1), wire
callbacks (nav + analytics), preserve testIDs, then DELETE the old V1 screen body in the same commit
(directive #8/#22). Start from the per-group notes in §1/§1b/§1c/§1d. The components never import
nav/api/store/`useTranslation` — you bring those at the edge.

**Before you wire, do the ONE deferred atom PR in §4** (Banner + ListRow a11y) so every screen inherits the
fix — it touches 16+ test files and must be atomic.

### Final gap report (2026-06-07)
- **Coverage**: 100% of app screens have a V2 view. The only deliberate SKIP is `PlatformSubscriptionSuccess`
  (use `PremiumSuccessView`). Niche edge surfaces (Channel "Banned" tab, group-chat edge screens) remain
  scoped out per directive #22 — add to the same standard if a real screen needs them.
- **P0/P1 open**: 0 (every wave closed at 0/0).
- **Deferred (tracked)**: (1) shared-atom a11y PR (Banner + ListRow, §4); (2) i18n namespace
  auto-registration glob (§4); (3) `BottomSheet.backdropA11yHint` untranslated default (§4). None block wiring.
- **Verification**: tsc 0 · eslint 0 · full V2 + i18n suite **188 suites / 10255 tests** green · 164-namespace
  4-locale byte-identical parity · 0 forbidden imports across the library.
