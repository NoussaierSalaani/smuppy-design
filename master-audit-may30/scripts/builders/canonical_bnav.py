"""Canonical Smuppy bottom nav — EXACT SVG paths from v2_canonical_home_feed Stitch dump
(founder validated yesterday). Single source of truth — reused by ALL screens with bottom nav.

Slots :
  1. Home (custom SVG shield shape · active = mint fill + bar below)
  2. Peaks/Play (camcorder + play triangle · grey inactive)
  3. Create+ center (pill-active-dark style · slate bg + mint + + icon)
  4. Messages (chat bubble outline · grey inactive)
  5. Profile (avatar SQUARE 12px radius + mint outline 2px when active)
"""

# Real SVG paths from external_screens/v2_canonical_home_feed_dark/code.html
HOME_PATH = "M7.5601 3.3893C5.0178 5.277 3.7466 6.2209 3.2474 7.6151C3.2073 7.727 3.1713 7.8403 3.1394 7.9548C2.7414 9.3827 3.227 10.9099 4.198 13.9643C5.1691 17.0187 5.6546 18.5459 6.7978 19.462C6.8895 19.5355 6.9838 19.6055 7.0805 19.672C8.2863 20.5 9.8575 20.5 13 20.5C16.1425 20.5 17.7137 20.5 18.9195 19.672C19.0162 19.6055 19.1105 19.5355 19.2022 19.462C20.3454 18.5459 20.8309 17.0187 21.802 13.9643C22.773 10.9099 23.2586 9.3827 22.8606 7.9548C22.8287 7.8403 22.7927 7.727 22.7526 7.6151C22.2534 6.2209 20.9822 5.277 18.4399 3.3893C15.8976 1.5016 14.6265 0.5577 13.1747 0.5033C13.0583 0.4989 12.9417 0.4989 12.8253 0.5033C11.3735 0.5577 10.1024 1.5016 7.5601 3.3893ZM11.0934 15.1821C10.6985 15.1821 10.3784 15.5093 10.3784 15.9129C10.3784 16.3164 10.6985 16.6436 11.0934 16.6436H14.9066C15.3015 16.6436 15.6216 16.3164 15.6216 15.9129C15.6216 15.5093 15.3015 15.1821 14.9066 15.1821H11.0934Z"
PEAKS_PATH_A = "M15.7 19.335C14.528 19.5 13 19.5 10.95 19.5H9.05C5.019 19.5 3.004 19.5 1.752 18.248C0.5 16.996 0.5 14.981 0.5 10.95V9.05C0.5 5.019 0.5 3.004 1.752 1.752C3.004 0.5 5.019 0.5 9.05 0.5H10.95C14.981 0.5 16.996 0.5 18.248 1.752C19.5 3.004 19.5 5.019 19.5 9.05V10.95C19.5 12.158 19.5 13.185 19.466 14.065C19.439 14.77 19.426 15.123 19.159 15.254C18.892 15.386 18.593 15.175 17.996 14.752L16.65 13.8"
PEAKS_PATH_B = "M12.945 10.395C12.769 11.021 11.933 11.464 10.263 12.35C8.648 13.206 7.841 13.635 7.19 13.462C6.921 13.391 6.676 13.256 6.478 13.07C6 12.62 6 11.746 6 10C6 8.253 6 7.38 6.478 6.93C6.676 6.744 6.921 6.609 7.19 6.538C7.841 6.365 8.648 6.794 10.263 7.65C11.933 8.536 12.769 8.978 12.945 9.605C13.018 9.864 13.018 10.136 12.945 10.395Z"
MSG_PATH = "M12 3C7.029 3 3 7.029 3 12C3 13.689 3.466 15.274 4.287 16.628L3.016 19.832C2.76 20.478 3.303 21.14 3.985 20.994L7.789 20.158C9.05 20.693 10.447 21 12 21C16.971 21 21 16.971 21 12C21 7.029 16.971 3 12 3Z"


def canonical_msg_icon(size: int = 18, color: str = '#33A089') -> str:
    """Canonical chat-bubble message icon — SAME MSG_PATH as bnav Messages slot.
    Reused by the profile visitor 'Message' button so it's byte-identical to the nav."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none">'
            f'<path d="{MSG_PATH}" stroke="{color}" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')


def canonical_bnav(active: str = 'home', dark: bool = True) -> str:
    """Render the canonical 5-slot bottom nav (matches v2_canonical_home_feed validated).
    `active` ∈ ['home', 'peaks', 'create', 'msg', 'profile']."""
    grey = '#94a3b8'  # inactive color (same as canonical Stitch)
    mint = '#33A089'

    def svg_home(is_on):
        # Canonical: viewBox 0 0 20 21 + path translate(-3,0). Matches v2_canonical_home_feed_dark.
        # jun03: active = mint OUTLINE (not solid fill) — consistent w/ peaks/msg; full-green silhouette removed.
        col = mint if is_on else grey
        sw = '2.1' if is_on else '1.8'
        return f'<svg width="26" height="26" viewBox="0 0 20 21" fill="none"><path d="{HOME_PATH}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" transform="translate(-3, 0)"/></svg>'

    def svg_peaks(is_on):
        col = mint if is_on else grey
        # Use TWO paths : camera body + play triangle
        return (f'<svg width="26" height="26" viewBox="0 0 21 20" fill="none">'
                f'<path d="{PEAKS_PATH_A}" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
                f'<path d="{PEAKS_PATH_B}" stroke="{col}" stroke-width="1.8" stroke-linejoin="round" fill="none"/></svg>')

    def svg_msg(is_on):
        col = mint if is_on else grey
        return (f'<svg width="26" height="26" viewBox="0 0 24 24" fill="none">'
                f'<path d="{MSG_PATH}" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')

    def svg_plus():
        return (f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none">'
                f'<path d="M12 5V19M5 12H19" stroke="{mint}" stroke-width="2.5" stroke-linecap="round"/></svg>')

    def slot(key, svg_html):
        is_on = active == key
        bar = '<div class="cn-bnav-bar"></div>' if is_on else ''
        glow = ' cn-bnav-on' if is_on else ''
        return f'<button class="cn-bnav-item{glow}">{svg_html}{bar}</button>'

    profile_on = active == 'profile'
    profile_cls = 'cn-bnav-profile cn-bnav-profile-on' if profile_on else 'cn-bnav-profile'
    profile_bar = '<div class="cn-bnav-bar"></div>' if profile_on else ''

    return f'''<nav class="cn-bnav">
  {slot('home', svg_home(active == 'home'))}
  {slot('peaks', svg_peaks(active == 'peaks'))}
  <button class="cn-bnav-create">{svg_plus()}</button>
  {slot('msg', svg_msg(active == 'msg'))}
  <button class="{profile_cls}"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=80&h=80&fit=crop&q=80" alt=""/>{profile_bar}</button>
</nav>'''


CANONICAL_BNAV_CSS = """
<style>
  /* Canonical bottom nav — single source of truth (matches v2_canonical_home_feed) */
  .cn-bnav { position:absolute; bottom:0; left:0; right:0; z-index:80;
    display:flex; justify-content:space-around; align-items:center;
    padding:14px 24px 18px env(safe-area-inset-bottom,18px);
    background:var(--card);
    border-top:1px solid var(--border);
    border-radius:28px 28px 0 0;
    box-shadow:0 -4px 24px rgba(0,0,0,0.12); }
  .cn-bnav-item { position:relative; width:48px; height:48px;
    border:none; background:transparent; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .cn-bnav-on { filter:drop-shadow(0 0 6px rgba(51,160,137,0.275)); }
  .cn-bnav-bar { position:absolute; bottom:-6px; left:50%; transform:translateX(-50%);
    width:24px; height:3px; border-radius:999px; background:#33A089;
    box-shadow:0 0 8px rgba(51,160,137,0.3); }
  /* Create+ center : pill-active-dark style (card bg + mint border + mint icon halo) */
  .cn-bnav-create { width:48px; height:48px; border-radius:999px;
    border:1.5px solid rgba(51,160,137,0.225);
    background:var(--card); cursor:pointer;
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 16px rgba(51,160,137,0.175),
               0 4px 12px rgba(51,160,137,0.2),
               0 0 0 1px rgba(51,160,137,0.15) inset;
    filter:drop-shadow(0 0 6px rgba(51,160,137,0.2)); }
  /* Profile : SQUARE avatar 12px radius + mint outline when active */
  .cn-bnav-profile { position:relative; width:48px; height:48px;
    border:none; background:transparent; cursor:pointer;
    display:flex; align-items:center; justify-content:center; }
  .cn-bnav-profile img { width:32px; height:32px; border-radius:12px;
    object-fit:cover; opacity:.85;
    outline:1.5px solid transparent; transition:.18s ease; }
  .cn-bnav-profile-on img { opacity:1;
    outline:2px solid #33A089; outline-offset:2px;
    box-shadow:0 0 8px rgba(51,160,137,0.225); }
</style>
"""
