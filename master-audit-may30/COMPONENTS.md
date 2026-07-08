# Smuppy V2 — Composants canoniques (à coder EN PREMIER, 1 fois, partagés)

> Ces composants reviennent sur des dizaines d'écrans. Code-les une seule fois → les écrans héritent. Ne **jamais** les ré-implémenter par écran (c'est la cause #1 de dérive visuelle).

---

## 1. BottomNav (canonique) — sur tous les écrans "main"
- 5 slots : **Home** · **Peaks** · **Create (+)** · **Messages** · **Profile (avatar)**.
- Icônes custom SVG (Home = bouclier, Peaks = caméra+play, Msg = bulle) — **outline mint quand actif** (PAS de remplissage plein).
- Slot actif : couleur mint `#33A089` + **barre verte** (24×3px, radius 999) sous l'icône + glow doux.
- Create (+) : pill centrale (bord mint 1.5px, fond card, halo doux réduit).
- Profile : avatar carré 12px-radius, contour mint 2px quand actif + barre verte.
- Props : `active: 'home'|'peaks'|'create'|'msg'|'profile'`.
- ⚠️ Source de vérité : `canonical_bnav.py` (4 paths SVG exacts). Voir aussi `home_feed_v2` pour le rendu.

## 2. CreatorCard (Suggestions / Suggested creators) — DIMENSIONS IDENTIQUES partout
- `width: 160`, `padding: 16/12`, `radius: 20`, bg card + bordure.
- Avatar rond **56px** centré · nom (800, 13px) + badge vérifié · rôle (11px, sub) · bouton pleine largeur **« Devenir fan »** (gradient, 12.5px/700).
- Utilisé en : home "Suggestions pour toi" (scroll horizontal) ET search "Suggested creators" (grille 2 col de 160px). **Même composant, mêmes pixels.**

## 3. PeakLiveCard (thumbnails Peaks/Live) — IDENTIQUE partout
- `width: 132` (carousel) / `1fr` (grille 2 col), **aspect 3/4**, `radius: 20`.
- Image + scrim bas + nom (12px, blanc, bottom-left).
- Badge **LIVE** rouge (top) + **contour rouge clignotant** (`@keyframes`, box-shadow pulse) si live en cours.
- ⚠️ Le conteneur scroll a besoin de `padding vertical` sinon l'anneau rouge est clippé.

## 4. Logo (wordmark + icône)
- **VERT (gradient) en dark · NOIR en light** (variante selon thème, jamais figé).
- Centré dans la top bar des écrans main (notif à gauche, logo centre, search à droite).
- SVG réels : `smuppy_icon` / `smuppy_text` (74×74 / 215×46 viewBox).

## 5. Boutons
- **Primaire** : full-width 54px, gradient `#41AD96→#2C95A0` (135°), texte blanc 800, ombre douce. Radius 16.
- **Ghost** : transparent, texte `sub`, 48px.
- **Danger** : `#FF4658` (stop, supprimer).
- **Pills segmentées** (tabs, privacy) : conteneur radius 999 + fond inputBg ; actif = card + texte mint + ring mint.

## 6. PostCard (feed) — logique média multi-layout
- Header : avatar 38 + nom+vérifié + temps + ⋯ · **légende** texte · média (layout auto ci-dessous) · actions cœur+compteur / partage / save. **PAS de commentaires** (contrat Smuppy).
- **Logique média** (fonction pure sur `(count, types)`) :
  - 1 photo → `aspect 4/3`
  - 1 vidéo → `aspect 16/9` + bouton play
  - 2 photos → **côte à côte** (grid 2 col)
  - 3+ ou mixte → **carrousel swipable** (scroll-snap) + dots + compteur "1/N"
- Média inset (margin 14px) + radius 14.

## 7. ProfileHeader (Instagram-style) — tous types de compte
- Cover + **avatar à GAUCHE** (overlap) + actions à droite (visitor: Follow/msg · owner: Modifier/share).
- Name+vérifié + rôle/bio (left-aligned) · stats inline (**Fans** · Posts · Peaks).
- Tabs selon type : personal (Posts/Peaks/Activities/Saved-owner) · creator (Lifestyle/Channel 2 niveaux) · business (Lifestyle/Services). **Tabs interactifs** (JS swap → en RN : state).
- États : owner / visitor / **fan** (Fan✓ + badge + débloqué) / **privé** (gate 🔒).

## 8. Cards génériques
- Card contenu : bg card, bordure 1px hairline, **radius 20**, padding 14-16.
- OfferCard (monétisation) : hero image + badge + titre + prix + perks + CTA (lien vers écran validé).
- StatTile (run/wallet) : icône + grand chiffre (800, tabular-nums) + label (10px uppercase).
- ActivityRing (run) : SVG cercle progress, gradient, gros chiffre centre (Apple-Watch style).

---

### Ordre de build recommandé
1. `theme.ts` (tokens) → 2. BottomNav + Logo + Boutons → 3. Card primitives (Card, StatTile, pills) →
4. CreatorCard + PeakLiveCard + PostCard → 5. ProfileHeader → 6. les écrans (qui composent ces blocs).
