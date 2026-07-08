#!/usr/bin/env python3
"""Smuppy V2 — clickable HTML prototype shell.
Device frame + iframe + control bar (Feeds/Search/Peaks-Live/Create/Profiles) + full screen
picker + dark/light toggle. Navigates the live served maquettes. Open via the design server:
  http://127.0.0.1:8765/prototype_v5.html
Generated from the harmonized/ dir so the screen list stays in sync. Pure stdlib.
"""
from pathlib import Path
import json

ROOT = Path('/tmp/smuppy-v2-recovery')
HARM = ROOT / 'maquettes' / 'harmonized'
OUT = ROOT / 'prototype_v5.html'

# Curated nav: control-bar primary destinations (screen key WITHOUT theme suffix)
PRIMARY = [
    ('home', 'Feeds', 'home', 'home_feed_v2'),
    ('search', 'Search', 'search', 'search_v2'),
    ('peaks', 'Peaks/Live', 'film', 'peaks_live_feed_v2'),
    ('create', 'Créer', 'add-circle', 'post_create_menu_v2'),
    ('profile', 'Profil', 'person', 'profile_personal_owner_v2'),
]

# Category groups for the full picker (label, prefixes)
GROUPS = [
    ('Feeds & Discover', ['home_feed', 'vibes_feed', 'xplorer_map', 'search', 'peaks_live']),
    ('Profils', ['profile_personal', 'profile_creator', 'profile_business']),
    ('Creator monétisation', ['creator_channel', 'creator_1on1', 'creator_packages']),
    ('Booking & Sessions', ['p2_creator_booking', 'p2_business_booking', 'p2_my_sessions',
                            'p2_session_payment', 'p2_private_call', 'p2_session_ended']),
    ('Création', ['post_create', 'post_gallery', 'post_details', 'post_success', 'peak_camera']),
    ('Settings & Messages', ['settings_definitive', 'p1_settings', 'p1_notification', 'p1_privacy',
                             'p1_security', 'p1_messages', 'p1_edit_profile']),
    ('Auth & Onboarding', ['auth_', 'onb_']),
]


def screen_keys():
    """All unique screen keys (theme stripped) present in harmonized/."""
    keys = set()
    for d in HARM.iterdir():
        if d.is_dir() and (d / 'code.html').exists():
            n = d.name
            for suf in ('_dark', '_light'):
                if n.endswith(suf):
                    keys.add(n[: -len(suf)]); break
            else:
                keys.add(n)
    return sorted(keys)


def has(key, theme):
    return (HARM / f'{key}_{theme}' / 'code.html').exists() or (HARM / key / 'code.html').exists()


def resolve(key, theme):
    """Return the served path for key+theme, falling back to no-suffix dir."""
    if (HARM / f'{key}_{theme}').is_dir():
        return f'maquettes/harmonized/{key}_{theme}/code.html'
    if (HARM / key).is_dir():
        return f'maquettes/harmonized/{key}/code.html'
    # try other theme
    other = 'light' if theme == 'dark' else 'dark'
    if (HARM / f'{key}_{other}').is_dir():
        return f'maquettes/harmonized/{key}_{other}/code.html'
    return None


def main():
    keys = screen_keys()
    # Build picker groups (only keys that exist), keep an "Autres" bucket
    grouped, seen = [], set()
    for label, prefixes in GROUPS:
        items = [k for k in keys if any(k.startswith(p) for p in prefixes) and k not in seen]
        for k in items:
            seen.add(k)
        if items:
            grouped.append((label, items))
    autres = [k for k in keys if k not in seen]
    if autres:
        grouped.append(('Autres', autres))

    picker = ''
    for label, items in grouped:
        chips = ''.join(f'<button class="pk" data-key="{k}">{k.replace("_v2", "")}</button>' for k in items)
        picker += f'<div class="pk-group"><div class="pk-label">{label}</div><div class="pk-chips">{chips}</div></div>'

    primary = ''.join(
        f'<button class="cb {"cb-on" if i == 0 else ""}" data-key="{key}">'
        f'<ion-icon name="{ic}" style="font-size:22px"></ion-icon><span>{label}</span></button>'
        for i, (slot, label, ic, key) in enumerate(PRIMARY))

    start = resolve(PRIMARY[0][3], 'dark') or 'maquettes/harmonized/home_feed_v2_dark/code.html'

    doc = f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Smuppy V2 · Prototype clickable</title>
<meta http-equiv="Cache-Control" content="no-cache">
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Plus Jakarta Sans',system-ui,sans-serif;
  background:radial-gradient(circle at 50% 0%,#1a1a25,#050508 70%);color:#F1F4F6;
  min-height:100vh;display:flex;gap:28px;padding:32px;align-items:flex-start;justify-content:center;flex-wrap:wrap}}
.stage{{display:flex;flex-direction:column;align-items:center;gap:16px}}
.frame{{width:413px;height:872px;border-radius:46px;padding:10px;background:#0b0b10;
  box-shadow:0 0 0 2px #33A08933,0 30px 80px rgba(0,0,0,.6);position:relative}}
iframe{{width:393px;height:852px;border:none;border-radius:38px;background:#000;display:block}}
/* control bar (prototype nav) */
.ctrl{{display:flex;gap:6px;background:rgba(20,20,26,.8);backdrop-filter:blur(12px);
  border:1px solid rgba(51,160,137,0.25);border-radius:20px;padding:8px}}
.cb{{display:flex;flex-direction:column;align-items:center;gap:3px;width:74px;padding:9px 4px;
  border:none;border-radius:14px;background:transparent;color:#8B8B95;cursor:pointer;
  font-family:inherit;font-size:11px;font-weight:700;transition:.15s}}
.cb-on,.cb:hover{{background:rgba(51,160,137,0.14);color:#33A089}}
.toggle{{display:flex;gap:8px;align-items:center}}
.tg{{padding:7px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.12);background:transparent;
  color:#8B8B95;font-family:inherit;font-size:12px;font-weight:700;cursor:pointer}}
.tg-on{{background:#33A089;color:#04201B;border-color:#33A089}}
/* side picker */
.side{{width:300px;max-height:872px;overflow-y:auto;background:rgba(20,20,26,.55);
  border:1px solid rgba(51,160,137,0.18);border-radius:24px;padding:20px}}
.side h2{{font-size:16px;font-weight:900;background:linear-gradient(90deg,#33A089,#2C95A0);
  -webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:4px}}
.side .sub{{font-size:11px;color:#8B8B95;font-weight:600;margin-bottom:16px}}
.pk-group{{margin-bottom:16px}}
.pk-label{{font-size:10px;font-weight:800;color:#33A089;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px}}
.pk-chips{{display:flex;flex-wrap:wrap;gap:6px}}
.pk{{padding:6px 10px;border-radius:10px;border:1px solid rgba(255,255,255,.08);background:rgba(255,255,255,.03);
  color:#C9C9D2;font-family:inherit;font-size:11px;font-weight:600;cursor:pointer;transition:.15s}}
.pk:hover{{border-color:rgba(51,160,137,0.25);color:#33A089}}
</style></head>
<body>
<div class="side">
  <h2>Smuppy V2 · Prototype</h2>
  <p class="sub">Clique un écran ou utilise la barre du bas. Toggle dark/light.</p>
  {picker}
</div>
<div class="stage">
  <div class="toggle">
    <button class="tg tg-on" data-theme="dark">Dark</button>
    <button class="tg" data-theme="light">Light</button>
  </div>
  <div class="frame"><iframe id="screen" src="{start}"></iframe></div>
  <div class="ctrl">{primary}</div>
</div>
<script>
  const RESOLVE = {json.dumps({k: {'dark': resolve(k, 'dark'), 'light': resolve(k, 'light')} for k in keys})};
  let curKey = {json.dumps(PRIMARY[0][3])};
  let curTheme = 'dark';
  const frame = document.getElementById('screen');
  function load(key){{
    const r = RESOLVE[key]; if(!r) return;
    const path = r[curTheme] || r.dark || r.light; if(!path) return;
    curKey = key; frame.src = path;
    document.querySelectorAll('.cb').forEach(b=>b.classList.toggle('cb-on', b.dataset.key===key));
  }}
  document.querySelectorAll('.cb').forEach(b=>b.addEventListener('click',()=>load(b.dataset.key)));
  document.querySelectorAll('.pk').forEach(b=>b.addEventListener('click',()=>load(b.dataset.key)));
  document.querySelectorAll('.tg').forEach(b=>b.addEventListener('click',()=>{{
    curTheme=b.dataset.theme;
    document.querySelectorAll('.tg').forEach(x=>x.classList.toggle('tg-on',x.dataset.theme===curTheme));
    load(curKey);
  }}));
</script>
</body></html>'''
    OUT.write_text(doc, encoding='utf-8')
    print(f'wrote {OUT} · {len(keys)} screens · {len(grouped)} groups')


if __name__ == '__main__':
    main()
