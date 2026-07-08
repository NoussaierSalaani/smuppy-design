# Figma V2 Maquettes — Detailed Status (2026-06-21)

File: `55jclAfHRctBGIglAWYTWT` ("Smuppy — App Maquettes V2 (auto")). Legend: ✅ done & render-verified · ⚠️ built, not re-QA'd against visible-diff bar · ❌ not yet.

## Kit components (`✦ Kit`) — propagate to all instances
| Component | Status | Note |
|---|---|---|
| Header / feed (96:9) | ✅ verified | search LEFT + Smuppy center, bell removed |
| BottomNav (100:83) | ✅ verified | pentagon home, subtle +, profile mint-ring; sweep done → instance on all nav screens |
| Tabs / feed (99:35) | ✅ | Fan/Vibes/Xplorer pill + line icons |
| Tabs / profile-segment (1190:94) + profile-subtabs (1191:105) | ✅ verified | created + applied to all 12 profile frames |
| Cards peak-live(96:4)/suggestion(96:48)/selectable(96:68) | ✅ | |
| Buttons CTA(96:30)/ghost(96:32)/fan(96:34) | ✅ | |
| Field/input (96:39) | ✅ | rebuilt |
| Chip/selectable(96:47) + Chip/interest(153:83) | ✅ | |
| IconTile (97:79) | ⚠️ | exists; per-screen "colored dots → real icons" audit NOT done everywhere |
| Logo HQ (Assets) | ✅ | real vectors from SmuppyLogo.tsx (gradient icon + S, wordmark) |
| V2 Tokens (87:3 Light/Dark) + Plus Jakarta Sans | ✅ verified | 5128 text segments re-fonted |

## Pages
| Page | Status |
|---|---|
| ✦ Auth (24) | ⚠️ built + re-fonted + header propagated |
| ✦ Onboarding (24) | ⚠️ built + 3 corrections (AccountType multicolor icons, BusinessCategory establishments section, Success logo) |
| ✦ Daily | ✅ feeds Home/Fan/Vibes/Peaks + VibesFeed mood+chips + pentagon nav; sub-screen navs removed; 11 wrong-screens fixed (wave1) |
| ✦ Profile | ✅ COMPLETE — 12 shells, tab components, message icon, pentagon nav, light+dark |
| ✦ Activities | ⚠️ built + P0 fixes + nav swept + tail Sessions/Activity/Run built |
| ✦ Creator-Pay | ⚠️ built + tail (CreatorEarnings/PackagesSetup/SmupWallet ✅) — ❌ 3 missing: ChannelMembers, UpgradeToPro, PackPurchase |
| ✦ Settings | ⚠️ built + P0 fixes + tail (SoundUsage/PasswordManager ✅) |
| ✦ Live | ⚠️ GoLive/Preview/Ended/Streaming + tail ViewerLiveStream/WaitingRoom ✅ |
| ✦ Business-Disputes | ⚠️ built, sub-screen navs removed |
| ✦ Other | ⚠️ BlockedUsers + tail ResetCode/SmuppyForm/WebView ✅ |
| ✦ Stitch Screens | ✅ 55 reference PNGs + 63 editable rebuilds (re-fonted PJS) |
| ✦ Assets | ✅ HQ logo + tokens |
| ✦ Prototype | ⚠️ 100 light + 94 dark + ~37 flow connections — STALE (cloned before kit fixes → re-sync needed) |

## Outstanding (next quota windows)
1. 3 tail Creator-Pay: ChannelMembers, UpgradeToPro, PackPurchase (specs documented in workflow result + memory)
2. Icon-dots → real vector icons audit across all screens
3. QA Round 2 (zero-VISIBLE-diff bar) on the 63 editable rebuilds (round-1 strict bar = only 12 byte-identical)
4. Re-sync ✦ Prototype (reflect fixed kit + wire dark connections)
5. Confirm profile dark icons (likely resolved by nav/tabs fixes)

## Platform constraints hit (2026-06-20→21)
- Figma seat/plan tool-call quota (use_figma writes) repeatedly exhausted; REST renders free. Resume workflows with resumeFromRunId after reset.
- Anthropic API 529 Overloaded (transient) during the tail build — resolved via resume.
- Method locked: kit-first (components propagate) + small batches per quota window + adversarial QA. Editable ≠ pixel-identical to raster PNG (font/AA) → founder standard = PNG canonical kept + editable beside at "0 visible diff".
- SECURITY: Figma read token shared in plaintext in this session → ROTATE in Figma settings when done.
