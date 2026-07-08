# V2 Feed + sub-screen wiring plan (audit + waves) — Jun 13, 2026

> Founder directive: every button / card / flow / sub-screen / sub-sub-screen
> reachable from the home feeds must be wired to V2. Audit (3 parallel agents)
> found: Fan/Vibes feeds ~wired with gaps, Xplorer 0% V2, and **every tap from a
> feed lands on a V1 screen** (16 V2 views built but never mounted). V2_UI is now
> ON by default → this V1/V2 mix is visible NOW.

Rules for EVERY item below (non-negotiable, per founder): design-only behind
`FEATURES.V2_UI`; V1 path intact; render immediately (no blocking spinner);
keep V1 testIDs/analytics/handlers; map controller→view props; topInset added to
each view; gates per commit (tsc 0 · eslint 0 · jest green) ; review-loop to
0 P0/P1 ; never push main.

---
## WAVE 0 — close the gaps on the ALREADY-wired feeds (fast, high impact)
**0.1 Fan Feed P0 (HomeFeedView + FanFeed)**
- Avatar tap on post header → profile. Add `onPressAuthor?(authorId)` to
  HomeFeedView PostCell; wire FanFeed `goToUserProfile`. (HomeFeedView.tsx:662-673)
- Likes-count tappable → likers. Add `onPressLikeCount?(postId)`; wire FanFeed
  `handleLikersPress`. (HomeFeedView.tsx:874-885)
- Caption mentions tappable (hashtags already colored). Add mention/hashtag tap
  handlers (RichText-equivalent) → profile / hashtag feed. (HomeFeedView.tsx:726-748)
- P1: rename PostCell menu testID `*-more` → `*-menu` (V1 parity). offline state.
- P2: skeleton suggestions rail, peak viewsLabel, challenge progress ring.
**0.2 Vibes P1 (VibesFeed → VibesFeedView)**
- Wire `onPressSearch` / `onPressNotifications` / `brand` wordmark / `notifCount`
  (mirror FanFeed). Wire `onEmptyAction` (+label) → discovery.
**0.3 Xplorer V2 (P0 consistency)** — XplorerSheetView is built+tested but unmounted.
- New container `XplorerFeed` V2 branch: map (Mapbox) via `mapSlot`, transform
  useXplorerData → XplorerSheetView props, wire filters/results/FAB/search/location.
- FeedScreen: extend `v2OnFanOrVibes` → include Xplorer (activeTab===2) so
  FeedHeaderV2 renders consistently. (~300 LOC + review)

---
## WAVE 1 — P0 VIEWING flows (most-tapped from feed)
**1.1 Post detail** — `posts/PostDetailScreen.tsx` → `PostDetailView`. Pager mode
from feed; map post controller + like/share/save/menu + author tap + likers.
NO comments (directive #7).
**1.2 Peak viewer** — `peaks/PeakViewScreen.tsx` → `PeakViewerView`. modes
fullscreen + live-preview; map peak controller + reactions + creator + share.
**1.3 Post likers** — `profile/PostLikersScreen.tsx` → `PostLikersView`. list +
follow/become-fan per row + profile tap.

---
## WAVE 2 — P0 CREATION flows (founder: "publication en ligne")
**2.1 Create-post menu** — the "+" entry → `PostCreateMenuView` (built, unmounted):
post / peak / live options. Wire wherever the create button lives (tab/FAB).
**2.2 Add post details** — `home/AddPostDetailsScreen.tsx` → `PostComposeDetailsView`
(built): caption + mentions compose + location + tags + visibility + publish.
**2.3 Post success** — `home/PostSuccessScreen.tsx` → `PostSuccessView` (built):
published confirmation + stacked content cards (NOT onboarding).
**2.4 Create-post media picker** — `home/CreatePostScreen.tsx` has **NO V2 view**.
DECISION NEEDED: build `CreatePostView` (media grid/picker) or restyle V1 in place.
**2.5 Create peak** — `peaks/CreatePeakScreen.tsx` → `CreatePeakView` (built):
camera/editor minimal per PEAK contract.

---
## WAVE 3 — P1 secondary destinations
**3.1 Search** — `search/SearchScreen.tsx` → `SearchView` (TikTok search).
**3.2 Notifications** — `notifications/NotificationsScreen.tsx` → `NotificationsView`
(IG notifications; FollowRequests already wired this session).
**3.3 Foreign profile** — `profile/ProfileScreen.tsx` currently `FEATURES.V2_UI &&
isOwnProfile`. Extend `ProfileShellView` to visitor/fan/business role views (4-source
useProfileController = higher risk → behavior contract + careful review).

---
## WAVE 4 — P2 deeper destinations (as encountered, depth-first)
FansList (FansListView) · Prescriptions (PrescriptionsView) · CreateActivity ·
SuggestSpot (SuggestSpotView) · GoLiveIntro/GoLive (GoLive*View) · PersonalRunTracking
(RunTrackingView — Run V2 already built) · PlatformSubscription (PlatformSubscriptionView) ·
PeaksFeed (NO view — decision) · ViewerLiveStream.

---
## Build sequence (depth-first per founder)
Wave 0 (gaps on live feeds) → Wave 1 (viewing) → Wave 2 (creation) → Wave 3 →
Wave 4. Each screen: read V1+controller → read V2 view+fixtures → wire branch →
topInset → gates → +regression test → review-loop 0/0 → commit. Batch OTA per wave.
Two screens have NO V2 view (CreatePost media picker, PeaksFeed) → founder decision
to build the view vs restyle V1 in place.

## Founder decisions — RESOLVED (Jun 13)
1. **CreatePost media picker** → ✅ use the EXISTING `PostGalleryView` (media-picker
   grid with source tabs Galerie / Photo / Vidéo). No new view. (Wave 2.4 → wire
   `CreatePostScreen` to PostGalleryView.)
2. **PeaksFeed** → ✅ use the EXISTING `PeaksLiveView` (assembled Peaks/Live feed:
   header Peaks/Live segmented tabs + 2-col PeakLiveCard grid, views pill / red LIVE
   badge). The audit's "NO-VIEW" was WRONG — it's PeaksLiveView. (Wave 4 → wire
   `PeaksFeedScreen` to PeaksLiveView.) **+ add the V2 `BottomNav`** to this screen
   (it's a MAIN feed surface, not a sub-screen → canonical bottom nav, not just a back arrow).
3. Foreign-profile V2 (Wave 3.3) → ship a behavior contract first (directive #9). PENDING.
4. Start order → Wave 1.1 first (post-detail loupe, founder-locked), executed FRESH
   per founder; then 0.1 (Fan feed avatar/likes-count) → 0.3 (Xplorer) → 1.2 (PeakViewer) → …
