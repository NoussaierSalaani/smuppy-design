"""Smuppy V2 — HOME canonical at 393×852 device format (replaces external Stitch dump).
Fan / Vibes / Xplorer tabs + Peaks & Live carousel + Suggestions + Post feed + bottom nav.
"""

import sys, json
from pathlib import Path

sys.path.insert(0, '/tmp/smuppy-v2-recovery/maquettes')
from build_auth_v2 import (
    MINT, MINT_HI, MINT_DEEP,
    theme, smuppy_text, smuppy_icon, smuppy_full,
    build as auth_build_fn,
)
from build_p1_v2 import _P1_CSS

OUT_DIR = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')


from canonical_bnav import canonical_bnav, CANONICAL_BNAV_CSS


def bottom_nav_canonical(active: str = 'home') -> str:
    """Single source of truth — uses canonical_bnav helper with EXACT SVG paths
    from v2_canonical_home_feed Stitch dump (founder may30 lock)."""
    mapped = 'peaks' if active == 'play' else active
    return canonical_bnav(mapped)


def screen_home_fan(th: dict) -> str:
    """Fan tab : header + 3 tabs pill + Peaks&Live carousel + Suggestions + Posts feed."""
    return f'''<header class="hf-topbar">
  <button class="hf-top-btn hf-top-btn-notif">
    <ion-icon name="notifications-outline" style="font-size:22px;color:var(--text)"></ion-icon>
    <span class="hf-top-badge">3</span>
  </button>
  <div class="hf-brand">{smuppy_text(98, 'gradient' if th['html'] == 'dark' else 'dark')}</div>
  <button class="hf-top-btn hf-top-btn-search"><ion-icon name="search-outline" style="font-size:22px;color:var(--text)"></ion-icon></button>
</header>

<main class="hf-main">
  <!-- Tab pills (Fan / Vibes / Xplorer) — canonical v5 pattern -->
  <div class="hf-tabs">
    <button class="hf-tab hf-tab-on">
      <ion-icon name="heart" style="font-size:14px;vertical-align:middle;margin-right:4px"></ion-icon>
      Fan
    </button>
    <button class="hf-tab">
      <ion-icon name="happy-outline" style="font-size:14px;vertical-align:middle;margin-right:4px"></ion-icon>
      Vibes
    </button>
    <button class="hf-tab">
      <ion-icon name="compass-outline" style="font-size:14px;vertical-align:middle;margin-right:4px"></ion-icon>
      Xplorer
    </button>
  </div>

  <!-- Peaks & Live horizontal -->
  <h2 class="hf-sec">Peaks &amp; Live</h2>
  <div class="hf-peaks">
    <div class="hf-peak-card hf-peak-live">
      <img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=240&h=400&fit=crop&q=80" alt=""/>
      <span class="hf-live-badge"><span class="hf-live-dot"></span>LIVE</span>
      <span class="hf-peak-name">Sunrise Yoga</span>
    </div>
    <div class="hf-peak-card">
      <img src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=240&h=400&fit=crop&q=80" alt=""/>
      <span class="hf-peak-name">Marc D.</span>
    </div>
    <div class="hf-peak-card">
      <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=240&h=400&fit=crop&q=80" alt=""/>
      <span class="hf-peak-name">Mile run</span>
    </div>
  </div>

  <!-- Suggestions for you -->
  <h2 class="hf-sec">Suggestions pour toi</h2>
  <div class="hf-suggest">
{_sug_card('1438761681033-6461ffad8d80', 'Alex Rossi', 'Digital Art')}
{_sug_card('1507003211169-0a1dd7228f2d', 'Marc Bloom', 'Urban Gardening')}
{_sug_card('1531746020798-e6953c6e8e04', 'Luna Chen', 'Yoga & Mind')}
  </div>

  <!-- Post feed -->
  <h2 class="hf-sec">Ta tribu</h2>

{_post('1494790108377-be9c29b29330', 'Mia Wong', 'Central Park · 2h', '412',
       "Morning flow by the river 🌿 The light was unreal today. <span style='color:var(--mint);font-weight:700'>#yogalife</span>",
       [('photo', '1517836357463-d25dfeac3438')], liked=True)}
{_post('1438761681033-6461ffad8d80', 'Marcus Theron', 'Trail du matin · 4h', '1.2k',
       "Focus on form 🏃 The weather was absolutely perfect today. New PR incoming.",
       [('video', '1441974231531-c6227db76b6e')])}
{_post('1535713875002-d1d0cf377fde', 'Sara Khan', 'Healthy bowl · 6h', '843',
       "Healthy eats to start the week right. Fuel that feels good 🥗",
       [('photo', '1512621776951-a57141f2eefd'), ('photo', '1490645935967-10de6ba17061')])}
{_post('1500648767791-00dcc994a43e', 'Alex Rivera', 'Studio · 8h', '2.4k',
       "Full session recap 💪 swipe → before / after / the grind.",
       [('photo', '1571019614242-c5c5dee9f50b'), ('photo', '1534438327276-14e5300c3a48'), ('video', '1517836357463-d25dfeac3438')])}
</main>

{bottom_nav_canonical('home')}'''


def _im(id_, w, h):
    return f'https://images.unsplash.com/photo-{id_}?w={w}&h={h}&fit=crop&q=80'


def _post_media(items: list) -> str:
    """Canonical multi-media layout logic (founder jun03) :
      1 photo → 4:3 · 1 vidéo → 16:9 + play · 2 photos → côte à côte ·
      3+ ou mixte → carrousel swipable (scroll-snap) + dots + compteur."""
    n = len(items)
    if n == 1:
        kind, id_ = items[0]
        if kind == 'video':
            return (f'<div class="hf-media hf-media-video"><img src="{_im(id_,900,506)}" alt=""/>'
                    f'<span class="hf-media-play"><ion-icon name="play" style="font-size:24px;color:#fff"></ion-icon></span>'
                    f'<span class="hf-media-tag">0:42</span></div>')
        return f'<div class="hf-media"><img class="hf-media-photo" src="{_im(id_,900,700)}" alt=""/></div>'
    if n == 2 and all(k == 'photo' for k, _ in items):
        cells = ''.join(f'<img src="{_im(i,450,560)}" alt=""/>' for _, i in items)
        return f'<div class="hf-media hf-media-duo">{cells}</div>'
    # 3+ OR mixed → horizontal swipable carousel
    slides = ''
    for kind, id_ in items:
        play = ('<span class="hf-media-play"><ion-icon name="play" style="font-size:22px;color:#fff"></ion-icon></span>'
                if kind == 'video' else '')
        slides += f'<div class="hf-slide"><img src="{_im(id_,820,700)}" alt=""/>{play}</div>'
    dots = ''.join(f'<span class="hf-dot{" hf-dot-on" if i == 0 else ""}"></span>' for i in range(n))
    return (f'<div class="hf-media hf-media-carousel"><div class="hf-track">{slides}</div>'
            f'<span class="hf-media-count">1/{n}</span></div><div class="hf-dots">{dots}</div>')


def _post(avatar_id: str, name: str, sub: str, likes: str, caption: str,
          media: list, liked: bool = False) -> str:
    """Canonical feed post — header · légende · média (layout auto) · cœur/partage/save (NO comments #7)."""
    heart = ('<ion-icon name="heart" style="font-size:21px;color:#FF4658"></ion-icon>' if liked
             else '<ion-icon name="heart-outline" style="font-size:21px"></ion-icon>')
    return f'''  <article class="hf-post">
    <div class="hf-post-head">
      <img src="{_im(avatar_id,120,120)}" alt="" class="hf-post-avatar"/>
      <div class="hf-post-meta">
        <div class="hf-post-name">{name}
          <ion-icon name="checkmark-circle" style="font-size:12px;color:var(--mint);vertical-align:middle"></ion-icon>
        </div>
        <div class="hf-post-sub">{sub}</div>
      </div>
      <button class="hf-post-more"><ion-icon name="ellipsis-horizontal" style="font-size:18px;color:var(--sub)"></ion-icon></button>
    </div>
    <p class="hf-post-caption">{caption}</p>
    {_post_media(media)}
    <div class="hf-post-actions">
      <button class="hf-post-action">{heart}<span>{likes}</span></button>
      <button class="hf-post-action"><ion-icon name="paper-plane-outline" style="font-size:21px"></ion-icon></button>
      <button class="hf-post-action" style="margin-left:auto"><ion-icon name="bookmark-outline" style="font-size:21px"></ion-icon></button>
    </div>
  </article>'''


def _sug_card(avatar_id: str, name: str, role: str) -> str:
    """Canonical creator card — IDENTIQUE à la card search Suggested creators (avatar+nom+rôle+Devenir fan)."""
    return f'''    <div class="hf-sug-card">
      <img src="{_im(avatar_id,160,160)}" alt=""/>
      <div class="hf-sug-name">{name}<ion-icon name="checkmark-circle" style="font-size:12px;color:var(--mint);vertical-align:middle;margin-left:3px"></ion-icon></div>
      <div class="hf-sug-role">{role}</div>
      <button class="hf-sug-fan">Devenir fan</button>
    </div>'''


SCREENS = {
    'home_feed_v2': ('Home Feed (canonical)', screen_home_fan),
}


_HOME_CSS = """
<style>
  /* Home topbar */
  /* jun03 canonical : notif LEFT · Smuppy CENTER · search RIGHT */
  .hf-topbar { position:absolute; top:0; left:0; right:0; z-index:10;
    height:54px; padding:0 14px;
    display:grid; grid-template-columns:40px 1fr 40px; align-items:center;
    background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%);
    border-bottom:1px solid var(--border); }
  .hf-brand { display:flex; align-items:center; justify-content:center;
    filter:drop-shadow(0 0 12px rgba(51,160,137,0.25)); }
  .smuppy-full { display:inline-flex; align-items:center; gap:7px; }
  .smuppy-full svg { display:block; }
  .hf-top-btn-search { justify-self:end; }
  .hf-top-actions { display:flex; gap:6px; }
  .hf-top-btn { position:relative; width:38px; height:38px; border:none; background:transparent;
    border-radius:999px; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .hf-top-badge { position:absolute; top:4px; right:4px;
    width:16px; height:16px; border-radius:999px;
    background:#FF4658; color:#fff;
    font-size:9px; font-weight:900;
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 6px rgba(255,70,88,.55); }

  .hf-main { padding:62px 0 92px; height:100%; overflow-y:auto; }

  /* Tab pills v5 canonical */
  .hf-tabs { display:grid; grid-template-columns:1fr 1fr 1fr; gap:4px;
    margin:6px 16px 18px; padding:4px;
    background:var(--input-bg); border:1px solid var(--input-border);
    border-radius:999px; }
  .hf-tab { padding:10px 0; border:none; border-radius:999px;
    background:transparent; color:var(--sub);
    font-family:inherit; font-size:13px; font-weight:700;
    cursor:pointer; transition:.18s ease;
    display:inline-flex; align-items:center; justify-content:center; }
  .hf-tab-on { background:var(--card); color:var(--mint);
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 0 0 1px rgba(51,160,137,0.225),
               0 2px 8px rgba(0,0,0,0.10); }

  /* Section header */
  .hf-sec { font-size:18px; font-weight:800; color:var(--text);
    letter-spacing:-.02em; padding:0 16px; margin:0 0 12px; }

  /* Peaks & Live horizontal */
  .hf-peaks { display:flex; gap:11px; padding:7px 16px 18px;
    overflow-x:auto; scrollbar-width:none; }
  .hf-peaks::-webkit-scrollbar { display:none; }
  /* CANONICAL peak/live thumbnail card — aspect 3/4 · radius 20 · width 132 (identique partout) */
  .hf-peak-card { position:relative; flex-shrink:0;
    width:132px; aspect-ratio:3/4; border-radius:20px;
    overflow:hidden; cursor:pointer;
    box-shadow:0 4px 16px rgba(0,0,0,0.25); }
  .hf-peak-card img { width:100%; height:100%; object-fit:cover; }
  /* live en cours → contour rouge clignotant */
  .hf-peak-live { animation:hf-live-pulse 1.4s ease-in-out infinite; }
  @keyframes hf-live-pulse {
    0%,100% { box-shadow:0 0 0 2.5px #FF4658, 0 0 14px 2px rgba(255,70,88,.55); }
    50%     { box-shadow:0 0 0 2.5px rgba(255,70,88,.35), 0 0 4px 1px rgba(255,70,88,.15); } }
  .hf-live-badge { position:absolute; top:8px; left:8px;
    display:flex; align-items:center; gap:4px;
    padding:3px 8px; border-radius:999px;
    background:#FF4658; color:#fff;
    font-size:9px; font-weight:900; letter-spacing:.06em;
    box-shadow:0 2px 8px rgba(255,70,88,.50); }
  .hf-live-dot { width:5px; height:5px; border-radius:999px; background:#fff;
    animation:hf-pulse 1.5s infinite; }
  @keyframes hf-pulse { 50% { opacity:.4; } }
  .hf-peak-name { position:absolute; bottom:10px; left:11px; right:11px;
    color:#fff; font-size:12px; font-weight:700;
    text-shadow:0 2px 4px rgba(0,0,0,.6); }

  /* Suggestions */
  .hf-suggest { display:flex; gap:10px; padding:0 16px 18px;
    overflow-x:auto; scrollbar-width:none; }
  .hf-suggest::-webkit-scrollbar { display:none; }
  /* CANONICAL creator card — dimensions IDENTIQUES au search (.sr-cr) */
  .hf-sug-card { display:flex; flex-direction:column; align-items:center; gap:7px;
    flex-shrink:0; width:160px; padding:16px 12px;
    background:var(--card); border:1px solid var(--border);
    border-radius:20px; }
  .hf-sug-card img { width:56px; height:56px; border-radius:999px; object-fit:cover; }
  .hf-sug-name { font-size:13px; font-weight:800; color:var(--text);
    text-align:center;
    display:flex; align-items:center; justify-content:center; }
  .hf-sug-role { font-size:11px; font-weight:500; color:var(--sub);
    text-align:center; }
  .hf-sug-fan { width:100%; margin-top:2px; padding:8px 0;
    border:none; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi), var(--mint-deep)); color:#fff;
    font-family:inherit; font-size:12.5px; font-weight:700;
    cursor:pointer; }

  /* Posts feed */
  /* jun03 canonical post : CARTE (bg+bordure) · header · légende · média arrondi inset · actions */
  .hf-post { margin:0 16px 16px; background:var(--card);
    border:1px solid var(--border); border-radius:20px; overflow:hidden;
    box-shadow:0 4px 18px rgba(0,0,0,0.18); }
  .hf-post-head { display:flex; align-items:center; gap:10px;
    padding:12px 14px 8px; }
  .hf-post-avatar { width:38px; height:38px; border-radius:999px; object-fit:cover; }
  .hf-post-meta { flex:1; }
  .hf-post-name { font-size:14px; font-weight:800; color:var(--text);
    display:flex; align-items:center; gap:4px; }
  .hf-post-sub { font-size:11.5px; font-weight:500; color:var(--sub); margin-top:1px; }
  .hf-post-more { width:32px; height:32px; border:none; background:transparent;
    cursor:pointer; display:flex; align-items:center; justify-content:center; }
  .hf-post-caption { padding:0 14px 10px; font-size:13px; font-weight:500;
    color:var(--text); line-height:1.45; }
  /* canonical multi-media layouts (founder jun03) */
  .hf-media { position:relative; margin:0 14px; border-radius:14px; overflow:hidden; }
  .hf-media-photo { display:block; width:100%; aspect-ratio:4/3; object-fit:cover; }
  .hf-media-video img { display:block; width:100%; aspect-ratio:16/9; object-fit:cover; }
  .hf-media-play { position:absolute; inset:0; margin:auto; width:52px; height:52px; border-radius:999px;
    background:rgba(0,0,0,.45); -webkit-backdrop-filter:blur(6px); backdrop-filter:blur(6px);
    display:flex; align-items:center; justify-content:center; }
  .hf-media-tag { position:absolute; bottom:8px; right:8px; padding:2px 7px; border-radius:6px;
    background:rgba(0,0,0,.55); color:#fff; font-size:11px; font-weight:700; }
  .hf-media-duo { display:grid; grid-template-columns:1fr 1fr; gap:3px; }
  .hf-media-duo img { width:100%; aspect-ratio:3/4; object-fit:cover; display:block; }
  .hf-media-carousel .hf-track { display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:3px; }
  .hf-media-carousel .hf-track::-webkit-scrollbar { display:none; }
  .hf-slide { position:relative; flex:0 0 100%; scroll-snap-align:center; }
  .hf-slide img { width:100%; aspect-ratio:4/3; object-fit:cover; display:block; }
  .hf-media-count { position:absolute; top:8px; right:8px; padding:2px 9px; border-radius:999px;
    background:rgba(0,0,0,.55); color:#fff; font-size:11px; font-weight:700; }
  .hf-dots { display:flex; justify-content:center; gap:5px; padding:9px 0 2px; }
  .hf-dot { width:6px; height:6px; border-radius:999px; background:var(--input-border); }
  .hf-dot-on { background:var(--mint); width:7px; height:7px; }
  .hf-post-media { display:block; width:calc(100% - 28px); margin:0 14px;
    aspect-ratio:4/3; object-fit:cover; border-radius:14px; }
  .hf-post-actions { display:flex; align-items:center; gap:16px;
    padding:11px 16px 13px; }
  .hf-post-action { display:flex; align-items:center; gap:5px;
    border:none; background:transparent; cursor:pointer;
    color:var(--text); font-family:inherit; font-size:13px; font-weight:700; }

  /* Bottom nav canonical — DEPRECATED .hf-bnav classes (kept commented for any
     stale markup). Real bottom nav is rendered via shared canonical_bnav helper
     which emits .cn-bnav* classes; styles are appended below from CANONICAL_BNAV_CSS. */
</style>
""" + CANONICAL_BNAV_CSS


def build(key, dark):
    th = theme(dark)
    title, fn = SCREENS[key]
    body = fn(th)
    auth_full = auth_build_fn('auth_welcome_v2', dark)
    head_end = auth_full.index('</style>') + len('</style>')
    head = auth_full[:head_end].replace('Smuppy V2 — Welcome', f'Smuppy V2 — {title}')
    return head + _P1_CSS + '\n' + _HOME_CSS + '\n</head><body>\n' + body + '\n</body></html>'


def write_all():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for key in SCREENS:
        for dark in (True, False):
            t = 'dark' if dark else 'light'
            d = OUT_DIR / f'{key}_{t}'
            d.mkdir(parents=True, exist_ok=True)
            (d / 'code.html').write_text(build(key, dark))
    print(f'  built {len(SCREENS)*2} home maquettes')


if __name__ == '__main__':
    write_all()
