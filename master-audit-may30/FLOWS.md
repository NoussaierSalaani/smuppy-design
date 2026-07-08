# Smuppy V2 — Flows de navigation (quel écran → quel écran)

> Pour câbler la navigation. Chaque bouton a une destination (zéro cul-de-sac). Navigue-les en live dans `prototype_v5.html`.

---

## 🏃 RUN (Personal Activity)
```
Map → bouton "Run" → run_permission ──Autoriser──┐  (refusé → run_gps_denied → fallback)
run_start (DÉPART) ──bouton DÉPART──▶ run_countdown (3·2·1) ──▶ run_gps_search ──▶ run_tracking
  run_tracking : [Pause]→run_paused→[Reprendre] · [Stop]→run_stop_confirm
  run_stop_confirm : [Terminer]→run_share · [Reprendre]→run_tracking
  run_share : [Enregistrer & partager]→run_published · [Enregistrer]→toast→run_history · [Abandonner]→run_discard_confirm
  run_published : [Voir mon post]→post · [Voir mes runs]→run_history
run_history (Mes runs) : tabs [Runs|Records] · clic run→run_detail (splits) · vide→run_empty
```
Background : actif écran verrouillé (perm "Always") + musique OK. Auto-pause <0.5m/s>10s. Auto-stop 15 min (sauve + push).

## 👤 PROFIL (tabs interactifs)
```
profile_{type}_{view} : tap main pill (Lifestyle ↔ Channel/Services) → swap sous-tabs + contenu
  creator Channel : sous-tabs [Channel|1:1|Packs] → offres → CTA :
    Channel "S'abonner" → creator_channel_view · 1:1 "Réserver" → p2_creator_booking · Packs "Acheter" → creator_packages_view
  business Services : [Booking|Programme] → Booking "Réserver" → p2_business_booking · Programme = tableau accordéon
  owner : bouton "Configurer" → creator_*_setup
  visitor non-fan → "Become a fan" · fan → contenu débloqué · privé → gate 🔒
```

## 📅 BOOKING
```
Creator 1:1 : profil tab 1:1 (info+CTA) → p2_creator_booking (durée→date→créneau→paiement) → p2_session_payment → p2_session_ended (+ CTA Smups)
Business : profil tab Services → p2_business_booking (Service→Date→Créneau→Confirmer)
```

## 🔴 LIVE → PAYWALL
```
peaks_live_live (grille de lives) → clic card → live_preview (aperçu gratuit 0:05) → paywall "S'abonner 9,99€" → creator_channel_view
Fin de live → p2_live_ended (récap + CTA "Envoyer des Smups" + s'abonner)
```

## ✍️ CRÉATION
```
bnav (+) → post_create_menu [Post|Peak|Go Live|Activity]
  Post → post_gallery → post_details → post_success (carte inclinée + vignette)
  Peak → peak_camera
  Go Live → p2_go_live → p2_live_streaming
```

## 🚀 ONBOARDING
```
onb_account_type → (personal: onb_tell_us · creator: onb_creator_info → onb_creator_optional · business: onb_business_category → onb_business_info)
  → onb_interests/profession/expertise → onb_guidelines (accepter) → onb_find_friends → onb_success (auto-redirect, pas de bouton)
```

## 🔐 AUTH
```
auth_welcome → [Créer un compte]→auth_signup · [Se connecter]→auth_login
  signup → auth_verify_code → onboarding · login → home · "mot de passe oublié" → auth_forgot
```

## 🔔 NOTIFICATIONS
```
top bar notif → p1_notifications : avatars de profil (empilés si multi-likers) + badge type · tabs [Tous|Likes|Fans|Mentions]
```
