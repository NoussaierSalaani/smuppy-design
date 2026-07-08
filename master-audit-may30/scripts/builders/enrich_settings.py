#!/usr/bin/env python3
"""
Enrich the harmonized settings_definitive light + dark mockups with the REAL
30+ items from src/screens/settings/SettingsScreen.tsx.

We keep the existing Stitch design system :
- Material Symbols Outlined icons (mint #33A089 primary color)
- Section headers with .font-label-caps + .text-outline
- Bordered button rows (.border-t .border-surface-variant/20)
- Back arrow header on top (already injected by harmonize.py)

We REPLACE the body content between the existing <main> opening and the destructive bottom
(logout / delete) block.
"""
import re
from pathlib import Path

HARMONIZED = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')

# Real items from /Users/noussaier/smuppy-mobile/src/screens/settings/SettingsScreen.tsx
# Mapped to Material Symbols equivalents of the Ionicons
SECTIONS = [
    {
        'title': 'Account',
        'items': [
            ('person',          'Edit Profile'),
            ('favorite',        'Interests'),
            ('school',          'Expertise'),
            ('storefront',      'Business Category'),
            ('lock',            'Change Password'),
            ('payments',        'Channel Setup'),
            ('star',            'Upgrade to Pro'),
        ],
    },
    {
        'title': 'Preferences',
        'items': [
            ('notifications',   'Notifications'),
            ('person_add',      'Follow Requests'),
            ('group',           'Find Friends'),
            ('account_balance_wallet', 'Smup Wallet'),
            ('credit_card',     'Manage Subscription'),
            ('subscriptions',   'My Subscriptions'),
            ('analytics',       'Business Dashboard'),
        ],
    },
    {
        'title': 'Visibility',
        'items': [
            ('lock_open',       'Account Visibility'),
            ('contrast',        'Theme'),
            ('language',        'Language'),
        ],
    },
    {
        'title': 'Support & Legal',
        'items': [
            ('help',            'Help'),
            ('shield',          'Privacy Settings'),
            ('block',           'Blocked Users'),
            ('volume_off',      'Muted Users'),
            ('flag',            'Dispute Center'),
            ('report',          'Report a Problem'),
            ('download',        'Export My Data'),
            ('description',     'Terms & Policies'),
        ],
    },
]


def build_section(title: str, items: list, dark: bool) -> str:
    """Build a section with header + bordered buttons."""
    section_header_color = 'text-slate-400' if dark else 'text-slate-500'
    surface_bg = 'bg-slate-800' if dark else 'bg-white'
    border = 'border-slate-700/40' if dark else 'border-slate-100'
    hover = 'hover:bg-slate-700/30' if dark else 'hover:bg-slate-50'
    label_color = 'text-slate-100' if dark else 'text-slate-900'
    chevron_color = 'text-slate-500' if dark else 'text-slate-400'

    out = [f'''
<div class="px-4 mt-6">
  <h3 class="text-[11px] font-bold uppercase tracking-wider {section_header_color} px-2 mb-2">{title}</h3>
  <div class="{surface_bg} rounded-2xl overflow-hidden shadow-sm">''']

    for i, (icon, label) in enumerate(items):
        border_class = f'border-t {border}' if i > 0 else ''
        out.append(f'''
    <button class="w-full flex items-center justify-between px-4 py-3.5 {hover} active:scale-[0.99] transition-all {border_class}">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-full flex items-center justify-center" style="background: rgba(51,160,137,0.1);">
          <span class="material-symbols-outlined text-[20px]" style="color:#33A089;font-variation-settings:'wght' 400;">{icon}</span>
        </div>
        <span class="text-[15px] font-medium {label_color}">{label}</span>
      </div>
      <span class="material-symbols-outlined text-[20px] {chevron_color}">chevron_right</span>
    </button>''')

    out.append('  </div>\n</div>')
    return ''.join(out)


def build_destructive_block(dark: bool) -> str:
    """Logout + Delete account block at the bottom."""
    return '''
<div class="px-4 mt-8 mb-12 space-y-3">
  <button class="w-full flex items-center justify-center gap-2 px-4 py-3.5 rounded-2xl font-semibold text-[15px]"
          style="background: rgba(220,38,38,0.10); color: #DC2626;">
    <span class="material-symbols-outlined text-[20px]">logout</span>
    <span>Log Out</span>
  </button>
  <button class="w-full flex items-center justify-center gap-2 px-4 py-3.5 rounded-2xl font-semibold text-[15px]"
          style="background: rgba(220,38,38,0.05); color: #DC2626; border: 1px solid rgba(220,38,38,0.2);">
    <span class="material-symbols-outlined text-[20px]">delete</span>
    <span>Delete Account</span>
  </button>
  <p class="text-[11px] text-center text-slate-400 mt-3">Smuppy V2 · Version 1.0.1</p>
</div>'''


def build_profile_card(dark: bool) -> str:
    """Top profile card with avatar + name + email + edit button."""
    bg = 'bg-slate-800' if dark else 'bg-white'
    text_primary = 'text-slate-100' if dark else 'text-slate-900'
    text_sub = 'text-slate-400' if dark else 'text-slate-500'

    return f'''
<div class="px-4 pt-2">
  <div class="{bg} rounded-2xl p-5 flex items-center gap-4 shadow-sm">
    <div class="relative">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop"
           class="w-14 h-14 rounded-full object-cover"
           style="box-shadow: 0 0 0 2px rgba(51,160,137,0.25);" alt="Profile" />
      <div class="absolute -bottom-0.5 -right-0.5 w-5 h-5 rounded-full flex items-center justify-center"
           style="background:#33A089;border: 2px solid {('#1E293B' if dark else '#fff')};">
        <span class="material-symbols-outlined text-white text-[12px]">edit</span>
      </div>
    </div>
    <div class="flex-1 min-w-0">
      <h2 class="text-[17px] font-bold {text_primary} truncate">Clara Montgomery</h2>
      <p class="text-[13px] {text_sub} truncate">clara.montgomery@example.com</p>
    </div>
    <button class="px-3 py-1.5 rounded-full text-[12px] font-bold text-white"
            style="background: linear-gradient(135deg, #33A089 0%, #1ABC9C 100%);">
      Pro
    </button>
  </div>
</div>'''


def enrich(src_path: Path, out_path: Path, dark: bool):
    html = src_path.read_text()

    # Build the full enriched body content
    body = build_profile_card(dark)
    for sec in SECTIONS:
        body += build_section(sec['title'], sec['items'], dark)
    body += build_destructive_block(dark)

    # Wrap in <main>
    bg_outer = 'bg-slate-900' if dark else 'bg-slate-50'
    enriched_main = f'<main class="pt-14 pb-8 min-h-screen {bg_outer}">{body}</main>'

    # Replace the existing <main>...</main> (or <header>...</header><main>...) up to before the destructive section.
    # Find <main ...> ... and the last </main> before destructive logout block.
    # Simpler approach : strip everything between </header> and </body>, keep <header> (back arrow) and <body> wrapper.

    # 1. Find the back-arrow header
    header_match = re.search(r'<!-- BACK ARROW HEADER[^>]*-->\s*<header[^>]*>.*?</header>', html, re.DOTALL)
    if not header_match:
        # Fallback: take any first <header>
        header_match = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL)

    if not header_match:
        raise RuntimeError(f'No back-arrow header found in {src_path}')

    back_header = header_match.group(0)

    # 2. Extract the <head>...</head> + <body class="...">  opening (preserve all the canonical styles & scripts)
    head_close = html.find('</head>')
    body_open_match = re.search(r'<body[^>]*>', html)
    if head_close == -1 or not body_open_match:
        raise RuntimeError('Malformed HTML')

    pre_body = html[:body_open_match.end()]

    # 3. Compose new body : back header + enriched main + closing tags
    closing = '</body></html>'
    new_html = pre_body + '\n' + back_header + '\n' + enriched_main + '\n' + closing

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(new_html)
    return out_path


for variant in ['settings_definitive', 'settings_definitive_dark']:
    dark = variant.endswith('_dark')
    src = HARMONIZED / variant / 'code.html'
    out = HARMONIZED / variant / 'code.html'  # overwrite
    if src.exists():
        result = enrich(src, out, dark)
        print(f"✓ Enriched: {result}")
    else:
        print(f"✗ Missing: {src}")
