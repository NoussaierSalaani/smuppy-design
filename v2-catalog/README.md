# Catalogue V2 — inventaire écrans (sauvegardé 2026-06-18)

Source: repo handoff `smuppy-v2-ui` (cloné dans `/tmp/smuppy-v2-ui`).

## Données fiables (`inventory.json`)
149 écrans. Champs par écran: `name`, `code` (tous=true), `inapp` (dans `src/components/v2/`), `wired` (rendu par un écran `src/screens/`), `maq` (maquette PNG: yes/dsfill), chemins PNG.

- **27 live** (code RN dans l'app + branché à un écran)
- **5** dans l'app, non branchés (PostCompose/PostCreateMenu/PostSuccess/ProfileShell/VideoRecorder)
- **117** repo only (code RN, pas encore dans l'app)
- **29** DS-fill (pas de maquette PNG, code seulement)

## ⚠️ Pollution maquettes repo
94 dossiers `maquette/` propres (≤2 PNG), **26 pollués** (PNG mélangés → ne pas se fier au 1er PNG), 29 sans maquette.
Pollués: AuthPasswordSuccess, BookingHistory, BusinessBookingSuccess/Booking, ChannelOwner, CreateGroupChat, CreatorChannelSetup, CreatorPackagesSetup, HomeFeed, MyRatingsSettings, NotificationSettings, Notifications, OnboardingBusinessInfo, OnboardingCreatorInfo, **OnboardingSuccess(10)**, PackagesOwner, PeakCamera, PostDetail, PostGallery, PostSuccess, PrivacySettings, PrivateCall, Search, SecuritySettings, SmupWallet, VibesFeed.

## Pour re-servir les galeries
Les HTML référencent les PNG via `http://127.0.0.1:8772/screens/...` servis depuis `/tmp/smuppy-v2-ui`:
`cd /tmp/smuppy-v2-ui && python3 -m http.server 8772 --bind 127.0.0.1`
puis ouvrir `GALERIE_V2.html` (visuel) ou `CATALOGUE_V2.html` (table). (Re-cloner smuppy-v2-ui dans /tmp si absent.)

## Vérifié chirurgicalement
Fin d'onboarding = `SuccessScreen.tsx` → `OnboardingSuccessView` → "Bienvenue {{name}}, ton profil est prêt, découvre la tribu" = CORRECT. La confusion venait des vignettes du catalogue (pollution), pas du câblage.
