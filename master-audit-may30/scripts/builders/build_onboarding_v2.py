"""Smuppy V2 — ONBOARDING category canonical maquettes (Sprint P0 #2).
12 screens × 2 themes = 24 HTML maquettes at 393×852 device format.

Uses REAL SmuppyLogo SVG paths + REAL i18n texts from src/i18n/locales/fr/onboarding.json.
Reuses helpers + CSS atoms from build_auth_v2.py via re-import.
"""

import json
import sys
from pathlib import Path

# Re-use AUTH builder helpers (same logo, same atoms, same CSS root)
sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from build_auth_v2 import (
    MINT, MINT_HI, MINT_DEEP, DANGER,
    theme,
    smuppy_icon, smuppy_text, smuppy_full, smuppy_stacked,
    primary_cta, ghost_cta, social_btn,
    input_field, back_button, close_button, onb_header, code_input,
)

OUT_DIR = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
i18n_onb = json.loads(Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/onboarding.json').read_text())

# Real categories config (parsed from src/config/{interests,expertise}.ts)
_CATEGORIES = json.loads(Path('/tmp/smuppy_categories.json').read_text())
INTERESTS = _CATEGORIES['interests']     # 114 items
EXPERTISE = _CATEGORIES['expertise']      # 162 items


def to(*keys):
    d = i18n_onb
    for k in keys:
        d = d.get(k, '?')
    return d


# ─── SCREEN BODIES ──────────────────────────────────────────


def card_select(label: str, desc: str, icon_name: str, icon_hue: str, selected: bool = False, badge: str = None) -> str:
    """Onboarding card with colored icon. Halo glow ONLY on selected state (mint), not on hue icons."""
    sel = ' onb-card-sel' if selected else ''
    bg_op = '14' if selected else '0F'
    badge_html = f'<span class="onb-card-badge">{badge}</span>' if badge else ''
    # Calm icon : just colored bg + colored icon, no hue halo / drop-shadow
    return f'''<button class="onb-card{sel}">
  <span class="onb-card-ic" style="background:{icon_hue}{bg_op};color:{icon_hue}">
    <ion-icon name="{icon_name}" style="font-size:22px;color:{icon_hue}"></ion-icon>
  </span>
  <div class="onb-card-text">
    <div class="onb-card-title">{label}{badge_html}</div>
    <div class="onb-card-desc">{desc}</div>
  </div>
  <ion-icon name="chevron-forward" class="onb-card-chev"></ion-icon>
</button>'''


def category_chip(label: str, icon: str = None, color: str = None, on: bool = False) -> str:
    """Real-style chip with colored icon (per item color from config) — matches CategorySelectionScreen.tsx."""
    cls = 'cat-chip cat-chip-on' if on else 'cat-chip'
    if icon and color:
        ico = f'<ion-icon name="{icon}" style="font-size:16px;color:{color};margin-right:6px;flex-shrink:0"></ion-icon>'
    elif icon:
        ico = f'<ion-icon name="{icon}" style="font-size:16px;color:var(--sub);margin-right:6px"></ion-icon>'
    else:
        ico = ''
    return f'<span class="{cls}">{ico}{label}</span>'


def category_section(cat_label: str, cat_icon: str, cat_color: str, items: list, selected_names: set, selected_count: int = 0) -> str:
    """Real CategorySelectionScreen pattern : section with category header + items grid."""
    count_html = f'<span class="cat-section-count"> ({selected_count})</span>' if selected_count > 0 else ''
    chips = ''.join(category_chip(it['label'], it['icon'], it['color'], on=(it['label'] in selected_names)) for it in items)
    return f'''<div class="cat-section">
  <div class="cat-section-header">
    <span class="cat-section-ic" style="background:{cat_color}15;color:{cat_color};">
      <ion-icon name="{cat_icon}" style="font-size:18px;color:{cat_color}"></ion-icon>
    </span>
    <h3 class="cat-section-title">{cat_label}{count_html}</h3>
  </div>
  <div class="cat-section-items">{chips}</div>
</div>'''


def explore_more_btn(remaining: int) -> str:
    return f'''<button class="cat-explore-more">
  <ion-icon name="add-circle-outline" style="font-size:20px;color:var(--mint);vertical-align:middle;margin-right:6px"></ion-icon>
  <span>Voir plus ({remaining} catégories de plus)</span>
</button>'''


# Parse category structure from src/config (top-level categories + items inside each)
_FULL_CATS = json.loads(Path('/tmp/smuppy-v2-recovery/cat_structure.json').read_text()) if Path('/tmp/smuppy-v2-recovery/cat_structure.json').exists() else None


def screen_account_type(th: dict) -> str:
    return f'''{onb_header(1, 5, back=False)}
<main class="auth-main auth-main-onb">
  <div class="auth-brand-row">{smuppy_full(icon_size=32, text_width=96, dark=th['html']=='dark')}</div>
  <h1 class="auth-title">{to('accountType','title')}</h1>
  <p class="auth-sub">{to('accountType','subtitle')}</p>

  <div class="onb-cards">
    {card_select(to('accountType','personal'), to('accountType','personalDesc'), 'person-outline', '#11C6FF')}
    {card_select(to('accountType','professional'), to('accountType','professionalDesc'), 'briefcase-outline', '#9966FF', selected=True)}
  </div>

  <div class="onb-sub-prompt">
    <ion-icon name="chevron-down" style="font-size:14px;color:var(--mint);vertical-align:middle"></ion-icon>
    <span>{to('accountType','proSubTitle')}</span>
  </div>
  <div class="onb-cards">
    {card_select(to('accountType','creator'), to('accountType','creatorDesc'), 'star-outline', MINT)}
    {card_select(to('accountType','business'), to('accountType','businessDesc'), 'storefront-outline', '#FFA63D')}
  </div>
</main>'''


def screen_tell_us(th: dict) -> str:
    return f'''{onb_header(1, 3, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{to('tellUsAboutYou','title')}</h1>
  <p class="auth-sub">{to('tellUsAboutYou','subtitle')}</p>

  <div class="onb-avatar-pick">
    <div class="onb-avatar-wrap">
      <ion-icon name="camera" style="font-size:34px;color:var(--mint)"></ion-icon>
    </div>
    <p class="onb-avatar-lbl">Ajouter une photo de profil</p>
  </div>

  <div class="auth-form">
    {input_field("Nom", value='Sara Khan', icon='person-outline')}
    {input_field("Date de naissance", value='12 mars 1994', icon='calendar-outline')}
    {input_field("Genre", value='Femme', icon='male-female-outline', trailing='<ion-icon name="chevron-down" style="font-size:16px;color:var(--sub)"></ion-icon>')}
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_interests(th: dict) -> str:
    # Real CategorySelectionScreen pattern : show first 4 categories, "Voir plus" for the rest.
    all_cats = _FULL_CATS['interests']  # 16 categories
    initial = 4
    visible_cats = all_cats[:initial]
    remaining = len(all_cats) - initial
    # Sample selections from 1st category (Sports : Running + Swimming) + 2nd (Fitness : Gym)
    selected_names = {'Running', 'Swimming', 'Gym'}
    sections_html = ''
    for cat in visible_cats:
        cnt = sum(1 for it in cat['items'] if it['label'] in selected_names)
        sections_html += category_section(cat['category'], cat['icon'], cat['color'], cat['items'], selected_names, cnt)
    title_txt = "Tes centres d&rsquo;intérêt"
    sub_txt = "Sélectionne ce qui te branche · au moins 3"
    return f'''{onb_header(2, 3, back=True)}
<main class="auth-main auth-main-onb auth-main-scroll">
  <h1 class="auth-title">{title_txt}</h1>
  <p class="auth-sub">{sub_txt}</p>

  <div class="cat-sections">
    {sections_html}
    {explore_more_btn(remaining)}
  </div>

  <div class="onb-cat-count">
    <span class="onb-cat-count-num">{len(selected_names)}</span> sélectionnés · min. 3
  </div>

  <div class="auth-form auth-form-sticky">
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_profession(th: dict) -> str:
    # Categorized display, 4 visible + show more, real expertise.ts categories
    all_cats = _FULL_CATS['expertise']  # 24 categories
    initial = 4
    visible_cats = all_cats[:initial]
    remaining = len(all_cats) - initial
    selected_names = {'General Fitness', 'Vinyasa Flow'}
    sections_html = ''
    for cat in visible_cats:
        cnt = sum(1 for it in cat['items'] if it['label'] in selected_names)
        sections_html += category_section(cat['category'], cat['icon'], cat['color'], cat['items'], selected_names, cnt)
    return f'''{onb_header(2, 5, back=True)}
<main class="auth-main auth-main-onb auth-main-scroll">
  <h1 class="auth-title">Ton métier</h1>
  <p class="auth-sub">Sélectionne tes domaines d&rsquo;expertise pour aider les gens à te trouver</p>

  <div class="cat-sections">
    {sections_html}
    {explore_more_btn(remaining)}
  </div>

  <div class="onb-cat-count">
    <span class="onb-cat-count-num">{len(selected_names)}</span> sélectionnés
  </div>

  <div class="auth-form auth-form-sticky">
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_expertise(th: dict) -> str:
    # Same pattern, different offset to show different categories than Profession
    all_cats = _FULL_CATS['expertise']
    visible_cats = all_cats[4:8]  # show categories 5-8 (Combat / Mind & Wellness / Sports Coaching / Rehabilitation)
    remaining = len(all_cats) - 8
    selected_names = {'HIIT Classes', 'Meditation', 'Mindfulness'}
    sections_html = ''
    for cat in visible_cats:
        cnt = sum(1 for it in cat['items'] if it['label'] in selected_names)
        sections_html += category_section(cat['category'], cat['icon'], cat['color'], cat['items'], selected_names, cnt)
    return f'''{onb_header(3, 5, back=True)}
<main class="auth-main auth-main-onb auth-main-scroll">
  <h1 class="auth-title">Tes spécialités</h1>
  <p class="auth-sub">Affine en sélectionnant tes spécialisations</p>

  <div class="cat-sections">
    {sections_html}
    {explore_more_btn(remaining)}
  </div>

  <div class="onb-cat-count">
    <span class="onb-cat-count-num">{len(selected_names)}</span> sélectionnés
  </div>

  <div class="auth-form auth-form-sticky">
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_find_friends(th: dict) -> str:
    contacts = [
        ('https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=120&h=120&fit=crop&q=80', 'Emma Chen', '+33 6 12 34 56 78'),
        ('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&q=80', 'Marc Dubois', '+33 7 89 12 34 56'),
        ('https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=80', 'Léa Martin', '+33 6 45 67 89 01'),
        ('https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&q=80', 'Thomas Roy', '+33 7 23 45 67 89'),
        ('https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?w=120&h=120&fit=crop&q=80', 'Sara Khan', '+33 6 78 90 12 34'),
    ]
    rows = ''
    for i, (url, name, phone) in enumerate(contacts):
        invited = i < 2
        btn = ('<button class="onb-friend-btn onb-friend-btn-done"><ion-icon name="checkmark" style="font-size:14px;vertical-align:middle"></ion-icon> Invité</button>'
               if invited else '<button class="onb-friend-btn">Inviter</button>')
        rows += f'''<div class="onb-friend-row">
  <img src="{url}" alt="" class="onb-friend-avatar"/>
  <div class="onb-friend-text">
    <div class="onb-friend-name">{name}</div>
    <div class="onb-friend-phone">{phone}</div>
  </div>
  {btn}
</div>'''
    return f'''{onb_header(3, 3, back=False)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">Trouve tes amis</h1>
  <p class="auth-sub">Invite tes contacts pour démarrer avec ta tribu</p>

  <div class="onb-friends-list">
    {rows}
  </div>

  <div class="auth-form">
    {primary_cta("Continuer")}
    <button class="auth-link-row">Passer cette étape</button>
  </div>
</main>'''


def screen_guidelines(th: dict) -> str:
    """Real guidelines from src/i18n/locales/fr/onboarding.json — full 7 sections + intro + conclusion.
    Long-scroll readable layout per founder may30 ref."""
    g = i18n_onb.get('guidelines', {})

    # Intro paragraph (compiled from intro1 + intro2)
    intro1 = g.get('intro1', {})
    intro2 = g.get('intro2', {})
    intro_para = (
        f"{intro1.get('before','Chez ')}<b style='color:var(--mint)'>Smuppy</b>"
        f"{intro1.get('after1','')}<b>{intro1.get('bold1','')}</b>"
        f"{intro1.get('after2','')}<b>{intro1.get('bold2','')}</b>"
        f"{intro1.get('after3','')}<b>{intro1.get('bold3','')}</b>"
        f"{intro1.get('after4','')}"
    )
    intro2_para = (
        f"{intro2.get('before','')}<b>{intro2.get('bold1','')}</b>{intro2.get('after','')}"
    )

    # Section helpers
    def section_block(num, key, color, ic):
        s = g.get(key, {})
        items_html = ''
        for k in ['item1','item2','item3','item4','item5','item6']:
            if k in s:
                items_html += f'<div class="gl-item">{s[k]}</div>'
        # Variants : allowedTitle/prohibitedTitle + allowed/prohibited lists
        if 'allowedTitle' in s:
            items_html += f'<div class="gl-sub-title">{s["allowedTitle"]}</div>'
            for k in ['allowed1','allowed2','allowed3']:
                if k in s: items_html += f'<div class="gl-item">{s[k]}</div>'
        if 'prohibitedTitle' in s:
            items_html += f'<div class="gl-sub-title gl-sub-title-warn">{s["prohibitedTitle"]}</div>'
            for k in ['prohibited1','prohibited2','prohibited3']:
                if k in s: items_html += f'<div class="gl-item">{s[k]}</div>'
        # Sanctions sub-list
        if 'bullet1' in s:
            for k in ['bullet1','bullet2','bullet3']:
                if k in s: items_html += f'<div class="gl-item gl-item-bullet">{s[k]}</div>'
        if 'contestText' in s:
            items_html += f'<div class="gl-note">{s["contestText"]}</div>'
        if 'proAccountText' in s:
            items_html += f'<div class="gl-note">{s["proAccountText"]}</div>'
        footer = s.get('footer','')
        text = s.get('text','')
        intro = s.get('intro','')
        return f'''<div class="gl-section">
          <div class="gl-section-head">
            <span class="gl-section-num" style="background:{color}22;color:{color};box-shadow:0 0 10px {color}44 inset, 0 0 16px {color}33">
              <ion-icon name="{ic}" style="font-size:16px"></ion-icon>
            </span>
            <h3 class="gl-section-title">{s.get('title','')}</h3>
          </div>
          {f'<p class="gl-intro">{intro}</p>' if intro else ''}
          {items_html}
          {f'<p class="gl-text">{text}</p>' if text else ''}
          {f'<p class="gl-footer-note">{footer}</p>' if footer else ''}
        </div>'''

    sections = (
        section_block(1, 'section1', '#33A089', 'heart')
        + section_block(2, 'section2', '#11C6FF', 'briefcase')
        + section_block(3, 'section3', '#EF4444', 'ban')
        + section_block(4, 'section4', '#FFA63D', 'star')
        + section_block(5, 'section5', '#9966FF', 'shield')
        + section_block(6, 'section6', '#F59E0B', 'lock-closed')
        + section_block(7, 'section7', '#64748B', 'refresh')
    )

    conclusion = g.get('conclusion', {})
    conclusion_html = f'''<div class="gl-conclusion">
      <h3 class="gl-conclusion-title">{conclusion.get('title','CONCLUSION')}</h3>
      <p class="gl-conclusion-text">{conclusion.get('text','')}</p>
      <p class="gl-conclusion-highlight">{conclusion.get('highlight','')}</p>
    </div>'''

    title_txt = g.get('title', 'Règles de la communauté Smuppy')
    subtitle_txt = g.get('subtitle', 'Un espace positif et professionnel')
    accept_btn = g.get('acceptButton', 'Accepter')

    return f'''{onb_header(3, 3, back=True)}
<main class="auth-main auth-main-onb auth-main-scroll gl-main">
  <div class="auth-brand-row" style="margin-bottom:14px">{smuppy_stacked(icon_size=58, text_width=120, dark=th['html']=='dark')}</div>
  <h1 class="auth-title gl-title">{title_txt}</h1>
  <p class="auth-sub">{subtitle_txt}</p>

  <p class="gl-intro-para">{intro_para}</p>
  <p class="gl-intro-para">{intro2_para}</p>

  {sections}
  {conclusion_html}

  <div class="auth-form auth-form-sticky">
    {primary_cta(accept_btn + " et créer mon profil")}
  </div>
</main>'''


def screen_business_category(th: dict) -> str:
    cats = [
        ('Salle de sport', 'barbell-outline', True),
        ('Studio Yoga', 'flower-outline', False),
        ('Crossfit Box', 'flash-outline', False),
        ('Cours de boxe', 'fitness-outline', False),
        ('Pilates studio', 'body-outline', False),
        ('Club running', 'walk-outline', False),
        ('Wellness center', 'leaf-outline', False),
        ('Boutique sport', 'bag-outline', False),
    ]
    chips = ''.join(category_chip(label, icon, on) for label, icon, on in cats)
    return f'''{onb_header(2, 3, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{to('businessCategory','title')}</h1>
  <p class="auth-sub">{to('businessCategory','subtitle')}</p>

  <div class="onb-cat-wrap">
    {chips}
  </div>

  <div class="onb-locations">
    <div class="onb-loc-label">{to('businessCategory','locationsTitle')}</div>
    <div class="onb-loc-row">
      {card_select(to('businessCategory','singleLocation'), to('businessCategory','singleLocationDesc'), 'location-outline', MINT, selected=True)}
      {card_select(to('businessCategory','multipleLocations'), to('businessCategory','multipleLocationsDesc'), 'business-outline', '#11C6FF')}
    </div>
  </div>

  <div class="auth-form">
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_business_info(th: dict) -> str:
    return f'''{onb_header(3, 3, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{to('businessInfo','title')}</h1>
  <p class="auth-sub">{to('businessInfo','subtitle')}</p>

  <div class="onb-avatar-pick">
    <div class="onb-avatar-wrap onb-avatar-wrap-square">
      <ion-icon name="image" style="font-size:34px;color:var(--mint)"></ion-icon>
    </div>
    <p class="onb-avatar-lbl">Ajouter ton logo</p>
  </div>

  <div class="auth-form">
    {input_field(to('businessInfo','businessNameLabel'), value='Vibe Fitness Studio', icon='storefront-outline')}
    {input_field(to('businessInfo','addressLabel'), value='12 rue de Rivoli, Paris 75001', icon='location-outline')}
    <div class="onb-info-note">
      <ion-icon name="information-circle" style="font-size:14px;color:var(--sub);vertical-align:middle;margin-right:4px"></ion-icon>
      {to('businessInfo','infoNote')}
    </div>
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_creator_info(th: dict) -> str:
    # Enriched per founder may30 ref : avatar + display name + date of birth + gender + city.
    # Matches OnboardingProfileForm (used for personal too) — adapted to canonical V2.
    return f'''{onb_header(2, 5, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{to('creatorInfo','title')}</h1>
  <p class="auth-sub">{to('creatorInfo','subtitle')}</p>

  <div class="onb-avatar-pick">
    <div class="onb-avatar-wrap">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80" alt="" class="onb-avatar-img"/>
      <span class="onb-avatar-edit"><ion-icon name="camera" style="font-size:16px;color:#fff"></ion-icon></span>
    </div>
    <p class="onb-avatar-lbl">Change ta photo</p>
  </div>

  <div class="auth-form">
    {input_field(to('creatorInfo','nameLabel'), value='Sara Khan', icon='star-outline')}
    {input_field("Date de naissance", value='12 mars 1994', icon='calendar-outline')}
    {input_field("Genre", value='Femme', icon='male-female-outline', trailing='<ion-icon name="chevron-down" style="font-size:16px;color:var(--sub)"></ion-icon>')}
    {input_field("Ville", value='Montréal, Canada', icon='location-outline')}
    {primary_cta("Continuer")}
  </div>
</main>'''


def screen_creator_optional(th: dict) -> str:
    return f'''{onb_header(4, 5, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{to('creatorOptional','title')}</h1>
  <p class="auth-sub">{to('creatorOptional','subtitle')}</p>

  <div class="auth-form">
    {input_field(to('creatorOptional','bioLabel'), value='Coach yoga · Montréal · Daily flows 🧘‍♀️', icon='document-text-outline')}
    {input_field(to('creatorOptional','websiteLabel'), placeholder='https://...', icon='globe-outline')}

    <div class="onb-social-lbl">{to('creatorOptional','socialLinksTitle')}</div>
    <div class="onb-social-grid">
      <div class="onb-social-row">
        <span class="onb-social-ic" style="background:#E4405F1A;color:#E4405F"><ion-icon name="logo-instagram" style="font-size:18px"></ion-icon></span>
        <span class="onb-social-val">@sara.yoga</span>
      </div>
      <div class="onb-social-row">
        <span class="onb-social-ic" style="background:#0000001A;color:var(--text)"><ion-icon name="logo-tiktok" style="font-size:18px"></ion-icon></span>
        <span class="onb-social-val">@sarayoga</span>
      </div>
      <div class="onb-social-row">
        <span class="onb-social-ic" style="background:#FF00001A;color:#FF0000"><ion-icon name="logo-youtube" style="font-size:18px"></ion-icon></span>
        <span class="onb-social-val onb-social-val-empty">Ajouter ton chaîne YouTube</span>
      </div>
    </div>

    {primary_cta("Continuer")}
    <button class="auth-link-row">{to('creatorOptional','skipForNow')}</button>
  </div>
</main>'''


def screen_success(th: dict) -> str:
    title_txt = to('success','title')
    if title_txt == '?': title_txt = 'Bienvenue, Sara !'
    sub_txt = to('success','subtitle')
    if sub_txt == '?': sub_txt = 'Ton profil est prêt. Découvre la tribu maintenant.'
    return f'''<div class="success-wrap">
  <div class="success-confetti"></div>
  <div class="success-confetti-particles"></div>
  <div class="auth-brand-row" style="margin-bottom:26px">{smuppy_stacked(icon_size=90, text_width=180, dark=th['html']=='dark')}</div>
  <h1 class="success-title">{title_txt}</h1>
  <p class="success-body">{sub_txt}</p>
  <div class="success-redirect" style="margin-top:26px;display:flex;align-items:center;gap:6px;color:var(--sub);font-size:13px;font-weight:600">
    <span style="width:7px;height:7px;border-radius:999px;background:var(--mint);display:inline-block;opacity:.5"></span>
    <span style="width:7px;height:7px;border-radius:999px;background:var(--mint);display:inline-block;opacity:.8"></span>
    <span style="width:7px;height:7px;border-radius:999px;background:var(--mint);display:inline-block"></span>
    <span style="margin-left:6px">Redirection vers ta tribu…</span>
  </div>
</div>'''


SCREENS = {
    'onb_account_type_v2': ('Account Type', screen_account_type),
    'onb_tell_us_v2': ('Tell Us About You', screen_tell_us),
    'onb_interests_v2': ('Interests', screen_interests),
    'onb_profession_v2': ('Profession', screen_profession),
    'onb_expertise_v2': ('Expertise', screen_expertise),
    'onb_find_friends_v2': ('Find Friends', screen_find_friends),
    'onb_guidelines_v2': ('Guidelines', screen_guidelines),
    'onb_business_category_v2': ('Business Category', screen_business_category),
    'onb_business_info_v2': ('Business Info', screen_business_info),
    'onb_creator_info_v2': ('Creator Info', screen_creator_info),
    'onb_creator_optional_v2': ('Creator Optional', screen_creator_optional),
    'onb_success_v2': ('Success', screen_success),
}


from build_auth_v2 import build as auth_build_fn


def build(key: str, dark: bool) -> str:
    th = theme(dark)
    title, fn = SCREENS[key]
    body = fn(th)
    # Borrow auth_v2 head/styles (palette, atoms, scaffolding) — append onboarding CSS + body
    auth_full = auth_build_fn('auth_welcome_v2', dark)
    # Replace AUTH body with onboarding body
    head_end = auth_full.index('</style>') + len('</style>')
    head = auth_full[:head_end]
    head = head.replace('Smuppy V2 — Welcome', f'Smuppy V2 — {title}')
    return head + _ONBOARDING_CSS + '\n</head><body>\n' + body + '\n</body></html>'

_ONBOARDING_CSS = """
<style>
  /* ── ONBOARDING atoms ─────────────────────────────────────── */
  .onb-cards { display:flex; flex-direction:column; gap:10px; margin:0 0 14px; }
  .onb-card { display:flex; align-items:center; gap:14px;
    width:100%; padding:14px 14px; border-radius:18px;
    background:var(--card); border:1.5px solid var(--input-border);
    cursor:pointer; font-family:inherit; transition:.18s ease; text-align:left; }
  .onb-card-sel { border-color:rgba(51,160,137,0.225);
    box-shadow:0 0 18px rgba(51,160,137,0.2),
               0 0 0 1px rgba(51,160,137,0.15) inset; }
  .onb-card-ic { width:42px; height:42px; border-radius:14px;
    display:inline-flex; align-items:center; justify-content:center; flex-shrink:0; }
  .onb-card-text { flex:1; min-width:0; }
  .onb-card-title { font-size:15px; font-weight:700; color:var(--text);
    display:inline-flex; align-items:center; gap:6px; }
  .onb-card-desc { font-size:12px; font-weight:500; color:var(--sub); margin-top:3px; line-height:1.35; }
  .onb-card-chev { font-size:18px; color:var(--sub); opacity:.55; }
  .onb-card-badge { display:inline-block; padding:2px 8px; border-radius:999px;
    background:rgba(51,160,137,0.18); color:var(--mint);
    font-size:9.5px; font-weight:800; letter-spacing:.06em; }

  .onb-sub-prompt {
    display:flex; align-items:center; gap:5px;
    font-size:11px; font-weight:700; color:var(--mint);
    text-transform:uppercase; letter-spacing:.10em;
    margin:6px 0 8px; padding-left:4px;
  }

  /* Category chips multi-select */
  .onb-cat-wrap { display:flex; flex-wrap:wrap; gap:8px; margin:0 0 18px; }
  .cat-chip {
    display:inline-flex; align-items:center;
    padding:8px 14px; border-radius:999px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    color:var(--sub); font-family:inherit; font-size:13px; font-weight:600;
    cursor:pointer; transition:.15s ease;
  }
  .cat-chip-on {
    background:rgba(51,160,137,0.12); border-color:rgba(51,160,137,0.225);
    color:var(--mint); font-weight:700;
    box-shadow:0 0 14px rgba(51,160,137,0.2);
  }
  .onb-cat-count {
    text-align:center; font-size:12px; font-weight:600; color:var(--sub);
    margin:0 0 14px;
  }
  .onb-cat-count-num { color:var(--mint); font-weight:800; font-size:14px; }

  /* Avatar picker */
  .onb-avatar-pick { display:flex; flex-direction:column; align-items:center; gap:10px;
    margin:6px 0 22px; }
  .onb-avatar-wrap {
    position:relative;
    width:96px; height:96px; border-radius:999px;
    background:rgba(51,160,137,0.1);
    border:2px dashed rgba(51,160,137,0.2);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 24px rgba(51,160,137,0.25);
    overflow:hidden;
  }
  .onb-avatar-img { width:100%; height:100%; object-fit:cover; border-radius:999px; }
  .onb-avatar-edit {
    position:absolute; bottom:0; right:0;
    width:32px; height:32px; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi) 0%, var(--mint-deep) 100%);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 4px 12px rgba(51,160,137,0.225),
               0 0 0 3px var(--page);
  }
  .onb-avatar-wrap-square { border-radius:22px; }
  .onb-avatar-lbl { font-size:12px; font-weight:700; color:var(--mint);
    letter-spacing:.02em; }

  /* Category sections (real CategorySelectionScreen.tsx pattern) ──── */
  .cat-sections { display:flex; flex-direction:column; gap:18px; margin:0 0 18px; }
  .cat-section { display:flex; flex-direction:column; gap:10px; }
  .cat-section-header { display:flex; align-items:center; gap:10px; padding:0 4px; }
  .cat-section-ic { width:32px; height:32px; border-radius:11px;
    display:inline-flex; align-items:center; justify-content:center; flex-shrink:0; }
  .cat-section-title { font-size:14px; font-weight:800; color:var(--text);
    letter-spacing:-.01em; margin:0; }
  .cat-section-count { color:var(--mint); font-weight:700; font-size:12.5px;
    text-shadow:0 0 8px rgba(51,160,137,0.15); }
  .cat-section-items { display:flex; flex-wrap:wrap; gap:6px; }

  /* "Voir plus" button */
  .cat-explore-more {
    display:flex; align-items:center; justify-content:center;
    width:100%; padding:11px 16px; border:1.5px dashed rgba(51,160,137,0.2);
    border-radius:14px; background:rgba(51,160,137,0.06);
    color:var(--mint); font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; margin-top:6px;
    box-shadow:0 0 14px rgba(51,160,137,0.1);
  }
  .cat-explore-more:hover { border-style:solid; }

  /* Long-scroll main */
  .auth-main-scroll {
    padding-bottom:120px;
  }

  /* Guidelines main override — slightly tighter */
  .gl-main { padding-top:60px; }
  .gl-title { font-size:21px; line-height:1.25; }
  .gl-intro-para {
    font-size:12.5px; line-height:1.55; color:var(--sub);
    margin:0 4px 12px; text-align:left;
  }
  .gl-intro-para b { color:var(--text); font-weight:700; }
  .gl-section {
    background:var(--card); border:1px solid var(--input-border);
    border-radius:16px; padding:14px 14px;
    margin:0 0 14px;
    box-shadow:0 0 14px rgba(51,160,137,0.04);
  }
  .gl-section-head { display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; }
  .gl-section-num {
    flex-shrink:0; width:28px; height:28px; border-radius:9px;
    display:inline-flex; align-items:center; justify-content:center;
    margin-top:1px;
  }
  .gl-section-title { font-size:13.5px; font-weight:800; color:var(--text);
    letter-spacing:-.005em; line-height:1.35; margin:0; }
  .gl-intro {
    font-size:12px; line-height:1.5; color:var(--sub); margin:0 0 8px;
  }
  .gl-sub-title {
    font-size:11.5px; font-weight:800; color:var(--mint);
    letter-spacing:.02em; margin:6px 0 6px;
  }
  .gl-sub-title-warn { color:#EF4444; }
  .gl-item {
    font-size:11.5px; line-height:1.45; color:var(--text);
    padding:6px 10px; border-radius:8px;
    background:var(--input-bg); border:1px solid var(--input-border);
    margin-bottom:5px;
  }
  .gl-item-bullet { background:transparent; border-color:transparent;
    padding:2px 4px; color:var(--sub); font-size:12px; }
  .gl-text { font-size:12px; line-height:1.5; color:var(--text);
    margin:6px 0 0; }
  .gl-note {
    font-size:11.5px; line-height:1.4; color:var(--sub);
    padding:10px 12px; border-radius:10px;
    background:rgba(245,158,11,.06);
    border:1px solid rgba(245,158,11,.22);
    margin:8px 0 4px;
  }
  .gl-footer-note {
    font-size:11.5px; line-height:1.45; color:var(--mint);
    background:rgba(51,160,137,0.06);
    border-left:3px solid var(--mint);
    padding:8px 12px; border-radius:0 8px 8px 0;
    margin:8px 0 0;
  }
  .gl-conclusion {
    background:linear-gradient(135deg, rgba(51,160,137,0.1), rgba(0,179,199,.05));
    border:1.5px solid rgba(51,160,137,0.15);
    border-radius:18px; padding:16px 16px;
    margin:14px 0;
    box-shadow:0 0 24px rgba(51,160,137,0.15);
  }
  .gl-conclusion-title {
    font-size:11px; font-weight:900; color:var(--mint);
    letter-spacing:.18em; margin:0 0 10px;
  }
  .gl-conclusion-text {
    font-size:12.5px; line-height:1.55; color:var(--text); margin:0 0 10px;
  }
  .gl-conclusion-highlight {
    font-size:12.5px; line-height:1.5; color:var(--mint);
    font-weight:700; margin:0;
  }

  /* Chip refinement (colored icon inline, no chip-ic box) — founder may30 */
  .cat-chip { padding:7px 14px; gap:0; }
  .cat-chip ion-icon { flex-shrink:0; }

  /* Find friends list */
  .onb-friends-list { display:flex; flex-direction:column; gap:8px; margin:0 0 18px; }
  .onb-friend-row {
    display:flex; align-items:center; gap:12px;
    padding:12px 14px; border-radius:14px;
    background:var(--card); border:1px solid var(--input-border);
  }
  .onb-friend-avatar { width:44px; height:44px; border-radius:999px; object-fit:cover; flex-shrink:0; }
  .onb-friend-text { flex:1; min-width:0; }
  .onb-friend-name { font-size:14px; font-weight:700; color:var(--text); }
  .onb-friend-phone { font-size:11.5px; font-weight:500; color:var(--sub); margin-top:2px; }
  .onb-friend-btn {
    padding:7px 14px; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi) 0%, var(--mint-deep) 100%);
    color:#fff; border:none; cursor:pointer;
    font-family:inherit; font-size:12px; font-weight:700;
    box-shadow:0 4px 12px rgba(51,160,137,0.175);
  }
  .onb-friend-btn-done {
    background:rgba(51,160,137,0.12); color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.225);
    box-shadow:0 0 14px rgba(51,160,137,0.18);
  }

  /* Guidelines list */
  .onb-guidelines {
    background:var(--card); border:1px solid rgba(51,160,137,0.18);
    border-radius:20px; padding:14px 16px; margin:0 0 18px;
    box-shadow:0 0 20px rgba(51,160,137,0.08);
    display:flex; flex-direction:column; gap:14px;
  }
  .onb-guide-item { display:flex; align-items:flex-start; gap:12px; }
  .onb-guide-ic {
    width:36px; height:36px; border-radius:11px;
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0;
  }
  .onb-guide-title { font-size:14px; font-weight:700; color:var(--text); margin-bottom:2px; }
  .onb-guide-sub { font-size:12px; font-weight:500; color:var(--sub); line-height:1.35; }

  /* Business locations */
  .onb-locations { margin:6px 0 14px; }
  .onb-loc-label { font-size:11px; font-weight:800; color:var(--sub);
    margin:0 0 8px 4px; text-transform:uppercase; letter-spacing:.10em; }
  .onb-loc-row { display:flex; flex-direction:column; gap:8px; }

  /* Info note */
  .onb-info-note { font-size:11.5px; font-weight:500; color:var(--sub);
    background:var(--input-bg); border:1px dashed var(--input-border);
    border-radius:12px; padding:10px 12px; margin:4px 0 14px; line-height:1.4; }

  /* Social grid */
  .onb-social-lbl { font-size:11px; font-weight:800; color:var(--sub);
    margin:14px 0 8px 4px; text-transform:uppercase; letter-spacing:.10em; }
  .onb-social-grid { display:flex; flex-direction:column; gap:8px; margin-bottom:10px; }
  .onb-social-row { display:flex; align-items:center; gap:12px;
    padding:11px 14px; border-radius:14px;
    background:var(--card); border:1px solid var(--input-border); }
  .onb-social-ic { width:32px; height:32px; border-radius:10px;
    display:inline-flex; align-items:center; justify-content:center;
    flex-shrink:0; }
  .onb-social-val { font-size:13.5px; font-weight:600; color:var(--text); }
  .onb-social-val-empty { color:var(--sub); font-weight:500; }

  /* Success confetti particles */
  .success-confetti-particles {
    position:absolute; inset:0; pointer-events:none;
    background:
      radial-gradient(circle 4px at 20% 30%, var(--mint), transparent 70%),
      radial-gradient(circle 3px at 80% 35%, #11C6FF, transparent 70%),
      radial-gradient(circle 5px at 35% 65%, var(--mint-deep), transparent 70%),
      radial-gradient(circle 3px at 65% 70%, #FFA63D, transparent 70%),
      radial-gradient(circle 4px at 75% 25%, #9966FF, transparent 70%);
    opacity:.45;
  }

  /* Sticky form on long lists */
  .auth-form-sticky {
    position:sticky; bottom:0;
    background:linear-gradient(180deg, transparent 0%, var(--page) 30%, var(--page) 100%);
    padding:14px 0 4px;
    margin:0 -24px;
    padding-left:24px; padding-right:24px;
  }
</style>
"""


def write_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for key in SCREENS.keys():
        for dark in (True, False):
            theme_str = 'dark' if dark else 'light'
            screen_dir = OUT_DIR / f'{key}_{theme_str}'
            screen_dir.mkdir(parents=True, exist_ok=True)
            html = build(key, dark)
            (screen_dir / 'code.html').write_text(html)
            n += 1
    print(f'  built {n} ONBOARDING HTML maquettes')


if __name__ == '__main__':
    write_all()
