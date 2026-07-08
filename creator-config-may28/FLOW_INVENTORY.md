# Creator Monetization — 3-perspective Flow Inventory

> Generated 2026-05-28 14:20 after founder correction "you mixed visitor view and owner config view".
> Goal : explicitly separate the 3 viewpoints per service. Founder validates this doc BEFORE final commit.

---

## The 3 perspectives (canonical model)

For every monetization feature, the same data has THREE representations :

| # | Perspective | Reached from | Who sees it | Affordances |
|---|---|---|---|---|
| **A** | **Owner config** | Settings → CREATOR → `<service> setup` | Only the creator (gated `pro_creator`) | Editable inputs, toggles, save CTA |
| **B** | **Owner profile self-view** | Creator's own profile → `<service>` tab | Only the creator | Preview "as fans see it" + small **Gérer** chip top-right that links back to A |
| **C** | **Visitor view** | Other user's profile → `<service>` tab | Fans / visitors | Purchase / book CTA at bottom |

Plus 2 secondary states for completeness :
| # | Perspective | Difference |
|---|---|---|
| **C1** | **Subscribed visitor** (Channel) | CTA replaced by "Abonné · gérer" |
| **C2** | **Booked visitor** (1:1) | "Ma prochaine session le jeudi 5 juin · 14h" + "Annuler" |
| **C3** | **Purchased visitor** (Pack) | "Pack actif · 2 sessions restantes" + "Réserver une session" |

---

## Channel (subscription)

| # | Status | File | Notes |
|---|---|---|---|
| A | ✅ Built | `creator_channel_setup_v2_{light,dark}/code.html` | cover + prix + 3 perks + commission note |
| B | ⏳ **MISSING** | (to build) `creator_channel_owner_profile_v2_*` | Same as visitor view but with "Gérer" chip top-right + no "S'abonner" CTA (replaced by "X abonnés actifs" stat row) |
| C | ✅ Built | `creator_channel_view_v2_{light,dark}/code.html` | compressed hero + 4 colored perks + S'abonner CTA |
| C1 | ⏳ **MISSING** | (to build) `creator_channel_view_v2_subscribed_*` | Same as C with CTA changed to "Abonné · 12 jours" + "Gérer l'abonnement" link |

**Supporting popups (Channel)** :
- ✅ `success` (saved → "Chaîne publiée 🎉")
- ✅ `leave` (unsaved changes warn)
- ✅ `add-perk` (add a benefit)

---

## 1:1 Sessions (Agora video)

| # | Status | File | Notes |
|---|---|---|---|
| A | ✅ Built | `creator_1on1_setup_v2_{light,dark}/code.html` | 5 durées toggle+price + multi-slot days + dates fermées + sujet par défaut |
| B | ⏳ **MISSING** | (to build) `creator_1on1_owner_profile_v2_*` | Shows durées active + slots aggregated for current week + "Gérer la dispo" chip top-right. NO booking CTA (creator can't book themselves). |
| C | ✅ Built | `creator_1on1_view_v2_{light,dark}/code.html` | Avatar + duration grid + time slots + "Réserver" CTA |
| C2 | ⏳ **MISSING** | (to build) `creator_1on1_view_v2_booked_*` | "Ma prochaine session · jeudi 5 juin · 14h" big card + "Lien Agora à 13h55" + "Annuler la réservation" |

**Supporting popups (1:1)** :
- ✅ `success` (saved → "Sessions 1:1 activées")
- ✅ `leave` (unsaved warn)
- ✅ `slot-editor` (tap day → edit hours/close day)
- ✅ `add-date` (closed date picker)

---

## Package (follow-up coaching)

| # | Status | File | Notes |
|---|---|---|---|
| A | ✅ Built | `creator_packages_setup_v2_{light,dark}/code.html` | Existing packs list + nouveau pack editor (title/durée/services/prix/badge) |
| B | ⏳ **MISSING** | (to build) `creator_packages_owner_profile_v2_*` | List of my packs as cards (similar to visitor view) + "Nouveau pack" mint CTA + each pack tappable → opens A in edit mode |
| C | ✅ Built | `creator_packages_view_v2_{light,dark}/code.html` | Pack details + price block + 3 perks + "Acheter le pack" CTA |
| C3 | ⏳ **MISSING** | (to build) `creator_packages_view_v2_purchased_*` | "Pack actif · 11 sessions restantes" status card + "Réserver une session" + "Voir mes sessions" |

**Supporting popups (Package)** :
- ✅ `success` (saved → "Pack publié")
- ✅ `leave` (unsaved warn)
- ✅ `add-service` (add a service line to a pack)

---

## Profile entry-point (where all 3 services live)

> NEW INSIGHT : the 3 services are surfaced on the **creator's profile** under a tab/section system.
> Need a profile shell maquette that shows the entry points to A/B/C in context.

| State | What it shows |
|---|---|
| **Owner sees own profile** | Tabs : Posts · Peaks · **Channel** · **Sessions** · **Packs** — each → perspective B |
| **Visitor sees creator profile** | Same tabs — each → perspective C |

> The tabs are gated : `Channel`/`Sessions`/`Packs` tabs only appear if the creator is `pro_creator` AND the respective offer is published.

| Status | File | Notes |
|---|---|---|
| ⏳ **MISSING** | `creator_profile_owner_v2_*` | Profile header + tabs with mint underline · default tab Posts |
| ⏳ **MISSING** | `creator_profile_visitor_v2_*` | Same shell but with "Fan" / "Fanned" toggle CTA on header |

---

## Total inventory after this iteration

| Perspective | Built (✅) | Missing (⏳) | Total target |
|---|---|---|---|
| Owner config (A) | 3 services × 2 themes = 6 | 0 | 6 |
| Owner profile (B) | 0 | 3 services × 2 themes = 6 | 6 |
| Visitor (C) | 3 services × 2 themes = 6 | 0 | 6 |
| Visitor purchased (C1/C2/C3) | 0 | 3 × 2 = 6 | 6 |
| Profile shell | 0 | 2 × 2 = 4 | 4 |
| Popups | 6 | 0 | 6 |
| **TOTAL** | **18 (50%)** | **16 (50%)** | **34 maquettes** |

---

## Founder validation decisions (2026-05-28 14:25)

1. ✅ **3-perspective model OK** — build in order A → B → C → D
2. ✅ **State variants = SEPARATE files** (my reco) — easier to review screenshots, no JS state to maintain. Naming : `creator_<svc>_view_v2_{subscribed,booked,purchased}_{light,dark}`
3. ✅ **Profile shell = FULL** — avatar + cover + bio + stats + tab bar + active tab content
4. ✅ **Pack edit included in Sprint D**

## Additional founder request (2026-05-28 14:25) — FULL FLOW POPUPS

For each service, the complete booking/subscribe/purchase flow including IAP. Required popups:

### 1:1 booking flow (visitor)
1. Tap date in calendar → `popup_date_picker` (full calendar bottom-sheet)
2. Pick time slot (already shown in view) → button enables
3. Tap "Réserver" → `popup_book_objective` (bottom sheet : "Décris ton objectif / sujet" textarea, optional)
4. Confirm objective → `popup_iap_confirm_1on1` (mock Apple/Google StoreKit sheet : amount + Face ID prompt)
5. Native IAP processing → `popup_payment_loading` (spinner)
6. Server confirms → `popup_booking_success` (✓ "Session réservée · jeudi 5 juin 14h · Lien Agora à 13h55")
7. Redirect to C2 booked state

### Channel subscribe flow (visitor)
1. Tap "S'abonner" → `popup_iap_confirm_channel` (StoreKit mock : $9.99/mo subscription terms)
2. Native IAP processing → `popup_payment_loading`
3. Server confirms → `popup_subscribe_success` ("Bienvenue dans la chaîne 🎉")
4. Redirect to C1 subscribed state

### Package purchase flow (visitor)
1. Tap "Acheter le pack" → `popup_iap_confirm_pack` (StoreKit mock : $269 one-time)
2. Native IAP processing → `popup_payment_loading`
3. Server confirms → `popup_purchase_success` ("Pack actif · 11 sessions restantes")
4. Redirect to C3 purchased state

**New popups to build : 9 total** (date-picker + book-objective + 3 iap-confirm variants + payment-loading + 3 success-by-flow variants)

---

## Revised execution order (validated)

- [ ] **Sprint A** — 3 owner-profile views B (Channel/Sessions/Packs) light+dark = 6 files
- [ ] **Sprint B** — 3 visitor-state variants (C1/C2/C3) light+dark = 6 files + 9 flow popups = **15 files**
- [ ] **Sprint C** — Profile shell (owner + visitor) light+dark = 4 files
- [ ] **Sprint D** — Pack edit mode (light+dark) = 2 files + cleanup

**Updated total target : ~43 maquettes** (vs initial 34). Building order A→B→C→D, founder validates after each sprint before next.

---

## Status as of 2026-05-28 14:25

- ✅ Sprint pre-work : 18 maquettes shipped (6 config + 6 visitor + 6 popups)
- ⏳ Starting Sprint A now
