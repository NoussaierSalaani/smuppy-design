#!/usr/bin/env python3
"""
build_settings_canonical.py — Rebuild settings_definitive {light,dark} to match the
founder's canonical reference (2026-05-26): centered header (Clara Montgomery + verified +
"PARAMÈTRES DU COMPTE"), 4 clean sections / 16 rows, badges (NEW / ◇2 480 / Public),
Log out + Delete buttons, disclaimer, Smuppy wordmark + version.

Replaces the over-stuffed 25-item enrich_settings.py output. Dark = pure #000000 (brand rule #4).
Settings is a SUBSCREEN → back-arrow header only, NO bottomnav (founder rule).

Regenerate: python3 build_settings_canonical.py
"""
from pathlib import Path

HARMONIZED = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')

# ── Canonical sections / rows ───────────────────────────────────────────────
# (icon, label, hue, badge_html_or_None)
SECTIONS = [
    ("ACCOUNT", [
        ("person",                 "Edit profile",        "#6366F1", None),
        ("lock",                   "Change password",     "#14B8A6", None),
        ("dashboard_customize",    "Channel setup",       "#F59E0B", None),
        ("bolt",                   "Upgrade to Pro",      "#8B5CF6", "NEW"),
    ]),
    ("PREFERENCES", [
        ("notifications",          "Notifications",       "#8B5CF6", None),
        ("group",                  "Find friends",        "#14B8A6", None),
        ("account_balance_wallet", "Smup wallet",         "#F59E0B", "SMUP"),
        ("credit_card",            "Manage subscription", "#3B82F6", None),
    ]),
    ("PRIVACY & SAFETY", [
        ("shield",                 "Privacy settings",    "#10B981", "PUBLIC"),
        ("block",                  "Blocked accounts",    "#EF4444", None),
        ("volume_off",             "Muted accounts",      "#64748B", None),
        ("gavel",                  "Dispute center",      "#F59E0B", None),
    ]),
    ("SUPPORT & LEGAL", [
        ("help",                   "Help center",         "#64748B", None),
        ("report",                 "Report a problem",    "#F59E0B", None),
        ("download",               "Export my data",      "#3B82F6", None),
        ("description",            "Terms & policies",    "#64748B", None),
    ]),
]

MINT = "#26C1A4"
MINT_HI = "#4EDCBE"


def theme(dark: bool) -> dict:
    if dark:
        return dict(
            page="#000000", card="#14141A", row_hover="#1D1D24",
            text="#F1F4F6", sub="#8B8B95", section="#6B6B75",
            header_bg="rgba(10,10,12,0.92)", border="rgba(255,255,255,0.06)",
            chevron="#5A5A66", danger_bg="rgba(239,68,68,0.08)",
            danger_border="rgba(239,68,68,0.25)", danger="#F87171",
            back_stroke="#F1F4F6", html_class="dark",
        )
    return dict(
        page="#F6F8FA", card="#FFFFFF", row_hover="#F4F6F8",
        text="#0F172A", sub="#64748B", section="#94A3B8",
        header_bg="rgba(255,255,255,0.95)", border="#EEF1F4",
        chevron="#CBD5E1", danger_bg="rgba(239,68,68,0.04)",
        danger_border="rgba(239,68,68,0.20)", danger="#EF4444",
        back_stroke="#0E1116", html_class="light",
    )


def badge_html(kind: str, t: dict) -> str:
    if kind == "NEW":
        return (f'<span style="background:linear-gradient(135deg,{MINT} 0%,{MINT_HI} 100%);'
                f'color:#fff;font-size:9px;font-weight:800;letter-spacing:.04em;'
                f'padding:2px 7px;border-radius:999px;">NEW</span>')
    if kind == "SMUP":
        return (f'<span style="color:{MINT};font-size:13px;font-weight:700;display:inline-flex;'
                f'align-items:center;gap:3px;">◇ 2 480</span>')
    if kind == "PUBLIC":
        return f'<span style="color:{t["sub"]};font-size:13px;font-weight:500;">Public</span>'
    return ""


def row_html(icon: str, label: str, hue: str, badge: str | None, t: dict, last: bool) -> str:
    sep = "" if last else f'border-bottom:1px solid {t["border"]};'
    b = badge_html(badge, t) if badge else ""
    return f'''        <button class="settings-row" style="{sep}">
          <span class="ico" style="background:{hue}1A;color:{hue};box-shadow:0 0 18px {hue}55;filter:drop-shadow(0 0 10px {hue}80);">
            <span class="material-symbols-outlined" style="font-size:20px;font-variation-settings:'wght' 400;">{icon}</span>
          </span>
          <span class="lbl">{label}</span>
          <span class="trail">{b}<span class="material-symbols-outlined chev">chevron_right</span></span>
        </button>'''


def section_html(title: str, rows: list, t: dict) -> str:
    n = len(rows)
    body = "\n".join(row_html(*r, t, i == n - 1) for i, r in enumerate(rows))
    return f'''      <h3 class="section-label">{title}</h3>
      <div class="card">
{body}
      </div>'''


def smuppy_wordmark() -> str:
    return ('<svg width="92" height="20" viewBox="0 0 215 46" fill="none" '
            'xmlns="http://www.w3.org/2000/svg" aria-label="Smuppy" role="img">'
            '<defs><linearGradient id="setLogo" x1="0" y1="0" x2="11.5" y2="74.5" '
            'gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0EBF8A"/>'
            '<stop offset="1" stop-color="#00B3C7"/></linearGradient></defs>'
            '<text x="0" y="34" font-family="Plus Jakarta Sans" font-weight="800" '
            'font-size="40" fill="url(#setLogo)">Smuppy</text></svg>')


def build(dark: bool) -> str:
    t = theme(dark)
    sections = "\n".join(section_html(title, rows, t) for title, rows in SECTIONS)
    return f'''<!DOCTYPE html>
<html class="{t["html_class"]}" lang="fr"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Smuppy — Settings</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&amp;display=swap" rel="stylesheet"/>
<style>
  * {{ box-sizing:border-box; -webkit-font-smoothing:antialiased; }}
  body {{ margin:0; min-height:max(844px,100dvh); background:{t["page"]}; color:{t["text"]};
         font-family:'Plus Jakarta Sans',sans-serif; padding-bottom:40px; }}
  .topbar {{ position:fixed; top:0; left:0; right:0; z-index:50; height:56px;
            display:flex; align-items:center; padding:0 12px; background:{t["header_bg"]};
            backdrop-filter:blur(12px); border-bottom:1px solid {t["border"]}; }}
  .back {{ width:40px; height:40px; border:none; background:transparent; border-radius:999px;
          display:flex; align-items:center; justify-content:center; cursor:pointer; }}
  .topbar h1 {{ flex:1; text-align:center; font-size:16px; font-weight:700; margin:0; padding-right:40px; color:{t["text"]}; }}
  main {{ padding:72px 16px 0; }}
  .profile {{ display:flex; flex-direction:column; align-items:center; gap:6px; margin-bottom:26px; }}
  .avatar-wrap {{ position:relative; }}
  .avatar-wrap img {{ width:72px; height:72px; border-radius:999px; object-fit:cover;
                     box-shadow:0 0 0 2.5px {MINT}; }}
  .avatar-edit {{ position:absolute; bottom:-2px; right:-2px; width:24px; height:24px;
                 border-radius:999px; background:{MINT}; border:2.5px solid {t["page"]};
                 display:flex; align-items:center; justify-content:center; }}
  .pname {{ display:flex; align-items:center; gap:5px; font-size:19px; font-weight:800; margin-top:8px; color:{t["text"]}; }}
  .psub {{ font-size:11px; font-weight:700; letter-spacing:.12em; color:{MINT}; text-transform:uppercase; }}
  .section-label {{ font-size:11px; font-weight:700; letter-spacing:.10em; text-transform:uppercase;
                   color:{t["section"]}; margin:22px 8px 8px; }}
  .card {{ background:{t["card"]}; border-radius:18px; overflow:hidden;
          box-shadow:0 1px 3px rgba(0,0,0,{0.4 if dark else 0.05}); }}
  .settings-row {{ width:100%; display:flex; align-items:center; gap:13px; padding:14px 16px;
                  background:transparent; border:none; cursor:pointer; text-align:left; }}
  .settings-row:active {{ background:{t["row_hover"]}; }}
  .ico {{ width:36px; height:36px; border-radius:999px; display:flex; align-items:center;
         justify-content:center; flex-shrink:0; }}
  .lbl {{ flex:1; font-size:15px; font-weight:500; color:{t["text"]}; }}
  .trail {{ display:flex; align-items:center; gap:8px; }}
  .chev {{ font-size:20px; color:{t["chevron"]}; }}
  .danger-btn {{ width:100%; display:flex; align-items:center; justify-content:center; gap:8px;
                margin-top:14px; padding:15px; border-radius:16px; font-size:15px; font-weight:700;
                background:{t["danger_bg"]}; border:1.5px solid {t["danger_border"]};
                color:{t["danger"]}; cursor:pointer; }}
  .disclaimer {{ text-align:center; font-size:11px; line-height:1.5; color:{t["sub"]};
                margin:22px 14px 18px; }}
  .footer-logo {{ display:flex; flex-direction:column; align-items:center; gap:4px; opacity:.9; }}
  .ver {{ font-size:11px; color:{t["sub"]}; font-weight:600; }}
</style>
</head>
<body>
<header class="topbar">
  <button class="back" aria-label="Back">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{t["back_stroke"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <h1>Settings</h1>
</header>
<main>
  <div class="profile">
    <div class="avatar-wrap">
      <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=160&h=160&fit=crop" alt="Clara Montgomery"/>
      <span class="avatar-edit"><span class="material-symbols-outlined" style="color:#fff;font-size:13px;">edit</span></span>
    </div>
    <div class="pname">Clara Montgomery
      <span class="material-symbols-outlined" style="color:{MINT};font-size:18px;font-variation-settings:'FILL' 1;">verified</span>
    </div>
    <div class="psub">Paramètres du compte</div>
  </div>
{sections}
  <button class="danger-btn">
    <span class="material-symbols-outlined" style="font-size:20px;">logout</span> Log out
  </button>
  <button class="danger-btn">
    <span class="material-symbols-outlined" style="font-size:20px;">delete</span> Delete my account permanently
  </button>
  <p class="disclaimer">Deletion is permanent after 14 days. All your posts, peaks, activities,
    channel subscriptions and Smups balance will be erased.</p>
  <div class="footer-logo">
    {smuppy_wordmark()}
    <span class="ver">V2 · 4.0</span>
  </div>
</main>
</body>
</html>
'''


def main() -> None:
    for dark, name in [(False, 'settings_definitive'), (True, 'settings_definitive_dark')]:
        out = HARMONIZED / name / 'code.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build(dark), encoding='utf-8')
        print(f'  wrote: {name}/code.html  (dark={dark})')


if __name__ == '__main__':
    main()
