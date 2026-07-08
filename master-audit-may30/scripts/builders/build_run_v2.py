#!/usr/bin/env python3
"""Smuppy V2 — RUN feature (Personal Activity Run V1) — ultra-modern redesign.
Audit source: docs/features/PERSONAL_ACTIVITY_RUN_BEHAVIOR_CONTRACT.md + src/screens/activities/.
Screens (toutes + tous boutons) :
  permission · gps_denied · countdown · tracking · paused · gps_search · stop_confirm ·
  share · history (Mes runs + activity ring) · records · detail (splits) · empty
DS V2 soft teal #33A089. 393×852. Pure stdlib + ionicons CDN. Self-contained.
"""
import sys
from pathlib import Path
sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from canonical_bnav import canonical_bnav, CANONICAL_BNAV_CSS  # noqa: E402

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
MINT, GRAD_A, GRAD_B = '#33A089', '#41AD96', '#2C95A0'
IMG = "https://images.unsplash.com/photo-"


def theme(dark):
    if dark:
        return dict(page='#000000', card='#14141A', text='#F1F4F6', sub='#8B8B95',
                    border='rgba(255,255,255,0.06)', input_bg='rgba(255,255,255,0.04)',
                    input_border='rgba(255,255,255,0.10)', dim='0.5', html='dark',
                    map='linear-gradient(135deg,#0d1b1a,#0a0f14 60%,#101820)')
    return dict(page='#F6F8FA', card='#FFFFFF', text='#0F172A', sub='#64748B',
                border='#EEF1F4', input_bg='#FFFFFF', input_border='#E5E9EB',
                dim='0.06', html='light', map='linear-gradient(135deg,#e8f3f0,#dfeaf0 60%,#eef3f6)')


# ── shared bits ──────────────────────────────────────────────
ROUTE = "M40,520 C70,470 60,400 110,380 C170,355 180,300 150,250 C125,205 165,160 230,165 C300,170 320,120 300,80"


def _perspective_grid(night: bool) -> str:
    """Hyper-realistic NIGHTRUN city grid — 1-point perspective floor receding to a
    horizon, glowing neon-teal streets. Founder ref jun03 ('comme ça la map')."""
    W, H = 393, 600
    horizon = 78          # y of the vanishing horizon
    vpx = 196             # vanishing point x (center)
    # Vertical avenues: ground points spread wide (beyond viewport), converge to VP.
    verticals = []
    gx = -340
    while gx <= W + 340:
        verticals.append(f'M{gx},{H} L{vpx},{horizon}')
        gx += 46
    # Cross streets: perspective-spaced y (denser toward horizon), full-width span.
    horizontals = []
    N = 16
    for i in range(1, N + 1):
        d = i / N
        y = horizon + (H - horizon) * (d ** 2.3)   # ease → bunching near horizon
        # width of the visible band grows with depth (closer = wider)
        spread = 60 + d * 520
        horizontals.append(f'M{vpx - spread},{y:.1f} L{vpx + spread},{y:.1f}')
    grid = ' '.join(verticals + horizontals)
    # A few brighter "main avenues" for depth richness.
    mains = f'M{vpx-150},{H} L{vpx-28},{horizon} M{vpx+150},{H} L{vpx+28},{horizon} M-200,{H-40} L{vpx},{horizon}'
    if night:
        faint, bright = 'rgba(51,160,137,.16)', 'rgba(91,240,200,.55)'
    else:
        faint, bright = 'rgba(23,106,90,.18)', 'rgba(51,160,137,.42)'
    return (f'<path d="{grid}" fill="none" stroke="{faint}" stroke-width="1.1" filter="url(#gridglow)"/>'
            f'<path d="{mains}" fill="none" stroke="{bright}" stroke-width="1.8" filter="url(#gridglow)"/>')


def map_route(t, dim=False):
    """NIGHTRUN/DAYRUN map — hyper-realistic 3D neon city grid (founder ref jun03).
      DARK  = NightRun : near-black city + glowing teal street grid receding to horizon.
      LIGHT = DayRun   : light premium city + teal grid + gradient ribbon route.
    En prod = Mapbox dark/light + pitch 3D + road LineLayers glow teal + route LineLayer."""
    scrim = '<div style="position:absolute;inset:0;background:rgba(0,0,0,.45)"></div>' if dim else ''
    night = t['html'] == 'dark'
    defs = (f'<linearGradient id="rgrad" x1="0" y1="1" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{GRAD_A}"/><stop offset="1" stop-color="{GRAD_B}"/></linearGradient>'
            f'<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">'
            f'<feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
            f'<filter id="gridglow" x="-20%" y="-20%" width="140%" height="140%">'
            f'<feGaussianBlur stdDeviation="1.6"/></filter>'
            f'<filter id="softsh" x="-30%" y="-30%" width="160%" height="160%">'
            f'<feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="rgba(20,90,78,.30)"/></filter>'
            f'<radialGradient id="horizonGlow" cx="50%" cy="13%" r="55%">'
            f'<stop offset="0" stop-color="{"rgba(51,160,137,.30)" if night else "rgba(51,160,137,.16)"}"/>'
            f'<stop offset="1" stop-color="rgba(0,0,0,0)"/></radialGradient>'
            f'<radialGradient id="vign" cx="50%" cy="42%" r="75%">'
            f'<stop offset="60%" stop-color="rgba(0,0,0,0)"/>'
            f'<stop offset="100%" stop-color="{"rgba(0,0,0,.55)" if night else "rgba(40,60,70,.18)"}"/></radialGradient>')
    if night:
        bg = 'radial-gradient(130% 100% at 50% 8%, #0a1f1c 0%, #050d12 45%, #03070b 100%)'
        route = (f'<path d="{ROUTE}" fill="none" stroke="rgba(91,240,200,.20)" stroke-width="20" stroke-linecap="round" filter="url(#glow)"/>'
                 f'<path d="{ROUTE}" fill="none" stroke="rgba(91,240,200,.5)" stroke-width="9" stroke-linecap="round"/>'
                 f'<path d="{ROUTE}" fill="none" stroke="#5BF0C8" stroke-width="4" stroke-linecap="round"/>'
                 f'<circle cx="300" cy="80" r="11" fill="#5BF0C8" stroke="#fff" stroke-width="3"/>')
    else:
        bg = 'radial-gradient(130% 100% at 50% 10%, #f5faf8 0%, #e7f0f1 50%, #d6e3e6 100%)'
        route = (f'<path d="{ROUTE}" fill="none" stroke="url(#rgrad)" stroke-width="7" stroke-linecap="round" filter="url(#softsh)"/>'
                 f'<path d="{ROUTE}" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="2" stroke-linecap="round"/>'
                 f'<circle cx="300" cy="80" r="11" fill="{MINT}" stroke="#fff" stroke-width="3"/>')
    return (f'<div class="rn-map" style="background:{bg}">'
            f'<svg class="rn-route" viewBox="0 0 393 600" preserveAspectRatio="xMidYMid slice">'
            f'<defs>{defs}</defs>'
            f'<rect x="0" y="0" width="393" height="600" fill="url(#horizonGlow)"/>'
            f'{_perspective_grid(night)}'
            f'{route}'
            f'<circle cx="40" cy="520" r="9" fill="#fff" stroke="{MINT}" stroke-width="4"/>'
            f'<rect x="0" y="0" width="393" height="600" fill="url(#vign)"/>'
            f'</svg>{scrim}</div>')


def ring(pct, label_top, label_bot, size=180):
    import math
    r = size / 2 - 14
    circ = 2 * math.pi * r
    off = circ * (1 - pct)
    c = size / 2
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
            f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" stroke="rgba(51,160,137,.16)" stroke-width="14"/>'
            f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" stroke="url(#rg)" stroke-width="14" stroke-linecap="round"'
            f' stroke-dasharray="{circ:.1f}" stroke-dashoffset="{off:.1f}" transform="rotate(-90 {c} {c})"/>'
            f'<defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{GRAD_A}"/><stop offset="1" stop-color="{GRAD_B}"/></linearGradient></defs>'
            f'<text x="{c}" y="{c-4}" text-anchor="middle" font-size="30" font-weight="900" fill="var(--text)">{label_top}</text>'
            f'<text x="{c}" y="{c+20}" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sub)">{label_bot}</text>'
            f'</svg>')


def stat(num, lbl, ic, color=None):
    col = color or 'var(--mint)'
    return (f'<div class="rn-stat"><ion-icon name="{ic}" style="font-size:15px;color:{col}"></ion-icon>'
            f'<div class="rn-stat-n">{num}</div><div class="rn-stat-l">{lbl}</div></div>')


def close_btn():
    return '<button class="rn-close"><ion-icon name="close" style="font-size:22px;color:#fff"></ion-icon></button>'


def primary(label):
    return f'<button class="rn-primary">{label}</button>'


def ghost(label):
    return f'<button class="rn-ghost">{label}</button>'


# ── screens ──────────────────────────────────────────────────
def s_permission(t):
    bullets = ''.join(
        f'<div class="rn-bul"><ion-icon name="{ic}" style="font-size:18px;color:var(--mint)"></ion-icon>'
        f'<div><h4>{h}</h4><p>{p}</p></div></div>'
        for ic, h, p in [
            ('navigate', 'Tracé GPS précis', 'On suit ta distance, ton allure et ton parcours.'),
            ('lock-closed', 'En arrière-plan', 'Continue le suivi écran verrouillé, sans drainer ta batterie.'),
            ('shield-checkmark', 'Privé par défaut', 'Tes runs sont à toi — tu choisis quoi partager.')])
    return (f'<section class="rn-pad rn-center">'
            f'<div class="rn-hero-ic"><ion-icon name="location" style="font-size:34px;color:#fff"></ion-icon></div>'
            f'<h1 class="rn-h1">Active la localisation</h1>'
            f'<p class="rn-sub">Pour suivre ton run, Smuppy a besoin de ta position — même en arrière-plan.</p>'
            f'<div class="rn-bullets">{bullets}</div>'
            f'<div class="rn-actions">{primary("Autoriser la localisation")}{ghost("Plus tard")}</div></section>')


def s_gps_denied(t):
    return (f'<section class="rn-pad rn-center">'
            f'<div class="rn-hero-ic" style="background:rgba(255,166,61,.16)"><ion-icon name="warning" style="font-size:34px;color:#FFA63D"></ion-icon></div>'
            f'<h1 class="rn-h1">Localisation refusée</h1>'
            f'<p class="rn-sub">Sans localisation « Toujours », le suivi s\'arrête si tu verrouilles l\'écran. '
            f'Tu peux courir en gardant l\'app ouverte, ou l\'activer dans les réglages.</p>'
            f'<div class="rn-warn"><ion-icon name="information-circle" style="font-size:18px;color:#FFA63D"></ion-icon>'
            f'Mode premier plan uniquement · garde l\'écran allumé</div>'
            f'<div class="rn-actions">{primary("Activer dans les réglages")}{ghost("Continuer quand même")}</div></section>')


def s_start(t):
    goals = ''.join(
        f'<button class="rn-goal{" rn-goal-on" if on else ""}">{l}</button>'
        for l, on in [('Libre', True), ('5 km', False), ('10 km', False), ('Temps', False)])
    return (f'<div class="rn-full">{map_route(t)}'
            f'<header class="rn-top">{close_btn()}'
            f'<span class="rn-gps rn-gps-ok"><span class="rn-gps-dot"></span>GPS prêt</span></header>'
            f'<div class="rn-start-top"><h2 class="rn-start-h">Prêt à courir&nbsp;?</h2>'
            f'<nav class="rn-goals">{goals}</nav></div>'
            f'<div class="rn-start-center">'
            f'<button class="rn-go"><span class="rn-go-ring"></span>'
            f'<ion-icon name="play" style="font-size:46px;color:#fff;margin-left:6px"></ion-icon>'
            f'<span class="rn-go-lbl">DÉPART</span></button>'
            f'<p class="rn-go-hint">Appuie pour lancer · décompte 3·2·1</p></div>'
            f'<div class="rn-start-opts">'
            f'<span class="rn-opt rn-opt-on"><ion-icon name="mic" style="font-size:15px"></ion-icon>Coach vocal</span>'
            f'<span class="rn-opt"><ion-icon name="lock-closed" style="font-size:15px"></ion-icon>Actif écran verrouillé</span>'
            f'</div></div>')


def s_countdown(t):
    return (f'<div class="rn-full">{map_route(t, dim=True)}'
            f'<div class="rn-cd"><div class="rn-cd-num">3</div><div class="rn-cd-go">Prépare-toi…</div></div></div>')


def _stats_row():
    return (f'<div class="rn-stats">'
            f'{stat("5,2", "km", "navigate")}'
            f'{stat("5\'29\"", "/km", "speedometer-outline", "#11C6FF")}'
            f'{stat("412", "cal", "flame", "#FF7A45")}</div>')


def s_tracking(t):
    return (f'<div class="rn-full">{map_route(t)}'
            f'<header class="rn-top">{close_btn()}'
            f'<span class="rn-gps rn-gps-ok"><span class="rn-gps-dot"></span>GPS</span></header>'
            f'<div class="rn-panel">'
            f'<div class="rn-time">28:30</div><div class="rn-time-l">Temps</div>'
            f'{_stats_row()}'
            f'<div class="rn-ctrls"><button class="rn-pause"><ion-icon name="pause" style="font-size:26px;color:#fff"></ion-icon></button>'
            f'<button class="rn-stop"><ion-icon name="stop" style="font-size:24px;color:#fff"></ion-icon></button></div>'
            f'</div></div>')


def s_paused(t):
    return (f'<div class="rn-full">{map_route(t, dim=True)}'
            f'<header class="rn-top">{close_btn()}'
            f'<span class="rn-gps rn-gps-ok"><span class="rn-gps-dot"></span>GPS</span></header>'
            f'<div class="rn-pause-badge"><ion-icon name="pause-circle" style="font-size:18px"></ion-icon> En pause — en attente de mouvement</div>'
            f'<div class="rn-panel">'
            f'<div class="rn-time" style="color:var(--sub)">28:30</div><div class="rn-time-l">En pause</div>'
            f'{_stats_row()}'
            f'<div class="rn-ctrls"><button class="rn-resume"><ion-icon name="play" style="font-size:24px;color:#fff"></ion-icon>Reprendre</button>'
            f'<button class="rn-stop"><ion-icon name="stop" style="font-size:24px;color:#fff"></ion-icon></button></div>'
            f'</div></div>')


def s_gps_search(t):
    return (f'<div class="rn-full">{map_route(t, dim=True)}'
            f'<header class="rn-top">{close_btn()}</header>'
            f'<div class="rn-search"><div class="rn-search-pulse"><ion-icon name="navigate" style="font-size:30px;color:var(--mint)"></ion-icon></div>'
            f'<h3>Recherche du signal GPS…</h3><p>Sors à découvert pour un meilleur signal.</p></div></div>')


def s_stop_confirm(t):
    return (f'<div class="rn-full">{map_route(t, dim=True)}'
            f'<div class="rn-sheet">'
            f'<div class="rn-sheet-h"></div>'
            f'<h3 class="rn-sheet-t">Terminer ce run ?</h3>'
            f'<div class="rn-sheet-stats"><span><b>5,2</b> km</span><span><b>28:30</b></span><span><b>5\'29"</b>/km</span></div>'
            f'{primary("Terminer le run")}{ghost("Reprendre")}</div></div>')


def s_share(t):
    toggles = ''.join(
        f'<label class="rn-tog{" rn-tog-on" if on else ""}"><span class="rn-tog-ic" style="background:{c}1A;color:{c}">'
        f'<ion-icon name="{ic}" style="font-size:19px"></ion-icon></span>'
        f'<div class="rn-tog-t"><h4>{h}</h4><p>{p}</p></div>'
        f'<span class="rn-check{" rn-check-on" if on else ""}">'
        f'{"<ion-icon name=" + chr(34) + "checkmark" + chr(34) + " style=" + chr(34) + "font-size:14px;color:#fff" + chr(34) + "></ion-icon>" if on else ""}</span></label>'
        for ic, c, h, p, on in [
            ('grid', MINT, 'Publier en Post', 'Carte + stats dans ton feed', True),
            ('film', '#9966FF', 'Partager en Peak', 'Vidéo verticale avec stats animées', False),
            ('location', '#FFA63D', 'Map pin « J\'ai couru ici »', 'Drop un pin sur la carte Xplorer', False)])
    privacy = ''.join(
        f'<button class="rn-priv{" rn-priv-on" if on else ""}"><ion-icon name="{ic}" style="font-size:14px"></ion-icon>{l}</button>'
        for ic, l, on in [('earth', 'Public', True), ('people', 'Fans', False), ('lock-closed', 'Privé', False)])
    return (f'<div class="rn-share">'
            f'<header class="rn-shead">{close_btn()}<span>Partager ton run</span><span style="width:34px"></span></header>'
            f'<div class="rn-scroll">'
            f'<div class="rn-pr"><span class="rn-pr-em">🏆</span><div><b>Nouveau record sur 5K !</b><span>28:30 · 1:42 de mieux que ton précédent best</span></div></div>'
            f'<div class="rn-hero">{map_route(t)}<div class="rn-hero-ov"><span><b>5,2</b> km</span><span><b>28:30</b></span><span><b>5\'29"</b>/km</span></div></div>'
            f'<div class="rn-field"><label>Titre</label><div class="rn-input">Run du matin · nouveau record 🏆 <ion-icon name="pencil" style="font-size:14px;color:var(--sub)"></ion-icon></div></div>'
            f'<div class="rn-field"><label>Description <span style="color:var(--sub)">(optionnel)</span></label><div class="rn-input rn-ta">Belle lumière ce matin le long du fleuve…</div></div>'
            f'<div class="rn-field"><label>Confidentialité</label><div class="rn-privs">{privacy}</div></div>'
            f'<div class="rn-field"><label>Publier vers</label>{toggles}</div>'
            f'</div>'
            f'<div class="rn-share-cta">{primary("Enregistrer &amp; partager")}<div class="rn-share-row">{ghost("Enregistrer")}{ghost("Supprimer")}</div></div>'
            f'</div>')


def s_published(t):
    """Destination de [Enregistrer & partager] — confirmation + récap des cibles publiées."""
    recap = ''.join(
        f'<div class="rn-pub-chip"><ion-icon name="checkmark-circle" style="font-size:16px;color:var(--mint)"></ion-icon>{l}</div>'
        for l in ['Publié en Post', 'Partagé en Peak', 'Map pin déposé'])
    return (f'<section class="rn-pad rn-center">'
            f'<div class="rn-hero-ic"><ion-icon name="checkmark" style="font-size:38px;color:#fff"></ion-icon></div>'
            f'<h1 class="rn-h1">Run partagé&nbsp;! 🎉</h1>'
            f'<p class="rn-sub">5,2 km en 28:30 · ta tribu peut le voir maintenant.</p>'
            f'<div class="rn-pr" style="margin:18px 0"><span class="rn-pr-em">🏆</span>'
            f'<div><b>Nouveau record sur 5K&nbsp;!</b><span>1:42 de mieux que ton précédent best</span></div></div>'
            f'<div class="rn-pub-recap">{recap}</div>'
            f'<div class="rn-actions">{primary("Voir mon post")}{ghost("Voir mes runs")}</div></section>')


def s_discard(t):
    """Modal de [Abandonner] — confirmation destructive."""
    return (f'<div class="rn-full">{map_route(t, dim=True)}'
            f'<div class="rn-sheet">'
            f'<div class="rn-sheet-h"></div>'
            f'<div class="rn-disc-ic"><ion-icon name="trash" style="font-size:26px;color:#FF4658"></ion-icon></div>'
            f'<h3 class="rn-sheet-t">Abandonner ce run&nbsp;?</h3>'
            f'<p class="rn-disc-p">Tu vas perdre ce parcours de <b>5,2 km · 28:30</b> définitivement. '
            f'Cette action est irréversible.</p>'
            f'<button class="rn-danger">Supprimer le run</button>{ghost("Annuler")}</div></div>')


def _run_item():
    items = [('1571019614242-c5c5dee9f50b', "Aujourd'hui · 7h12", '5,2 km', '28:30', "5'29\"/km", True),
             ('1502086223501-7ea6ecd79368', 'Hier · 18h30', '8,1 km', '46:02', "5'41\"/km", False),
             ('1486218119243-13883505764c', 'Lun · 6h45', '3,0 km', '15:48', "5'16\"/km", False)]
    out = ''
    for im, when, dist, dur, pace, pr in items:
        prb = '<span class="rn-li-pr">🏆 PR</span>' if pr else ''
        out += (f'<div class="rn-li"><div class="rn-li-map" style="background:{("linear-gradient(135deg,#0d1b1a,#101820)")}">'
                f'<svg viewBox="0 0 120 90" preserveAspectRatio="none" style="width:100%;height:100%">'
                f'<path d="M12,75 C30,60 25,40 45,38 C70,35 65,15 90,20" fill="none" stroke="{MINT}" stroke-width="3" stroke-linecap="round"/></svg></div>'
                f'<div class="rn-li-t"><div class="rn-li-top"><h4>{dist}</h4>{prb}</div>'
                f'<p>{when}</p><div class="rn-li-meta"><span><ion-icon name="time-outline" style="font-size:12px"></ion-icon>{dur}</span>'
                f'<span><ion-icon name="speedometer-outline" style="font-size:12px"></ion-icon>{pace}</span></div></div>'
                f'<ion-icon name="chevron-forward" style="font-size:18px;color:var(--sub)"></ion-icon></div>')
    return out


def s_history(t, dark):
    return (f'<header class="rn-hh"><button class="rn-back"><ion-icon name="chevron-back" style="font-size:24px;color:var(--text)"></ion-icon></button>'
            f'<span>Mes runs</span><span style="width:34px"></span></header>'
            f'<nav class="rn-tabs"><button class="rn-tab rn-tab-on">Runs</button><button class="rn-tab">Records</button></nav>'
            f'<section class="rn-ringwrap">{ring(0.5, "12,5", "/ 25 km")}'
            f'<div class="rn-ring-side"><div class="rn-ring-stat"><b>3</b><span>runs</span></div>'
            f'<div class="rn-ring-stat"><b>16,3</b><span>km</span></div>'
            f'<div class="rn-ring-stat"><b>1h30</b><span>cette sem.</span></div></div></section>'
            f'<div class="rn-list">{_run_item()}</div>{canonical_bnav("profile", dark=dark)}')


def s_records(t, dark):
    recs = [('flash', MINT, 'Plus rapide 1 km', "4'58\"", 'le 2 juin'),
            ('flash', '#11C6FF', 'Plus rapide 5 km', '28:30', "aujourd'hui · NEW 🏆"),
            ('flash', '#9966FF', 'Plus rapide 10 km', '59:14', 'le 21 mai'),
            ('trail-sign', '#FFA63D', 'Plus longue distance', '21,1 km', 'le 12 mai'),
            ('time', '#FF7A45', 'Plus longue durée', '2h04', 'le 12 mai')]
    rows = ''.join(
        f'<div class="rn-rec"><span class="rn-rec-ic" style="background:{c}1A;color:{c}"><ion-icon name="{ic}" style="font-size:20px"></ion-icon></span>'
        f'<div class="rn-rec-t"><h4>{h}</h4><p>{d}</p></div><div class="rn-rec-v">{v}</div></div>'
        for ic, c, h, v, d in recs)
    return (f'<header class="rn-hh"><button class="rn-back"><ion-icon name="chevron-back" style="font-size:24px;color:var(--text)"></ion-icon></button>'
            f'<span>Mes runs</span><span style="width:34px"></span></header>'
            f'<nav class="rn-tabs"><button class="rn-tab">Runs</button><button class="rn-tab rn-tab-on">Records</button></nav>'
            f'<div class="rn-recs">{rows}</div>{canonical_bnav("profile", dark=dark)}')


def s_detail(t):
    splits = [('1', "5'16\"", '+2m', 100), ('2', "5'24\"", '−1m', 92), ('3', "5'29\"", '+4m', 86),
              ('4', "5'38\"", '0m', 78), ('5', "5'12\"", '−3m', 100)]
    maxw = ''
    rows = ''
    for k, pace, elev, w in splits:
        rows += (f'<div class="rn-split"><span class="rn-split-k">{k}</span>'
                 f'<div class="rn-split-bar"><div class="rn-split-fill" style="width:{w}%"></div></div>'
                 f'<span class="rn-split-p">{pace}</span><span class="rn-split-e">{elev}</span></div>')
    return (f'<header class="rn-shead">{close_btn()}<span>Run du matin 🏆</span><button class="rn-back" style="background:transparent;border:none"><ion-icon name="share-social-outline" style="font-size:20px;color:var(--text)"></ion-icon></button></header>'
            f'<div class="rn-scroll">'
            f'<div class="rn-hero">{map_route(t)}</div>'
            f'<div class="rn-dstats">'
            f'{stat("5,2", "km", "navigate")}{stat("28:30", "temps", "time")}{stat("5\'29\"", "/km", "speedometer-outline", "#11C6FF")}{stat("412", "cal", "flame", "#FF7A45")}</div>'
            f'<h3 class="rn-sec">Splits par km</h3><div class="rn-splits">{rows}</div>'
            f'<div class="rn-dcta">{primary("Repartager ce run")}</div>'
            f'</div>')


def s_empty(t, dark):
    return (f'<header class="rn-hh"><button class="rn-back"><ion-icon name="chevron-back" style="font-size:24px;color:var(--text)"></ion-icon></button>'
            f'<span>Mes runs</span><span style="width:34px"></span></header>'
            f'<section class="rn-empty"><div class="rn-empty-ic"><ion-icon name="walk" style="font-size:38px;color:var(--mint)"></ion-icon></div>'
            f'<h3>Aucun run pour l\'instant</h3><p>Lance ton premier run depuis la carte — distance, allure et records suivis automatiquement.</p>'
            f'{primary("Lancer mon premier run")}</section>{canonical_bnav("profile", dark=dark)}')


CSS = """
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%}}
body{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;background:var(--page);color:var(--text);-webkit-font-smoothing:antialiased}}
:root{{--page:{page};--card:{card};--text:{text};--sub:{sub};--mint:{MINT};--border:{border};--input-bg:{input_bg};--input-border:{input_border}}}
.device{{position:relative;width:393px;height:852px;overflow-y:auto;overflow-x:hidden;background:var(--page)}}
.device::-webkit-scrollbar{{display:none}}
.rn-full{{position:relative;width:393px;height:852px;overflow:hidden}}
.rn-map{{position:absolute;inset:0}}
.rn-grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(51,160,137,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(51,160,137,.08) 1px,transparent 1px);background-size:44px 44px}}
.rn-route{{position:absolute;inset:0;width:100%;height:100%}}
.rn-top{{position:absolute;top:16px;left:16px;right:16px;display:flex;justify-content:space-between;align-items:center;z-index:6}}
.rn-close{{width:38px;height:38px;border:none;border-radius:999px;background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;cursor:pointer}}
.rn-gps{{display:flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:#fff;font-size:11px;font-weight:800}}
.rn-gps-dot{{width:7px;height:7px;border-radius:999px;background:{MINT};box-shadow:0 0 8px {MINT}}}
/* floating tracking panel */
.rn-panel{{position:absolute;left:12px;right:12px;bottom:22px;z-index:6;background:var(--card);border:1px solid var(--border);
  border-radius:28px;padding:22px 20px 20px;text-align:center;box-shadow:0 -8px 40px rgba(0,0,0,.4)}}
.rn-time{{font-size:62px;font-weight:900;letter-spacing:-.04em;line-height:1;font-variant-numeric:tabular-nums}}
.rn-time-l{{font-size:12px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:.1em;margin-top:4px}}
.rn-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:18px 0}}
.rn-stat{{display:flex;flex-direction:column;align-items:center;gap:2px;padding:12px 0;border-radius:16px;background:var(--input-bg);border:1px solid var(--input-border)}}
.rn-stat-n{{font-size:19px;font-weight:800;letter-spacing:-.02em;font-variant-numeric:tabular-nums}}
.rn-stat-l{{font-size:10px;font-weight:700;color:var(--sub);text-transform:uppercase;letter-spacing:.06em}}
.rn-ctrls{{display:flex;gap:12px;justify-content:center}}
.rn-pause,.rn-stop,.rn-resume{{height:58px;border:none;border-radius:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px;font-family:inherit;font-size:16px;font-weight:800;color:#fff}}
.rn-pause{{flex:1;background:linear-gradient(135deg,{GRAD_A},{GRAD_B})}}
.rn-resume{{flex:1;background:linear-gradient(135deg,{GRAD_A},{GRAD_B})}}
.rn-stop{{width:58px;background:#FF4658}}
.rn-pause-badge{{position:absolute;top:64px;left:16px;right:16px;z-index:6;display:flex;align-items:center;gap:7px;justify-content:center;
  padding:9px;border-radius:14px;background:rgba(255,166,61,.92);color:#fff;font-size:12.5px;font-weight:700}}
/* countdown */
.rn-cd{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:6}}
.rn-cd-num{{font-size:160px;font-weight:900;color:#fff;line-height:1;text-shadow:0 8px 40px rgba(51,160,137,.6)}}
.rn-cd-go{{font-size:18px;font-weight:700;color:rgba(255,255,255,.85);margin-top:8px}}
/* start screen — gros bouton Départ */
.rn-start-top{{position:absolute;top:70px;left:0;right:0;z-index:6;text-align:center}}
.rn-start-h{{font-size:24px;font-weight:900;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.5);margin-bottom:14px}}
.rn-goals{{display:inline-flex;gap:7px;padding:5px;border-radius:999px;background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}}
.rn-goal{{padding:8px 16px;border:none;border-radius:999px;background:transparent;color:rgba(255,255,255,.7);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer}}
.rn-goal-on{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff}}
.rn-start-center{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:6}}
.rn-go{{position:relative;width:188px;height:188px;border-radius:999px;border:none;cursor:pointer;
  background:linear-gradient(135deg,{GRAD_A},{GRAD_B});display:flex;flex-direction:column;align-items:center;justify-content:center;
  box-shadow:0 0 0 10px rgba(51,160,137,.18),0 20px 50px rgba(51,160,137,.5);animation:rngo 2s ease-in-out infinite}}
.rn-go-ring{{position:absolute;inset:-10px;border-radius:999px;border:2px solid rgba(51,160,137,.5);animation:rngoring 2s ease-out infinite}}
.rn-go-lbl{{color:#fff;font-size:18px;font-weight:900;letter-spacing:.08em;margin-top:2px}}
.rn-go-hint{{color:rgba(255,255,255,.8);font-size:13px;font-weight:600;margin-top:22px;text-shadow:0 2px 8px rgba(0,0,0,.5)}}
@keyframes rngo{{50%{{box-shadow:0 0 0 16px rgba(51,160,137,.10),0 20px 60px rgba(51,160,137,.6)}}}}
@keyframes rngoring{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(1.25);opacity:0}}}}
.rn-start-opts{{position:absolute;bottom:36px;left:0;right:0;z-index:6;display:flex;gap:10px;justify-content:center}}
.rn-opt{{display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);color:rgba(255,255,255,.7);font-size:12px;font-weight:700}}
.rn-opt-on{{color:{MINT}}}
/* gps search */
.rn-search{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 40px;z-index:6}}
.rn-search-pulse{{width:88px;height:88px;border-radius:999px;background:rgba(51,160,137,.15);border:2px solid rgba(51,160,137,.4);display:flex;align-items:center;justify-content:center;margin-bottom:18px;animation:rnpulse 1.4s ease-in-out infinite}}
@keyframes rnpulse{{50%{{transform:scale(1.12);opacity:.7}}}}
.rn-search h3{{color:#fff;font-size:17px;font-weight:800}}.rn-search p{{color:rgba(255,255,255,.7);font-size:13px;margin-top:6px}}
/* stop confirm sheet */
.rn-sheet{{position:absolute;left:0;right:0;bottom:0;z-index:8;background:var(--page);border-radius:28px 28px 0 0;padding:10px 22px 30px;text-align:center;box-shadow:0 -10px 40px rgba(0,0,0,.5)}}
.rn-sheet-h{{width:40px;height:4px;border-radius:999px;background:var(--input-border);margin:0 auto 18px}}
.rn-sheet-t{{font-size:19px;font-weight:800;margin-bottom:12px}}
.rn-sheet-stats{{display:flex;justify-content:center;gap:20px;margin-bottom:20px;font-size:15px;color:var(--sub)}}
.rn-sheet-stats b{{color:var(--text);font-weight:800}}
/* generic pad/center screens */
.rn-pad{{padding:64px 28px 36px;min-height:852px}}
.rn-center{{display:flex;flex-direction:column;align-items:center;text-align:center}}
.rn-hero-ic{{width:84px;height:84px;border-radius:26px;background:linear-gradient(135deg,{GRAD_A},{GRAD_B});display:flex;align-items:center;justify-content:center;margin-bottom:22px;box-shadow:0 12px 32px rgba(51,160,137,.4)}}
.rn-h1{{font-size:25px;font-weight:900;letter-spacing:-.02em}}
.rn-sub{{font-size:14px;font-weight:500;color:var(--sub);line-height:1.55;margin-top:10px;max-width:300px}}
.rn-bullets{{display:flex;flex-direction:column;gap:14px;margin:30px 0;width:100%}}
.rn-bul{{display:flex;gap:13px;text-align:left;align-items:flex-start}}
.rn-bul h4{{font-size:14px;font-weight:800}}.rn-bul p{{font-size:12.5px;color:var(--sub);margin-top:2px;line-height:1.45}}
.rn-warn{{display:flex;align-items:center;gap:8px;padding:12px 14px;border-radius:14px;background:rgba(255,166,61,.12);border:1px solid rgba(255,166,61,.3);color:var(--text);font-size:12.5px;font-weight:600;margin:24px 0}}
.rn-actions{{margin-top:auto;width:100%;display:flex;flex-direction:column;gap:10px}}
.rn-primary{{width:100%;height:54px;border:none;border-radius:16px;background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:15px;font-weight:800;cursor:pointer;box-shadow:0 8px 22px rgba(51,160,137,.35)}}
.rn-ghost{{width:100%;height:48px;border:none;background:transparent;color:var(--sub);font-family:inherit;font-size:14px;font-weight:700;cursor:pointer}}
/* share */
.rn-share{{display:flex;flex-direction:column;height:852px}}
.rn-shead{{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;font-size:16px;font-weight:800;border-bottom:1px solid var(--border)}}
.rn-scroll{{flex:1;overflow-y:auto;padding:16px}}
.rn-scroll::-webkit-scrollbar{{display:none}}
.rn-pr{{display:flex;align-items:center;gap:12px;padding:14px;border-radius:18px;background:linear-gradient(135deg,rgba(65,173,150,.18),rgba(44,149,160,.10));border:1px solid rgba(51,160,137,.35);margin-bottom:16px}}
.rn-pr-em{{font-size:26px}}.rn-pr b{{font-size:14px;font-weight:800;display:block}}.rn-pr span{{font-size:11.5px;color:var(--sub)}}
.rn-hero{{position:relative;height:200px;border-radius:20px;overflow:hidden;margin-bottom:16px}}
.rn-hero .rn-map{{position:absolute;inset:0}}
.rn-hero-ov{{position:absolute;bottom:0;left:0;right:0;display:flex;justify-content:space-around;padding:14px;background:linear-gradient(transparent,rgba(0,0,0,.7));color:#fff}}
.rn-hero-ov b{{font-size:18px;font-weight:900}}.rn-hero-ov span{{font-size:11px;opacity:.85;display:flex;flex-direction:column;align-items:center}}
.rn-field{{margin-bottom:16px}}.rn-field>label{{font-size:11px;font-weight:800;color:var(--sub);text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:8px}}
.rn-input{{padding:13px 14px;border-radius:14px;background:var(--input-bg);border:1px solid var(--input-border);font-size:13.5px;font-weight:500;display:flex;align-items:center;justify-content:space-between;gap:8px}}
.rn-ta{{min-height:64px;align-items:flex-start;color:var(--sub)}}
.rn-privs{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}
.rn-priv{{display:flex;align-items:center;justify-content:center;gap:5px;padding:11px 0;border-radius:12px;border:1px solid var(--input-border);background:var(--input-bg);color:var(--sub);font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer}}
.rn-priv-on{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;border-color:transparent}}
.rn-tog{{display:flex;align-items:center;gap:12px;padding:14px;border-radius:16px;background:var(--card);border:1.5px solid var(--border);margin-bottom:9px;cursor:pointer}}
.rn-tog-on{{border-color:rgba(51,160,137,.55);background:linear-gradient(135deg,rgba(51,160,137,.08),rgba(44,149,160,.04))}}
.rn-tog-ic{{width:40px;height:40px;border-radius:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.rn-tog-t{{flex:1;min-width:0}}.rn-tog-t h4{{font-size:14px;font-weight:800}}.rn-tog-t p{{font-size:12px;color:var(--sub);margin-top:2px;line-height:1.35}}
.rn-check{{width:26px;height:26px;border-radius:999px;border:2px solid var(--input-border);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s}}
.rn-check-on{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});border-color:transparent}}
.rn-share-cta{{padding:14px 16px;border-top:1px solid var(--border)}}
.rn-share-row{{display:flex;gap:10px;margin-top:6px}}.rn-share-row .rn-ghost{{flex:1}}
/* history / records */
.rn-hh{{display:flex;align-items:center;justify-content:space-between;padding:16px;font-size:18px;font-weight:900}}
.rn-back{{width:34px;height:34px;border:none;background:transparent;cursor:pointer;display:flex;align-items:center;justify-content:center}}
.rn-tabs{{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin:0 16px 16px;padding:4px;border-radius:999px;background:var(--input-bg);border:1px solid var(--input-border)}}
.rn-tab{{padding:9px 0;border:none;border-radius:999px;background:transparent;color:var(--sub);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer}}
.rn-tab-on{{background:var(--card);color:var(--mint);box-shadow:0 0 16px rgba(51,160,137,.3),0 0 0 1px rgba(51,160,137,.4)}}
.rn-ringwrap{{display:flex;align-items:center;gap:18px;padding:6px 22px 24px}}
.rn-ring-side{{flex:1;display:flex;flex-direction:column;gap:12px}}
.rn-ring-stat b{{font-size:22px;font-weight:900;letter-spacing:-.02em}}.rn-ring-stat span{{font-size:11px;color:var(--sub);font-weight:600;margin-left:5px}}
.rn-list{{padding:0 16px 100px;display:flex;flex-direction:column;gap:10px}}
.rn-li{{display:flex;align-items:center;gap:12px;padding:10px;border-radius:18px;background:var(--card);border:1px solid var(--border)}}
.rn-li-map{{width:64px;height:64px;border-radius:14px;overflow:hidden;flex-shrink:0}}
.rn-li-t{{flex:1;min-width:0}}.rn-li-top{{display:flex;align-items:center;gap:8px}}.rn-li-top h4{{font-size:16px;font-weight:900}}
.rn-li-pr{{font-size:9px;font-weight:800;color:var(--mint);background:rgba(51,160,137,.14);padding:2px 7px;border-radius:999px}}
.rn-li-t p{{font-size:11.5px;color:var(--sub);margin:2px 0 5px}}
.rn-li-meta{{display:flex;gap:12px}}.rn-li-meta span{{display:flex;align-items:center;gap:4px;font-size:11.5px;font-weight:600;color:var(--text)}}
.rn-recs{{padding:0 16px 100px;display:flex;flex-direction:column;gap:10px}}
.rn-rec{{display:flex;align-items:center;gap:12px;padding:14px;border-radius:16px;background:var(--card);border:1px solid var(--border)}}
.rn-rec-ic{{width:42px;height:42px;border-radius:13px;display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.rn-rec-t{{flex:1}}.rn-rec-t h4{{font-size:14px;font-weight:800}}.rn-rec-t p{{font-size:11.5px;color:var(--sub);margin-top:2px}}
.rn-rec-v{{font-size:19px;font-weight:900;color:var(--mint);letter-spacing:-.02em;font-variant-numeric:tabular-nums}}
/* detail */
.rn-dstats{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:16px 0}}
.rn-sec{{font-size:15px;font-weight:800;margin:6px 0 12px}}
.rn-splits{{display:flex;flex-direction:column;gap:9px;margin-bottom:20px}}
.rn-split{{display:flex;align-items:center;gap:10px}}
.rn-split-k{{width:18px;font-size:13px;font-weight:800;color:var(--sub);text-align:center}}
.rn-split-bar{{flex:1;height:22px;border-radius:8px;background:var(--input-bg);overflow:hidden}}
.rn-split-fill{{height:100%;border-radius:8px;background:linear-gradient(90deg,{GRAD_A},{GRAD_B})}}
.rn-split-p{{font-size:13px;font-weight:800;width:48px;text-align:right;font-variant-numeric:tabular-nums}}
.rn-split-e{{font-size:11px;color:var(--sub);width:32px;text-align:right}}
.rn-dcta{{padding-bottom:30px}}
/* empty */
.rn-empty{{display:flex;flex-direction:column;align-items:center;text-align:center;padding:70px 36px}}
.rn-empty-ic{{width:96px;height:96px;border-radius:999px;background:var(--input-bg);display:flex;align-items:center;justify-content:center;margin-bottom:20px}}
.rn-empty h3{{font-size:18px;font-weight:800}}.rn-empty p{{font-size:13.5px;color:var(--sub);line-height:1.55;margin:8px 0 24px;max-width:280px}}
/* published recap + discard modal */
.rn-pub-recap{{display:flex;flex-direction:column;gap:9px;width:100%;margin-bottom:8px}}
.rn-pub-chip{{display:flex;align-items:center;gap:9px;padding:13px 16px;border-radius:14px;background:var(--card);border:1px solid var(--border);font-size:13.5px;font-weight:700}}
.rn-disc-ic{{width:64px;height:64px;border-radius:999px;background:rgba(255,70,88,.12);display:flex;align-items:center;justify-content:center;margin:0 auto 14px}}
.rn-disc-p{{font-size:13.5px;color:var(--sub);line-height:1.55;margin-bottom:20px;max-width:300px;margin-left:auto;margin-right:auto}}
.rn-disc-p b{{color:var(--text)}}
.rn-danger{{width:100%;height:52px;border:none;border-radius:16px;background:#FF4658;color:#fff;font-family:inherit;font-size:15px;font-weight:800;cursor:pointer;box-shadow:0 8px 22px rgba(255,70,88,.35);margin-bottom:6px}}
{bnav_css}
"""


def page(title, body, dark):
    t = theme(dark)
    bnav_css = CANONICAL_BNAV_CSS.strip().removeprefix('<style>').removesuffix('</style>')
    css = CSS.format(MINT=MINT, GRAD_A=GRAD_A, GRAD_B=GRAD_B, bnav_css=bnav_css, **t)
    return f'''<!DOCTYPE html><html lang="fr" class="{t['html']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=393, initial-scale=1"><title>Smuppy V2 — Run {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<style>{css}</style></head><body><div class="device">{body}</div></body></html>'''


SCREENS = {
    'run_permission_v2': ('Permission', lambda t, d: s_permission(t)),
    'run_gps_denied_v2': ('GPS denied', lambda t, d: s_gps_denied(t)),
    'run_start_v2': ('Start · Départ', lambda t, d: s_start(t)),
    'run_countdown_v2': ('Countdown', lambda t, d: s_countdown(t)),
    'run_tracking_v2': ('Tracking', lambda t, d: s_tracking(t)),
    'run_paused_v2': ('Paused', lambda t, d: s_paused(t)),
    'run_gps_search_v2': ('GPS search', lambda t, d: s_gps_search(t)),
    'run_stop_confirm_v2': ('Stop confirm', lambda t, d: s_stop_confirm(t)),
    'run_share_v2': ('Share', lambda t, d: s_share(t)),
    'run_published_v2': ('Published', lambda t, d: s_published(t)),
    'run_discard_confirm_v2': ('Discard', lambda t, d: s_discard(t)),
    'run_history_v2': ('Mes runs', lambda t, d: s_history(t, d)),
    'run_records_v2': ('Records', lambda t, d: s_records(t, d)),
    'run_detail_v2': ('Detail', lambda t, d: s_detail(t)),
    'run_empty_v2': ('Empty', lambda t, d: s_empty(t, d)),
}


def main():
    n = 0
    for key, (title, fn) in SCREENS.items():
        for dark in (True, False):
            th = 'dark' if dark else 'light'
            d = OUT / f'{key}_{th}'
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(page(title, fn(theme(dark), dark), dark), encoding='utf-8')
            n += 1
    print(f'wrote {n} run screens ({len(SCREENS)} x2) to {OUT}')


if __name__ == '__main__':
    main()
