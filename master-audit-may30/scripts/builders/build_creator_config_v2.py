#!/usr/bin/env python3
"""
build_creator_config_v2.py — Creator-tooling CONFIG screens (v2 rebuild, iteration 2).

Founder corrections 2026-05-28 13:00 applied:
  1. **NO bottomnav on subscreens** (V2 brand-rules #10 — back-arrow only).
     Reverted my prior misinterpretation of his 2026-05-27 20:28 flag.
  2. **NO free trial on Channel** ("pas d'essai gratuit pour pas de complexite").
  3. **Success popup** on save (V2 BottomSheet-style sheet at bottom).
  4. **Confirm-leave popup** if user taps back with unsaved changes.

3 screens x light/dark = 6 files:
  creator_channel_setup_*   - cover hero / name / tagline / monthly price / perks
  creator_1on1_setup_*      - durations {15/30/45/60} toggle+price / days / hours / subject
  creator_packages_setup_*  - existing packs list / pack editor (free services) / prices

V2 foundation (tokens.md, brand-rules.md):
  - mint solid #33A089 (95% UI), mint-hi #5BB8A6 (dark accent)
  - Plus Jakarta Sans only (weights 400/500/600/700/800)
  - Dark = pure #000000 (never navy)
  - Subscreens: arrow_back only, NO bottom nav (rule #10)

Regenerate: python3 build_creator_config_v2.py
"""
from pathlib import Path

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
MINT = '#33A089'
MINT_HI = '#5BB8A6'
MINT_DEEP = '#176A5A'
GRAD_A = '#41AD96'
GRAD_B = '#2C95A0'


def theme(dark: bool) -> dict:
    if dark:
        return dict(
            page='#000000', card='#14141A', card_inner='#0F0F14',
            text='#F1F4F6', sub='#8B8B95', section='#6B6B75',
            header='rgba(10,10,12,0.85)', border='rgba(255,255,255,0.06)',
            input_bg='rgba(255,255,255,0.04)', input_border='rgba(255,255,255,0.10)',
            chev='#5A5A66', back='#F1F4F6', html='dark',
            tog_off='#2E2E38', dim_shadow='0.5',
        )
    return dict(
        page='#F6F8FA', card='#FFFFFF', card_inner='#FAFBFC',
        text='#0F172A', sub='#64748B', section='#94A3B8',
        header='rgba(255,255,255,0.92)', border='#EEF1F4',
        input_bg='#FFFFFF', input_border='#E5E9EB',
        chev='#CBD5E1', back='#0E1116', html='light',
        tog_off='#E2E8F0', dim_shadow='0.06',
    )


# Material Symbols name → Ionicons (canonical Smuppy set) mapping
# When fill=1 we use the filled variant ("-sharp" or no-outline suffix)
IONIC_MAP = {
    'photo_camera':        ('camera-outline', 'camera'),
    'camera':              ('camera-outline', 'camera'),
    'badge':               ('id-card-outline', 'id-card'),
    'format_quote':        ('chatbox-ellipses-outline', 'chatbox-ellipses'),
    'euro':                ('cash-outline', 'cash'),
    'card_giftcard':       ('gift-outline', 'gift'),
    'check_circle':        ('checkmark-circle-outline', 'checkmark-circle'),
    'add':                 ('add', 'add'),
    'close':               ('close', 'close'),
    'add_circle':          ('add-circle-outline', 'add-circle'),
    'video_camera_front':  ('videocam-outline', 'videocam'),
    'videocam':            ('videocam-outline', 'videocam'),
    'schedule':            ('time-outline', 'time'),
    'event':               ('calendar-outline', 'calendar'),
    'do_not_disturb_on':   ('ban-outline', 'ban'),
    'inventory_2':         ('cube-outline', 'cube'),
    'rocket_launch':       ('rocket-outline', 'rocket'),
    'edit_note':           ('create-outline', 'create'),
    'timer':               ('timer-outline', 'timer'),
    'workspace_premium':   ('ribbon-outline', 'ribbon'),
    'chevron_right':       ('chevron-forward', 'chevron-forward'),
    'chevron_left':        ('chevron-back', 'chevron-back'),
    'logout':              ('log-out-outline', 'log-out'),
    'delete':              ('trash-outline', 'trash'),
    'edit':                ('pencil-outline', 'pencil'),
    'arrow_back':          ('arrow-back', 'arrow-back'),
    'verified':            ('checkmark-circle', 'checkmark-circle'),
    'star':                ('star-outline', 'star'),
    'share':               ('share-social-outline', 'share-social'),
    'home':                ('home-outline', 'home'),
    'forum':               ('chatbubbles-outline', 'chatbubbles'),
    'person':              ('person-outline', 'person'),
    'movie':               ('film-outline', 'film'),
}


def ms(name: str, size: int = 20, color: str = 'currentColor', fill: int = 0, wght: int = 400) -> str:
    """Render an icon. Uses canonical Ionicons set when available, falls back to Material Symbols.
    `fill=1` returns the filled variant; `fill=0` returns the outline variant."""
    if name in IONIC_MAP:
        outline_name, fill_name = IONIC_MAP[name]
        ionic_name = fill_name if fill else outline_name
        return (f'<ion-icon name="{ionic_name}" '
                f'style="font-size:{size}px;color:{color};vertical-align:middle"></ion-icon>')
    # fallback to Material Symbols for unmapped icons (e.g. strikethrough_s)
    return (f'<span class="material-symbols-outlined" '
            f'style="font-size:{size}px;color:{color};'
            f"font-variation-settings:'FILL' {fill},'wght' {wght},'GRAD' 0,'opsz' 24\">{name}</span>")


def chip(icon: str, hue: str, size: int = 34) -> str:
    icon_size = 19 if size == 34 else 17
    # Punchy hue-matched halo glow (founder ref may28 21:55 — wow effect)
    return (f'<span class="ico" style="width:{size}px;height:{size}px;background:{hue}1A;color:{hue};'
            f'box-shadow:0 0 18px {hue}55, 0 0 0 1px {hue}40 inset;'
            f'filter:drop-shadow(0 0 8px {hue}80);">'
            f'{ms(icon, icon_size, hue, wght=500)}</span>')


def toggle(on: bool) -> str:
    return f'<span class="tog{" on" if on else ""}"><span class="knob"></span></span>'


def row(label: str, control: str, icon: str = None, hue: str = MINT, sub: str = None, last: bool = False) -> str:
    sep = '' if last else 'border-bottom:1px solid var(--border)'
    ico_html = chip(icon, hue) if icon else ''
    sub_html = f'<span class="lbl-sub">{sub}</span>' if sub else ''
    lbl_block = f'<div class="lbl-block"><span class="lbl">{label}</span>{sub_html}</div>'
    return (f'<div class="row" style="{sep}">'
            f'{ico_html}{lbl_block}<span class="ctrl">{control}</span></div>')


def section(title: str, body: str) -> str:
    return f'<h3 class="sec">{title}</h3><div class="card">{body}</div>'


def input_value(value: str, placeholder: bool = False, mint: bool = False) -> str:
    cls = 'val'
    if placeholder:
        cls += ' ph'
    if mint:
        cls += ' mint'
    return f'<span class="{cls}">{value}</span>'


def chev() -> str:
    return f'<span class="material-symbols-outlined" style="font-size:20px;color:var(--chev)">chevron_right</span>'


def benefit_row(text: str, last: bool = False) -> str:
    sep = '' if last else 'border-bottom:1px solid var(--border)'
    return (f'<div class="ben" style="{sep}">'
            f'<span class="ben-check">{ms("check_circle", 18, MINT, fill=1)}</span>'
            f'<span class="ben-text">{text}</span>'
            f'<button class="ben-remove" aria-label="Remove">{ms("close", 18, "currentColor")}</button>'
            f'</div>')


def add_row(label: str) -> str:
    return (f'<button class="add-row">'
            f'{ms("add_circle", 20, MINT, fill=1)}<span>{label}</span></button>')


def topbar(title: str) -> str:
    return f'''<header class="topbar">
  <button class="back" aria-label="Retour">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--back)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <h1>{title}</h1>
  <span style="width:40px"></span>
</header>'''


def bottomnav_canonical(active: str = 'home') -> str:
    """Single source of truth — uses canonical_bnav from canonical_bnav.py with EXACT SVG paths
    extracted from v2_canonical_home_feed Stitch dump (founder validated yesterday)."""
    import sys
    sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
    from canonical_bnav import canonical_bnav
    # Re-map 'play' -> 'peaks' to match canonical key naming
    mapped = 'peaks' if active == 'play' else active
    return canonical_bnav(mapped)


def msg_icon_canonical(size: int = 18, color: str = '#33A089') -> str:
    """Canonical chat-bubble message icon (same MSG_PATH as bnav Messages slot)."""
    import sys
    sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
    from canonical_bnav import canonical_msg_icon
    return canonical_msg_icon(size, color)


def _legacy_bottomnav_DEPRECATED() -> str:
    """Canonical Smuppy bottom nav · 5 slots (Home / Peaks / Create / Chat / Profile)."""
    return '''<nav class="bnav-canonical">
  <button class="bnav-item" aria-label="Home"><ion-icon name="home-outline" style="font-size:24px"></ion-icon></button>
  <button class="bnav-item" aria-label="Peaks"><ion-icon name="film-outline" style="font-size:24px"></ion-icon></button>
  <button class="bnav-create" aria-label="Create"><ion-icon name="add" style="font-size:28px;color:#fff"></ion-icon></button>
  <button class="bnav-item" aria-label="Chat"><ion-icon name="chatbubble-outline" style="font-size:24px"></ion-icon></button>
  <button class="bnav-item bnav-profile" aria-label="Profile"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&q=80" alt=""/></button>
</nav>'''


def topbar_view() -> str:
    """Fan-facing topbar: × close · Smuppy mint wordmark · share."""
    return f'''<header class="topbar topbar-view">
  <button class="back" aria-label="Fermer">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--back)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
  </button>
  <span class="topbar-logo">Smuppy</span>
  <button class="back" aria-label="Partager">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--back)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
  </button>
</header>'''


def bottomnav() -> str:
    # Inline SVG icons (24x24 viewBox) — bulletproof for headless render
    icon_color = '#9CA3AF'
    svg = lambda d: f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{icon_color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
    icons = {
        'home': svg('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20a1 1 0 0 0 1 1h4v-6h4v6h4a1 1 0 0 0 1-1V9.5"/>'),
        'peaks': svg('<rect x="3" y="4" width="18" height="16" rx="3"/><path d="M3 8h18M7 4v4M11 4v4M15 4v4M19 4v4M7 20v-4M11 20v-4M15 20v-4M19 20v-4"/>'),
        'messages': svg('<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'),
        'profile': svg('<circle cx="12" cy="8" r="4"/><path d="M4 20c0-4.4 3.6-8 8-8s8 3.6 8 8"/>'),
    }
    return (
        f'<nav class="bottomnav">'
        f'<button class="nav-item" aria-label="Home">{icons["home"]}</button>'
        f'<button class="nav-item" aria-label="Peaks">{icons["peaks"]}</button>'
        f'<button class="nav-create" aria-label="Create">'
        f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
        f'</button>'
        f'<button class="nav-item" aria-label="Messages">{icons["messages"]}</button>'
        f'<button class="nav-item" aria-label="Profile">{icons["profile"]}</button>'
        f'</nav>'
    )


def cta(label: str) -> str:
    return f'<div class="cta-wrap"><button class="cta">{label}</button></div>'


def popup_leave(t: dict) -> str:
    """Confirm-leave bottom sheet — shown if creator taps back with unsaved changes."""
    return f'''<div class="sheet-scrim" id="sheet-leave" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <div class="sheet-icon-wrap warn">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    </div>
    <h3 class="sheet-title">Quitter sans enregistrer ?</h3>
    <p class="sheet-body">Tes modifications ne seront pas conservées. Tu peux revenir et appuyer sur <b>Enregistrer</b> pour les sauvegarder.</p>
    <div class="sheet-actions">
      <button class="sheet-btn sheet-btn-ghost">Continuer la config</button>
      <button class="sheet-btn sheet-btn-danger">Quitter quand même</button>
    </div>
  </div>
</div>'''


def popup_add_text(field_label: str, placeholder: str, sheet_id: str, title: str, body_copy: str) -> str:
    """Generic 'add text' bottom sheet — used for Channel perks + Package services."""
    return f'''<div class="sheet-scrim" id="sheet-{sheet_id}" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <div class="sheet-icon-wrap success">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{MINT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
    </div>
    <h3 class="sheet-title">{title}</h3>
    <p class="sheet-body">{body_copy}</p>
    <label class="sheet-field-label">{field_label}</label>
    <input type="text" class="sheet-input" placeholder="{placeholder}" maxlength="60"/>
    <span class="sheet-counter">0 / 60</span>
    <div class="sheet-actions" style="margin-top:18px">
      <button class="sheet-btn sheet-btn-ghost">Annuler</button>
      <button class="sheet-btn sheet-btn-primary">Ajouter</button>
    </div>
  </div>
</div>'''


def popup_add_date(t: dict) -> str:
    """Date picker bottom sheet — used for 1:1 closed dates."""
    return f'''<div class="sheet-scrim" id="sheet-add-date" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <h3 class="sheet-title" style="margin-bottom:4px">Ajouter une date fermée</h3>
    <p class="sheet-body" style="margin-bottom:14px">Vacances, jour férié, ou jour exceptionnel.</p>
    <div class="date-row">
      <div class="date-col">
        <label class="sheet-field-label">Du</label>
        <input type="text" class="sheet-input" value="20 août 2026" readonly/>
      </div>
      <div class="date-col">
        <label class="sheet-field-label">Au (optionnel)</label>
        <input type="text" class="sheet-input" value="28 août 2026" readonly/>
      </div>
    </div>
    <label class="sheet-field-label" style="margin-top:14px">Libellé (optionnel)</label>
    <input type="text" class="sheet-input" placeholder="Ex. Vacances d'été…" value="Vacances d'été"/>
    <div class="sheet-actions" style="margin-top:18px">
      <button class="sheet-btn sheet-btn-ghost">Annuler</button>
      <button class="sheet-btn sheet-btn-primary">Enregistrer</button>
    </div>
  </div>
</div>'''


def popup_channel_price_picker(current: str = '9.99') -> str:
    """Channel setup · price picker — REAL channel sub tiers (src/config/iap-products.ts
    CHANNEL_SUB_TIERS: $4.99/$6.99/$9.99/$14.99/$19.99). USD, matches code 1:1."""
    tiers = [
        ('4.99', 'Découverte'),
        ('6.99', 'Accessible'),
        ('9.99', 'Standard'),
        ('14.99', 'Premium'),
        ('19.99', 'Expert'),
    ]
    rows = ''
    for price, label in tiers:
        active = price == current
        cls = 'price-tier-row price-tier-on' if active else 'price-tier-row'
        check = '<ion-icon name="checkmark-circle" style="font-size:20px;color:#33A089"></ion-icon>' if active else ''
        rows += (f'<button class="{cls}">'
                 f'<div class="price-tier-meta"><span class="price-tier-amount">${price}</span>'
                 f'<span class="price-tier-label">{label}</span></div>'
                 f'<span class="price-tier-check">{check}</span>'
                 f'</button>')
    return f'''<div class="sheet-scrim" id="sheet-channel-price-picker" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <h3 class="sheet-title" style="margin-bottom:4px">Choisis ton prix mensuel</h3>
    <p class="sheet-body" style="margin-bottom:14px">Tarifs prédéfinis App Store (Apple/Google) · commission Smuppy 20–40%</p>
    <div class="price-tier-list">{rows}</div>
    <div class="sheet-actions" style="margin-top:14px">
      <button class="sheet-btn sheet-btn-ghost">Annuler</button>
      <button class="sheet-btn sheet-btn-primary">Confirmer</button>
    </div>
  </div>
</div>'''


def popup_iap_confirm(merchant: str, item: str, price_label: str, sheet_id: str = 'iap-confirm', recurring: bool = False) -> str:
    """Apple/Google IAP sheet mock — generic for subscribe / book / purchase flows."""
    sub = "Renouvellement automatique mensuel" if recurring else "Paiement unique"
    return f'''<div class="sheet-scrim" id="sheet-{sheet_id}" data-state="closed" aria-hidden="true">
  <div class="sheet sheet-iap">
    <div class="sheet-handle"></div>
    <div class="iap-header">
      <div class="iap-apple-icon"><ion-icon name="logo-apple" style="font-size:24px;color:var(--text)"></ion-icon></div>
      <div class="iap-merchant">
        <h4>{merchant}</h4>
        <p>{sub}</p>
      </div>
    </div>
    <div class="iap-item">
      <div class="iap-item-meta">
        <span class="iap-item-label">{item}</span>
        <span class="iap-item-sub">via App Store</span>
      </div>
      <span class="iap-item-price">{price_label}</span>
    </div>
    <p class="iap-tos">En confirmant, tu acceptes les <b>conditions d'achat App Store</b>.</p>
    <button class="iap-confirm-btn">
      <ion-icon name="scan-outline" style="font-size:22px;color:#fff"></ion-icon>
      <span>Confirmer avec Face ID</span>
    </button>
    <button class="iap-cancel-btn">Annuler</button>
  </div>
</div>'''


def popup_payment_loading() -> str:
    """Generic payment processing spinner."""
    return f'''<div class="sheet-scrim" id="sheet-payment-loading" data-state="closed" aria-hidden="true">
  <div class="sheet sheet-loading">
    <div class="loader"></div>
    <h3 class="sheet-title" style="margin-top:18px">Traitement du paiement</h3>
    <p class="sheet-body">Ne ferme pas l'application…</p>
  </div>
</div>'''


def popup_flow_success(sheet_id: str, emoji: str, title: str, body: str, primary: str, secondary: str = 'Fermer') -> str:
    """Flow-specific success popup (subscribe / booking / purchase)."""
    return f'''<div class="sheet-scrim" id="sheet-{sheet_id}" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <div class="sheet-icon-wrap success">
      <ion-icon name="checkmark-circle" style="font-size:38px;color:#33A089"></ion-icon>
    </div>
    <h3 class="sheet-title">{title} {emoji}</h3>
    <p class="sheet-body">{body}</p>
    <div class="sheet-actions sheet-actions-stacked">
      <button class="sheet-btn sheet-btn-primary">{primary}</button>
      <button class="sheet-btn sheet-btn-ghost">{secondary}</button>
    </div>
  </div>
</div>'''


def popup_book_objective() -> str:
    """1:1 booking flow — write session goal."""
    return f'''<div class="sheet-scrim" id="sheet-book-objective" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <h3 class="sheet-title" style="margin-bottom:4px">Décris ton objectif</h3>
    <p class="sheet-body" style="margin-bottom:14px">Optionnel · aide Sara à préparer ta session</p>
    <textarea class="sheet-textarea" rows="4" placeholder="Ex. Revue de mon programme actuel, ajustements nutrition…"></textarea>
    <span class="sheet-counter">0 / 240</span>
    <div class="sheet-actions" style="margin-top:14px">
      <button class="sheet-btn sheet-btn-ghost">Passer</button>
      <button class="sheet-btn sheet-btn-primary">Continuer</button>
    </div>
  </div>
</div>'''


def popup_date_picker() -> str:
    """1:1 booking flow — pick another date (mock calendar)."""
    days = ''
    selected = 5
    for d in range(1, 31):
        cls = 'cal-day-on' if d == selected else 'cal-day'
        if d in (1, 8, 15, 22, 29):
            cls += ' cal-day-disabled'
        days += f'<button class="{cls}">{d}</button>'
    return f'''<div class="sheet-scrim" id="sheet-date-picker" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <h3 class="sheet-title" style="margin-bottom:4px">Juin 2026</h3>
    <p class="sheet-body" style="margin-bottom:14px">Sélectionne le jour de ta session</p>
    <div class="cal-weekdays">
      <span>L</span><span>M</span><span>M</span><span>J</span><span>V</span><span>S</span><span>D</span>
    </div>
    <div class="cal-grid">{days}</div>
    <div class="sheet-actions" style="margin-top:18px">
      <button class="sheet-btn sheet-btn-ghost">Annuler</button>
      <button class="sheet-btn sheet-btn-primary">Voir les créneaux</button>
    </div>
  </div>
</div>'''


def popup_slot_editor(t: dict) -> str:
    """Day slot editor — opens when creator taps a day row in 1:1 Disponibilités."""
    slots = [('09:00', '12:00'), ('14:00', '19:00')]
    slot_rows = ''
    for i, (start, end) in enumerate(slots):
        slot_rows += (
            f'<div class="slot-row">'
            f'<div class="slot-time-pair">'
            f'<button class="slot-time">{start}</button>'
            f'<span class="slot-dash">–</span>'
            f'<button class="slot-time">{end}</button>'
            f'</div>'
            f'<button class="slot-x" aria-label="Supprimer">'
            f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M3 6h18M8 6V4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2m2 0v14a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V6h12z"/></svg>'
            f'</button>'
            f'</div>'
        )
    return f'''<div class="sheet-scrim" id="sheet-slot-editor" data-state="closed" aria-hidden="true">
  <div class="sheet sheet-tall">
    <div class="sheet-handle"></div>
    <div class="slot-editor-header">
      <h3 class="sheet-title" style="margin-bottom:4px">Lundi · plages d'ouverture</h3>
      <p class="sheet-body" style="margin-bottom:16px;padding:0">Tes fans pourront réserver pendant ces créneaux.</p>
    </div>
    <div class="slot-list">{slot_rows}</div>
    <button class="slot-add">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{MINT}" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>
      <span>Ajouter une plage</span>
    </button>
    <div class="sheet-actions" style="margin-top:18px">
      <button class="sheet-btn sheet-btn-danger">Fermer ce jour</button>
      <button class="sheet-btn sheet-btn-primary">Enregistrer</button>
    </div>
  </div>
</div>'''


def popup_success(screen_title: str, action: str, t: dict) -> str:
    """Success bottom sheet — shown after creator confirms save."""
    sucess_copy = {
        'Channel setup': ('Chaîne publiée 🎉', 'Tes fans peuvent maintenant s\'abonner.', 'Voir ma chaîne'),
        '1:1 setup': ('Sessions 1:1 activées', 'Tes fans peuvent réserver dans les créneaux choisis.', 'Voir mon profil'),
        'Package setup': ('Pack publié', 'Ton pack apparaît dans ta vitrine fans.', 'Voir mon profil'),
    }
    title, body, primary = sucess_copy.get(screen_title, ('Enregistré', 'Modifications sauvegardées.', 'Continuer'))
    return f'''<div class="sheet-scrim" id="sheet-success" data-state="closed" aria-hidden="true">
  <div class="sheet">
    <div class="sheet-handle"></div>
    <div class="sheet-icon-wrap success">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#33A089" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
    </div>
    <h3 class="sheet-title">{title}</h3>
    <p class="sheet-body">{body}</p>
    <div class="sheet-actions sheet-actions-stacked">
      <button class="sheet-btn sheet-btn-primary">{primary}</button>
      <button class="sheet-btn sheet-btn-ghost">Fermer</button>
    </div>
  </div>
</div>'''


# ── per-screen content ─────────────────────────────────────────────
def screen_channel(t: dict) -> tuple:
    # Payout-status banner (CTO directive: mirror the server gate). Shown when the
    # creator's Stripe Connect payout isn't verified yet — links to onboarding.
    payout_banner = '''<section style="padding:0 16px;margin-bottom:14px">
  <div style="display:flex;align-items:center;gap:12px;padding:13px 14px;border-radius:16px;
    background:rgba(232,163,61,0.12);border:1px solid rgba(232,163,61,0.30)">
    <div style="width:34px;height:34px;border-radius:11px;background:rgba(232,163,61,0.18);
      display:flex;align-items:center;justify-content:center;flex-shrink:0">
      <ion-icon name="alert-circle" style="font-size:19px;color:#E8A33D"></ion-icon></div>
    <div style="flex:1">
      <div style="font-size:13px;font-weight:800;color:#E8A33D">Configure tes paiements pour encaisser</div>
      <div style="font-size:11.5px;font-weight:500;color:var(--sub);margin-top:1px">Obligatoire avant de publier ta chaîne payante</div>
    </div>
    <button style="padding:7px 13px;border:none;border-radius:999px;background:#E8A33D;color:#1a1205;
      font-size:12px;font-weight:800;cursor:pointer;flex-shrink:0;font-family:inherit">Configurer</button>
  </div>
</section>'''

    # Hero cover card — preview-only (profile display name auto-used)
    hero = '''<section class="hero">
  <div class="hero-card">
    <img src="https://images.unsplash.com/photo-1518611012118-696072aa579a?w=900&h=900&fit=crop&q=80" alt="Channel cover"/>
    <div class="hero-overlay"></div>
    <div class="hero-edit"><span class="material-symbols-outlined" style="font-size:18px;color:#fff">photo_camera</span><span>Changer la couverture</span></div>
    <div class="hero-text">
      <span class="hero-tag">Aperçu</span>
      <h2 class="hero-name">Sara Khan</h2>
      <p class="hero-tag-line">Ton nom de profil sera utilisé automatiquement</p>
    </div>
  </div>
</section>'''

    pricing = section('Abonnement mensuel', (
        row('Prix mensuel', input_value('$9.99', mint=True), icon='euro', hue=MINT, sub='Prix vu par tes fans · TVA incluse', last=True)
    ))

    perks_body = (
        benefit_row('Accès à tous les lives') +
        benefit_row('Posts réservés aux abonnés') +
        benefit_row('Réductions sur les sessions 1:1') +
        add_row('Ajouter un avantage')
    )
    perks = section('Avantages abonnés', perks_body)

    note = ('<p class="note"><b>Commission Smuppy 20–40%</b> '
            'sur les abonnements, dégressive selon la taille de ta communauté.</p>')

    body = payout_banner + hero + pricing + perks + note
    return body, 'Publier la chaîne'


def screen_1on1(t: dict) -> tuple:
    # Hero summary card
    hero = f'''<section class="hero-compact">
  <div class="hero-compact-card">
    <div class="hero-compact-icon">{ms("video_camera_front", 28, MINT, fill=1)}</div>
    <div class="hero-compact-text">
      <h2>Sessions 1:1 en vidéo</h2>
      <p>Coaching direct via Agora · facturation auto</p>
    </div>
  </div>
</section>'''

    # 5 durations [15, 30, 45, 60, 90] — founder may28 13:10
    durations = ''
    items = [(15, '$15', True), (30, '$28', True), (45, None, False),
             (60, '$45', True), (90, '$69', True)]
    n = len(items)
    for i, (mins, price, on) in enumerate(items):
        price_html = (input_value(price, mint=True) if on
                      else '<span class="val ph">—</span>')
        last = i == n - 1
        durations += (
            f'<div class="row drow" style="{"" if last else "border-bottom:1px solid var(--border)"}">'
            f'<div class="dmin-block">'
            f'<span class="dmin">{mins} min</span>'
            f'<span class="dmin-sub">{"actif" if on else "inactif"}</span>'
            f'</div>'
            f'<div class="ctrl">{price_html}{toggle(on)}</div>'
            f'</div>'
        )
    durations_section = section('Durées proposées', durations)

    # Multi-slot availability per day — tap day → opens slot editor
    days_data = [
        ('Lun', ['09:00 – 12:00', '14:00 – 19:00'], True),
        ('Mar', ['09:00 – 19:00'], True),
        ('Mer', ['10:00 – 17:00'], True),
        ('Jeu', ['09:00 – 12:00', '14:00 – 19:00'], True),
        ('Ven', ['09:00 – 16:00'], True),
        ('Sam', ['10:00 – 14:00'], True),
        ('Dim', [], False),  # closed
    ]
    avail_rows = ''
    for i, (day, slots, is_open) in enumerate(days_data):
        last = i == len(days_data) - 1
        sep = '' if last else 'border-bottom:1px solid var(--border)'
        if is_open and slots:
            slots_html = ' · '.join(slots)
            ctrl = f'<span class="lbl-sub" style="text-align:right;max-width:none;color:var(--text);font-weight:600">{slots_html}</span>{chev()}'
        else:
            ctrl = f'<span class="day-closed">Fermé</span>{chev()}'
        avail_rows += (
            f'<button class="row day-row" style="{sep};width:100%;background:none;text-align:left">'
            f'{chip("event" if is_open else "do_not_disturb_on", MINT if is_open else "#94A3B8")}'
            f'<div class="lbl-block"><span class="lbl">{day}</span></div>'
            f'<div class="ctrl day-ctrl">{ctrl}</div>'
            f'</button>'
        )
    avail = section('Disponibilités · plages multiples', avail_rows)

    # Closed dates (vacations / public holidays)
    closed_chips = ''
    for label, sub in [('14 juillet', 'Fête nationale'), ('15 août', 'Assomption'),
                       ('20–28 août', 'Vacances')]:
        closed_chips += (
            f'<div class="chip-closed">'
            f'<span class="chip-closed-date">{label}</span>'
            f'<span class="chip-closed-sub">{sub}</span>'
            f'<button class="chip-x" aria-label="Supprimer">{ms("close", 16, "currentColor")}</button>'
            f'</div>'
        )
    closed_body = (
        f'<div class="closed-grid">{closed_chips}</div>'
        + add_row('Ajouter une date fermée')
    )
    closed = section('Dates fermées · vacances · jours fériés', closed_body)

    subject = section('Sujet par défaut · optionnel', (
        '<div class="ta-wrap">'
        '<textarea class="ta" rows="2" placeholder="Ex. Revue de programme et objectifs du mois…">'
        '</textarea>'
        '<span class="ta-count">0 / 240</span>'
        '</div>'
    ))

    note = ('<p class="note"><b>Vidéo en direct via Agora</b> · '
            'commission Smuppy <b>20 %</b> sur chaque session.</p>')

    body = hero + durations_section + avail + closed + subject + note
    return body, 'Enregistrer'


def screen_packages(t: dict) -> tuple:
    # Hero summary
    hero = f'''<section class="hero-compact">
  <div class="hero-compact-card">
    <div class="hero-compact-icon">{ms("inventory_2", 26, MINT, fill=1)}</div>
    <div class="hero-compact-text">
      <h2>Packs de coaching</h2>
      <p>Tu remplis chaque pack avec tes propres services</p>
    </div>
  </div>
</section>'''

    # Existing packs
    existing = section('Tes packs publiés', (
        '<button class="pack-row">'
        '<div class="pack-thumb" style="background:linear-gradient(135deg,#FFB4A2,#FFCFD2)">'
        '<span class="material-symbols-outlined" style="color:#fff;font-size:22px">rocket_launch</span>'
        '</div>'
        '<div class="pack-meta">'
        '<span class="pack-name">Kickstart</span>'
        '<span class="pack-sub">1 mois · $149 · 24 abonnés actifs</span>'
        '</div>'
        + chev() +
        '</button>'
    ))

    # Editor card
    editor_body = (
        row('Titre du pack', input_value('Transformation'), icon='edit_note', hue='#8B5CF6') +
        row('Durée', input_value('3 mois'), icon='timer', hue='#3B82F6') +
        '<div class="services-header">Inclus dans ce pack</div>' +
        benefit_row('2 sessions 1:1 / semaine') +
        benefit_row('Plan nutrition personnalisé') +
        benefit_row('Support WhatsApp quotidien') +
        add_row('Ajouter un service') +
        '<div class="price-block">' +
        row('Prix barré (promo)', input_value('$320'), icon='strikethrough_s', hue='#94A3B8') +
        row('Prix final', input_value('$269', mint=True), icon='euro', hue=MINT) +
        row('Badge (optionnel)', input_value('Best seller'), icon='workspace_premium', hue='#F59E0B', last=True) +
        '</div>'
    )
    editor = section('Nouveau pack', editor_body)

    note = ('<p class="note">Tu remplis chaque pack avec <b>tes propres services</b>. '
            'Commission Smuppy <b>20 %</b> sur chaque vente.</p>')

    body = hero + existing + editor + note
    return body, 'Enregistrer le pack'


def screen_channel_owner_profile(t: dict) -> tuple:
    """OWNER PROFILE VIEW for Channel — what creator sees on their own profile for the Channel tab."""
    body = '''<section class="cv-hero-compact">
  <img src="https://images.unsplash.com/photo-1518611012118-696072aa579a?w=900&h=675&fit=crop&q=80" alt="Channel cover"/>
  <div class="cv-hero-fade"></div>
  <div class="cv-premium-tag">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff" stroke="#fff" stroke-width="0.5" stroke-linejoin="round"><path d="M12 2l2.39 7.36H22l-6.19 4.5 2.37 7.32L12 16.66l-6.18 4.52 2.37-7.32L2 9.36h7.61z"/></svg>
    <span>TA CHAÎNE · LIVE</span>
  </div>
  <a class="manage-chip" href="creator_channel_setup_v2_dark/code.html">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>
    <span>Configurer</span>
  </a>
</section>
<section class="cv-headline">
  <h2 class="cv-title">Sara's Channel</h2>
  <p class="cv-tagline">$9.99/mois · publié il y a 12 jours</p>
</section>
<section class="owner-stats">
  <div class="owner-stat">
    <span class="owner-stat-num">48</span>
    <span class="owner-stat-label">Abonnés actifs</span>
  </div>
  <div class="owner-stat">
    <span class="owner-stat-num">$412</span>
    <span class="owner-stat-label">Ce mois</span>
  </div>
  <div class="owner-stat">
    <span class="owner-stat-num">+12%</span>
    <span class="owner-stat-label">vs mois dernier</span>
  </div>
</section>
<section class="cv-perks-list" style="padding-bottom:14px">
  <p class="cv-perks-label" style="padding:0 16px;font-size:11px;font-weight:700;letter-spacing:.10em;text-transform:uppercase;color:var(--section);margin:4px 0 8px">Ce que voient tes fans</p>
  <div class="cv-perk-row"><span class="cv-perk-icon" style="background:rgba(51,160,137,0.12);color:#33A089"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#33A089" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg></span><div class="cv-perk-text"><h4>Lives exclusifs</h4><p>Accès à tous les lives + replays</p></div></div>
  <div class="cv-perk-row"><span class="cv-perk-icon" style="background:rgba(139,92,246,.12);color:#8B5CF6"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="14" rx="3"/><path d="M7 21l5-4 5 4"/></svg></span><div class="cv-perk-text"><h4>Posts privés</h4><p>Contenu réservé aux abonnés</p></div></div>
  <div class="cv-perk-row"><span class="cv-perk-icon" style="background:rgba(245,158,11,.12);color:#F59E0B"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg></span><div class="cv-perk-text"><h4>−20% sur les 1:1</h4><p>Réduction sur sessions privées</p></div></div>
</section>'''
    return body, "Voir l'analytique"


def screen_1on1_owner_profile(t: dict) -> tuple:
    """OWNER PROFILE VIEW for 1:1 — what creator sees on their own profile for Sessions tab."""
    body = '''<section class="owner-banner">
  <div class="owner-banner-icon" style="background:rgba(51,160,137,0.16);color:#33A089">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#33A089" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter:drop-shadow(0 0 16px rgba(51,160,137,0.2))"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
  </div>
  <div class="owner-banner-text">
    <h2>Sessions 1:1 · actives</h2>
    <p>Vidéo Agora · 4 durées proposées</p>
  </div>
  <a class="manage-chip manage-chip-inline" href="creator_1on1_setup_v2_dark/code.html">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>
    <span>Configurer</span>
  </a>
</section>
<section class="owner-stats">
  <div class="owner-stat"><span class="owner-stat-num">11</span><span class="owner-stat-label">Réservations ce mois</span></div>
  <div class="owner-stat"><span class="owner-stat-num">$328</span><span class="owner-stat-label">Revenus 30j</span></div>
  <div class="owner-stat"><span class="owner-stat-num">4.9★</span><span class="owner-stat-label">Note moyenne</span></div>
</section>
<section class="bv-section" style="margin-top:6px">
  <h3 class="sec" style="margin:0 6px 10px">Tes prochaines sessions</h3>
  <div class="upcoming-list">
    <div class="upcoming-row">
      <div class="upcoming-when">
        <span class="upcoming-day">Jeu 5 juin</span>
        <span class="upcoming-time">14:00 · 30 min</span>
      </div>
      <div class="upcoming-who">
        <img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=80&h=80&fit=crop&q=80" alt="fan"/>
        <span>Marc D.</span>
      </div>
      <span class="upcoming-status upcoming-status-ok">Confirmée</span>
    </div>
    <div class="upcoming-row">
      <div class="upcoming-when">
        <span class="upcoming-day">Ven 6 juin</span>
        <span class="upcoming-time">10:30 · 60 min</span>
      </div>
      <div class="upcoming-who">
        <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=80&h=80&fit=crop&q=80" alt="fan"/>
        <span>Lina K.</span>
      </div>
      <span class="upcoming-status upcoming-status-ok">Confirmée</span>
    </div>
    <div class="upcoming-row">
      <div class="upcoming-when">
        <span class="upcoming-day">Lun 9 juin</span>
        <span class="upcoming-time">17:00 · 30 min</span>
      </div>
      <div class="upcoming-who">
        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=80&h=80&fit=crop&q=80" alt="fan"/>
        <span>Yann B.</span>
      </div>
      <span class="upcoming-status upcoming-status-ok">Confirmée</span>
    </div>
  </div>
</section>'''
    return body, "Voir toutes les réservations"


def screen_packages_owner_profile(t: dict) -> tuple:
    """OWNER PROFILE VIEW for Packs — list of own packs with stats + Manage."""
    body = '''<section class="owner-banner">
  <div class="owner-banner-icon" style="background:rgba(255,180,162,.16);color:#FFB4A2">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FFB4A2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter:drop-shadow(0 0 16px rgba(255,180,162,.5))"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
  </div>
  <div class="owner-banner-text">
    <h2>Tes packs · 2 publiés</h2>
    <p>Coaching follow-up · commission 20%</p>
  </div>
  <a class="manage-chip manage-chip-inline" href="creator_packages_setup_v2_dark/code.html">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
    <span>Nouveau pack</span>
  </a>
</section>
<section class="owner-stats">
  <div class="owner-stat"><span class="owner-stat-num">7</span><span class="owner-stat-label">Ventes ce mois</span></div>
  <div class="owner-stat"><span class="owner-stat-num">$1,883</span><span class="owner-stat-label">Revenus 30j</span></div>
  <div class="owner-stat"><span class="owner-stat-num">96%</span><span class="owner-stat-label">Complétion</span></div>
</section>
<section style="padding:0 16px">
  <h3 class="sec" style="margin:6px 6px 10px">Tes packs publiés</h3>
  <div class="pack-card">
    <div class="pack-card-thumb" style="background:linear-gradient(135deg,#FFB4A2,#FFCFD2)">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" stroke="#fff" stroke-width="0.5"><path d="M12 2l2.39 7.36H22l-6.19 4.5 2.37 7.32L12 16.66l-6.18 4.52 2.37-7.32L2 9.36h7.61z"/></svg>
    </div>
    <div class="pack-card-meta">
      <span class="pack-card-name">Transformation · 3 mois</span>
      <span class="pack-card-sub">$269 · 5 abonnés actifs · BEST SELLER</span>
    </div>
    <span class="material-symbols-outlined" style="color:var(--chev);font-size:22px">chevron_right</span>
  </div>
  <div class="pack-card">
    <div class="pack-card-thumb" style="background:linear-gradient(135deg,#A8E6D9,#33A089)">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" stroke="#fff" stroke-width="0.5"><path d="M12 2l2.39 7.36H22l-6.19 4.5 2.37 7.32L12 16.66l-6.18 4.52 2.37-7.32L2 9.36h7.61z"/></svg>
    </div>
    <div class="pack-card-meta">
      <span class="pack-card-name">Kickstart · 1 mois</span>
      <span class="pack-card-sub">$149 · 2 abonnés actifs</span>
    </div>
    <span class="material-symbols-outlined" style="color:var(--chev);font-size:22px">chevron_right</span>
  </div>
</section>'''
    return body, "Voir l'historique des ventes"


def screen_1on1_view(t: dict) -> tuple:
    """1:1 TAB (visitor) — INFO + CTA only. Booking form lives ONLY in p2_creator_booking
    (founder jun03 : tab 1:1 ne duplique plus l'écran de réservation)."""
    body = '''<section class="bv-hero">
  <div class="bv-avatar-wrap">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=240&h=240&fit=crop&q=80" alt="Sara"/>
    <span class="bv-verified">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="#33A089" stroke="#fff" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
    </span>
  </div>
  <h2 class="bv-name">Sara Khan</h2>
  <p class="bv-role">Coach yoga · vidéo live (Agora)</p>
</section>
<section style="padding:0 16px">
  <div style="background:var(--card);border:1px solid var(--border);border-radius:20px;padding:18px 16px;box-shadow:0 2px 12px rgba(0,0,0,.10)">
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px">
      <span style="font-size:14px;font-weight:800;color:var(--mint)">4.9★</span>
      <span style="font-size:12px;color:var(--sub);font-weight:500">138 sessions réalisées</span>
    </div>
    <p style="font-size:13.5px;color:var(--text);line-height:1.55;font-weight:500;margin-bottom:16px">
      Coaching 1:1 personnalisé en visio live. Revue de programme, ajustements nutrition, objectifs du mois — adapté à ton niveau.</p>
    <div style="font-size:10px;font-weight:700;letter-spacing:.10em;text-transform:uppercase;color:var(--sub);margin-bottom:8px">Durées & tarifs</div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:16px">''' + ''.join(
        f'<div style="background:var(--input-bg);border:1px solid var(--input-border);border-radius:12px;'
        f'padding:8px 0;text-align:center"><div style="font-size:15px;font-weight:800;color:var(--text)">{m}'
        f'</div><div style="font-size:9px;color:var(--sub);font-weight:600">min</div>'
        f'<div style="font-size:11px;font-weight:700;color:var(--mint);margin-top:2px">${p}</div></div>'
        for m, p in [('15', '15'), ('30', '28'), ('60', '45'), ('90', '69')]) + '''
    </div>
    <div style="display:flex;flex-direction:column;gap:8px">''' + ''.join(
        f'<div style="display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--text);font-weight:500">'
        f'<ion-icon name="checkmark-circle" style="font-size:16px;color:var(--mint)"></ion-icon>{txt}</div>'
        for txt in ['Visio live HD (Agora)', 'Plan personnalisé écrit après la session', 'Replay dispo 7 jours']) + '''
    </div>
  </div>
  <p style="text-align:center;font-size:11px;color:var(--sub);margin-top:12px;font-weight:500">
    <ion-icon name="time-outline" style="font-size:13px;vertical-align:middle"></ion-icon> Prochaine dispo : jeudi 5 juin, 14:00</p>
</section>'''
    return body, "Réserver une session"


def screen_package_view(t: dict) -> tuple:
    """FAN-FACING package purchase view — visitor sees pack details + buys."""
    body = '''<section class="cv-hero-compact" style="aspect-ratio:5/3">
  <img src="https://images.unsplash.com/photo-1607962837359-5e7e89f86776?w=900&h=540&fit=crop&q=80" alt="Pack"/>
  <div class="cv-hero-fade"></div>
  <div class="cv-premium-tag" style="background:linear-gradient(135deg,#FFB4A2,#FFCFD2);box-shadow:0 4px 16px rgba(255,180,162,.45)">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="#fff" stroke="#fff" stroke-width="0.5"><path d="M12 2l2.39 7.36H22l-6.19 4.5 2.37 7.32L12 16.66l-6.18 4.52 2.37-7.32L2 9.36h7.61z"/></svg>
    <span>BEST SELLER</span>
  </div>
</section>
<section class="cv-headline">
  <h2 class="cv-title">Transformation · 3 mois</h2>
  <p class="cv-tagline">Coaching personnalisé par Sara Khan · résultats garantis</p>
</section>
<section class="pv-price-block">
  <div class="pv-price-old">$320</div>
  <div class="pv-price-new">$269</div>
  <div class="pv-price-save">Économise $51</div>
</section>
<section class="cv-perks-list" style="padding-bottom:14px">
  <div class="cv-perk-row">
    <span class="cv-perk-icon" style="background:rgba(51,160,137,0.12);color:#33A089">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#33A089" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/></svg>
    </span>
    <div class="cv-perk-text"><h4>2 sessions 1:1 / semaine</h4><p>24 sessions vidéo en 3 mois</p></div>
  </div>
  <div class="cv-perk-row">
    <span class="cv-perk-icon" style="background:rgba(245,158,11,.12);color:#F59E0B">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v6a9 9 0 0 1-18 0z"/><circle cx="12" cy="15" r="6"/></svg>
    </span>
    <div class="cv-perk-text"><h4>Plan nutrition personnalisé</h4><p>Mis à jour chaque mois selon tes progrès</p></div>
  </div>
  <div class="cv-perk-row">
    <span class="cv-perk-icon" style="background:rgba(139,92,246,.12);color:#8B5CF6">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    </span>
    <div class="cv-perk-text"><h4>Support WhatsApp quotidien</h4><p>Réponse sous 2h en semaine</p></div>
  </div>
</section>'''
    return body, "Acheter le pack · $269"


def screen_channel_view(t: dict) -> tuple:
    """FAN-FACING Channel view — matches founder ref may28 18:24:45.
    Hero photo + overlapping card with "Sara's Channel" + tagline + "PREMIUM ACCESS"
    pill with star + "What's included" + 4 mint check perks."""
    body = '''<section class="cv-hero-tall">
  <img src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=900&h=900&fit=crop&q=80" alt="Sara Khan"/>
  <div class="cv-hero-fade"></div>
</section>
<section class="cv-overlap-card">
  <h2 class="cv-title">Sara's Channel</h2>
  <p class="cv-tagline">Yoga flows · plans repas · Q&amp;A live mensuel</p>
  <div class="cv-premium-pill">
    <div class="cv-premium-meta">
      <span class="cv-premium-label">PREMIUM ACCESS</span>
      <p class="cv-premium-price">$9.99 <span>/ mois</span></p>
    </div>
    <div class="cv-premium-star">
      <ion-icon name="star" style="font-size:18px;color:#33A089"></ion-icon>
    </div>
  </div>
  <p class="cv-included">Inclus dans l'abonnement</p>
  <div class="cv-perks-simple">
    <div class="cv-perk-simple"><span class="cv-check-small"><ion-icon name="checkmark" style="font-size:12px;color:#fff"></ion-icon></span><span>Accès à tous les lives + replays</span></div>
    <div class="cv-perk-simple"><span class="cv-check-small"><ion-icon name="checkmark" style="font-size:12px;color:#fff"></ion-icon></span><span>Posts privés réservés aux abonnés</span></div>
    <div class="cv-perk-simple"><span class="cv-check-small"><ion-icon name="checkmark" style="font-size:12px;color:#fff"></ion-icon></span><span>Q&amp;A live mensuel exclusif</span></div>
    <div class="cv-perk-simple"><span class="cv-check-small"><ion-icon name="checkmark" style="font-size:12px;color:#fff"></ion-icon></span><span>−20% sur toutes les sessions 1:1</span></div>
  </div>
</section>'''
    return body, "S'abonner"


# ── C1/C2/C3 · Visitor lifecycle states (post-transaction) ────────────
def screen_channel_view_subscribed(t: dict) -> tuple:
    """C1 · Fan already subscribed to Channel."""
    base, _ = screen_channel_view(t)
    status_banner = '''<div class="state-status state-status-active">
  <ion-icon name="checkmark-circle" style="font-size:18px;color:#33A089"></ion-icon>
  <div class="state-status-text"><h4>Abonné depuis 12 jours</h4><p>Prochain prélèvement le 28 juin · $9.99</p></div>
</div>'''
    body = status_banner + base
    return body, 'Gérer mon abonnement'


def screen_1on1_view_booked(t: dict) -> tuple:
    """C2 · Fan already booked a 1:1 session.
    Founder ref (may28 18:24): Booking Confirmation style — centered check icon
    with glow, big title, body, compact card with coach + Date/Heure grid +
    Ajouter au calendrier button. Gradient pill CTA at bottom."""
    body = '''<section class="confirm-hero">
  <div class="confirm-check-wrap">
    <div class="confirm-check-ring"></div>
    <div class="confirm-check-inner">
      <ion-icon name="checkmark" style="font-size:30px;color:#33A089"></ion-icon>
    </div>
  </div>
  <h2 class="confirm-title">Session Confirmée !</h2>
  <p class="confirm-body">Votre séance en tête-à-tête est programmée. Préparez-vous à avancer !</p>
</section>
<section class="confirm-card">
  <div class="confirm-coach">
    <img class="confirm-coach-avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80" alt="Sara"/>
    <div class="confirm-coach-meta">
      <span class="confirm-coach-label">COACH</span>
      <span class="confirm-coach-name">Sara Khan</span>
    </div>
  </div>
  <div class="confirm-grid">
    <div class="confirm-grid-col">
      <div class="confirm-grid-icon"><ion-icon name="calendar-outline" style="font-size:18px;color:#33A089"></ion-icon><span>DATE</span></div>
      <span class="confirm-grid-val">Jeudi 5<br>Juin</span>
    </div>
    <div class="confirm-grid-col">
      <div class="confirm-grid-icon"><ion-icon name="time-outline" style="font-size:18px;color:#33A089"></ion-icon><span>HEURE</span></div>
      <span class="confirm-grid-val">14:00</span>
    </div>
  </div>
  <button class="confirm-calendar-btn">
    <ion-icon name="calendar-outline" style="font-size:18px"></ion-icon>
    <span>Ajouter au calendrier</span>
  </button>
</section>'''
    return body, 'Aller au profil du coach →'


def screen_package_view_purchased(t: dict) -> tuple:
    """C3 · Fan already purchased a Pack."""
    base, _ = screen_package_view(t)
    status_banner = '''<div class="state-status state-status-active">
  <ion-icon name="checkmark-circle" style="font-size:18px;color:#33A089"></ion-icon>
  <div class="state-status-text"><h4>Pack actif · 11 sessions restantes</h4><p>Valable jusqu'au 28 août · 24 sessions au total</p></div>
</div>'''
    body = status_banner + base
    return body, 'Réserver une session'


def _profile_shell_body(is_owner: bool) -> tuple:
    """Sprint C v3 · CANONICAL pro_creator profile (founder ref may28 20:35).
    Header (cover + avatar + name + actions) + bio with hashtags + stats row +
    main pills (Lifestyle / Channel) + sub-tabs (Library / 1:1 / Packs) +
    1:1 booking content (day scroll + slot grid) + bottom nav 5 slots."""
    if is_owner:
        cta_main = '<button class="prof-follow-btn">Modifier</button>'
        cta_icon = '<button class="prof-msg-icon" aria-label="Partager"><ion-icon name="share-social-outline" style="font-size:18px"></ion-icon></button>'
        cta_label = 'Statistiques'
    else:
        cta_main = '<button class="prof-follow-btn">Become a fan</button>'
        cta_icon = f'<button class="prof-msg-icon" aria-label="Message">{msg_icon_canonical(18)}</button>'
        cta_label = "S'abonner à la chaîne · $9.99/mois"

    # Profile shell v4 · canonical match (founder ref may29 19:21) :
    # Cover + avatar gauche + name + bio + stats bordered + Become a fan + msg icon
    # + Main segmented (Lifestyle/Channel) + Sub-pills (Posts/Peaks/Activities) +
    # 3-col uniform grid + bottom nav
    body = f'''<section class="prof-cover-strip">
  <img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=900&h=400&fit=crop&q=80" alt="Cover"/>
  <button class="prof-back" aria-label="Retour"><ion-icon name="chevron-back" style="font-size:22px;color:#fff"></ion-icon></button>
  <button class="prof-more" aria-label="Plus"><ion-icon name="ellipsis-horizontal" style="font-size:20px;color:#fff"></ion-icon></button>
</section>
<section class="prof-head">
  <div class="prof-avatar">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="Sara"/>
    <span class="prof-verified"><ion-icon name="checkmark" style="font-size:11px;color:#fff"></ion-icon></span>
  </div>
</section>
<section class="prof-meta">
  <h1 class="prof-name">Sara Khan</h1>
  <p class="prof-role">Yoga coach · Montréal · Daily flows 🍃</p>
  <p class="prof-bio">Helping you find your inner peace through movement and breath. <span class="prof-tag">#wellnessjourney</span> <span class="prof-tag">#yogalife</span></p>
</section>
<section class="prof-stats-bordered">
  <div class="prof-stat-cell"><span class="prof-stat-num">24K</span><span class="prof-stat-lbl">FANS</span></div>
  <div class="prof-stat-cell"><span class="prof-stat-num">412</span><span class="prof-stat-lbl">POSTS</span></div>
  <div class="prof-stat-cell"><span class="prof-stat-num">89</span><span class="prof-stat-lbl">PEAKS</span></div>
</section>
<section class="prof-actions-row">
  {cta_main}
  {cta_icon}
</section>
<nav class="prof-main-pills">
  <button class="prof-main-pill prof-main-pill-on">
    <ion-icon name="heart" style="font-size:14px;vertical-align:middle;margin-right:4px"></ion-icon>Lifestyle</button>
  <button class="prof-main-pill">
    <ion-icon name="play-circle-outline" style="font-size:14px;vertical-align:middle;margin-right:4px"></ion-icon>Channel</button>
</nav>
<nav class="prof-sub-pills">
  <button class="prof-sub-pill prof-sub-pill-on">
    <ion-icon name="grid-outline" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Posts</button>
  <button class="prof-sub-pill">
    <ion-icon name="film-outline" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Peaks</button>
  <button class="prof-sub-pill">
    <ion-icon name="walk-outline" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Activities</button>
</nav>
<section class="prof-grid-uniform">
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=400&h=400&fit=crop&q=80" alt=""/></div>
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&h=400&fit=crop&q=80" alt=""/></div>
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1517363898874-737b62a7db91?w=400&h=400&fit=crop&q=80" alt=""/></div>
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=400&h=400&fit=crop&q=80" alt=""/></div>
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1494390248081-4e521a5940db?w=400&h=400&fit=crop&q=80" alt=""/></div>
  <div class="prof-tile-uniform"><img src="https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=400&h=400&fit=crop&q=80" alt=""/></div>
</section>
{bottomnav_canonical('profile')}'''
    return body, cta_label


def screen_profile_owner(t: dict) -> tuple:
    return _profile_shell_body(is_owner=True)


def screen_profile_visitor(t: dict) -> tuple:
    return _profile_shell_body(is_owner=False)


# ─── Post-creation flow (founder may30 — canonical rebuild of stitch ZIP9 screens) ──
# Each screen below is BARE : returns full 393×852 self-contained content.
# build() detects key prefix and skips default topbar/cta wrapper.
# All 6 use canonical V2 : ion-icons + chip tiers + mint glow + V2 palette.

def screen_post_create_menu(t: dict) -> tuple:
    """BottomSheet "Que veux-tu créer ?" — fan/creator entry point.
    4 options : Post / Peak / Go Live (red live dot) / Activity.
    Behind: darkened solid feed silhouette (canonical V2 palette).
    """
    # ion-icon names directly (not via chip helper which expects material symbols name)
    OPTS = [
        ('images-outline', '#11C6FF', 'Post', "Photo, carrousel, légende", False),
        ('film-outline',   '#9966FF', 'Peak', "Vidéo verticale 15-60s", False),
        ('videocam',       '#FF4658', 'Go Live', "Stream en direct avec ta tribu", True),
        ('walk-outline',   '#FFA63D', 'Activity', "Run, ride, training, hike", False),
    ]
    rows = ''
    for ion_name, hue, title, sub, is_live in OPTS:
        live_dot = '<span class="pcm-live-dot" aria-label="LIVE"></span>' if is_live else ''
        ic = (f'<span class="pcm-ic" style="background:{hue}1A;color:{hue};'
              f'box-shadow:0 0 18px {hue}55, 0 0 0 1px {hue}40 inset;'
              f'filter:drop-shadow(0 0 8px {hue}80);">'
              f'<ion-icon name="{ion_name}" style="font-size:22px;color:{hue}"></ion-icon></span>')
        rows += f'''  <button class="pcm-row">
    {ic}
    <div class="pcm-row-text">
      <div class="pcm-row-title">{title} {live_dot}</div>
      <div class="pcm-row-sub">{sub}</div>
    </div>
    <ion-icon name="chevron-forward" style="font-size:20px;color:var(--sub);opacity:.55"></ion-icon>
  </button>
'''
    body = f'''<div class="pcm-backdrop"></div>
<div class="pcm-sheet">
  <div class="pcm-handle"></div>
  <h2 class="pcm-title">Que veux-tu créer&nbsp;?</h2>
  <div class="pcm-rows">
{rows}  </div>
</div>'''
    return body, None


def screen_post_gallery(t: dict) -> tuple:
    """Photo picker for new post. Topbar (back / 'Nouveau post' / Suivant pill)
    + preview large + Recents dropdown + camera icon + 4-col grid + tabs Gallery/Photo/Vidéo + bottom nav.
    """
    THUMBS = [
        ('1488161628813-04466f6efb19', 'flower-orange'),
        ('1494790108377-be9c29b29330', 'woman-portrait'),
        ('1542038784456-1ea8e935640e', 'red-paint'),
        ('1517999144091-3d9dca6d1e43', 'wide-shot'),
        ('1494790108755-2616c84d7e9f', 'portrait-2'),
        ('1502691876148-a84978e59af8', 'palm-tree'),
        ('1502086223501-7ea6ecd79368', 'rooftop'),
        ('1438761681033-6461ffad8d80', 'studio-girl'),
        ('1531746020798-e6953c6e8e04', 'bridge'),
        ('1502134249126-9f3755a50d78', 'street-night'),
        ('1502716119720-b23a93e5fe1b', 'tower'),
        ('1485518882345-15568b007407', 'food'),
        ('1488376739361-66f47020a2dc', 'pasta'),
        ('1518791841217-8f162f1e1131', 'cat'),
        ('1517336714731-489689fd1ca8', 'lake'),
        ('1492684223066-81342ee5ff30', 'shoes'),
    ]
    grid = ''
    for i, (uid, alt) in enumerate(THUMBS):
        sel = ' pg-tile-on' if i == 1 else ''
        check = '<span class="pg-tile-check">' + ms('check', 14, '#fff', wght=700) + '</span>' if i == 1 else ''
        grid += f'<div class="pg-tile{sel}"><img src="https://images.unsplash.com/photo-{uid}?w=200&h=200&fit=crop&q=80" alt="{alt}"/>{check}</div>'
    body = f'''<header class="pg-topbar">
  <button class="back" aria-label="Retour">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--back)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <h1>Nouveau post</h1>
  <button class="pg-next">Suivant</button>
</header>
<main class="pg-main">
  <div class="pg-preview">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800&h=800&fit=crop&q=80" alt="Preview"/>
    <div class="pg-preview-overlay"></div>
    <div class="pg-preview-tag">
      <span class="pg-preview-logo">Smuppy</span>
    </div>
  </div>
  <div class="pg-meta">
    <button class="pg-recents">
      <span>Recents</span>
      <ion-icon name="chevron-down" style="font-size:14px;vertical-align:middle"></ion-icon>
    </button>
    <button class="pg-cam-btn" aria-label="Camera">
      <ion-icon name="camera-outline" style="font-size:20px"></ion-icon>
    </button>
  </div>
  <div class="pg-grid">{grid}</div>
  <div class="pg-source-tabs">
    <button class="pg-source-tab pg-source-tab-on">Galerie</button>
    <button class="pg-source-tab">Photo</button>
    <button class="pg-source-tab">Vidéo</button>
  </div>
</main>'''
    return body, None


def _post_details_body(t: dict) -> tuple:
    """Caption + hashtags + 3-row card (location / tag fans / visibility).
    Used for both dark and light themes — palette switches via t['dark'] not the function.
    """
    HASHTAGS_ON = ['summer', 'vibes']
    HASHTAGS_OFF = ['outfit', 'ootd', 'fashion']
    chips_on = ''.join(
        f'<span class="pd-tag pd-tag-on">#{h}<span class="pd-tag-x">{ms("close", 11, "currentColor")}</span></span>'
        for h in HASHTAGS_ON
    )
    chips_off = ''.join(f'<span class="pd-tag">#{h}</span>' for h in HASHTAGS_OFF)
    body = f'''<header class="pd-topbar">
  <button class="back" aria-label="Retour">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--back)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <h1>Nouveau post</h1>
  <button class="pd-publish">Publier</button>
</header>
<main class="pd-main">
  <section class="pd-caption-row">
    <div class="pd-thumb">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="Preview"/>
    </div>
    <textarea class="pd-caption" placeholder="Écris une légende…" rows="3"></textarea>
  </section>
  <section class="pd-hashtags">
    <h3 class="pd-section-label">Hashtags</h3>
    <div class="pd-tags-wrap">{chips_on}{chips_off}</div>
  </section>
  <section class="pd-settings">
    <div class="pd-row">
      {chip("location_on", "#11C6FF")}
      <div class="pd-row-text">
        <div class="pd-row-title">Ajouter un lieu</div>
        <div class="pd-row-sub">Montmartre, Paris</div>
      </div>
      <ion-icon name="chevron-forward" style="font-size:18px;color:var(--sub);opacity:.55"></ion-icon>
    </div>
    <div class="pd-row-sep"></div>
    <div class="pd-row">
      {chip("group", "#9966FF")}
      <div class="pd-row-text">
        <div class="pd-row-title">Identifier des fans</div>
        <div class="pd-row-sub">Aucune personne identifiée</div>
      </div>
      <ion-icon name="chevron-forward" style="font-size:18px;color:var(--sub);opacity:.55"></ion-icon>
    </div>
    <div class="pd-row-sep"></div>
    <div class="pd-row">
      {chip("public", MINT)}
      <div class="pd-row-text">
        <div class="pd-row-title">Visibilité</div>
        <div class="pd-row-sub">Public · visible dans Explorer</div>
      </div>
      <ion-icon name="chevron-forward" style="font-size:18px;color:var(--sub);opacity:.55"></ion-icon>
    </div>
  </section>
  <button class="pd-advanced">
    <ion-icon name="settings-outline" style="font-size:16px;vertical-align:middle;margin-right:6px"></ion-icon>
    Paramètres avancés
  </button>
</main>'''
    return body, None


def screen_post_details_dark(t: dict) -> tuple:
    return _post_details_body(t)


def screen_post_details_light(t: dict) -> tuple:
    return _post_details_body(t)


def screen_post_success(t: dict) -> tuple:
    """Publication réussie (founder jun03) : check animé + carte du post INCLINÉE (-5°)
    avec 2 cartes empilées derrière (stack), + animations pop/tilt-in. 'Voir ma publication'."""
    body = f'''<style>
  .psx-wrap{{position:relative;width:100%;min-height:852px;display:flex;flex-direction:column;
    align-items:center;padding:64px 24px 40px;text-align:center;overflow:hidden}}
  .psx-check{{width:72px;height:72px;border-radius:999px;background:linear-gradient(135deg,{GRAD_A},{GRAD_B});
    display:flex;align-items:center;justify-content:center;margin-bottom:20px;
    box-shadow:0 10px 30px rgba(51,160,137,0.225);animation:psxPop .55s cubic-bezier(.2,1.4,.4,1) both}}
  .psx-check ion-icon{{font-size:38px;color:#fff;animation:psxDraw .4s .25s ease both}}
  .psx-title{{font-size:23px;font-weight:900;letter-spacing:-.02em;color:var(--text);
    animation:psxUp .5s .15s ease both}}
  .psx-sub{{font-size:13.5px;font-weight:500;color:var(--sub);margin-top:7px;line-height:1.5;max-width:280px;
    animation:psxUp .5s .25s ease both}}
  /* card plus grande + imposante + vignette noire dégradée (effet trou) · pas de nom de profil */
  .psx-stack{{position:relative;width:252px;height:340px;margin:34px 0 46px}}
  .psx-card{{position:absolute;inset:0;border-radius:24px;overflow:hidden;background:#000;
    border:1px solid rgba(255,255,255,.07);box-shadow:0 26px 60px rgba(0,0,0,{t['dim_shadow']})}}
  .psx-card-3{{transform:rotate(8deg) translateY(12px) scale(.92);opacity:.45;
    animation:psxFan3 .7s .35s cubic-bezier(.2,1,.4,1) both}}
  .psx-card-2{{transform:rotate(-6deg) translateY(5px) scale(.96);opacity:.75;
    animation:psxFan2 .7s .45s cubic-bezier(.2,1,.4,1) both}}
  .psx-card-1{{transform:rotate(-5deg);animation:psxTilt .8s .5s cubic-bezier(.2,1.1,.35,1) both}}
  .psx-card-1 img{{width:100%;height:100%;object-fit:cover;display:block}}
  /* vignette interne : dégradé noir vers le contour → aspect "trou" */
  .psx-vignette{{position:absolute;inset:0;border-radius:inherit;pointer-events:none;
    box-shadow:inset 0 0 46px 16px rgba(0,0,0,.62), inset 0 0 0 1px rgba(0,0,0,.5)}}
  .psx-live{{position:absolute;top:12px;left:12px;display:flex;align-items:center;gap:5px;padding:4px 10px;
    border-radius:999px;background:rgba(51,160,137,0.475);color:#fff;font-size:10px;font-weight:800;letter-spacing:.04em}}
  .psx-live-dot{{width:6px;height:6px;border-radius:999px;background:#fff}}
  .psx-actions{{width:100%;margin-top:auto;display:flex;flex-direction:column;gap:10px;
    animation:psxUp .5s .7s ease both}}
  .psx-primary{{width:100%;height:52px;border:none;border-radius:16px;
    background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:15px;font-weight:700;
    cursor:pointer;box-shadow:0 8px 22px rgba(51,160,137,0.2)}}
  .psx-ghost{{width:100%;height:46px;border:none;background:transparent;color:var(--sub);
    font-family:inherit;font-size:13.5px;font-weight:700;cursor:pointer}}
  @keyframes psxPop{{from{{transform:scale(0)}}to{{transform:scale(1)}}}}
  @keyframes psxDraw{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:scale(1)}}}}
  @keyframes psxUp{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:translateY(0)}}}}
  @keyframes psxTilt{{from{{opacity:0;transform:rotate(2deg) translateY(40px)}}to{{opacity:1;transform:rotate(-5deg) translateY(0)}}}}
  @keyframes psxFan2{{from{{opacity:0;transform:rotate(0) translateY(40px) scale(.96)}}to{{opacity:.8;transform:rotate(-6deg) translateY(4px) scale(.96)}}}}
  @keyframes psxFan3{{from{{opacity:0;transform:rotate(0) translateY(40px) scale(.92)}}to{{opacity:.5;transform:rotate(8deg) translateY(10px) scale(.92)}}}}
</style>
<div class="psx-wrap">
  <div class="psx-check"><ion-icon name="checkmark"></ion-icon></div>
  <h2 class="psx-title">Publication en ligne 🎉</h2>
  <p class="psx-sub">Ta tribu peut maintenant voir ta nouvelle publication.</p>
  <div class="psx-stack">
    <div class="psx-card psx-card-3"></div>
    <div class="psx-card psx-card-2"></div>
    <div class="psx-card psx-card-1">
      <img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=520&h=700&fit=crop&q=80" alt="post"/>
      <div class="psx-vignette"></div>
      <span class="psx-live"><span class="psx-live-dot"></span>EN LIGNE</span>
    </div>
  </div>
  <div class="psx-actions">
    <button class="psx-primary">Voir ma publication</button>
    <button class="psx-ghost">Créer une autre publication</button>
  </div>
</div>'''
    return body, None


def screen_peak_camera(t: dict) -> tuple:
    """TikTok-style camera. × close / Add Music pill / flash · camera bg · right action stack
    Flip/Timer/Filters/Adjust · speed pills · duration pills · record button · library + filters.
    Wrapped in pkc-root with explicit 393x852 to defeat Chrome headless collapse.
    """
    body = f'''<div class="pkc-root">
<div class="pkc-bg">
  <img src="https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=786&h=1704&fit=crop&q=80" width="393" height="852" alt="Camera view"/>
  <div class="pkc-bg-overlay"></div>
</div>
<header class="pkc-topbar">
  <button class="pkc-close" aria-label="Fermer">
    <ion-icon name="close" style="font-size:24px;color:#fff"></ion-icon>
  </button>
  <button class="pkc-music-pill">
    <ion-icon name="musical-notes" style="font-size:14px;vertical-align:middle;margin-right:6px"></ion-icon>
    Ajouter son
  </button>
  <button class="pkc-flash" aria-label="Flash">
    <ion-icon name="flash-off-outline" style="font-size:22px;color:#fff"></ion-icon>
  </button>
</header>
<div class="pkc-side">
  <button class="pkc-side-item">
    <span class="pkc-side-icon">{ms("flip_camera_ios", 22, "#fff")}</span>
    <span class="pkc-side-label">Flip</span>
  </button>
  <button class="pkc-side-item">
    <span class="pkc-side-icon"><ion-icon name="timer-outline" style="font-size:22px;color:#fff"></ion-icon></span>
    <span class="pkc-side-label">Timer</span>
  </button>
  <button class="pkc-side-item">
    <span class="pkc-side-icon"><ion-icon name="color-wand-outline" style="font-size:22px;color:#fff"></ion-icon></span>
    <span class="pkc-side-label">Effets</span>
  </button>
  <button class="pkc-side-item">
    <span class="pkc-side-icon"><ion-icon name="options-outline" style="font-size:22px;color:#fff"></ion-icon></span>
    <span class="pkc-side-label">Ajuster</span>
  </button>
</div>
<div class="pkc-speed-strip">
  <span>Slow</span><span>Normal</span><span class="pkc-speed-on">1x</span><span>Fast</span><span>Très rapide</span>
</div>
<div class="pkc-duration">
  <button>10s</button>
  <button class="pkc-dur-on">15s</button>
  <button>60s</button>
</div>
<div class="pkc-record-row">
  <button class="pkc-library">
    <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&q=80" alt="Last clip"/>
    <span>Galerie</span>
  </button>
  <button class="pkc-record" aria-label="Enregistrer"><span class="pkc-record-inner"></span></button>
  <button class="pkc-filter">
    <ion-icon name="sparkles-outline" style="font-size:22px;color:#fff"></ion-icon>
    <span>Filtres</span>
  </button>
</div>
</div>'''
    return body, None


def screen_packages_edit(t: dict) -> tuple:
    """Pack editor EDIT mode (Sprint D). Existing pack prefilled, services editable,
    danger zone with Supprimer button, stats pill."""
    services = [
        ("2 sessions 1:1 / semaine", "24 sessions vidéo en 3 mois"),
        ("Plan nutrition personnalisé", "Mis à jour chaque mois selon tes progrès"),
        ("Support WhatsApp quotidien", "Réponse sous 2h en semaine"),
    ]
    svc_rows = ''
    for i, (title, sub) in enumerate(services):
        last = (i == len(services) - 1)
        sep = '' if last else 'border-bottom:1px solid var(--border)'
        svc_rows += f'''<div class="row" style="{sep}">
  <span class="ico" style="width:32px;height:32px;background:{MINT}1A;color:{MINT};
    box-shadow:0 0 14px {MINT}55, 0 0 0 1px {MINT}40 inset;
    filter:drop-shadow(0 0 6px {MINT}80);border-radius:11px;
    display:inline-flex;align-items:center;justify-content:center;">
    <ion-icon name="checkmark" style="font-size:18px;color:{MINT}"></ion-icon>
  </span>
  <div class="lbl-block">
    <span class="lbl">{title}</span>
    <span class="lbl-sub">{sub}</span>
  </div>
  <button class="ben-remove" aria-label="Retirer">
    <ion-icon name="close" style="font-size:18px;color:var(--sub)"></ion-icon>
  </button>
</div>'''
    body = f'''<section class="pe-thumb-wrap">
  <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&h=500&fit=crop&q=80" alt="Pack cover"/>
  <button class="pe-thumb-edit">
    <ion-icon name="camera-outline" style="font-size:14px;vertical-align:middle"></ion-icon>
    Changer la photo
  </button>
</section>

<section class="pe-stats-row">
  <div class="pe-stat-pill"><div class="pe-stat-num">12</div><div class="pe-stat-lbl">Achats total</div></div>
  <div class="pe-stat-pill"><div class="pe-stat-num">8</div><div class="pe-stat-lbl">Packs actifs</div></div>
  <div class="pe-stat-pill"><div class="pe-stat-num">$3,228</div><div class="pe-stat-lbl">Gagné</div></div>
</section>

<h3 class="sec">Identité du pack</h3>
<div class="card">
  {row('Nom du pack', input_value('Transformation · 3 mois'), icon='photo_camera', hue=MINT)}
  {row('Tagline', input_value('Coaching personnalisé · résultats garantis'), icon='format_quote', hue='#11C6FF')}
  {row('Durée', input_value('3 mois'), icon='timer-outline', hue='#9966FF', last=True)}
</div>

<h3 class="sec">Tarif</h3>
<div class="card">
  {row('Prix actuel', input_value('$269', mint=True), icon='euro', hue=MINT)}
  {row('Prix barré (optionnel)', input_value('$320'), icon='card_giftcard', hue='#FFA63D', last=True)}
</div>

<h3 class="sec">Services inclus ({len(services)})</h3>
<div class="card">
{svc_rows}
</div>
{add_row("Ajouter un service")}

<h3 class="sec">Visibilité</h3>
<div class="card">
  {row('Pack public', toggle(True), icon='public', hue=MINT)}
  {row('Renouvellement auto', toggle(False), icon='refresh-outline', hue='#11C6FF', last=True)}
</div>

<h3 class="sec" style="color:#EF4444">Zone danger</h3>
<button class="pe-danger-btn">
  <ion-icon name="trash-outline" style="font-size:18px"></ion-icon>
  Supprimer ce pack
</button>
<p class="pe-danger-sub">Les 8 packs actifs resteront utilisables jusqu'à leur fin. Plus aucune nouvelle vente possible.</p>'''
    return body, "Sauvegarder"


SCREENS = {
    # A · Owner config (Settings subscreens)
    'creator_channel_setup_v2': ('Channel setup', screen_channel),
    'creator_1on1_setup_v2': ('1:1 setup', screen_1on1),
    'creator_packages_setup_v2': ('Package setup', screen_packages),
    # C · Visitor (fan-facing, pre-transaction)
    'creator_channel_view_v2': ("Sara's Channel", screen_channel_view),
    'creator_1on1_view_v2': ('Réserver une session', screen_1on1_view),
    'creator_packages_view_v2': ('Transformation · pack', screen_package_view),
    # B · Owner profile (creator's own profile)
    'creator_channel_owner_profile_v2': ("Sara's Channel", screen_channel_owner_profile),
    'creator_1on1_owner_profile_v2': ('Sessions 1:1', screen_1on1_owner_profile),
    'creator_packages_owner_profile_v2': ('Tes packs', screen_packages_owner_profile),
    # C1/C2/C3 · Visitor post-transaction states (Sprint B)
    'creator_channel_view_v2_subscribed': ("Sara's Channel", screen_channel_view_subscribed),
    'creator_1on1_view_v2_booked': ('Session réservée', screen_1on1_view_booked),
    'creator_packages_view_v2_purchased': ('Transformation · pack', screen_package_view_purchased),
    # Sprint C · Full profile shell (owner + visitor)
    # NOTE jun03: creator_profile_owner/visitor SUPERSEDED by build_profiles_v5.py
    # (Instagram avatar-left header + owner/visitor/fan states). Removed to avoid duplicate.
    # Sprint E · Post-creation flow (canonical V2 rebuild of stitch ZIP9 — founder may30)
    # Each key auto-renders dark + light. _light variant naturally fits backgroundless screens.
    'post_create_menu_v2': ('Créer', screen_post_create_menu),
    'post_gallery_v2': ('Nouveau post', screen_post_gallery),
    'post_details_v2': ('Nouveau post', screen_post_details_dark),
    'post_success_v2': ('Post publié', screen_post_success),
    'peak_camera_v2': ('Peak camera', screen_peak_camera),
    # Sprint D · Pack editor edit mode (founder may30)
    'creator_packages_edit_v2': ('Modifier le pack', screen_packages_edit),
}


def build(key: str, dark: bool) -> str:
    t = theme(dark)
    title, fn = SCREENS[key]
    body, cta_label = fn(t)
    pure_black = '#000000' if dark else '#FFFFFF'
    LIFECYCLE_SUFFIXES = ('_subscribed', '_booked', '_purchased')
    is_lifecycle = key.endswith(LIFECYCLE_SUFFIXES)
    is_profile_shell = 'profile_owner_v2' in key or 'profile_visitor_v2' in key
    is_view = (key.endswith('_view_v2') or key.endswith('_owner_profile_v2')
               or is_lifecycle or is_profile_shell)
    is_owner_profile = key.endswith('_owner_profile_v2')
    # Sprint E : post-creation screens are bare (own topbar/CTA/nav inside body)
    is_bare = key.startswith('post_') or key.startswith('peak_')

    top = '' if is_bare else (topbar_view() if is_view else topbar(title))
    main_class = 'main-view' if is_view else 'main-config'
    # Strip 'creator_' prefix and '_v2' suffix to compute SCREEN_KEY for JS NAV_BY_KEY lookup
    SCREEN_KEY = key.replace('creator_', '').replace('_v2', '')
    MODE = 'dark' if dark else 'light'
    if is_owner_profile:
        cta_subtext = ''  # owner profile = no fan-facing CTA, ghost button "Voir l'analytique"
    elif is_view:
        cta_subtext = '<p class="cta-sub">Annulable à tout moment</p>'
    else:
        cta_subtext = ''
    return f'''<!DOCTYPE html>
<html class="{t['html']}" lang="fr"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<title>Smuppy — {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<!-- Ionicons web component — canonical Smuppy icon set (matches @expo/vector-icons Ionicons in mobile app) -->
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<!-- Material Symbols still used as fallback for icons not in Ionicons -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap" rel="stylesheet"/>
<!-- Figma MCP capture script — activates ONLY when URL contains #figmacapture=... -->
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
<style>
  :root {{
    --mint: {MINT}; --mint-hi: {MINT_HI}; --mint-deep: {MINT_DEEP};
    --page: {t['page']}; --card: {t['card']}; --card-inner: {t['card_inner']};
    --text: {t['text']}; --sub: {t['sub']}; --section: {t['section']};
    --header: {t['header']}; --border: {t['border']};
    --input-bg: {t['input_bg']}; --input-border: {t['input_border']};
    --chev: {t['chev']}; --back: {t['back']};
    --tog-off: {t['tog_off']};
  }}
  * {{ box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-tap-highlight-color:transparent; }}
  html {{ background:var(--page); }}
  html, body {{ max-width:100%; overflow-x:hidden; }}
  .material-symbols-outlined {{
    font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;
    user-select:none;
  }}
  /* Body IS the device — 393×852 native. No scaffold, no centering.
     Founder may29 lock : Figma captures must come out in device format,
     not screen format. Killing the dark page wrapper makes body the phone. */
  body {{
    margin:0; width:393px; height:852px; overflow:hidden;
    background:var(--page); color:var(--text);
    font-family:'Plus Jakarta Sans',-apple-system,system-ui,sans-serif;
    font-size:15px; line-height:1.5;
    position:relative;
  }}
  /* Phone-frame container is now redundant (body = phone) but kept as identity
     pass-through so all existing .phone-root selectors keep working. */
  .phone-root {{
    position:relative; width:100%; height:100%;
    background:var(--page); overflow:hidden;
  }}
  /* ── Topbar ───────────────────────────────────────────────── */
  .topbar {{
    position:absolute; top:0; left:0; right:0; z-index:50;
    height:56px; display:flex; align-items:center; gap:8px;
    padding:0 12px; background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%);
    border-bottom:1px solid var(--border);
  }}
  .topbar-view {{ justify-content:space-between; }}
  .back {{ width:40px; height:40px; border:none; background:transparent;
    border-radius:999px; display:flex; align-items:center; justify-content:center;
    cursor:pointer; transition:background .15s ease; }}
  .back:active {{ background:rgba(51,160,137,0.1); }}
  .topbar h1 {{ flex:1; text-align:center; font-size:16px; font-weight:700; margin:0; color:var(--text); letter-spacing:-.01em; }}
  .topbar-logo {{
    font-size:22px; font-weight:900; letter-spacing:-.02em;
    background:linear-gradient(90deg, var(--mint) 0%, var(--mint-deep) 100%);
    -webkit-background-clip:text; background-clip:text; color:transparent;
    font-family:'Plus Jakarta Sans',sans-serif;
  }}
  /* ── Main ─────────────────────────────────────────────────── */
  main {{ max-width:393px; margin:0 auto; width:100%; height:100%; overflow-y:auto; }}
  .main-config {{ padding:64px 14px 90px; }}
  .main-view {{ padding:0 0 100px; }}
  .main-view-no-topbar {{ padding-top:0; }}
  /* ── Hero (Channel) ───────────────────────────────────────── */
  .hero {{ margin:12px 0 22px; }}
  .hero-card {{ position:relative; width:100%; aspect-ratio:5/4; border-radius:24px; overflow:hidden;
    box-shadow:0 12px 32px rgba(0,107,89,0.18); }}
  .hero-card img {{ width:100%; height:100%; object-fit:cover; }}
  .hero-overlay {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.05) 50%, rgba(0,0,0,0.55) 100%); }}
  .hero-edit {{ position:absolute; top:12px; right:12px;
    display:inline-flex; align-items:center; gap:6px;
    padding:7px 11px; border-radius:999px;
    background:rgba(0,0,0,0.45); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    color:#fff; font-size:11px; font-weight:600; white-space:nowrap; }}
  .hero-text {{ position:absolute; left:20px; right:20px; bottom:18px; color:#fff; }}
  .hero-tag {{ display:inline-block; padding:4px 10px; border-radius:999px;
    background:rgba(255,255,255,0.18); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    font-size:10px; font-weight:700; letter-spacing:.10em; text-transform:uppercase; margin-bottom:8px; }}
  .hero-name {{ font-size:22px; font-weight:800; margin:0 0 4px; letter-spacing:-.02em; }}
  .hero-tag-line {{ font-size:13px; font-weight:500; margin:0; opacity:0.92; }}
  /* ── Hero compact (1:1 + Packages) ────────────────────────── */
  .hero-compact {{ margin:18px 0 22px; }}
  .hero-compact-card {{ display:flex; align-items:center; gap:14px;
    padding:16px; border-radius:20px;
    background:linear-gradient(135deg, rgba(51,160,137,0.1), rgba(0,179,199,.06));
    border:1px solid rgba(51,160,137,0.18); }}
  .hero-compact-icon {{ width:48px; height:48px; border-radius:14px;
    background:rgba(51,160,137,0.16); display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
    box-shadow:0 0 24px rgba(51,160,137,0.15); }}
  .hero-compact-text h2 {{ font-size:16px; font-weight:700; margin:0 0 2px; color:var(--text); letter-spacing:-.01em; }}
  .hero-compact-text p {{ font-size:12px; font-weight:500; margin:0; color:var(--sub); line-height:1.4; }}
  /* ── Section ──────────────────────────────────────────────── */
  .sec {{
    font-size:11px; font-weight:700; letter-spacing:.10em;
    text-transform:uppercase; color:var(--section);
    margin:24px 6px 10px;
  }}
  .card {{ background:var(--card); border-radius:24px; overflow:hidden;
    border:1.5px solid rgba(51,160,137,0.18);
    box-shadow:0 0 24px rgba(51,160,137,0.1),
               0 0 0 1px rgba(51,160,137,0.06) inset,
               0 4px 14px rgba(0,0,0,{t['dim_shadow']}); }}
  /* ── Row ──────────────────────────────────────────────────── */
  .row {{ display:flex; align-items:center; gap:10px; padding:12px 14px; }}
  .ico {{ border-radius:11px; display:flex; align-items:center; justify-content:center;
    flex-shrink:0; }}
  .lbl-block {{ flex:1; display:flex; flex-direction:column; gap:1px; min-width:0; }}
  .lbl {{ font-size:13.5px; font-weight:600; color:var(--text); line-height:1.3;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
  .lbl-sub {{ font-size:11px; font-weight:500; color:var(--sub); line-height:1.3;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
  .ctrl {{ display:flex; align-items:center; gap:8px; flex-shrink:0; max-width:55%; }}
  /* ── Inputs ───────────────────────────────────────────────── */
  .val {{ font-size:13px; font-weight:600; color:var(--text);
    background:var(--input-bg); border:1px solid var(--input-border);
    border-radius:10px; padding:6px 10px; min-width:72px; max-width:128px; text-align:right;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
  .val.ph {{ color:var(--sub); font-weight:400; min-width:52px; }}
  .val.mint {{ color:var(--mint); font-weight:700; border-color:rgba(51,160,137,0.15);
    background:rgba(51,160,137,0.06); }}
  /* ── Benefit rows ─────────────────────────────────────────── */
  .ben {{ display:flex; align-items:center; gap:12px; padding:13px 16px; }}
  .ben-check {{ flex-shrink:0; }}
  .ben-text {{ flex:1; font-size:14px; font-weight:500; color:var(--text); line-height:1.4; }}
  .ben-remove {{ width:32px; height:32px; border-radius:8px; border:none; background:transparent;
    color:var(--sub); cursor:pointer; display:flex; align-items:center; justify-content:center;
    transition:background .15s ease; }}
  .ben-remove:hover {{ background:rgba(239,68,68,.10); color:#EF4444; }}
  .add-row {{ width:100%; display:flex; align-items:center; gap:10px;
    padding:14px 16px; border:none; background:transparent; cursor:pointer;
    border-top:1px dashed var(--border); color:var(--mint); font-size:14px; font-weight:700;
    font-family:inherit; transition:background .15s ease; }}
  .add-row:hover {{ background:rgba(51,160,137,0.06); }}
  /* ── Durations (1:1) ──────────────────────────────────────── */
  .drow {{ padding:13px 16px; }}
  .dmin-block {{ flex:1; display:flex; flex-direction:column; gap:2px; }}
  .dmin {{ font-size:16px; font-weight:700; color:var(--text); letter-spacing:-.01em; }}
  .dmin-sub {{ font-size:11px; font-weight:600; color:var(--sub); text-transform:uppercase; letter-spacing:.08em; }}
  /* ── Day rows (1:1) — multi-slot ──────────────────────────── */
  .day-row {{ border:none; cursor:pointer; padding:12px 14px; }}
  .day-row .day-ctrl {{ flex:1; justify-content:flex-end; min-width:0; }}
  .day-row .day-ctrl > .lbl-sub {{ font-size:12px; line-height:1.4;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .day-closed {{ font-size:12px; font-weight:600; color:var(--sub);
    padding:4px 10px; border-radius:999px; background:var(--input-bg);
    border:1px solid var(--input-border); }}
  /* ── Closed dates chips ───────────────────────────────────── */
  .closed-grid {{ display:flex; flex-wrap:wrap; gap:8px; padding:14px 14px 10px; }}
  .chip-closed {{ display:flex; align-items:center; gap:8px;
    padding:8px 6px 8px 14px; border-radius:14px;
    background:rgba(245,158,11,.08); border:1px solid rgba(245,158,11,.25); }}
  .chip-closed-date {{ font-size:13px; font-weight:700; color:#F59E0B; }}
  .chip-closed-sub {{ font-size:11px; font-weight:500; color:var(--sub); }}
  .chip-x {{ width:24px; height:24px; border-radius:999px; border:none;
    background:rgba(255,255,255,0.05); color:var(--sub); cursor:pointer;
    display:flex; align-items:center; justify-content:center; padding:0; }}
  /* ── Textarea (1:1 subject) ───────────────────────────────── */
  .ta-wrap {{ position:relative; padding:14px 16px; }}
  .ta {{ width:100%; padding:14px; border-radius:14px; border:1px solid var(--input-border);
    background:var(--input-bg); color:var(--text); font-size:14px; font-family:inherit;
    line-height:1.5; resize:none; outline:none; transition:border-color .18s ease, box-shadow .18s ease; }}
  .ta:focus {{ border-color:var(--mint); box-shadow:0 0 0 3px rgba(51,160,137,0.18); }}
  .ta::placeholder {{ color:var(--sub); }}
  .ta-count {{ position:absolute; right:24px; bottom:22px;
    font-size:10px; font-weight:600; color:var(--sub); }}
  /* ── Pack list (Packages) ─────────────────────────────────── */
  .pack-row {{ width:100%; display:flex; align-items:center; gap:14px; padding:14px 16px;
    border:none; background:transparent; cursor:pointer; font-family:inherit; text-align:left; }}
  .pack-thumb {{ width:48px; height:48px; border-radius:14px; display:flex; align-items:center;
    justify-content:center; flex-shrink:0; box-shadow:0 4px 12px rgba(255,180,162,.30); }}
  .pack-meta {{ flex:1; min-width:0; }}
  .pack-name {{ display:block; font-size:15px; font-weight:700; color:var(--text); letter-spacing:-.01em; }}
  .pack-sub {{ display:block; font-size:12px; font-weight:500; color:var(--sub); margin-top:2px; }}
  /* ── Services header (Packages) ───────────────────────────── */
  .services-header {{ padding:14px 16px 6px; font-size:11px; font-weight:700;
    letter-spacing:.08em; text-transform:uppercase; color:var(--section);
    border-top:1px solid var(--border); margin-top:0; }}
  /* ── Price block (Packages) ───────────────────────────────── */
  .price-block {{ border-top:1px solid var(--border); }}
  /* ── Toggle ───────────────────────────────────────────────── */
  .tog {{ width:46px; height:28px; border-radius:999px; background:var(--tog-off);
    position:relative; flex-shrink:0; transition:.2s ease; cursor:pointer; }}
  .tog.on {{ background:var(--mint); box-shadow:0 0 16px rgba(51,160,137,0.225); }}
  .knob {{ position:absolute; top:3px; left:3px; width:22px; height:22px; border-radius:999px;
    background:#fff; transition:.2s ease;
    box-shadow:0 2px 6px rgba(0,0,0,.20); }}
  .tog.on .knob {{ left:21px; }}
  /* ── Note ─────────────────────────────────────────────────── */
  .note {{ font-size:12px; line-height:1.55; color:var(--sub);
    margin:18px 12px 8px; padding:0; }}
  .note b {{ color:var(--text); font-weight:700; }}
  /* ── CTA + bottom nav ─────────────────────────────────────── */
  .cta-wrap {{ position:absolute; left:0; right:0; bottom:0; z-index:55;
    padding:14px 16px 24px;
    background:transparent;
  }}
  .cta-wrap-view {{
    background:transparent;
    padding-top:20px;
  }}
  .cta {{ width:100%; height:54px; border:none; border-radius:999px;
    background:linear-gradient(135deg, {GRAD_A} 0%, {GRAD_B} 100%); color:#fff;
    font-family:inherit; font-size:15px; font-weight:800; letter-spacing:.01em;
    cursor:pointer; transition:transform .15s ease;
    box-shadow:0 8px 24px rgba(51,160,137,0.225), 0 0 0 1px rgba(255,255,255,.06) inset; }}
  .cta:active {{ transform:scale(0.98); }}
  .cta-sub {{ text-align:center; font-size:11px; font-weight:600;
    color:var(--sub); margin:8px 0 0; letter-spacing:.02em; }}
  /* ── Channel View (founder ref may28 18:24:45 — hero + overlap card) */
  .cv-hero-tall {{ position:relative; width:100%; aspect-ratio:1/1; overflow:hidden; }}
  .cv-hero-tall img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .cv-hero-fade {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,0) 60%, var(--page) 100%); }}
  /* Legacy compact hero kept for owner-profile views */
  .cv-hero-compact {{ position:relative; width:100%; aspect-ratio:4/3; overflow:hidden; }}
  .cv-hero-compact img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .cv-premium-tag {{ position:absolute; bottom:16px; left:16px; z-index:2;
    display:inline-flex; align-items:center; gap:6px;
    padding:7px 12px 7px 10px; border-radius:999px;
    background:linear-gradient(135deg, {GRAD_A} 0%, {GRAD_B} 100%);
    color:#fff; font-size:10px; font-weight:800; letter-spacing:.12em;
    box-shadow:0 4px 16px rgba(51,160,137,0.225);
  }}
  /* Overlapping card pattern + subtle mint identity glow (founder ref may28 18:44) */
  .cv-overlap-card {{ position:relative; z-index:5;
    margin:-72px 16px 0; padding:24px 24px 22px;
    border-radius:32px; background:var(--card);
    border:1px solid rgba(51,160,137,0.15);
    box-shadow:0 14px 40px rgba(0,0,0,{t['dim_shadow']}),
               0 0 0 1px rgba(51,160,137,0.08),
               0 0 32px rgba(51,160,137,0.1);
    text-align:center;
  }}
  .cv-title {{ font-size:26px; font-weight:800; margin:0 0 6px;
    color:var(--text); letter-spacing:-.02em; line-height:1.15; }}
  .cv-tagline {{ font-size:13px; font-weight:500; color:var(--sub);
    margin:0 0 18px; line-height:1.4; }}
  .cv-premium-pill {{ display:flex; align-items:center; justify-content:space-between;
    padding:14px 16px; border-radius:20px;
    background:var(--input-bg); border:1.5px solid rgba(51,160,137,0.15);
    box-shadow:0 0 18px rgba(51,160,137,0.12);
    margin-bottom:20px; text-align:left; }}
  .cv-premium-meta {{ flex:1; min-width:0; }}
  .cv-premium-label {{ display:block; font-size:10px; font-weight:700;
    letter-spacing:.12em; text-transform:uppercase; color:var(--sub); margin-bottom:4px; }}
  .cv-premium-price {{ margin:0; font-size:20px; font-weight:800;
    color:var(--text); letter-spacing:-.01em; }}
  .cv-premium-price span {{ font-size:12px; font-weight:500; color:var(--sub); }}
  .cv-premium-star {{ width:36px; height:36px; border-radius:999px;
    background:rgba(51,160,137,0.12); display:flex; align-items:center; justify-content:center;
    flex-shrink:0; box-shadow:0 0 16px rgba(51,160,137,0.15); }}
  .cv-included {{ font-size:11px; font-weight:700; letter-spacing:.10em;
    text-transform:uppercase; color:var(--sub); margin:0 0 12px;
    text-align:left; }}
  .cv-perks-simple {{ display:flex; flex-direction:column; gap:12px; text-align:left; }}
  .cv-perk-simple {{ display:flex; align-items:center; gap:12px;
    font-size:13px; font-weight:500; color:var(--text); }}
  .cv-check-small {{ flex-shrink:0; width:20px; height:20px; border-radius:999px;
    background:var(--mint); display:flex; align-items:center; justify-content:center;
    box-shadow:0 2px 6px rgba(51,160,137,0.15); }}
  /* Legacy perks-list kept for owner profile views */
  .cv-perks-list {{ display:flex; flex-direction:column; gap:10px;
    padding:0 16px 20px; }}
  .cv-perk-row {{ display:flex; align-items:center; gap:14px;
    padding:12px 14px; border-radius:24px;
    background:var(--card); border:1px solid var(--border);
  }}
  .cv-perk-icon {{ width:42px; height:42px; border-radius:13px;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
    box-shadow:0 0 18px currentColor;
    filter:drop-shadow(0 0 10px currentColor);
  }}
  .cv-perk-text {{ flex:1; min-width:0; }}
  .cv-perk-text h4 {{ font-size:14px; font-weight:700; margin:0 0 2px;
    color:var(--text); letter-spacing:-.01em; line-height:1.25; }}
  .cv-perk-text p {{ font-size:11.5px; font-weight:500; margin:0;
    color:var(--sub); line-height:1.35;
    overflow:hidden; text-overflow:ellipsis; display:-webkit-box;
    -webkit-line-clamp:2; -webkit-box-orient:vertical;
  }}
  /* ── Sprint C v2 · CANONICAL profile (founder ref may28 19:07) ───── */
  .prof-cover-strip {{ position:relative; width:100%; aspect-ratio:21/9; overflow:hidden; }}
  .prof-cover-strip img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .prof-back, .prof-more {{ position:absolute; top:12px; width:34px; height:34px;
    border:none; border-radius:999px; background:rgba(0,0,0,0.35);
    -webkit-backdrop-filter:blur(10px); backdrop-filter:blur(10px);
    display:flex; align-items:center; justify-content:center; cursor:pointer; z-index:5; }}
  .prof-back {{ left:12px; }} .prof-more {{ right:12px; }}
  /* Avatar : CENTERED above name/bio (founder may30 — was left-aligned, broke symmetry) */
  .prof-head {{ display:flex; align-items:flex-end; justify-content:center;
    padding:0 16px; margin-top:-40px; }}
  .prof-avatar {{ position:relative; }}
  .prof-avatar img {{ width:88px; height:88px; border-radius:999px; object-fit:cover;
    border:4px solid var(--page); box-shadow:0 6px 18px rgba(0,0,0,.3); }}
  .prof-verified {{ position:absolute; bottom:2px; right:2px; width:24px; height:24px;
    border-radius:999px; background:var(--mint);
    display:flex; align-items:center; justify-content:center;
    border:2.5px solid var(--page); }}
  .prof-actions {{ display:flex; align-items:center; gap:8px; padding-bottom:6px; }}
  /* Actions row : Follow FULL-WIDTH + small share icon (Instagram canonical) — symmetric */
  .prof-actions-row {{ display:flex; align-items:center; gap:10px;
    padding:0 16px 16px; }}
  .prof-actions-row .prof-follow-btn {{ flex:1; padding:0; height:42px; font-size:14px; }}
  .prof-actions-row .prof-msg-icon {{ flex-shrink:0; width:42px; height:42px; }}
  /* Grid 3-col uniform (founder ref) */
  .prof-grid-uniform {{ display:grid; grid-template-columns:repeat(3,1fr);
    gap:6px; padding:0 16px 90px; }}
  .prof-tile-uniform {{ position:relative; aspect-ratio:1/1; border-radius:16px; overflow:hidden;
    box-shadow:0 2px 8px rgba(0,0,0,.15); }}
  .prof-tile-uniform img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .prof-follow-btn {{ height:36px; padding:0 20px; border:none; border-radius:999px;
    background:linear-gradient(135deg, {GRAD_A} 0%, {GRAD_B} 100%); color:#fff;
    font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; box-shadow:0 4px 14px rgba(51,160,137,0.175); }}
  .prof-msg-icon {{ width:36px; height:36px;
    border:1.5px solid rgba(51,160,137,0.225);
    border-radius:999px; background:var(--card); color:var(--mint);
    display:flex; align-items:center; justify-content:center; cursor:pointer;
    box-shadow:0 0 18px rgba(51,160,137,0.15),
               0 0 0 1px rgba(51,160,137,0.15) inset;
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.2)); }}
  .prof-meta {{ padding:12px 16px 6px; text-align:center; }}
  .prof-name {{ font-size:19px; font-weight:800; margin:0 0 3px;
    color:var(--text); letter-spacing:-.01em; }}
  .prof-role {{ font-size:13px; font-weight:500; color:var(--sub); margin:0 0 8px; }}
  .prof-stats {{ display:flex; gap:24px; }}
  .prof-stat {{ display:flex; align-items:baseline; gap:5px; }}
  .prof-stat-num {{ font-size:14px; font-weight:800; color:var(--text); }}
  .prof-stat-lbl {{ font-size:12px; font-weight:500; color:var(--sub); }}
  /* Bio + hashtags */
  .prof-bio {{ font-size:13px; font-weight:500; color:var(--sub);
    margin:8px 0 0; line-height:1.5; text-align:center; padding:0 16px; }}
  .prof-tag {{ color:var(--mint); font-weight:700; }}
  /* Stats bordered row (hairlines top + bottom) */
  .prof-stats-bordered {{ display:grid; grid-template-columns:repeat(3,1fr);
    margin:16px 16px 18px; padding:14px 0;
    border-top:1px solid var(--border); border-bottom:1px solid var(--border); }}
  .prof-stat-cell {{ display:flex; flex-direction:column; align-items:center; gap:4px; }}
  .prof-stat-cell .prof-stat-num {{ font-size:20px; font-weight:800; color:var(--text); letter-spacing:-.02em; }}
  .prof-stat-cell .prof-stat-lbl {{ font-size:10px; font-weight:700; color:var(--sub);
    letter-spacing:.10em; text-transform:uppercase; }}
  /* Main tab pills (Lifestyle / Channel) — canonical home_feed style */
  .prof-main-pills {{ display:grid; grid-template-columns:1fr 1fr; gap:4px;
    margin:0 16px 10px; padding:4px; border-radius:999px;
    background:var(--input-bg); border:1px solid var(--input-border); }}
  .prof-main-pill {{ padding:10px 0; border:none; border-radius:999px;
    background:transparent; color:var(--sub);
    font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; transition:.18s ease;
    display:inline-flex; align-items:center; justify-content:center; }}
  .prof-main-pill-on {{
    background:var(--card); color:var(--mint);
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 0 0 1px rgba(51,160,137,0.225),
               0 2px 8px rgba(0,0,0,{t['dim_shadow']}); }}
  /* Sub-tabs (Posts / Peaks / Activities) — same pattern, smaller */
  .prof-sub-pills {{ display:grid; grid-template-columns:repeat(3,1fr); gap:4px;
    margin:0 16px 18px; padding:4px; border-radius:999px;
    background:var(--input-bg); border:1px solid var(--input-border); }}
  .prof-sub-pill {{ padding:8px 0; border:none; border-radius:999px;
    background:transparent; color:var(--sub);
    font-family:inherit; font-size:12px; font-weight:600;
    cursor:pointer; transition:.18s ease;
    display:inline-flex; align-items:center; justify-content:center; }}
  .prof-sub-pill-on {{ background:var(--card); color:var(--mint);
    box-shadow:0 0 14px rgba(51,160,137,0.15),
               0 0 0 1px rgba(51,160,137,0.2),
               0 2px 6px rgba(0,0,0,{t['dim_shadow']}); }}
  /* Tab content (1:1 booking content) */
  .prof-content {{ padding:0 16px 16px; }}
  .prof-content-title {{ font-size:18px; font-weight:800; margin:0 0 4px;
    color:var(--text); letter-spacing:-.01em; text-align:center; }}
  .prof-content-body {{ font-size:12.5px; font-weight:500; color:var(--sub);
    margin:0 0 18px; line-height:1.4; text-align:center; }}
  .prof-content-label {{ font-size:10px; font-weight:700; letter-spacing:.10em;
    text-transform:uppercase; color:var(--sub); margin:0 0 10px; }}
  .prof-day-scroll {{ display:flex; gap:8px; padding:0 0 18px;
    overflow-x:auto; scrollbar-width:none; }}
  .prof-day-scroll::-webkit-scrollbar {{ display:none; }}
  .prof-day-card {{ flex-shrink:0; min-width:54px; padding:10px 0; border-radius:14px;
    border:1px solid var(--input-border); background:var(--card);
    display:flex; flex-direction:column; align-items:center; gap:3px;
    font-family:inherit; cursor:pointer; transition:.18s ease; }}
  .prof-day-card span {{ font-size:10px; font-weight:700; color:var(--sub); text-transform:uppercase; letter-spacing:.06em; }}
  .prof-day-card b {{ font-size:18px; font-weight:800; color:var(--text); letter-spacing:-.02em; }}
  .prof-day-card-on {{
    background:var(--card);
    border-color:rgba(51,160,137,0.225);
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 0 0 1px rgba(51,160,137,0.15),
               0 2px 8px rgba(0,0,0,{t['dim_shadow']}); }}
  .prof-day-card-on span, .prof-day-card-on b {{ color:var(--mint); }}
  .prof-slots-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px;
    padding-bottom:80px; }}
  .prof-slot {{ padding:13px 0; border-radius:12px;
    border:1px solid var(--input-border); background:var(--card);
    font-family:inherit; font-size:13px; font-weight:700; color:var(--text);
    cursor:pointer; transition:.18s ease; }}
  .prof-slot-on {{ background:rgba(51,160,137,0.12); border-color:var(--mint); color:var(--mint);
    box-shadow:0 4px 14px rgba(51,160,137,0.22); }}
  .prof-slot-off {{ color:var(--sub); text-decoration:line-through; opacity:.45; cursor:not-allowed; }}
  /* ── NEW canonical bottom nav (cn-bnav classes) — uses EXACT SVG paths from
     v2_canonical_home_feed Stitch dump (founder may30 lock). Replaces .bnav-canonical. */
  .cn-bnav {{ position:absolute; bottom:0; left:0; right:0; z-index:80;
    display:flex; justify-content:space-around; align-items:center;
    padding:14px 24px 18px env(safe-area-inset-bottom,18px);
    background:var(--card); border-top:1px solid var(--border);
    border-radius:28px 28px 0 0; box-shadow:0 -4px 24px rgba(0,0,0,{t['dim_shadow']}); }}
  .cn-bnav-item {{ position:relative; width:48px; height:48px;
    border:none; background:transparent; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }}
  .cn-bnav-on {{ filter:drop-shadow(0 0 6px rgba(51,160,137,0.275)); }}
  .cn-bnav-bar {{ position:absolute; bottom:-6px; left:50%; transform:translateX(-50%);
    width:24px; height:3px; border-radius:999px; background:var(--mint);
    box-shadow:0 0 8px rgba(51,160,137,0.3); }}
  .cn-bnav-create {{ width:48px; height:48px; border-radius:999px;
    border:1.5px solid rgba(51,160,137,0.225); background:var(--card); cursor:pointer;
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 4px 12px rgba(51,160,137,0.2),
               0 0 0 1px rgba(51,160,137,0.15) inset;
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.2)); }}
  .cn-bnav-profile {{ width:48px; height:48px; border:none; background:transparent; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }}
  .cn-bnav-profile img {{ width:32px; height:32px; border-radius:12px;
    object-fit:cover; opacity:.85;
    outline:1.5px solid transparent; transition:.18s ease; }}
  .cn-bnav-profile-on img {{ opacity:1;
    outline:2px solid var(--mint); outline-offset:2px;
    box-shadow:0 0 8px rgba(51,160,137,0.225); }}
  /* ── DEPRECATED below — kept only to avoid breaking any stale markup not yet migrated */
  .bnav-canonical {{
    position:absolute; left:0; right:0; bottom:0; z-index:80;
    display:flex; justify-content:space-around; align-items:center;
    padding:14px 24px 18px env(safe-area-inset-bottom,0);
    background:var(--card);
    border-top:1px solid var(--border);
    border-radius:28px 28px 0 0;
    box-shadow:0 -4px 24px rgba(0,0,0,{t['dim_shadow']}); }}
  /* Slot icon T4 — 48px hit area, 24px glyph, no bg, no border */
  .bnav-item {{ position:relative;
    display:flex; align-items:center; justify-content:center;
    width:48px; height:48px; border:none; background:none;
    color:var(--sub); cursor:pointer; transition:.15s ease; }}
  .bnav-item ion-icon {{ font-size:24px; }}
  /* Active state — mint icon + halo + small bar below */
  .bnav-item.bnav-on {{ color:var(--mint);
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.275)); }}
  .bnav-bar {{ position:absolute; bottom:2px; left:50%; transform:translateX(-50%);
    width:24px; height:3px; border-radius:999px; background:var(--mint);
    box-shadow:0 0 8px rgba(51,160,137,0.3); }}
  /* Center create FAB — pill-active-dark pattern (card bg + mint border + mint icon glow) */
  .bnav-create {{ display:flex; align-items:center; justify-content:center;
    width:48px; height:48px; border:1.5px solid rgba(51,160,137,0.225);
    border-radius:999px; background:var(--card); color:var(--mint);
    cursor:pointer;
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 4px 12px rgba(51,160,137,0.2),
               0 0 0 1px rgba(51,160,137,0.15) inset;
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.2)); }}
  /* Profile slot — SQUARE avatar 32×32, mint outline frame (founder may29 lock) */
  .bnav-profile {{ position:relative;
    display:flex; align-items:center; justify-content:center;
    width:48px; height:48px; border:none; background:none; cursor:pointer; }}
  .bnav-profile img {{ width:32px; height:32px; object-fit:cover;
    border-radius:12px;
    outline:1.5px solid transparent;
    transition:.18s ease; opacity:.85; }}
  .bnav-profile.bnav-profile-on img {{ opacity:1;
    outline:2px solid var(--mint); outline-offset:2px;
    box-shadow:0 0 8px rgba(51,160,137,0.225); }}
  /* Tab pills (legacy — kept for back-compat) */
  .prof-tabs-pills {{ display:flex; gap:6px; padding:0 16px 12px;
    overflow-x:auto; scrollbar-width:none; }}
  .prof-tabs-pills::-webkit-scrollbar {{ display:none; }}
  .prof-tab-pill {{ flex-shrink:0; padding:8px 14px; border-radius:999px; border:none;
    background:transparent; color:var(--sub);
    font-family:inherit; font-size:13px; font-weight:600;
    cursor:pointer; transition:.15s ease; }}
  .prof-tab-pill-on {{ background:var(--card); color:var(--mint);
    box-shadow:0 0 14px rgba(51,160,137,0.15),
               0 0 0 1px rgba(51,160,137,0.2),
               0 2px 6px rgba(0,0,0,{t['dim_shadow']}); }}
  .prof-tab-pill-has-sub {{ display:inline-flex; align-items:center; }}
  /* 3-col uniform grid (matches canonical ref) */
  .prof-grid-3col {{ display:grid; grid-template-columns:repeat(3,1fr);
    gap:8px; padding:0 16px 16px; }}
  .prof-tile {{ position:relative; aspect-ratio:1/1; border-radius:18px; overflow:hidden;
    box-shadow:0 4px 12px rgba(0,0,0,.15); }}
  .prof-tile img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  /* ── (legacy Sprint C profile classes kept below for back-compat) ── */
  .profile-cover {{ position:relative; width:100%; aspect-ratio:16/9; overflow:hidden; }}
  .profile-cover img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .profile-cover-fade {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,0.25) 0%, transparent 40%, rgba(0,0,0,0.40) 100%); }}
  .profile-back, .profile-more {{ position:absolute; top:14px; width:34px; height:34px;
    border:none; border-radius:999px; background:rgba(0,0,0,0.40);
    -webkit-backdrop-filter:blur(10px); backdrop-filter:blur(10px);
    display:flex; align-items:center; justify-content:center; cursor:pointer; z-index:5; }}
  .profile-back {{ left:12px; }}
  .profile-more {{ right:12px; }}
  .profile-header {{ position:relative; padding:0 16px 12px; margin-top:-44px; z-index:5; text-align:center; }}
  .profile-avatar-wrap {{ position:relative; display:inline-block; }}
  .profile-avatar-wrap img {{ width:88px; height:88px; border-radius:999px;
    object-fit:cover; border:4px solid var(--page);
    box-shadow:0 6px 16px rgba(0,0,0,.25); }}
  .profile-verified {{ position:absolute; bottom:2px; right:2px;
    width:24px; height:24px; border-radius:999px; background:var(--mint);
    display:flex; align-items:center; justify-content:center;
    border:2.5px solid var(--page); }}
  .profile-name {{ font-size:22px; font-weight:800; margin:10px 0 4px;
    color:var(--text); letter-spacing:-.02em; }}
  .profile-bio {{ font-size:13px; font-weight:500; color:var(--sub);
    margin:0 12px 14px; line-height:1.4; }}
  .profile-stats {{ display:flex; justify-content:center; gap:36px; margin-bottom:16px; }}
  .profile-stat {{ display:flex; flex-direction:column; gap:1px; align-items:center; }}
  .profile-stat-num {{ font-size:17px; font-weight:800; color:var(--text); letter-spacing:-.01em; }}
  .profile-stat-lbl {{ font-size:11px; font-weight:600; color:var(--sub); }}
  .profile-cta-row {{ display:flex; gap:8px; padding:0 16px; }}
  .profile-cta-secondary {{ flex:1; height:40px; border:1px solid var(--input-border);
    background:var(--card); color:var(--text); border-radius:12px;
    font-family:inherit; font-size:13px; font-weight:700; cursor:pointer; }}
  .profile-cta-primary {{ flex:1; height:40px; border:none;
    background:linear-gradient(135deg, {GRAD_A} 0%, {GRAD_B} 100%); color:#fff;
    border-radius:12px; font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; box-shadow:0 4px 14px rgba(51,160,137,0.15); }}
  .profile-cta-icon {{ width:40px; height:40px; border-radius:12px;
    border:1px solid var(--input-border); background:var(--card);
    color:var(--text); display:flex; align-items:center; justify-content:center; cursor:pointer; }}
  .profile-tabs {{ display:flex; gap:14px; padding:14px 16px 8px;
    overflow-x:auto; scrollbar-width:none; }}
  .profile-tabs::-webkit-scrollbar {{ display:none; }}
  .profile-tab {{ flex-shrink:0; padding:8px 2px; border:none; background:transparent;
    font-family:inherit; font-size:13px; font-weight:600; color:var(--sub);
    cursor:pointer; border-bottom:2px solid transparent; }}
  .profile-tab-on {{ color:var(--text); font-weight:700; border-bottom-color:var(--mint); }}
  /* Layout 3 hybride : featured + 2-col grid + video horizontal (CANONIC validated may28) */
  .profile-grid {{ display:grid; grid-template-columns:2fr 1fr 1fr;
    gap:4px; padding:4px 4px 16px; }}
  .profile-grid-featured {{ grid-column:1; grid-row:1/3; position:relative;
    aspect-ratio:2/3; border-radius:6px; overflow:hidden; }}
  .profile-grid-side {{ display:contents; }}
  .profile-grid-tile {{ position:relative; aspect-ratio:1/1; border-radius:6px; overflow:hidden;
    grid-row:auto; }}
  .profile-grid-video {{ position:relative; grid-column:1/4; aspect-ratio:16/9;
    border-radius:6px; overflow:hidden; }}
  .profile-grid img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .profile-grid-badge {{ position:absolute; bottom:6px; right:6px;
    display:inline-flex; align-items:center; gap:3px;
    padding:3px 7px; border-radius:999px;
    background:rgba(0,0,0,.55); color:#fff;
    font-size:10px; font-weight:700; }}
  .profile-grid-play {{ position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
    width:44px; height:44px; border-radius:999px;
    background:rgba(0,0,0,.55); -webkit-backdrop-filter:blur(6px); backdrop-filter:blur(6px);
    display:flex; align-items:center; justify-content:center; }}
  /* ── Owner profile (B) ────────────────────────────────────── */
  .manage-chip {{
    position:absolute; top:14px; right:14px;
    display:inline-flex; align-items:center; gap:6px;
    padding:7px 12px 7px 10px; border-radius:999px;
    background:rgba(255,255,255,0.18);
    -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    color:#fff; font-size:11px; font-weight:700;
    text-decoration:none; cursor:pointer;
    border:1px solid rgba(255,255,255,0.22);
  }}
  .manage-chip-inline {{
    position:static; flex-shrink:0;
    background:rgba(51,160,137,0.12); color:var(--mint);
    border:1px solid rgba(51,160,137,0.15);
  }}
  .owner-stats {{
    display:grid; grid-template-columns:repeat(3,1fr); gap:8px;
    padding:0 16px 16px;
  }}
  .owner-stat {{
    display:flex; flex-direction:column; align-items:center; gap:2px;
    padding:12px 6px; border-radius:14px;
    background:var(--card); border:1px solid var(--border);
  }}
  .owner-stat-num {{ font-size:18px; font-weight:800; color:var(--text); letter-spacing:-.02em; }}
  .owner-stat-label {{ font-size:10px; font-weight:600; color:var(--sub);
    text-align:center; letter-spacing:.02em; }}
  .owner-banner {{
    display:flex; align-items:center; gap:12px;
    margin:20px 16px 16px;
    padding:14px; border-radius:22px;
    background:var(--card); border:1px solid rgba(51,160,137,0.15);
    box-shadow:0 0 0 1px rgba(51,160,137,0.05),
               0 0 22px rgba(51,160,137,0.08);
  }}
  .owner-banner-icon {{ width:48px; height:48px; border-radius:14px;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
    box-shadow:0 0 18px currentColor;
    filter:drop-shadow(0 0 10px currentColor);
  }}
  .owner-banner-text {{ flex:1; min-width:0; }}
  .owner-banner-text h2 {{ font-size:15px; font-weight:800; margin:0 0 2px;
    color:var(--text); letter-spacing:-.01em; }}
  .owner-banner-text p {{ font-size:11.5px; font-weight:500; margin:0;
    color:var(--sub); }}
  /* ── Upcoming sessions list (1:1 owner) ───────────────────── */
  .upcoming-list {{ display:flex; flex-direction:column; gap:8px; padding:0 4px; }}
  .upcoming-row {{
    display:flex; align-items:center; gap:12px;
    padding:12px 14px; border-radius:18px;
    background:var(--card); border:1.5px solid rgba(51,160,137,0.18);
    box-shadow:0 0 18px rgba(51,160,137,0.08),
               0 4px 12px rgba(0,0,0,{t['dim_shadow']});
  }}
  .upcoming-when {{ display:flex; flex-direction:column; gap:1px; min-width:80px; }}
  .upcoming-day {{ font-size:13px; font-weight:700; color:var(--text); }}
  .upcoming-time {{ font-size:11px; font-weight:500; color:var(--sub); }}
  .upcoming-who {{ flex:1; display:flex; align-items:center; gap:8px; min-width:0; }}
  .upcoming-who img {{ width:28px; height:28px; border-radius:999px; object-fit:cover; }}
  .upcoming-who span {{ font-size:13px; font-weight:600; color:var(--text);
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
  .upcoming-status {{ font-size:10px; font-weight:700; letter-spacing:.05em;
    padding:4px 8px; border-radius:999px; text-transform:uppercase; }}
  .upcoming-status-ok {{ background:rgba(51,160,137,0.12); color:var(--mint); }}
  /* ── Pack card (owner profile packs) ──────────────────────── */
  .pack-card {{
    display:flex; align-items:center; gap:12px;
    padding:12px 14px; border-radius:20px; margin-bottom:10px;
    background:var(--card); border:1.5px solid rgba(51,160,137,0.18);
    box-shadow:0 0 18px rgba(51,160,137,0.08),
               0 4px 12px rgba(0,0,0,{t['dim_shadow']});
    cursor:pointer; transition:.15s ease;
  }}
  .pack-card-thumb {{ width:44px; height:44px; border-radius:13px;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
  }}
  .pack-card-meta {{ flex:1; min-width:0; }}
  .pack-card-name {{ display:block; font-size:14px; font-weight:700; color:var(--text); letter-spacing:-.01em; }}
  .pack-card-sub {{ display:block; font-size:11.5px; font-weight:500; color:var(--sub); margin-top:2px; }}
  /* ── Ghost CTA (for owner profile views) ──────────────────── */
  .cta-ghost {{
    background:transparent !important;
    color:var(--mint) !important;
    border:1.5px solid var(--mint) !important;
    box-shadow:none !important;
  }}
  /* ── 1:1 booking view (visitor) ───────────────────────────── */
  .bv-hero {{ text-align:center; padding:30px 24px 18px; }}
  .bv-avatar-wrap {{ position:relative; display:inline-block; }}
  .bv-avatar-wrap img {{ width:80px; height:80px; border-radius:999px;
    object-fit:cover; box-shadow:0 0 0 3px var(--mint); }}
  .bv-verified {{ position:absolute; bottom:-2px; right:-2px;
    width:24px; height:24px; border-radius:999px; background:var(--mint);
    display:flex; align-items:center; justify-content:center;
    border:2.5px solid var(--page); }}
  .bv-name {{ font-size:22px; font-weight:800; margin:14px 0 4px;
    color:var(--text); letter-spacing:-.02em; }}
  .bv-role {{ font-size:13px; font-weight:500; color:var(--sub); margin:0; }}
  .bv-section {{ padding:0 16px; margin-bottom:18px; }}
  .bv-durs {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; }}
  .bv-dur {{ display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:12px 4px; border-radius:14px; gap:2px;
    border:1px solid var(--input-border); background:var(--card);
    font-family:inherit; cursor:pointer; transition:.18s ease; }}
  .bv-dur span {{ font-size:18px; font-weight:800; color:var(--text); letter-spacing:-.02em; }}
  .bv-dur em {{ font-size:10px; font-weight:600; color:var(--sub); font-style:normal;
    letter-spacing:.02em; }}
  .bv-dur-on {{ background:rgba(51,160,137,0.1); border-color:var(--mint);
    box-shadow:0 4px 14px rgba(51,160,137,0.22); }}
  .bv-dur-on span, .bv-dur-on em {{ color:var(--mint); }}
  /* Weekday row (1:1 booking) */
  .bv-week-row {{ display:grid; grid-template-columns:repeat(7,1fr); gap:6px; margin-bottom:10px; }}
  .bv-day {{ display:flex; flex-direction:column; align-items:center; gap:3px;
    padding:10px 0; border-radius:12px;
    border:1px solid var(--input-border); background:var(--card);
    font-family:inherit; cursor:pointer; transition:.15s ease; }}
  .bv-day span {{ font-size:10px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; color:var(--sub); }}
  .bv-day b {{ font-size:15px; font-weight:800; color:var(--text); letter-spacing:-.01em; }}
  .bv-day-on {{ background:rgba(51,160,137,0.1); border-color:var(--mint);
    box-shadow:0 4px 14px rgba(51,160,137,0.22); }}
  .bv-day-on span, .bv-day-on b {{ color:var(--mint); }}
  .bv-day-disabled {{ opacity:.4; cursor:not-allowed; }}
  .bv-times {{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin-bottom:10px; }}
  .bv-time {{ padding:12px 0; border-radius:12px;
    border:1px solid var(--input-border); background:var(--card);
    font-family:inherit; font-size:14px; font-weight:700; color:var(--text);
    cursor:pointer; transition:.18s ease; }}
  .bv-time-on {{ background:rgba(51,160,137,0.1); border-color:var(--mint); color:var(--mint);
    box-shadow:0 4px 14px rgba(51,160,137,0.22); }}
  .bv-time-off {{ color:var(--sub); text-decoration:line-through; opacity:.55; cursor:not-allowed; }}
  .bv-date-pick {{ width:100%; display:flex; align-items:center; justify-content:center;
    gap:8px; padding:12px; border-radius:14px;
    background:rgba(51,160,137,0.06); border:1px dashed rgba(51,160,137,0.175);
    color:var(--mint); font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; }}
  /* Subject textarea (1:1 booking flow) */
  .bv-subject-wrap {{ position:relative; }}
  .bv-subject {{ width:100%; padding:14px 16px; border-radius:18px;
    background:var(--card); border:1.5px solid rgba(51,160,137,0.2);
    box-shadow:0 0 18px rgba(51,160,137,0.1);
    font-family:inherit; font-size:13px; color:var(--text); resize:none;
    line-height:1.5; outline:none; box-sizing:border-box;
    transition:border-color .15s ease, box-shadow .15s ease; }}
  .bv-subject:focus {{ border-color:var(--mint);
    box-shadow:0 0 24px rgba(51,160,137,0.25), 0 0 0 3px rgba(51,160,137,0.15); }}
  .bv-subject::placeholder {{ color:var(--sub); }}
  .bv-subject-count {{ position:absolute; bottom:10px; right:14px;
    font-size:10px; font-weight:600; color:var(--sub); }}
  /* ── Package visitor view ─────────────────────────────────── */
  .pv-price-block {{ display:flex; align-items:baseline; justify-content:center;
    gap:14px; padding:0 16px 8px; }}
  .pv-price-old {{ font-size:18px; font-weight:600; color:var(--sub);
    text-decoration:line-through; }}
  .pv-price-new {{ font-size:32px; font-weight:800; color:var(--mint); letter-spacing:-.02em; }}
  .pv-price-save {{ font-size:11px; font-weight:700; letter-spacing:.06em;
    text-transform:uppercase; padding:5px 10px; border-radius:999px;
    background:rgba(51,160,137,0.12); color:var(--mint); }}
  /* ── V2 BottomSheet popup (success + confirm-leave) ───────── */
  .sheet-scrim {{
    position:absolute; inset:0; z-index:200;
    background:rgba(0,0,0,0.45);
    -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    display:flex; align-items:flex-end; justify-content:center;
    opacity:0; pointer-events:none;
    transition:opacity .22s ease;
  }}
  .sheet-scrim[data-state="open"] {{ opacity:1; pointer-events:auto; }}
  .sheet {{
    width:100%; max-width:393px; box-sizing:border-box;
    background:var(--card); border-radius:28px 28px 0 0;
    padding:8px 24px max(28px, env(safe-area-inset-bottom, 24px));
    border-top:1.5px solid rgba(51,160,137,0.2);
    transform:translateY(100%); transition:transform .28s cubic-bezier(0.32,0.72,0,1);
    box-shadow:0 -16px 48px rgba(0,0,0,0.30),
               0 -8px 30px rgba(51,160,137,0.12);
  }}
  .sheet-scrim[data-state="open"] .sheet {{ transform:translateY(0); }}
  .sheet-handle {{
    width:38px; height:4px; border-radius:999px; background:var(--input-border);
    margin:8px auto 18px;
  }}
  .sheet-icon-wrap {{
    width:64px; height:64px; border-radius:999px;
    display:flex; align-items:center; justify-content:center;
    margin:0 auto 16px;
  }}
  .sheet-icon-wrap.success {{
    background:rgba(51,160,137,0.12);
    box-shadow:0 0 24px rgba(51,160,137,0.2);
  }}
  .sheet-icon-wrap.warn {{
    background:rgba(245,158,11,.12);
    box-shadow:0 0 24px rgba(245,158,11,.28);
  }}
  .sheet-title {{
    text-align:center; font-size:19px; font-weight:800;
    color:var(--text); margin:0 0 8px; letter-spacing:-.01em;
  }}
  .sheet-body {{
    text-align:center; font-size:14px; font-weight:500; line-height:1.5;
    color:var(--sub); margin:0 0 22px; padding:0 8px;
  }}
  .sheet-body b {{ color:var(--text); font-weight:700; }}
  .sheet-actions {{ display:flex; gap:10px; }}
  .sheet-actions-stacked {{ flex-direction:column; }}
  .sheet-btn {{
    flex:1; height:52px; border-radius:16px; border:none;
    font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; transition:transform .15s ease, opacity .15s ease;
  }}
  .sheet-btn:active {{ transform:scale(0.98); }}
  .sheet-btn-primary {{
    background:linear-gradient(135deg, {GRAD_A} 0%, {GRAD_B} 100%);
    color:#fff;
    box-shadow:0 6px 20px rgba(51,160,137,0.225);
  }}
  .sheet-btn-ghost {{
    background:transparent; color:var(--sub);
    border:1px solid var(--input-border);
  }}
  .sheet-btn-danger {{
    background:rgba(239,68,68,.10); color:#EF4444;
    border:1px solid rgba(239,68,68,.30);
  }}
  /* ── Channel price picker ────────────────────────────────── */
  .price-tier-list {{ display:flex; flex-direction:column; gap:8px;
    max-height:380px; overflow-y:auto; padding:4px 0; }}
  .price-tier-row {{ display:flex; align-items:center; justify-content:space-between;
    width:100%; padding:14px 16px; border-radius:16px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    font-family:inherit; cursor:pointer; transition:.15s ease;
    text-align:left; }}
  .price-tier-row:hover {{ border-color:rgba(51,160,137,0.175); }}
  .price-tier-on {{ background:rgba(51,160,137,0.08);
    border-color:var(--mint);
    box-shadow:0 0 18px rgba(51,160,137,0.22); }}
  .price-tier-meta {{ display:flex; flex-direction:column; gap:2px; }}
  .price-tier-amount {{ font-size:17px; font-weight:800; color:var(--text); letter-spacing:-.01em; }}
  .price-tier-on .price-tier-amount {{ color:var(--mint); }}
  .price-tier-label {{ font-size:11px; font-weight:500; color:var(--sub); letter-spacing:.02em; }}
  .price-tier-check {{ display:flex; align-items:center; }}
  /* ── Sheet text inputs ────────────────────────────────────── */
  .sheet-field-label {{ display:block; font-size:11px; font-weight:700;
    letter-spacing:.08em; text-transform:uppercase; color:var(--sub);
    margin:0 0 8px; }}
  .sheet-input {{ width:100%; padding:14px 16px; border-radius:14px;
    border:1px solid var(--input-border); background:var(--input-bg);
    font-family:inherit; font-size:15px; font-weight:600; color:var(--text);
    box-sizing:border-box; outline:none; transition:border-color .15s ease, box-shadow .15s ease; }}
  .sheet-input:focus {{ border-color:var(--mint); box-shadow:0 0 0 3px rgba(51,160,137,0.18); }}
  .sheet-input::placeholder {{ color:var(--sub); font-weight:400; }}
  .sheet-counter {{ display:block; text-align:right; font-size:11px; font-weight:600;
    color:var(--sub); margin:6px 4px 0; }}
  .date-row {{ display:flex; gap:10px; }}
  .date-col {{ flex:1; min-width:0; }}
  /* ── Lifecycle status banner (subscribed/purchased) ───────── */
  .state-status {{ display:flex; align-items:center; gap:12px;
    margin:14px 16px 6px; padding:12px 14px;
    border-radius:16px; background:rgba(51,160,137,0.08);
    border:1px solid rgba(51,160,137,0.25); }}
  .state-status-text h4 {{ font-size:13px; font-weight:700; margin:0 0 2px; color:var(--text); letter-spacing:-.01em; }}
  .state-status-text p {{ font-size:11px; font-weight:500; margin:0; color:var(--sub); line-height:1.35; }}
  /* ── Booking confirmation (Ref founder may28 18:24) ───────── */
  .confirm-hero {{ text-align:center; padding:48px 32px 24px; }}
  .confirm-check-wrap {{ position:relative; width:88px; height:88px;
    margin:0 auto 22px; }}
  .confirm-check-ring {{ position:absolute; inset:0; border-radius:999px;
    background:radial-gradient(circle, rgba(51,160,137,0.15) 0%, rgba(51,160,137,0) 70%);
    filter:blur(6px); }}
  .confirm-check-inner {{ position:absolute; inset:14px; border-radius:999px;
    background:rgba(51,160,137,0.1); border:2px solid rgba(51,160,137,0.15);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 24px rgba(51,160,137,0.175); }}
  .confirm-title {{ font-size:26px; font-weight:800; margin:0 0 12px;
    color:var(--text); letter-spacing:-.02em; }}
  .confirm-body {{ font-size:14px; font-weight:500; color:var(--sub);
    margin:0 12px; line-height:1.5; }}
  .confirm-card {{ margin:8px 24px 24px; padding:18px; border-radius:24px;
    background:var(--card); border:1px solid rgba(51,160,137,0.15);
    box-shadow:0 8px 24px rgba(0,0,0,{t['dim_shadow']}),
               0 0 0 1px rgba(51,160,137,0.06),
               0 0 28px rgba(51,160,137,0.08); }}
  .confirm-coach {{ display:flex; align-items:center; gap:12px; margin-bottom:18px; }}
  .confirm-coach-avatar {{ width:38px; height:38px; border-radius:999px; object-fit:cover; }}
  .confirm-coach-meta {{ display:flex; flex-direction:column; gap:0; }}
  .confirm-coach-label {{ font-size:10px; font-weight:700; letter-spacing:.10em;
    text-transform:uppercase; color:var(--sub); }}
  .confirm-coach-name {{ font-size:15px; font-weight:800; color:var(--text); letter-spacing:-.01em; }}
  .confirm-grid {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:18px;
    padding-top:18px; border-top:1px solid var(--border); }}
  .confirm-grid-col {{ display:flex; flex-direction:column; gap:8px; }}
  .confirm-grid-icon {{ display:flex; align-items:center; gap:6px;
    font-size:10px; font-weight:700; letter-spacing:.10em;
    color:var(--sub); text-transform:uppercase; }}
  .confirm-grid-val {{ font-size:15px; font-weight:800; color:var(--text);
    letter-spacing:-.01em; line-height:1.2; }}
  .confirm-calendar-btn {{ width:100%; padding:13px; border:1px solid var(--border);
    border-radius:14px; background:transparent; color:var(--text);
    font-family:inherit; font-size:13px; font-weight:600;
    display:flex; align-items:center; justify-content:center; gap:8px;
    cursor:pointer; }}
  /* ── IAP sheet (Apple StoreKit mock) ──────────────────────── */
  .sheet-iap {{ padding-top:8px; }}
  .iap-header {{ display:flex; align-items:center; gap:14px; margin-bottom:18px;
    padding-bottom:16px; border-bottom:1px solid var(--border); }}
  .iap-apple-icon {{ width:44px; height:44px; border-radius:11px;
    background:var(--input-bg); border:1px solid var(--input-border);
    display:flex; align-items:center; justify-content:center; }}
  .iap-merchant h4 {{ font-size:15px; font-weight:700; margin:0; color:var(--text); }}
  .iap-merchant p {{ font-size:12px; font-weight:500; margin:0; color:var(--sub); }}
  .iap-item {{ display:flex; align-items:center; justify-content:space-between;
    padding:14px; border-radius:14px; background:var(--input-bg);
    border:1px solid var(--input-border); margin-bottom:16px; }}
  .iap-item-meta {{ display:flex; flex-direction:column; gap:2px; }}
  .iap-item-label {{ font-size:14px; font-weight:700; color:var(--text); }}
  .iap-item-sub {{ font-size:11px; font-weight:500; color:var(--sub); }}
  .iap-item-price {{ font-size:18px; font-weight:800; color:var(--text); letter-spacing:-.01em; }}
  .iap-tos {{ font-size:11px; line-height:1.5; color:var(--sub);
    text-align:center; margin:0 0 18px; padding:0 8px; }}
  .iap-tos b {{ color:var(--text); }}
  .iap-confirm-btn {{ width:100%; height:54px; border:none; border-radius:16px;
    background:var(--text); color:var(--page); font-family:inherit;
    font-size:15px; font-weight:700;
    display:flex; align-items:center; justify-content:center; gap:10px;
    cursor:pointer; margin-bottom:8px; }}
  .iap-confirm-btn ion-icon {{ color:var(--page) !important; }}
  .iap-cancel-btn {{ width:100%; height:44px; border:none; background:transparent;
    color:var(--mint); font-family:inherit; font-size:14px; font-weight:600;
    cursor:pointer; }}
  /* ── Loading spinner ──────────────────────────────────────── */
  .sheet-loading {{ text-align:center; padding:32px 24px max(28px, env(safe-area-inset-bottom, 24px)); }}
  .loader {{ width:48px; height:48px; border:3px solid var(--input-border);
    border-top-color:var(--mint); border-radius:50%;
    animation:spin 0.8s linear infinite; margin:0 auto; }}
  @keyframes spin {{ to {{ transform:rotate(360deg); }} }}
  /* ── Sheet textarea (book-objective) ──────────────────────── */
  .sheet-textarea {{ width:100%; padding:14px; border-radius:14px;
    border:1px solid var(--input-border); background:var(--input-bg);
    font-family:inherit; font-size:14px; font-weight:500; color:var(--text);
    box-sizing:border-box; outline:none; resize:none; line-height:1.45;
    transition:border-color .15s ease, box-shadow .15s ease; }}
  .sheet-textarea:focus {{ border-color:var(--mint); box-shadow:0 0 0 3px rgba(51,160,137,0.18); }}
  .sheet-textarea::placeholder {{ color:var(--sub); }}
  /* ── Calendar (date-picker) ───────────────────────────────── */
  .cal-weekdays {{ display:grid; grid-template-columns:repeat(7,1fr); gap:4px; margin-bottom:6px; }}
  .cal-weekdays span {{ text-align:center; font-size:11px; font-weight:700;
    letter-spacing:.06em; color:var(--sub); text-transform:uppercase; }}
  .cal-grid {{ display:grid; grid-template-columns:repeat(7,1fr); gap:4px; }}
  .cal-day, .cal-day-on, .cal-day-disabled {{
    width:38px; height:38px; border-radius:10px; border:none;
    background:transparent; font-family:inherit; font-size:13px; font-weight:600;
    color:var(--text); cursor:pointer; transition:.15s ease;
  }}
  .cal-day:hover {{ background:var(--input-bg); }}
  .cal-day-on {{ background:var(--mint); color:#fff;
    box-shadow:0 4px 12px rgba(51,160,137,0.175); }}
  .cal-day-disabled {{ color:var(--sub); opacity:.4; cursor:not-allowed; }}
  /* ── Slot editor sheet ────────────────────────────────────── */
  .sheet-tall {{ padding-top:8px; }}
  .slot-editor-header {{ text-align:center; padding:0 8px 4px; }}
  .slot-list {{ display:flex; flex-direction:column; gap:10px;
    padding:8px 0 10px; max-height:300px; overflow-y:auto; }}
  .slot-row {{ display:flex; align-items:center; gap:10px;
    padding:12px 14px; border-radius:14px;
    background:var(--input-bg); border:1px solid var(--input-border); }}
  .slot-time-pair {{ flex:1; display:flex; align-items:center; gap:10px; }}
  .slot-time {{ flex:1; padding:10px 12px; border-radius:10px;
    background:var(--card); border:1px solid var(--input-border);
    font-family:inherit; font-size:14px; font-weight:700; color:var(--text);
    text-align:center; cursor:pointer; transition:border-color .15s ease; }}
  .slot-time:active {{ border-color:var(--mint); }}
  .slot-dash {{ font-size:14px; font-weight:600; color:var(--sub); }}
  .slot-x {{ width:36px; height:36px; border-radius:10px; border:none;
    background:rgba(239,68,68,.08); color:#EF4444; cursor:pointer;
    display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
  .slot-add {{ width:100%; display:flex; align-items:center; justify-content:center;
    gap:8px; padding:14px; border-radius:14px;
    background:rgba(51,160,137,0.06); border:1.5px dashed rgba(51,160,137,0.175);
    color:var(--mint); font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; transition:background .15s ease; }}
  .slot-add:hover {{ background:rgba(51,160,137,0.12); }}

  /* ─── Sprint E · Post-creation flow (canonical may30) ───────────────── */
  /* 1) post_create_menu — BottomSheet */
  /* Backdrop : layered silhouette of feed (canonical V2, no external image). */
  .pcm-backdrop {{ position:absolute; inset:0; z-index:1; overflow:hidden;
    background:var(--page); }}
  .pcm-backdrop::before, .pcm-backdrop::after {{
    content:''; position:absolute; border-radius:24px;
    background:var(--input-bg); }}
  .pcm-backdrop::before {{ top:46px; left:14px; width:170px; height:215px;
    box-shadow:6px 6px 0 -2px var(--input-border) inset; }}
  .pcm-backdrop::after {{ top:46px; right:14px; width:170px; height:215px;
    box-shadow:6px 6px 0 -2px var(--input-border) inset;
    background:linear-gradient(135deg, rgba(51,160,137,0.12), rgba(255,255,255,.04)); }}
  /* Icon chip (canonical V2, 42x42) */
  .pcm-ic {{ width:42px; height:42px; border-radius:14px;
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0; }}
  .pcm-sheet {{ position:absolute; left:0; right:0; bottom:0; z-index:5;
    background:var(--card);
    border-radius:32px 32px 0 0;
    padding:14px 20px 28px;
    box-shadow:0 -10px 40px rgba(0,0,0,.32),
               0 -2px 24px rgba(51,160,137,0.12);
    border-top:1px solid rgba(51,160,137,0.2); }}
  .pcm-handle {{ width:42px; height:5px; border-radius:999px;
    background:var(--input-border); margin:0 auto 16px; }}
  .pcm-title {{ font-size:18px; font-weight:800; margin:0 0 18px;
    color:var(--text); text-align:center; letter-spacing:-.01em; }}
  .pcm-rows {{ display:flex; flex-direction:column; gap:6px; }}
  .pcm-row {{ display:flex; align-items:center; gap:14px;
    width:100%; padding:14px 12px; border:none; border-radius:18px;
    background:var(--input-bg); cursor:pointer;
    font-family:inherit; transition:.15s ease;
    border:1px solid var(--input-border); }}
  .pcm-row:hover {{ border-color:rgba(51,160,137,0.175);
    box-shadow:0 0 16px rgba(51,160,137,0.1); }}
  .pcm-row-text {{ flex:1; min-width:0; text-align:left; }}
  .pcm-row-title {{ font-size:15px; font-weight:700; color:var(--text);
    display:inline-flex; align-items:center; gap:6px; }}
  .pcm-row-sub {{ font-size:12px; font-weight:500; color:var(--sub); margin-top:2px; }}
  .pcm-live-dot {{ display:inline-block; width:8px; height:8px;
    border-radius:999px; background:#FF4658;
    box-shadow:0 0 8px rgba(255,70,88,.6); }}

  /* 2) post_gallery */
  .pg-topbar {{ position:absolute; top:0; left:0; right:0; z-index:10;
    height:56px; display:flex; align-items:center; gap:8px;
    padding:0 12px 0 8px; background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%);
    border-bottom:1px solid var(--border); }}
  .pg-topbar h1 {{ flex:1; text-align:center; font-size:16px;
    font-weight:700; margin:0; color:var(--text); letter-spacing:-.01em; }}
  .pg-next {{ padding:7px 14px; border:none; border-radius:999px;
    background:var(--card); color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.225);
    font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer;
    box-shadow:0 0 14px rgba(51,160,137,0.15); }}
  .pg-main {{ padding-top:56px; height:100%; overflow:hidden; }}
  .pg-preview {{ position:relative; width:100%; aspect-ratio:1/1; overflow:hidden;
    background:#000; }}
  .pg-preview img {{ width:100%; height:100%; object-fit:cover; }}
  .pg-preview-overlay {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,0) 60%, rgba(0,0,0,.35) 100%); }}
  .pg-preview-tag {{ position:absolute; top:14px; right:14px;
    padding:6px 12px; border-radius:999px;
    background:rgba(0,0,0,.50); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px); }}
  .pg-preview-logo {{ font-size:13px; font-weight:900; letter-spacing:-.02em;
    background:linear-gradient(90deg, var(--mint) 0%, var(--mint-deep) 100%);
    -webkit-background-clip:text; background-clip:text; color:transparent; }}
  .pg-meta {{ display:flex; justify-content:space-between; align-items:center;
    padding:10px 14px; }}
  .pg-recents {{ display:inline-flex; align-items:center; gap:4px;
    border:none; background:transparent; cursor:pointer;
    font-family:inherit; font-size:13px; font-weight:700; color:var(--text); }}
  .pg-cam-btn {{ width:36px; height:36px; border:1.5px solid rgba(51,160,137,0.225);
    border-radius:999px; background:var(--card); color:var(--mint);
    display:flex; align-items:center; justify-content:center; cursor:pointer;
    box-shadow:0 0 14px rgba(51,160,137,0.15);
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.15)); }}
  .pg-grid {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:2px; padding:0; }}
  .pg-tile {{ position:relative; aspect-ratio:1/1; overflow:hidden; }}
  .pg-tile img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .pg-tile-on {{ outline:2px solid var(--mint); outline-offset:-2px; }}
  .pg-tile-check {{ position:absolute; top:6px; right:6px; width:18px; height:18px;
    border-radius:999px; background:var(--mint);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 8px rgba(51,160,137,0.3); }}
  .pg-source-tabs {{ position:absolute; bottom:0; left:0; right:0; z-index:8;
    display:flex; gap:6px; padding:12px 14px 18px env(safe-area-inset-bottom,18px);
    background:var(--card);
    border-top:1px solid var(--border);
    justify-content:center; }}
  .pg-source-tab {{ padding:8px 18px; border:none; border-radius:999px;
    background:transparent; color:var(--sub);
    font-family:inherit; font-size:13px; font-weight:600; cursor:pointer; }}
  .pg-source-tab-on {{ background:var(--input-bg); color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.225);
    box-shadow:0 0 14px rgba(51,160,137,0.15); }}

  /* 3) post_details */
  .pd-topbar {{ position:absolute; top:0; left:0; right:0; z-index:10;
    height:56px; display:flex; align-items:center; gap:8px;
    padding:0 12px 0 8px; background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%);
    border-bottom:1px solid var(--border); }}
  .pd-topbar h1 {{ flex:1; text-align:center; font-size:16px;
    font-weight:700; margin:0; color:var(--text); letter-spacing:-.01em; }}
  .pd-publish {{ padding:8px 16px; border:none; border-radius:999px;
    background:linear-gradient(135deg, {MINT_HI} 0%, {MINT_DEEP} 100%); color:#fff;
    font-family:inherit; font-size:13px; font-weight:800;
    cursor:pointer;
    box-shadow:0 4px 14px rgba(51,160,137,0.225),
               0 0 0 1px rgba(255,255,255,.08) inset; }}
  .pd-main {{ padding:72px 18px 32px; height:100%; overflow-y:auto; }}
  .pd-caption-row {{ display:flex; gap:14px; align-items:flex-start; }}
  .pd-thumb {{ width:72px; height:72px; flex-shrink:0;
    border-radius:14px; overflow:hidden;
    border:1px solid var(--border);
    box-shadow:0 2px 8px rgba(0,0,0,{t['dim_shadow']}); }}
  .pd-thumb img {{ width:100%; height:100%; object-fit:cover; }}
  .pd-caption {{ flex:1; min-height:72px;
    border:none; background:transparent; outline:none; resize:none;
    color:var(--text); font-family:inherit; font-size:15px;
    line-height:1.4; font-weight:500; }}
  .pd-caption::placeholder {{ color:var(--sub); opacity:.55; }}
  .pd-section-label {{ font-size:10px; font-weight:800; letter-spacing:.14em;
    text-transform:uppercase; color:var(--sub); margin:24px 0 10px; }}
  .pd-tags-wrap {{ display:flex; flex-wrap:wrap; gap:8px; }}
  .pd-tag {{ display:inline-flex; align-items:center; gap:4px;
    padding:7px 12px; border-radius:999px;
    background:var(--input-bg); color:var(--sub);
    border:1px solid var(--input-border);
    font-size:13px; font-weight:600; cursor:pointer; transition:.15s ease; }}
  .pd-tag-on {{ background:rgba(51,160,137,0.14); color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.225);
    box-shadow:0 0 14px rgba(51,160,137,0.25); }}
  .pd-tag-x {{ display:inline-flex; opacity:.7; }}
  .pd-settings {{ margin-top:24px; padding:6px 4px;
    background:var(--card); border-radius:22px;
    border:1px solid rgba(51,160,137,0.15);
    box-shadow:0 0 24px rgba(51,160,137,0.06),
               0 8px 24px rgba(0,0,0,{t['dim_shadow']}); }}
  .pd-row {{ display:flex; align-items:center; gap:14px;
    padding:14px 14px; cursor:pointer; }}
  .pd-row-text {{ flex:1; min-width:0; }}
  .pd-row-title {{ font-size:14px; font-weight:700; color:var(--text); }}
  .pd-row-sub {{ font-size:12px; font-weight:500; color:var(--sub); margin-top:2px; }}
  .pd-row-sep {{ height:1px; background:var(--border); margin:0 18px; }}
  .pd-advanced {{ display:inline-flex; align-items:center; gap:4px;
    margin:18px auto 0;
    padding:9px 16px; border:none; border-radius:999px;
    background:transparent; color:var(--sub); cursor:pointer;
    font-family:inherit; font-size:12px; font-weight:600; }}

  /* 4) post_success */
  .ps-wrap {{ position:absolute; inset:0; padding:0 24px;
    display:flex; flex-direction:column; align-items:center;
    justify-content:center; gap:6px; }}
  .ps-particles {{ position:absolute; inset:0; pointer-events:none;
    background:radial-gradient(circle at 30% 25%, rgba(51,160,137,0.12) 0%, transparent 28%),
               radial-gradient(circle at 75% 70%, rgba(0,179,199,.08) 0%, transparent 30%); }}
  .ps-check {{ position:relative; width:120px; height:120px;
    border-radius:999px; background:rgba(51,160,137,0.1);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 60px rgba(51,160,137,0.2),
               0 0 0 2px rgba(51,160,137,0.15) inset;
    margin-bottom:24px; }}
  .ps-check-ring {{ position:absolute; inset:-12px; border-radius:999px;
    border:2px solid rgba(51,160,137,0.175);
    box-shadow:0 0 24px rgba(51,160,137,0.25);
    animation:ps-pulse 2.4s ease-in-out infinite; }}
  @keyframes ps-pulse {{ 0%,100% {{ transform:scale(1); opacity:.5; }} 50% {{ transform:scale(1.06); opacity:1; }} }}
  .ps-check-icon {{ font-size:64px; color:var(--mint);
    filter:drop-shadow(0 0 10px rgba(51,160,137,0.3)); }}
  .ps-title {{ font-size:24px; font-weight:800; margin:0 0 6px;
    color:var(--text); letter-spacing:-.02em; }}
  .ps-body {{ font-size:14px; font-weight:500; color:var(--sub);
    text-align:center; margin:0 0 28px; max-width:280px; line-height:1.45; }}
  .ps-actions {{ display:flex; flex-direction:column; gap:10px; width:100%; max-width:320px;
    margin-bottom:20px; }}
  .ps-cta-primary {{ padding:14px 20px; border:none; border-radius:999px;
    background:linear-gradient(135deg, {MINT_HI} 0%, {MINT_DEEP} 100%); color:#fff;
    font-family:inherit; font-size:15px; font-weight:800;
    cursor:pointer;
    box-shadow:0 8px 24px rgba(51,160,137,0.225),
               0 0 0 1px rgba(255,255,255,.08) inset; }}
  .ps-cta-ghost {{ padding:14px 20px; border-radius:999px;
    background:transparent; color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.225);
    font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; box-shadow:0 0 14px rgba(51,160,137,0.18); }}
  .ps-status-card {{ display:flex; align-items:center; gap:12px;
    padding:10px 12px; border-radius:18px;
    background:var(--card); border:1px solid rgba(51,160,137,0.18);
    box-shadow:0 0 16px rgba(51,160,137,0.08),
               0 4px 16px rgba(0,0,0,{t['dim_shadow']});
    width:100%; max-width:300px; }}
  .ps-status-card img {{ width:42px; height:42px; border-radius:10px; object-fit:cover; }}
  .ps-status-text {{ flex:1; }}
  .ps-status-label {{ font-size:12px; font-weight:600; color:var(--sub); }}
  .ps-status-live {{ display:flex; align-items:center; gap:6px;
    font-size:11px; font-weight:800; color:var(--mint);
    letter-spacing:.10em; text-transform:uppercase; margin-top:2px; }}
  .ps-live-dot {{ width:7px; height:7px; border-radius:999px; background:var(--mint);
    box-shadow:0 0 8px rgba(51,160,137,0.3); }}

  /* 5) peak_camera */
  .pkc-bg {{ position:absolute; inset:0; z-index:1; }}
  .pkc-bg img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .pkc-bg-overlay {{ position:absolute; inset:0;
    background:linear-gradient(180deg, rgba(0,0,0,.45) 0%, transparent 22%,
                                       transparent 70%, rgba(0,0,0,.65) 100%); }}
  .pkc-topbar {{ position:absolute; top:14px; left:0; right:0; z-index:6;
    display:flex; align-items:center; gap:8px; padding:0 14px;
    justify-content:space-between; }}
  .pkc-close, .pkc-flash {{ width:38px; height:38px; border:none; border-radius:999px;
    background:rgba(0,0,0,.45); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    display:flex; align-items:center; justify-content:center; cursor:pointer; }}
  .pkc-music-pill {{ display:inline-flex; align-items:center;
    padding:9px 16px; border:none; border-radius:999px;
    background:rgba(0,0,0,.55); -webkit-backdrop-filter:blur(10px); backdrop-filter:blur(10px);
    color:#fff; font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; border:1px solid rgba(255,255,255,.12); }}
  .pkc-side {{ position:absolute; right:14px; top:80px; z-index:5;
    display:flex; flex-direction:column; gap:18px; align-items:center; }}
  .pkc-side-item {{ display:flex; flex-direction:column; gap:4px;
    align-items:center; border:none; background:transparent; cursor:pointer;
    font-family:inherit; }}
  .pkc-side-icon {{ width:42px; height:42px; border-radius:999px;
    background:rgba(0,0,0,.50); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    display:flex; align-items:center; justify-content:center;
    border:1px solid rgba(255,255,255,.10); }}
  .pkc-side-label {{ font-size:10px; font-weight:700; color:#fff;
    text-shadow:0 1px 2px rgba(0,0,0,.6); letter-spacing:.04em; }}
  .pkc-speed-strip {{ position:absolute; left:0; right:0; bottom:200px; z-index:5;
    display:flex; gap:14px; justify-content:center; align-items:center;
    overflow-x:auto; padding:0 20px; font-family:inherit;
    color:rgba(255,255,255,.65); font-size:12px; font-weight:600;
    text-shadow:0 1px 2px rgba(0,0,0,.6); }}
  .pkc-speed-on {{ color:#fff; font-weight:800; font-size:15px;
    text-shadow:0 0 8px rgba(255,255,255,.5); }}
  .pkc-duration {{ position:absolute; left:0; right:0; bottom:160px; z-index:5;
    display:flex; gap:6px; justify-content:center; padding:0 20px; }}
  .pkc-duration button {{ padding:6px 14px; border:none; border-radius:999px;
    background:rgba(0,0,0,.45); color:#fff;
    font-family:inherit; font-size:12px; font-weight:700;
    cursor:pointer; border:1px solid rgba(255,255,255,.10); }}
  .pkc-dur-on {{ background:rgba(255,255,255,.85) !important;
    color:#000 !important; }}
  .pkc-record-row {{ position:absolute; left:0; right:0; bottom:36px; z-index:6;
    display:flex; align-items:center; justify-content:space-between; padding:0 28px; }}
  .pkc-library {{ display:flex; flex-direction:column; gap:4px;
    align-items:center; border:none; background:transparent; cursor:pointer;
    font-family:inherit; }}
  .pkc-library img {{ width:46px; height:46px; border-radius:10px;
    object-fit:cover; border:2px solid #fff;
    box-shadow:0 2px 8px rgba(0,0,0,.6); }}
  .pkc-library span {{ font-size:10px; font-weight:700; color:#fff;
    text-shadow:0 1px 2px rgba(0,0,0,.6); }}
  .pkc-record {{ width:82px; height:82px; border:none; border-radius:999px;
    background:transparent; padding:0;
    border:5px solid #fff;
    cursor:pointer;
    box-shadow:0 4px 20px rgba(0,0,0,.5),
               0 0 0 2px rgba(255,255,255,.4) inset; }}
  .pkc-record-inner {{ display:block; width:60px; height:60px; margin:6px auto;
    border-radius:999px; background:#FF4658;
    box-shadow:0 0 20px rgba(255,70,88,.6); }}
  .pkc-filter {{ display:flex; flex-direction:column; gap:4px;
    align-items:center; border:none; background:transparent; cursor:pointer;
    font-family:inherit; padding:8px; }}
  .pkc-filter span {{ font-size:10px; font-weight:700; color:#fff;
    text-shadow:0 1px 2px rgba(0,0,0,.6); }}
  /* pkc-root : explicit 393x852 to defeat Chrome headless body collapse */
  .pkc-root {{ position:relative; width:393px; height:852px; overflow:hidden;
    background:#000; }}

  /* ─── Sprint D · Package edit mode (founder may30) ──────────── */
  .pe-thumb-wrap {{ position:relative; margin:18px 16px 22px;
    aspect-ratio:16/10; border-radius:24px; overflow:hidden;
    box-shadow:0 12px 32px rgba(0,0,0,{t['dim_shadow']}),
               0 0 24px rgba(51,160,137,0.12); }}
  .pe-thumb-wrap img {{ width:100%; height:100%; object-fit:cover; }}
  .pe-thumb-edit {{ position:absolute; top:12px; right:12px;
    display:inline-flex; align-items:center; gap:6px;
    padding:8px 12px; border-radius:999px;
    background:rgba(0,0,0,.55); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px);
    color:#fff; font-size:12px; font-weight:700;
    border:1px solid rgba(255,255,255,.12); cursor:pointer; }}
  .pe-stats-row {{ display:flex; gap:8px; margin:0 16px 18px; }}
  .pe-stat-pill {{ flex:1; padding:10px 14px; border-radius:14px;
    background:var(--card); border:1px solid rgba(51,160,137,0.18);
    box-shadow:0 0 14px rgba(51,160,137,0.08); }}
  .pe-stat-num {{ font-size:18px; font-weight:800; color:var(--mint);
    letter-spacing:-.01em; }}
  .pe-stat-lbl {{ font-size:11px; font-weight:600; color:var(--sub); margin-top:2px; }}
  .pe-danger-btn {{ display:flex; align-items:center; justify-content:center; gap:8px;
    margin:24px 16px 12px; padding:14px 18px; width:calc(100% - 32px);
    border-radius:16px; border:1.5px solid rgba(239,68,68,.40);
    background:rgba(239,68,68,.08); color:#EF4444;
    font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; box-shadow:0 0 14px rgba(239,68,68,.10); }}
  .pe-danger-sub {{ font-size:11px; font-weight:500; color:var(--sub);
    text-align:center; padding:0 28px; margin:0 0 24px; line-height:1.4; }}
</style>
</head>
<body>
<div class="phone-root">
{body if is_bare else f'''{('' if is_view else top)}
<main class="{main_class}{'' if not is_view else ' main-view-no-topbar'}">
{body}
</main>
{('' if is_profile_shell else f"""<div class="cta-wrap{' cta-wrap-view' if is_view else ''}">
  <button class="cta{' cta-ghost' if is_owner_profile else ''}">{cta_label}</button>
  {cta_subtext}
</div>""")}'''}
{popup_leave(t) if not is_view else ''}
{popup_success(title, cta_label, t) if not is_view else ''}
{popup_slot_editor(t) if title == '1:1 setup' else ''}
{popup_add_text('Avantage', 'Ex. Accès à tous les lives', 'add-perk', 'Ajouter un avantage', 'Tes fans verront ce point dans la liste des avantages.') if title == 'Channel setup' else ''}
{popup_channel_price_picker() if title == 'Channel setup' else ''}
{popup_add_text('Service inclus', 'Ex. 2 sessions 1:1 / semaine', 'add-service', 'Ajouter un service au pack', 'Décris en une ligne ce qui est inclus dans le pack.') if title == 'Package setup' else ''}
{popup_add_date(t) if title == '1:1 setup' else ''}
{popup_iap_confirm("Smuppy Inc.", "Abonnement Sara's Channel", "$9.99 / mois", 'iap-confirm', recurring=True) if key == 'creator_channel_view_v2' else ''}
{popup_iap_confirm("Smuppy Inc.", "Session 1:1 · 30 min", "$28", 'iap-confirm', recurring=False) if key == 'creator_1on1_view_v2' else ''}
{popup_iap_confirm("Smuppy Inc.", "Pack Transformation · 3 mois", "$269", 'iap-confirm', recurring=False) if key == 'creator_packages_view_v2' else ''}
{popup_payment_loading() if key in ('creator_channel_view_v2', 'creator_1on1_view_v2', 'creator_packages_view_v2') else ''}
{popup_flow_success('subscribe-success', '🎉', "Bienvenue dans la chaîne", "Tu es maintenant abonné à Sara's Channel. Tu reçois tous les contenus exclusifs.", "Voir la chaîne") if key == 'creator_channel_view_v2' else ''}
{popup_flow_success('booking-success', '✓', "Session réservée", "Jeudi 5 juin à 14h00. Tu recevras le lien Agora 5 min avant.", "Voir ma réservation") if key == 'creator_1on1_view_v2' else ''}
{popup_flow_success('purchase-success', '✓', "Pack acheté", "Pack Transformation · 24 sessions disponibles pendant 3 mois.", "Réserver ma 1ère session") if key == 'creator_packages_view_v2' else ''}
{popup_book_objective() if key == 'creator_1on1_view_v2' else ''}
{popup_date_picker() if key == 'creator_1on1_view_v2' else ''}
</div>
<script>
  // ── Open a sheet via URL hash ────────────────────────────────────
  const validHashes = ['success', 'leave', 'slot-editor', 'add-perk', 'add-service', 'add-date',
    'iap-confirm', 'payment-loading', 'subscribe-success', 'booking-success', 'purchase-success',
    'book-objective', 'date-picker', 'channel-price-picker'];
  function openSheetFromHash() {{
    const hash = location.hash.replace('#','');
    if (validHashes.includes(hash)) {{
      const el = document.getElementById('sheet-' + hash);
      if (el) el.setAttribute('data-state', 'open');
    }}
  }}
  openSheetFromHash();
  window.addEventListener('hashchange', openSheetFromHash);

  // ── Prototype click-through navigation map ───────────────────────
  const SCREEN_KEY = {SCREEN_KEY!r};
  const MODE = {MODE!r};
  const url = (k) => 'creator_' + k + '_v2_' + MODE + '/code.html';
  // Navigation targets per screen
  const NAV_BY_KEY = {{
    'channel_setup':        {{ back: 'channel_owner_profile', save: 'channel_owner_profile' }},
    '1on1_setup':           {{ back: '1on1_owner_profile',    save: '1on1_owner_profile'    }},
    'packages_setup':       {{ back: 'packages_owner_profile',save: 'packages_owner_profile' }},
    'channel_owner_profile':{{ close: 'channel_view',         manage: 'channel_setup'       }},
    '1on1_owner_profile':   {{ close: '1on1_view',            manage: '1on1_setup'          }},
    'packages_owner_profile':{{ close: 'packages_view',       manage: 'packages_setup'      }},
    'channel_view':         {{ close: 'channel_owner_profile' }},
    '1on1_view':            {{ close: '1on1_owner_profile' }},
    'packages_view':        {{ close: 'packages_owner_profile' }},
  }};
  const nav = NAV_BY_KEY[SCREEN_KEY] || {{}};

  // ── Wire interactive elements ────────────────────────────────────
  function go(targetKey) {{ if (targetKey) location.href = url(targetKey); }}
  function closeSheets() {{ document.querySelectorAll('.sheet-scrim').forEach(el => el.setAttribute('data-state','closed')); history.replaceState(null,'',location.pathname); }}
  function openSheet(name) {{ const el = document.getElementById('sheet-' + name); if (el) el.setAttribute('data-state','open'); }}

  // Topbar back arrow (config screens)
  document.querySelectorAll('.topbar:not(.topbar-view) .back').forEach(b => b.addEventListener('click', () => go(nav.back || nav.close)));
  // Topbar × close (view/owner-profile screens)
  document.querySelectorAll('.topbar-view .back:first-of-type').forEach(b => b.addEventListener('click', () => go(nav.close)));
  // "Gérer" / "Nouveau pack" chip (owner profile views)
  document.querySelectorAll('.manage-chip').forEach(b => b.addEventListener('click', (e) => {{ e.preventDefault(); go(nav.manage); }}));
  // Main CTA — config screens save → open success sheet (which links to view)
  document.querySelectorAll('.cta-wrap:not(.cta-wrap-view) .cta').forEach(b => b.addEventListener('click', () => openSheet('success')));
  // Main CTA — visitor/view screens → open success directly (placeholder for IAP — Sprint B)
  document.querySelectorAll('.cta-wrap-view .cta:not(.cta-ghost)').forEach(b => b.addEventListener('click', () => openSheet('success')));
  // Ghost CTA on owner profile = no-op (analytics destination not built yet)
  document.querySelectorAll('.cta-ghost').forEach(b => b.addEventListener('click', (e) => e.preventDefault()));
  // Success sheet primary button → navigate to view/owner_profile
  document.querySelectorAll('#sheet-success .sheet-btn-primary').forEach(b => b.addEventListener('click', () => go(nav.save || nav.close)));
  // Success sheet ghost (Fermer) → close
  document.querySelectorAll('#sheet-success .sheet-btn-ghost').forEach(b => b.addEventListener('click', closeSheets));
  // Confirm-leave : Continuer = close, Quitter quand même = go back
  document.querySelectorAll('#sheet-leave .sheet-btn-ghost').forEach(b => b.addEventListener('click', closeSheets));
  document.querySelectorAll('#sheet-leave .sheet-btn-danger').forEach(b => b.addEventListener('click', () => go(nav.back || nav.close)));
  // Any other popup buttons (slot-editor, add-perk, add-service, add-date) → close
  document.querySelectorAll('#sheet-slot-editor .sheet-btn, #sheet-add-perk .sheet-btn, #sheet-add-service .sheet-btn, #sheet-add-date .sheet-btn').forEach(b => b.addEventListener('click', closeSheets));
  // Click on sheet scrim (outside the sheet box) closes
  document.querySelectorAll('.sheet-scrim').forEach(s => s.addEventListener('click', (e) => {{ if (e.target === s) closeSheets(); }}));
  // Add-perk / add-service / add-date / slot-editor : opening triggers
  document.querySelectorAll('.add-row').forEach(b => {{
    const txt = b.textContent.toLowerCase();
    if (txt.includes('avantage')) b.addEventListener('click', () => openSheet('add-perk'));
    else if (txt.includes('service')) b.addEventListener('click', () => openSheet('add-service'));
    else if (txt.includes('date')) b.addEventListener('click', () => openSheet('add-date'));
  }});
  // Day rows in 1:1 setup → open slot-editor
  document.querySelectorAll('.day-row').forEach(b => b.addEventListener('click', () => openSheet('slot-editor')));
  // Prix mensuel row (Channel setup) → open price-picker
  document.querySelectorAll('.row').forEach(row => {{
    const lbl = row.querySelector('.lbl');
    if (lbl && lbl.textContent.includes('Prix mensuel')) {{
      row.style.cursor = 'pointer';
      row.addEventListener('click', () => openSheet('channel-price-picker'));
    }}
  }});
  // Pack rows in Pack setup (existing) — for now, no-op (Sprint D will add edit destination)
  document.querySelectorAll('.pack-row, .pack-card').forEach(b => b.addEventListener('click', (e) => e.preventDefault()));
</script>
</body></html>
'''


def main() -> None:
    for key in SCREENS:
        for dark in (False, True):
            name = f'{key}_{"dark" if dark else "light"}'
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(build(key, dark), encoding='utf-8')
            print(f'  built: {name}/code.html  ({len(build(key, dark))} bytes)')


if __name__ == '__main__':
    main()
