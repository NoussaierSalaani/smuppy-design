# Smuppy V2 UI Branch Audit - local only

Date: 2026-06-14  
Repo: `/Users/noussaier/smuppy-mobile`  
Current branch: `design/v2-canonic-jun14`  
Scope: audit, comparison, and visual-validation artifacts only. No commit, no push, no existing screen/component/token change.

## 1. Resume executif

Best base to continue: `design/v2-canonic-jun14`, with a strict split of responsibilities:

- Use `feat/v2-ui-integration` as the RN integration base. It contains the broad V2 component/screen wiring and the latest local app implementation work.
- Use the three commits on top in `design/v2-canonic-jun14` as the current design truth layer. They add `docs/design/CORRECTIONS_REFERENCE.md`, `docs/design/CANONIC_FINAL_VERSION.md`, `docs/design/_kit/canonic.css`, `MASTER_V2_FLOW.html`, `PROTOTYPE.html`, `COMPARE.html`, and the canonic gallery.
- Do not use `main` as the UI base. Local `main` has only early V2 atoms and no `docs/design`.
- Treat `develop`, `origin/ui/NewUi`, and `ui/nouss/auth` as the same older UI family (`db2643ba7`) useful for comparison only.
- Treat old remote atom branches like `origin/feat/v2-final-hardening`, `origin/feat/v2-ui-upload-menu`, and `origin/feat/v2-*atom` as historical sources only; their tokens still show older bright/neon colors.

Important audit caveat: I did not fetch remote refs, to avoid modifying `.git` during this audit. This report uses the local and remote-tracking refs already present in the repo.

## 2. Working tree snapshot

`git status -sb` at audit start:

```text
## design/v2-canonic-jun14...origin/design/v2-canonic-jun14
 M _preview/main.jsx
 M aws-migration/lambda/api/__tests__/activities/gallery-list.test.ts
?? _preview/index.html.bak
?? docs/audit/AUDIT_FABLE_7DIM_DEVELOP_2026-06-10.md
?? docs/security/AUDIT_FABLE_DEVELOP_2026-06-10.md
?? src/__tests__/screens/_nmmin.test.tsx
```

These pre-existing changes were not touched.

## 3. Branch cartography - high signal refs

| Branch/ref | Last SHA | Date | Last message | docs/design | src/components/v2 | src/theme/v2 | HTML maquettes | Prototype/gallery | Probable interest |
|---|---:|---|---|---:|---:|---:|---:|---|---|
| `design/v2-canonic-jun14` | `d47f90cb0` | 2026-06-14 16:39 -04:00 | docs(design): CORRECTIONS_REFERENCE.md | 846 | 551 | 7 | 363 | Yes: `PROTOTYPE`, `MASTER_V2_FLOW`, `COMPARE`, canonic gallery | Best current combined base: RN from `feat` plus latest design truth. |
| `origin/design/v2-canonic-jun14` | `d47f90cb0` | 2026-06-14 16:39 -04:00 | same as local | 846 | 551 | 7 | 363 | Yes | Remote-tracking mirror of current branch. |
| `feat/v2-ui-integration` | `93b1b5c99` | 2026-06-14 13:49 -04:00 | fix(v2): systemic back-arrow sweep | 646 | 551 | 7 | 170 | Partial: creator-config gallery, no canonic final docs | Best RN implementation base before the canonic docs layer. |
| `origin/feat/v2-ui-integration` | `30617eb2e` | 2026-06-12 21:23 -04:00 | feat(v2): Report a problem | 644 | 548 | 7 | ~168 | Partial | Remote is behind local `feat/v2-ui-integration`; do not prefer it over local without fetching/reconciling. |
| `main` | `685d36686` | 2026-05-24 12:09 -04:00 | feat(feeds): peaks-lives FanFeed scope split | 0 | 16 | 5 | 0 | No | Stable older baseline, not enough for V2 harmonization. |
| `origin/main` | `437131ef0` | 2026-05-25 17:27 +01:00 | Fix3/bugs template1 (#361) | 0 | 16 | 5 | 0 | No | Remote-tracking main differs from local main but still lacks V2 design docs. |
| `develop` | `db2643ba7` | 2026-06-10 18:29 +01:00 | fix(v2-ui): feed review round 4 | 0 | 57 | 5 | 0 | No | Older UI review branch; useful as drift reference only. |
| `origin/develop` | `db2643ba7` | 2026-06-10 18:29 +01:00 | same as local | 0 | 57 | 5 | 0 | No | Same as `develop`. |
| `origin/ui/NewUi` | `db2643ba7` | 2026-06-10 18:29 +01:00 | same as develop | 0 | 57 | 5 | 0 | No | Same SHA as `develop` and `ui/nouss/auth`; not current truth. |
| `ui/nouss/auth` | `db2643ba7` | 2026-06-10 18:29 +01:00 | same as develop | 0 | 57 | 5 | 0 | No | Same SHA as `develop`. |
| `origin/design/creator-config-may28` | `f733294ca` | 2026-06-07 23:13 -04:00 | docs(v2): wave-25 + flow-audit | 578 | 542 | 6 | 168 | Creator config gallery/screenshots | Useful historical creator-config proof, not global truth. |
| `origin/feat/v2-ui-upload-menu` | `5384ab7af` | 2026-06-09 02:55 +01:00 | wire V2 create menu | 0 | 20 | 5 | 0 | No | Historical create-menu integration; tokens still old neon. |
| `origin/feat/v2-final-hardening` | `134b5b089` | 2026-05-17 12:48 -04:00 | V2-FINAL-HARDENING | 0 | 8 | 5 | 0 | No | Historical atom hardening; not enough V2 surface. |

## 4. All refs matched by keywords

Matched keywords: `ui`, `v2`, `design`, `canonic`, `canonical`, `maquette`, `mockup`, `creator`, `integration`, `feat`, plus `main` and `develop`. Count: 138 refs.

```text
chore/delete-battles-feature
claude/peak-creation-feat
deploy/ml-staging-may13-v2
design/creator-config-may28
design/v2-canonic-jun14
develop
feat/activities-v2-phase-2
feat/activities-v2-phase-3-ui
feat/activities-v2-phase-3a
feat/audit-100-batch-may17
feat/batch-smu268-smu273-lambda-hardening
feat/cdk-aspects-wire-may17
feat/channel-members-management
feat/ci-auto-rerun-flakes-may17
feat/dev-env-setup-may21
feat/fan-creator-1on1-booking-may19
feat/fixed-conflict-uiux
feat/jira-tickets-decortication-may19
feat/ml-service-phase2-may13
feat/ml-service-phase3-may14
feat/ml-service-phase3-pr249-text-shadow
feat/nim-routing
feat/personal-activity-run-v1
feat/post-controller-consolidation
feat/sentinel-otp-signup-probe-may17
feat/smu160-apple-jws-chain-validation
feat/smu161-ws-lambda-authorizer
feat/smu192-kms-encryption-gaps
feat/smu197-secret-rotation
feat/smu206-expo-image-migration
feat/smu228-iam-allowlist-baseline
feat/smu241-activate-ota-regression-sentinel
feat/smu268-webhook-lru-cap
feat/smu273-ws-lambda-reserved-concurrency
feat/smuppy-train
feat/smuppy-train-frontend-fan
feat/v2-ui-integration
feat/vague1-prA-smu164-smu188-db-security
feat/vague1-prB-smu167-sentry-observability
feat/vague1-prD-smu170-smu171-iam-allowlist
feat/vague2-prF-smu194-smu185-dlq-alarms
feat/vague2-prG-smu131-pg-promiseall-client-race
feat/vague2-prH-smu193-smu183-network-aurora
feat/vague3-lambda-dlq-wiring
feat/vague4-prJ-smu203-useuserstore-controller-migration
feat/vague4-prK-smu210-expo-image-16-sites
feat/vague4-prL-smu206-reanimated-native-driver
feat/vague4-prM-smu260-smu261-smu263-v2-theme-codemod
feat/vague5-prN-smu248-gdpr-rectify-endpoint
feat/vague5-prO-smu240-smu241-sentinels-activate
feat/vague6-prP-smu162-175-176-preauth-cognito-batch
feat/vague6-prQ-smu182-eager-eval-env-codemod
feat/vague6-prR-smu169-fnimportvalue-audit
feat/visual-regression
feature/activities-phase4a
feature/activities-phase4b
feature/activities-phase4c
feature/smups-implementation
fix/bug-009-search-creator-tab-and-scrollable-chips
fix/ci-required-checks-paths-deadlock
main
origin/chore/ai-feature-flags-phase0-may17
origin/design/creator-config-may28
origin/design/v2-canonic-jun14
origin/develop
origin/docs/ai-feature-suite-master-spec-may17
origin/feat/activities-v2-phase-2
origin/feat/activities-v2-phase-3-ui
origin/feat/activities-v2-phase-3a
origin/feat/age-up-minors-cron-may17
origin/feat/audit-100-batch-may17
origin/feat/cdk-aspects-wire-may17
origin/feat/channel-members-management
origin/feat/ci-auto-rerun-flakes-may17
origin/feat/dev-env-setup-may21
origin/feat/dsar-include-is-minor-may17
origin/feat/fan-creator-1on1-booking-may19
origin/feat/image-optimization-pipeline
origin/feat/ml-service-phase2-may13
origin/feat/ml-service-phase3-may14
origin/feat/ml-service-phase3-pr249-text-shadow
origin/feat/ml-service-phase3-pr251-video
origin/feat/ml-service-phase3-pr252-live
origin/feat/ml-service-phase3-pr253-tier-router
origin/feat/ml-shadow-mode-enable
origin/feat/mmp-branch-sdk-may15
origin/feat/nim-routing
origin/feat/peaks-challenge-redesign
origin/feat/personal-activity-run-v1
origin/feat/post-controller-consolidation
origin/feat/pr-validator-auto-patch
origin/feat/privacy-policy-ai-disclosure-may17
origin/feat/profiles-blocked-fields-may17
origin/feat/profiles-is-minor-migration-may17
origin/feat/sentinel-otp-signup-probe-may17
origin/feat/skill-smuppy-pr-shipper
origin/feat/smu160-apple-jws-chain-validation
origin/feat/smu161-ws-lambda-authorizer
origin/feat/smu192-kms-encryption-gaps
origin/feat/smu197-secret-rotation
origin/feat/smu206-expo-image-migration
origin/feat/smu268-webhook-lru-cap
origin/feat/smu273-ws-lambda-reserved-concurrency
origin/feat/smuppy-train
origin/feat/smuppy-train-frontend-fan
origin/feat/unified-activities
origin/feat/v2-bottomsheet-atom
origin/feat/v2-emptystate-atom
origin/feat/v2-final-hardening
origin/feat/v2-tabbar-atom
origin/feat/v2-toast-atom
origin/feat/v2-ui-integration
origin/feat/v2-ui-upload-menu
origin/feat/vague1-prA-smu164-smu188-db-security
origin/feat/vague1-prB-smu167-sentry-observability
origin/feat/vague1-prD-smu170-smu171-iam-allowlist
origin/feat/vague2-prF-smu194-smu185-dlq-alarms
origin/feat/vague2-prG-smu131-pg-promiseall-client-race
origin/feat/vague2-prH-smu193-smu183-network-aurora
origin/feat/vague3-lambda-dlq-wiring
origin/feat/vague4-prJ-smu203-useuserstore-controller-migration
origin/feat/vague4-prK-smu210-expo-image-16-sites
origin/feat/vague4-prL-smu206-reanimated-native-driver
origin/feat/vague4-prM-smu260-smu261-smu263-v2-theme-codemod
origin/feat/vague5-prN-smu248-gdpr-rectify-endpoint
origin/feat/vague5-prO-smu240-smu241-sentinels-activate
origin/feat/vague6-prP-smu162-175-176-preauth-cognito-batch
origin/feat/vague6-prQ-smu182-eager-eval-env-codemod
origin/feat/visual-regression
origin/feature/activities-phase4a
origin/feature/activities-phase4b
origin/feature/activities-phase4c
origin/feature/smups-implementation
origin/fix/bug-009-search-creator-tab-and-scrollable-chips
origin/fix/ci-required-checks-paths-deadlock
origin/main
origin/ui/NewUi
ui/nouss/auth
```

## 5. Main branch comparisons

| Comparison | Ahead/behind | Files changed | UI/design changed | RN changed | docs/design changed | maquette/prototype changed | Probable conflicts | Base recommendation |
|---|---:|---:|---:|---:|---:|---:|---|---|
| `design/v2-canonic-jun14` vs `feat/v2-ui-integration` | `3 / 0` | 257 | 255 docs/design | 0 RN V2; only `src/config/iap-products.ts` and one test | 255 | 238 | Low: merge-base is `feat/v2-ui-integration`, overlap changed = 0 | Continue from `design/v2-canonic-jun14`; it is exactly `feat` plus design truth. |
| `design/v2-canonic-jun14` vs `main` | `418 / 0` | 2614 | 544 V2 UI/theme files and 846 design docs | 675 RN files | 846 | 369 | Low by merge-tree/overlap, but huge operational blast radius | Do not restart from `main`; too much V2 work missing. |
| `feat/v2-ui-integration` vs `main` | `415 / 0` | 2413 | 544 V2 UI/theme files and 646 design docs | 675 RN files | 646 | 175 | Low by merge-tree/overlap, but huge operational blast radius | Best app implementation baseline if canonic docs are applied after. |

Three commits between `feat/v2-ui-integration` and `design/v2-canonic-jun14`:

```text
d47f90cb0 docs(design): CORRECTIONS_REFERENCE.md
503e44a74 test(v2): mock @expo/vector-icons in ProfessionScreen test
29e19ab10 design(v2): canonic maquette campaign + shared canonic.css + CANONIC_FINAL_VERSION
```

Non-doc files changed by those three commits:

```text
M src/__tests__/screens/ProfessionScreen.test.tsx
M src/config/iap-products.ts
```

## 6. Design-system audit

| Candidate | Tokens | Button | Header | Bottom nav | Tabs/chips | No emoji rule | Assessment |
|---|---|---|---|---|---|---|---|
| `design/v2-canonic-jun14` | `#33A089`, CTA `#1A7D68 -> #157082`, glow tokens present | Gradient button uses `LinearGradient` and white ink; outline variant present | Canonical header specified in docs: search / Smuppy / notif | `BottomNav` component present with founder notes, mint ring/glow | `TabBar` has pill-card and outline/glow guidance; no separate `Chip` atom found | Docs explicitly require no emoji as icon; some gallery nav HTML still uses emoji labels | Best source of truth; RN still needs disciplined application of docs. |
| `feat/v2-ui-integration` | Same current RN tokens as `design/v2-canonic-jun14` | Same Button as current base | `FeedHeaderV2` exists; final canonic docs absent | `BottomNav` present | `TabBar` present; no separate `Chip` atom found | RN code still has glyph fallback defaults in several views | Best RN integration base, but missing latest founder correction docs. |
| `main` | V2 tokens exist, but older surface | `Button` and `TabBar` only | No current canonic header docs | No `BottomNav` component in `src/components/v2` | Limited atom set | Not enough V2 surface to audit globally | Too old for harmonization. |
| `develop` / `origin/ui/NewUi` / `ui/nouss/auth` | Current-ish `#33A089` token family | Button exists | No canonic docs | BottomNav exists | TabBar exists, less complete | Multiple glyph/emoji fallbacks in RN views | Useful as earlier UI review state, not final truth. |
| `origin/design/creator-config-may28` | Current-ish `#33A089` RN tokens | Button exists | No canonic final docs | BottomNav exists | TabBar exists | Creator maquettes include emojis in success/profile copy and scripts | Good creator-config reference only. |
| `origin/feat/v2-ui-upload-menu` / `origin/feat/v2-final-hardening` | Old bright/neon tokens: `#26C1A4`, gradient `#11E3A3 -> #00B3C7` | Older Button | No final header docs | Missing BottomNav in these refs | Atom-only/partial | Not reliable for founder-canonical direction | Historical only. |

Specific requested file/path checks:

| Path | Current `design/v2-canonic-jun14` | `feat/v2-ui-integration` | `main` | Notes |
|---|---|---|---|---|
| `src/theme/v2/tokens.ts` | Present | Present | Present | Current branch locks RN CTA gradient to `#1A7D68 -> #157082`. |
| `src/components/v2/Button/Button.tsx` | Present | Present | Present | Current branch uses `LinearGradient`, outline variant, white gradient ink. |
| `src/components/v2/**/Button*` | Present | Present | Present | Button atom exists. |
| `src/components/v2/**/Header*` | `FeedHeaderV2` present | `FeedHeaderV2` present | Not broad/current | Header canon is currently more documented than atomized. |
| `src/components/v2/**/BottomNav*` | Present | Present | Absent | Main lacks the V2 BottomNav atom. |
| `src/components/v2/**/Tab*` | Present | Present | Present | Current branch adds fuller pill-card behavior. |
| `src/components/v2/**/Chip*` | No dedicated chip atom found | No dedicated chip atom found | No dedicated chip atom found | Chips appear implemented per view; should be consolidated later only after validation. |
| `docs/design/CORRECTIONS_REFERENCE.md` | Present | Absent | Absent | Founder correction truth. |
| `docs/design/CANONIC_FINAL_VERSION.md` | Present | Absent | Absent | Current canonic plan. |
| `docs/design/_kit/canonic.css` | Present | Absent | Absent | HTML prototype visual kit, not RN truth. |
| `docs/design/MASTER_V2_FLOW.html` | Present | Absent | Absent | Gallery/prototype review artifact. |
| `docs/design/PROTOTYPE.html` | Present | Absent | Absent | Review artifact. |
| `docs/design/COMPARE.html` | Present | Absent | Absent | Review artifact. |

## 7. Reliable vs dangerous sources

Reliable in `design/v2-canonic-jun14`:

- `docs/design/CORRECTIONS_REFERENCE.md`: founder remarks and global correction rules.
- `docs/design/CANONIC_FINAL_VERSION.md`: current canonical plan and source-of-truth list.
- `src/theme/v2/tokens.ts`: RN token truth for CTA option A/C.
- `src/components/v2/Button/Button.tsx`: RN gradient/outline button behavior.
- `src/components/v2/BottomNav/BottomNav.tsx`: most advanced current BottomNav implementation.
- `src/components/v2/TabBar/TabBar.tsx`: most advanced current segmented tab primitive.

Reliable in `feat/v2-ui-integration`:

- Broad RN V2 implementation and wiring.
- BackButton sweep and keyboard-avoiding follow-up.
- Screens/components under `src/components/v2` that match current local branch because `design/v2-canonic-jun14` is built on top.

Dangerous / drift / approximate:

- Any old atom branch with `#11E3A3 -> #00B3C7` tokens.
- `origin/feat/v2-ui-integration` if assumed equal to local `feat/v2-ui-integration`; local is ahead.
- `develop`, `origin/ui/NewUi`, `ui/nouss/auth` for final decisions; same older SHA and no final docs.
- HTML galleries as literal implementation truth. They are useful for visual review but include known drift, generated variants, and in some navigation/prototype shells still show emoji labels.

## 8. Branch base recommendation

Recommended base: `design/v2-canonic-jun14`.

Reason: it is a fast-forward continuation of `feat/v2-ui-integration` with only 3 extra commits and no overlapping changed files versus `feat`. It contains the RN integration base plus the latest design evidence and founder correction documents.

Implementation rule after founder validation:

1. Do not rewrite from HTML.
2. Apply the validated direction to RN tokens/components first.
3. Pilot on 3-4 screens: FanFeed, VibesFeed, Search/Xplorer, one settings/profile surface.
4. Then sweep global rules: header, bottom nav, segmented tabs, chips outline, CTA gradient/glow, no emoji-as-icon.

## 9. Workflow recommendation

- Keep one lot: "V2 visual harmonization foundation".
- Scope that lot to RN foundation only: tokens, Button, BottomNav, header atom/usage, TabBar/chip treatment, and a few pilot screens.
- Do not mix backend, migrations, unrelated tests, or feature behavior changes.
- Before implementation, freeze the founder choice from `VALIDATE_CANONIC_DIRECTION.html`: A, B, or C.
- After implementation, validate on device, not only HTML.
- Use `docs/design/CORRECTIONS_REFERENCE.md` as the founder feedback source, and `src/theme/v2/tokens.ts` as the RN token source.

## 10. Files not to use as source of truth

Use these for visual exploration/review only, not as implementation truth:

- `docs/design/MASTER_V2_FLOW.html`
- `docs/design/MASTER_V2_DESIGN.html`
- `docs/design/PROTOTYPE.html`
- `docs/design/COMPARE.html`
- `docs/design/_ALL_SCREENS.html`
- `docs/design/_VALIDATE.html`
- `docs/design/_DSFILL.html`
- `docs/design/canonic/harmonized/**/code.html`
- `docs/design/creator-config-may28/**/code.html`
- `_preview/index.html`

Reason: these are generated/review HTML artifacts and can drift in icons, spacing, scroll, and color treatment.

## 11. Files that should be source of truth

Design/founder truth:

- `docs/design/CORRECTIONS_REFERENCE.md`
- `docs/design/CANONIC_FINAL_VERSION.md`
- `docs/design/VIBES_FEED_CARD_SPECS.md`

RN implementation truth:

- `src/theme/v2/tokens.ts`
- `src/components/v2/Button/Button.tsx`
- `src/components/v2/BottomNav/BottomNav.tsx`
- `src/components/v2/TabBar/TabBar.tsx`
- `src/components/v2/FeedHeaderV2/FeedHeaderV2.tsx`
- Active screen/view components under `src/components/v2/**` and the screens that mount them.

Validation artifact created by this audit:

- `docs/design/VALIDATE_CANONIC_DIRECTION.html`

