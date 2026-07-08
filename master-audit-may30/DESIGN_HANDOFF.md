# Smuppy V2 — Design Handoff (pour implémentation)

> **116 écrans uniques · 230 PNGs device (393×852) · dark + light.** Maquettes HTML/CSS pixel-exactes, prêtes à traduire en React Native. Branche `design/creator-config-may28`.

### 📦 Le package (à lire dans cet ordre)
1. **`theme.ts`** — tokens prêts à coller (couleurs, typo, spacing, radius, useTheme). **Code ça en premier.**
2. **`COMPONENTS.md`** — composants canoniques réutilisables (BottomNav, CreatorCard, PeakLiveCard, PostCard, ProfileHeader…) à coder une fois.
3. **`FLOWS.md`** — navigation (quel écran → quel écran) pour chaque feature.
4. **`_figma-gallery.html`** — visualiser les 230 écrans · **`prototype_v5.html`** — naviguer.
5. **`_figma-device-import/*.png`** (réf visuelle) + **`maquettes/harmonized/{screen}/code.html`** (valeurs exactes).

---

## 1. Où est tout (3 façons d'y accéder)

| Accès | Quoi | Comment |
|-------|------|---------|
| **Repo (recommandé)** | PNGs + **code source HTML/CSS** + builders + gallery + prototype | `git checkout design/creator-config-may28` → tout est dans `docs/design/master-audit-may30/` |
| **Lien live** | Prototype cliquable + galerie scrollable | `https://<tunnel>.trycloudflare.com/prototype_v5.html` (tant que le Mac du founder tourne) |
| **Zip** | Bundle statique auto-contenu | `smuppy-ui.zip` (drag → Netlify Drop pour un lien permanent) |

**Dans `docs/design/master-audit-may30/` :**
- `_figma-device-import/*.png` — **230 PNGs** (réf visuelle, 393×852, nommés `{screen}_v2_{dark|light}.png`)
- `_figma-gallery.html` — galerie de tous les écrans (clic image → version scrollable live)
- `prototype_v5.html` — prototype navigable (picker par catégorie + dark/light)
- `scripts/builders/*.py` — générateurs (source de vérité du CSS exact)
- **Le HTML source de chaque écran** est servi/généré dans `maquettes/harmonized/{screen}/code.html` — **c'est là que Hamza lit les valeurs exactes** (couleurs, paddings, font-sizes, radius) à traduire en styles RN.

---

## 2. Design tokens (valeurs exactes — à mettre dans le thème RN)

```ts
// Couleurs
const colors = {
  // Brand — soft teal (PAS de néon, glows réduits)
  mint:      '#33A089',           // accent principal
  gradient:  ['#41AD96', '#2C95A0'], // boutons CTA (linear 135°)
  // Dark theme
  darkBg:    '#000000', darkCard: '#14141A', darkText: '#F1F4F6', darkSub: '#8B8B95',
  darkBorder:'rgba(255,255,255,0.06)', darkInputBg: 'rgba(255,255,255,0.04)',
  // Light theme
  lightBg:   '#F6F8FA', lightCard:'#FFFFFF', lightText:'#0F172A', lightSub:'#64748B',
  lightBorder:'#EEF1F4',
  // Status
  danger:'#FF4658', live:'#FF4658', calories:'#FF7A45', pace:'#11C6FF',
  peak:'#9966FF', warning:'#FFA63D',
};

// Typo : Plus Jakarta Sans (400/500/600/700/800/900). Grands chiffres = 900 + tabular-nums.
// Radius : cards 20px · pills/CTA 999px ou 16px · tiles image 14-16px
// Bottom nav : canonical (icônes home/peaks/+/msg/profile · barre verte sous l'actif)
// Logo : wordmark vert (dark) / noir (light) · icône idem
// Texte fan : "Become a fan" / "Devenir fan" (jamais Follow/Suivre) · stat "Fans"
```

**Icons** : Ionicons (déjà dans le projet via `@expo/vector-icons` / `ion-icon`). Les noms utilisés dans les maquettes = noms Ionicons directs.

---

## 3. Inventaire des écrans par feature (230 PNGs)

| Feature | Écrans | Notes |
|---------|--------|-------|
| **Run** (Personal Activity) | 15 | permission · gps_denied · **start (Départ)** · countdown · gps_search · tracking · paused · stop_confirm · share · published · discard · history (Mes runs) · records · detail (splits) · empty |
| **Profils v5** | 15 | personal/creator/business × owner/visitor/fan/private + états channel/packs/services (tabs interactifs) |
| **Feeds** | 6 | home_feed (Fan multi-média) · vibes (masonry) · xplorer (map+filtres) · search · peaks_live · live_preview |
| **Creator monétisation** | 13 | channel/1:1/packages setup+view+owner+états |
| **Booking / Sessions** | 14 | p2_creator_booking · business_booking · my_sessions · session/live ended · private_call · payment |
| **Settings / Messages** | 19 | p1_* |
| **Auth** | 13 | welcome/login/signup/forgot/verify/MFA |
| **Onboarding** | 12 | account_type/tell_us/interests/guidelines/success… |
| **Création** | 5 | post menu/gallery/details/success · peak camera |

---

## 4. Flow Run (exemple de parcours complet — tous boutons câblés)

```
Map → bouton Run → Permission → DÉPART → Décompte 3·2·1 → Tracking
  Tracking: [Pause]→Auto-pause→[Reprendre] · [Stop]→Stop confirm
  Stop confirm: [Terminer]→Share
  Share: [Enregistrer & partager]→"Run partagé" · [Enregistrer]→toast · [Abandonner]→modal suppression
  → Mes runs (ring + historique) → clic run → Détail (splits)
```

*(Les flows des autres features sont navigables dans `prototype_v5.html`.)*

---

## 5. Comment implémenter (méthode recommandée)

1. **Ouvre le PNG** de l'écran (réf visuelle) + le **`code.html`** correspondant (valeurs exactes).
2. **Copie les valeurs CSS** → styles RN : `background`, `border-radius`, `padding`, `font-size`, `font-weight`, `color`, `gap`. Les maquettes sont à l'échelle 1:1 (393pt de large = largeur iPhone).
3. **Réutilise les composants canoniques** : la **bottom nav** (`canonical_bnav` → 1 composant RN partagé), les **cards créateur** (160px), les **cards peak/live** (132px, 3:4), le **logo** (vert/noir selon thème). Ne pas les ré-implémenter par écran.
4. **Tokens d'abord** : crée le thème (colors/spacing/radius ci-dessus) avant les écrans → cohérence garantie.
5. **Dark + light** : chaque écran a ses 2 PNGs. Le thème pilote tout.
6. **Données réelles** : les écrans existants en code (`src/screens/activities/PersonalRunTrackingScreen.tsx`, etc.) ont déjà la logique — c'est le **design** qui change, pas forcément la logique.

---

## 6. Pour démarrer (côté founder)

- **Le plus simple** : `git push` la branche `design/creator-config-may28` → Hamza fait `git pull` → il a TOUT (PNGs + HTML + builders).
- **Ou** : envoie-lui le lien tunnel (galerie + prototype) pour visualiser en attendant.
- **Ou** : `smuppy-ui.zip` → Netlify Drop → lien permanent à partager.

> ⚠️ Le design n'est pas encore mergé sur `main` — c'est une branche de design. Hamza implémente en lisant les maquettes ; le code RN final part d'une nouvelle branche feature.
