/**
 * Smuppy V2 — Design tokens (prêt à coller / adapter).
 * Source de vérité extraite des maquettes V2 (docs/design/master-audit-may30).
 * Usage RN : const t = useTheme(); t.bg, t.text, spacing.md, radius.card, font.h1 …
 *
 * Règles d'or :
 *  - Accent = soft teal #33A089 (PAS de néon, glows réduits ÷2).
 *  - Gradient CTA = linear 135° #41AD96 → #2C95A0.
 *  - Grands chiffres : weight 900 + fontVariant tabular-nums.
 *  - Logo : wordmark/icône VERT en dark, NOIR en light.
 *  - Texte fan : "Become a fan" / "Devenir fan" (jamais Follow/Suivre) · stat "Fans".
 */

// ─────────────────────────────────────────── COULEURS
export const palette = {
  // Brand
  mint:        '#33A089',   // accent principal (texte/icônes actifs, anneaux)
  mintHi:      '#41AD96',   // gradient start
  mintDeep:    '#2C95A0',   // gradient end
  gradient:    ['#41AD96', '#2C95A0'] as const, // CTA — angle 135°
  // Status
  danger:      '#FF4658',   // stop, supprimer, live
  live:        '#FF4658',
  calories:    '#FF7A45',
  pace:        '#11C6FF',
  peak:        '#9966FF',
  warning:     '#FFA63D',
  white:       '#FFFFFF',
} as const;

export const dark = {
  bg:          '#000000',
  card:        '#14141A',
  cardInner:   '#0F0F14',
  text:        '#F1F4F6',
  sub:         '#8B8B95',
  section:     '#6B6B75',
  border:      'rgba(255,255,255,0.06)',
  inputBg:     'rgba(255,255,255,0.04)',
  inputBorder: 'rgba(255,255,255,0.10)',
  dimShadow:   0.5,
  mapBg:       '#0d1b1a',   // fond carte teinté
  logoVariant: 'green' as const, // logo vert en dark
} as const;

export const light = {
  bg:          '#F6F8FA',
  card:        '#FFFFFF',
  cardInner:   '#FAFBFC',
  text:        '#0F172A',
  sub:         '#64748B',
  section:     '#94A3B8',
  border:      '#EEF1F4',
  inputBg:     '#FFFFFF',
  inputBorder: '#E5E9EB',
  dimShadow:   0.06,
  mapBg:       '#e8f3f0',
  logoVariant: 'black' as const, // logo noir en light
} as const;

export type ThemeColors = typeof dark;

// ─────────────────────────────────────────── TYPO  (Plus Jakarta Sans)
export const fontFamily = {
  // brancher via expo-font : PlusJakartaSans_400Regular … _900Black
  regular: 'PlusJakartaSans_400Regular',
  medium:  'PlusJakartaSans_500Medium',
  semi:    'PlusJakartaSans_600SemiBold',
  bold:    'PlusJakartaSans_700Bold',
  extra:   'PlusJakartaSans_800ExtraBold',
  black:   'PlusJakartaSans_900Black',
} as const;

/** Échelle typographique (size / weight / letterSpacing). Chiffres = tabular-nums. */
export const font = {
  hero:    { fontSize: 62, fontFamily: fontFamily.black, letterSpacing: -1.5 }, // chrono run
  h1:      { fontSize: 25, fontFamily: fontFamily.black, letterSpacing: -0.5 },
  h2:      { fontSize: 19, fontFamily: fontFamily.extra, letterSpacing: -0.2 },
  title:   { fontSize: 15, fontFamily: fontFamily.extra },
  body:    { fontSize: 13.5, fontFamily: fontFamily.medium, lineHeight: 21 },
  sub:     { fontSize: 12, fontFamily: fontFamily.medium },
  label:   { fontSize: 10, fontFamily: fontFamily.extra, letterSpacing: 1, textTransform: 'uppercase' as const },
  statNum: { fontSize: 19, fontFamily: fontFamily.extra, letterSpacing: -0.4 }, // + fontVariant: ['tabular-nums']
} as const;

// ─────────────────────────────────────────── ESPACEMENT / RAYONS
export const spacing = { xs: 4, sm: 8, md: 12, lg: 16, xl: 22, xxl: 28 } as const;

export const radius = {
  pill: 999,
  card: 20,     // cards de contenu
  tile: 16,     // tuiles image
  input: 14,
  cta: 16,      // boutons primaires
  panel: 28,    // panneaux flottants (tracking run, sheets)
} as const;

// ─────────────────────────────────────────── COMPOSANTS CANONIQUES (specs figées)
export const tokens = {
  // Bottom nav canonique (1 composant partagé — NE PAS ré-implémenter par écran)
  bnav: { height: 64, iconSize: 26, createSize: 48, activeBar: { w: 24, h: 3, color: palette.mint } },
  // Card créateur (home Suggestions = search Suggested creators) — IDENTIQUE partout
  creatorCard: { width: 160, avatar: 56, padding: [16, 12], radius: radius.card },
  // Card peak/live (carousels + grilles) — IDENTIQUE partout
  peakCard: { width: 132, aspectRatio: 3 / 4, radius: radius.card, liveBorder: palette.live }, // live = contour rouge pulsant
  // Boutons
  ctaPrimary: { height: 54, radius: radius.cta, gradient: palette.gradient },  // white text, weight 800
  ctaGhost:   { height: 48, color: 'sub' },
  // Glows réduits (÷2 vs origine) — ne pas re-saturer
  glow: { soft: 'rgba(51,160,137,0.15)' },
} as const;

// ─────────────────────────────────────────── HOOK D'USAGE (exemple)
import { useColorScheme } from 'react-native';
export function useTheme() {
  const scheme = useColorScheme();
  const c = scheme === 'light' ? light : dark;
  return { ...c, palette, font, spacing, radius, tokens, fontFamily, scheme };
}

/**
 * Exemple :
 *   const t = useTheme();
 *   <View style={{ backgroundColor: t.card, borderRadius: t.radius.card, padding: t.spacing.lg, borderWidth: 1, borderColor: t.border }}>
 *     <Text style={{ ...t.font.h2, color: t.text }}>Mes runs</Text>
 *   </View>
 *
 * CTA dégradé : <LinearGradient colors={t.palette.gradient} start={{x:0,y:0}} end={{x:1,y:1}} style={{ height: t.tokens.ctaPrimary.height, borderRadius: t.radius.cta }} />
 */
