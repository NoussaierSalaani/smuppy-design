# V2 Dogfood Fix Plan — "tout conforme aux maquettes, 1000%"

> Source: founder device dogfood 2026-06-13. Goal: every wired V2 screen is maquette-identical in **design + logic + wiring + 100% functional + backend-exists + security/perf**, validated screen-by-screen before moving on. Branch `feat/v2-ui-integration` (never main).

## Per-screen DONE gate (founder rule — no screen is "done" until ALL true)
1. **Design** = byte-faithful to the maquette (layout, mint tokens, spacing, icons, FR copy).
2. **Logic** = correct behaviour (the screen does what the maquette implies).
3. **Wiring** = every button/tap/field connected to a real handler/route.
4. **Functional 100%** = works on device (no dead button, no stuck loader, no lost state).
5. **Backend exists + correct** = the data/endpoint is real; if missing → ultra-detailed Jira ticket → Hamza.
6. **Security + perf** = inputs validated, no leak, FlatList/memo perf, cleanup on unmount.
7. **+1 regression test** + tsc 0 / lint 0 / jest green.

---

## WAVE 0 — SYSTEMIC (fix once → fixes many screens) — HIGHEST LEVERAGE
- **S1 — Text inputs broken app-wide.** Every multi-line field renders single-line, can't wrap, can't scroll back to line start, bio can't grow. → Fix the V2 `Input`/`TextArea` atom: `multiline` support, auto-grow, `textAlignVertical: top`, proper height, line wrap. Sweep ALL `<Input>`/`TextInput` usages (bio, appeal, report, correction, channel desc, etc.).
- **S2 — Design-system not applied to some screens.** Some render V1 design (Dispute Center) or wrong mint.
  - **MINT DECISION (CTO, locked Jun 13):** the theme is correct — keep `primary = #33A089` (deepened for WCAG: #26C1A4 on white = 2.48:1 < the 3:1 non-text minimum + white-CTA-ink contrast). The maquette's brighter mint **#26C1A4 already exists as `primaryAccent`**. RULE: **text + CTA ink** use `primary`/`gradientAA`; **decorative** surfaces (icon tiles, glows, active chips, rings, badges, accent fills) use **`primaryAccent` (#26C1A4)** = the maquette mint. Do NOT globally change the brand token (breaks a11y + App Store). Per-screen, switch decorative mint from `primary`→`primaryAccent` where the maquette shows the brighter shade.
  - V1→V2 design: rebuild screens still rendering V1 (Dispute Center) + apply the canonical **tab** style everywhere tabs appear.
- **S3 — Tappability pattern.** Profile stats / avatar / cover / post-peak-saved tiles must be tappable to the right destination. → A consistent `onPress` wiring pass.

## WAVE 1 — FEEDS
- **F1 — VibesFeed card models by content type.** Currently shows author name BELOW the post. Correct: **video** → full video card; **image / multi-content** → card shows author avatar+name INSIDE the card overlaid on the content image. → Rework `VibesFeedView` cell to branch on media type.
- **F2 — Peaks feed.** Add the **bottom nav**; tabs are NOT maquette-conform (fix to maquette tab style); create **mock data** to populate so it shows realistic content. → `PeaksLiveView` tabs + bottomnav + fixtures.

## WAVE 2 — PROFILE (big)
- **P1 — Header.** Fans/Posts/Peaks counters not maquette-identical; **cover photo dimensions** wrong → enlarge avatar a bit + lower the cover so the avatar sits at the **lower third-quarter** of the cover; **settings icon** wrong position. Tabs (Posts/Peaks/Activités/Enregistré) too cramped → fit the dedicated space; **"Posts" is English → FR**.
- **P2 — Tappability.** Stats → Fans/Tracking screen (exists in maquettes); avatar + cover tappable; post/peak/saved tiles → open detail.
- **P3 — Packs (owner).** Each pack must be **clickable to view** + a **"Configurer" button per pack** (edit). Current "Configurer" opens the create-pack screen only → missing per-pack edit. → Pane + per-pack edit route (+ Jira if backend missing).
- **P4 — Activités tab logic.** Must show activities the user **CREATED** + activities the user **PARTICIPATES** in, with **past ones kept in history**. Verify maquettes + code; likely missing → Jira Hamza.
- **P5 — 1:1 owner stats row + business Programme tab** (from earlier audit).

## WAVE 3 — SETTINGS SUB-SCREENS (the biggest batch — all flagged non-conform)
- **Edit profile**: wrong format; bio single-line → multiline; gender select icons colored (♂ blue / ♀ pink / other black); harmonize design with app; **Save button not visible** → show it; lose-changes-on-exit (keep existing logic); **photo crop/edit before save**; Save button stuck loading → fix wiring.
- **Appearance + Language**: clicking changes the option DIRECTLY → must open a **small choice sub-screen** instead.
- **Notification settings**: every filter + toggle must be **really functional**.
- **Privacy & consent**: REMOVE "Données & analytics" + the consent-withdraw section + "Conformité Art 16 RGPD" label; KEEP Télécharger + Rectifier; INTEGRATE the Privacy-Settings visibility toggles here; make all toggles really functional.
- **Security**: "Changer le mot de passe" → open the **reset-password flow** (like auth, code entry) not a dead email; REMOVE bio-auth toggle (N/A); ADD the **MFA flow** from the maquettes.
- **Blocked users** (wrong + misfit), **Find friends** (wrong, not the maquette), **Follow requests** (suivies des demandes), **Muted users** (sourdine) → maquette-conform.
- **Manage subscriptions**: apply maquette + verify every button.
- **Channel ("Ma chaîne")**: "Voir l'analytique" not clickable; verify the real maquette UI for this screen + sub-screens.
- **Help center**: premiers pas / payment / abonnement — nothing works on click → wire; **Dispute center renders V1 design** → rebuild V2.
- **Export data**: verify wiring + design + backend exists + functional.
- **Terms & policies**: validate design coherent with app.

## WAVE 4 — PAYMENTS
- **SmupWallet** ("Mon portefeuille"): wrong design/format/mint + missing "Envoyer" CTA + wrong title namespace.
- **CreatorWallet**: not the maquette + wrong format.

## "Explorer des créateurs" button (home/profile)
- It's an **incorrect button** (wrong logic) that opens a non-conform, non-fullscreen search screen with a dead back arrow. → Remove/fix the button + the screen it opens.

---

## BACKEND TICKETS (Hamza) — where code/backend is missing
- Activities: user's CREATED + PARTICIPATING activities + history endpoint.
- Per-pack edit (get + update a single package).
- Channel analytics screen data.
- 1:1 closed-dates persistence + multi-duration (KAN-2342 already covers multi-duration).
- FollowRequests requester: business_category + fan_count fields.
- (Others surface during the waves.)

## ORCHESTRATION
- Execute wave by wave. Within a wave, screens are independent → parallel main-tree agents (NO worktree — lesson learned), each owns disjoint files, no commit; I run central gates (tsc/lint/jest) + commit per screen.
- **Per-screen validation gate** (the 7 points above) before marking done. No "câblé = done" — only "conforme device-ready = done".
- Founder validates each wave on the preview OTA before the next.
