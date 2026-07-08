# Smuppy V2 — Guide d'intégration UI (pour Hamza)

> But : reproduire **à l'identique** le design V2 validé. Tout ce qu'il faut est ici.

## 1. La source de vérité unique = `theme.js`

`docs/v2-implementation/theme.js` (aussi à la racine du repo) contient **toutes** les
variables + **où** les appliquer :

- `color.light.*` / `color.dark.*` — surfaces, textes, bordures (adaptatif clair/sombre)
- `brand.*` — mint **#33A089**, gradient bouton **#41AD96 → #2C95A0**, glows subtils
- `type.*` — 10 presets typo (Plus Jakarta Sans, tailles/poids/interlignes)
- `spacing.*` (grille 4pt) · `radius.*` (avec le composant qui l'utilise) · `size.*` (hauteurs, icônes, avatars)
- `shadow.*` — glows **subtils** (rgba(51,160,137, 0.05→0.18)) — JAMAIS de halo brillant
- `motion.*` · `zIndex.*`
- `usage` — **carte élément → tokens** (toggle feed, Devenir fan, card, input, row, avatar…)
- `components` — **dimensions exactes px** de chaque bloc (suggestionCard 160px, peakCard 132px, profileAvatar 84px, mediaCard…)

**Règle : 0 valeur en dur.** Toute couleur/taille/rayon vient de `theme.js`.

## 2. Règles de charte (non négociables)

- **Police** = Plus Jakarta Sans uniquement (400/500/600/700/800). Pas d'italique.
- **Avatars** = carrés arrondis (radius 12). *(les maquettes validées montrent des cercles sur certains écrans → à trancher avec le fondateur ; `theme.js` note les deux.)*
- **Clair + Sombre** systématiquement.
- **Icônes** = Ionicons (`@expo/vector-icons`), `<Ionicons name="…" />`.
- Boutons pleins = **gradient en pilule (radius 999)**, texte blanc, poids 600, glow subtil.
- Boutons secondaires = **outline radius 12**.

## 3. Workflow par écran

1. Ouvre `screens/<NomEcran>/` → tu as côte à côte :
   - `maquette/` — le PNG de référence (clair + sombre) = le rendu cible exact
   - `code/<NomEcran>.tsx` + `__fixtures__/` (contrat de props) + test
   - `README.md` — namespace i18n, statut maquette, où est le contrat de props
2. Reproduis le code en lisant **uniquement** `theme.js` pour les styles.
3. Compare ton rendu au PNG `maquette/` → doit être identique (couleurs, tailles, rayons, glow).
4. Câble les données : map ton contrôleur V1 sur la forme du `fixtures.ts`.

## 4. Vérifier « identique »

- ✅ couleurs = tokens `theme.js` (aucune valeur en dur)
- ✅ dimensions = `components.*` (ex. carte suggestion = 160px / padding 16×12 / radius 20)
- ✅ gradient bouton = #41AD96→#2C95A0 · mint accent = #33A089 · glow subtil
- ✅ police Plus Jakarta Sans · icônes Ionicons
- ✅ clair ET sombre rendus comme les 2 PNG

## 5. Où est quoi

| Quoi | Où |
|---|---|
| Tokens + usage + dimensions | `theme.js` (racine + `docs/v2-implementation/`) |
| 149 écrans (maquette × code) | `screens/<Nom>/` |
| Atoms partagés | `atoms/<Nom>/` |
| Toutes les maquettes (réf. visuelle) | `_all-maquettes/` |
| Guide de câblage détaillé | `docs/v2-implementation/HANDOVER_HAMZA.md` |
| Index écran × maquette | `SCREEN_INDEX.md` |

## 6. ⚠️ Accessibilité (à savoir)

Le gradient validé `#41AD96→#2C95A0` avec texte blanc ≈ 2,6–3,3:1 (sous le seuil WCAG AA
4,5). `theme.js` expose `brand.gradientAA` (#1A7D68→#157082, blanc = 5:1) comme alternative
si on veut la conformité AA sur les boutons texte. Décision fondateur à confirmer.
