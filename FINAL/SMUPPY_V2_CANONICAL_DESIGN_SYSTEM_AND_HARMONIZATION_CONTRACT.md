# SMUPPY V2 — CANONICAL DESIGN SYSTEM & HARMONIZATION CONTRACT

**Purpose**  
This file is the canonical UI/UX contract Claude must read before harmonizing Smuppy screens.  
It is based on the existing Smuppy V2 maquettes, founder corrections, and the approved visual direction: **premium social fitness, mint signature, dark elegant, light clean, controlled glow**.

**Absolute rule**  
Do **not** recreate screens from scratch.  
Retouch existing screens/components so every screen follows the same visual logic, spacing, CTA behavior, tabs, cards, iconography, and navigation system.

---

## 0. NON-NEGOTIABLE FOUNDER RULES

These rules apply to **all screens**.

1. **Safe-area top**
   - No back arrow, close button, header, progress bar, or content may touch the top edge.
   - Every full-screen view must use the same safe-area/header inset contract.

2. **Logo by theme**
   - Light mode: Smuppy icon + wordmark = **dark navy / black**.
   - Dark mode: Smuppy icon + wordmark = **mint**.
   - On photo backgrounds, use overlay/contrast so the logo remains readable.

3. **Primary CTA**
   - All primary CTAs use the same mint→teal gradient **with glow**.
   - The reference is the strongest existing auth/post CTA style, especially Verify Code / Publish / Become a fan.
   - No flat primary CTA unless disabled.

4. **Header**
   - Main app header = Search left · Smuppy centered · Notification right.
   - Main tabs below = Fan / Vibes / Xplorer.
   - No emoji in header/tabs.

5. **Bottom navigation**
   - One canonical bottom nav everywhere on main app surfaces.
   - Items: Home · Peaks/Vibes · Central + · Messages · Profile avatar.
   - Central `+` has mint glow.
   - Active state is mint with clear icon activation.
   - No alternate bottom nav style.

6. **Chips / filters / sub-tabs**
   - No solid green full background.
   - Use mint text + mint outline.
   - Active state = subtle mint translucent fill + mint outline + optional light glow.

7. **Cards**
   - Friend suggestions, live cards, profile cards, settings rows, creator cards must use the same radius/spacing/shadow logic.
   - Same card family, not screen-specific random styles.

8. **CTA must never overlap**
   - CTA must not cover text, chips, fields, or scroll content.
   - If a screen is scrollable, CTA placement must be intentionally defined.

9. **Avoid unnecessary scroll**
   - Auth/Login/Signup are the zero-scroll reference.
   - Onboarding selection screens should avoid “1 mm scroll” layouts.

10. **No emoji as icons**
   - Replace emoji/icon-like text with flat SVG/icon atoms.
   - Emoji inside user-generated content can exist, but system UI must use real icons.

---

## 1. DESIGN PHILOSOPHY

Smuppy V2 must feel:

- **Premium**, not generic.
- **Social and energetic**, not corporate.
- **Fitness/community-oriented**, not finance/SaaS.
- **Mint as signature**, not random decoration.
- **Glow controlled**, not neon everywhere.

### Final recommendation

Use **Glow Premium controlled**, not pure flat design.

- 90% of the UI should remain clean/flat/readable.
- 10% of the UI gets glow: primary CTA, central plus, active navigation, premium/live/action states.
- Glow is a brand signature, not a decoration everywhere.

---

## 2. FOUNDATIONS

### 2.1 Color tokens

Use semantic tokens. Do not hardcode random hex values in screens.

#### Brand

| Token | Value | Usage |
|---|---:|---|
| `brand.mint` | `#2ED8C3` | Main mint accent |
| `brand.mintSoft` | `#A7F3E7` | Soft backgrounds, light mode active fills |
| `brand.teal` | `#16B8AA` | CTA gradient end |
| `brand.tealDeep` | `#0F8E82` | Pressed/darker CTA |
| `brand.glow` | `rgba(46,216,195,0.35)` | Glow shadow |
| `brand.glowStrong` | `rgba(46,216,195,0.50)` | Central plus / hero CTA only |

#### Dark theme

| Token | Value | Usage |
|---|---:|---|
| `dark.bg` | `#020403` | Full-screen background |
| `dark.bgAlt` | `#050807` | App shell background |
| `dark.surface` | `#10131C` | Cards/sheets |
| `dark.surfaceElevated` | `#171922` | Raised cards |
| `dark.surfaceSoft` | `#1F2330` | Inputs/secondary cards |
| `dark.border` | `rgba(255,255,255,0.10)` | Neutral border |
| `dark.borderStrong` | `rgba(255,255,255,0.16)` | Elevated border |
| `dark.text` | `#FFFFFF` | Primary text |
| `dark.textMuted` | `#A8B0C2` | Secondary text |
| `dark.textSubtle` | `#6F7788` | Tertiary text |

#### Light theme

| Token | Value | Usage |
|---|---:|---|
| `light.bg` | `#F7FAF9` | Full-screen background |
| `light.surface` | `#FFFFFF` | Cards/sheets |
| `light.surfaceSoft` | `#F1F6F5` | Active tab backgrounds, soft rows |
| `light.border` | `#E3E9EA` | Neutral border |
| `light.borderStrong` | `#D4DDDF` | Elevated border |
| `light.text` | `#071421` | Primary text |
| `light.textMuted` | `#64748B` | Secondary text |
| `light.textSubtle` | `#94A3B8` | Tertiary text |

#### Status

| Token | Value | Usage |
|---|---:|---|
| `status.live` | `#FF4B68` | Live border/pill |
| `status.success` | `#2ED8A3` | Success, check |
| `status.warning` | `#F6A623` | Warning |
| `status.danger` | `#EF4444` | Destructive actions |
| `status.info` | `#22C7FF` | Info / location |

---

## 3. SPACING

Use a strict spacing scale.

| Token | Value |
|---|---:|
| `space.2xs` | `4` |
| `space.xs` | `8` |
| `space.sm` | `12` |
| `space.md` | `16` |
| `space.lg` | `20` |
| `space.xl` | `24` |
| `space.2xl` | `32` |
| `space.3xl` | `40` |

### Screen padding

| Surface | Horizontal padding |
|---|---:|
| Auth centered screens | `24` |
| Onboarding forms | `24` |
| Dense chip screens | `20` |
| Main feed screens | `16` |
| Settings screens | `20` |
| Creator/dashboard screens | `20` |
| Bottom sheets | `24` |

---

## 4. RADIUS

| Token | Value | Usage |
|---|---:|---|
| `radius.xs` | `8` | Small badges |
| `radius.sm` | `12` | Chips |
| `radius.md` | `16` | Inputs / small cards |
| `radius.lg` | `20` | Standard cards |
| `radius.xl` | `24` | Large cards / media cards |
| `radius.2xl` | `30` | Bottom sheets |
| `radius.pill` | `999` | CTA / tabs / pills |

---

## 5. SHADOWS / GLOW

### Light mode

| Token | Shadow |
|---|---|
| `shadow.light.card` | `0 8 24 rgba(7,20,33,0.08)` |
| `shadow.light.cta` | `0 12 28 rgba(46,216,195,0.24)` |
| `shadow.light.glow` | `0 0 18 rgba(46,216,195,0.22)` |

### Dark mode

| Token | Shadow |
|---|---|
| `shadow.dark.card` | `0 12 34 rgba(0,0,0,0.38)` |
| `shadow.dark.cta` | `0 12 32 rgba(46,216,195,0.34)` |
| `shadow.dark.glow` | `0 0 24 rgba(46,216,195,0.35)` |
| `shadow.dark.glowStrong` | `0 0 34 rgba(46,216,195,0.48)` |

### Glow rules

Use glow on:
- Primary CTA
- Central plus button
- Active top tab if needed
- Active profile sub-tab
- Premium/live/creator action cards
- Focused input only if focus state matters visually

Do not use glow on:
- Every card
- Every text
- Every list row
- Static labels
- Disabled buttons

---

## 6. TYPOGRAPHY

Use one type scale.

| Token | Size | Weight | Usage |
|---|---:|---:|---|
| `text.display` | `32` | `800` | Welcome/logo hero only |
| `text.h1` | `28` | `800` | Main screen title |
| `text.h2` | `24` | `800` | Auth/onboarding titles |
| `text.h3` | `20` | `700` | Section title |
| `text.body` | `16` | `500` | Body text |
| `text.bodyBold` | `16` | `700` | Important body |
| `text.small` | `14` | `500` | Secondary copy |
| `text.caption` | `12` | `700` | Labels, meta, uppercase |
| `text.micro` | `10` | `700` | Small badges |

### Label casing

- Form labels: uppercase small caps, letter spacing `0.8`.
- Button text: sentence case or title case, weight `800`.
- Chips: medium/bold, no all caps unless status badge.

---

## 7. COMPONENT CONTRACTS

## 7.1 `SmButton`

### Primary

Use for all main actions.

| Property | Value |
|---|---:|
| Height | `56` |
| Border radius | `999` |
| Padding horizontal | `20` |
| Font | `16 / 800` |
| Text color | `#FFFFFF` |
| Gradient | `#2EE6C7 → #12B6C3` |
| Dark shadow | `shadow.dark.cta` |
| Light shadow | `shadow.light.cta` |

Usage:
- Se connecter
- Créer un compte
- Vérifier le code
- Continuer
- Publier
- Become a fan
- Rejoindre
- Enregistrer

### Primary small

Used for header actions like `Publier`.

| Property | Value |
|---|---:|
| Height | `40` |
| Radius | `999` |
| Padding horizontal | `18` |
| Font | `15 / 800` |
| Shadow | glow medium |

### Secondary outline

| Property | Value |
|---|---:|
| Height | `52` |
| Radius | `999` |
| Background | transparent |
| Border | `1.5` mint |
| Text | mint |
| Shadow | none or very subtle |

### Ghost / text

Use only for tertiary links:
- Renvoyer le code
- Passer cette étape
- Retour à la connexion

### Disabled

| Property | Value |
|---|---:|
| Opacity | `0.45` |
| Gradient | disabled neutral |
| Glow | none |
| Text | muted |

---

## 7.2 `SmTopHeader`

### Main app header

Default for Fan/Vibes/Xplorer/Search/Home surfaces.

| Element | Rule |
|---|---|
| Left | Search icon |
| Center | Smuppy wordmark |
| Right | Notification bell |
| Height | Safe-area + `56` |
| Light wordmark | dark navy |
| Dark wordmark | mint |
| Icons | Flat SVG, no emoji |

### Secondary screen header

Default for create/detail/settings screens.

| Element | Rule |
|---|---|
| Left | Back or close |
| Center | Title |
| Right | Optional small CTA |
| Height | Safe-area + `56` |
| Border bottom | subtle, only when content needs separation |

Examples:
- Nouveau post
- Réglages
- Sécurité
- Modifier le pack

---

## 7.3 `SmSegmentedTabs`

Used for:
- Fan / Vibes / Xplorer
- Peaks / Live
- Profile high-level tabs if needed

| Property | Value |
|---|---:|
| Height | `44` |
| Radius | `999` |
| Container background light | `rgba(241,246,245,0.85)` |
| Container background dark | `rgba(255,255,255,0.05)` |
| Active bg light | `#FFFFFF` |
| Active bg dark | `#161824` |
| Active text | mint |
| Active border | mint subtle |
| Active shadow | subtle mint glow |
| Inactive text | muted |

Important:
- No emoji.
- Do not make active tab solid green.
- Same dimensions across Home, Vibes, Xplorer, Peaks/Live.

---

## 7.4 `SmChip`

Used for filters, hashtags, categories, interests, profession, expertise.

### Default

| Property | Value |
|---|---:|
| Height | `32–36` |
| Radius | `999` |
| Padding H | `12–14` |
| Border | `1.2` neutral |
| Text | muted |

### Active

| Property | Value |
|---|---:|
| Border | mint |
| Text | mint |
| Background light | `rgba(46,216,195,0.08)` |
| Background dark | `rgba(46,216,195,0.10)` |
| Shadow | only when active/selected, subtle |

### “Voir plus” chip/button

| Property | Value |
|---|---:|
| Height | `40` |
| Radius | `14–16` |
| Border | dashed/outline mint |
| Text | mint |
| Icon | plus circle SVG |

---

## 7.5 `SmCard`

### Standard card

| Property | Value |
|---|---:|
| Radius | `20` |
| Padding | `16` |
| Background light | white |
| Background dark | `dark.surface` |
| Border | theme border |
| Shadow | card shadow |

Used for:
- Settings rows groups
- Form rows
- Profile sections
- Instruction cards

### Selection card

| Property | Value |
|---|---:|
| Height | `76–88` |
| Radius | `18` |
| Icon square | `44` |
| Active border | mint |
| Active bg | mint translucent |
| Chevron | right |

Used for:
- Account type
- Business establishment count
- Business cards
- Create menu rows

### Premium/action card

| Property | Value |
|---|---:|
| Radius | `20–24` |
| Border | mint/status subtle |
| Shadow | glow controlled |
| Background | elevated surface |

Used for:
- Creator channel
- 1:1
- Packs
- Live
- Paywall cards

---

## 7.6 `SmInput`

| Property | Value |
|---|---:|
| Height | `56` |
| Radius | `16` |
| Padding H | `16` |
| Label | caption uppercase |
| Icon | left flat SVG |
| Background light | white |
| Background dark | `dark.surface` |
| Border default | neutral |
| Border focus | mint |
| Focus glow | subtle mint |
| Error border | red |
| Error text | red |

Password field:
- Right action text = mint
- No random button styling.

---

## 7.7 `SmBottomNav`

Canonical bottom nav.

| Property | Value |
|---|---:|
| Height | `72–82` including safe bottom |
| Container radius | `28–32` top corners or floating pill depending screen |
| Background light | white |
| Background dark | `#12131A` |
| Shadow | elevated |
| Items | Home · Peaks/Vibes · Plus · Messages · Profile |
| Central plus size | `56` |
| Central plus glow | strong mint |
| Active indicator | mint line/dot/fill |
| Profile item | avatar with mint ring when active |

Rules:
- Main surfaces use bottom nav.
- Auth/onboarding do not.
- Modal/live full-screen can hide it intentionally.
- No business/premium route branching in the visual shell.

---

## 7.8 `SmBottomSheet`

Used for:
- Create menu
- Report
- Visibility
- Tag
- Location
- Confirmations

| Property | Value |
|---|---:|
| Radius top | `30` |
| Padding | `24` |
| Handle | centered, 44x5, muted |
| Background light | white |
| Background dark | `dark.surface` |
| Overlay | black 40–60% |
| Row height | `72–88` |
| Row radius | `18–20` |
| Row icon square | `52` |
| Row active glow | optional by feature/status |

Create menu row style:
- Use the **right-side maquette style** from the screenshot:
  - each row is a rounded card
  - icon has colored glow
  - title + subtitle
  - chevron right
- This is stronger than the flat left version and fits Smuppy better.

---

## 8. SCREEN FAMILY CONTRACTS

## 8.1 Auth / Access

Screens:
- Welcome
- Login
- Signup
- VerifyCode
- ResetCode
- CheckEmail
- ForgotPassword
- NewPassword
- PasswordSuccess
- EmailVerificationPending
- MFA screens

Rules:
- Centered content.
- No unnecessary scroll.
- Logo follows theme rule.
- CTA = `SmButton primary`.
- Inputs = `SmInput`.
- Code boxes use same height/radius/border.
- Success/interruption screens use same icon glow shell.
- MFA hidden if product flag off; still use same visual system if shown.

Specific corrections:
- `VerifyCode` CTA should be “Vérifier le code”, not “Saisis le code”, unless the field is incomplete.
- Signup checkbox: “J’accepte les Conditions générales et la Politique de confidentialité”.
- Welcome CTA: “Créer un compte”, no question mark.

---

## 8.2 Onboarding

Screens:
- AccountType
- TellUsAboutYou
- Interests
- Profession
- Expertise
- CreatorInfo
- CreatorOptional
- BusinessCategory
- BusinessInfo
- Guidelines
- Success
- FindFriends

Rules:
- Progress header uniform.
- Back button safe-area uniform.
- CTA bottom uses `SmButton primary`.
- Dense chip screens use `SmChip`.
- “Voir plus” uses `SmChip more`.
- No CTA overlay.
- If content cannot fit, use a clear scroll area with CTA outside scroll or CTA at end, not accidental overlap.

BusinessCategory:
- Use one final pattern only.
- Must include:
  - categories/cards/chips
  - “Voir plus”
  - custom text field for other activity
  - establishment count cards
- Do not keep two conflicting visual versions.

---

## 8.3 Home / Fan / Vibes / Xplorer

Rules:
- Header = `SmTopHeader main`.
- Tabs = `SmSegmentedTabs`.
- Bottom nav = `SmBottomNav`.
- Fan/Vibes/Xplorer must share one shell.
- Only content changes per tab.
- Vibes must not include fake creator/fan cards that are not real in code.
- Vibe mood card + filter chips can remain if real.
- Home/Fan keeps “LA TRIBU”.
- Save icon = star, not bookmark/ticket.

Live/Peaks rules:
- Live border = red, can blink/animate if existing.
- Peaks border = mint/green.
- Filters are outline, not solid green.

---

## 8.4 Profile

Screens:
- personal owner
- personal visitor
- creator owner
- creator visitor
- business owner
- fans list
- likers
- follow requests

Rules:
- Use the creator profile tab style as the reference.
- Cover image + avatar + badge remain.
- Stats use consistent stat block.
- Profile tabs use pill-card style with flat icon + text.
- Channel / 1:1 / Packages integrate under creator profile tabs.
- Personal owner: remove “Modifier” if it does not exist in real code.
- Add vibesmood counter where required.
- Apply variants by account type, but do not invent separate design systems.

Profile sub-tab component:
- Height `44–48`
- Radius `999`
- Active outline mint + subtle glow
- Icon left + label
- Inactive muted
- No solid green background.

---

## 8.5 Post / Peak creation

Screens:
- Post create menu
- Post gallery
- Post details
- Post success
- CreatePeak
- VideoRecorder

Rules:
- Post create menu = canonical `SmBottomSheet`.
- Use row-card glow style, not flat list.
- Post gallery:
  - remove unnecessary camera icon if photo/video already exists in bottom tabs.
- Post details:
  - keep existing maquette direction.
  - use header secondary + small primary publish button.
  - hashtags = `SmChip`.
  - action rows = `SmCard selection`.
- Post success:
  - auto-dismiss.
  - show post card/status if needed.
  - message only: “Post publié & en ligne avec succès.”
  - no CTA, per founder correction.
- Sound usage: deprecated / remove from active product docs.

---

## 8.6 Messaging / Notifications

Rules:
- Messages list should use user message cards, not a plain list.
- New message and group creation follow same card system.
- Chat is OK; only harmonize chrome/composer if needed.
- Notifications:
  - person photo as icon.
  - multiple users = stacked avatars + counter.
  - tabs use `SmChip` / `SmSegmentedTabs` style.
  - no emoji icons.

---

## 8.7 Settings / Account

Rules:
- `p1_settings_v2` is reference.
- Flat colored icons are OK.
- Rows grouped in cards.
- No duplicate old settings style.
- Privacy/Notification/Security/Report Problem are already strong; only tokenize and align CTA/glow.
- Terms/Policies: icons not emoji.
- Data Export / My Subscription / Blocked / Muted / Blocked Region use same list/card/CTA system.

---

## 8.8 Creator / Channel / 1:1 / Packages

Rules:
- Use creator profile/channel visual style as reference.
- Channel setup sub-screens must be fixed if off-screen/deformed.
- Channel owner profile gets “Configurer”, reusing channel setup content.
- 1:1 owner setup:
  - no visitor “subject” field.
  - each day has a sub-screen with active/closed times.
  - owner controls 15/30 min slots.
  - success screens must not deform.
- Package setup/edit:
  - one component with `mode=create|edit`.
  - CTA “Enregistrer le pack” at end of scroll, not fixed over content.
  - package edit visual bug must be removed.
- Package purchased: fix margins if text too close.

---

## 8.9 Premium / Payments / Business / Live

Rules:
- Payment/paywall screens use one plan purchase template.
- Pro creator and pro business have separate adapted content.
- Upgrade to pro does not include verified account.
- Verified badge purchase: one canonical flow, remove duplicate.
- Live ended/session ended: add Smups CTA where required.
- Go Live: remove preview card if founder requested.
- Business remains hidden unless product scope revives it.

---

## 9. IMPLEMENTATION STRATEGY FOR CLAUDE

Claude must work in lots.

### Lot 0 — Foundation only
Create/confirm:
- tokens
- button
- chip
- tab
- card
- input
- header
- bottom nav
- bottom sheet

No screen-level redesign yet.

### Lot 1 — Auth / Onboarding
Apply only:
- logo theme rule
- CTA rule
- safe-area
- chips outline
- voir plus
- no overlay
- no emoji icons

### Lot 2 — Main Shell
Apply:
- header
- Fan/Vibes/Xplorer tabs
- bottom nav
- Home/Fan/Vibes/Xplorer shared shell

### Lot 3 — Post/Create
Apply:
- create menu sheet
- post gallery camera icon removal
- post details chip/card style
- post success auto-dismiss/no CTA

### Lot 4 — Profile
Apply:
- profile tabs/pill-card system
- creator channel/1:1/packs integration
- owner/visitor variants
- vibesmood counter

### Lot 5 — Messaging/Notifications/Settings
Apply:
- message cards
- notification avatars
- settings card/list system

### Lot 6 — Creator/Payments/Live/Business hidden
Apply after founder validation.

---

## 10. VALIDATION RULES

Before any commit, Claude must show:

1. Files changed.
2. Screens affected.
3. Before/after screenshots or HTML preview.
4. Dark + light mode.
5. At least one device/simulator check if RN changed.
6. `npx tsc --noEmit` result.
7. No unrelated files changed.

No bulk app-wide refactor without:
- design preview
- founder validation
- narrow file list
- rollback plan

---

## 11. SCREEN STATUS CHECKLIST

Use this status model:

| Status | Meaning |
|---|---|
| `OK` | Keep, only tokenize if needed |
| `POLISH` | Minor spacing/CTA/logo/icon correction |
| `HARMONIZE` | Must adopt shared component |
| `FIX_FUNCTIONAL_FIRST` | Route/logic issue before design |
| `HIDDEN` | Behind flag, do not prioritize |
| `DEPRECATED` | Remove from active docs/flows |
| `REDESIGN_PREVIEW_REQUIRED` | Existing screen is too divergent; preview before implementation |

---

## 12. FIRST PRIORITY TARGETS

Based on current audit and maquettes:

### P0
- ActivitySessionDetail routing issue.
- BottomNav / V2BottomNav unification.
- CreateOptionsPopup canonical sheet.
- Fan/Vibes/Xplorer shared shell.
- ProfileScreen shell.
- Settings information architecture / duplicate removal.

### P1
- Auth/onboarding polish.
- Post flow polish.
- Peaks/live filters.
- Messaging cards.
- Notification avatars.
- Creator packages setup/edit consolidation.

### P2
- Business hidden flows.
- MFA hidden screens.
- Premium/payments hidden/late-scope flows.

---

## 13. FINAL CLAUDE COMMAND SUMMARY

Claude must read this file and apply the design system by retouching existing screens, not recreating them.

Core instruction:

> “Use existing screens as base. Replace inconsistent local styles with canonical Smuppy V2 components and tokens. Do not change product logic, navigation, or routes unless the task explicitly says so. Show before/after before applying broad changes.”

