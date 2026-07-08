"""Smuppy V2 — P2 Payments + Sessions + Business + Live canonical maquettes.
~11 screens × 2 themes = 22 HTML maquettes.
"""

import json, sys
from pathlib import Path

sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from build_auth_v2 import (
    MINT, MINT_HI, MINT_DEEP, DANGER,
    theme, smuppy_icon, smuppy_text, smuppy_full,
    primary_cta, ghost_cta, input_field, back_button, close_button,
    build as auth_build_fn,
)
from build_p1_v2 import settings_topbar, settings_row, toggle_on, section_title, card_block, _P1_CSS

OUT_DIR = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')


# ─── PAYMENTS ──────────────────────────────────────────────


def screen_creator_wallet(th: dict) -> str:
    txns = [
        ('star', MINT, 'Léa Martin · Abonnement chaîne', '+9,99 €', '+6,99 €', '−30%'),
        ('person', '#11C6FF', 'Emma Chen · Session 1:1', '+45 €', '+31,50 €', '−30%'),
        ('cube', '#9966FF', 'Marc Dubois · Pack Transformation', '+269 €', '+188,30 €', '−30%'),
        ('cash', '#FFA63D', 'Thomas R. · 50 Smups 👊', '+4,99 €', '+3,49 €', '−30%'),
    ]
    rows = ''
    for icon, hue, label, gross, net, fee in txns:
        rows += f'''<div class="p2-txn">
  <span class="p1-row-ic" style="background:{hue}14;color:{hue}">
    <ion-icon name="{icon}" style="font-size:18px;color:{hue}"></ion-icon>
  </span>
  <div class="p2-txn-text">
    <div class="p2-txn-lbl">{label}</div>
    <div class="p2-txn-meta">Gross {gross} · fee {fee}</div>
  </div>
  <div class="p2-txn-amount">{net}</div>
</div>'''
    return f'''{settings_topbar('Wallet Créateur')}
<main class="p1-main">
  <div class="p2-wallet-hero">
    <div class="p2-wallet-label">Solde disponible</div>
    <div class="p2-wallet-amount">2 847,50 €</div>
    <div class="p2-wallet-row">
      <div class="p2-wallet-stat">
        <span class="p2-wallet-stat-num">+284 €</span>
        <span class="p2-wallet-stat-lbl">Ce mois</span>
      </div>
      <div class="p2-wallet-divider"></div>
      <div class="p2-wallet-stat">
        <span class="p2-wallet-stat-num">12 384 €</span>
        <span class="p2-wallet-stat-lbl">Total gagné</span>
      </div>
    </div>
    <button class="p2-wallet-cashout">
      <ion-icon name="arrow-down-circle" style="font-size:18px;color:#fff;vertical-align:middle"></ion-icon>
      Retirer mes gains
    </button>
  </div>

  <div class="p2-tabs">
    <span class="p2-tab p2-tab-on">Transactions</span>
    <span class="p2-tab">Analytics</span>
    <span class="p2-tab">Tier</span>
  </div>

  <h3 class="p1-sec-title">Tier · Diamond 💎</h3>
  <div class="p2-tier">
    <div class="p2-tier-bar"><div class="p2-tier-fill" style="width:78%"></div></div>
    <div class="p2-tier-text">
      <span><b style="color:var(--mint)">8.4K</b> fans · <b>76%</b> revenue share</span>
      <span class="p2-tier-next">2.6K → Black tier (80%)</span>
    </div>
  </div>

  <h3 class="p1-sec-title">Dernières transactions</h3>
  {rows}

  <button class="p2-view-all">Voir tout l&rsquo;historique</button>
</main>'''


def screen_smup_wallet(th: dict) -> str:
    txns = [
        ('add-circle', MINT, 'Achat · 100 Smups', '+100', '4,99 €', 'today'),
        ('arrow-up-circle', '#FFA63D', 'Envoyé à Sara Khan', '−50', '', 'today'),
        ('arrow-down-circle', '#11C6FF', 'Reçu de Marc Dubois', '+25', '', 'yesterday'),
        ('add-circle', MINT, 'Achat · 50 Smups', '+50', '2,49 €', 'yesterday'),
    ]
    rows = ''
    for icon, hue, label, count, price, _date in txns:
        rows += f'''<div class="p2-txn">
  <span class="p1-row-ic" style="background:{hue}14;color:{hue}">
    <ion-icon name="{icon}" style="font-size:18px;color:{hue}"></ion-icon>
  </span>
  <div class="p2-txn-text">
    <div class="p2-txn-lbl">{label}</div>
    {f'<div class="p2-txn-meta">{price}</div>' if price else ''}
  </div>
  <div class="p2-smup-count">{count} 👊</div>
</div>'''
    return f'''{settings_topbar('Wallet Smups')}
<main class="p1-main">
  <div class="p2-smup-hero">
    <div class="p2-smup-icon">👊</div>
    <div class="p2-smup-amount">412</div>
    <div class="p2-smup-lbl">Smups disponibles</div>
    <div class="p2-smup-equiv">≈ 20,55 € en valeur d&rsquo;envoi</div>
  </div>

  <div class="p2-smup-actions">
    <button class="p2-smup-btn p2-smup-btn-primary">
      <ion-icon name="add" style="font-size:18px;color:#fff;vertical-align:middle"></ion-icon>
      Acheter
    </button>
    <button class="p2-smup-btn">
      <ion-icon name="arrow-up-circle" style="font-size:18px;color:var(--mint);vertical-align:middle"></ion-icon>
      Envoyer
    </button>
  </div>

  <div class="p2-tabs">
    <span class="p2-tab p2-tab-on">Tous · 24</span>
    <span class="p2-tab">Achetés · 8</span>
    <span class="p2-tab">Envoyés · 12</span>
    <span class="p2-tab">Reçus · 4</span>
  </div>

  <h3 class="p1-sec-title">Historique</h3>
  {rows}
</main>'''


def screen_platform_subscription(th: dict) -> str:
    return f'''{settings_topbar('Smuppy Premium')}
<main class="p1-main">
  <div class="p1-pro-hero">
    {smuppy_icon(80, 'gradient')}
    <h1 class="p1-pro-title">Smuppy Premium</h1>
    <p class="p1-pro-sub">Accède à tout · sans pub · sans limite</p>
  </div>

  <div class="p1-plans">
    <div class="p1-plan p1-plan-active">
      <div class="p1-plan-header"><span class="p1-plan-badge">−40% · MEILLEUR DEAL</span></div>
      <div class="p1-plan-name">Lifetime</div>
      <div class="p1-plan-price">199 €<span> 1×</span></div>
      <div class="p1-plan-equiv">À vie · 0 abonnement</div>
    </div>
    <div class="p1-plan">
      <div class="p1-plan-name">Annuel</div>
      <div class="p1-plan-price">79 €<span> / an</span></div>
      <div class="p1-plan-equiv">6,58 €/mois</div>
    </div>
  </div>

  <h3 class="p1-sec-title">Avantages Premium</h3>
  {card_block(
    settings_row('infinite-outline', MINT, 'Posts &amp; peaks illimités', sub='Aucune limite quotidienne') +
    settings_row('eye-off-outline', '#11C6FF', 'Aucune publicité', sub='Expérience 100% clean') +
    settings_row('shield-checkmark-outline', '#9966FF', 'Badge vérifié', sub='Crédibilité boost dans le feed') +
    settings_row('color-palette-outline', '#26C1A4', 'Thèmes premium', sub='6 styles exclusifs') +
    settings_row('download-outline', '#FFA63D', 'Téléchargement HD', sub='Sauvegarde tes peaks favoris') +
    settings_row('headset-outline', '#E63946', 'Support prioritaire', sub='Réponse sous 4h')
  )}

  <div class="p1-form">
    {primary_cta("Essayer 7 jours gratuits")}
    <p class="p1-trial-note">Annulable à tout moment · pas de prélèvement avant J+7</p>
  </div>
</main>'''


def screen_identity_verification(th: dict) -> str:
    return f'''{settings_topbar('Vérification d&rsquo;identité')}
<main class="p1-main">
  <p class="p1-sec-desc">Requis pour recevoir tes paiements (KYC). Tes données sont chiffrées et conservées par Stripe Identity.</p>

  <div class="p2-kyc-progress">
    <div class="p2-kyc-step p2-kyc-step-done">
      <span class="p2-kyc-num"><ion-icon name="checkmark" style="font-size:14px;color:#fff"></ion-icon></span>
      Type de pièce
    </div>
    <div class="p2-kyc-step p2-kyc-step-on">
      <span class="p2-kyc-num">2</span>
      Photo recto
    </div>
    <div class="p2-kyc-step">
      <span class="p2-kyc-num">3</span>
      Photo verso
    </div>
    <div class="p2-kyc-step">
      <span class="p2-kyc-num">4</span>
      Selfie liveness
    </div>
  </div>

  <h3 class="p1-sec-title">Type de document</h3>
  <div class="p2-kyc-cards">
    <button class="p2-kyc-card p2-kyc-card-on">
      <ion-icon name="card-outline" style="font-size:28px;color:var(--mint)"></ion-icon>
      <span class="p2-kyc-card-title">Carte d&rsquo;identité</span>
      <span class="p2-kyc-card-sub">Recommandé</span>
    </button>
    <button class="p2-kyc-card">
      <ion-icon name="book-outline" style="font-size:28px;color:#11C6FF"></ion-icon>
      <span class="p2-kyc-card-title">Passeport</span>
    </button>
    <button class="p2-kyc-card">
      <ion-icon name="car-outline" style="font-size:28px;color:#9966FF"></ion-icon>
      <span class="p2-kyc-card-title">Permis</span>
    </button>
  </div>

  <div class="p2-kyc-photo">
    <div class="p2-kyc-photo-frame">
      <ion-icon name="camera" style="font-size:38px;color:var(--mint)"></ion-icon>
      <span class="p2-kyc-photo-lbl">Place ta pièce dans le cadre</span>
    </div>
  </div>

  <div class="p2-kyc-info">
    <ion-icon name="lock-closed" style="font-size:16px;color:var(--mint);flex-shrink:0;margin-top:1px"></ion-icon>
    <div>
      <div class="p2-kyc-info-title">Tes données sont sécurisées</div>
      <div class="p2-kyc-info-sub">Stripe Identity chiffre + supprime les images après vérification. Conformité RGPD + PCI-DSS.</div>
    </div>
  </div>

  <div class="p1-form">{primary_cta("Prendre la photo recto")}</div>
</main>'''


# ─── SESSIONS FAN-SIDE ─────────────────────────────────────


def screen_my_sessions(th: dict) -> str:
    upcoming = [
        ('Sara Khan', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80',
         'Yoga vinyasa flow', 'Demain · 16h00 · 30 min', 'confirmed', 'Rejoindre dans 21h', True),
        ('Marc Dubois', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&q=80',
         'Coaching nutrition', 'Jeu. 5 juin · 14h · 60 min', 'pending', '', False),
    ]
    past = [
        ('Coach Mike', 'https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=120&h=120&fit=crop&q=80',
         'Course longue', '28 mai · Terminée · 45 min', 'completed', '★★★★☆ noté', False),
    ]
    def row(s):
        n, av, title, sub, status, action, joinable = s
        status_color = {'confirmed': MINT, 'pending': '#FFA63D', 'completed': '#64748B'}[status]
        status_label = {'confirmed': 'Confirmé', 'pending': 'En attente', 'completed': 'Terminé'}[status]
        action_html = ''
        if joinable:
            action_html = '<button class="p2-sess-join">Rejoindre</button>'
        elif status == 'completed':
            action_html = f'<div class="p2-sess-rating">{action}</div>'
        return f'''<div class="p2-sess-row">
  <img src="{av}" alt="" class="p2-sess-avatar"/>
  <div class="p2-sess-text">
    <div class="p2-sess-name">{n}</div>
    <div class="p2-sess-title">{title}</div>
    <div class="p2-sess-meta"><span class="p2-sess-dot" style="background:{status_color}"></span>{status_label} · {sub}</div>
  </div>
  {action_html}
</div>'''
    return f'''<header class="p1-topbar p1-topbar-msg">
  <h1 class="p1-msg-h1">Mes sessions</h1>
</header>
<main class="p1-main p1-main-msg">
  <div class="p1-msg-tabs" style="margin-top:8px">
    <span class="p1-msg-tab p1-msg-tab-on">À venir · 2</span>
    <span class="p1-msg-tab">Passées · 12</span>
  </div>
  <div class="p2-sess-list">
    {''.join(row(s) for s in upcoming)}
    <h3 class="p1-sec-title" style="margin-left:18px">Passées (extrait)</h3>
    {''.join(row(s) for s in past)}
  </div>
</main>'''


def screen_book_session(th: dict) -> str:
    days = [
        ('LUN', '3', False, False), ('MAR', '4', False, False),
        ('MER', '5', False, True),  # selected
        ('JEU', '6', False, False), ('VEN', '7', False, False),
        ('SAM', '8', True, False),  # full
        ('DIM', '9', True, False),
    ]
    days_html = ''
    for d, n, full, sel in days:
        cls = 'p2-day p2-day-on' if sel else ('p2-day p2-day-disabled' if full else 'p2-day')
        days_html += f'<button class="{cls}"><span>{d}</span><b>{n}</b></button>'
    slots = [('09:00', False), ('10:30', False), ('12:00', False), ('14:00', True), ('15:30', False), ('17:00', False), ('18:30', False), ('20:00', False)]
    slots_html = ''.join(f'<button class="p2-slot{" p2-slot-on" if on else ""}">{t}</button>' for t, on in slots)
    durations = [(30, '15 €'), (45, '21 €'), (60, '28 €'), (90, '40 €')]
    dur_html = ''
    for d, p in durations:
        on = d == 60
        cls = ' p2-dur-on' if on else ''
        dur_html += f'''<button class="p2-dur{cls}"><b>{d} min</b><span>{p}</span></button>'''
    return f'''{settings_topbar('Réserver une session')}
<main class="p1-main">

  <div class="p2-creator-card">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="" class="p2-creator-avatar"/>
    <div class="p2-creator-text">
      <div class="p2-creator-name">Sara Khan
        <ion-icon name="checkmark-circle" style="font-size:14px;color:var(--mint);vertical-align:middle"></ion-icon>
      </div>
      <div class="p2-creator-sub">Coach yoga · 4.9 ★ · 138 sessions</div>
    </div>
  </div>

  <div class="p1-msg-tabs" style="padding:0">
    <span class="p1-msg-tab p1-msg-tab-on">Single session</span>
    <span class="p1-msg-tab">Pack (économise 25%)</span>
  </div>

  <h3 class="p1-sec-title">Durée &amp; tarif</h3>
  <div class="p2-dur-grid">{dur_html}</div>

  <h3 class="p1-sec-title">Date</h3>
  <div class="p2-days">{days_html}</div>

  <h3 class="p1-sec-title">Créneau · mercredi 5 juin</h3>
  <div class="p2-slots">{slots_html}</div>

  <div class="p2-book-summary">
    <div>
      <div class="p2-book-sum-lbl">Total</div>
      <div class="p2-book-sum-amount">28 €</div>
    </div>
    {primary_cta("Continuer · payer")}
  </div>
</main>'''


def screen_session_payment(th: dict) -> str:
    return f'''{settings_topbar('Paiement')}
<main class="p1-main">

  <div class="p2-pay-summary">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80" alt="" class="p2-pay-avatar"/>
    <div class="p2-pay-text">
      <div class="p2-pay-creator">Sara Khan</div>
      <div class="p2-pay-when">Mer. 5 juin · 14h00 · 60 min</div>
    </div>
  </div>

  <h3 class="p1-sec-title">Méthode de paiement</h3>
  <div class="p2-pay-methods">
    <button class="p2-pay-method p2-pay-method-on">
      <ion-icon name="logo-apple" style="font-size:24px;color:var(--text)"></ion-icon>
      <span>Apple Pay</span>
      <span class="p2-pay-method-tag">Plus rapide</span>
    </button>
    <button class="p2-pay-method">
      <ion-icon name="card-outline" style="font-size:22px;color:var(--mint)"></ion-icon>
      <span>•••• 4242 (Visa)</span>
    </button>
    <button class="p2-pay-method">
      <ion-icon name="add-circle-outline" style="font-size:22px;color:var(--sub)"></ion-icon>
      <span style="color:var(--sub)">Ajouter une carte</span>
    </button>
  </div>

  <h3 class="p1-sec-title">Détail</h3>
  <div class="p2-pay-detail">
    <div class="p2-pay-line"><span>Session 1:1 · 60 min</span><span>28,00 €</span></div>
    <div class="p2-pay-line"><span>Frais de service</span><span>1,40 €</span></div>
    <div class="p2-pay-line"><span>TVA (20%)</span><span>5,88 €</span></div>
    <div class="p2-pay-line p2-pay-line-total"><span>Total</span><span>35,28 €</span></div>
  </div>

  <div class="p2-pay-secure">
    <ion-icon name="lock-closed" style="font-size:14px;color:var(--mint);vertical-align:middle"></ion-icon>
    Paiement sécurisé par Stripe · données chiffrées
  </div>

  <div class="p1-form">
    <button class="cta-primary p2-applepay-cta">
      <ion-icon name="logo-apple" style="font-size:20px;color:#fff;vertical-align:middle"></ion-icon>
      <span style="margin-left:6px">Payer 35,28 €</span>
    </button>
    <p class="p1-trial-note">Annulable jusqu&rsquo;à 24h avant · remboursement intégral</p>
  </div>
</main>'''


def screen_private_call(th: dict) -> str:
    return f'''<div class="p2-call-root">
  <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&h=1500&fit=crop&q=80" alt="" class="p2-call-bg"/>
  <div class="p2-call-overlay"></div>

  <header class="p2-call-top">
    <div class="p2-call-info">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80" alt="" class="p2-call-avatar-mini"/>
      <div>
        <div class="p2-call-name">Sara Khan</div>
        <div class="p2-call-timer">
          <span class="p2-call-live-dot"></span>
          18:24
        </div>
      </div>
    </div>
    <button class="p2-call-flip"><ion-icon name="camera-reverse" style="font-size:22px;color:#fff"></ion-icon></button>
  </header>

  <div class="p2-call-me-thumb">
    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=300&fit=crop&q=80" alt=""/>
  </div>

  <div class="p2-call-quality">
    <ion-icon name="cellular" style="font-size:14px;color:var(--mint)"></ion-icon>
    <span>HD · 720p</span>
  </div>

  <div class="p2-call-controls">
    <button class="p2-call-btn">
      <ion-icon name="mic" style="font-size:24px;color:#fff"></ion-icon>
    </button>
    <button class="p2-call-btn">
      <ion-icon name="videocam" style="font-size:24px;color:#fff"></ion-icon>
    </button>
    <button class="p2-call-btn p2-call-btn-secondary">
      <ion-icon name="volume-high" style="font-size:24px;color:#fff"></ion-icon>
    </button>
    <button class="p2-call-btn p2-call-btn-end">
      <ion-icon name="call" style="font-size:24px;color:#fff;transform:rotate(135deg)"></ion-icon>
    </button>
  </div>
</div>'''


def screen_session_ended(th: dict) -> str:
    return f'''<div class="success-wrap">
  <div class="success-confetti"></div>
  <div class="success-check">
    <div class="success-check-ring"></div>
    <ion-icon name="checkmark" class="success-check-icon"></ion-icon>
  </div>
  <h1 class="success-title">Session terminée !</h1>
  <p class="success-body">60 min avec Sara Khan · Yoga vinyasa</p>

  <div class="p2-stats-card">
    <div class="p2-stat">
      <div class="p2-stat-num">60</div>
      <div class="p2-stat-lbl">min</div>
    </div>
    <div class="p2-stat-divider"></div>
    <div class="p2-stat">
      <div class="p2-stat-num">HD</div>
      <div class="p2-stat-lbl">Qualité</div>
    </div>
  </div>

  <h3 class="p2-rate-title">Note ta session</h3>
  <div class="p2-rate-stars">
    <span class="p2-star p2-star-on">★</span>
    <span class="p2-star p2-star-on">★</span>
    <span class="p2-star p2-star-on">★</span>
    <span class="p2-star p2-star-on">★</span>
    <span class="p2-star p2-star-on">★</span>
  </div>

  <div class="p2-rate-actions">
    <button class="cta-primary">Réserver à nouveau</button>
    <button class="auth-link-row">Terminé</button>
  </div>
</div>'''


# ─── BUSINESS ──────────────────────────────────────────────


def screen_business_discovery(th: dict) -> str:
    spots = [
        ('https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600&h=400&fit=crop&q=80', 'Vibe Fitness Studio', 'Salle de sport · 0.8 km', '4.8 ★', '24 reviews'),
        ('https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=600&h=400&fit=crop&q=80', 'Yoga Lounge MTL', 'Studio yoga · 1.2 km', '4.9 ★', '156 reviews'),
        ('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600&h=400&fit=crop&q=80', 'CrossFit Plateau', 'Crossfit · 2.1 km', '4.7 ★', '89 reviews'),
    ]
    rows = ''
    for img, name, sub, rating, reviews in spots:
        rows += f'''<div class="p2-biz-card">
  <img src="{img}" alt="" class="p2-biz-cover"/>
  <div class="p2-biz-info">
    <div class="p2-biz-name">{name}</div>
    <div class="p2-biz-sub">{sub}</div>
    <div class="p2-biz-meta">
      <span class="p2-biz-rating">{rating}</span>
      <span class="p2-biz-reviews">· {reviews}</span>
    </div>
  </div>
</div>'''
    return f'''<header class="p1-topbar p1-topbar-msg">
  <h1 class="p1-msg-h1">Découvrir</h1>
  <button class="p1-msg-new-btn"><ion-icon name="map" style="font-size:22px;color:var(--mint)"></ion-icon></button>
</header>
<main class="p1-main p1-main-msg">
  <div class="p1-msg-search" style="margin-top:6px">
    <ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
    <span class="p1-msg-search-val">Yoga · Paris</span>
  </div>

  <div class="p1-msg-tabs">
    <span class="p1-msg-tab p1-msg-tab-on">Tous · 24km</span>
    <span class="p1-msg-tab">Yoga</span>
    <span class="p1-msg-tab">CrossFit</span>
    <span class="p1-msg-tab">Pilates</span>
    <span class="p1-msg-tab">Boxe</span>
  </div>

  <div class="p2-biz-list">{rows}</div>
</main>'''


def screen_business_booking(th: dict) -> str:
    return f'''{settings_topbar('Réserver')}
<main class="p1-main">
  <div class="p2-creator-card">
    <img src="https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=200&h=200&fit=crop&q=80" alt="" class="p2-creator-avatar"/>
    <div class="p2-creator-text">
      <div class="p2-creator-name">Vibe Fitness Studio</div>
      <div class="p2-creator-sub">12 rue de Rivoli, Paris · 4.8 ★</div>
    </div>
  </div>

  <div class="p2-kyc-progress">
    <div class="p2-kyc-step p2-kyc-step-done"><span class="p2-kyc-num"><ion-icon name="checkmark" style="font-size:12px;color:#fff"></ion-icon></span>Service</div>
    <div class="p2-kyc-step p2-kyc-step-on"><span class="p2-kyc-num">2</span>Date</div>
    <div class="p2-kyc-step"><span class="p2-kyc-num">3</span>Créneau</div>
    <div class="p2-kyc-step"><span class="p2-kyc-num">4</span>Confirmer</div>
  </div>

  <h3 class="p1-sec-title">Service choisi</h3>
  <div class="p2-svc-chosen">
    <span class="p1-row-ic" style="background:rgba(38,193,164,.15);color:var(--mint)"><ion-icon name="barbell-outline" style="font-size:18px"></ion-icon></span>
    <div class="p2-svc-text">
      <div class="p2-svc-name">CrossFit Box · 60 min</div>
      <div class="p2-svc-meta">Coach Mike · 25 €</div>
    </div>
    <button class="p2-svc-change">Changer</button>
  </div>

  <h3 class="p1-sec-title">Date</h3>
  <div class="p2-days">
    <button class="p2-day"><span>LUN</span><b>3</b></button>
    <button class="p2-day p2-day-on"><span>MAR</span><b>4</b></button>
    <button class="p2-day"><span>MER</span><b>5</b></button>
    <button class="p2-day"><span>JEU</span><b>6</b></button>
    <button class="p2-day"><span>VEN</span><b>7</b></button>
    <button class="p2-day p2-day-disabled"><span>SAM</span><b>8</b></button>
    <button class="p2-day"><span>DIM</span><b>9</b></button>
  </div>

  <h3 class="p1-sec-title">Créneau · mardi 4 juin</h3>
  <div class="p2-slots">
    <button class="p2-slot">07:00</button>
    <button class="p2-slot">08:30</button>
    <button class="p2-slot p2-slot-on">10:00</button>
    <button class="p2-slot">12:30</button>
    <button class="p2-slot p2-slot-full">14:00 ·</button>
    <button class="p2-slot">17:00</button>
    <button class="p2-slot">18:30</button>
    <button class="p2-slot">19:30</button>
  </div>

  <div class="p2-book-summary">
    <div>
      <div class="p2-book-sum-lbl">Total</div>
      <div class="p2-book-sum-amount">25 €</div>
    </div>
    {primary_cta("Continuer · confirmer")}
  </div>
</main>'''


# ─── LIVE ──────────────────────────────────────────────────


def screen_go_live(th: dict) -> str:
    return f'''<header class="auth-topbar">{close_button()}<span style="width:40px"></span></header>
<main class="auth-main">
  <h1 class="auth-title" style="text-align:left">Configure ton live</h1>
  <p class="auth-sub" style="text-align:left">Vérifie tout avant de démarrer</p>

  <div class="auth-form">
    {input_field("Titre du live", value='Sunrise yoga · Plateau MTL ☀️', icon='videocam-outline')}
  </div>

  <h3 class="p1-sec-title">Accès</h3>
  <div class="p2-access-cards">
    <button class="p2-access p2-access-on">
      <ion-icon name="globe-outline" style="font-size:22px;color:var(--mint)"></ion-icon>
      <div>
        <div class="p2-access-title">Public · gratuit</div>
        <div class="p2-access-sub">Tout le monde peut rejoindre</div>
      </div>
      <ion-icon name="radio-button-on" style="font-size:18px;color:var(--mint)"></ion-icon>
    </button>
    <button class="p2-access">
      <ion-icon name="star-outline" style="font-size:22px;color:#9966FF"></ion-icon>
      <div>
        <div class="p2-access-title">Abonnés de la chaîne</div>
        <div class="p2-access-sub">9,99 €/mois · 412 fans actifs</div>
      </div>
      <ion-icon name="radio-button-off" style="font-size:18px;color:var(--sub)"></ion-icon>
    </button>
    <button class="p2-access">
      <ion-icon name="cash-outline" style="font-size:22px;color:#FFA63D"></ion-icon>
      <div>
        <div class="p2-access-title">Pay-per-view · 4,99 €</div>
        <div class="p2-access-sub">Stripe Connect requis</div>
      </div>
      <ion-icon name="radio-button-off" style="font-size:18px;color:var(--sub)"></ion-icon>
    </button>
  </div>

  <h3 class="p1-sec-title">Prévisualisation</h3>
  <div class="p2-live-preview">
    <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600&h=900&fit=crop&q=80" alt="" class="p2-live-preview-img"/>
    <div class="p2-live-preview-overlay"></div>
    <div class="p2-live-preview-controls">
      <button class="p2-live-pre-btn"><ion-icon name="camera-reverse" style="font-size:22px;color:#fff"></ion-icon></button>
      <button class="p2-live-pre-btn"><ion-icon name="color-wand" style="font-size:22px;color:#fff"></ion-icon></button>
    </div>
  </div>

  <div class="p1-form">
    {primary_cta("Démarrer le live · LIVE 🔴")}
  </div>
</main>'''


def screen_live_streaming(th: dict) -> str:
    return f'''<div class="p2-call-root">
  <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=900&h=1700&fit=crop&q=80" alt="" class="p2-call-bg"/>
  <div class="p2-call-overlay"></div>

  <header class="p2-live-top">
    <span class="p2-live-badge">
      <span class="p2-call-live-dot"></span>
      LIVE
    </span>
    <div class="p2-live-title">Sunrise yoga · Plateau ☀️</div>
    <div class="p2-live-stats">
      <span class="p2-live-viewers">
        <ion-icon name="eye" style="font-size:14px;color:#fff"></ion-icon>
        184
      </span>
      <button class="p2-live-close"><ion-icon name="close" style="font-size:18px;color:#fff"></ion-icon></button>
    </div>
  </header>

  <div class="p2-live-side">
    <button class="p2-live-side-btn">
      <ion-icon name="heart" style="font-size:26px;color:#FF4658"></ion-icon>
      <span>2.4K</span>
    </button>
    <button class="p2-live-side-btn">
      <ion-icon name="cash" style="font-size:26px;color:#FFA63D"></ion-icon>
      <span>👊 +50</span>
    </button>
    <button class="p2-live-side-btn">
      <ion-icon name="share-social" style="font-size:24px;color:#fff"></ion-icon>
      <span>Partager</span>
    </button>
  </div>

  <div class="p2-live-bottom">
    <button class="p2-live-mic">
      <ion-icon name="mic" style="font-size:24px;color:#fff"></ion-icon>
    </button>
    <button class="p2-live-cam">
      <ion-icon name="videocam" style="font-size:24px;color:#fff"></ion-icon>
    </button>
    <button class="p2-live-end">
      <ion-icon name="stop" style="font-size:22px;color:#fff"></ion-icon>
      <span>Arrêter</span>
    </button>
  </div>
</div>'''


SCREENS = {
    'p2_creator_wallet_v2': ('Wallet Créateur', screen_creator_wallet),
    'p2_smup_wallet_v2': ('Wallet Smups', screen_smup_wallet),
    'p2_platform_subscription_v2': ('Premium', screen_platform_subscription),
    'p2_identity_verification_v2': ('KYC Identity', screen_identity_verification),
    'p2_my_sessions_v2': ('Mes sessions', screen_my_sessions),
    'p2_book_session_v2': ('Book session', screen_book_session),
    'p2_session_payment_v2': ('Paiement', screen_session_payment),
    'p2_private_call_v2': ('Private call', screen_private_call),
    'p2_session_ended_v2': ('Session ended', screen_session_ended),
    'p2_business_discovery_v2': ('Business discovery', screen_business_discovery),
    'p2_business_booking_v2': ('Business booking', screen_business_booking),
    'p2_go_live_v2': ('Go Live', screen_go_live),
    'p2_live_streaming_v2': ('Live streaming', screen_live_streaming),
}


_P2_CSS = """
<style>
  /* P2 wallet hero */
  .p2-wallet-hero { background:linear-gradient(135deg, rgba(38,193,164,.20), rgba(0,179,199,.10));
    border:1.5px solid rgba(38,193,164,.45); border-radius:24px; padding:20px;
    box-shadow:0 0 32px rgba(38,193,164,.20); margin:0 0 14px; }
  .p2-wallet-label { font-size:11px; font-weight:800; color:var(--mint); letter-spacing:.14em;
    text-transform:uppercase; }
  .p2-wallet-amount { font-size:36px; font-weight:900; color:var(--text);
    letter-spacing:-.03em; margin:6px 0; line-height:1; }
  .p2-wallet-row { display:flex; align-items:center; gap:14px; margin-top:10px; }
  .p2-wallet-stat { display:flex; flex-direction:column; }
  .p2-wallet-stat-num { font-size:14px; font-weight:800; color:var(--mint); }
  .p2-wallet-stat-lbl { font-size:10.5px; font-weight:600; color:var(--sub);
    margin-top:1px; letter-spacing:.04em; }
  .p2-wallet-divider { width:1px; height:32px; background:rgba(38,193,164,.30); }
  .p2-wallet-cashout { width:100%; margin-top:14px; padding:11px;
    border:none; border-radius:14px;
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    color:#fff; font-family:inherit; font-size:14px; font-weight:800;
    cursor:pointer; display:flex; align-items:center; justify-content:center; gap:6px;
    box-shadow:0 4px 14px rgba(38,193,164,.45); }
  .p2-tabs { display:flex; gap:6px; margin:0 0 12px; overflow-x:auto; scrollbar-width:none; }
  .p2-tabs::-webkit-scrollbar { display:none; }
  .p2-tab { padding:7px 14px; border-radius:999px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    font-size:12.5px; font-weight:700; color:var(--sub); white-space:nowrap; cursor:pointer; }
  .p2-tab-on { background:var(--card); color:var(--mint);
    border-color:rgba(38,193,164,.45);
    box-shadow:0 0 14px rgba(38,193,164,.25); }
  .p2-tier { background:var(--card); border:1px solid var(--input-border);
    border-radius:14px; padding:12px 14px; margin:0 0 14px; }
  .p2-tier-bar { height:6px; border-radius:999px; background:var(--input-border); overflow:hidden;
    margin-bottom:8px; }
  .p2-tier-fill { height:100%; border-radius:999px;
    background:linear-gradient(90deg, var(--mint-hi), var(--mint-deep));
    box-shadow:0 0 8px rgba(38,193,164,.40); }
  .p2-tier-text { display:flex; justify-content:space-between; align-items:center;
    font-size:11.5px; font-weight:600; color:var(--text); }
  .p2-tier-next { color:var(--sub); font-size:10.5px; }

  /* Transactions */
  .p2-txn { display:flex; align-items:center; gap:12px;
    padding:11px 12px; border-radius:14px;
    background:var(--card); border:1px solid var(--input-border);
    margin-bottom:8px; }
  .p2-txn-text { flex:1; min-width:0; }
  .p2-txn-lbl { font-size:13px; font-weight:700; color:var(--text); }
  .p2-txn-meta { font-size:11px; font-weight:500; color:var(--sub); margin-top:2px; }
  .p2-txn-amount { font-size:15px; font-weight:800; color:var(--mint);
    letter-spacing:-.01em; flex-shrink:0; }
  .p2-smup-count { font-size:13px; font-weight:800; color:var(--mint); flex-shrink:0; }
  .p2-view-all { width:100%; padding:11px; margin-top:6px;
    border:1.5px solid var(--input-border); border-radius:14px;
    background:transparent; color:var(--text);
    font-family:inherit; font-size:13px; font-weight:700; cursor:pointer; }

  /* Smups wallet hero */
  .p2-smup-hero { display:flex; flex-direction:column; align-items:center;
    background:linear-gradient(135deg, rgba(255,166,61,.15), rgba(255,70,88,.08));
    border:1.5px solid rgba(255,166,61,.45);
    border-radius:24px; padding:24px;
    margin:0 0 14px;
    box-shadow:0 0 32px rgba(255,166,61,.20); }
  .p2-smup-icon { font-size:48px; line-height:1;
    filter:drop-shadow(0 0 12px rgba(255,166,61,.50)); margin-bottom:6px; }
  .p2-smup-amount { font-size:42px; font-weight:900; color:var(--text);
    letter-spacing:-.03em; line-height:1; }
  .p2-smup-lbl { font-size:11px; font-weight:800; color:#FFA63D;
    letter-spacing:.10em; text-transform:uppercase; margin-top:6px; }
  .p2-smup-equiv { font-size:12px; font-weight:600; color:var(--sub); margin-top:10px; }
  .p2-smup-actions { display:flex; gap:10px; margin:0 0 14px; }
  .p2-smup-btn { flex:1; display:inline-flex; align-items:center; justify-content:center; gap:6px;
    padding:13px; border-radius:14px;
    background:var(--card); border:1.5px solid rgba(38,193,164,.45);
    color:var(--mint); font-family:inherit; font-size:13.5px; font-weight:800;
    cursor:pointer; box-shadow:0 0 14px rgba(38,193,164,.20); }
  .p2-smup-btn-primary {
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep)) !important;
    color:#fff !important; border:none !important;
    box-shadow:0 4px 14px rgba(38,193,164,.45) !important; }

  /* KYC */
  .p2-kyc-progress { display:flex; align-items:center; gap:6px;
    padding:0 0 8px; margin:0 0 14px; overflow-x:auto; }
  .p2-kyc-step { display:flex; align-items:center; gap:6px;
    padding:5px 10px; border-radius:999px;
    background:var(--input-bg); border:1px solid var(--input-border);
    font-size:11px; font-weight:700; color:var(--sub);
    white-space:nowrap; flex-shrink:0; }
  .p2-kyc-step-on { background:var(--card); color:var(--mint);
    border-color:rgba(38,193,164,.45);
    box-shadow:0 0 10px rgba(38,193,164,.20); }
  .p2-kyc-step-done { background:rgba(38,193,164,.10); color:var(--mint);
    border-color:rgba(38,193,164,.30); }
  .p2-kyc-num { width:18px; height:18px; border-radius:999px;
    background:var(--input-border); color:var(--sub);
    display:inline-flex; align-items:center; justify-content:center;
    font-size:10px; font-weight:800; }
  .p2-kyc-step-on .p2-kyc-num { background:var(--mint); color:#fff;
    box-shadow:0 0 6px rgba(38,193,164,.50); }
  .p2-kyc-step-done .p2-kyc-num { background:var(--mint); }
  .p2-kyc-cards { display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; margin:0 0 16px; }
  .p2-kyc-card { display:flex; flex-direction:column; align-items:center; gap:5px;
    padding:14px 8px; border-radius:14px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; }
  .p2-kyc-card-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.06);
    box-shadow:0 0 14px rgba(38,193,164,.20); }
  .p2-kyc-card-title { font-size:12px; font-weight:700; color:var(--text); }
  .p2-kyc-card-sub { font-size:10px; font-weight:700; color:var(--mint); }
  .p2-kyc-photo { margin:0 0 14px; }
  .p2-kyc-photo-frame { aspect-ratio:5/3;
    background:var(--input-bg); border:2px dashed rgba(38,193,164,.40);
    border-radius:18px; display:flex; flex-direction:column;
    align-items:center; justify-content:center; gap:6px;
    box-shadow:0 0 18px rgba(38,193,164,.15); }
  .p2-kyc-photo-lbl { font-size:12px; font-weight:700; color:var(--mint); }
  .p2-kyc-info { display:flex; align-items:flex-start; gap:10px;
    padding:12px 14px; border-radius:14px;
    background:rgba(38,193,164,.06); border:1px solid rgba(38,193,164,.20);
    margin:0 0 14px; }
  .p2-kyc-info-title { font-size:12.5px; font-weight:800; color:var(--mint); margin-bottom:3px; }
  .p2-kyc-info-sub { font-size:11.5px; font-weight:500; color:var(--sub); line-height:1.4; }

  /* Sessions list */
  .p2-sess-list { display:flex; flex-direction:column; gap:0; }
  .p2-sess-row { display:flex; align-items:center; gap:12px;
    padding:14px 18px; border-bottom:1px solid var(--border); }
  .p2-sess-avatar { width:52px; height:52px; border-radius:14px; object-fit:cover;
    border:2px solid rgba(38,193,164,.30);
    box-shadow:0 0 10px rgba(38,193,164,.18); flex-shrink:0; }
  .p2-sess-text { flex:1; min-width:0; }
  .p2-sess-name { font-size:14px; font-weight:800; color:var(--text); }
  .p2-sess-title { font-size:12.5px; font-weight:600; color:var(--text); margin-top:2px; opacity:.85; }
  .p2-sess-meta { font-size:11px; font-weight:600; color:var(--sub); margin-top:3px;
    display:flex; align-items:center; gap:5px; }
  .p2-sess-dot { width:6px; height:6px; border-radius:999px; }
  .p2-sess-join { padding:8px 14px; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    color:#fff; border:none; font-family:inherit; font-size:12px; font-weight:800;
    cursor:pointer; box-shadow:0 4px 12px rgba(38,193,164,.40); }
  .p2-sess-rating { font-size:12px; font-weight:700; color:#FFA63D; }

  /* Book session */
  .p2-creator-card { display:flex; align-items:center; gap:12px;
    padding:12px 14px; margin:0 0 14px;
    background:var(--card); border:1.5px solid rgba(38,193,164,.30);
    border-radius:18px;
    box-shadow:0 0 20px rgba(38,193,164,.12); }
  .p2-creator-avatar { width:56px; height:56px; border-radius:999px; object-fit:cover;
    border:2px solid var(--mint); flex-shrink:0; }
  .p2-creator-text { flex:1; min-width:0; }
  .p2-creator-name { font-size:14.5px; font-weight:800; color:var(--text);
    display:flex; align-items:center; gap:4px; }
  .p2-creator-sub { font-size:12px; font-weight:600; color:var(--sub); margin-top:2px; }
  .p2-dur-grid { display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; margin:0 0 14px; }
  .p2-dur { display:flex; flex-direction:column; align-items:center; gap:2px;
    padding:14px 4px; border-radius:14px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; }
  .p2-dur b { font-size:13.5px; font-weight:800; color:var(--text); }
  .p2-dur span { font-size:11px; font-weight:600; color:var(--sub); }
  .p2-dur-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.08);
    box-shadow:0 0 14px rgba(38,193,164,.20); }
  .p2-dur-on b, .p2-dur-on span { color:var(--mint); }
  .p2-days { display:grid; grid-template-columns:repeat(7, 1fr); gap:5px; margin:0 0 14px; }
  .p2-day { display:flex; flex-direction:column; align-items:center; gap:1px;
    padding:10px 0; border-radius:12px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; }
  .p2-day span { font-size:9px; font-weight:800; color:var(--sub); letter-spacing:.06em; }
  .p2-day b { font-size:15px; font-weight:800; color:var(--text); }
  .p2-day-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.10);
    box-shadow:0 0 12px rgba(38,193,164,.25); }
  .p2-day-on span, .p2-day-on b { color:var(--mint); }
  .p2-day-disabled { opacity:.4; cursor:not-allowed; }
  .p2-slots { display:grid; grid-template-columns:repeat(4, 1fr); gap:6px; margin:0 0 14px; }
  .p2-slot { padding:9px 4px; border-radius:11px;
    background:var(--card); border:1.5px solid var(--input-border);
    color:var(--text); font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; }
  .p2-slot-on { background:linear-gradient(135deg, rgba(38,193,164,.16), rgba(0,179,199,.10));
    color:var(--mint); border-color:rgba(38,193,164,.45);
    box-shadow:0 0 14px rgba(38,193,164,.25); }
  .p2-slot-full { opacity:.4; cursor:not-allowed; text-decoration:line-through; }
  .p2-book-summary { display:flex; align-items:center; gap:14px;
    padding:14px 16px; margin:14px 0 0;
    background:var(--card); border:1.5px solid rgba(38,193,164,.30);
    border-radius:18px; box-shadow:0 0 20px rgba(38,193,164,.15); }
  .p2-book-sum-lbl { font-size:11px; font-weight:700; color:var(--sub); letter-spacing:.04em;
    text-transform:uppercase; }
  .p2-book-sum-amount { font-size:22px; font-weight:900; color:var(--mint);
    letter-spacing:-.02em; margin-top:2px; }
  .p2-book-summary .cta-primary { flex:1; }

  /* Payment */
  .p2-pay-summary { display:flex; align-items:center; gap:12px;
    padding:14px; background:var(--card);
    border:1.5px solid rgba(38,193,164,.30); border-radius:18px;
    box-shadow:0 0 18px rgba(38,193,164,.10); margin:0 0 14px; }
  .p2-pay-avatar { width:48px; height:48px; border-radius:999px; object-fit:cover;
    border:2px solid var(--mint); flex-shrink:0; }
  .p2-pay-creator { font-size:14px; font-weight:800; color:var(--text); }
  .p2-pay-when { font-size:12px; font-weight:600; color:var(--sub); margin-top:2px; }
  .p2-pay-methods { display:flex; flex-direction:column; gap:8px; margin:0 0 14px; }
  .p2-pay-method { display:flex; align-items:center; gap:14px;
    padding:14px 14px; border-radius:14px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; }
  .p2-pay-method-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.06);
    box-shadow:0 0 14px rgba(38,193,164,.20); }
  .p2-pay-method span { font-size:14px; font-weight:700; color:var(--text);
    text-align:left; flex:1; }
  .p2-pay-method-tag { font-size:10px; font-weight:800; color:var(--mint);
    background:rgba(38,193,164,.14); padding:3px 8px; border-radius:999px;
    flex:0 !important; }
  .p2-pay-detail { background:var(--card); border:1px solid var(--input-border);
    border-radius:14px; padding:12px 14px; margin:0 0 14px; }
  .p2-pay-line { display:flex; justify-content:space-between;
    padding:6px 0; font-size:13px; font-weight:600; color:var(--text); }
  .p2-pay-line-total { font-weight:800; font-size:15px; color:var(--mint);
    border-top:1px solid var(--border); margin-top:6px; padding-top:10px; }
  .p2-pay-secure { display:flex; align-items:center; justify-content:center; gap:6px;
    font-size:11.5px; font-weight:600; color:var(--sub); margin:0 0 12px; }
  .p2-applepay-cta { background:#000 !important; box-shadow:0 8px 24px rgba(0,0,0,.45) !important;
    border:1px solid rgba(255,255,255,.08) !important; }

  /* Private call */
  .p2-call-root { position:absolute; inset:0; }
  .p2-call-bg { width:100%; height:100%; object-fit:cover; }
  .p2-call-overlay { position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,.45) 0%, transparent 25%, transparent 75%, rgba(0,0,0,.65) 100%); }
  .p2-call-top { position:absolute; top:14px; left:14px; right:14px; z-index:6;
    display:flex; justify-content:space-between; align-items:center; }
  .p2-call-info { display:flex; align-items:center; gap:10px; }
  .p2-call-avatar-mini { width:38px; height:38px; border-radius:999px; object-fit:cover;
    border:2px solid #fff; }
  .p2-call-name { font-size:14px; font-weight:800; color:#fff;
    text-shadow:0 2px 4px rgba(0,0,0,.6); }
  .p2-call-timer { display:flex; align-items:center; gap:6px;
    font-size:12px; font-weight:700; color:#fff;
    text-shadow:0 2px 4px rgba(0,0,0,.6); margin-top:1px; }
  .p2-call-live-dot { width:7px; height:7px; border-radius:999px; background:#FF4658;
    box-shadow:0 0 8px rgba(255,70,88,.7);
    animation:pulse 1.6s infinite; }
  @keyframes pulse { 0%,100% { opacity:1; } 50% { opacity:.4; } }
  .p2-call-flip { width:38px; height:38px; border-radius:999px; border:none;
    background:rgba(0,0,0,.55); backdrop-filter:blur(10px); cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .p2-call-me-thumb { position:absolute; top:70px; right:14px; z-index:5;
    width:96px; aspect-ratio:9/16; border-radius:14px; overflow:hidden;
    box-shadow:0 4px 16px rgba(0,0,0,.5), 0 0 0 2px #fff; }
  .p2-call-me-thumb img { width:100%; height:100%; object-fit:cover; }
  .p2-call-quality { position:absolute; bottom:160px; left:50%; transform:translateX(-50%); z-index:5;
    display:flex; align-items:center; gap:5px;
    padding:5px 10px; border-radius:999px;
    background:rgba(0,0,0,.55); backdrop-filter:blur(8px);
    color:#fff; font-size:11px; font-weight:700; }
  .p2-call-controls { position:absolute; bottom:36px; left:0; right:0; z-index:6;
    display:flex; justify-content:center; gap:14px; padding:0 18px; }
  .p2-call-btn { width:56px; height:56px; border-radius:999px;
    background:rgba(0,0,0,.55); backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,.15);
    display:flex; align-items:center; justify-content:center;
    cursor:pointer; }
  .p2-call-btn-end { background:#FF4658; border-color:transparent;
    box-shadow:0 8px 20px rgba(255,70,88,.45); }
  .p2-call-btn-secondary { background:rgba(255,255,255,.20); }

  /* Session ended stats */
  .p2-stats-card { display:flex; align-items:center; gap:14px;
    padding:12px 18px; border-radius:18px;
    background:var(--card); border:1px solid rgba(38,193,164,.20);
    box-shadow:0 0 16px rgba(38,193,164,.08);
    margin:0 0 20px; }
  .p2-stat { display:flex; flex-direction:column; align-items:center; flex:1; }
  .p2-stat-num { font-size:22px; font-weight:900; color:var(--mint); letter-spacing:-.02em; }
  .p2-stat-lbl { font-size:10.5px; font-weight:700; color:var(--sub);
    letter-spacing:.04em; margin-top:2px; text-transform:uppercase; }
  .p2-stat-divider { width:1px; height:32px; background:var(--border); }
  .p2-rate-title { font-size:13px; font-weight:800; color:var(--sub);
    text-transform:uppercase; letter-spacing:.06em; margin:0 0 8px; }
  .p2-rate-stars { display:flex; gap:6px; margin:0 0 20px; }
  .p2-star { font-size:32px; line-height:1; color:var(--input-border); cursor:pointer; }
  .p2-star-on { color:#FFA63D; filter:drop-shadow(0 0 6px rgba(255,166,61,.50)); }
  .p2-rate-actions { display:flex; flex-direction:column; gap:8px; width:100%; max-width:320px; }

  /* Business discovery */
  .p2-biz-list { display:flex; flex-direction:column; gap:10px;
    padding:0 18px; }
  .p2-biz-card { display:flex; gap:12px; padding:10px;
    background:var(--card); border:1px solid var(--input-border);
    border-radius:18px; cursor:pointer; }
  .p2-biz-cover { width:88px; height:88px; border-radius:14px; object-fit:cover; flex-shrink:0; }
  .p2-biz-info { flex:1; padding:4px 0; }
  .p2-biz-name { font-size:15px; font-weight:800; color:var(--text); letter-spacing:-.01em; }
  .p2-biz-sub { font-size:12px; font-weight:600; color:var(--sub); margin-top:3px; }
  .p2-biz-meta { display:flex; align-items:center; gap:5px; margin-top:6px; }
  .p2-biz-rating { font-size:12px; font-weight:800; color:#FFA63D; }
  .p2-biz-reviews { font-size:11px; font-weight:600; color:var(--sub); }

  /* Business booking */
  .p2-svc-chosen { display:flex; align-items:center; gap:12px;
    padding:12px 14px; border-radius:14px;
    background:var(--card); border:1.5px solid rgba(38,193,164,.35);
    box-shadow:0 0 16px rgba(38,193,164,.15); margin:0 0 6px; }
  .p2-svc-text { flex:1; min-width:0; }
  .p2-svc-name { font-size:14px; font-weight:800; color:var(--text); }
  .p2-svc-meta { font-size:12px; font-weight:600; color:var(--sub); margin-top:2px; }
  .p2-svc-change { padding:6px 12px; border-radius:999px;
    background:rgba(38,193,164,.10); border:1px solid rgba(38,193,164,.30);
    color:var(--mint); font-family:inherit; font-size:11.5px; font-weight:700; cursor:pointer; }

  /* GoLive */
  .p2-access-cards { display:flex; flex-direction:column; gap:8px; margin:0 0 14px; }
  .p2-access { display:flex; align-items:center; gap:14px;
    padding:14px; border-radius:16px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; text-align:left; }
  .p2-access-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.06);
    box-shadow:0 0 16px rgba(38,193,164,.20); }
  .p2-access div { flex:1; }
  .p2-access-title { font-size:13.5px; font-weight:800; color:var(--text); }
  .p2-access-sub { font-size:11.5px; font-weight:600; color:var(--sub); margin-top:2px; }

  .p2-live-preview { position:relative; aspect-ratio:9/16; max-height:280px;
    border-radius:18px; overflow:hidden; margin:0 0 14px;
    box-shadow:0 0 24px rgba(38,193,164,.15); }
  .p2-live-preview-img { width:100%; height:100%; object-fit:cover; }
  .p2-live-preview-overlay { position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,.10) 0%, transparent 30%, rgba(0,0,0,.40) 100%); }
  .p2-live-preview-controls { position:absolute; bottom:14px; right:14px;
    display:flex; gap:8px; }
  .p2-live-pre-btn { width:38px; height:38px; border-radius:999px; border:none;
    background:rgba(0,0,0,.55); backdrop-filter:blur(8px);
    display:flex; align-items:center; justify-content:center; cursor:pointer; }

  /* Live streaming */
  .p2-live-top { position:absolute; top:14px; left:14px; right:14px; z-index:6;
    display:flex; align-items:center; gap:10px; }
  .p2-live-badge { display:flex; align-items:center; gap:5px;
    padding:5px 10px; border-radius:999px;
    background:#FF4658; color:#fff; font-size:10.5px; font-weight:900;
    letter-spacing:.06em;
    box-shadow:0 4px 12px rgba(255,70,88,.45); }
  .p2-live-title { flex:1; font-size:14px; font-weight:800; color:#fff;
    text-shadow:0 2px 4px rgba(0,0,0,.6); white-space:nowrap; overflow:hidden;
    text-overflow:ellipsis; }
  .p2-live-stats { display:flex; align-items:center; gap:8px; flex-shrink:0; }
  .p2-live-viewers { display:flex; align-items:center; gap:4px;
    padding:5px 10px; border-radius:999px;
    background:rgba(0,0,0,.55); backdrop-filter:blur(8px);
    color:#fff; font-size:11.5px; font-weight:700; }
  .p2-live-close { width:32px; height:32px; border-radius:999px; border:none;
    background:rgba(0,0,0,.55); backdrop-filter:blur(8px);
    display:flex; align-items:center; justify-content:center; cursor:pointer; }
  .p2-live-side { position:absolute; right:14px; top:80px; z-index:5;
    display:flex; flex-direction:column; gap:18px; align-items:center; }
  .p2-live-side-btn { display:flex; flex-direction:column; align-items:center; gap:4px;
    border:none; background:transparent; cursor:pointer; font-family:inherit; }
  .p2-live-side-btn span { font-size:10.5px; font-weight:800; color:#fff;
    text-shadow:0 2px 4px rgba(0,0,0,.6); }
  .p2-live-bottom { position:absolute; bottom:36px; left:0; right:0; z-index:6;
    display:flex; justify-content:center; gap:10px; padding:0 18px; }
  .p2-live-mic, .p2-live-cam { width:50px; height:50px; border-radius:999px;
    background:rgba(0,0,0,.55); backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,.15);
    display:flex; align-items:center; justify-content:center; cursor:pointer; }
  .p2-live-end { display:flex; align-items:center; gap:6px;
    padding:14px 22px; border:none; border-radius:999px;
    background:#FF4658; color:#fff;
    font-family:inherit; font-size:14px; font-weight:800;
    cursor:pointer;
    box-shadow:0 8px 20px rgba(255,70,88,.45); }
</style>
"""


def build(key: str, dark: bool) -> str:
    th = theme(dark)
    title, fn = SCREENS[key]
    body = fn(th)
    auth_full = auth_build_fn('auth_welcome_v2', dark)
    head_end = auth_full.index('</style>') + len('</style>')
    head = auth_full[:head_end].replace('Smuppy V2 — Welcome', f'Smuppy V2 — {title}')
    return head + _P1_CSS + '\n' + _P2_CSS + '\n</head><body>\n' + body + '\n</body></html>'


def write_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for key in SCREENS.keys():
        for dark in (True, False):
            t = 'dark' if dark else 'light'
            d = OUT_DIR / f'{key}_{t}'
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(build(key, dark))
            n += 1
    print(f'  built {n} P2 maquettes')


if __name__ == '__main__':
    write_all()
