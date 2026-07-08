# SMUPPY V2 — COMPONENT LIBRARY, MOTION SYSTEM & PERFECT-POLISH CHECKLIST

**Role of this document**  
This is the implementation-level companion to:

`SMUPPY_V2_CANONICAL_DESIGN_SYSTEM_AND_HARMONIZATION_CONTRACT.md`

Claude must read **both files** before applying any UI harmonization.

This file exists to remove ambiguity around micro-components, dimensions, states, motion, safe-area, and visual polish.  
It is designed to prevent inconsistent screens, random sizes, broken top spacing, CTA overlap, and “each screen has its own design style”.

---

## 0. ABSOLUTE RULE

Do **not** redesign screens from scratch.

Use the existing Smuppy V2 screens and maquettes as the base.  
Retouch only what is necessary to make them follow the same component system.

Every screen must pass:

1. Safe-area check.
2. Header/back/close positioning check.
3. CTA position check.
4. Dark/light parity check.
5. Button style check.
6. Chip/tab style check.
7. Icon style check.
8. Card spacing/radius check.
9. Scroll/keyboard check.
10. No overlap / no clipped text / no off-screen controls.

---

## 1. PERFECT-POLISH PRIORITIES

### P0 — Must fix before founder validation

- Back arrows outside or too close to the top.
- Close buttons outside or too close to the top.
- CTA overlapping content, chips, cards, keyboard, or bottom nav.
- Multiple bottom nav styles.
- Multiple primary CTA styles.
- Light mode logo appearing mint when rule says dark.
- Dark mode logo not mint.
- Main app header different from canonical FanFeed header.
- Solid green filter/chip backgrounds where outline mint is required.
- Emojis used as system icons.
- Button/route that leads to a missing screen.
- Text clipped or hidden under fixed footer.
- Modal/sheet content off-screen or deformed.

### P1 — Must fix during harmonization lot

- Uneven spacing between similar cards.
- Different input heights across auth/onboarding/settings.
- Different tab heights/radius across Home/Profile/Peaks.
- Non-token colors in screen-local styles.
- Inconsistent shadow/glow intensity.
- Mismatched icon sizes.
- Too much glow on static content.
- Dense screens with unnecessary micro-scroll.
- Light/dark versions with different hierarchy.

### P2 — Polish

- Better copy consistency.
- Slightly softer shadows.
- Skeleton polish.
- Transition smoothness.
- Haptic alignment.
- Minor alignment of icon/text baselines.

---

## 2. SAFE AREA & SCREEN SHELLS

### 2.1 Universal safe-area contract

All full-screen pages must use a safe-area aware shell.

| Element | Minimum top distance from physical screen |
|---|---:|
| Back arrow / close icon | `safeAreaTop + 8` |
| Progress bar | `safeAreaTop + 14` if no title; `safeAreaTop + 54` if under header |
| Header title | `safeAreaTop + 18` |
| First content block | At least `16` below header/progress |
| Scroll content bottom padding | `bottomNavHeight + 24` or `CTAHeight + safeBottom + 24` |

### 2.2 Header heights

| Header type | Height excluding safe area |
|---|---:|
| Auth/onboarding minimal header | `44` |
| Secondary header with title | `56` |
| Main app header | `56` |
| Main app header + Fan/Vibes/Xplorer tabs | `112–124` total excluding safe area |
| Modal sheet handle zone | `28` |

### 2.3 Back/close button

| Property | Value |
|---|---:|
| Touch target | `44 x 44` minimum |
| Icon visual size | `22–24` |
| Circular bg when needed | `40 x 40` |
| Radius | `999` |
| Left inset | `16–20` |
| Top | `safeAreaTop + 8` |

Rules:
- Never position back arrow with absolute `top: 0`.
- Never rely on status bar height assumptions.
- If header has a title, back icon and title must align vertically.

---

## 3. AVATARS

### 3.1 Sizes

| Token | Size | Usage |
|---|---:|---|
| `avatar.xs` | `24` | stacked avatars, tiny notification meta |
| `avatar.sm` | `32` | compact list rows |
| `avatar.md` | `40` | message rows, notification rows |
| `avatar.lg` | `56` | feed cards, invite cards |
| `avatar.xl` | `80` | profile header compact |
| `avatar.hero` | `96–108` | profile cover overlap |

### 3.2 Avatar styling

| State | Rule |
|---|---|
| Default | circular image |
| Active/current user | mint ring `2` |
| Verified | badge bottom-right |
| Online | small green dot bottom-right |
| Stacked | overlap `-8` to `-12`, max 3 visible + counter |
| Placeholder | initials or flat user icon, not emoji |

### 3.3 Verified badge on avatar

| Property | Value |
|---|---:|
| Size on `avatar.md` | `14` |
| Size on `avatar.lg` | `18` |
| Size on profile avatar | `24` |
| Background | mint |
| Icon | white check |
| Border | theme surface `2` |

---

## 4. ICON SYSTEM

### 4.1 Icon sizes

| Token | Size | Usage |
|---|---:|---|
| `icon.xs` | `14` | micro labels, badges |
| `icon.sm` | `18` | chips, small rows |
| `icon.md` | `22` | inputs, list rows |
| `icon.lg` | `26` | header/nav |
| `icon.xl` | `32` | hero icon cards |
| `icon.hero` | `44–56` | success/security large icons |

### 4.2 Icon style

Rules:
- Use flat SVG icons.
- Stroke width should visually match `2`.
- Do not mix heavy filled icons with thin outline icons in the same component.
- Colored icon squares are allowed and should follow semantic colors.
- No emoji as UI icons.

### 4.3 Icon container sizes

| Container | Size | Radius | Usage |
|---|---:|---:|---|
| `iconBox.sm` | `32` | `10` | setting rows compact |
| `iconBox.md` | `40` | `12` | inputs/list rows |
| `iconBox.lg` | `52` | `16` | create menu, premium rows |
| `iconBox.hero` | `72–88` | `999` | auth/security success |

---

## 5. BADGES & PILLS

### 5.1 Status badges

| Badge | Visual |
|---|---|
| Verified | mint circle/check |
| PRO | mint/teal pill |
| Premium | mint pill or gradient accent |
| Live | red pill with optional pulse |
| New | mint or blue small pill |
| Online | small green dot |
| Recommended | mint pill |
| Best seller | warm coral/orange pill |
| Hidden/Locked | neutral/dimmed pill |

### 5.2 Badge dimensions

| Badge type | Height | Radius | Padding H | Text |
|---|---:|---:|---:|---|
| Micro | `18` | `999` | `6` | `10/700` |
| Small | `22` | `999` | `8` | `11/700` |
| Standard | `26` | `999` | `10` | `12/800` |

### 5.3 Live badge

| Property | Value |
|---|---:|
| Background | `status.live` |
| Text | white |
| Height | `22–24` |
| Pulse | opacity/scale pulse every `1200–1600ms` |
| Card border | red for live cards |

Rules:
- Live card border may animate if already supported.
- Animation must be subtle, not distracting.

---

## 6. BUTTON SYSTEM

### 6.1 Primary CTA

Use everywhere for primary actions.

| Property | Value |
|---|---:|
| Height | `56` |
| Radius | `999` |
| Padding H | `20–24` |
| Font | `16/800` |
| Text | white |
| Gradient | `#2EE6C7 → #12B6C3` |
| Dark shadow | `0 12 32 rgba(46,216,195,0.34)` |
| Light shadow | `0 12 28 rgba(46,216,195,0.24)` |

### 6.2 Primary compact

Used for header actions like `Publier`.

| Property | Value |
|---|---:|
| Height | `40` |
| Radius | `999` |
| Padding H | `16–18` |
| Font | `15/800` |
| Glow | medium |

### 6.3 Secondary outline

| Property | Value |
|---|---:|
| Height | `52` |
| Radius | `999` |
| Border | `1.5` mint |
| Background | transparent |
| Text | mint |
| Glow | none or very subtle |

### 6.4 Tertiary text

Used for:
- Renvoyer le code
- Passer cette étape
- Retour à la connexion
- Fermer

| Property | Value |
|---|---:|
| Height | `36–44` touch target |
| Text color | mint |
| Font | `14/700` |

### 6.5 Press states

| State | Rule |
|---|---|
| Pressed primary | scale `0.98`, opacity `0.92` |
| Pressed card | scale `0.99`, border slightly stronger |
| Disabled | opacity `0.45`, no glow |
| Loading | spinner left or centered, label optional |

---

## 7. INPUTS & FORM CONTROLS

### 7.1 Text input

| Property | Value |
|---|---:|
| Height | `56` |
| Radius | `16` |
| Padding H | `16` |
| Icon left | `20–22` |
| Label | `12/700`, uppercase, letter spacing `0.8` |
| Border default | theme border |
| Border focus | mint |
| Focus glow | subtle |
| Error border | danger |
| Helper/error text | `12/600` |

### 7.2 Text area

| Property | Value |
|---|---:|
| Min height | `120` |
| Radius | `18` |
| Padding | `16` |
| Counter | bottom-right or below |

### 7.3 Code input boxes

| Property | Value |
|---|---:|
| Size | `52–58` square |
| Radius | `14–16` |
| Gap | `8–10` |
| Active border | mint |
| Active glow | subtle |
| Text | `28/800`, mint |
| Empty border | neutral |

### 7.4 Search bar

| Property | Value |
|---|---:|
| Height | `44–48` |
| Radius | `14–999` depending context |
| Icon | left search |
| Clear icon | right if text exists |
| Background | theme surface |
| Focus border | mint subtle |

---

## 8. CHIPS, TAGS, FILTERS

### 8.1 Standard chip

| Property | Value |
|---|---:|
| Height | `32–36` |
| Radius | `999` |
| Padding H | `12–14` |
| Border | neutral |
| Text | `13–14/700` |

### 8.2 Active chip

| Property | Value |
|---|---:|
| Border | mint |
| Text | mint |
| Background | mint translucent |
| Glow | subtle only |

### 8.3 Hashtag chip

| Property | Value |
|---|---:|
| Height | `36–40` |
| Radius | `999` |
| Active | mint text/border/glow |
| Remove icon | x, `14–16` |

### 8.4 Filter chips

Rules:
- Never solid green.
- Active chip may have mint translucent background only.
- Used in Peaks/Live, Search, Interests, Profession, Expertise.

---

## 9. TABS

### 9.1 Fan / Vibes / Xplorer

| Property | Value |
|---|---:|
| Container height | `44` |
| Tab height | `38–40` |
| Radius | `999` |
| Active bg light | white |
| Active bg dark | `dark.surface` |
| Active text | mint |
| Active border | mint subtle |
| Inactive text | muted |
| Glow | active tab subtle |

### 9.2 Profile sub-tabs

Used for:
- Posts / Peaks / Activities / Saved
- Lifestyle / Channel
- Channel / 1:1 / Packs

| Property | Value |
|---|---:|
| Height | `44–48` |
| Radius | `999` |
| Icon | left `16–18` |
| Active | mint text + border + glow |
| Inactive | muted |
| Background | transparent or surface |

Rules:
- Max two visible tab levels if possible.
- If three levels are needed, make the third level visually lighter.

---

## 10. CARDS

### 10.1 Standard card

| Property | Value |
|---|---:|
| Radius | `20` |
| Padding | `16` |
| Border | theme border |
| Shadow | theme card shadow |

### 10.2 Compact row card

| Property | Value |
|---|---:|
| Height | `64–76` |
| Radius | `16–18` |
| Padding | `12–16` |
| Icon box | `40` |
| Chevron | right |

### 10.3 Create menu row card

Use the stronger right-side maquette style.

| Property | Value |
|---|---:|
| Height | `78–88` |
| Radius | `20` |
| Icon box | `52` |
| Icon glow | feature color |
| Title | `18/800` |
| Subtitle | `14/500` |
| Chevron | right |
| Gap between rows | `10–12` |

### 10.4 Feed card

| Property | Value |
|---|---:|
| Radius | `20–24` |
| Media radius | `18–22` |
| Padding | `12–16` |
| Avatar | `32–40` |
| Meta text | muted |
| Action row | fixed spacing |

### 10.5 Profile stat block

| Property | Value |
|---|---:|
| Min height | `64` |
| Radius | `16` |
| Number | `24–28/800` |
| Label | `11–12/700 uppercase` |

### 10.6 Settings row group

| Property | Value |
|---|---:|
| Group radius | `18–20` |
| Row height | `56–64` |
| Divider | subtle |
| Icon box | `36–40` |
| Chevron | muted |

---

## 11. MODALS, SHEETS, ALERTS

### 11.1 Bottom sheet

| Property | Value |
|---|---:|
| Top radius | `30` |
| Padding H | `24` |
| Padding top | `12` after handle |
| Handle | `44 x 5`, radius pill |
| Overlay | black `0.45–0.60` |
| Max height | `90% screen` |

### 11.2 Confirmation modal

| Property | Value |
|---|---:|
| Width | screen - `40` |
| Radius | `24` |
| Padding | `24` |
| Icon hero | `56–72` |
| Primary CTA | `SmButton primary` |
| Secondary | outline/text |

### 11.3 Toast

| Property | Value |
|---|---:|
| Height | `48–56` |
| Radius | `16` |
| Position | top safe-area + 12 or bottom above nav |
| Icon | `20` |
| Shadow | card shadow |
| Duration | `2400–3200ms` |

Toast types:
- success
- error
- warning
- info

---

## 12. EMPTY / ERROR / LOADING STATES

### 12.1 Empty state

| Element | Rule |
|---|---|
| Icon | `56–72`, flat SVG |
| Title | `20/800` |
| Body | `14–16` muted |
| CTA | optional primary or secondary |
| Container | centered or card, depending screen |

Examples:
- No posts
- No peaks
- No notifications
- No messages
- No sessions
- No search results

### 12.2 Error state

Use:
- error icon
- short title
- human body copy
- retry CTA
- no raw red wall of text

### 12.3 Skeletons

| Skeleton | Rule |
|---|---|
| Feed card | media rectangle + text bars |
| Profile | cover + avatar + stat blocks |
| List | avatar + two bars |
| Settings | icon + title row |
| Grid | rounded blocks |

Animation:
- shimmer duration `1200–1600ms`
- low contrast
- respect reduced motion if available

---

## 13. MOTION SYSTEM

### 13.1 Durations

| Token | Duration | Usage |
|---|---:|---|
| `motion.instant` | `80ms` | tap feedback |
| `motion.fast` | `150ms` | hover/press, chip select |
| `motion.normal` | `220ms` | tab switch, row expand |
| `motion.slow` | `320ms` | modal/sheet enter |
| `motion.extraSlow` | `450ms` | hero/success only |

### 13.2 Easing

| Token | Usage |
|---|---|
| `ease.standard` | normal UI transitions |
| `ease.out` | elements entering |
| `ease.in` | elements exiting |
| `ease.springSoft` | central plus / sheet snap |
| `ease.springTight` | tab active indicator |

### 13.3 Component motion

| Component | Motion |
|---|---|
| Button press | scale `0.98`, `80–120ms` |
| Card press | scale `0.99`, border strengthen |
| Bottom sheet enter | translateY from bottom, `320ms` |
| Modal enter | opacity + scale `0.96→1`, `220ms` |
| Tab active | indicator slide, `220ms` |
| Toast | slide/fade, `220ms` |
| Live pulse | `1200–1600ms` loop |
| Skeleton | shimmer, `1200–1600ms` |

---

## 14. SCREEN-SPECIFIC POLISH CHECKS

### Auth / Access
- Logo theme correct.
- CTA glow consistent.
- No scroll unless keyboard forces it.
- Keyboard does not cover CTA without scroll recovery.
- Back/close safe-area correct.
- Code boxes aligned.

### Onboarding
- Progress bar consistent.
- CTA not on chips.
- Dense chip screens have stable “Voir plus”.
- BusinessCategory has one final design only.
- Form fields same height/radius.
- Success screens minimal and not over-buttoned.

### Home / Vibes / Xplorer
- Same main header.
- Same Fan/Vibes/Xplorer tabs.
- Same bottom nav.
- Vibes does not include fake cards.
- Xplorer sheet uses same card/chip system.
- Home keeps required “LA TRIBU”.

### Profile
- Same cover/avatar/stat system.
- Same profile tabs.
- Same creator sub-tabs.
- Owner/visitor variants do not invent separate styles.
- Personal owner removes nonexistent Modifier button.
- Vibesmood counter added where required.

### Create / Post / Peak
- Create menu uses row-card glowing sheet style.
- Gallery camera icon removed if redundant.
- Details uses secondary header + compact primary CTA.
- Post success has no CTA and auto-dismisses.
- Hashtags use `SmChip`.

### Settings / Messages / Notifications
- Settings use p1_settings_v2 style.
- New message uses user cards.
- Notifications use person photos / stacked avatars.
- Icons flat, no emoji.

### Creator / Packages / 1:1
- Package setup/edit unified.
- Fixed CTA not covering scroll content.
- 1:1 owner screens remove visitor-only subject field.
- Success screens not deformed.
- Channel setup sub-screens fixed if off-screen.

### Live / Premium / Business
- Go Live preview card removed if founder requested.
- Live ended has Smups CTA.
- Business hidden routes not polished unless revived.
- UpgradeToPro does not include verified badge.

---

## 15. CLAUDE EXECUTION GUARDRAILS

Claude must not do broad work without a lot plan.

For each lot:

1. Read both design docs.
2. List target files.
3. List components to reuse/create.
4. Show expected visual change.
5. Modify only those files.
6. Run `npx tsc --noEmit`.
7. Generate/serve preview or screenshots.
8. Stop for founder validation.

### Required output per lot

Claude must report:

- changed files
- screens affected
- before/after visual link or screenshots
- typecheck result
- unresolved questions
- rollback plan

---

## 16. DO NOT DO

- Do not create a new unrelated design.
- Do not change business logic while harmonizing style.
- Do not expose hidden flows just because they look designed.
- Do not add fake content/cards that do not exist in code.
- Do not replace working screens with HTML-inspired approximations.
- Do not use one-off hardcoded colors.
- Do not keep two styles for the same component.
- Do not let CTA overlap scroll content.
- Do not hide broken route issues behind visual polish.

---

## 17. FINAL STANDARD

A Smuppy screen is considered visually harmonized only if:

- It uses canonical tokens.
- It uses canonical CTA.
- It uses canonical card/chip/input/tab/nav components.
- It respects safe-area.
- It works in light and dark mode.
- It has no emoji system icons.
- It has no off-screen controls.
- It has no duplicate visual pattern for the same function.
- It can be compared side-by-side with the approved Auth/Profile/Vibes/Post maquettes and feel like the same app.
