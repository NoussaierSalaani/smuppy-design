#!/usr/bin/env python3
"""
build_profile_cover.py — Canonical Profile, ALL 6 sub-tabs, cover+avatar header (NO hero).

Header (validated 2026-05-27): cover banner (background-image) + circular avatar LEFT +
"Become a fan" gradient pill + message circle (44px, grey bubble 20px, mint glow both modes) +
name/verified/role/bio/stats LEFT + tabs Lifestyle/Channel (pills, canonical mint glow, NO About)
+ sub-pills + canonical Smuppy bottom nav (exact SVGs, square mint-outlined profile avatar) +
canonical message bubble icon. overflow-x hidden, local assets.

Content per sub-tab faithful to ~/Desktop/smuppy-v2-design/screens/04-profile/04-profile-sub-tabs.md
+ foundation tokens. Lifestyle = Posts/Peaks/Activities · Channel = Library/1:1/Packs.

Regenerate: python3 build_profile_cover.py
"""
from pathlib import Path

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')
MINT = '#33A089'
GREY = '#94a3b8'
GRAD = 'linear-gradient(135deg,#41AD96 0%,#2C95A0 100%)'
COVER = '/maquettes/_assets/cover.jpg'
AVATAR = '/maquettes/_assets/avatar.jpg'
U = 'https://images.unsplash.com/'

NAV_HOME = ('<svg width="26" height="26" viewBox="0 0 20 21" fill="none"><path fill-rule="evenodd" '
            'clip-rule="evenodd" d="M7.5601 3.3893C5.0178 5.277 3.7466 6.2209 3.2474 7.6151C3.2073 7.727 '
            '3.1713 7.8403 3.1394 7.9548C2.7414 9.3827 3.227 10.9099 4.198 13.9643C5.1691 17.0187 5.6546 '
            '18.5459 6.7978 19.462C6.8895 19.5355 6.9838 19.6055 7.0805 19.672C8.2863 20.5 9.8575 20.5 13 '
            '20.5C16.1425 20.5 17.7137 20.5 18.9195 19.672C19.0162 19.6055 19.1105 19.5355 19.2022 '
            '19.462C20.3454 18.5459 20.8309 17.0187 21.802 13.9643C22.773 10.9099 23.2586 9.3827 22.8606 '
            '7.9548C22.8287 7.8403 22.7927 7.727 22.7526 7.6151C22.2534 6.2209 20.9822 5.277 18.4399 '
            '3.3893C15.8976 1.5016 14.6265 0.5577 13.1747 0.5033C13.0583 0.4989 12.9417 0.4989 12.8253 '
            '0.5033C11.3735 0.5577 10.1024 1.5016 7.5601 3.3893ZM11.0934 15.1821C10.6985 15.1821 10.3784 '
            '15.5093 10.3784 15.9129C10.3784 16.3164 10.6985 16.6436 11.0934 16.6436H14.9066C15.3015 '
            '16.6436 15.6216 16.3164 15.6216 15.9129C15.6216 15.5093 15.3015 15.1821 14.9066 15.1821H11.0934Z" '
            'fill="{c}" transform="translate(-3, 0)"/></svg>')
NAV_PEAKS = ('<svg width="26" height="26" viewBox="0 0 21 20" fill="none"><path d="M15.7 19.335C14.528 '
             '19.5 13 19.5 10.95 19.5H9.05C5.019 19.5 3.004 19.5 1.752 18.248C0.5 16.996 0.5 14.981 0.5 '
             '10.95V9.05C0.5 5.019 0.5 3.004 1.752 1.752C3.004 0.5 5.019 0.5 9.05 0.5H10.95C14.981 0.5 '
             '16.996 0.5 18.248 1.752C19.5 3.004 19.5 5.019 19.5 9.05V10.95C19.5 12.158 19.5 13.185 19.466 '
             '14.065C19.439 14.77 19.426 15.123 19.159 15.254C18.892 15.386 18.593 15.175 17.996 '
             '14.752L16.65 13.8" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
             'fill="none"/><path d="M12.945 10.395C12.769 11.021 11.933 11.464 10.263 12.35C8.648 13.206 '
             '7.841 13.635 7.19 13.462C6.921 13.391 6.676 13.256 6.478 13.07C6 12.62 6 11.746 6 10C6 8.253 '
             '6 7.38 6.478 6.93C6.676 6.744 6.921 6.609 7.19 6.538C7.841 6.365 8.648 6.794 10.263 7.65C11.933 '
             '8.536 12.769 8.978 12.945 9.605C13.018 9.864 13.018 10.136 12.945 10.395Z" stroke="{c}" '
             'stroke-width="1.8" stroke-linejoin="round" fill="none"/></svg>')
NAV_MSG = ('<svg width="26" height="26" viewBox="0 0 24 24" fill="none"><path d="M12 3C7.029 3 3 7.029 3 '
           '12C3 13.689 3.466 15.274 4.287 16.628L3.016 19.832C2.76 20.478 3.303 21.14 3.985 20.994L7.789 '
           '20.158C9.05 20.693 10.447 21 12 21C16.971 21 21 16.971 21 12C21 7.029 16.971 3 12 3Z" '
           'stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')
NAV_PLUS = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 5V19M5 12H19" '
            'stroke="#33A089" stroke-width="2.5" stroke-linecap="round"/></svg>')

# tab → (group, sub-pill labels, active index)
TABS = {
    'posts':      ('Lifestyle', ['Posts', 'Peaks', 'Activities'], 0),
    'peaks':      ('Lifestyle', ['Posts', 'Peaks', 'Activities'], 1),
    'activities': ('Lifestyle', ['Posts', 'Peaks', 'Activities'], 2),
    'library':    ('Channel',   ['Library', '1:1', 'Packs'], 0),
    'calendly':   ('Channel',   ['Library', '1:1', 'Packs'], 1),
    'coaching':   ('Channel',   ['Library', '1:1', 'Packs'], 2),
}


def theme(dark):
    if dark:
        return dict(page='#000000', text='#F1F4F6', sub='#8B8B95', outline='#26262E',
                    glass='rgba(10,10,12,.55)', grid='#14141A', card='#0E0E13', nav_bg='#0A0A0C',
                    nav_border='#1A1A20', create_bg='#14141A', html='dark', dim='0.4',
                    chat_border='rgba(51,160,137,0.175)', chat_glow='0 0 18px rgba(51,160,137,0.275)',
                    msg_icon='#CBD5E1', msg_glow='drop-shadow(0 0 6px rgba(51,160,137,0.3))',
                    pill_on_bg='#2E2E38', pill_on_shadow='0 4px 12px rgba(51,160,137,0.15)',
                    pill_on_outline='1px solid rgba(51,160,137,0.15)')
    return dict(page='#FFFFFF', text='#0F1419', sub='#5A6671', outline='#E5E9EB',
                glass='rgba(255,255,255,.55)', grid='#F5F7F8', card='#FFFFFF', nav_bg='#FFFFFF',
                nav_border='#EEF1F4', create_bg='#FFFFFF', html='light', dim='0.06',
                chat_border='#E5E9EB', chat_glow='0 2px 12px rgba(51,160,137,0.15)',
                msg_icon='#64748B', msg_glow='none',
                pill_on_bg='#FFFFFF', pill_on_shadow='0 4px 12px rgba(51,160,137,0.2)',
                pill_on_outline='none')


def ms(name, size, color, fill=0):
    return (f'<span class="material-symbols-outlined" '
            f"style=\"font-size:{size}px;color:{color};font-variation-settings:'FILL' {fill}\">{name}</span>")


# ───────────────────────── content per sub-tab ─────────────────────────
def c_posts(t):
    ids = ['photo-1517836357463-d25dfeac3438', 'photo-1518310383802-640c2de311b2',
           'photo-1571019613454-1cb2f99b2d8b', 'photo-1599058917212-d750089bc07e',
           'photo-1534438327276-14e5300c3a48', 'photo-1540206395-68808572332f',
           'photo-1518611012118-696072aa579a', 'photo-1506126613408-eca07ce68773',
           'photo-1544367567-0f2fcb009e0b']
    cells = ''.join(f'<div class="cell"><img src="{U}{i}?w=300&h=300&fit=crop" alt=""/></div>' for i in ids)
    return f'<div class="grid posts">{cells}</div>'


def c_peaks(t):
    ids = ['photo-1518459031867-a89b944bffe4', 'photo-1546483875-ad9014c88eba',
           'photo-1517836357463-d25dfeac3438', 'photo-1540206395-68808572332f',
           'photo-1551698618-1dfe5d97d256', 'photo-1574680096145-d05b474e2155']
    views = ['12K', '8.4K', '23K', '5.1K', '17K', '9.9K']
    cells = ''.join(
        f'<div class="pcell"><img src="{U}{i}?w=300&h=520&fit=crop" alt=""/>'
        f'<span class="pviews">{ms("play_arrow",14,"#fff",1)} {v}</span></div>'
        for i, v in zip(ids, views))
    return f'<div class="grid peaks">{cells}</div>'


def c_activities(t):
    items = [
        ('photo-1538805060514-97d9cc17730c', 'Morning trail run', 'Running', '📍 Mount Royal · Sat 8:00 · 12 joined', True),
        ('photo-1571019614242-c5c5dee9f50b', 'Power yoga flow', 'Yoga', '📍 Studio Mile-End · Sun 10:00 · 8 joined', False),
        ('photo-1517963879433-6ad2b056d712', 'Sunset HIIT session', 'HIIT', '📍 Parc Jarry · Wed 18:30 · 21 joined', False),
    ]
    cards = ''
    for img, title, sport, meta, joined in items:
        badge = (f'<span class="joined">{ms("check",13,"#fff",1)} Joined</span>' if joined else '')
        cards += (
            f'<div class="acard"><div class="acover"><img src="{U}{img}?w=600&h=340&fit=crop" alt=""/>'
            f'<span class="chip">{sport}</span>{badge}</div>'
            f'<div class="abody"><div class="atitle">{title}</div>'
            f'<div class="ameta">{meta}</div></div></div>')
    return f'<div class="list">{cards}</div>'


def c_library(t):
    banner = (f'<div class="unlock">{ms("lock_open",16,"#fff")} Unlock library — 4,99€/mois</div>')
    items = [
        ('photo-1599058917212-d750089bc07e', 'Full body morning flow — Day 1', 'Sara Khan', '42:10', 65, False),
        ('photo-1518611012118-696072aa579a', 'Hip mobility deep dive', 'Sara Khan', '28:46', 0, True),
        ('photo-1544367567-0f2fcb009e0b', 'Core stability essentials', 'Sara Khan', '35:02', 0, True),
    ]
    cards = ''
    for img, title, author, dur, prog, locked in items:
        lock = (f'<div class="clock">{ms("lock",26,"#fff",1)}</div>' if locked else '')
        play = '' if locked else f'<div class="cplay">{ms("play_circle",48,"#fff",1)}</div>'
        bar = (f'<div class="cprog"><span style="width:{prog}%"></span></div>' if prog else '')
        blur = 'filter:blur(6px);' if locked else ''
        cards += (
            f'<div class="ccard"><div class="cthumb"><img src="{U}{img}?w=600&h=340&fit=crop" style="{blur}" alt=""/>'
            f'{play}{lock}<span class="cdur">{dur}</span>{bar}</div>'
            f'<div class="cbody"><div class="ctitle">{title}</div><div class="cauthor">{author}</div></div></div>')
    return f'<div class="list">{banner}{cards}</div>'


def c_calendly(t):
    pricing = (f'<div class="pricing"><div class="pr-h">Coaching 1:1</div>'
               f'<div class="pr-p">45€ <span>/ 60 min</span></div>'
               f'<div class="pr-d">One-on-one video session — personalised program & live feedback.</div></div>')
    days = [('Mon', '12', True), ('Tue', '13', True), ('Wed', '14', False), ('Thu', '15', True),
            ('Fri', '16', True), ('Sat', '17', True), ('Sun', '18', False)]
    scroller = ''.join(
        f'<div class="day{" sel" if i==1 else ""}"><span class="dow">{d}</span><span class="dn">{n}</span>'
        f'<span class="dot" style="{"opacity:0" if not av else ""}"></span></div>'
        for i, (d, n, av) in enumerate(days))
    slots = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']
    booked = {'11:00', '15:00'}
    sel = '14:00'
    sl = ''.join(
        f'<div class="slot{" booked" if s in booked else ""}{" ssel" if s==sel else ""}">{s}</div>' for s in slots)
    return (f'<div class="cal">{pricing}'
            f'<div class="scroller">{scroller}</div>'
            f'<div class="slots">{sl}</div></div>'
            f'<div class="reserve">Réserver — 45€</div>')


def c_coaching(t):
    items = [
        ('Transformation 4 weeks', '4 sem · 8 sessions',
         ['2 live 1:1 sessions / week', 'Custom nutrition plan', 'WhatsApp daily support', 'Weekly progress review'],
         '320€', '269€', 'Best seller'),
        ('Kickstart pack', '2 sem · 4 sessions',
         ['1 live 1:1 session / week', 'Starter workout program', 'Form-check video reviews'],
         '180€', '149€', None),
    ]
    cards = ''
    for title, dur, benefits, promo, price, badge in items:
        bd = (f'<span class="pbadge">{badge}</span>' if badge else '')
        bl = ''.join(f'<li>{ms("check_circle",16,MINT,1)} {b}</li>' for b in benefits)
        cards += (
            f'<div class="pack">{bd}<div class="pk-h"><div><div class="pk-t">{title}</div>'
            f'<div class="pk-d">{dur}</div></div></div>'
            f'<ul class="pk-ben">{bl}</ul>'
            f'<div class="pk-foot"><div class="pk-price"><s>{promo}</s><b>{price}</b></div></div>'
            f'<button class="pk-cta">Réserver le pack {ms("arrow_forward",18,"#fff")}</button></div>')
    return f'<div class="list packs">{cards}</div>'


CONTENT = {'posts': c_posts, 'peaks': c_peaks, 'activities': c_activities,
           'library': c_library, 'calendly': c_calendly, 'coaching': c_coaching}


def build(tab, dark):
    t = theme(dark)
    group, subs, active = TABS[tab]
    toptabs = ''.join(
        f'<button class="pill {"on" if g==group else "off"}">{g}</button>' for g in ('Lifestyle', 'Channel'))
    subpills = ''.join(
        f'<button class="pill {"on" if i==active else "off"}">{s}</button>' for i, s in enumerate(subs))
    content = CONTENT[tab](t)
    return f'''<!DOCTYPE html>
<html class="{t['html']}" lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Smuppy — Profile / {tab}</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&amp;display=swap" rel="stylesheet"/>
<style>
  *{{box-sizing:border-box;-webkit-font-smoothing:antialiased}}
  html,body{{max-width:100%;overflow-x:hidden}}
  body{{margin:0;background:{t['page']};color:{t['text']};font-family:'Plus Jakarta Sans',sans-serif;
       padding-bottom:104px;min-height:max(844px,100dvh)}}
  .cover{{position:relative;width:100%;height:200px;overflow:hidden;background:url('{COVER}') center/cover no-repeat}}
  .cover::after{{content:'';position:absolute;inset:0;background:linear-gradient(to bottom,
       rgba(0,0,0,.18) 0%,transparent 28%,transparent 72%,{t['page']} 100%)}}
  .cover-btn{{position:absolute;top:18px;right:18px;background:none;border:none;cursor:pointer;
       display:flex;align-items:center;justify-content:center;z-index:2;filter:drop-shadow(0 1px 5px rgba(0,0,0,.55))}}
  .body{{padding:0 20px}}
  .avatar-row{{display:flex;align-items:flex-end;justify-content:space-between;margin-top:-44px;position:relative;z-index:2}}
  .avatar{{width:96px;height:96px;border-radius:999px;object-fit:cover;box-shadow:0 0 0 3px {MINT},0 0 0 6px {t['page']}}}
  .cta{{display:flex;align-items:center;gap:8px;padding-bottom:6px}}
  .fan{{display:inline-flex;align-items:center;gap:6px;padding:10px 18px;border-radius:999px;background:{GRAD};
       color:#fff;font-size:14px;font-weight:700;border:none;cursor:pointer;box-shadow:0 6px 16px rgba(51,160,137,0.175)}}
  .chat{{width:44px;height:44px;border-radius:999px;border:1.5px solid {t['chat_border']};background:none;
       display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:{t['chat_glow']};flex-shrink:0}}
  .chat svg{{width:20px;height:20px}}
  .navmsg svg{{filter:{t['msg_glow']}}}
  .name{{display:flex;align-items:center;gap:6px;margin-top:12px;font-size:24px;font-weight:800}}
  .meta{{font-size:13px;color:{t['sub']};margin-top:2px}}
  .bio{{font-size:14px;line-height:1.5;color:{t['text']};margin-top:10px}}
  .stats{{display:flex;gap:28px;margin-top:16px}}
  .stat b{{font-size:17px;font-weight:800;color:{t['text']};display:block}}
  .stat span{{font-size:12px;color:{t['sub']}}}
  .toptabs{{display:flex;gap:6px;background:{t['grid']};padding:4px;border-radius:999px;margin:20px 20px 0}}
  .subpills{{display:flex;gap:6px;background:{t['grid']};padding:4px;border-radius:999px;margin:10px 20px 0}}
  .pill{{flex:1;padding:8px;border-radius:999px;border:none;font-size:13px;cursor:pointer;font-weight:500;color:{t['sub']};background:none}}
  .pill.on{{background:{t['pill_on_bg']};color:{MINT};font-weight:700;box-shadow:{t['pill_on_shadow']};outline:{t['pill_on_outline']}}}
  /* content */
  .grid{{display:grid;gap:4px;padding:14px 20px 0}}
  .grid.posts{{grid-template-columns:repeat(3,1fr)}}
  .cell{{aspect-ratio:1;background:{t['grid']};border-radius:10px;overflow:hidden}}
  .cell img{{width:100%;height:100%;object-fit:cover}}
  .grid.peaks{{grid-template-columns:repeat(3,1fr)}}
  .pcell{{position:relative;aspect-ratio:9/16;background:{t['grid']};border-radius:12px;overflow:hidden}}
  .pcell img{{width:100%;height:100%;object-fit:cover}}
  .pviews{{position:absolute;left:6px;bottom:6px;display:flex;align-items:center;gap:2px;color:#fff;
       font-size:11px;font-weight:700;text-shadow:0 1px 4px rgba(0,0,0,.6)}}
  .list{{padding:14px 20px 0;display:flex;flex-direction:column;gap:14px}}
  /* activities */
  .acard{{background:{t['card']};border:1px solid {t['outline']};border-radius:20px;overflow:hidden;
       box-shadow:0 6px 20px rgba(0,107,89,{t['dim']})}}
  .acover{{position:relative;aspect-ratio:16/9}}
  .acover img{{width:100%;height:100%;object-fit:cover}}
  .chip{{position:absolute;top:10px;left:10px;background:{MINT};color:#fff;font-size:11px;font-weight:700;
       padding:4px 10px;border-radius:999px}}
  .joined{{position:absolute;top:10px;right:10px;display:flex;align-items:center;gap:3px;background:rgba(0,0,0,.55);
       color:#fff;font-size:11px;font-weight:700;padding:4px 9px;border-radius:999px;backdrop-filter:blur(6px)}}
  .abody{{padding:12px 14px 14px}}
  .atitle{{font-size:16px;font-weight:700}}
  .ameta{{font-size:12px;color:{t['sub']};margin-top:4px}}
  /* library */
  .unlock{{display:flex;align-items:center;justify-content:center;gap:6px;background:{GRAD};color:#fff;
       font-size:13px;font-weight:700;padding:11px;border-radius:14px}}
  .ccard{{background:{t['card']};border:1px solid {t['outline']};border-radius:18px;overflow:hidden;
       box-shadow:0 6px 20px rgba(0,107,89,{t['dim']})}}
  .cthumb{{position:relative;aspect-ratio:16/9;background:#000}}
  .cthumb img{{width:100%;height:100%;object-fit:cover}}
  .cplay{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
       filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}}
  .clock{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.35)}}
  .cdur{{position:absolute;bottom:8px;right:8px;background:rgba(0,0,0,.6);color:#fff;font-size:11px;
       font-weight:700;padding:3px 7px;border-radius:8px}}
  .cprog{{position:absolute;left:0;bottom:0;width:100%;height:2px;background:rgba(255,255,255,.2)}}
  .cprog span{{display:block;height:100%;background:{MINT}}}
  .cbody{{padding:11px 14px 13px}}
  .ctitle{{font-size:15px;font-weight:700}}
  .cauthor{{font-size:12px;color:{t['sub']};margin-top:3px}}
  /* calendly */
  .cal{{padding:14px 20px 0;display:flex;flex-direction:column;gap:16px}}
  .pricing{{background:{t['glass']};backdrop-filter:blur(20px) saturate(180%);border:1px solid {t['outline']};
       border-radius:24px;padding:18px}}
  .pr-h{{font-size:20px;font-weight:700}}
  .pr-p{{font-size:24px;font-weight:800;color:{MINT};margin-top:4px}}
  .pr-p span{{font-size:14px;font-weight:600;color:{t['sub']}}}
  .pr-d{{font-size:13px;color:{t['sub']};margin-top:8px;line-height:1.5}}
  .scroller{{display:flex;gap:8px;overflow-x:auto}}
  .day{{flex:0 0 auto;width:50px;padding:10px 0;border-radius:16px;border:1px solid {t['outline']};
       display:flex;flex-direction:column;align-items:center;gap:3px}}
  .day.sel{{background:{MINT};border-color:{MINT}}}
  .day.sel .dow,.day.sel .dn{{color:#fff}}
  .dow{{font-size:11px;color:{t['sub']}}}
  .dn{{font-size:17px;font-weight:700}}
  .dot{{width:5px;height:5px;border-radius:9px;background:{MINT}}}
  .day.sel .dot{{background:#fff}}
  .slots{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}
  .slot{{padding:11px;border-radius:12px;border:1.5px solid {MINT};color:{MINT};font-size:14px;
       font-weight:700;text-align:center}}
  .slot.ssel{{background:{MINT};color:#fff}}
  .slot.booked{{border-color:{t['outline']};color:{t['sub']};opacity:.5}}
  .reserve{{position:fixed;left:16px;right:16px;bottom:100px;background:{GRAD};color:#fff;text-align:center;
       padding:16px;border-radius:18px;font-size:15px;font-weight:700;box-shadow:0 8px 24px rgba(51,160,137,0.2)}}
  /* coaching packs */
  .pack{{position:relative;background:{t['glass']};backdrop-filter:blur(20px) saturate(180%);
       border:1px solid {t['outline']};border-radius:28px;padding:20px}}
  .pbadge{{position:absolute;top:16px;right:16px;background:{MINT};color:#fff;font-size:10px;font-weight:800;
       letter-spacing:.04em;padding:3px 9px;border-radius:999px;text-transform:uppercase}}
  .pk-t{{font-size:19px;font-weight:700}}
  .pk-d{{font-size:11px;color:{t['sub']};margin-top:2px}}
  .pk-ben{{list-style:none;margin:14px 0 0;padding:0;display:flex;flex-direction:column;gap:9px}}
  .pk-ben li{{display:flex;align-items:center;gap:8px;font-size:14px}}
  .pk-foot{{margin-top:16px}}
  .pk-price s{{color:{t['sub']};font-size:14px;margin-right:8px}}
  .pk-price b{{color:{MINT};font-size:22px;font-weight:800}}
  .pk-cta{{margin-top:14px;width:100%;display:flex;align-items:center;justify-content:center;gap:6px;
       background:{GRAD};color:#fff;border:none;padding:14px;border-radius:16px;font-size:15px;font-weight:700;cursor:pointer}}
  /* canonical bottom nav */
  .nav{{position:fixed;bottom:0;left:0;right:0;z-index:50;background:{t['nav_bg']};
       border-top:1px solid {t['nav_border']};border-radius:28px 28px 0 0;
       box-shadow:0 -4px 24px rgba(0,0,0,{t['dim']});padding:16px 24px 22px;
       display:flex;justify-content:space-around;align-items:center}}
  .nav button{{background:none;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;
       width:48px;height:48px;position:relative}}
  .nav .create{{width:48px;height:48px;border-radius:999px;background:{t['create_bg']};box-shadow:0 4px 12px rgba(51,160,137,0.2)}}
  .nav .active-bar{{position:absolute;bottom:-6px;left:50%;transform:translateX(-50%);width:24px;height:3px;
       border-radius:999px;background:{MINT};box-shadow:0 0 8px rgba(51,160,137,0.3)}}
  .nav .me{{width:30px;height:30px;border-radius:9px;object-fit:cover;outline:2px solid {MINT};
       outline-offset:2px;box-shadow:0 0 8px rgba(51,160,137,0.225)}}
</style>
</head>
<body>
<div class="cover" role="img" aria-label="Cover photo">
  <button class="cover-btn" aria-label="Settings">{ms('settings',26,'#fff')}</button>
</div>
<div class="body">
  <div class="avatar-row">
    <img class="avatar" src="{AVATAR}" alt="Sara Khan"/>
    <div class="cta">
      <button class="fan">{ms('favorite',16,'#fff',1)} Become a fan</button>
      <button class="chat" aria-label="Message">{NAV_MSG.format(c=t['msg_icon'])}</button>
    </div>
  </div>
  <div class="name">Sara Khan {ms('verified',20,MINT,1)}</div>
  <div class="meta">Yoga coach · Montreal · Contributor</div>
  <div class="bio">Helping you find inner peace through movement and breath. 🧘 #wellnessjourney</div>
  <div class="stats">
    <div class="stat"><b>24K</b><span>Fans</span></div>
    <div class="stat"><b>412</b><span>Posts</span></div>
    <div class="stat"><b>89</b><span>Peaks</span></div>
  </div>
</div>
<div class="toptabs">{toptabs}</div>
<div class="subpills">{subpills}</div>
{content}
<nav class="nav">
  <button aria-label="Home">{NAV_HOME.format(c=GREY)}</button>
  <button aria-label="Peaks">{NAV_PEAKS.format(c=GREY)}</button>
  <button class="create" aria-label="Create">{NAV_PLUS}</button>
  <button class="navmsg" aria-label="Messages">{NAV_MSG.format(c=GREY)}</button>
  <button aria-label="Profile"><img class="me" src="{AVATAR}" alt="Profile"/><span class="active-bar"></span></button>
</nav>
</body>
</html>
'''


def main():
    for tab in TABS:
        for dark in (False, True):
            name = f'profile_{tab}_{"dark" if dark else "light"}'
            d = OUT / name
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(build(tab, dark), encoding='utf-8')
            # drop stale screen.png from the old PNG-display version
            png = d / 'screen.png'
            if png.exists():
                png.unlink()
            print(f'  built: {name}')


if __name__ == '__main__':
    main()
