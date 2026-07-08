#!/usr/bin/env python3
"""Smuppy V2 — Feed/Discover screens v5 (founder jun03 screenshots + DS V2).
  - vibes_feed   : home tab "Vibes" — masonry polymorphe (photo/vidéo/activité/événement/citation/communauté)
  - search       : Discover — search bar + Trending + Live now + Suggested creators + Places near you
  - xplorer_map  : home tab "Xplorer" — carte plein écran + pins + live near you
  - peaks_live   : écran séparé (bnav Peaks) — 2 tabs haut Peaks / Live, vue immersive reels
393×852 device. Self-contained — imports canonical_bnav. Pure stdlib, deterministic.
"""
import sys
from pathlib import Path

sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from canonical_bnav import canonical_bnav, CANONICAL_BNAV_CSS  # noqa: E402
from build_auth_v2 import smuppy_text  # noqa: E402  — canonical wordmark (vert dark / noir light)

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
MINT = '#33A089'  # softer (was #33A089)
GRAD_A, GRAD_B = '#41AD96', '#2C95A0'  # softer (was #41AD96/#2C95A0)
IMG = "https://images.unsplash.com/photo-"
PH = {
    'run': '1571019614242-c5c5dee9f50b', 'yoga': '1545205597-3d9d02c29597',
    'forest': '1441974231531-c6227db76b6e', 'hike': '1551632811-561732d1e306',
    'bowl': '1512621776951-a57141f2eefd', 'gym': '1517836357463-d25dfeac3438',
    'window': '1518611012118-696072aa579a', 'trail': '1506126613408-eca07ce68773',
    'a1': '1494790108377-be9c29b29330', 'a2': '1500648767791-00dcc994a43e',
    'a3': '1438761681033-6461ffad8d80', 'a4': '1535713875002-d1d0cf377fde',
    'cafe': '1554118811-1e0d58224f24', 'studio': '1571902943202-507ec2618e8f',
}


def theme(dark):
    if dark:
        return dict(page='#000000', card='#14141A', text='#F1F4F6', sub='#8B8B95',
                    border='rgba(255,255,255,0.06)', input_bg='rgba(255,255,255,0.04)',
                    input_border='rgba(255,255,255,0.10)', dim='0.5', html='dark')
    return dict(page='#F6F8FA', card='#FFFFFF', text='#0F172A', sub='#64748B',
                border='#EEF1F4', input_bg='#FFFFFF', input_border='#E5E9EB',
                dim='0.06', html='light')


def img(key, w=400, h=400):
    return f'{IMG}{PH[key]}?w={w}&h={h}&fit=crop&q=80'


def topbar(active='vibes', dark=True):
    """Home top bar (canonical jun03) : notif LEFT · Smuppy wordmark CENTER (vert dark/noir light) · search RIGHT."""
    tabs = ''
    for key, label in [('fan', 'Fan'), ('vibes', 'Vibes'), ('xplorer', 'Xplorer')]:
        on = ' ft-tab-on' if key == active else ''
        tabs += f'<button class="ft-tab{on}">{label}</button>'
    wordmark = smuppy_text(94, 'gradient' if dark else 'dark')
    return f'''<header class="ft-top">
  <button class="ft-ic ft-ic-l" aria-label="Notifications"><ion-icon name="notifications-outline" style="font-size:22px"></ion-icon><span class="ft-badge">3</span></button>
  <div class="ft-brand">{wordmark}</div>
  <button class="ft-ic ft-ic-r" aria-label="Recherche"><ion-icon name="search-outline" style="font-size:22px"></ion-icon></button>
</header>
<nav class="ft-tabs">{tabs}</nav>'''


# ─────────────────────────── VIBES (masonry polymorphe) ───────────────────────────
def vibes_cards():
    def photo(im, cap, user):
        return (f'<div class="vc"><img loading="lazy" src="{img(im,500,650)}" alt=""/>'
                f'<div class="vc-cap">{cap}</div><div class="vc-user">'
                f'<img src="{img("a1",40,40)}"/>@{user}</div></div>')

    def video(im, cap, user):
        return (f'<div class="vc"><div class="vc-vid"><img loading="lazy" src="{img(im,500,640)}" alt=""/>'
                f'<span class="vc-play"><ion-icon name="play" style="font-size:20px;color:#fff"></ion-icon></span></div>'
                f'<div class="vc-cap">{cap}</div><div class="vc-user"><img src="{img("a3",40,40)}"/>@{user}</div></div>')

    def quote(txt):
        return (f'<div class="vc vc-quote"><ion-icon name="chatbox-ellipses" style="font-size:22px;color:#fff;opacity:.85"></ion-icon>'
                f'<p>{txt}</p></div>')

    def activity(title, loc):
        return (f'<div class="vc vc-soft"><div class="vc-badge" style="background:rgba(51,160,137,0.16);color:{MINT}">'
                f'<ion-icon name="fitness" style="font-size:13px"></ion-icon>Activité</div>'
                f'<h4>{title}</h4><p class="vc-meta"><ion-icon name="location-outline" style="font-size:12px"></ion-icon>{loc}</p>'
                f'<button class="vc-cta">Rejoindre</button></div>')

    def event(title, when):
        return (f'<div class="vc vc-soft"><div class="vc-badge" style="background:rgba(255,166,61,.16);color:#FFA63D">'
                f'<ion-icon name="calendar" style="font-size:13px"></ion-icon>Événement</div>'
                f'<h4>{title}</h4><p class="vc-meta"><ion-icon name="time-outline" style="font-size:12px"></ion-icon>{when}</p>'
                f'<button class="vc-cta vc-cta-ghost">Je participe</button></div>')

    def community(title, sub):
        return (f'<div class="vc vc-soft"><div class="vc-badge" style="background:rgba(139,92,246,.16);color:#9966FF">'
                f'<ion-icon name="people" style="font-size:13px"></ion-icon>Communauté</div>'
                f'<h4>{title}</h4><p class="vc-meta">{sub}</p></div>')

    # interleaved into 2 masonry columns
    col_a = [photo('yoga', 'Chasing the golden hour glow', 'alex_vibes'),
             quote('Connection is the energy that exists between people when they feel seen, heard, and valued.'),
             video('hike', 'Weekend trail therapy', 'mia_w'),
             community('New meetup spot just dropped', 'Parc La Fontaine · 18h')]
    col_b = [activity('Sunset Yoga Session', 'Central Park, NY'),
             photo('window', 'Slow mornings, big dreams', 'sara_k'),
             event("Who's down for a weekend hike?", 'Sam 7 juin · 09h'),
             photo('bowl', 'Fuel that feels good', 'jordan_eats')]
    return (f'<div class="vc-col">{"".join(col_a)}</div>'
            f'<div class="vc-col">{"".join(col_b)}</div>')


def screen_vibes(dark):
    return topbar('vibes', dark) + f'<section class="vc-masonry">{vibes_cards()}</section>' + canonical_bnav('home', dark=dark)


# ─────────────────────────── SEARCH / DISCOVER ───────────────────────────
def screen_search(dark):
    pills = ''.join(f'<button class="sr-pill">{h}</button>'
                    for h in ['#yogaflow', '#padel', '#mindfulness', '#trailrun', '#healthyeats'])
    lives = ''.join(
        f'<div class="sr-live"><img src="{img(a,200,260)}"/><span class="sr-live-dot">LIVE</span>'
        f'<span class="sr-live-name">{n}</span></div>'
        for a, n in [('a1', 'Maya'), ('a2', 'Sara'), ('a4', 'Léa')])
    creators = ''.join(
        f'<div class="sr-cr"><img src="{img(a,80,80)}"/><div class="sr-cr-n">{n}</div>'
        f'<div class="sr-cr-r">{r}</div><button class="sr-cr-follow">Devenir fan</button></div>'
        for a, n, r in [('a1', 'Alex Rossi', 'Digital Art'), ('a3', 'Marc Bloom', 'Urban Gardening'),
                        ('a2', 'Luna Chen', 'Yoga & Mind'), ('a4', 'Elsa Thorne', 'Slow Living')])
    places = ''.join(
        f'<div class="sr-place"><img src="{img(im,120,120)}"/><div class="sr-place-t"><h4>{n}</h4>'
        f'<p>{d} · {tag}</p><span class="sr-place-map"><ion-icon name="location" style="font-size:12px"></ion-icon>Voir sur la carte</span></div></div>'
        for im, n, d, tag in [('studio', 'Studio Verde', '0.8 km', 'Yoga & Pilates'),
                              ('cafe', 'Café Recover', '1.2 km', 'Healthy Eats')])
    return f'''<header class="ft-top">
  <button class="ft-ic ft-ic-l" aria-label="Retour"><ion-icon name="chevron-back" style="font-size:24px"></ion-icon></button>
  <div class="ft-brand">{smuppy_text(94, 'gradient' if dark else 'dark')}</div>
  <span style="width:40px"></span>
</header>
<div class="sr-bar"><ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
  <span>Chercher créateurs, hashtags, lieux</span></div>
<section class="sr-sec"><h3 class="sr-h">Trending now</h3><div class="sr-pills">{pills}</div></section>
<section class="sr-sec"><h3 class="sr-h">Live now</h3><div class="sr-lives">{lives}</div></section>
<section class="sr-sec"><h3 class="sr-h">Suggested creators</h3><div class="sr-crs">{creators}</div></section>
<section class="sr-sec"><h3 class="sr-h">Places near you</h3><div class="sr-places">{places}</div></section>
{canonical_bnav('home', dark=dark)}'''


# ─────────────────────────── XPLORER (map) ───────────────────────────
def screen_xplorer(dark):
    """Xplorer map (founder jun03) : intègre BUSINESS / ÉVÉNEMENTS / ACTIVITÉS / SPOTS (pas des gens).
    Filtre clean par type. Pins = marqueurs de lieu (icône + couleur), pas des avatars."""
    tile = 'dark' if dark else 'light'
    # Type-based filter — clean, simple, modern (replaces coach professions)
    cats = [('Tous', 'apps-outline'), ('Business', 'business-outline'), ('Événements', 'calendar-outline'),
            ('Activités', 'fitness-outline'), ('Spots', 'location-outline')]
    fchips = ''.join(
        f'<button class="xp-fchip{" xp-fchip-on" if i == 0 else ""}">'
        f'<ion-icon name="{ic}" style="font-size:13px;vertical-align:middle;margin-right:4px"></ion-icon>{c}</button>'
        for i, (c, ic) in enumerate(cats))
    # location markers : (icon, color, x%, y%)
    pins = ''.join(
        f'<span class="xp-marker" style="top:{y}%;left:{x}%;--mc:{col}">'
        f'<ion-icon name="{ic}" style="font-size:15px;color:#fff"></ion-icon></span>'
        for ic, col, x, y in [('business', '#33A089', 30, 30), ('calendar', '#9966FF', 62, 22),
                              ('fitness', '#11C6FF', 48, 50), ('location', '#FFA63D', 72, 58),
                              ('business', '#33A089', 22, 62)])
    items = [('studio', '#33A089', 'business', 'Vibe Fitness Studio', 'Business', '0.4 km', '12 rue de Rivoli'),
             ('yoga', '#9966FF', 'calendar', 'Yoga sunrise · Parc', 'Événement', '1.1 km', 'Sam 7 juin · 7h'),
             ('run', '#11C6FF', 'fitness', 'Run club du matin', 'Activité', '0.7 km', 'Tous les jours · 6h30'),
             ('trail', '#FFA63D', 'location', 'Spot street workout', 'Spot', '1.3 km', 'Parc La Fontaine')]
    cards = ''.join(
        f'<div class="xp-card"><img src="{img(a,120,120)}"/>'
        f'<div class="xp-card-t"><span class="xp-badge" style="background:{col}1A;color:{col}">'
        f'<ion-icon name="{ic}" style="font-size:11px"></ion-icon>{badge}</span>'
        f'<h4>{n}</h4><p><ion-icon name="location-outline" style="font-size:12px"></ion-icon>{d} · {sub}</p></div></div>'
        for a, col, ic, n, badge, d, sub in items)
    return topbar('xplorer', dark) + f'''<section class="xp-map xp-map-{tile}">
  <div class="xp-grid-lines"></div>
  <div class="xp-searchbar"><ion-icon name="search-outline" style="font-size:18px;color:var(--sub)"></ion-icon>
    <span>Chercher un lieu, un spot, un événement…</span>
    <button class="xp-filter-btn"><ion-icon name="options-outline" style="font-size:18px;color:{MINT}"></ion-icon></button>
  </div>
  <nav class="xp-fchips">{fchips}</nav>
  {pins}
  <button class="xp-recenter"><ion-icon name="locate" style="font-size:20px;color:{MINT}"></ion-icon></button>
</section>
<section class="xp-sheet">
  <div class="xp-handle"></div>
  <h3 class="xp-h">Près de toi</h3>
  <div class="xp-cards">{cards}</div>
</section>
{canonical_bnav('home', dark=dark)}'''


# ─────────────────────────── PEAKS / LIVE feed (founder jun03 screenshots) ───────────────────────────
def screen_peaks_live(dark, active='peaks'):
    """Écran séparé (bnav Peaks). Back + tabs Peaks/Live (underline) + chips filtre +
    grille 2-col (Peaks) / empty state (Live). PAS immersif."""
    tabs = ''.join(
        f'<button class="pl-tab{" pl-tab-on" if k == active else ""}">{l}</button>'
        for k, l in [('peaks', 'Peaks'), ('live', 'Live')])
    chip_set = (['Tous', 'Challenge', 'Following', 'Trending'] if active == 'peaks'
                else ['Tous', 'Sport', 'Bien-être', 'Musique', 'Combat'])
    chips = ''.join(
        f'<button class="pl-chip{" pl-chip-on" if i == 0 else ""}">{c}</button>'
        for i, c in enumerate(chip_set))

    if active == 'peaks':
        cards = ''.join(
            f'<div class="pl-card"><img loading="lazy" src="{img(im,400,560)}" alt=""/>'
            f'<div class="pl-card-scrim"></div><span class="pl-card-name">{nm}</span>'
            f'<span class="pl-card-play"><ion-icon name="play" style="font-size:14px;color:#fff"></ion-icon>{views}</span></div>'
            for im, nm, views in [('gym', 'Hamza15up Djebiri', '12k'), ('hike', 'Coach Nou', '8.4k'),
                                  ('run', 'Sara K.', '21k'), ('yoga', 'Mia W.', '5.1k'),
                                  ('trail', 'Marc D.', '9.7k'), ('bowl', 'Léa P.', '3.2k')])
        content = f'<section class="pl-grid">{cards}</section>'
    else:
        # Live tab = grille de cards de lives EN COURS (clic → preview 5s → paywall chaîne)
        lives = ''.join(
            f'<a class="pl-card pl-card-live" href="../live_preview_v2_{"dark" if dark else "light"}/code.html">'
            f'<img loading="lazy" src="{img(im,400,560)}" alt=""/><div class="pl-card-scrim"></div>'
            f'<span class="pl-livebadge"><span class="pl-livedot"></span>LIVE</span>'
            f'<span class="pl-card-play"><ion-icon name="eye" style="font-size:13px;color:#fff"></ion-icon>{v}</span>'
            f'<span class="pl-card-name">{nm}</span></a>'
            for im, nm, v in [('yoga', 'Sara K. · Yoga flow', '342'), ('gym', 'Coach Mike · HIIT', '1.2k'),
                              ('run', 'Marc D. · Run club', '88'), ('bowl', 'Léa · Nutrition Q&A', '215')])
        content = f'<section class="pl-grid">{lives}</section>'

    return f'''<header class="pl-top">
  <button class="pl-back" aria-label="Retour"><ion-icon name="chevron-back" style="font-size:24px;color:var(--text)"></ion-icon></button>
  <nav class="pl-tabs">{tabs}</nav>
  <span style="width:34px"></span>
</header>
<nav class="pl-chips">{chips}</nav>
{content}
{canonical_bnav('peaks', dark=dark)}'''


# ─────────────────────────── LIVE preview → paywall (flow) ───────────────────────────
def screen_live_preview(dark):
    """Clic sur un live → aperçu gratuit 5s → paywall abonnement chaîne (founder jun03).
    État capturé : aperçu en cours (badge 0:05) + sheet paywall qui monte pour continuer."""
    return f'''<section class="lp-stage">
  <img class="lp-media" src="{img("yoga",800,1400)}" alt=""/>
  <div class="lp-scrim"></div>
  <button class="lp-close" aria-label="Fermer"><ion-icon name="close" style="font-size:24px;color:#fff"></ion-icon></button>
  <div class="lp-livebadge"><span class="pl-livedot"></span>LIVE · 342</div>
  <div class="lp-preview-tag"><ion-icon name="time-outline" style="font-size:14px"></ion-icon> Aperçu gratuit · 0:05</div>
  <div class="lp-creator"><img src="{img("a1",60,60)}"/><div><span class="lp-name">Sara K.</span><span class="lp-cap">Yoga flow du matin 🌅</span></div></div>
  <!-- paywall sheet (apparaît après l'aperçu 5s) -->
  <div class="lp-paywall">
    <div class="lp-pw-handle"></div>
    <div class="lp-pw-lock"><ion-icon name="lock-closed" style="font-size:22px;color:{MINT}"></ion-icon></div>
    <h3 class="lp-pw-title">Aperçu terminé</h3>
    <p class="lp-pw-sub">Abonne-toi à la chaîne de Sara pour continuer ce live + tous ses lives & replays.</p>
    <a class="lp-pw-cta" href="../creator_channel_view_v2_{"dark" if dark else "light"}/code.html">S'abonner · $9.99/mois</a>
    <button class="lp-pw-ghost">Plus tard</button>
  </div>
</section>
{canonical_bnav('peaks', dark=dark)}'''


# ─────────────────────────── shell ───────────────────────────
def page(title, body, dark):
    t = theme(dark)
    bnav_css = CANONICAL_BNAV_CSS.strip().removeprefix('<style>').removesuffix('</style>')
    return f'''<!DOCTYPE html><html lang="fr" class="{t['html']}"><head><meta charset="utf-8">
<meta name="viewport" content="width=393, initial-scale=1"><title>Smuppy V2 — {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{height:100%}}
body{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;background:var(--page);color:var(--text);-webkit-font-smoothing:antialiased}}
:root{{--page:{t['page']};--card:{t['card']};--text:{t['text']};--sub:{t['sub']};--mint:{MINT};
  --border:{t['border']};--input-bg:{t['input_bg']};--input-border:{t['input_border']}}}
.device{{position:relative;width:393px;height:852px;overflow-y:auto;overflow-x:hidden;background:var(--page)}}
.device::-webkit-scrollbar{{display:none}}
/* top bar (canonical) : notif LEFT · Smuppy CENTER · search RIGHT */
.ft-top{{display:grid;grid-template-columns:42px 1fr 42px;align-items:center;padding:14px 16px 10px}}
.ft-brand{{display:flex;align-items:center;justify-content:center}}
.smuppy-full{{display:inline-flex;align-items:center;gap:7px}}
.smuppy-full svg{{display:block}}
.ft-ic{{position:relative;width:40px;height:40px;border:none;background:transparent;color:var(--text);cursor:pointer;
  display:flex;align-items:center;justify-content:center}}
.ft-ic-r{{justify-self:end}}
.ft-badge{{position:absolute;top:4px;right:4px;min-width:15px;height:15px;padding:0 3px;border-radius:999px;
  background:#FF4658;color:#fff;font-size:9px;font-weight:800;display:flex;align-items:center;justify-content:center}}
.ft-tabs{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;padding:2px 16px 12px}}
.ft-tab{{padding:8px 0;border:none;border-radius:999px;background:var(--input-bg);color:var(--sub);
  font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;border:1px solid transparent}}
.ft-tab-on{{background:var(--card);color:var(--mint);border:1px solid rgba(51,160,137,0.225);
  box-shadow:0 0 16px rgba(51,160,137,0.15)}}
/* VIBES masonry */
.vc-masonry{{display:flex;gap:10px;padding:0 14px 100px;align-items:flex-start}}
.vc-col{{flex:1;display:flex;flex-direction:column;gap:10px}}
.vc{{position:relative;border-radius:20px;overflow:hidden;background:var(--card);border:1px solid var(--border);
  box-shadow:0 4px 18px rgba(0,0,0,{t['dim']})}}
.vc>img{{width:100%;display:block;object-fit:cover}}
.vc-cap{{padding:9px 11px 4px;font-size:12.5px;font-weight:600;color:var(--text);line-height:1.35}}
.vc-user{{display:flex;align-items:center;gap:6px;padding:0 11px 10px;font-size:11px;font-weight:600;color:var(--sub)}}
.vc-user img{{width:18px;height:18px;border-radius:999px;object-fit:cover}}
.vc-vid{{position:relative}}.vc-vid img{{width:100%;display:block}}
.vc-play{{position:absolute;inset:0;margin:auto;width:46px;height:46px;border-radius:999px;
  background:rgba(0,0,0,.45);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);
  display:flex;align-items:center;justify-content:center}}
.vc-quote{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});padding:18px 16px;border:none}}
.vc-quote p{{margin-top:10px;font-size:15px;font-weight:800;color:#04201B;line-height:1.4}}
.vc-soft{{padding:14px 13px}}
.vc-badge{{display:inline-flex;align-items:center;gap:5px;padding:4px 9px;border-radius:999px;
  font-size:10px;font-weight:800;letter-spacing:.02em;margin-bottom:9px}}
.vc-soft h4{{font-size:14px;font-weight:800;color:var(--text);line-height:1.3;margin-bottom:6px}}
.vc-meta{{display:flex;align-items:center;gap:4px;font-size:11.5px;font-weight:600;color:var(--sub)}}
.vc-cta{{margin-top:11px;width:100%;height:34px;border:none;border-radius:11px;
  background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer}}
.vc-cta-ghost{{background:var(--input-bg);color:var(--mint);border:1px solid rgba(51,160,137,0.2)}}
/* SEARCH */
.sr-bar{{display:flex;align-items:center;gap:9px;margin:4px 16px 16px;padding:12px 14px;border-radius:14px;
  background:var(--input-bg);border:1px solid var(--input-border);font-size:13px;color:var(--sub);font-weight:500}}
.sr-sec{{padding:0 16px;margin-bottom:22px}}
.sr-h{{font-size:14px;font-weight:800;color:var(--text);margin-bottom:12px}}
.sr-pills{{display:flex;flex-wrap:wrap;gap:8px}}
.sr-pill{{padding:8px 14px;border-radius:999px;background:var(--input-bg);border:1px solid rgba(51,160,137,0.15);
  color:var(--mint);font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer}}
/* CANONICAL peak/live thumbnail card — identique au home (.hf-peak-card) + grilles (.pl-card) */
.sr-lives{{display:flex;gap:11px;overflow-x:auto;overflow-y:hidden;padding:6px 3px 9px}}
.sr-lives::-webkit-scrollbar{{display:none}}
.sr-live{{position:relative;flex-shrink:0;width:132px;aspect-ratio:3/4;border-radius:20px;overflow:hidden;animation:liveRedPulse 1.4s ease-in-out infinite}}
.sr-live img{{width:100%;height:100%;object-fit:cover}}
.sr-live-dot{{position:absolute;top:8px;left:8px;padding:3px 7px;border-radius:6px;background:#FF4658;
  color:#fff;font-size:9px;font-weight:800;letter-spacing:.05em}}
.sr-live-name{{position:absolute;bottom:10px;left:11px;right:11px;color:#fff;font-size:12px;font-weight:700;text-shadow:0 1px 4px rgba(0,0,0,.6)}}
/* CANONICAL creator card — dimensions IDENTIQUES au fanfeed (.hf-sug-card) */
.sr-crs{{display:grid;grid-template-columns:repeat(2,160px);justify-content:space-between;gap:14px}}
.sr-cr{{display:flex;flex-direction:column;align-items:center;gap:7px;width:160px;padding:16px 12px;border-radius:20px;
  background:var(--card);border:1px solid var(--border)}}
.sr-cr img{{width:56px;height:56px;border-radius:999px;object-fit:cover}}
.sr-cr-n{{font-size:13px;font-weight:800;color:var(--text);text-align:center}}
.sr-cr-r{{font-size:11px;font-weight:500;color:var(--sub);text-align:center}}
.sr-cr-follow{{margin-top:2px;width:100%;padding:8px 0;border:none;border-radius:999px;
  background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer}}
.sr-places{{display:flex;flex-direction:column;gap:10px}}
.sr-place{{display:flex;gap:12px;padding:10px;border-radius:20px;background:var(--card);border:1px solid var(--border)}}
.sr-place img{{width:62px;height:62px;border-radius:12px;object-fit:cover}}
.sr-place-t h4{{font-size:13.5px;font-weight:800;color:var(--text)}}
.sr-place-t p{{font-size:11.5px;color:var(--sub);font-weight:500;margin:2px 0 6px}}
.sr-place-map{{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;color:var(--mint)}}
/* XPLORER map */
.xp-map{{position:relative;width:100%;height:420px;overflow:hidden}}
/* Night/Day premium (tuné pour lisibilité des pins, moins immersif que le run) */
.xp-map-dark{{background:radial-gradient(120% 90% at 50% 28%, #0f201e 0%, #0a141a 60%, #0b1620 100%)}}
.xp-map-light{{background:radial-gradient(120% 90% at 50% 24%, #f4f9f7 0%, #e7f0f1 55%, #dde8ea 100%)}}
.xp-grid-lines{{position:absolute;inset:0;
  background-image:
    linear-gradient(rgba(51,160,137,0.08) 1px,transparent 1px),
    linear-gradient(90deg,rgba(51,160,137,0.08) 1px,transparent 1px),
    linear-gradient(60deg,transparent 49.6%,rgba(51,160,137,0.06) 50%,transparent 50.4%),
    linear-gradient(-60deg,transparent 49.6%,rgba(51,160,137,0.05) 50%,transparent 50.4%);
  background-size:46px 46px,46px 46px,180px 180px,240px 240px}}
.xp-pin{{position:absolute;transform:translate(-50%,-50%);width:42px;height:42px;border-radius:999px;
  border:2.5px solid {MINT};overflow:hidden;box-shadow:0 0 0 4px rgba(51,160,137,0.2),0 4px 12px rgba(0,0,0,.4)}}
.xp-pin img{{width:100%;height:100%;object-fit:cover}}
/* location markers (business/event/activity/spot) — icon + category color, not avatars */
.xp-marker{{position:absolute;transform:translate(-50%,-50%);width:34px;height:34px;border-radius:999px;
  background:var(--mc);display:flex;align-items:center;justify-content:center;border:2px solid #fff;
  box-shadow:0 0 0 3px color-mix(in srgb, var(--mc) 25%, transparent),0 4px 12px rgba(0,0,0,.45)}}
.xp-badge{{display:inline-flex;align-items:center;gap:4px;padding:2px 8px;border-radius:999px;
  font-size:10px;font-weight:800;margin-bottom:5px}}
.xp-recenter{{position:absolute;bottom:16px;right:16px;width:42px;height:42px;border-radius:999px;
  border:1px solid var(--border);background:var(--card);display:flex;align-items:center;justify-content:center;cursor:pointer;
  box-shadow:0 4px 14px rgba(0,0,0,.3)}}
.xp-searchbar{{position:absolute;top:12px;left:14px;right:14px;z-index:6;display:flex;align-items:center;gap:9px;
  padding:11px 12px;border-radius:16px;background:var(--card);border:1px solid var(--border);
  box-shadow:0 4px 16px rgba(0,0,0,.25);font-size:13px;color:var(--sub);font-weight:500}}
.xp-searchbar>span{{flex:1}}
.xp-filter-btn{{width:30px;height:30px;border:none;border-radius:10px;background:var(--input-bg);cursor:pointer;
  display:flex;align-items:center;justify-content:center}}
.xp-fchips{{position:absolute;top:62px;left:0;right:0;z-index:6;display:flex;gap:8px;overflow-x:auto;padding:4px 14px}}
.xp-fchips::-webkit-scrollbar{{display:none}}
.xp-fchip{{flex-shrink:0;padding:7px 14px;border-radius:999px;border:1px solid var(--border);background:var(--card);
  color:var(--text);font-family:inherit;font-size:12.5px;font-weight:700;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.15)}}
.xp-fchip-on{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;border-color:transparent}}
.xp-sheet{{position:relative;margin-top:-24px;background:var(--page);border-radius:24px 24px 0 0;
  padding:8px 16px 100px;z-index:5}}
.xp-handle{{width:38px;height:4px;border-radius:999px;background:var(--input-border);margin:6px auto 14px}}
.xp-h{{font-size:14px;font-weight:800;color:var(--text);margin-bottom:12px}}
.xp-cards{{display:flex;flex-direction:column;gap:10px}}
.xp-card{{display:flex;gap:12px;align-items:center;padding:10px;border-radius:20px;background:var(--card);border:1px solid var(--border)}}
.xp-card img{{width:50px;height:50px;border-radius:12px;object-fit:cover}}
.xp-card-t h4{{font-size:13.5px;font-weight:800;color:var(--text)}}
.xp-card-t p{{display:flex;align-items:center;gap:5px;font-size:11.5px;color:var(--sub);font-weight:600;margin-top:2px}}
.xp-dot{{width:7px;height:7px;border-radius:999px;background:{MINT};box-shadow:0 0 6px {MINT}}}
/* PEAKS / LIVE — grille + chips (founder jun03) */
/* Peaks/Live tabs = SAME canonical pill segmented control as Fan/Vibes/Xplorer + profile */
.pl-top{{display:grid;grid-template-columns:34px 1fr 34px;align-items:center;padding:14px 16px 8px}}
.pl-back{{width:34px;height:34px;border:none;background:transparent;cursor:pointer;display:flex;align-items:center;justify-content:center}}
.pl-tabs{{justify-self:center;display:inline-grid;grid-auto-flow:column;gap:4px;padding:4px;border-radius:999px;
  background:var(--input-bg);border:1px solid var(--input-border)}}
.pl-tab{{padding:8px 26px;border:none;border-radius:999px;background:transparent;color:var(--sub);
  font-family:inherit;font-size:14px;font-weight:700;cursor:pointer}}
.pl-tab-on{{background:var(--card);color:var(--mint);
  box-shadow:0 0 16px rgba(51,160,137,0.15),0 0 0 1px rgba(51,160,137,0.225)}}
.pl-chips{{display:flex;gap:8px;overflow-x:auto;padding:10px 16px 14px}}
.pl-chips::-webkit-scrollbar{{display:none}}
.pl-chip{{flex-shrink:0;padding:8px 16px;border-radius:999px;border:1px solid var(--input-border);background:var(--input-bg);
  color:var(--text);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer}}
.pl-chip-on{{background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;border-color:transparent}}
.pl-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 16px 100px}}
.pl-card{{position:relative;aspect-ratio:3/4;border-radius:20px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,{t['dim']})}}
.pl-card img{{width:100%;height:100%;object-fit:cover;display:block}}
.pl-card-scrim{{position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(0,0,0,.7) 100%)}}
.pl-card-name{{position:absolute;left:11px;bottom:10px;right:11px;color:#fff;font-size:12px;font-weight:700;
  text-shadow:0 1px 4px rgba(0,0,0,.5)}}
.pl-card-play{{position:absolute;top:10px;left:10px;display:flex;align-items:center;gap:3px;padding:3px 8px;border-radius:999px;
  background:rgba(0,0,0,.45);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);color:#fff;font-size:11px;font-weight:700}}
.pl-empty{{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:90px 32px;gap:16px}}
.pl-empty-ic{{width:80px;height:80px;border-radius:999px;background:var(--input-bg);display:flex;align-items:center;justify-content:center}}
.pl-empty-txt{{font-size:15px;font-weight:600;color:var(--sub);text-align:center}}
.pl-empty-cta{{padding:13px 28px;border:none;border-radius:999px;background:linear-gradient(135deg,{GRAD_A},{GRAD_B});
  color:#fff;font-family:inherit;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 6px 18px rgba(51,160,137,0.175)}}
.pl-card-live{{text-decoration:none;animation:liveRedPulse 1.4s ease-in-out infinite}}
.pl-livebadge{{position:absolute;top:10px;right:10px;display:flex;align-items:center;gap:5px;padding:3px 9px;border-radius:999px;
  background:rgba(255,70,88,.95);color:#fff;font-size:10px;font-weight:800;letter-spacing:.03em}}
.pl-livedot{{width:6px;height:6px;border-radius:999px;background:#fff}}
/* LIVE preview → paywall */
.lp-stage{{position:relative;width:393px;height:852px;overflow:hidden;background:#000}}
.lp-media{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.lp-scrim{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.4) 0%,transparent 30%,rgba(0,0,0,.5) 70%,rgba(0,0,0,.85) 100%)}}
.lp-close{{position:absolute;top:16px;right:16px;width:36px;height:36px;border:none;border-radius:999px;
  background:rgba(0,0,0,.4);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);cursor:pointer;
  display:flex;align-items:center;justify-content:center;z-index:7}}
.lp-livebadge{{position:absolute;top:18px;left:16px;display:flex;align-items:center;gap:6px;padding:5px 11px;border-radius:999px;
  background:rgba(255,70,88,.95);color:#fff;font-size:11px;font-weight:800;z-index:7}}
.lp-preview-tag{{position:absolute;top:54px;left:16px;display:flex;align-items:center;gap:5px;padding:5px 11px;border-radius:999px;
  background:rgba(0,0,0,.5);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:#fff;font-size:11px;font-weight:700;z-index:7}}
.lp-creator{{position:absolute;top:140px;left:16px;display:flex;align-items:center;gap:10px;z-index:6}}
.lp-creator img{{width:42px;height:42px;border-radius:999px;object-fit:cover;border:2px solid #fff}}
.lp-creator div{{display:flex;flex-direction:column}}
.lp-name{{color:#fff;font-size:15px;font-weight:800;text-shadow:0 1px 4px rgba(0,0,0,.5)}}
.lp-cap{{color:rgba(255,255,255,.85);font-size:12px;font-weight:500;text-shadow:0 1px 4px rgba(0,0,0,.5)}}
.lp-paywall{{position:absolute;left:0;right:0;bottom:74px;z-index:8;background:var(--page);
  border-radius:26px 26px 0 0;padding:10px 22px 26px;text-align:center;
  box-shadow:0 -10px 40px rgba(0,0,0,.5)}}
.lp-pw-handle{{width:40px;height:4px;border-radius:999px;background:var(--input-border);margin:0 auto 16px}}
.lp-pw-lock{{width:54px;height:54px;border-radius:999px;margin:0 auto 12px;background:var(--input-bg);
  display:flex;align-items:center;justify-content:center}}
.lp-pw-title{{font-size:18px;font-weight:800;color:var(--text);margin-bottom:6px}}
.lp-pw-sub{{font-size:13px;color:var(--sub);font-weight:500;line-height:1.5;margin:0 auto 18px;max-width:290px}}
.lp-pw-cta{{display:block;width:100%;padding:14px 0;border:none;border-radius:16px;text-decoration:none;
  background:linear-gradient(135deg,{GRAD_A},{GRAD_B});color:#fff;font-family:inherit;font-size:15px;font-weight:700;
  box-shadow:0 6px 18px rgba(51,160,137,0.175);cursor:pointer}}
.lp-pw-ghost{{margin-top:10px;width:100%;padding:12px 0;border:none;background:transparent;color:var(--sub);
  font-family:inherit;font-size:13px;font-weight:700;cursor:pointer}}
@keyframes liveRedPulse{{0%,100%{{box-shadow:0 0 0 2.5px #FF4658,0 0 14px 2px rgba(255,70,88,.55)}}50%{{box-shadow:0 0 0 2.5px rgba(255,70,88,.35),0 0 4px 1px rgba(255,70,88,.15)}}}}
{bnav_css}
</style></head><body><div class="device">{body}</div></body></html>'''


SCREENS = {
    'vibes_feed_v2': ('Vibes', screen_vibes),
    'search_v2': ('Search', screen_search),
    'xplorer_map_v2': ('Xplorer', screen_xplorer),
    'peaks_live_feed_v2': ('Peaks', lambda dark: screen_peaks_live(dark, 'peaks')),
    'peaks_live_live_v2': ('Live', lambda dark: screen_peaks_live(dark, 'live')),
    'live_preview_v2': ('Live preview → paywall', screen_live_preview),
}


def main():
    n = 0
    for key, (title, fn) in SCREENS.items():
        for dark in (True, False):
            th = 'dark' if dark else 'light'
            d = OUT / f'{key}_{th}'
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(page(title, fn(dark), dark), encoding='utf-8')
            n += 1
    print(f'wrote {n} feed screens to {OUT}')


if __name__ == '__main__':
    main()
