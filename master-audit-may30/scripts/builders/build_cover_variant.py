#!/usr/bin/env python3
"""
Build profile_visitor_cover_{light,dark} matching the Stitch screenshot:
- Cover photo 240px (top app bar OVERLAID: back / "Smuppy" / message)
- Avatar (ring mint thick) at LEFT, overlapping cover bottom by 50%
- Follow pill + message icon on same line at RIGHT of avatar
- Name + bio + stats LEFT-aligned (NOT centered)
- Preserve canonical tabs + grid + bottomnav
"""
import re
from pathlib import Path

HARMONIZED = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')


def get_new_block(dark: bool) -> str:
    if dark:
        page_bg = '#0f172a'
        text_main = '#f1f5f9'
        text_sub = '#94a3b8'
        ring_bg = '#0f172a'
        msg_border = '#334155'
        msg_stroke = '#cbd5e1'
    else:
        page_bg = '#ffffff'
        text_main = '#0f172a'
        text_sub = '#64748b'
        ring_bg = '#ffffff'
        msg_border = '#e2e8f0'
        msg_stroke = '#475569'

    return f'''
<!-- =========================================================== -->
<!-- COVER HEADER (replaces hero unique photo)                    -->
<!-- =========================================================== -->
<header class="cover-header relative w-full" style="background:{page_bg};">
  <!-- Cover photo, full-bleed -->
  <div class="cover-bg relative w-full overflow-hidden" style="height: 240px;">
    <img alt="Cover" loading="lazy"
         src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=900&h=600&fit=crop"
         class="absolute inset-0 w-full h-full object-cover"/>
    <!-- subtle bottom gradient for app-bar legibility -->
    <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(0,0,0,0.25) 0%, transparent 30%, transparent 70%, rgba(0,0,0,0.10) 100%);"></div>

    <!-- Top app bar over the cover -->
    <div class="absolute top-0 inset-x-0 flex items-center justify-between px-4 pt-12">
      <button class="cover-btn-circle" aria-label="Back">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0E1116" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <div class="text-white font-extrabold text-[20px] tracking-tight" style="text-shadow: 0 1px 2px rgba(0,0,0,0.3);">Smuppy</div>
      <button class="cover-btn-circle" aria-label="Message">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0E1116" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
      </button>
    </div>
  </div>

  <!-- Avatar + Follow row, overlap cover bottom -->
  <div class="px-5 flex items-end gap-3" style="margin-top: -40px; padding-bottom: 14px;">
    <!-- Avatar with thick mint ring -->
    <div class="avatar-ring-thick" style="padding: 4px; border-radius: 9999px; background: linear-gradient(135deg, #33A089, #1ABC9C); flex-shrink: 0; box-shadow: 0 0 0 4px {ring_bg}, 0 6px 20px rgba(0,0,0,0.15);">
      <img alt="Sara Khan" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop"
           class="block rounded-full object-cover"
           style="width: 80px; height: 80px;"/>
    </div>
    <!-- spacer pushes the actions to the right -->
    <div class="flex-1"></div>
    <!-- Follow pill -->
    <button class="follow-pill" style="background: linear-gradient(135deg, #33A089 0%, #1ABC9C 100%); color: #fff; padding: 9px 22px; border-radius: 9999px; font-weight: 700; font-size: 14px; box-shadow: 0 4px 14px rgba(51,160,137,0.175); border: none; cursor: pointer; align-self: flex-end; margin-bottom: 4px;">
      Follow
    </button>
    <!-- Message icon round -->
    <button class="msg-icon-btn" aria-label="Message" style="width: 38px; height: 38px; border-radius: 9999px; background: transparent; border: 1.5px solid {msg_border}; display: flex; align-items: center; justify-content: center; align-self: flex-end; margin-bottom: 4px; cursor: pointer;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{msg_stroke}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
    </button>
  </div>

  <!-- Identity block (LEFT-aligned) -->
  <div class="px-5 mb-3">
    <h1 class="font-bold text-[20px] leading-tight" style="color:{text_main};">Sara Khan</h1>
    <p class="text-[13px] mt-0.5" style="color:{text_sub};">Yoga coach · Montreal · Daily flows 🌿</p>
  </div>

  <!-- Stats row, LEFT-aligned, stacked number+label -->
  <div class="px-5 flex items-center gap-6 mb-5">
    <div class="flex items-baseline gap-1.5">
      <span class="text-[15px] font-bold" style="color:{text_main};">24.3K</span>
      <span class="text-[12px]" style="color:{text_sub};">Followers</span>
    </div>
    <div class="flex items-baseline gap-1.5">
      <span class="text-[15px] font-bold" style="color:{text_main};">412</span>
      <span class="text-[12px]" style="color:{text_sub};">Posts</span>
    </div>
    <div class="flex items-baseline gap-1.5">
      <span class="text-[15px] font-bold" style="color:{text_main};">89</span>
      <span class="text-[12px]" style="color:{text_sub};">Peaks</span>
    </div>
  </div>
</header>
<style>
  .cover-btn-circle {{ width: 36px; height: 36px; border-radius: 9999px; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.10); }}
  .cover-btn-circle:active {{ transform: scale(0.95); }}
  .avatar-ring-thick:hover img {{ filter: brightness(1.04); }}
  .follow-pill:active {{ transform: scale(0.97); }}
</style>
'''


def build_variant(src: Path, out: Path, dark: bool = False):
    html = src.read_text()

    # Splice strategy :
    # 1. Remove the <section class="hero">...</section>
    # 2. Inside the <main class="...">: remove from grabber pill through stats div (everything before TOP TABS comment)
    # 3. Insert new cover header BEFORE <main>
    # 4. Adjust <main> to remove negative margin + rounded top (no longer overlapping)

    # Remove old hero section
    html = re.sub(r'<section class="hero"[^>]*>.*?</section>', '', html, count=1, flags=re.DOTALL)

    # Strip the <main>'s content from its opening up to the TOP TABS comment
    # The grabber + name + bio + chip + buttons + caption + stats — all gone.
    pattern = re.compile(
        r'(<main[^>]*>)(.*?)(<!-- TOP TABS)',
        re.DOTALL
    )
    if not pattern.search(html):
        raise RuntimeError('Could not find main+TOP TABS to splice')

    # Replace : keep main opening (but rewrite class to remove -mt-8 + rounded-t-[32px]),
    # then re-insert just the TOP TABS marker.
    def rewrite_main(m):
        main_open = m.group(1)
        # Rewrite the main class : drop -mt-8 and rounded-t-[32px], keep px-6 pb-32 z-20
        new_main_open = re.sub(r'class="[^"]*"',
                               'class="relative px-5 pb-32"',
                               main_open, count=1)
        # Inject our new cover header BEFORE main and re-open main with the tabs
        return get_new_block(dark) + new_main_open + '\n\n  <!-- TOP TABS'

    html = pattern.sub(rewrite_main, html, count=1)

    # Drop body bg-white min-h-screen (we manage bg via our header)
    html = re.sub(r'<body class="bg-white([^"]*)"',
                  lambda m: f'<body class="bg-white' + m.group(1) + '"', html, count=1)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    return out


for variant in ['light', 'dark']:
    src = HARMONIZED / f'profile_visitor_{variant}' / 'code.html'
    out = HARMONIZED / f'profile_visitor_cover_{variant}' / 'code.html'
    if src.exists():
        result = build_variant(src, out, dark=(variant == 'dark'))
        print(f"✓ Built: {result}")
    else:
        print(f"✗ Source missing: {src}")
