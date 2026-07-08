/**
 * ============================================================================
 * Smuppy V2 — DESIGN SYSTEM  (theme.js)
 * ----------------------------------------------------------------------------
 * SOURCE OF TRUTH for the V2 UI. Mirrors `src/theme/v2/tokens.ts` (the real RN
 * tokens) + the founder-validated palette. Every value is documented with
 * WHERE it applies, so it can be wired without guessing.
 *
 * Validated palette (locked):
 *   • Mint accent      #33A089
 *   • Button gradient  #41AD96 → #2C95A0  (135°)
 *   • Glows            SUBTLE — rgba(51,160,137, 0.05 → 0.18)
 *
 * Charter rules (non-negotiable):
 *   • Font = Plus Jakarta Sans ONLY (weights 400/500/600/700/800). No italics.
 *   • Avatars = ROUNDED SQUARES (radius 12). NEVER circles.
 *   • Light + Dark both shipped. No neon. Calm, editorial, premium-fitness.
 *
 * How to read: `color.light.*` / `color.dark.*` = theme-adaptive. `brand.*`,
 * `radius.*`, `spacing.*`, `type.*`, `shadow.*`, `size.*` = constant. The
 * `usage` map at the bottom says element → which tokens.
 * ============================================================================
 */

// ── BRAND (constant across light/dark) ──────────────────────────────────────
export const brand = {
  // Mint accent (locked #33A089 — a11y-safe: #2BB89E as a graphic on white = 2.48:1,
  // below the 3:1 low-vision bar). Borders, badges, chips, single-color icons,
  // ACTIVE tab TEXT (Fan/Vibes/Xplorer), links, focus ring, selected states.
  // The "alive" look = the green GLOW + RING contour below, NOT a brighter hue.
  mint: '#33A089',
  // Pressed / hover darker mint + solid primary button bg on LIGHT.
  mintDeep: '#176A5A',
  // Soft mint tint — light container backgrounds (10–15% surfaces).
  mintSoft: '#A8E6D9',
  // Mint accent on DARK surfaces.
  mintInverse: '#5BB8A6',

  // GREEN GLOW + RING — the "contour" that makes buttons/toggle ALIVE (the look
  // the founder validated). rgb(43,184,158) = #2BB89E. Apply on: active toggle,
  // primary & outline buttons, hero icons, accent tiles.
  glow: 'rgba(51,160,137,0.175)',   // box-shadow blur halo (rgb of #33A089)
  ring: 'rgba(51,160,137,0.225)',   // 1px outline ring (0 0 0 1px) — the "contour"

  // PRIMARY GRADIENT — the "filled" button look.
  // Applied to: primary CTA, "Devenir fan"/"Become a fan" filled, suggestion-card
  // avatars, hero icons, go-live button. (Active TOGGLE is NOT this — it's a
  // card-bg pill with mint text + glow/ring; see usage['feed toggle…'].)
  gradient: { from: '#41AD96', to: '#2C95A0', angle: 135 },
  gradientCss: 'linear-gradient(135deg,#41AD96,#2C95A0)',
  // ⚠️ ACCESSIBILITY NOTE: white text on this gradient ≈ 2.6–3.3:1 (below WCAG AA
  // 4.5 for normal text). The RN code (tokens.ts) ships a DEEPER gradient
  // #1A7D68 → #157082 (white = 5.0/5.7:1, AA-pass) for that reason. DECISION:
  // either keep the validated look (#41AD96→#2C95A0) and accept sub-AA white ink,
  // or use the deeper gradient on text-bearing buttons. Don't ship white-on-mint
  // body text below 4.5 without a conscious call.
  gradientAA: { from: '#1A7D68', to: '#157082', angle: 135 }, // a11y-safe alt for white text
};

// ── GLOWS / SHADOWS (subtle — the validated, NON-"brillant" look) ───────────
// Mint glow = rgba(51,160,137, A). Use SPARINGLY. These are the validated levels.
export const shadow = {
  // Cards (groups of rows, content cards). Barely-there mint halo.
  card: { color: 'rgba(51,160,137,0.05)', x: 0, y: 0, blur: 16, css: '0 0 16px rgba(51,160,137,0.05)' },
  // Primary button / active toggle — soft mint lift (NOT a bright halo).
  button: { color: 'rgba(51,160,137,0.18)', x: 0, y: 6, blur: 18, css: '0 6px 18px rgba(51,160,137,0.18)' },
  // Feature / hero card (premium, MFA hero) — slightly stronger mint presence.
  feature: { color: 'rgba(51,160,137,0.15)', x: 0, y: 0, blur: 24, css: '0 0 24px rgba(51,160,137,0.15)' },
  // Neutral elevation (modals, raised surfaces) — NO mint, plain depth.
  modal: { color: 'rgba(0,0,0,0.18)', x: 0, y: 12, blur: 32, css: '0 12px 32px rgba(0,0,0,0.18)' },
  // Tinted icon-container backgrounds: use the element's hue at 0x22 (~13%).
  // e.g. mint icon box bg = 'rgba(51,160,137,0.13)'.
  iconTintAlpha: 0.13,
};

// ── THEME-ADAPTIVE COLORS ───────────────────────────────────────────────────
export const color = {
  light: {
    surface: '#FFFFFF',            // app background
    surfaceContainer: '#F8FAFC',   // cards, sheets, list groups
    surfaceContainerHigh: '#F1F5F9', // sticky headers, raised navbars, input bg
    onSurface: '#0F172A',          // primary body text, titles
    onSurfaceVariant: '#475569',   // subtitles, captions, secondary text
    onSurfaceMuted: '#475569',     // placeholders, tertiary
    outline: '#E2E8F0',            // borders, dividers between rows
    outlineVariant: '#F1F5F9',     // hairline dividers (lighter)
    primary: '#176A5A',            // SOLID primary on light (white text AA-pass 6.9:1)
    onPrimary: '#FFFFFF',          // text/icon on a primary/gradient button
    pressed: 'rgba(15,23,42,0.12)',// press overlay
    focusRing: '#176A5A',          // focus outline
    success: '#10B981', warning: '#F59E0B', danger: '#DC2626', info: '#3B82F6',
    skeleton: '#F1F5F9', skeletonHighlight: '#E2E8F0',
  },
  dark: {
    surface: '#0A0E1A',
    surfaceContainer: '#161B2A',
    surfaceContainerHigh: '#1F2538',
    onSurface: '#FFFFFF',
    onSurfaceVariant: '#94A3B8',
    onSurfaceMuted: '#94A3B8',
    outline: '#2A3142',
    outlineVariant: '#1F2538',
    primary: '#5BB8A6',            // mint on dark (use for accents; white text on gradient as above)
    onPrimary: '#003B30',
    pressed: 'rgba(255,255,255,0.12)',
    focusRing: '#5BB8A6',
    success: '#34D399', warning: '#FBBF24', danger: '#F87171', info: '#60A5FA',
    skeleton: '#1F2538', skeletonHighlight: '#2A3142',
  },
};

// ── TYPOGRAPHY (Plus Jakarta Sans) ──────────────────────────────────────────
export const font = {
  family: 'PlusJakartaSans',
  byWeight: {
    regular: 'PlusJakartaSans_400Regular',
    medium: 'PlusJakartaSans_500Medium',
    semibold: 'PlusJakartaSans_600SemiBold',
    bold: 'PlusJakartaSans_700Bold',
    extrabold: 'PlusJakartaSans_800ExtraBold',
  },
};

// preset = { fontSize, lineHeight, letterSpacing(px), fontWeight }. WHERE it applies:
export const type = {
  displayLg:  { fontSize: 32, lineHeight: 38, letterSpacing: -0.64, fontWeight: '800' }, // big hero numbers, splash titles
  headlineLg: { fontSize: 24, lineHeight: 30, letterSpacing: 0,     fontWeight: '700' }, // screen H1 (e.g. "Centre d'aide")
  headlineMd: { fontSize: 20, lineHeight: 26, letterSpacing: 0,     fontWeight: '700' }, // section headers
  headlineSm: { fontSize: 18, lineHeight: 25, letterSpacing: 0,     fontWeight: '600' }, // card titles, profile name
  title:      { fontSize: 16, lineHeight: 22, letterSpacing: 0,     fontWeight: '600' }, // list row label (emphasis), button text
  bodyLg:     { fontSize: 16, lineHeight: 26, letterSpacing: 0.16,  fontWeight: '400' }, // primary button label, paragraph
  bodyMd:     { fontSize: 14, lineHeight: 21, letterSpacing: 0.14,  fontWeight: '400' }, // list row label, body copy, sublabels
  labelMd:    { fontSize: 12, lineHeight: 17, letterSpacing: 0.24,  fontWeight: '600' }, // chips, small buttons, status pills
  labelSm:    { fontSize: 11, lineHeight: 15, letterSpacing: 0.44,  fontWeight: '500' }, // captions, row sublabel
  labelCaps:  { fontSize: 12, lineHeight: 17, letterSpacing: 1.2,   fontWeight: '700', textTransform: 'uppercase' }, // EYEBROWS / section titles ("SUPPORT", "COMPTE")
};

// ── SPACING (4pt grid). Use tokens, never raw numbers. ──────────────────────
export const spacing = {
  none: 0, xxs: 2, xs: 4, sm: 8, md: 12, lg: 16, xl: 24, '2xl': 32, '3xl': 48, '4xl': 64, '5xl': 96,
  // screen horizontal padding = lg→xl (16–20). Card inner padding = lg (16). Row gap = 12–13.
};

// ── RADIUS — with the component that uses each ──────────────────────────────
export const radius = {
  none: 0,
  xs: 6,    // tiny chips
  sm: 10,   // small avatars (24/32px)
  md: 12,   // ⬅ Button (solid/outline/ghost), Input, avatars 40px+, icon mini-cards
  lg: 16,   // small cards, secondary surfaces
  xl: 20,   // medium cards
  '2xl': 28, // ⬅ Card atom (content cards, sheets)
  '3xl': 32, // large media
  '4xl': 48, // single-post media (all aspect ratios)
  pill: 999, // ⬅ GRADIENT button / "Devenir fan" / active toggle / status pills / chips
};

// ── SIZING — control heights, icons, avatars, bottom nav ────────────────────
export const size = {
  control: { sm: 36, md: 44, lg: 52 },         // button / input heights. Primary CTA = lg(52).
  icon: { xs: 14, sm: 16, md: 20, lg: 24, xl: 28 }, // Ionicons sizes. List-row icon = sm/md (16–20).
  avatar: { xs: 24, sm: 32, md: 40, lg: 56, xl: 80, '2xl': 120 }, // rounded squares (radius.md), NEVER circles
  iconSquare: { side: 34, radius: 11 },         // ListRow leading icon container (tinted bg = hue at 13%)
  bottomNav: { height: 56, iconSize: 28 },      // flat 5-icon bar; active icon = brand.mint
  hairline: 0.5, border: 1,
  hitSlop: { sm: 6, md: 10, lg: 16 },
};

// ── ICON SYSTEM ─────────────────────────────────────────────────────────────
// All glyphs = Ionicons via @expo/vector-icons (`<Ionicons name="..." />`).
// Leading list icons sit in a 34×34 r11 square tinted with the row's hue @13%.
export const icons = { set: 'Ionicons', pkg: '@expo/vector-icons' };

// ── MOTION (calm > playful) ─────────────────────────────────────────────────
export const motion = {
  duration: { instant: 80, pressFeedback: 150, fast: 200, standard: 250, slow: 320 }, // ms
  easing: { standard: [0, 0, 0.2, 1], hover: [0.4, 0, 0.2, 1] }, // cubic-bezier (ease-out)
  pressScale: 0.97,        // applied to: any pressable on press-in
  bottomNavTapScale: 0.95, // applied to: bottom-nav icon tap
  // No bouncy springs. Toggle/sheet transitions = standard 250ms ease-out.
};

// ── Z-INDEX (predictable layering) ──────────────────────────────────────────
export const zIndex = {
  base: 0, raised: 10, dropdown: 100, sticky: 200, header: 300,
  bottomNav: 400, overlay: 500, modal: 600, toast: 700, tooltip: 800,
};

// ════════════════════════════════════════════════════════════════════════════
// USAGE MAP — element → exactly which tokens to apply (the part Hamza needs)
// ════════════════════════════════════════════════════════════════════════════
export const usage = {
  // FEEDS -------------------------------------------------------------------
  'feed toggle Fan/Vibes/Xplorer — ACTIVE pill': {
    background: 'brand.gradientCss', text: 'onPrimary (white)', radius: 'pill',
    height: 38, shadow: 'shadow.button', icon: 'Ionicons (heart for Fan) white',
  },
  'feed toggle — INACTIVE': {
    background: 'transparent', text: 'color.*.onSurfaceVariant', icon: 'onSurfaceVariant',
  },
  'feed toggle container (segmented)': {
    background: 'color.*.surfaceContainerHigh', radius: 'pill', padding: 'spacing.xs(4)',
  },
  'suggestion card "Devenir fan" button': {
    background: 'brand.gradientCss', text: 'white', radius: 'pill', height: 38, shadow: 'shadow.button',
  },
  // BUTTONS -----------------------------------------------------------------
  'PRIMARY button (gradient / Devenir fan / Follow filled / Connecter)': {
    background: 'brand.gradientCss', text: 'white', weight: '600', radius: 'pill(999)',
    height: 'size.control.lg(52)', paddingX: 'spacing.xl(24)', shadow: 'shadow.button',
    a11y: 'see brand.gradientAA if white text must clear WCAG AA',
  },
  'SECONDARY button (Modifier / outline)': {
    background: 'transparent', border: '1px color.*.outline', text: 'color.*.onSurface',
    radius: 'radius.md(12)', height: 'size.control.lg(52)',
  },
  'GHOST button (tertiary)': { background: 'transparent', text: 'color.*.onSurface', radius: 'radius.md(12)' },
  // CARDS / LISTS -----------------------------------------------------------
  'content Card': {
    background: 'color.*.surfaceContainer', radius: 'radius.2xl(28)',
    border: 'none (default) OR 1px brand.mint @12% for grouped lists', shadow: 'shadow.card', padding: 'spacing.lg(16)',
  },
  'list row': {
    minHeight: 56, paddingY: 'spacing.md(12)', gap: 13,
    divider: '1px color.*.outline (between rows, none on last)',
    label: 'type.bodyMd onSurface', sublabel: 'type.labelSm onSurfaceVariant',
    chevron: '› Ionicons chevron-forward, onSurfaceVariant @55% (shown when navigational & no trailing)',
  },
  'list row leading icon container': {
    size: '34×34', radius: 'radius.sm-ish(11)',
    background: 'row hue @13% (mint OR per-item hue like settings: blue/purple/orange…)',
    glyph: 'Ionicons in the hue color, size 18–20',
  },
  'settings rows (per-section)': {
    note: 'each row icon uses its OWN hue tint (blue=profile, purple=appearance, orange=language, mint=notifications, green=privacy…), NOT all mint',
  },
  // INPUTS ------------------------------------------------------------------
  'text Input': {
    background: 'color.*.surface or surfaceContainer', border: '1px color.*.outline',
    radius: 'radius.md(12)', height: 'size.control.md(44)', leadingIcon: 'Ionicons onSurfaceVariant',
    placeholder: 'color.*.onSurfaceMuted', focus: 'border color.*.focusRing',
  },
  // PROFILE -----------------------------------------------------------------
  'profile header buttons (Modifier / Devenir fan)': {
    Modifier: 'SECONDARY outline', 'Devenir fan': 'PRIMARY gradient pill',
  },
  'profile tab bar (Posts/Peaks/Activities, Lifestyle/Channel)': {
    active: 'brand.mint text + mint underline/pill', inactive: 'onSurfaceVariant',
  },
  'avatar': { shape: 'ROUNDED SQUARE', radius: 'radius.md(12)', sizes: 'size.avatar.*', note: 'NEVER a circle (charter)' },
  'verified badge': { color: 'brand.mint', icon: 'Ionicons checkmark-circle' },
  // PILLS / STATUS ----------------------------------------------------------
  'status pill (Actif/En cours/Banni…)': {
    radius: 'pill', font: 'type.labelMd', background: 'semantic color @16%', text: 'matching semantic color',
    examples: 'ok=success, warn=warning, danger=danger',
  },
  'badge (PRO CREATOR · Premium)': { background: 'brand.mint @16%', text: 'brand.mint', radius: 'pill', font: 'type.labelSm uppercase' },
  // NAV ---------------------------------------------------------------------
  'bottom navigation': { height: 56, iconSize: 28, active: 'brand.mint', inactive: 'color.*.onSurfaceVariant' },
  'screen header (back + title)': { height: 56, back: 'Ionicons chevron-back onSurface', title: 'type.title' },
  'eyebrow / section title': { font: 'type.labelCaps', color: 'brand.mint (eyebrow) OR onSurfaceVariant (section)' },
  // TOGGLES -----------------------------------------------------------------
  'switch / toggle': {
    track: '42×24 pill', on: 'brand.mint + shadow.button', off: 'color.*.outline',
    knob: '20px white circle, shadow 0 2 4 rgba(0,0,0,.2)',
  },
  // HERO / EMPTY ------------------------------------------------------------
  'hero icon (status screens)': { size: '80×80', radius: 'radius.xl-2xl', background: 'brand.gradientCss', glyph: 'white Ionicon', shadow: 'shadow.feature' },
  'feature card (premium plan)': { border: '1.5px brand.mint @15%', radius: 'radius.xl(22)', shadow: 'shadow.feature' },
};

// ════════════════════════════════════════════════════════════════════════════
// COMPONENTS — EXACT dimensions per reusable block (extracted from the validated
// canonical maquettes: build_home_v2 / build_profiles_v5). All values in px.
// Avatars in the validated maquettes are circles (r999); the V2 charter prefers
// rounded squares (radius 12). ⚠️ reconcile per founder — values below mirror
// what the validated maquettes actually render.
// ════════════════════════════════════════════════════════════════════════════
export const components = {
  // HOME — suggestion creator card ("Devenir fan"). ⬅ the one to match exactly.
  suggestionCard: {
    width: 160, paddingV: 16, paddingH: 12, gap: 7,
    background: 'color.*.surfaceContainer', border: '1px color.*.outline', radius: 20,
    layout: 'column, center-aligned',
    avatar: { width: 56, height: 56, radius: 999 /* validated=circle; charter=12 */ },
    name: 'fontSize 13 / weight 800 / center',
    role: 'fontSize 11 / weight 500 / sub / center',
    fanButton: { width: '100%', paddingV: 8, radius: 999, background: 'brand.gradientCss', text: 'white 12.5/700', marginTop: 2 },
    rowGap: 10, rowPadding: '0 16 18', // the horizontal scroller around the cards
  },
  // HOME — peaks / live thumbnail (carousel)
  peakCard: { width: 132, aspectRatio: '3/4', radius: 20, gap: 11, rowPadding: '7 16 18',
    liveBadge: { top: 8, left: 8, dot: 5, font: 'uppercase' }, name: { bottom: 10, leftRight: 11 } },
  // HOME — post card
  postCard: { margin: '0 16 16', background: 'color.*.surfaceContainer', border: '1px color.*.outline',
    radius: 20, shadow: '0 4px 18px rgba(0,0,0,0.18)',
    header: { padding: '12 14 8', gap: 10, avatar: { width: 38, height: 38, radius: 999 }, name: '14/800' } },
  // PROFILE — cover + header
  profileCover: { width: '100%', aspectRatio: '2/1' },
  profileAvatar: { width: 84, height: 84, radius: 999 /* validated=circle; charter=12 */, border: '3px color.*.surface' },
  profileStats: { gap: 22, padding: '14 16 4', value: '15/800', label: '13/500' },
  profileConfigButton: { margin: '0 16 12', width: 'calc(100% - 32px)', height: 40,
    border: '1.5px brand.mint @22.5%', radius: 999, text: 'brand.mint, center' },
  // PROFILE — media card (channel / package / 1:1)
  mediaCard: { radius: 20, background: 'color.*.surfaceContainer', border: '1px color.*.outline',
    shadow: '0 4px 18px rgba(0,0,0,0.18)',
    hero: { width: '100%', aspectRatio: '16/9' },
    badge: { top: 10, left: 10, padding: '4 10', radius: 999, font: '10/800 uppercase', text: 'white' },
    body: { padding: 14, title: '15/800', sub: '12/500' },
    cta: { marginTop: 14, paddingV: 12, radius: 14, full: true },
  },
  // GENERIC ATOMS (from src/components/v2 — the code truth)
  button: { heights: { sm: 36, md: 44, lg: 52 }, radiusGradient: 999, radiusOther: 12, paddingX: { sm: 12, md: 16, lg: 24 }, textWeight: 600 },
  card: { radius: 28, padding: 16, background: 'color.*.surfaceContainer' }, // Card atom (note: maquettes use 18–20 on some lists)
  input: { height: 44, radius: 12, paddingX: 14, gap: 10 },
  listRow: { minHeight: 56, paddingV: 12, gap: 13, iconSquare: { side: 34, radius: 11, tintAlpha: 0.13 }, chevron: 'chevron-forward 18 / onSurfaceVariant @55%' },
  statusPill: { paddingV: 4, paddingH: 10, radius: 999, font: '11/700' },
  toggle: { track: { width: 42, height: 24, radius: 999 }, knob: { size: 20, radius: 999 } },
  bottomNav: { height: 56, iconSize: 28 },
  screenHeader: { height: 56, backIcon: 24, title: '16/700' },
  heroIcon: { size: 80, radius: 24, background: 'brand.gradientCss', shadow: 'shadow.feature' },
  featureCard: { radius: 22, border: '1.5px brand.mint @15%', shadow: 'shadow.feature', padding: 16 },
};

export default { brand, shadow, color, font, type, spacing, radius, size, icons, motion, zIndex, usage, components };
