"""Smuppy V2 — P1 SETTINGS + MESSAGES + NOTIFICATIONS canonical maquettes.
19 screens × 2 themes = 38 HTML maquettes at 393×852.
Reuses helpers + base CSS from build_auth_v2.py.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from build_auth_v2 import (
    MINT, MINT_HI, MINT_DEEP, DANGER,
    theme,
    smuppy_icon, smuppy_text, smuppy_full,
    primary_cta, ghost_cta, social_btn,
    input_field, back_button, close_button,
    build as auth_build_fn,
)

OUT_DIR = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')

i18n_settings = json.loads(Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/settings.json').read_text())
i18n_common = json.loads(Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/common.json').read_text()) if Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/common.json').exists() else {}


def ts(*keys):
    d = i18n_settings
    for k in keys:
        d = d.get(k, '?')
    return d


# ─── Atoms ────────────────────────────────────────────────


def settings_topbar(title: str) -> str:
    return f'''<header class="p1-topbar">
  {back_button()}
  <h1 class="p1-topbar-title">{title}</h1>
  <span style="width:40px"></span>
</header>'''


def settings_row(icon: str, hue: str, label: str, value: str = None, control: str = None, is_danger: bool = False, sub: str = None) -> str:
    """Calm settings row : colored bg + colored icon, no hue halo (visual noise reduction may30)."""
    danger_cls = ' p1-row-danger' if is_danger else ''
    val_html = ''
    if value:
        val_html = f'<span class="p1-row-val">{value}</span>'
    if control:
        val_html = control
    elif not control:
        val_html = val_html + '<ion-icon name="chevron-forward" class="p1-row-chev"></ion-icon>'
    sub_html = f'<div class="p1-row-sub">{sub}</div>' if sub else ''
    return f'''<div class="p1-row{danger_cls}">
  <span class="p1-row-ic" style="background:{hue}14;color:{hue}">
    <ion-icon name="{icon}" style="font-size:18px;color:{hue}"></ion-icon>
  </span>
  <div class="p1-row-text">
    <div class="p1-row-lbl">{label}</div>
    {sub_html}
  </div>
  {val_html}
</div>'''


def toggle_on(on: bool = True) -> str:
    cls = 'p1-tog p1-tog-on' if on else 'p1-tog'
    return f'<span class="{cls}"><span class="p1-tog-knob"></span></span>'


def section_title(label: str) -> str:
    return f'<h3 class="p1-sec-title">{label}</h3>'


def card_block(rows_html: str) -> str:
    return f'<div class="p1-card">{rows_html}</div>'


# ─── SETTINGS SCREENS ──────────────────────────────────────


def screen_settings(th: dict) -> str:
    """Settings entry — already partially canonical via v2_canonical_settings_definitive.
    This is the V2 rebuild with sections + canonical bottom nav."""
    return f'''{settings_topbar(ts('sections','title') if ts('sections','title') != '?' else 'Réglages')}
<main class="p1-main">
  <div class="p1-profile-card">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="" class="p1-profile-avatar"/>
    <div class="p1-profile-info">
      <div class="p1-profile-name">Sara Khan
        <ion-icon name="checkmark-circle" style="font-size:14px;color:var(--mint);vertical-align:middle"></ion-icon>
      </div>
      <div class="p1-profile-sub">Coach yoga · Montréal</div>
      <span class="p1-profile-badge">PRO CREATOR · Premium</span>
    </div>
  </div>

  {section_title("Compte")}
  {card_block(
    settings_row('person-outline', '#11C6FF', 'Modifier le profil') +
    settings_row('color-palette-outline', '#9966FF', 'Apparence', value='Sombre') +
    settings_row('language-outline', '#FFA63D', 'Langue', value='Français')
  )}

  {section_title("Préférences")}
  {card_block(
    settings_row('notifications-outline', '#11C6FF', 'Notifications') +
    settings_row('shield-checkmark-outline', '#26C1A4', 'Confidentialité &amp; consentement') +
    settings_row('lock-closed-outline', '#9966FF', 'Sécurité', sub='MFA activée') +
    settings_row('eye-off-outline', '#64748B', 'Utilisateurs bloqués', value='3')
  )}

  {section_title("Création")}
  {card_block(
    settings_row('star-outline', MINT, 'Chaîne · 9,99 € / mois') +
    settings_row('person-circle-outline', '#FFA63D', 'Sessions 1:1') +
    settings_row('cube-outline', '#9966FF', 'Packages')
  )}

  {section_title("Abonnements &amp; paiements")}
  {card_block(
    settings_row('card-outline', MINT, 'Gérer mes abonnements') +
    settings_row('wallet-outline', '#11C6FF', 'Wallet Créateur', value='284,50 €') +
    settings_row('cash-outline', '#FFA63D', 'Wallet Smups', value='👊 412')
  )}

  {section_title("Support")}
  {card_block(
    settings_row('help-circle-outline', '#11C6FF', 'Aide &amp; FAQ') +
    settings_row('flag-outline', '#FFA63D', 'Signaler un problème') +
    settings_row('document-text-outline', '#64748B', 'Conditions &amp; politiques')
  )}

  {section_title("Compte")}
  {card_block(
    settings_row('log-out-outline', '#64748B', 'Se déconnecter') +
    settings_row('trash-outline', DANGER, ts('danger','deleteAccount') if ts('danger','deleteAccount') != '?' else 'Supprimer mon compte', is_danger=True)
  )}
</main>'''


def screen_edit_profile(th: dict) -> str:
    return f'''{settings_topbar(ts('editProfile','title') if ts('editProfile','title') != '?' else 'Modifier le profil')}
<main class="p1-main">
  <div class="p1-cover-wrap">
    <img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=900&h=400&fit=crop&q=80" alt="" class="p1-cover-img"/>
    <button class="p1-cover-edit"><ion-icon name="camera" style="font-size:14px;vertical-align:middle"></ion-icon> Modifier</button>
    <div class="p1-avatar-on-cover">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt=""/>
      <span class="p1-avatar-edit"><ion-icon name="camera" style="font-size:14px;color:#fff"></ion-icon></span>
    </div>
  </div>

  <div class="p1-form">
    {input_field('Prénom', value='Sara', icon='person-outline')}
    {input_field('Nom', value='Khan', icon='person-outline')}
    {input_field('Bio', value='Coach yoga · Montréal · Daily flows 🧘‍♀️', icon='document-text-outline')}
    {input_field('Date de naissance', value='12 mars 1994', icon='calendar-outline')}
    {input_field('Genre', value='Femme', icon='male-female-outline', trailing='<ion-icon name="chevron-down" style="font-size:16px;color:var(--sub)"></ion-icon>')}
    {input_field('Ville', value='Montréal, Canada', icon='location-outline')}
    {primary_cta(ts('editProfile','save') if ts('editProfile','save') != '?' else 'Enregistrer')}
  </div>
</main>'''


def screen_notification_settings(th: dict) -> str:
    return f'''{settings_topbar('Notifications')}
<main class="p1-main">
  <p class="p1-sec-desc">Choisis quelles notifications recevoir</p>

  {section_title("Engagement")}
  {card_block(
    settings_row('heart-outline', '#E63946', 'Likes sur tes posts', control=toggle_on(True)) +
    settings_row('person-add-outline', '#11C6FF', 'Nouveaux fans', control=toggle_on(True)) +
    settings_row('at-outline', '#9966FF', 'Mentions', control=toggle_on(True)) +
    settings_row('chatbubble-outline', '#26C1A4', 'Messages directs', control=toggle_on(True))
  )}

  {section_title("Sessions &amp; rappels")}
  {card_block(
    settings_row('calendar-outline', '#FFA63D', 'Rappels de session 1:1', control=toggle_on(True), sub='15 min avant + 1 jour avant') +
    settings_row('videocam-outline', '#E63946', 'Lives de tes créateurs', control=toggle_on(True)) +
    settings_row('walk-outline', MINT, 'Activités à proximité', control=toggle_on(False))
  )}

  {section_title("Paiements")}
  {card_block(
    settings_row('card-outline', MINT, 'Paiements reçus', control=toggle_on(True)) +
    settings_row('cash-outline', '#FFA63D', 'Smups reçus 👊', control=toggle_on(True)) +
    settings_row('wallet-outline', '#11C6FF', 'Cashout disponible', control=toggle_on(True))
  )}

  {section_title("Marketing")}
  {card_block(
    settings_row('megaphone-outline', '#9966FF', 'Nouvelles features', control=toggle_on(False), sub='Updates Smuppy + nouveautés') +
    settings_row('gift-outline', '#FFA63D', 'Offres &amp; promotions', control=toggle_on(False))
  )}
</main>'''


def screen_privacy_settings(th: dict) -> str:
    return f'''{settings_topbar(ts('privacySettings','title') if ts('privacySettings','title') != '?' else 'Confidentialité')}
<main class="p1-main">
  <p class="p1-sec-desc">Gère ta vie privée et tes données</p>

  {section_title("Visibilité du profil")}
  {card_block(
    settings_row('globe-outline', MINT, 'Profil public', sub='Tout le monde peut te trouver', control=toggle_on(True)) +
    settings_row('people-outline', '#11C6FF', 'Approuver les nouveaux fans', sub='Les demandes apparaissent dans tes notifications', control=toggle_on(False)) +
    settings_row('eye-off-outline', '#9966FF', 'Cacher ma liste de fans', control=toggle_on(False))
  )}

  {section_title("Données &amp; analytics")}
  {card_block(
    settings_row('analytics-outline', '#11C6FF', 'Analytics anonymes', control=toggle_on(True), sub='Aide à améliorer Smuppy') +
    settings_row('megaphone-outline', '#FFA63D', 'Personnalisation pub', control=toggle_on(False))
  )}

  {section_title("Tes droits GDPR")}
  {card_block(
    settings_row('download-outline', MINT, 'Télécharger mes données') +
    settings_row('create-outline', '#11C6FF', 'Rectifier mes données', sub='Conformité Art. 16 RGPD') +
    settings_row('shield-checkmark-outline', '#9966FF', 'Historique des consentements')
  )}

  <div class="p1-correction-banner">
    <ion-icon name="checkmark-circle" style="font-size:18px;color:{MINT};flex-shrink:0;margin-top:1px"></ion-icon>
    <div>
      <div class="p1-banner-title">Demande de rectification soumise</div>
      <div class="p1-banner-sub">Tu seras notifié sous 30 jours.</div>
    </div>
  </div>
</main>'''


def screen_security_settings(th: dict) -> str:
    return f'''{settings_topbar('Sécurité')}
<main class="p1-main">

  <div class="p1-mfa-card">
    <span class="p1-mfa-ic" style="background:rgba(38,193,164,.14);color:{MINT};box-shadow:0 0 18px rgba(38,193,164,.30);filter:drop-shadow(0 0 10px rgba(38,193,164,.30))">
      <ion-icon name="shield-checkmark" style="font-size:32px"></ion-icon>
    </span>
    <div class="p1-mfa-text">
      <div class="p1-mfa-title">Authentification 2 facteurs</div>
      <div class="p1-mfa-status">
        <span class="p1-mfa-dot"></span>
        Activée
      </div>
    </div>
  </div>

  {section_title("Authentification")}
  {card_block(
    settings_row('key-outline', MINT, 'Régénérer codes de secours') +
    settings_row('phone-portrait-outline', '#11C6FF', 'Apps autorisées', value='Google Auth') +
    settings_row('close-circle-outline', DANGER, 'Désactiver le 2FA', is_danger=True)
  )}

  {section_title("Mot de passe")}
  {card_block(
    settings_row('lock-closed-outline', '#9966FF', 'Changer le mot de passe', sub='Dernier changement il y a 3 mois') +
    settings_row('finger-print-outline', MINT, 'Biométrique', control=toggle_on(True))
  )}

  {section_title("Sessions actives")}
  {card_block(
    settings_row('phone-portrait-outline', MINT, 'iPhone 15 Pro (cet appareil)', sub='Montréal, Canada · maintenant') +
    settings_row('phone-portrait-outline', '#64748B', 'iPhone 13', sub='Montréal · il y a 2 jours · Déconnecter')
  )}
</main>'''


def screen_manage_subscription(th: dict) -> str:
    return f'''{settings_topbar('Abonnements')}
<main class="p1-main">

  <div class="p1-sub-hero">
    <div class="p1-sub-hero-row">
      <div>
        <div class="p1-sub-hero-label">SMUPPY PRO CREATOR</div>
        <div class="p1-sub-hero-name">Premium · Annuel</div>
      </div>
      <span class="p1-sub-hero-badge">ACTIF</span>
    </div>
    <div class="p1-sub-hero-price">119,90 € <span>/ an</span></div>
    <div class="p1-sub-hero-renew">
      <ion-icon name="refresh-outline" style="font-size:14px;color:var(--mint);vertical-align:middle"></ion-icon>
      Renouvelle le 12 mars 2027
    </div>
    <button class="p1-sub-hero-btn">Modifier l'abonnement</button>
  </div>

  {section_title("Chaînes auxquelles tu es abonné")}
  {card_block(
    settings_row('star-outline', MINT, 'Sara&rsquo;s Channel', value='9,99 €/mois', sub='Renouvelle le 5 juin') +
    settings_row('star-outline', '#11C6FF', 'Marc Yoga', value='6,99 €/mois', sub='Renouvelle le 18 juin')
  )}

  {section_title("Gérer")}
  {card_block(
    settings_row('logo-apple', '#64748B', 'Gérer sur Apple Store') +
    settings_row('logo-google', '#64748B', 'Gérer sur Google Play') +
    settings_row('document-text-outline', '#9966FF', 'Politique de remboursement', sub='Apple G3.1.2')
  )}
</main>'''


def screen_upgrade_to_pro(th: dict) -> str:
    return f'''{settings_topbar('Upgrade')}
<main class="p1-main">

  <div class="p1-pro-hero">
    {smuppy_icon(72, 'gradient')}
    <h1 class="p1-pro-title">Passe à Smuppy Pro</h1>
    <p class="p1-pro-sub">Débloque toutes les fonctionnalités créateurs</p>
  </div>

  <div class="p1-plans">
    <div class="p1-plan p1-plan-active">
      <div class="p1-plan-header">
        <span class="p1-plan-badge">RECOMMANDÉ · -33%</span>
      </div>
      <div class="p1-plan-name">Annuel</div>
      <div class="p1-plan-price">119,90 € <span>/ an</span></div>
      <div class="p1-plan-equiv">9,99 € / mois économise 40 €</div>
    </div>
    <div class="p1-plan">
      <div class="p1-plan-name">Mensuel</div>
      <div class="p1-plan-price">14,99 € <span>/ mois</span></div>
    </div>
  </div>

  <h3 class="p1-sec-title">Ce que tu débloques</h3>
  {card_block(
    settings_row('infinite-outline', MINT, 'Posts illimités', sub='Pas de limite quotidienne') +
    settings_row('videocam-outline', '#E63946', 'Aller en live', sub='Diffusion Agora HD') +
    settings_row('cash-outline', '#FFA63D', 'Monétisation 1:1 / Channels / Packs') +
    settings_row('analytics-outline', '#11C6FF', 'Analytics avancés', sub='Audience, revenus, rétention') +
    settings_row('shield-checkmark-outline', '#9966FF', 'Badge vérifié + Support prioritaire') +
    settings_row('color-palette-outline', '#26C1A4', 'Personnalisation profil')
  )}

  <div class="p1-form" style="padding:0">
    {primary_cta("Commencer mon essai 7 jours")}
    <p class="p1-trial-note">Annulable avant la fin de l&rsquo;essai · pas de prélèvement</p>
  </div>
</main>'''


def screen_report_problem(th: dict) -> str:
    return f'''{settings_topbar('Signaler un problème')}
<main class="p1-main">
  <p class="p1-sec-desc">Aide-nous à améliorer Smuppy en signalant ce qui ne marche pas</p>

  {section_title("Type de problème")}
  <div class="p1-issue-grid">
    <button class="p1-issue p1-issue-on">
      <ion-icon name="bug-outline" style="font-size:22px;color:#E63946"></ion-icon>
      <span>Bug</span>
    </button>
    <button class="p1-issue">
      <ion-icon name="flame-outline" style="font-size:22px;color:#FFA63D"></ion-icon>
      <span>Crash</span>
    </button>
    <button class="p1-issue">
      <ion-icon name="card-outline" style="font-size:22px;color:#11C6FF"></ion-icon>
      <span>Paiement</span>
    </button>
    <button class="p1-issue">
      <ion-icon name="warning-outline" style="font-size:22px;color:#9966FF"></ion-icon>
      <span>Contenu</span>
    </button>
    <button class="p1-issue">
      <ion-icon name="speedometer-outline" style="font-size:22px;color:#26C1A4"></ion-icon>
      <span>Perf</span>
    </button>
    <button class="p1-issue">
      <ion-icon name="help-circle-outline" style="font-size:22px;color:#64748B"></ion-icon>
      <span>Autre</span>
    </button>
  </div>

  {section_title("Décris le problème")}
  <div class="p1-textarea">
    <span class="p1-textarea-val">Quand je tape sur le bouton « Réserver » de la session 1:1 de Sara Khan, l'app crash directement. Ça arrive systématiquement depuis ce matin.</span>
    <div class="p1-textarea-count">183 / 500</div>
  </div>

  {section_title("Captures d'écran (optionnel)")}
  <div class="p1-screenshots">
    <button class="p1-ss-add">
      <ion-icon name="add" style="font-size:24px;color:var(--mint)"></ion-icon>
      <span>Ajouter</span>
    </button>
    <div class="p1-ss-thumb">
      <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=200&h=400&fit=crop&q=80" alt=""/>
      <button class="p1-ss-x"><ion-icon name="close" style="font-size:12px;color:#fff"></ion-icon></button>
    </div>
  </div>

  <div class="p1-form">
    {primary_cta("Envoyer le rapport")}
  </div>
</main>'''


# ─── MESSAGES SCREENS ──────────────────────────────────────


def screen_messages(th: dict) -> str:
    """Messages list — DM/group threads with search."""
    msgs = [
        ('Marc Dubois', 'Marc D.', 'Tu es dispo demain pour la session ?', '14h', True, 2, True),
        ('Emma Chen', 'Emma C.', 'Merci pour le yoga flow ! ❤️', '12h', True, 0, False),
        ('Team Premium 💎', None, 'Sara : J\'ai envoyé le nouveau plan...', '11h', False, 0, False, True),
        ('Léa Martin', 'Léa M.', 'Photo', '10h45', False, 0, False),
        ('Thomas Roy', 'Thomas R.', 'Tu as vu ma nouvelle vidéo ?', 'Hier', False, 0, False),
        ('Coach Mike', 'Coach M.', 'Plan d\'entrainement S38 envoyé', 'Mer.', False, 0, False),
        ('Studio Vibe', None, 'Confirmation de réservation', '28/05', False, 0, False, True),
    ]
    rows = ''
    avatars = [
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80',
        'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80',
        'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=120&h=120&fit=crop&q=80',
        'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80',
        'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80',
        'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=120&h=120&fit=crop&q=80',
        'https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=120&h=120&fit=crop&q=80',
    ]
    for i, m in enumerate(msgs):
        name, _, preview, time, online, unread, urgent, *rest = m + (False,) * (8 - len(m))
        is_group = rest[0] if rest else False
        online_html = '<span class="p1-msg-online"></span>' if online else ''
        unread_html = f'<span class="p1-msg-unread">{unread}</span>' if unread else ''
        urgent_class = ' p1-msg-urgent' if urgent else ''
        group_badge = '<ion-icon name="people" style="font-size:11px;color:var(--mint);margin-right:4px;vertical-align:middle"></ion-icon>' if is_group else ''
        rows += f'''<div class="p1-msg-row{urgent_class}">
  <div class="p1-msg-avatar-wrap">
    <img src="{avatars[i]}" alt="" class="p1-msg-avatar"/>
    {online_html}
  </div>
  <div class="p1-msg-text">
    <div class="p1-msg-name-row">
      <span class="p1-msg-name">{group_badge}{name}</span>
      <span class="p1-msg-time">{time}</span>
    </div>
    <div class="p1-msg-preview">{preview}</div>
  </div>
  {unread_html}
</div>'''
    return f'''<header class="p1-topbar p1-topbar-msg">
  <h1 class="p1-msg-h1">Messages</h1>
  <button class="p1-msg-new-btn">
    <ion-icon name="create-outline" style="font-size:22px;color:var(--mint)"></ion-icon>
  </button>
</header>
<main class="p1-main p1-main-msg">
  <div class="p1-msg-search">
    <ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
    <span class="p1-msg-search-ph">Rechercher</span>
  </div>
  <div class="p1-msg-tabs">
    <span class="p1-msg-tab p1-msg-tab-on">Tous · 7</span>
    <span class="p1-msg-tab">DM</span>
    <span class="p1-msg-tab">Groupes</span>
    <span class="p1-msg-tab">Non lus · 2</span>
  </div>
  <div class="p1-msg-list">{rows}</div>
</main>'''


def screen_chat(th: dict) -> str:
    """Single conversation thread — Marc DM."""
    return f'''<header class="p1-topbar p1-topbar-chat">
  {back_button()}
  <div class="p1-chat-head">
    <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80" alt="" class="p1-chat-avatar"/>
    <div>
      <div class="p1-chat-name">Marc Dubois</div>
      <div class="p1-chat-status"><span class="p1-msg-online"></span>En ligne</div>
    </div>
  </div>
  <button class="p1-chat-more"><ion-icon name="ellipsis-vertical" style="font-size:18px;color:var(--text)"></ion-icon></button>
</header>
<main class="p1-main p1-main-chat">
  <div class="p1-chat-day">Aujourd&rsquo;hui</div>

  <div class="p1-bubble p1-bubble-them">
    <div class="p1-bubble-text">Salut Sara ! J&rsquo;ai vu ta dernière vidéo, super flow 🔥</div>
    <div class="p1-bubble-time">14:32</div>
  </div>
  <div class="p1-bubble p1-bubble-them">
    <div class="p1-bubble-text">Tu es dispo demain pour une session 1:1 ?</div>
    <div class="p1-bubble-time">14:33</div>
  </div>

  <div class="p1-bubble p1-bubble-me">
    <div class="p1-bubble-text">Merci ! 💚</div>
    <div class="p1-bubble-time">14:40 ✓✓</div>
  </div>
  <div class="p1-bubble p1-bubble-me">
    <div class="p1-bubble-text">Oui demain 16h ça marche pour toi ?</div>
    <div class="p1-bubble-time">14:41 ✓✓</div>
  </div>

  <!-- Shared post bubble -->
  <div class="p1-bubble p1-bubble-them p1-bubble-shared">
    <div class="p1-shared">
      <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400&h=400&fit=crop&q=80" alt=""/>
      <div class="p1-shared-meta">
        <div class="p1-shared-type">📍 Post de Sara Khan</div>
        <div class="p1-shared-title">Sunrise yoga · Mont-Royal</div>
      </div>
    </div>
    <div class="p1-bubble-time">14:42</div>
  </div>

  <div class="p1-bubble p1-bubble-them">
    <div class="p1-bubble-text">Parfait 16h !</div>
    <div class="p1-bubble-time">14:43</div>
  </div>

  <div class="p1-typing">
    <span></span><span></span><span></span>
    <span class="p1-typing-lbl">Marc écrit…</span>
  </div>
</main>
<footer class="p1-chat-input">
  <button class="p1-chat-input-btn"><ion-icon name="add-circle-outline" style="font-size:24px;color:var(--mint)"></ion-icon></button>
  <div class="p1-chat-input-field"><span class="p1-chat-input-ph">Écrire un message…</span></div>
  <button class="p1-chat-input-btn"><ion-icon name="mic-outline" style="font-size:22px;color:var(--sub)"></ion-icon></button>
  <button class="p1-chat-input-send"><ion-icon name="send" style="font-size:18px;color:#fff"></ion-icon></button>
</footer>'''


def screen_new_message(th: dict) -> str:
    """Search to start a new message."""
    contacts = [
        ('Emma Chen', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80', True),
        ('Marc Dubois', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80', True),
        ('Léa Martin', 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80', False),
        ('Thomas Roy', 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80', False),
        ('Coach Mike', 'https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=120&h=120&fit=crop&q=80', False),
    ]
    rows = ''
    for n, av, on in contacts:
        on_html = '<span class="p1-msg-online"></span>' if on else ''
        rows += f'''<div class="p1-contact-row">
  <div class="p1-msg-avatar-wrap">
    <img src="{av}" alt="" class="p1-msg-avatar"/>
    {on_html}
  </div>
  <div class="p1-contact-text"><div class="p1-contact-name">{n}</div></div>
</div>'''
    return f'''{settings_topbar('Nouveau message')}
<main class="p1-main p1-main-nomargin">
  <div class="p1-msg-search">
    <ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
    <span class="p1-msg-search-val">Sara</span>
  </div>

  <button class="p1-new-group">
    <span class="p1-new-group-ic"><ion-icon name="people" style="font-size:18px;color:var(--mint)"></ion-icon></span>
    <span>Créer un groupe</span>
    <ion-icon name="chevron-forward" class="p1-row-chev"></ion-icon>
  </button>

  <h3 class="p1-sec-title">Suggestions</h3>
  <div class="p1-contacts">{rows}</div>
</main>'''


def screen_create_group_chat(th: dict) -> str:
    """Step 2 of group : confirm name + members."""
    members = [
        ('Emma Chen', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80'),
        ('Marc Dubois', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80'),
        ('Léa Martin', 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80'),
        ('Thomas Roy', 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80'),
    ]
    pills = ''.join(f'<div class="p1-mb-pill"><img src="{av}"/><span>{n.split()[0]}</span><button class="p1-mb-pill-x"><ion-icon name="close" style="font-size:14px"></ion-icon></button></div>' for n, av in members)
    return f'''{settings_topbar('Nouveau groupe')}
<main class="p1-main">

  <div class="p1-group-avatar">
    <div class="p1-group-avatar-wrap">
      <ion-icon name="camera" style="font-size:32px;color:var(--mint)"></ion-icon>
    </div>
    <p class="p1-group-avatar-lbl">Photo du groupe</p>
  </div>

  <div class="p1-form">
    {input_field('Nom du groupe', value='Team Yoga Premium 💎', icon='people-outline')}
  </div>

  {section_title(f"Membres · {len(members) + 1}")}
  <div class="p1-mb-pills">
    <div class="p1-mb-pill p1-mb-pill-me"><span>Toi · admin</span></div>
    {pills}
  </div>
  <button class="p1-mb-add">
    <ion-icon name="add" style="font-size:18px;color:var(--mint)"></ion-icon>
    <span>Ajouter des membres</span>
  </button>

  <div class="p1-form" style="margin-top:18px">
    {primary_cta("Créer le groupe")}
  </div>
</main>'''


# ─── NOTIFICATIONS SCREENS ─────────────────────────────────


def screen_notifications(th: dict) -> str:
    notifs = [
        ('like', '#E63946', 'Emma Chen', 'a aimé ta photo', '5 min', False, 'photo'),
        ('person-add', '#11C6FF', 'Marc Dubois', 'est devenu un fan', '1 h', False, None),
        ('star', MINT, 'Léa Martin', 's\'est abonnée à ta chaîne', '2 h', False, None),
        ('chatbox', '#9966FF', 'Thomas Roy', 't\'a envoyé un message', '3 h', True, None),
        ('cash', '#FFA63D', 'Coach Mike', 't\'a envoyé 50 👊 Smups', '6 h', True, None),
        ('videocam', '#E63946', 'Sara Khan', 'est en live', 'Hier', True, None),
        ('person-add', '#11C6FF', 'Emma Chen', 'a demandé à être ton fan', 'Hier', True, None),
        ('walk', MINT, 'Activité', 'Tu as battu ton record · 5K à 4:30 / km', '2 jours', True, None),
    ]
    by_date = {'Aujourd&rsquo;hui': notifs[:5], 'Hier': notifs[5:7], 'Cette semaine': notifs[7:]}
    out = ''
    for date, group in by_date.items():
        out += f'<div class="p1-notif-day">{date}</div>'
        for icon, hue, name, action, time, read, _photo in group:
            read_cls = ' p1-notif-read' if read else ''
            photo_html = '<img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=80&h=80&fit=crop&q=80" alt="" class="p1-notif-photo"/>' if _photo else ''
            out += f'''<div class="p1-notif-row{read_cls}">
  <span class="p1-notif-ic" style="background:{hue}14;color:{hue}">
    <ion-icon name="{icon}" style="font-size:18px;color:{hue}"></ion-icon>
  </span>
  <div class="p1-notif-text">
    <span><b>{name}</b> {action}</span>
    <div class="p1-notif-time">{time}</div>
  </div>
  {photo_html}
</div>'''
    return f'''<header class="p1-topbar p1-topbar-msg">
  <h1 class="p1-msg-h1">Notifications</h1>
  <button class="p1-msg-new-btn">
    <ion-icon name="settings-outline" style="font-size:22px;color:var(--text)"></ion-icon>
  </button>
</header>
<main class="p1-main p1-main-msg">
  <div class="p1-msg-tabs">
    <span class="p1-msg-tab p1-msg-tab-on">Tous · 8</span>
    <span class="p1-msg-tab">Likes</span>
    <span class="p1-msg-tab">Fans</span>
    <span class="p1-msg-tab">Mentions</span>
  </div>
  <div class="p1-notif-list">{out}</div>
</main>'''


def screen_follow_requests(th: dict) -> str:
    reqs = [
        ('Emma Chen', '@emma · Yoga & Wellness · 1.2K fans', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80'),
        ('Marc Dubois', '@marc · CrossFit · 856 fans', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80'),
        ('Léa Martin', '@lea · Running coach · 543 fans', 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80'),
        ('Thomas Roy', '@thomas · Trail runner · 312 fans', 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80'),
    ]
    rows = ''
    for n, sub, av in reqs:
        rows += f'''<div class="p1-req-row">
  <img src="{av}" alt="" class="p1-req-avatar"/>
  <div class="p1-req-text">
    <div class="p1-req-name">{n}</div>
    <div class="p1-req-sub">{sub}</div>
  </div>
  <div class="p1-req-btns">
    <button class="p1-req-btn p1-req-btn-decline"><ion-icon name="close" style="font-size:18px"></ion-icon></button>
    <button class="p1-req-btn p1-req-btn-accept"><ion-icon name="checkmark" style="font-size:18px"></ion-icon></button>
  </div>
</div>'''
    return f'''{settings_topbar(f'Demandes · {len(reqs)}')}
<main class="p1-main">
  <p class="p1-sec-desc">Ces personnes veulent te suivre. Accepte pour qu'elles voient tes posts.</p>
  <div class="p1-req-list">{rows}</div>
</main>'''


# ─── PROFILE SUB-SCREENS ───────────────────────────────────


def screen_fans_list(th: dict) -> str:
    fans = [
        ('Emma Chen', '@emma', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80', 'fan', True),
        ('Marc Dubois', '@marc', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80', 'fan', False),
        ('Léa Martin', '@lea', 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80', 'unfan', False),
        ('Thomas Roy', '@thomas', 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80', 'fan', False),
        ('Coach Mike', '@coachmike', 'https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=120&h=120&fit=crop&q=80', 'fan', True),
        ('Studio Vibe', '@studiovibe', 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=120&h=120&fit=crop&q=80', 'fan', False),
    ]
    rows = ''
    for n, _at, av, btn, verified in fans:
        v = '<ion-icon name="checkmark-circle" style="font-size:13px;color:var(--mint);vertical-align:middle"></ion-icon>' if verified else ''
        if btn == 'fan':
            btn_html = '<button class="p1-fan-btn-on">Fan</button>'
        elif btn == 'unfan':
            btn_html = '<button class="p1-fan-btn">Devenir fan</button>'
        rows += f'''<div class="p1-fan-row">
  <img src="{av}" alt="" class="p1-fan-avatar"/>
  <div class="p1-fan-text">
    <div class="p1-fan-name">{n} {v}</div>
    <div class="p1-fan-sub">Coach &middot; 1.2K fans</div>
  </div>
  {btn_html}
</div>'''
    return f'''{settings_topbar("Sara Khan")}
<main class="p1-main p1-main-nomargin">
  <div class="p1-msg-tabs">
    <span class="p1-msg-tab p1-msg-tab-on">Fans · 24K</span>
    <span class="p1-msg-tab">Tracking · 412</span>
  </div>
  <div class="p1-msg-search">
    <ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
    <span class="p1-msg-search-ph">Rechercher un fan</span>
  </div>
  <div class="p1-fan-list">{rows}</div>
</main>'''


def screen_post_likers(th: dict) -> str:
    likers = [
        ('Emma Chen', '@emma', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80', True),
        ('Marc Dubois', '@marc', 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=face&q=80', False),
        ('Léa Martin', '@lea', 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80', True),
        ('Thomas Roy', '@thomas', 'https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80', False),
        ('Coach Mike', '@coachmike', 'https://images.unsplash.com/photo-1517999144091-3d9dca6d1e43?w=120&h=120&fit=crop&q=80', True),
        ('Studio Vibe', '@studiovibe', 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=120&h=120&fit=crop&q=80', False),
    ]
    rows = ''
    for n, _at, av, verified in likers:
        v = '<ion-icon name="checkmark-circle" style="font-size:13px;color:var(--mint);vertical-align:middle"></ion-icon>' if verified else ''
        rows += f'''<div class="p1-fan-row">
  <img src="{av}" alt="" class="p1-fan-avatar"/>
  <div class="p1-fan-text">
    <div class="p1-fan-name">{n} {v}</div>
  </div>
  <button class="p1-fan-btn">Devenir fan</button>
</div>'''
    return f'''{settings_topbar("412 likes")}
<main class="p1-main">
  <div class="p1-fan-list">{rows}</div>
</main>'''


def screen_player_abilities(th: dict) -> str:
    abilities = [
        ('Cardio', '#FF6347', 4.8, 32),
        ('Souplesse', '#9B59B6', 4.6, 28),
        ('Force', '#1E90FF', 4.2, 18),
        ('Coordination', MINT, 4.5, 24),
        ('Récup', '#11C6FF', 3.9, 14),
        ('Endurance', '#27AE60', 4.7, 22),
    ]
    rows = ''
    for label, hue, score, raters in abilities:
        pct = int((score / 5) * 100)
        rows += f'''<div class="p1-ab-row">
  <div class="p1-ab-head">
    <span class="p1-ab-name">{label}</span>
    <span class="p1-ab-score" style="color:{hue}">{score:.1f}<span class="p1-ab-of">/5</span></span>
  </div>
  <div class="p1-ab-bar">
    <div class="p1-ab-fill" style="width:{pct}%;background:linear-gradient(90deg, {hue}88, {hue})"></div>
  </div>
  <div class="p1-ab-meta">{raters} notes · {pct}%</div>
</div>'''
    return f'''{settings_topbar('Sara Khan · Player Card')}
<main class="p1-main">
  <div class="p1-pc-hero">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="" class="p1-pc-avatar"/>
    <div class="p1-pc-overall">
      <div class="p1-pc-overall-num">4.5</div>
      <div class="p1-pc-overall-lbl">Note globale<br/>· 138 votes</div>
    </div>
  </div>

  <h3 class="p1-sec-title">Capacités</h3>
  <div class="p1-ab-list">{rows}</div>

  <div class="p1-form" style="margin-top:14px">
    {primary_cta("Voir ma carte joueur")}
  </div>
</main>'''


def screen_player_career_card(th: dict) -> str:
    return f'''{settings_topbar('Player Card')}
<main class="p1-main">

  <div class="p1-cc-theme-pills">
    <span class="p1-cc-theme-pill p1-cc-theme-pill-on">Classic</span>
    <span class="p1-cc-theme-pill">Gold</span>
    <span class="p1-cc-theme-pill">Dark</span>
  </div>

  <div class="p1-cc-card">
    <div class="p1-cc-card-top">
      <span class="p1-cc-card-rating">4.5</span>
      <span class="p1-cc-card-pos">YGA</span>
    </div>
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop&q=80" alt="" class="p1-cc-card-photo"/>
    <div class="p1-cc-card-name">SARA KHAN</div>
    <div class="p1-cc-card-stats">
      <div><span class="p1-cc-stat-num">85</span><span class="p1-cc-stat-lbl">CAR</span></div>
      <div><span class="p1-cc-stat-num">92</span><span class="p1-cc-stat-lbl">SOU</span></div>
      <div><span class="p1-cc-stat-num">78</span><span class="p1-cc-stat-lbl">FOR</span></div>
      <div><span class="p1-cc-stat-num">88</span><span class="p1-cc-stat-lbl">COO</span></div>
      <div><span class="p1-cc-stat-num">75</span><span class="p1-cc-stat-lbl">REC</span></div>
      <div><span class="p1-cc-stat-num">94</span><span class="p1-cc-stat-lbl">END</span></div>
    </div>
  </div>

  <div class="p1-form">
    {primary_cta("Partager ma carte")}
    <button class="auth-link-row" style="margin-top:8px">Télécharger en PNG</button>
  </div>
</main>'''


def screen_my_ratings_settings(th: dict) -> str:
    abilities = [
        ('Cardio', '#FF6347', True),
        ('Souplesse', '#9B59B6', True),
        ('Force', '#1E90FF', True),
        ('Coordination', MINT, False),
        ('Récup', '#11C6FF', True),
        ('Endurance', '#27AE60', True),
    ]
    rows = ''
    for label, hue, on in abilities:
        rows += settings_row('analytics-outline', hue, label, control=toggle_on(on),
                             sub='Visible · 32 votes' if on else 'Caché · 28 votes')
    return f'''{settings_topbar('Confidentialité des notes')}
<main class="p1-main">
  <p class="p1-sec-desc">Choisis quelles capacités sont visibles sur ta carte joueur</p>

  {section_title("Capacités")}
  {card_block(rows)}

  <div class="p1-info-card">
    <ion-icon name="information-circle-outline" style="font-size:18px;color:var(--mint);flex-shrink:0"></ion-icon>
    <div>
      <div class="p1-info-title">Comment ça marche</div>
      <div class="p1-info-sub">Les visiteurs voient une note moyenne agrégée. Tu peux cacher des capacités sensibles, mais tu dois en garder au moins 3 visibles pour générer une carte joueur.</div>
    </div>
  </div>
</main>'''


SCREENS = {
    # SETTINGS top 8 most touched
    'p1_settings_v2': ('Réglages', screen_settings),
    'p1_edit_profile_v2': ('Modifier le profil', screen_edit_profile),
    'p1_notification_settings_v2': ('Notifications', screen_notification_settings),
    'p1_privacy_settings_v2': ('Confidentialité', screen_privacy_settings),
    'p1_security_settings_v2': ('Sécurité', screen_security_settings),
    'p1_manage_subscription_v2': ('Abonnements', screen_manage_subscription),
    'p1_upgrade_to_pro_v2': ('Upgrade', screen_upgrade_to_pro),
    'p1_report_problem_v2': ('Signaler un problème', screen_report_problem),
    # MESSAGES
    'p1_messages_v2': ('Messages', screen_messages),
    'p1_chat_v2': ('Chat', screen_chat),
    'p1_new_message_v2': ('Nouveau message', screen_new_message),
    'p1_create_group_chat_v2': ('Nouveau groupe', screen_create_group_chat),
    # NOTIFICATIONS
    'p1_notifications_v2': ('Notifications', screen_notifications),
    'p1_follow_requests_v2': ('Demandes', screen_follow_requests),
    # PROFILE SUBS
    'p1_fans_list_v2': ('Fans', screen_fans_list),
    'p1_post_likers_v2': ('Likes', screen_post_likers),
    'p1_player_abilities_v2': ('Player Card', screen_player_abilities),
    'p1_player_career_card_v2': ('Career Card', screen_player_career_card),
    'p1_my_ratings_settings_v2': ('Mes notes', screen_my_ratings_settings),
}


_P1_CSS = """
<style>
  /* ── P1 base ────────────────────────────────────────────────── */
  .p1-topbar { position:absolute; top:0; left:0; right:0; z-index:10;
    height:54px; padding:0 12px;
    display:flex; align-items:center; gap:8px;
    background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%);
    border-bottom:1px solid var(--border); }
  .p1-topbar-title { flex:1; text-align:center; font-size:16px;
    font-weight:800; margin:0; color:var(--text); letter-spacing:-.01em; }
  .p1-main { padding:66px 18px 32px; height:100%; overflow-y:auto; }
  .p1-main-nomargin { padding-left:0; padding-right:0; }
  .p1-main-nomargin > * { margin-left:18px; margin-right:18px; }
  .p1-main-nomargin .p1-fan-list,
  .p1-main-nomargin .p1-contacts,
  .p1-main-nomargin .p1-msg-search,
  .p1-main-nomargin .p1-msg-tabs { margin-left:0; margin-right:0; padding-left:18px; padding-right:18px; }

  /* Section title */
  .p1-sec-title { font-size:11px; font-weight:800;
    color:var(--sub); margin:18px 0 8px 4px;
    text-transform:uppercase; letter-spacing:.10em; }
  .p1-sec-desc { font-size:12.5px; font-weight:500; color:var(--sub);
    margin:0 0 8px; padding:0 4px; line-height:1.45; }

  /* Card block (groups rows) */
  .p1-card { background:var(--card);
    border:1px solid rgba(38,193,164,.12);
    border-radius:18px; padding:4px 4px;
    box-shadow:0 0 16px rgba(38,193,164,.05); }

  /* Settings row */
  .p1-row { display:flex; align-items:center; gap:12px;
    padding:10px 10px;
    border-bottom:1px solid var(--border); }
  .p1-row:last-child { border-bottom:none; }
  .p1-row-danger .p1-row-lbl { color:#EF4444; }
  .p1-row-ic { width:32px; height:32px; border-radius:10px;
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0; }
  .p1-row-text { flex:1; min-width:0; }
  .p1-row-lbl { font-size:14px; font-weight:600; color:var(--text); }
  .p1-row-sub { font-size:11.5px; font-weight:500; color:var(--sub); margin-top:2px; }
  .p1-row-val { font-size:13px; font-weight:600; color:var(--sub); margin-right:8px; }
  .p1-row-chev { font-size:18px; color:var(--sub); opacity:.55; }

  /* Toggle */
  .p1-tog { width:42px; height:24px; border-radius:999px;
    background:var(--input-border); position:relative;
    flex-shrink:0; transition:.2s; }
  .p1-tog-on { background:var(--mint); box-shadow:0 0 12px rgba(38,193,164,.45); }
  .p1-tog-knob { position:absolute; top:2px; left:2px; width:20px; height:20px;
    border-radius:999px; background:#fff; transition:.2s;
    box-shadow:0 2px 4px rgba(0,0,0,.2); }
  .p1-tog-on .p1-tog-knob { left:20px; }

  /* Settings entry — profile card */
  .p1-profile-card { display:flex; align-items:center; gap:14px;
    padding:14px 14px; margin:0 0 14px;
    background:var(--card); border:1.5px solid rgba(38,193,164,.30);
    border-radius:22px;
    box-shadow:0 0 24px rgba(38,193,164,.15),
               0 0 0 1px rgba(38,193,164,.10) inset; }
  .p1-profile-avatar { width:60px; height:60px; border-radius:999px; object-fit:cover;
    border:2px solid var(--mint);
    box-shadow:0 0 12px rgba(38,193,164,.30); }
  .p1-profile-info { flex:1; min-width:0; }
  .p1-profile-name { font-size:17px; font-weight:800; color:var(--text);
    letter-spacing:-.02em; display:flex; align-items:center; gap:6px; }
  .p1-profile-sub { font-size:12px; font-weight:500; color:var(--sub); margin:2px 0 6px; }
  .p1-profile-badge { display:inline-block; padding:3px 8px; border-radius:999px;
    background:rgba(38,193,164,.16); color:var(--mint);
    font-size:9.5px; font-weight:800; letter-spacing:.10em; }

  /* EditProfile — cover */
  .p1-cover-wrap { position:relative; margin:0 -18px 14px; aspect-ratio:21/9; overflow:hidden; }
  .p1-cover-img { width:100%; height:100%; object-fit:cover; }
  .p1-cover-edit { position:absolute; top:12px; right:12px;
    padding:7px 12px; border-radius:999px;
    background:rgba(0,0,0,.5); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    color:#fff; font-size:11px; font-weight:700; border:1px solid rgba(255,255,255,.20); }
  .p1-avatar-on-cover { position:absolute; bottom:-32px; left:18px; }
  .p1-avatar-on-cover img { width:72px; height:72px; border-radius:999px;
    border:3px solid var(--page); object-fit:cover; }
  .p1-avatar-edit { position:absolute; bottom:0; right:0;
    width:24px; height:24px; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    display:flex; align-items:center; justify-content:center;
    border:2px solid var(--page); }
  .p1-form { display:flex; flex-direction:column; padding-top:38px; }

  /* MFA hero card */
  .p1-mfa-card { display:flex; align-items:center; gap:14px;
    padding:16px; margin:0 0 14px;
    background:linear-gradient(135deg, rgba(38,193,164,.12), rgba(0,179,199,.04));
    border:1.5px solid rgba(38,193,164,.35);
    border-radius:22px;
    box-shadow:0 0 24px rgba(38,193,164,.18); }
  .p1-mfa-ic { width:60px; height:60px; border-radius:18px;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0; }
  .p1-mfa-text { flex:1; }
  .p1-mfa-title { font-size:15px; font-weight:800; color:var(--text); letter-spacing:-.01em; }
  .p1-mfa-status { font-size:12px; font-weight:700; color:var(--mint);
    display:flex; align-items:center; gap:6px; margin-top:2px; }
  .p1-mfa-dot { width:7px; height:7px; border-radius:999px; background:var(--mint);
    box-shadow:0 0 8px rgba(38,193,164,.6); }

  /* Subscription hero */
  .p1-sub-hero {
    background:linear-gradient(135deg, rgba(38,193,164,.18), rgba(0,179,199,.10));
    border:1.5px solid rgba(38,193,164,.45);
    border-radius:24px; padding:18px;
    box-shadow:0 0 32px rgba(38,193,164,.22);
    margin:0 0 14px; }
  .p1-sub-hero-row { display:flex; justify-content:space-between; align-items:flex-start; }
  .p1-sub-hero-label { font-size:10px; font-weight:800; color:var(--mint);
    letter-spacing:.14em; }
  .p1-sub-hero-name { font-size:18px; font-weight:800; color:var(--text);
    letter-spacing:-.02em; margin-top:4px; }
  .p1-sub-hero-badge { padding:4px 10px; border-radius:999px;
    background:rgba(38,193,164,.30); color:var(--mint);
    font-size:9.5px; font-weight:800; letter-spacing:.08em; }
  .p1-sub-hero-price { font-size:32px; font-weight:900; color:var(--text);
    letter-spacing:-.02em; margin:10px 0 4px; }
  .p1-sub-hero-price span { font-size:14px; font-weight:600; color:var(--sub); }
  .p1-sub-hero-renew { font-size:12px; font-weight:600; color:var(--sub);
    display:flex; align-items:center; gap:6px; }
  .p1-sub-hero-btn { width:100%; margin-top:14px; padding:11px;
    border:1.5px solid rgba(38,193,164,.45); border-radius:14px;
    background:rgba(38,193,164,.08); color:var(--mint);
    font-family:inherit; font-size:13px; font-weight:700; cursor:pointer;
    box-shadow:0 0 14px rgba(38,193,164,.12); }

  /* Upgrade hero + plans */
  .p1-pro-hero { display:flex; flex-direction:column; align-items:center;
    text-align:center; gap:8px; margin:8px 0 18px;
    filter:drop-shadow(0 0 24px rgba(38,193,164,.40)); }
  .p1-pro-title { font-size:22px; font-weight:800; margin:8px 0 4px;
    color:var(--text); letter-spacing:-.02em; }
  .p1-pro-sub { font-size:13px; font-weight:500; color:var(--sub); margin:0; }
  .p1-plans { display:flex; gap:10px; margin:0 0 18px; }
  .p1-plan { flex:1; padding:14px; border-radius:18px;
    background:var(--card); border:1px solid var(--input-border);
    position:relative; }
  .p1-plan-active { border-color:rgba(38,193,164,.45);
    background:rgba(38,193,164,.06);
    box-shadow:0 0 20px rgba(38,193,164,.20); }
  .p1-plan-badge { position:absolute; top:-9px; left:50%; transform:translateX(-50%);
    padding:3px 10px; border-radius:999px;
    background:linear-gradient(90deg, var(--mint-hi), var(--mint-deep));
    color:#fff; font-size:9px; font-weight:900; letter-spacing:.08em;
    white-space:nowrap; }
  .p1-plan-name { font-size:13px; font-weight:700; color:var(--sub); margin:6px 0 4px;
    text-transform:uppercase; letter-spacing:.06em; }
  .p1-plan-price { font-size:18px; font-weight:800; color:var(--text);
    letter-spacing:-.02em; }
  .p1-plan-price span { font-size:11px; font-weight:600; color:var(--sub); }
  .p1-plan-equiv { font-size:10.5px; font-weight:600; color:var(--mint); margin-top:4px; }
  .p1-trial-note { font-size:11px; text-align:center; color:var(--sub);
    margin:8px 0 0; font-weight:500; }

  /* ReportProblem — issue grid */
  .p1-issue-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:8px;
    margin:0 0 14px; }
  .p1-issue { display:flex; flex-direction:column; align-items:center;
    gap:5px; padding:14px 8px; border-radius:14px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; font-size:12px;
    font-weight:700; color:var(--text); }
  .p1-issue-on { border-color:rgba(38,193,164,.45); background:rgba(38,193,164,.06);
    box-shadow:0 0 14px rgba(38,193,164,.20); }
  .p1-textarea { background:var(--input-bg); border:1.5px solid var(--input-border);
    border-radius:14px; padding:14px; min-height:120px;
    margin:0 0 14px; position:relative; }
  .p1-textarea-val { font-size:13.5px; line-height:1.45; color:var(--text);
    font-weight:500; }
  .p1-textarea-count { position:absolute; bottom:8px; right:12px;
    font-size:11px; font-weight:600; color:var(--sub); }
  .p1-screenshots { display:flex; gap:8px; margin:0 0 14px; }
  .p1-ss-add { width:72px; height:72px; border-radius:14px;
    background:var(--input-bg); border:1.5px dashed rgba(38,193,164,.45);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    gap:2px; cursor:pointer; font-family:inherit; font-size:10px; font-weight:700;
    color:var(--mint); }
  .p1-ss-thumb { position:relative; width:72px; height:72px;
    border-radius:14px; overflow:hidden; }
  .p1-ss-thumb img { width:100%; height:100%; object-fit:cover; }
  .p1-ss-x { position:absolute; top:4px; right:4px;
    width:20px; height:20px; border-radius:999px;
    background:rgba(0,0,0,.6); border:none;
    display:flex; align-items:center; justify-content:center; cursor:pointer; }

  /* Messages list */
  .p1-topbar-msg { padding-left:24px; padding-right:14px;
    justify-content:space-between; }
  .p1-msg-h1 { flex:1; text-align:left; font-size:24px; font-weight:900;
    margin:0; color:var(--text); letter-spacing:-.02em; }
  .p1-msg-new-btn { width:40px; height:40px; border:none; background:transparent;
    border-radius:999px; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .p1-main-msg { padding:60px 0 32px; }
  .p1-msg-search { display:flex; align-items:center; gap:8px;
    margin:6px 18px 12px; padding:10px 14px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    border-radius:14px; }
  .p1-msg-search-ph { font-size:14px; font-weight:500; color:var(--sub); opacity:.7; }
  .p1-msg-search-val { font-size:14px; font-weight:600; color:var(--text); }
  .p1-msg-tabs { display:flex; gap:6px; padding:0 18px; margin:0 0 12px;
    overflow-x:auto; scrollbar-width:none; }
  .p1-msg-tabs::-webkit-scrollbar { display:none; }
  .p1-msg-tab { padding:8px 14px; border-radius:999px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    font-size:12.5px; font-weight:700; color:var(--sub); white-space:nowrap; cursor:pointer; }
  .p1-msg-tab-on { background:var(--card); color:var(--mint);
    border-color:rgba(38,193,164,.45);
    box-shadow:0 0 14px rgba(38,193,164,.25); }
  .p1-msg-list { display:flex; flex-direction:column; }
  .p1-msg-row { display:flex; align-items:center; gap:12px;
    padding:12px 18px; cursor:pointer; transition:.15s; }
  .p1-msg-row:hover { background:rgba(38,193,164,.04); }
  .p1-msg-avatar-wrap { position:relative; flex-shrink:0; }
  .p1-msg-avatar { width:48px; height:48px; border-radius:999px; object-fit:cover; }
  .p1-msg-online { position:absolute; bottom:0; right:0;
    width:13px; height:13px; border-radius:999px; background:var(--mint);
    border:2.5px solid var(--page);
    box-shadow:0 0 6px rgba(38,193,164,.45); }
  .p1-msg-text { flex:1; min-width:0; }
  .p1-msg-name-row { display:flex; justify-content:space-between; gap:8px; }
  .p1-msg-name { font-size:14px; font-weight:700; color:var(--text);
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  .p1-msg-time { font-size:11px; font-weight:600; color:var(--sub); flex-shrink:0; }
  .p1-msg-preview { font-size:12.5px; font-weight:500; color:var(--sub);
    margin-top:2px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
    max-width:240px; }
  .p1-msg-unread { background:var(--mint); color:#fff;
    width:22px; height:22px; border-radius:999px;
    display:inline-flex; align-items:center; justify-content:center;
    font-size:11px; font-weight:800;
    box-shadow:0 0 10px rgba(38,193,164,.40); flex-shrink:0; }
  .p1-msg-urgent { background:rgba(38,193,164,.04); border-left:3px solid var(--mint); }

  /* Chat */
  .p1-topbar-chat { padding-left:8px; padding-right:14px; gap:10px; }
  .p1-chat-head { display:flex; align-items:center; gap:10px; flex:1; }
  .p1-chat-avatar { width:38px; height:38px; border-radius:999px; object-fit:cover; }
  .p1-chat-name { font-size:14.5px; font-weight:800; color:var(--text); }
  .p1-chat-status { font-size:11px; font-weight:600; color:var(--mint);
    display:flex; align-items:center; gap:6px; margin-top:1px; }
  .p1-chat-more { width:40px; height:40px; border:none; background:transparent;
    border-radius:999px; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .p1-main-chat { padding:60px 18px 86px; }
  .p1-chat-day { text-align:center; font-size:11px; font-weight:700; color:var(--sub);
    margin:12px 0 14px; }
  .p1-bubble { max-width:78%; margin-bottom:8px; padding:10px 14px;
    border-radius:18px; position:relative;
    box-shadow:0 1px 4px rgba(0,0,0,.10); }
  .p1-bubble-them { background:var(--card); border:1px solid var(--input-border);
    align-self:flex-start; }
  .p1-bubble-me { background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    color:#fff; margin-left:auto; }
  .p1-bubble-me .p1-bubble-text { color:#fff; }
  .p1-bubble-text { font-size:14px; font-weight:500; color:var(--text); line-height:1.4; }
  .p1-bubble-time { font-size:10px; font-weight:600; color:var(--sub); margin-top:3px; }
  .p1-bubble-me .p1-bubble-time { color:rgba(255,255,255,.85); }
  .p1-bubble-shared { padding:6px; }
  .p1-shared { background:var(--input-bg); border-radius:14px; overflow:hidden;
    margin-bottom:4px; }
  .p1-shared img { width:100%; aspect-ratio:1/1; object-fit:cover; }
  .p1-shared-meta { padding:8px 10px; }
  .p1-shared-type { font-size:10px; font-weight:700; color:var(--mint); margin-bottom:2px; }
  .p1-shared-title { font-size:13px; font-weight:700; color:var(--text); }
  .p1-typing { display:flex; align-items:center; gap:4px; padding:6px 14px;
    background:var(--card); border:1px solid var(--input-border);
    border-radius:18px; width:fit-content; margin-bottom:6px; }
  .p1-typing span:not(.p1-typing-lbl) {
    width:6px; height:6px; border-radius:999px; background:var(--sub);
    animation:typing 1.4s infinite ease-in-out; }
  .p1-typing span:nth-child(2):not(.p1-typing-lbl) { animation-delay:.2s; }
  .p1-typing span:nth-child(3):not(.p1-typing-lbl) { animation-delay:.4s; }
  @keyframes typing { 0%, 60%, 100% { opacity:.3; transform:translateY(0); } 30% { opacity:1; transform:translateY(-2px); } }
  .p1-typing-lbl { font-size:11px; font-weight:600; color:var(--sub); margin-left:4px; }

  /* Chat input */
  .p1-chat-input { position:absolute; bottom:0; left:0; right:0;
    display:flex; align-items:center; gap:8px;
    padding:10px 12px 14px;
    background:var(--card);
    border-top:1px solid var(--border); }
  .p1-chat-input-btn { width:36px; height:36px; border:none; background:transparent;
    cursor:pointer;
    display:flex; align-items:center; justify-content:center; flex-shrink:0; }
  .p1-chat-input-field { flex:1; padding:10px 14px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    border-radius:18px; min-height:40px;
    display:flex; align-items:center; }
  .p1-chat-input-ph { font-size:13.5px; font-weight:500; color:var(--sub); opacity:.7; }
  .p1-chat-input-send { width:36px; height:36px; border:none; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    color:#fff; cursor:pointer; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 4px 12px rgba(38,193,164,.40); }

  /* NewMessage — new group button */
  .p1-new-group { display:flex; align-items:center; gap:12px;
    width:calc(100% - 36px); margin:14px 18px 14px;
    padding:14px 16px; border-radius:16px;
    background:rgba(38,193,164,.08); border:1.5px solid rgba(38,193,164,.30);
    color:var(--text); font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; text-align:left; }
  .p1-new-group-ic { width:36px; height:36px; border-radius:11px;
    background:rgba(38,193,164,.16);
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0; }
  .p1-contacts { display:flex; flex-direction:column; }
  .p1-contact-row { display:flex; align-items:center; gap:12px;
    padding:11px 18px; cursor:pointer; }
  .p1-contact-name { font-size:14px; font-weight:600; color:var(--text); }

  /* CreateGroupChat */
  .p1-group-avatar { display:flex; flex-direction:column; align-items:center; gap:8px;
    margin:6px 0 18px; }
  .p1-group-avatar-wrap { width:96px; height:96px; border-radius:24px;
    background:rgba(38,193,164,.10);
    border:2px dashed rgba(38,193,164,.40);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 24px rgba(38,193,164,.25); }
  .p1-group-avatar-lbl { font-size:12px; font-weight:700; color:var(--mint); }
  .p1-mb-pills { display:flex; flex-wrap:wrap; gap:6px; margin:0 0 10px; }
  .p1-mb-pill { display:flex; align-items:center; gap:5px;
    padding:5px 6px 5px 5px; border-radius:999px;
    background:var(--card); border:1px solid var(--input-border);
    font-size:12px; font-weight:700; color:var(--text); }
  .p1-mb-pill-me { background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep)); color:#fff;
    border:none; padding:6px 12px; box-shadow:0 0 10px rgba(38,193,164,.35); }
  .p1-mb-pill img { width:24px; height:24px; border-radius:999px; object-fit:cover; }
  .p1-mb-pill-x { width:18px; height:18px; border-radius:999px; border:none;
    background:rgba(255,255,255,.05); display:flex; align-items:center; justify-content:center;
    cursor:pointer; color:var(--sub); }
  .p1-mb-add { display:inline-flex; align-items:center; gap:6px;
    padding:8px 14px; border-radius:999px;
    background:rgba(38,193,164,.08); border:1.5px dashed rgba(38,193,164,.45);
    color:var(--mint); font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; }

  /* Notifications */
  .p1-notif-day { font-size:12px; font-weight:800; color:var(--sub);
    text-transform:uppercase; letter-spacing:.08em;
    padding:14px 18px 8px; }
  .p1-notif-row { display:flex; align-items:center; gap:12px;
    padding:12px 18px; cursor:pointer;
    border-left:3px solid var(--mint); }
  .p1-notif-read { border-left-color:transparent; opacity:.6; }
  .p1-notif-ic { width:36px; height:36px; border-radius:11px;
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0; }
  .p1-notif-text { flex:1; min-width:0; }
  .p1-notif-text span { font-size:13px; font-weight:500; color:var(--text); }
  .p1-notif-text b { font-weight:800; }
  .p1-notif-time { font-size:11px; font-weight:600; color:var(--sub); margin-top:2px; }
  .p1-notif-photo { width:42px; height:42px; border-radius:12px;
    object-fit:cover; flex-shrink:0; }

  /* FollowRequests */
  .p1-req-row { display:flex; align-items:center; gap:12px;
    padding:14px 14px; border-radius:18px;
    background:var(--card); border:1px solid var(--input-border);
    margin-bottom:8px; }
  .p1-req-avatar { width:50px; height:50px; border-radius:999px; object-fit:cover;
    flex-shrink:0; }
  .p1-req-text { flex:1; min-width:0; }
  .p1-req-name { font-size:14px; font-weight:700; color:var(--text); }
  .p1-req-sub { font-size:11.5px; font-weight:500; color:var(--sub); margin-top:2px; }
  .p1-req-btns { display:flex; gap:6px; flex-shrink:0; }
  .p1-req-btn { width:38px; height:38px; border:none; border-radius:999px;
    cursor:pointer; display:flex; align-items:center; justify-content:center; }
  .p1-req-btn-decline { background:var(--input-bg); color:var(--sub);
    border:1px solid var(--input-border); }
  .p1-req-btn-accept { background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep));
    color:#fff; box-shadow:0 4px 12px rgba(38,193,164,.40); }

  /* FansList — fan row */
  .p1-fan-list { display:flex; flex-direction:column; padding:0 18px; }
  .p1-fan-row { display:flex; align-items:center; gap:12px;
    padding:10px 0; border-bottom:1px solid var(--border); }
  .p1-fan-avatar { width:48px; height:48px; border-radius:999px; object-fit:cover;
    flex-shrink:0; }
  .p1-fan-text { flex:1; min-width:0; }
  .p1-fan-name { font-size:14px; font-weight:700; color:var(--text);
    display:flex; align-items:center; gap:4px; }
  .p1-fan-sub { font-size:11.5px; font-weight:500; color:var(--sub); margin-top:1px; }
  .p1-fan-btn { padding:7px 14px; border:1.5px solid rgba(38,193,164,.45);
    border-radius:999px; background:rgba(38,193,164,.06);
    color:var(--mint); font-family:inherit; font-size:12.5px; font-weight:700;
    cursor:pointer;
    box-shadow:0 0 12px rgba(38,193,164,.15); }
  .p1-fan-btn-on { padding:7px 14px; border-radius:999px;
    background:rgba(38,193,164,.14); border:1.5px solid rgba(38,193,164,.40);
    color:var(--mint); font-family:inherit; font-size:12.5px; font-weight:700;
    box-shadow:0 0 12px rgba(38,193,164,.20); }

  /* PlayerCard hero */
  .p1-pc-hero { display:flex; align-items:center; gap:16px;
    padding:14px; background:var(--card);
    border:1.5px solid rgba(38,193,164,.30); border-radius:22px;
    box-shadow:0 0 24px rgba(38,193,164,.15);
    margin-bottom:16px; }
  .p1-pc-avatar { width:80px; height:80px; border-radius:999px; object-fit:cover;
    border:3px solid var(--mint);
    box-shadow:0 0 14px rgba(38,193,164,.35); }
  .p1-pc-overall { flex:1; }
  .p1-pc-overall-num { font-size:38px; font-weight:900; color:var(--mint);
    line-height:1; letter-spacing:-.04em;
    text-shadow:0 0 16px rgba(38,193,164,.30); }
  .p1-pc-overall-lbl { font-size:11px; font-weight:600; color:var(--sub);
    margin-top:6px; line-height:1.35; }

  /* Abilities list */
  .p1-ab-list { display:flex; flex-direction:column; gap:12px; margin:0 0 14px; }
  .p1-ab-row { background:var(--card); border:1px solid var(--input-border);
    border-radius:14px; padding:12px 14px; }
  .p1-ab-head { display:flex; justify-content:space-between; align-items:baseline;
    margin-bottom:6px; }
  .p1-ab-name { font-size:13px; font-weight:700; color:var(--text); }
  .p1-ab-score { font-size:18px; font-weight:800; letter-spacing:-.02em; }
  .p1-ab-of { font-size:12px; font-weight:600; color:var(--sub); margin-left:2px; }
  .p1-ab-bar { height:6px; border-radius:999px; background:var(--input-border);
    overflow:hidden; }
  .p1-ab-fill { height:100%; border-radius:999px;
    box-shadow:0 0 6px currentColor; }
  .p1-ab-meta { font-size:10.5px; font-weight:600; color:var(--sub); margin-top:4px; }

  /* CareerCard themes */
  .p1-cc-theme-pills { display:flex; gap:6px; margin:0 0 14px;
    justify-content:center; }
  .p1-cc-theme-pill { padding:7px 14px; border-radius:999px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    font-size:12px; font-weight:700; color:var(--sub); cursor:pointer; }
  .p1-cc-theme-pill-on { background:var(--card); color:var(--mint);
    border-color:rgba(38,193,164,.45);
    box-shadow:0 0 14px rgba(38,193,164,.25); }

  /* Career card */
  .p1-cc-card { position:relative; width:240px; aspect-ratio:5/7;
    background:linear-gradient(160deg, #1A1A22 0%, #0A0A12 100%);
    border-radius:18px; padding:14px;
    border:2px solid rgba(38,193,164,.40);
    box-shadow:0 0 40px rgba(38,193,164,.20),
               0 12px 32px rgba(0,0,0,.45);
    margin:0 auto 18px; }
  .p1-cc-card-top { display:flex; justify-content:space-between; }
  .p1-cc-card-rating { font-size:32px; font-weight:900; color:var(--mint);
    line-height:1; letter-spacing:-.02em;
    text-shadow:0 0 12px rgba(38,193,164,.6); }
  .p1-cc-card-pos { font-size:11px; font-weight:800; color:var(--mint);
    letter-spacing:.10em; align-self:center;
    padding:3px 10px; border-radius:999px;
    background:rgba(38,193,164,.15); }
  .p1-cc-card-photo { width:120px; height:120px; border-radius:999px;
    object-fit:cover; margin:8px auto 6px; display:block;
    border:2px solid var(--mint); }
  .p1-cc-card-name { text-align:center; font-size:14px; font-weight:900;
    color:#fff; letter-spacing:.04em; margin-bottom:8px; }
  .p1-cc-card-stats { display:grid; grid-template-columns:repeat(3, 1fr);
    gap:3px 8px; padding:0 6px; }
  .p1-cc-card-stats > div { display:flex; gap:5px; align-items:baseline; }
  .p1-cc-stat-num { font-size:13px; font-weight:900; color:#fff; }
  .p1-cc-stat-lbl { font-size:9px; font-weight:800; color:var(--mint); letter-spacing:.04em; }

  /* Info card */
  .p1-info-card { display:flex; gap:10px;
    padding:12px 14px; border-radius:14px;
    background:rgba(38,193,164,.06);
    border:1px solid rgba(38,193,164,.25);
    margin-top:14px; }
  .p1-info-title { font-size:12.5px; font-weight:800; color:var(--mint); margin-bottom:3px; }
  .p1-info-sub { font-size:11.5px; font-weight:500; color:var(--sub); line-height:1.4; }

  /* Correction banner */
  .p1-correction-banner { display:flex; gap:10px;
    padding:12px 14px; margin-top:14px;
    background:rgba(38,193,164,.08);
    border:1px solid rgba(38,193,164,.30);
    border-radius:14px;
    box-shadow:0 0 14px rgba(38,193,164,.10); }
  .p1-banner-title { font-size:12.5px; font-weight:800; color:var(--mint); }
  .p1-banner-sub { font-size:11px; font-weight:500; color:var(--sub); margin-top:2px; }
</style>
"""


def build(key: str, dark: bool) -> str:
    th = theme(dark)
    title, fn = SCREENS[key]
    body = fn(th)
    auth_full = auth_build_fn('auth_welcome_v2', dark)
    head_end = auth_full.index('</style>') + len('</style>')
    head = auth_full[:head_end].replace('Smuppy V2 — Welcome', f'Smuppy V2 — {title}')
    return head + _P1_CSS + '\n</head><body>\n' + body + '\n</body></html>'


def write_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for key in SCREENS.keys():
        for dark in (True, False):
            theme_str = 'dark' if dark else 'light'
            screen_dir = OUT_DIR / f'{key}_{theme_str}'
            screen_dir.mkdir(parents=True, exist_ok=True)
            (screen_dir / 'code.html').write_text(build(key, dark))
            n += 1
    print(f'  built {n} P1 maquettes')


if __name__ == '__main__':
    write_all()
