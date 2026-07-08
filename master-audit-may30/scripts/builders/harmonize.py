#!/usr/bin/env python3
"""
Harmonize Smuppy V2 Stitch sources : extract the canonical bottomnav + tailwind config
from home_feed_light/code.html and inject into every other source.

- Sources stay untouched in ~/Downloads
- Harmonized mirrors written to /tmp/smuppy-v2-recovery/maquettes/harmonized/<feature>/code.html
- Active state in the bottomnav adapted per feature (home/profile/message)
"""
import re
import shutil
from pathlib import Path

ROOT = Path('/tmp/smuppy-v2-recovery/maquettes')
SOURCES = ROOT / 'sources'
OUT = ROOT / 'harmonized'
OUT.mkdir(parents=True, exist_ok=True)

# 1. Read canonical home_feed_light source
canon_path = SOURCES / 'v2_canonical' / 'home_feed_light' / 'code.html'
canon = canon_path.read_text()

# 2. Extract canonical tailwind config
m_tw = re.search(r'<script id="tailwind-config">.*?</script>', canon, re.DOTALL)
canonical_tailwind = m_tw.group(0) if m_tw else ''

# 3. Extract canonical inline <style> (the one with pill-active-light, glow, etc.)
m_style = re.search(r'<style>\s*\.no-scrollbar.*?</style>', canon, re.DOTALL)
canonical_style = m_style.group(0) if m_style else ''

# 4. Extract canonical <nav class="fixed bottom-0 ...">...</nav>
m_nav = re.search(r'<!--\s*BottomNavBar\s*-->\s*<nav class="fixed bottom-0[^>]*>.*?</nav>', canon, re.DOTALL)
canonical_nav = m_nav.group(0) if m_nav else ''

# Fallback nav extraction (without comment)
if not canonical_nav:
    m_nav = re.search(r'<nav class="fixed bottom-0[^"]*"[^>]*>.*?</nav>', canon, re.DOTALL)
    canonical_nav = m_nav.group(0) if m_nav else ''

# 5. Extract scroll-hide CSS+JS block at bottom
m_scroll = re.search(r'<style>\s*\.scroll-hide-top.*?</script>', canon, re.DOTALL)
canonical_scroll_behavior = m_scroll.group(0) if m_scroll else ''

assert canonical_tailwind, 'Canonical tailwind config not found'
assert canonical_nav, 'Canonical bottomnav not found'

# 6. Feature → active tab mapping
# Active tabs available: home, peaks, plus, message, profile
ACTIVE_MAP = {
    # Home Feed
    'home_feed_light': 'home',
    'home_feed_dark': 'home',
    # Profile (visitor / private / owner / creator)
    'profile_visitor_light': 'profile',
    'profile_visitor_dark': 'profile',
    'profile_private_light': 'profile',
    'profile_private_dark': 'profile',
    'profile_owner_dark': 'profile',
    'profile_visitor_final_light_nav_updated': 'profile',
    'profile_visitor_final_dark_standardized': 'profile',
    'profile_private_final_light_nav_updated': 'profile',
    'profile_private_final_dark_standardized': 'profile',
    'profile_owner_hierarchical_nav_dark': 'profile',
    'creator_profile_light_mode': 'profile',
    'creator_profile_light_mode_dark': 'profile',
    'creator_profile_minimal': 'profile',
    'creator_profile_minimal_dark': 'profile',
    'creator_profile_minimal_rich': 'profile',
    'creator_profile_dark_mode': 'profile',
    'edit_profile_minimalist': 'profile',
    'edit_profile_minimalist_dark': 'profile',
    'edit_expertise_minimalist': 'profile',
    'edit_expertise_minimalist_dark': 'profile',
    # Settings
    'settings_definitive': 'profile',
    'settings_definitive_dark': 'profile',
    'settings_minimalist_1': 'profile',
    'settings_minimalist_2': 'profile',
    'settings_minimalist_dark_18': 'profile',
    'settings_minimalist_dark_223': 'profile',
    'notification_settings_minimalist': 'profile',
    'notification_settings_minimalist_dark': 'profile',
    # DM
    'dm_chat_minimal': 'message',
    'dm_chat_minimal_dark': 'message',
    'dm_chat_light_mode': 'message',
    'dm_chat_dark_mode': 'message',
    'dm_chat_light_mode_dark': 'message',
    # Discover
    'discover_minimal': 'home',
    'discover_minimal_dark': 'home',
    'discover_dark_mode': 'home',
    'discover_smuppy_social': 'home',
    'discover_smuppy_social_dark': 'home',
    # Find Friends
    'find_friends': 'home',
    'find_friends_dark': 'home',
    # Peak Editor (Create flow)
    'peak_editor_minimal_soft': 'plus',
    # Subscribe / Channel / Paywall — these are overlays/bottom sheets — keep home active
    'channel_subscribe_minimal': 'home',
    'channel_subscribe_minimal_dark': 'home',
    'channel_subscribe_minimal_rich': 'home',
    'channel_subscribe_smuppy_social': 'home',
    'creator_paywall_light_mode': 'home',
    'creator_paywall_light_mode_dark': 'home',
    'creator_paywall_dark_mode': 'home',
    # Booking
    'booking_confirmation': 'profile',
    'booking_confirmation_dark': 'profile',
    # Other home variants
    'home_feed_dark_mode': 'home',
    'home_feed_enhanced_dark': 'home',
    'home_feed_enhanced_minimal_soft': 'home',
    'home_feed_enhanced_light': 'home',
    'home_feed_final_evolution': 'home',
    'home_feed_final_evolution_dark': 'home',
    'home_feed_minimal': 'home',
    'home_feed_smuppy_social': 'home',
    # Smuppy Vibes
    'smuppy_vibes': 'home',
    'smuppy_vibes_dark': 'home',
    'smuppy_social': 'home',
    'smuppy_social_dark': 'home',
    'smuppy_minimal_soft': 'home',
    'smuppy_minimal_soft_1': 'home',
    'smuppy_minimal_soft_2': 'home',
}


def adapt_nav_active(nav_html: str, active: str) -> str:
    """Rewrite the canonical nav so the requested tab is the active one (mint glow + active-bar).

    The canonical nav has button order : home / peaks / plus(pill) / message / profile.
    Active class on home = `icon-active-glow` + nested `<div class="active-bar">`.
    Inactive buttons just have `flex items-center justify-center w-12 h-12`.
    The plus button keeps `pill-active-light` regardless (it's the create CTA).
    """
    # Parse the 5 buttons in order
    btn_pattern = re.compile(r'<button[^>]*>.*?</button>', re.DOTALL)
    buttons = btn_pattern.findall(nav_html)
    if len(buttons) != 5:
        return nav_html  # safety

    # Mapping: index 0=home, 1=peaks, 2=plus(pill), 3=message, 4=profile
    target_idx = {'home': 0, 'peaks': 1, 'plus': 2, 'message': 3, 'profile': 4}.get(active, 0)

    new_buttons = []
    for i, btn in enumerate(buttons):
        if i == 2:
            # The plus pill stays as-is
            new_buttons.append(btn)
            continue

        # Strip existing active markers (icon-active-glow, active-bar div, profile-avatar-active class)
        clean = btn
        clean = re.sub(r'\s+icon-active-glow', '', clean)
        clean = re.sub(r'<div class="active-bar"></div>', '', clean)
        clean = clean.replace('profile-avatar-active', 'profile-avatar-inactive')

        # Recolor SVG strokes/fills back to slate-400/500 for inactive
        if i != 4:  # not the avatar
            clean = clean.replace('fill="#33A089"', 'fill="#94a3b8"')
            clean = clean.replace('stroke="#33A089"', 'stroke="#94a3b8"')

        if i == target_idx:
            # Apply active state
            if i == 4:
                # Profile = swap inactive avatar class for active
                clean = clean.replace('profile-avatar-inactive', 'profile-avatar-active')
                clean = clean.replace('opacity-70', '')
            else:
                # Add icon-active-glow + active-bar
                clean = re.sub(r'class="(relative\s+)?flex items-center justify-center w-12 h-12',
                               r'class="relative flex items-center justify-center w-12 h-12 icon-active-glow', clean, count=1)
                # Recolor the SVG to mint
                clean = clean.replace('fill="#94a3b8"', 'fill="#33A089"')
                clean = clean.replace('stroke="#94a3b8"', 'stroke="#33A089"')
                # Append active-bar div before </button>
                clean = clean.rsplit('</button>', 1)
                clean = clean[0] + '<div class="active-bar"></div></button>' + (clean[1] if len(clean) > 1 else '')

        new_buttons.append(clean)

    # Reassemble : reconstruct the nav with the same opening tag
    nav_open = re.match(r'(<!--\s*BottomNavBar\s*-->\s*)?<nav[^>]*>', nav_html)
    open_tag = nav_open.group(0) if nav_open else '<nav>'
    return open_tag + '\n' + '\n'.join(new_buttons) + '\n</nav>'


def harmonize(src: Path, feature_name: str, active_tab: str) -> str:
    """Return harmonized HTML for a source code.html."""
    html = src.read_text()

    # 1. Replace tailwind config (or insert if missing)
    if '<script id="tailwind-config">' in html:
        html = re.sub(r'<script id="tailwind-config">.*?</script>',
                      lambda m: canonical_tailwind, html, count=1, flags=re.DOTALL)
    else:
        # Insert before </head>
        html = html.replace('</head>', canonical_tailwind + '\n</head>', 1)

    # 2. Ensure canonical style block is present (idempotent — only add if missing markers)
    if 'pill-active-light' not in html:
        html = html.replace('</head>', canonical_style + '\n</head>', 1)

    # 3. Replace bottomnav (or insert before </body> if missing)
    adapted_nav = adapt_nav_active(canonical_nav, active_tab)
    existing_nav = re.search(r'<nav class="fixed bottom-0[^"]*"[^>]*>.*?</nav>', html, re.DOTALL)
    if existing_nav:
        html = html[:existing_nav.start()] + adapted_nav + html[existing_nav.end():]
    else:
        html = html.replace('</body>', adapted_nav + '\n</body>', 1)

    # 4. Ensure scroll-hide behavior is present (so the bottomnav hides on scroll, like home)
    if 'scroll-hide-top' not in html and canonical_scroll_behavior:
        html = html.replace('</body>', canonical_scroll_behavior + '\n</body>', 1)

    # 5. Ensure body has padding-bottom to clear the fixed nav
    html = re.sub(r'<body class="([^"]*?)"', lambda m: f'<body class="{m.group(1)}{" pb-24" if "pb-24" not in m.group(1) else ""}"', html, count=1)
    # If no class attr
    if not re.search(r'<body class="', html):
        html = html.replace('<body>', '<body class="pb-24">', 1)

    return html


# Discover all sources to harmonize
all_sources = []
for sym in SOURCES.iterdir():
    if sym.is_symlink() or sym.is_dir():
        real = sym.resolve()
        # Look one level deep for screen directories
        for sd in real.iterdir():
            if sd.is_dir() and (sd / 'code.html').exists():
                all_sources.append((sym.name, sd.name, sd / 'code.html'))

# Deduplicate by feature_name (prefer v2_canonical > stitch_v0 > stitch_v2)
priority = {'v2_canonical': 0, 'stitch_v0': 1, 'stitch_v2': 2}
by_feature = {}
for sym_name, feature, path in all_sources:
    p = priority.get(sym_name, 99)
    if feature not in by_feature or by_feature[feature][0] > p:
        by_feature[feature] = (p, sym_name, path)

results = {'ok': [], 'skipped': []}
for feature, (_, sym_name, src_path) in sorted(by_feature.items()):
    active = ACTIVE_MAP.get(feature, 'home')
    try:
        out_html = harmonize(src_path, feature, active)
        out_dir = OUT / feature
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / 'code.html').write_text(out_html)
        # Copy screen.png if it exists
        png = src_path.parent / 'screen.png'
        if png.exists():
            shutil.copy(png, out_dir / 'screen.png')
        results['ok'].append((feature, sym_name, active))
    except Exception as e:
        results['skipped'].append((feature, str(e)))

print(f"Harmonized: {len(results['ok'])} features")
print(f"Skipped:    {len(results['skipped'])}")
for f, sn, a in sorted(results['ok']):
    print(f"  {f:50s}  active={a}  src={sn}")
if results['skipped']:
    print('\nSKIPPED:')
    for f, e in results['skipped']:
        print(f"  {f}: {e}")
