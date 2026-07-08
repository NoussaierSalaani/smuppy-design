#!/usr/bin/env python3
"""Smuppy V2 — Profile shell v5 (Instagram-style avatar-LEFT header).
Founder ref jun03 09:22 : cover + avatar gauche + name/bio left + stats inline +
Follow/msg (visitor) ou Modifier/share (owner) top-right. Tabs par type de compte :
  - personal : Posts · Peaks · Activities · Saved(owner-only)        [1 niveau]
  - creator  : [Lifestyle→Posts·Peaks·Activities] [Channel→Channel·1:1·Packages]  [2 niveaux]
  - business : [Lifestyle→Posts·Activities] [Services→Booking·Programme]          [2 niveaux]
Owner ≠ Visitor. Bottom nav = canonical_bnav (profile active). 393×852 device.
Self-contained — imports canonical_bnav only. Pure stdlib, deterministic.
"""
import sys
from pathlib import Path

sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from canonical_bnav import canonical_bnav, CANONICAL_BNAV_CSS, canonical_msg_icon  # noqa: E402

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
MINT = '#33A089'
GRAD_A, GRAD_B = '#41AD96', '#2C95A0'

COVER = "https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=900&h=400&fit=crop&q=80"
AVATAR = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop&q=80"
TILES = [
    "1545205597-3d9d02c29597", "1571019614242-c5c5dee9f50b", "1517363898874-737b62a7db91",
    "1559757148-5c350d0d3c56", "1494390248081-4e521a5940db", "1599901860904-17e6ed7083a0",
    "1518611012118-696072aa579a", "1506126613408-eca07ce68773", "1540206395-68808572332f",
]


def theme(dark: bool) -> dict:
    if dark:
        return dict(page='#000000', card='#14141A', text='#F1F4F6', sub='#8B8B95',
                    border='rgba(255,255,255,0.06)', input_bg='rgba(255,255,255,0.04)',
                    input_border='rgba(255,255,255,0.10)', dim='0.5', html='dark')
    return dict(page='#F6F8FA', card='#FFFFFF', text='#0F172A', sub='#64748B',
                border='#EEF1F4', input_bg='#FFFFFF', input_border='#E5E9EB',
                dim='0.06', html='light')


def grid(n: int = 9) -> str:
    cells = ''.join(
        f'<div class="pv-tile"><img loading="lazy" '
        f'src="https://images.unsplash.com/photo-{TILES[i % len(TILES)]}?w=400&h=400&fit=crop&q=80" alt=""/></div>'
        for i in range(n))
    return f'<section class="pv-grid">{cells}</section>'


def configure_btn() -> str:
    return ('<button class="pv-config"><ion-icon name="settings-outline" '
            'style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Configurer</button>')


def _pill(label, ic, on, cls):
    oncls = f' {cls}-on' if on else ''
    return (f'<button class="{cls}{oncls}">'
            f'<ion-icon name="{ic}" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>'
            f'{label}</button>')


def locked_gate() -> str:
    """Private-account gate replacing the content grid."""
    return ('<section style="padding:40px 28px 100px;text-align:center">'
            '<div style="width:64px;height:64px;border-radius:999px;margin:0 auto 16px;'
            'background:var(--input-bg);border:1px solid var(--input-border);'
            'display:flex;align-items:center;justify-content:center">'
            '<ion-icon name="lock-closed" style="font-size:28px;color:var(--mint)"></ion-icon></div>'
            '<h3 style="font-size:16px;font-weight:800;color:var(--text);margin-bottom:6px">Compte privé</h3>'
            '<p style="font-size:13px;color:var(--sub);font-weight:500;line-height:1.5;max-width:260px;margin:0 auto">'
            'Deviens fan pour voir ses posts, peaks et activités.</p></section>')


def _offer_card(icon, color, title, sub, cta, owner_cta=False) -> str:
    btn = (f'<button class="pv-config" style="width:100%;margin:0">{cta}</button>' if owner_cta
           else f'<button class="pv-buy">{cta}</button>')
    return (f'<div class="pv-offer"><div class="pv-offer-ic" style="background:{color}1A;color:{color}">'
            f'<ion-icon name="{icon}" style="font-size:22px"></ion-icon></div>'
            f'<div class="pv-offer-t"><h4>{title}</h4><p>{sub}</p></div>{btn}</div>')


def _th(dark):
    return 'dark' if dark else 'light'


def _perk(icon, color, h4, p):
    return (f'<div class="pv-perk"><span class="pv-perk-ic" style="background:{color}1A;color:{color}">'
            f'<ion-icon name="{icon}" style="font-size:18px"></ion-icon></span>'
            f'<div><h5>{h4}</h5><p>{p}</p></div></div>')


def _media_card(img_id, ratio, badge, badge_c, title, sub, body_html, cta, link, owner) -> str:
    """Rich offer card : hero IMAGE + badge + title + sub + body (perks/price) + CTA (link or Configurer)."""
    badge_html = (f'<span class="pv-mc-badge" style="background:{badge_c}">{badge}</span>' if badge else '')
    btn = (f'<button class="pv-config" style="width:100%;margin:14px 0 0">{cta}</button>' if owner
           else f'<a class="pv-mc-cta" href="{link}">{cta}</a>')
    return (f'<div class="pv-mc"><div class="pv-mc-hero" style="aspect-ratio:{ratio}">'
            f'<img loading="lazy" src="https://images.unsplash.com/photo-{img_id}?w=720&h=420&fit=crop&q=80" alt=""/>'
            f'{badge_html}</div><div class="pv-mc-body"><h4>{title}</h4><p class="pv-mc-sub">{sub}</p>'
            f'{body_html}{btn}</div></div>')


def channel_content(is_owner: bool, dark: bool = True) -> str:
    """Tab Channel — combine le DS au validé creator_channel_view (cover + perks + abo)."""
    th = _th(dark)
    perks = (_perk('videocam', '#33A089', 'Lives exclusifs', 'Accès à tous les lives + replays')
             + _perk('lock-closed', '#9966FF', 'Posts privés', 'Contenu réservé aux abonnés')
             + _perk('pricetag', '#F59E0B', '−20% sur les 1:1', 'Réduction sur sessions privées'))
    if is_owner:
        stats = ('<div class="pv-mon-stats">'
                 '<div class="pv-mon-stat"><b>48</b><span>Abonnés</span></div>'
                 '<div class="pv-mon-stat"><b>$412</b><span>Ce mois</span></div>'
                 '<div class="pv-mon-stat"><b>+12%</b><span>vs M-1</span></div></div>')
        card = _media_card('1518611012118-696072aa579a', '16/9', 'TA CHAÎNE · LIVE', 'rgba(0,0,0,.55)',
                           "Sara's Channel", '$9.99/mois · publié il y a 12 jours',
                           f'<div class="pv-perks">{perks}</div>', 'Configurer',
                           f'../creator_channel_owner_profile_v2_{th}/code.html', True)
        return f'<section class="pv-mon">{stats}{card}</section>'
    card = _media_card('1518611012118-696072aa579a', '16/9', 'PREMIUM', 'linear-gradient(135deg,#33A089,#2C95A0)',
                       "Sara's Channel · $9.99/mois", 'Yoga flows · plans repas · Q&A live mensuel',
                       f'<div class="pv-perks">{perks}</div>', "S'abonner · $9.99/mois",
                       f'../creator_channel_view_v2_{th}/code.html', False)
    return f'<section class="pv-mon">{card}</section>'


def services_content(is_owner: bool, dark: bool = True) -> str:
    """Tab Services business — combine DS au validé p2_business_booking (services image + réserver)."""
    th = _th(dark)
    if is_owner:
        stats = ('<div class="pv-mon-stats">'
                 '<div class="pv-mon-stat"><b>32</b><span>Résa · mois</span></div>'
                 '<div class="pv-mon-stat"><b>$1,240</b><span>Revenus 30j</span></div>'
                 '<div class="pv-mon-stat"><b>4.8★</b><span>Note</span></div></div>')
        cards = (_media_card('1534438327276-14e5300c3a48', '16/9', '8 SERVICES', 'rgba(0,0,0,.55)',
                             'CrossFit Box · $25', 'Coach Mike · 60 min · groupe',
                             '', 'Configurer', f'../p2_business_booking_v2_{th}/code.html', True))
        return f'<section class="pv-mon">{stats}{cards}</section>'
    cards = (_media_card('1534438327276-14e5300c3a48', '16/9', None, '',
                         'CrossFit Box · $25', 'Coach Mike · 60 min · niveau intermédiaire',
                         '', 'Réserver', f'../p2_business_booking_v2_{th}/code.html', False)
             + _media_card('1545205597-3d9d02c29597', '16/9', None, '',
                           'Yoga flow · $18', 'Coach Sara · 45 min · tous niveaux',
                           '', 'Réserver', f'../p2_business_booking_v2_{th}/code.html', False))
    return f'<section class="pv-mon">{cards}</section>'


def peaks_grid() -> str:
    cells = ''.join(
        f'<div class="pv-ptile">'
        f'<img loading="lazy" src="https://images.unsplash.com/photo-{TILES[i % len(TILES)]}?w=400&h=560&fit=crop&q=80" alt=""/>'
        f'<span class="pv-ptile-play"><ion-icon name="play" style="font-size:12px;color:#fff"></ion-icon>{v}</span></div>'
        for i, v in enumerate(['12k', '8.4k', '3.1k', '21k', '5.7k', '1.9k']))
    return f'<section class="pv-pgrid">{cells}</section>'


def activities_list() -> str:
    acts = [('walk', '#33A089', 'Morning Run', '8.2 km · 42:18 · 5:09/km', 'Aujourd\'hui · 7h12'),
            ('bicycle', '#11C6FF', 'Sortie vélo', '32 km · 1:08:42 · 27.9 km/h', 'Hier · 18h30'),
            ('barbell', '#FFA63D', 'Strength', '45 min · 320 kcal', 'Lun · 6h45')]
    rows = ''.join(
        f'<div class="pv-act"><div class="pv-act-ic" style="background:{c}1A;color:{c}">'
        f'<ion-icon name="{ic}" style="font-size:20px"></ion-icon></div>'
        f'<div class="pv-act-t"><h4>{ti}</h4><p>{st}</p><span>{wh}</span></div></div>'
        for ic, c, ti, st, wh in acts)
    return f'<section class="pv-acts">{rows}</section>'


def saved_grid() -> str:
    return grid(9).replace('pv-grid', 'pv-grid')


def tabs_block(account: str, is_owner: bool, dark: bool = True) -> str:
    """Interactive tabs : renders ALL panes (hidden except active) + JS swaps them.
    Founder jun03 : 'cree meme les ecran des peaks/activities/booking etc' + combine
    le DS aux écrans validés (image+desc, flow booking) — pas de placeholder texte."""
    def subnav(main_key, subs, active_main):
        pills = ''.join(
            f'<button class="pv-sub{" pv-sub-on" if i == 0 else ""}" data-sub="{main_key}.{sk}">'
            f'<ion-icon name="{ic}" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>{lbl}</button>'
            for i, (lbl, ic, sk) in enumerate(subs))
        disp = '' if main_key == active_main else 'display:none'
        return (f'<nav class="pv-subs" data-subnav="{main_key}" '
                f'style="grid-template-columns:repeat({len(subs)},1fr);{disp}">{pills}</nav>')

    def pane(key, html, active):
        hid = '' if active else 'hidden'
        return f'<div class="pv-pane" data-pane="{key}" {hid}>{html}</div>'

    # ---- personal : single-level ----
    if account == 'personal':
        subs = [('Posts', 'grid-outline', 'posts'), ('Peaks', 'film-outline', 'peaks'),
                ('Activities', 'walk-outline', 'acts')]
        if is_owner:
            subs.append(('Saved', 'bookmark-outline', 'saved'))
        nav = subnav('life', subs, 'life')
        panes = (pane('life.posts', grid(9), True) + pane('life.peaks', peaks_grid(), False)
                 + pane('life.acts', activities_list(), False)
                 + (pane('life.saved', saved_grid(), False) if is_owner else ''))
        return nav + panes

    # ---- creator : Lifestyle + Channel ----
    if account == 'creator':
        mains = (f'<button class="pv-main pv-main-on" data-main="life">'
                 f'<ion-icon name="heart" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Lifestyle</button>'
                 f'<button class="pv-main" data-main="chan">'
                 f'<ion-icon name="sparkles-outline" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Channel</button>')
        life_subs = [('Posts', 'grid-outline', 'posts'), ('Peaks', 'film-outline', 'peaks'),
                     ('Activities', 'walk-outline', 'acts')]
        if is_owner:
            life_subs.append(('Saved', 'bookmark-outline', 'saved'))
        chan_subs = [('Channel', 'sparkles-outline', 'chan'), ('1:1', 'videocam-outline', 'oneone'),
                     ('Packs', 'cube-outline', 'packs')]
        navs = subnav('life', life_subs, 'life') + subnav('chan', chan_subs, 'life')
        panes = (pane('life.posts', grid(9), True) + pane('life.peaks', peaks_grid(), False)
                 + pane('life.acts', activities_list(), False)
                 + (pane('life.saved', saved_grid(), False) if is_owner else '')
                 + pane('chan.chan', channel_content(is_owner, dark), False)
                 + pane('chan.oneone', _oneone_pane(is_owner, dark), False)
                 + pane('chan.packs', _packs_pane(is_owner, dark), False))
        return f'<nav class="pv-mains">{mains}</nav>{navs}{panes}'

    # ---- business : Lifestyle + Services ----
    mains = (f'<button class="pv-main pv-main-on" data-main="life">'
             f'<ion-icon name="heart" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Lifestyle</button>'
             f'<button class="pv-main" data-main="srv">'
             f'<ion-icon name="briefcase-outline" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>Services</button>')
    life_subs = [('Posts', 'grid-outline', 'posts'), ('Activities', 'walk-outline', 'acts')]
    if is_owner:
        life_subs.append(('Saved', 'bookmark-outline', 'saved'))
    srv_subs = [('Booking', 'calendar-outline', 'book'), ('Programme', 'today-outline', 'prog')]
    navs = subnav('life', life_subs, 'life') + subnav('srv', srv_subs, 'life')
    panes = (pane('life.posts', grid(9), True) + pane('life.acts', activities_list(), False)
             + (pane('life.saved', saved_grid(), False) if is_owner else '')
             + pane('srv.book', services_content(is_owner, dark), False)
             + pane('srv.prog', _programme_pane(), False))
    return f'<nav class="pv-mains">{mains}</nav>{navs}{panes}'


def _oneone_pane(is_owner: bool, dark: bool = True) -> str:
    """Tab 1:1 — combine DS au validé : avatar + rating + durées/tarifs + inclus +
    'Réserver une session' → FLOW COMPLET p2_creator_booking (founder : flow complet pour réserver)."""
    th = _th(dark)
    if is_owner:
        return ('<section class="pv-mon"><div class="pv-mon-stats">'
                '<div class="pv-mon-stat"><b>11</b><span>Résa · mois</span></div>'
                '<div class="pv-mon-stat"><b>$328</b><span>Revenus 30j</span></div>'
                '<div class="pv-mon-stat"><b>4.9★</b><span>Note</span></div></div>'
                '<div class="pv-1card"><div class="pv-1head"><ion-icon name="videocam" style="font-size:20px;color:#11C6FF"></ion-icon>'
                '<div><h4>Sessions 1:1 live</h4><p>Visio live (Agora) · 4.9★ · 138 sessions</p></div></div>'
                '<div class="pv-durs">' + ''.join(
                    f'<div class="pv-dur"><b>{m}</b><span>min</span><em>${p}</em></div>'
                    for m, p in [('15', '15'), ('30', '28'), ('60', '45'), ('90', '69')]) +
                '</div><button class="pv-config" style="width:100%;margin:14px 0 0">Configurer</button></div></section>')
    incl = ''.join(
        f'<div class="pv-incl"><ion-icon name="checkmark-circle" style="font-size:16px;color:var(--mint)"></ion-icon>{txt}</div>'
        for txt in ['Visio live HD (Agora)', 'Plan personnalisé écrit après', 'Replay dispo 7 jours'])
    return (f'<section class="pv-mon"><div class="pv-1card">'
            '<div class="pv-1head"><img class="pv-1av" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&q=80" alt=""/>'
            '<div><h4>Session 1:1 avec Sara</h4><p>Coaching perso visio live · 4.9★ · 138 sessions</p></div></div>'
            '<div class="pv-durs">' + ''.join(
                f'<div class="pv-dur"><b>{m}</b><span>min</span><em>${p}</em></div>'
                for m, p in [('15', '15'), ('30', '28'), ('60', '45'), ('90', '69')]) +
            f'</div><div class="pv-incls">{incl}</div>'
            f'<a class="pv-mc-cta" href="../p2_creator_booking_v2_{th}/code.html">Réserver une session</a>'
            '</div></section>')


def _packs_pane(is_owner: bool, dark: bool = True) -> str:
    """Tab Packs — combine DS au validé creator_packages_view : chaque pack = IMAGE + desc + prix (pas que texte)."""
    th = _th(dark)
    link = f'../creator_packages_view_v2_{th}/code.html'
    packs = [('1607962837359-5e7e89f86776', 'BEST SELLER', 'linear-gradient(135deg,#FFB4A2,#FFCFD2)',
              'Transformation · 3 mois', '$320', '$269',
              ['2 sessions 1:1 / semaine', 'Plan nutrition personnalisé']),
             ('1517836357463-d25dfeac3438', None, '', 'Reprise en douceur', None, '$99',
              ['4 séances · niveau débutant', 'Suivi messagerie 1 mois']),
             ('1534438327276-14e5300c3a48', None, '', 'Prep compétition', '$520', '$449',
              ['Programme 12 semaines intensif', 'Bilan hebdo + ajustements'])]
    cards = ''
    for img_id, badge, bc, title, old, new, perks in packs:
        price = (f'<div class="pv-price"><span class="pv-price-old">{old}</span>'
                 f'<span class="pv-price-new">{new}</span></div>' if old
                 else f'<div class="pv-price"><span class="pv-price-new">{new}</span></div>')
        perk_html = ''.join(_perk('checkmark-circle', '#33A089', p, '') for p in perks)
        cta = ('<button class="pv-config" style="width:100%;margin:12px 0 0">Configurer</button>' if is_owner
               else f'<a class="pv-mc-cta" href="{link}">Acheter</a>')
        badge_h = f'<span class="pv-mc-badge" style="background:{bc}">{badge}</span>' if badge else ''
        cards += (f'<div class="pv-mc"><div class="pv-mc-hero" style="aspect-ratio:16/9">'
                  f'<img loading="lazy" src="https://images.unsplash.com/photo-{img_id}?w=720&h=405&fit=crop&q=80" alt=""/>{badge_h}</div>'
                  f'<div class="pv-mc-body"><h4>{title}</h4>{price}'
                  f'<div class="pv-perks pv-perks-sm">{perk_html}</div>{cta}</div></div>')
    return f'<section class="pv-mon">{cards}</section>'


def _programme_pane() -> str:
    """Programme = petit TABLEAU clicable (jour/cours/heure) → déplie le détail du cours en dessous
    (coach, places, description). Founder jun03. Accordéon : 1 ligne ouverte à la fois."""
    courses = [
        ('Lun', 'CrossFit Box', '18h00', '#33A089', 'Coach Mike', '12 places · 8 prises',
         'WOD haute intensité · 60 min · niveau intermédiaire à avancé.'),
        ('Mar', 'Yoga flow', '07h00', '#9966FF', 'Sara Khan', '15 places · 11 prises',
         'Vinyasa matinal · 45 min · tous niveaux.'),
        ('Mer', 'PT individuel', '12h00', '#11C6FF', 'Coach Mike', 'Sur réservation',
         'Séance personnalisée 1:1 · 50 min.'),
        ('Jeu', 'HIIT', '19h00', '#FF4658', 'Léa P.', '20 places · 14 prises',
         'Circuit cardio · 40 min · brûle-graisses.'),
        ('Ven', 'Pilates', '08h00', '#FFA63D', 'Sara Khan', '10 places · 6 prises',
         'Renfo profond · 50 min · doux.'),
    ]
    rows = ''
    for i, (d, c, t, col, coach, places, desc) in enumerate(courses):
        open0 = i == 0  # première ligne ouverte par défaut (visible en PNG)
        rows += (
            f'<div class="pg-item">'
            f'<button class="pg-row{" pg-open" if open0 else ""}" data-prog="{i}">'
            f'<span class="pg-day" style="background:{col}1A;color:{col}">{d}</span>'
            f'<span class="pg-course">{c}</span><span class="pg-time">{t}</span>'
            f'<ion-icon name="chevron-down" class="pg-chev"></ion-icon></button>'
            f'<div class="pg-detail" data-prog-d="{i}"{"" if open0 else " hidden"}>'
            f'<div class="pg-drow"><ion-icon name="person-outline" style="font-size:15px;color:{col}"></ion-icon>{coach}</div>'
            f'<div class="pg-drow"><ion-icon name="people-outline" style="font-size:15px;color:{col}"></ion-icon>{places}</div>'
            f'<p class="pg-desc">{desc}</p></div></div>')
    return f'<section class="pv-mon"><div class="pv-prog-h">Cette semaine</div><div class="pg-table">{rows}</div></section>'


def role_line(account: str) -> str:
    return {
        'personal': 'Montréal · Daily flows 🍃',
        'creator': 'Yoga coach · Montréal · Daily flows 🍃',
        'business': 'Vibe Fitness Studio · 12 rue de Rivoli, Paris 🏋️',
    }[account]


def profile_html(account: str, view: str, dark: bool) -> str:
    """view ∈ {'owner','visitor','fan','private'}."""
    t = theme(dark)
    is_owner = view == 'owner'
    name = 'Vibe Fitness Studio' if account == 'business' else 'Sara Khan'
    peaks_stat = '' if account == 'business' else '<div class="pv-stat"><b>89</b><span>Peaks</span></div>'

    if is_owner:
        action = '<button class="pv-follow">Modifier</button>'
        icon = ('<button class="pv-icon-btn" aria-label="Partager">'
                '<ion-icon name="share-social-outline" style="font-size:18px"></ion-icon></button>')
    elif view == 'fan':
        action = ('<button class="pv-follow pv-follow-on">'
                  '<ion-icon name="checkmark" style="font-size:15px;vertical-align:middle;margin-right:3px"></ion-icon>Fan</button>')
        icon = (f'<button class="pv-icon-btn" aria-label="Message">{canonical_msg_icon(18)}</button>')
    else:  # visitor (not fan) or private — canonical Smuppy = "Become a fan" (jamais Follow/Suivre)
        action = '<button class="pv-follow">Become a fan</button>'
        icon = (f'<button class="pv-icon-btn" aria-label="Message">{canonical_msg_icon(18)}</button>')

    fan_badge = ('<span class="pv-fanbadge"><ion-icon name="ribbon" style="font-size:11px;vertical-align:middle;'
                 'margin-right:3px"></ion-icon>Membre depuis juin 2026</span>') if view == 'fan' else ''
    content = locked_gate() if view == 'private' else tabs_block(account, is_owner, dark)

    body = f'''<section class="pv-cover">
  <img src="{COVER}" alt="Cover"/>
  <button class="pv-back" aria-label="Retour"><ion-icon name="chevron-back" style="font-size:22px;color:#fff"></ion-icon></button>
  <button class="pv-more" aria-label="Plus"><ion-icon name="ellipsis-horizontal" style="font-size:20px;color:#fff"></ion-icon></button>
</section>
<section class="pv-headrow">
  <div class="pv-avatar">
    <img src="{AVATAR}" alt="{name}"/>
    <span class="pv-verified"><ion-icon name="checkmark" style="font-size:11px;color:#fff"></ion-icon></span>
  </div>
  <div class="pv-actions">{action}{icon}</div>
</section>
<section class="pv-meta">
  <h1 class="pv-name">{name} <ion-icon name="checkmark-circle" style="font-size:16px;color:{MINT}"></ion-icon></h1>
  <p class="pv-role">{role_line(account)}</p>
  <p class="pv-bio">Helping you find your inner peace through movement and breath. <span class="pv-tag">#wellnessjourney</span> <span class="pv-tag">#yogalife</span></p>
  {fan_badge}
</section>
<section class="pv-stats">
  <div class="pv-stat"><b>24.3K</b><span>Fans</span></div>
  <div class="pv-stat"><b>412</b><span>Posts</span></div>
  {peaks_stat}
</section>
{content}
{canonical_bnav('profile', dark=dark)}'''

    css = f'''
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{height:100%}}
  body{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;background:var(--page);color:var(--text);
    -webkit-font-smoothing:antialiased}}
  :root{{--page:{t['page']};--card:{t['card']};--text:{t['text']};--sub:{t['sub']};
    --mint:{MINT};--border:{t['border']};--input-bg:{t['input_bg']};--input-border:{t['input_border']}}}
  .device{{position:relative;width:393px;height:852px;overflow-y:auto;overflow-x:hidden;background:var(--page)}}
  .device::-webkit-scrollbar{{display:none}}
  .pv-cover{{position:relative;width:100%;aspect-ratio:2/1;overflow:hidden}}
  .pv-cover img{{width:100%;height:100%;object-fit:cover}}
  .pv-back,.pv-more{{position:absolute;top:14px;width:34px;height:34px;border:none;border-radius:999px;
    background:rgba(0,0,0,.35);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);
    display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:5}}
  .pv-back{{left:14px}} .pv-more{{right:14px}}
  /* Instagram header : avatar LEFT overlapping cover, actions aligned right */
  .pv-headrow{{display:flex;align-items:flex-end;justify-content:space-between;
    padding:0 16px;margin-top:-34px}}
  .pv-avatar{{position:relative;flex-shrink:0}}
  .pv-avatar img{{width:84px;height:84px;border-radius:999px;object-fit:cover;
    border:4px solid var(--page);box-shadow:0 6px 18px rgba(0,0,0,.3)}}
  .pv-verified{{position:absolute;bottom:3px;right:3px;width:22px;height:22px;border-radius:999px;
    background:var(--mint);display:flex;align-items:center;justify-content:center;border:2.5px solid var(--page)}}
  .pv-actions{{display:flex;align-items:center;gap:8px;padding-bottom:4px}}
  .pv-follow{{height:38px;padding:0 22px;border:none;border-radius:999px;
    background:linear-gradient(135deg,{GRAD_A} 0%,{GRAD_B} 100%);color:#fff;
    font-family:inherit;font-size:13.5px;font-weight:700;cursor:pointer;
    box-shadow:0 4px 14px rgba(51,160,137,0.175)}}
  .pv-follow-on{{background:var(--card);color:var(--mint);
    border:1.5px solid rgba(51,160,137,0.275);box-shadow:0 0 14px rgba(51,160,137,0.2)}}
  .pv-fanbadge{{display:inline-flex;align-items:center;margin-top:9px;padding:4px 11px;border-radius:999px;
    background:rgba(51,160,137,0.12);border:1px solid rgba(51,160,137,0.15);
    font-size:11px;font-weight:700;color:var(--mint)}}
  .pv-icon-btn{{width:38px;height:38px;border:1.5px solid rgba(51,160,137,0.225);border-radius:999px;
    background:var(--card);color:var(--mint);display:flex;align-items:center;justify-content:center;cursor:pointer;
    box-shadow:0 0 16px rgba(51,160,137,0.28),0 0 0 1px rgba(51,160,137,0.15) inset;
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.175))}}
  /* Meta : LEFT-aligned */
  .pv-meta{{padding:12px 16px 0}}
  .pv-name{{font-size:19px;font-weight:800;letter-spacing:-.01em;display:flex;align-items:center;gap:6px}}
  .pv-role{{font-size:13px;font-weight:500;color:var(--sub);margin-top:3px}}
  .pv-bio{{font-size:13px;font-weight:500;color:var(--sub);margin-top:7px;line-height:1.5}}
  .pv-tag{{color:var(--mint);font-weight:700}}
  /* Stats : inline left (Instagram) */
  .pv-stats{{display:flex;gap:22px;padding:14px 16px 4px}}
  .pv-stat{{display:flex;align-items:baseline;gap:5px}}
  .pv-stat b{{font-size:15px;font-weight:800;color:var(--text)}}
  .pv-stat span{{font-size:13px;font-weight:500;color:var(--sub)}}
  /* Main pills (2-level types) */
  .pv-mains{{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin:14px 16px 8px;
    padding:4px;border-radius:999px;background:var(--input-bg);border:1px solid var(--input-border)}}
  .pv-main{{padding:10px 0;border:none;border-radius:999px;background:transparent;color:var(--sub);
    font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;
    display:inline-flex;align-items:center;justify-content:center}}
  .pv-main-on{{background:var(--card);color:var(--mint);
    box-shadow:0 0 16px rgba(51,160,137,0.175),0 0 0 1px rgba(51,160,137,0.225),0 2px 8px rgba(0,0,0,{t['dim']})}}
  /* Sub pills */
  .pv-subs{{display:grid;gap:4px;margin:8px 16px 16px;padding:4px;border-radius:999px;
    background:var(--input-bg);border:1px solid var(--input-border)}}
  .pv-sub{{padding:8px 0;border:none;border-radius:999px;background:transparent;color:var(--sub);
    font-family:inherit;font-size:12px;font-weight:600;cursor:pointer;
    display:inline-flex;align-items:center;justify-content:center}}
  .pv-sub-on{{background:var(--card);color:var(--mint);
    box-shadow:0 0 14px rgba(51,160,137,0.15),0 0 0 1px rgba(51,160,137,0.2),0 2px 6px rgba(0,0,0,{t['dim']})}}
  .pv-config{{margin:0 16px 12px;width:calc(100% - 32px);height:40px;border:1.5px solid rgba(51,160,137,0.225);
    border-radius:14px;background:var(--card);color:var(--mint);font-family:inherit;font-size:13px;font-weight:700;
    cursor:pointer;box-shadow:0 0 14px rgba(51,160,137,0.2)}}
  /* Grid 3-col */
  .pv-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;padding:0 16px 100px}}
  .pv-tile{{position:relative;aspect-ratio:1/1;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
  .pv-tile img{{width:100%;height:100%;object-fit:cover;display:block}}
  /* Peaks grid (2-col taller) */
  .pv-pgrid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0 16px 100px}}
  .pv-ptile{{position:relative;aspect-ratio:3/4;border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
  .pv-ptile img{{width:100%;height:100%;object-fit:cover;display:block}}
  .pv-ptile-play{{position:absolute;top:8px;left:8px;display:flex;align-items:center;gap:3px;padding:2px 7px;
    border-radius:999px;background:rgba(0,0,0,.45);color:#fff;font-size:10px;font-weight:700}}
  /* Activities (Strava-style) */
  .pv-acts{{display:flex;flex-direction:column;gap:10px;padding:0 16px 100px}}
  .pv-act{{display:flex;align-items:center;gap:12px;padding:12px;border-radius:18px;
    background:var(--card);border:1px solid var(--border)}}
  .pv-act-ic{{width:44px;height:44px;border-radius:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
  .pv-act-t h4{{font-size:14px;font-weight:800;color:var(--text)}}
  .pv-act-t p{{font-size:12px;font-weight:600;color:var(--text);margin:2px 0}}
  .pv-act-t span{{font-size:11px;font-weight:500;color:var(--sub)}}
  /* Monetization panes (channel/services/packs/1:1) */
  .pv-mon{{padding:0 16px 100px;display:flex;flex-direction:column;gap:12px}}
  .pv-mon-stats{{display:grid;grid-template-columns:repeat(3,1fr);padding:12px 0;
    border-top:1px solid var(--border);border-bottom:1px solid var(--border)}}
  .pv-mon-stat{{display:flex;flex-direction:column;align-items:center;gap:3px}}
  .pv-mon-stat b{{font-size:17px;font-weight:800;color:var(--text)}}
  .pv-mon-stat span{{font-size:10px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:.06em}}
  .pv-offer{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:14px;border-radius:18px;
    background:var(--card);border:1px solid var(--border)}}
  .pv-offer-ic{{width:44px;height:44px;border-radius:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
  .pv-offer-t{{flex:1;min-width:140px}}
  .pv-offer-t h4{{font-size:13.5px;font-weight:800;color:var(--text)}}
  .pv-offer-t p{{font-size:11.5px;font-weight:500;color:var(--sub);margin-top:2px}}
  .pv-buy{{padding:9px 18px;border:none;border-radius:999px;background:linear-gradient(135deg,{GRAD_A},{GRAD_B});
    color:#fff;font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer;white-space:nowrap}}
  .pv-durs{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}}
  .pv-dur{{background:var(--input-bg);border:1px solid var(--input-border);border-radius:12px;padding:8px 0;text-align:center}}
  .pv-dur b{{font-size:15px;font-weight:800;color:var(--text)}}
  .pv-dur span{{display:block;font-size:9px;color:var(--sub);font-weight:600}}
  .pv-dur em{{font-size:11px;font-weight:700;color:var(--mint);font-style:normal}}
  .pv-prog-h{{font-size:13px;font-weight:800;color:var(--text);margin-bottom:2px}}
  .pv-prog{{display:flex;align-items:center;gap:12px;padding:11px 12px;border-radius:14px;
    background:var(--card);border:1px solid var(--border)}}
  .pv-prog-day{{width:42px;text-align:center;padding:4px 0;border-radius:9px;font-size:11px;font-weight:800}}
  .pv-prog-txt{{font-size:13px;font-weight:600;color:var(--text)}}
  /* Programme : tableau clicable + détail dépliable (accordéon) */
  .pg-table{{border-radius:18px;overflow:hidden;background:var(--card);border:1px solid var(--border)}}
  .pg-item:not(:last-child){{border-bottom:1px solid var(--border)}}
  .pg-row{{width:100%;display:flex;align-items:center;gap:12px;padding:13px 14px;border:none;
    background:transparent;cursor:pointer;font-family:inherit}}
  .pg-day{{width:42px;text-align:center;padding:4px 0;border-radius:9px;font-size:11px;font-weight:800;flex-shrink:0}}
  .pg-course{{flex:1;text-align:left;font-size:14px;font-weight:700;color:var(--text)}}
  .pg-time{{font-size:12.5px;font-weight:600;color:var(--sub)}}
  .pg-chev{{font-size:16px;color:var(--sub);transition:transform .2s}}
  .pg-row.pg-open .pg-chev{{transform:rotate(180deg)}}
  .pg-detail{{padding:2px 14px 14px 68px;display:flex;flex-direction:column;gap:7px}}
  .pg-drow{{display:flex;align-items:center;gap:7px;font-size:12.5px;font-weight:600;color:var(--text)}}
  .pg-desc{{font-size:12px;color:var(--sub);line-height:1.5;margin-top:2px}}
  /* rich media offer cards (combine DS + validated screens) */
  .pv-mc{{border-radius:20px;overflow:hidden;background:var(--card);border:1px solid var(--border);box-shadow:0 4px 18px rgba(0,0,0,{t['dim']})}}
  .pv-mc-hero{{position:relative;width:100%;overflow:hidden}}
  .pv-mc-hero img{{width:100%;height:100%;object-fit:cover;display:block}}
  .pv-mc-badge{{position:absolute;top:10px;left:10px;padding:4px 10px;border-radius:999px;color:#fff;font-size:10px;font-weight:800;letter-spacing:.04em}}
  .pv-mc-body{{padding:14px}}
  .pv-mc-body h4{{font-size:15px;font-weight:800;color:var(--text)}}
  .pv-mc-sub{{font-size:12px;font-weight:500;color:var(--sub);margin-top:3px}}
  .pv-mc-cta{{display:block;text-align:center;text-decoration:none;margin-top:14px;padding:12px 0;border-radius:14px;
    background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:14px;font-weight:700;
    box-shadow:0 6px 16px rgba(51,160,137,0.16)}}
  .pv-perks{{display:flex;flex-direction:column;gap:10px;margin-top:12px}}
  .pv-perks-sm{{gap:7px;margin-top:10px}}
  .pv-perk{{display:flex;align-items:center;gap:10px}}
  .pv-perk-ic{{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
  .pv-perks-sm .pv-perk-ic{{width:22px;height:22px;border-radius:7px}}
  .pv-perk h5{{font-size:12.5px;font-weight:800;color:var(--text)}}
  .pv-perk p{{font-size:11px;font-weight:500;color:var(--sub)}}
  .pv-price{{display:flex;align-items:baseline;gap:8px;margin-top:8px}}
  .pv-price-old{{font-size:13px;font-weight:600;color:var(--sub);text-decoration:line-through}}
  .pv-price-new{{font-size:20px;font-weight:900;color:var(--mint);letter-spacing:-.02em}}
  .pv-1card{{border-radius:20px;background:var(--card);border:1px solid var(--border);padding:16px;box-shadow:0 4px 18px rgba(0,0,0,{t['dim']})}}
  .pv-1head{{display:flex;align-items:center;gap:11px;margin-bottom:14px}}
  .pv-1av{{width:44px;height:44px;border-radius:999px;object-fit:cover}}
  .pv-1head h4{{font-size:14.5px;font-weight:800;color:var(--text)}}
  .pv-1head p{{font-size:11.5px;font-weight:500;color:var(--sub);margin-top:2px}}
  .pv-incls{{display:flex;flex-direction:column;gap:8px;margin-top:14px}}
  .pv-incl{{display:flex;align-items:center;gap:8px;font-size:12.5px;font-weight:500;color:var(--text)}}
{CANONICAL_BNAV_CSS.strip().removeprefix('<style>').removesuffix('</style>')}'''

    return f'''<!DOCTYPE html><html lang="fr" class="{t['html']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=393, initial-scale=1">
<title>Smuppy V2 — Profile {account} {'owner' if is_owner else 'visitor'}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<style>{css}</style></head>
<body><div class="device">{body}</div>
<script>
  // Interactive tabs : main pills swap sub-nav, sub pills swap content panes
  document.querySelectorAll('.pv-main').forEach(b => b.addEventListener('click', () => {{
    const m = b.dataset.main;
    document.querySelectorAll('.pv-main').forEach(x => x.classList.toggle('pv-main-on', x === b));
    document.querySelectorAll('.pv-subs').forEach(n => {{ n.style.display = n.dataset.subnav === m ? 'grid' : 'none'; }});
    const first = document.querySelector('.pv-subs[data-subnav="' + m + '"] .pv-sub');
    if (first) first.click();
  }}));
  document.querySelectorAll('.pv-sub').forEach(b => b.addEventListener('click', () => {{
    const key = b.dataset.sub;
    b.closest('.pv-subs').querySelectorAll('.pv-sub').forEach(x => x.classList.toggle('pv-sub-on', x === b));
    document.querySelectorAll('.pv-pane').forEach(p => {{ p.hidden = p.dataset.pane !== key; }});
  }}));
  // Programme accordéon : tap une ligne → déplie son détail (1 ouverte à la fois)
  document.querySelectorAll('.pg-row').forEach(b => b.addEventListener('click', () => {{
    const i = b.dataset.prog;
    const d = document.querySelector('.pg-detail[data-prog-d="' + i + '"]');
    const wasOpen = d && !d.hidden;
    document.querySelectorAll('.pg-detail').forEach(x => {{ x.hidden = true; }});
    document.querySelectorAll('.pg-row').forEach(x => x.classList.remove('pg-open'));
    if (!wasOpen && d) {{ d.hidden = false; b.classList.add('pg-open'); }}
  }}));
  // hash deep-link : #main.sub activates that tab on load (used to capture each state)
  if (location.hash.length > 1) {{
    const sub = document.querySelector('.pv-sub[data-sub="' + location.hash.slice(1) + '"]');
    if (sub) {{ const mn = sub.closest('.pv-subs').dataset.subnav;
      const mb = document.querySelector('.pv-main[data-main="' + mn + '"]'); if (mb) mb.click(); sub.click(); }}
  }}
</script>
</body></html>'''


def main() -> None:
    # (account, view) — view ∈ owner/visitor/fan/private
    variants = [
        ('personal', 'owner'), ('personal', 'visitor'), ('personal', 'private'),
        ('creator', 'owner'), ('creator', 'visitor'), ('creator', 'fan'), ('creator', 'private'),
        ('business', 'owner'), ('business', 'visitor'), ('business', 'private'),
    ]
    written = 0
    for account, view in variants:
        for dark in (True, False):
            theme_name = 'dark' if dark else 'light'
            name = f'profile_{account}_{view}_v2_{theme_name}'
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(profile_html(account, view, dark), encoding='utf-8')
            written += 1
    print(f'wrote {written} profile screens ({len(variants)} variants x2) to {OUT}')


if __name__ == '__main__':
    main()
