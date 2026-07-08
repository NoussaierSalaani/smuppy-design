#!/usr/bin/env python3
"""Build a single-page contact-sheet of all device PNGs in _figma-device-import/.
Output: docs/design/master-audit-may30/_figma-gallery.html (open via file://, no server needed).
Pairs dark+light per screen, groups by category prefix. Pure stdlib, deterministic (sorted)."""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]          # master-audit-may30/
IMG_DIR = ROOT / "_figma-device-import"
OUT = ROOT / "_figma-gallery.html"

# Category routing: (label, predicate on screen-key)
CATS = [
    ("★ Run (Personal Activity · tracking/share/records)", lambda k: k.startswith("run_")),
    ("★ Profils v5 (Instagram · owner/visitor/fan/private)", lambda k: k.startswith("profile_")),
    ("★ Feeds & Discover (Fan/Vibes/Xplorer/Search/Peaks-Live)", lambda k: k.startswith(("home_feed", "vibes_feed", "xplorer_map", "search_v2", "peaks_live"))),
    ("★ Canonical · Settings",       lambda k: k.startswith("settings_definitive")),
    ("Creator · Channel / 1:1 / Packages", lambda k: k.startswith(("creator_1on1", "creator_channel", "creator_packages"))),
    ("Creation · Post / Peak",       lambda k: k.startswith(("post_", "peak_"))),
    ("Auth",                         lambda k: k.startswith("auth_")),
    ("Onboarding",                   lambda k: k.startswith("onb_")),
    ("P1 · Settings / Messages / Profile", lambda k: k.startswith("p1_")),
    ("P2 · Payments / Sessions / Business / Live", lambda k: k.startswith("p2_")),
]

def screen_key(stem: str) -> str:
    for suf in ("_v2_dark", "_v2_light", "_dark", "_light"):
        if stem.endswith(suf):
            return stem[: -len(suf)]
    return stem

# Collect screen -> {theme: filename}
screens: dict[str, dict[str, str]] = {}
for p in sorted(IMG_DIR.glob("*.png")):
    stem = p.stem
    theme = "dark" if stem.endswith("dark") else "light" if stem.endswith("light") else "?"
    screens.setdefault(screen_key(stem), {})[theme] = p.name

# Assign each screen to first matching category, else "Autres"
buckets: dict[str, list[str]] = {label: [] for label, _ in CATS}
buckets["Autres"] = []
for key in sorted(screens):
    for label, pred in CATS:
        if pred(key):
            buckets[label].append(key); break
    else:
        buckets["Autres"].append(key)

total = sum(len(v) for v in screens.values() for _ in [0])  # screen count
png_count = sum(len(t) for t in screens.values())

def card(key: str) -> str:
    themes = screens[key]
    cells = ""
    for theme in ("dark", "light"):
        fn = themes.get(theme)
        if fn:
            src = f"_figma-device-import/{fn}"
            # live scrollable URL (served by design server). Handle settings _v2 naming.
            d = fn[:-4]  # strip .png
            if d.startswith("settings_definitive_v2_"):
                d = "settings_definitive_" + d.split("_v2_")[1]
            live = f"http://127.0.0.1:8765/maquettes/harmonized/{d}/code.html"
            cells += (f'<figure class="ph"><a href="{live}" target="_blank" rel="noopener" '
                      f'title="Ouvrir scrollable">'
                      f'<img loading="lazy" src="{html.escape(src)}" alt="{html.escape(key)} {theme}"/>'
                      f'<span class="ph-open">↗ scroll</span></a><figcaption>{theme}</figcaption></figure>')
        else:
            cells += '<figure class="ph missing"><div>—</div><figcaption>manquant</figcaption></figure>'
    return f'<div class="screen"><div class="screen-key">{html.escape(key)}</div><div class="pair">{cells}</div></div>'

sections = ""
for label in [l for l, _ in CATS] + ["Autres"]:
    keys = buckets.get(label, [])
    if not keys:
        continue
    cards = "".join(card(k) for k in keys)
    sections += (f'<section><h2>{html.escape(label)} '
                 f'<span class="cnt">{len(keys)} écrans</span></h2>'
                 f'<div class="grid">{cards}</div></section>')

doc = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Smuppy V2 · Galerie device complète</title>
<meta http-equiv="Cache-Control" content="no-cache">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:radial-gradient(circle at 50% 0%,#1a1a25 0%,#050508 70%);min-height:100vh;
  font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:#F1F4F6;padding:48px 32px 96px}}
h1{{font-size:30px;font-weight:900;letter-spacing:-.03em;
  background:linear-gradient(90deg,#26C1A4,#00B3C7);-webkit-background-clip:text;background-clip:text;color:transparent}}
.sub{{color:#8B8B95;font-weight:600;font-size:13px;margin:6px 0 36px}}
section{{margin-bottom:48px}}
h2{{font-size:16px;font-weight:800;color:#26C1A4;margin-bottom:16px;display:flex;align-items:center;gap:10px}}
.cnt{{font-size:11px;font-weight:700;color:#8B8B95;background:rgba(38,193,164,.10);
  border:1px solid rgba(38,193,164,.25);padding:3px 9px;border-radius:999px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:24px}}
.screen{{display:flex;flex-direction:column;gap:8px}}
.screen-key{{font-size:11px;font-weight:700;color:#B8B8C0;letter-spacing:.01em;word-break:break-all}}
.pair{{display:flex;gap:8px}}
.ph{{flex:1;display:flex;flex-direction:column;gap:4px;align-items:center}}
.ph a{{position:relative;display:block;cursor:pointer}}.ph a:hover img{{outline:2px solid #26C1A4;outline-offset:2px}}.ph-open{{position:absolute;top:8px;right:8px;padding:3px 8px;border-radius:999px;background:rgba(38,193,164,.9);color:#04201B;font-size:9px;font-weight:800;opacity:0;transition:.15s}}.ph a:hover .ph-open{{opacity:1}}
  .ph img{{width:100%;border-radius:14px;border:1px solid rgba(255,255,255,.08);
  box-shadow:0 6px 24px rgba(0,0,0,.4);background:#000}}
.ph figcaption{{font-size:9px;font-weight:700;color:#6B6B75;text-transform:uppercase;letter-spacing:.08em}}
.ph.missing div{{width:100%;aspect-ratio:393/852;display:flex;align-items:center;justify-content:center;
  border:1px dashed rgba(255,255,255,.15);border-radius:14px;color:#555;font-size:24px}}
</style></head><body>
<h1>Smuppy V2 · Galerie device complète</h1>
<p class="sub">{png_count} PNGs · {len(screens)} écrans uniques · 393×852 · dark + light appairés · prêts Figma</p>
{sections}
</body></html>"""

OUT.write_text(doc, encoding="utf-8")
print(f"wrote {OUT}")
print(f"screens={len(screens)} pngs={png_count} categories={sum(1 for l in buckets if buckets[l])}")
