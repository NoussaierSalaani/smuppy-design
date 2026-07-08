"""Smuppy V2 — DS-fill maquettes (the 25 screens that never had a drawn maquette).

Renders each at 393×852 (iPhone 14 Pro) in light + dark, in the EXACT V2 design
system grammar (tokens from src/theme/v2/tokens.ts): Plus Jakarta Sans, mint
#33A089 (founder choice A — a11y-safe) + green GLOW + RING contour (the "alive"
look), dark surface #0A0E1A, rounded cards, 4pt spacing.

ICONS = the REAL app icon set: Ionicons (@expo/vector-icons) loaded from
node_modules via @font-face + the official glyphmap (name → unicode). NO emoji.

Output: docs/design/master-audit-may30/dsfill-v2/<name>_v2_<light|dark>.png
Capture: Chrome headless (--screenshot).

Run:  python3 build_dsfill_v2.py
"""
import json
import subprocess
from pathlib import Path

ROOT = Path('/Users/noussaier/smuppy-mobile')
OUT = ROOT / 'docs/design/master-audit-may30/dsfill-v2'
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path('/tmp/_dsfill_html'); TMP.mkdir(exist_ok=True)
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
W, H = 393, 852

# ── Real app icon set: Ionicons (@expo/vector-icons) ───────────────────────
ION_TTF = ROOT / 'node_modules/@expo/vector-icons/build/vendor/react-native-vector-icons/Fonts/Ionicons.ttf'
ION_MAP = ROOT / 'node_modules/@expo/vector-icons/build/vendor/react-native-vector-icons/glyphmaps/Ionicons.json'
GLYPH = json.loads(ION_MAP.read_text())


def ion(name, size=20, color=None):
    """Render a REAL Ionicon glyph (falls back filled→outline→ellipse)."""
    cp = GLYPH.get(name) or GLYPH.get(name.replace('-outline', '')) or GLYPH.get('ellipse-outline')
    col = f';color:{color}' if color else ''
    return f'<span class=ion style="font-size:{size}px{col}">&#x{cp:x};</span>'


# FINAL locked palette (founder choice A): mint #33A089 (a11y-safe) + green
# glow/ring (the "alive" contour). COLOR ONLY — no structural change.
MINT_GRAD = 'linear-gradient(135deg,#41AD96,#2C95A0)'   # primary button / CTA gradient
GLOW = 'rgba(51,160,137,.175)'     # green glow halo
GLOW_SOFT = 'rgba(51,160,137,.10)'
RING = 'rgba(51,160,137,.225)'     # 1px green ring — the "contour" (0 0 0 1px)
# mint #33A089 = rgb(51,160,137) — tint opacities (structure unchanged)
T12 = 'rgba(51,160,137,.12)'   # card hairline border
T05 = 'rgba(51,160,137,.05)'   # card soft glow
T14 = 'rgba(51,160,137,.14)'   # icon-square tinted bg
T15 = 'rgba(51,160,137,.15)'   # feature-card border


def theme(dark):
    if dark:
        return dict(bg='#0A0E1A', card='#161B2A', high='#1F2538', text='#FFFFFF',
                    sub='#94A3B8', border='#2A3142', mint='#33A089', danger='#F87171',
                    warn='#FBBF24', ok='#34D399')
    return dict(bg='#FFFFFF', card='#F8FAFC', high='#F1F5F9', text='#0F172A',
                sub='#475569', border='#E2E8F0', mint='#33A089', danger='#DC2626',
                warn='#F59E0B', ok='#10B981')


def css(t):
    return f"""
@font-face{{font-family:'Ionicons';src:url('file://{ION_TTF}') format('truetype')}}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Plus Jakarta Sans',system-ui,sans-serif}}
.ion{{font-family:'Ionicons' !important;font-weight:normal;line-height:1}}
body{{width:{W}px;height:{H}px;background:{t['bg']};color:{t['text']};overflow:hidden}}
.nav{{height:56px;display:flex;align-items:center;gap:10px;padding:0 14px;border-bottom:1px solid {t['border']}}}
.back{{font-size:24px;color:{t['text']}}}
.navt{{font-size:16px;font-weight:700}}
.eyebrow{{font-size:11px;font-weight:800;letter-spacing:.10em;text-transform:uppercase;color:{t['mint']};margin-bottom:6px;text-shadow:0 0 14px {GLOW}}}
.h1{{font-size:24px;font-weight:800;letter-spacing:-.4px;margin-bottom:8px}}
.sub{{font-size:14px;color:{t['sub']};line-height:21px}}
.wrap{{padding:18px;height:{H-56}px;overflow:hidden;position:relative}}
.card{{background:{t['card']};border:1px solid {T12};border-radius:18px;padding:4px 14px;margin-bottom:14px;box-shadow:0 0 16px {T05}}}
.row{{display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid {t['border']}}}
.row:last-child{{border-bottom:none}}
.av{{width:40px;height:40px;border-radius:12px;background:{MINT_GRAD};display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:14px;flex-shrink:0;box-shadow:0 5px 16px {GLOW_SOFT}}}
.icon{{width:32px;height:32px;border-radius:10px;background:{T14};display:flex;align-items:center;justify-content:center;flex-shrink:0}}
.rt{{flex:1;min-width:0}}
.rp{{font-size:14px;font-weight:600}}
.rs{{font-size:11.5px;color:{t['sub']};margin-top:2px}}
.chev{{font-size:18px;color:{t['sub']};opacity:.55;margin-left:2px}}
.pill{{font-size:11px;font-weight:700;padding:4px 10px;border-radius:999px;background:{t['high']};color:{t['sub']};white-space:nowrap}}
.pill.ok{{background:rgba(52,211,153,.16);color:{t['ok']}}}
.pill.warn{{background:rgba(251,191,36,.16);color:{t['warn']}}}
.pill.dng{{background:rgba(248,113,113,.16);color:{t['danger']}}}
.cta{{position:absolute;left:20px;right:20px;bottom:24px;height:52px;border-radius:999px;background:{MINT_GRAD};color:#fff;font-size:16px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 10px 30px {GLOW},0 0 0 1px {RING}}}
.cta2{{height:52px;border-radius:12px;border:1px solid {t['border']};color:{t['text']};font-size:16px;font-weight:600;display:flex;align-items:center;justify-content:center;margin-top:10px}}
.field{{margin-bottom:14px}}
.lab{{font-size:13px;font-weight:600;color:{t['sub']};margin-bottom:6px}}
.inp{{height:44px;border:1px solid {t['border']};border-radius:12px;background:{t['card']};display:flex;align-items:center;gap:10px;padding:0 14px;font-size:15px;color:{t['text']}}}
.inp.ph{{color:{t['sub']}}}
.hero{{display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:54px}}
.heroIc{{width:80px;height:80px;border-radius:24px;background:{MINT_GRAD};display:flex;align-items:center;justify-content:center;margin-bottom:22px;box-shadow:0 12px 36px {GLOW}}}
.toggle{{width:42px;height:24px;border-radius:999px;background:{t['mint']};position:relative;flex-shrink:0;box-shadow:0 0 12px {GLOW_SOFT}}}
.toggle::after{{content:'';position:absolute;width:20px;height:20px;border-radius:999px;background:#fff;top:2px;right:2px;box-shadow:0 2px 4px rgba(0,0,0,.2)}}
.toggle.off{{background:{t['border']};box-shadow:none}}
.toggle.off::after{{left:2px;right:auto}}
.featcard{{background:{t['card']};border:1.5px solid {T15};border-radius:22px;box-shadow:0 0 24px {T15};padding:16px;margin-bottom:14px}}
.sec{{font-size:11px;font-weight:800;color:{t['sub']};text-transform:uppercase;letter-spacing:.10em;margin:6px 0 8px 4px}}
.body{{font-size:14px;color:{t['sub']};line-height:22px;margin-bottom:14px}}
.big{{font-size:34px;font-weight:800;letter-spacing:-1px}}
.bar{{height:10px;border-radius:999px;background:{t['high']};overflow:hidden;margin:6px 0}}
.bar>i{{display:block;height:100%;background:{MINT_GRAD}}}
"""


def page(t, title, body, footer=''):
    nav = (f'<div class=nav><span class=back>{ion("chevron-back",24,t["text"])}</span>'
           f'<span class=navt>{title}</span></div>') if title else ''
    return (f"<!doctype html><html><head><meta charset=utf-8>"
            f'<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel=stylesheet>'
            f"<style>{css(t)}</style></head><body>{nav}<div class=wrap>{body}{footer}</div></body></html>")


# ─────────── templates ───────────
def list_screen(t, eyebrow, h1, sub, rows, cta=None, cta_ic=None):
    rh = ''
    for r in rows:
        if r.get('av'):
            lead = f'<div class=av>{r["i"]}</div>'
        else:
            lead = f'<div class=icon>{ion(r["i"], 18, t["mint"])}</div>'
        if r.get('pill'):
            trail = f'<span class="pill {r.get("pc","")}">{r["pill"]}</span>'
        elif r.get('chev'):
            trail = f'<span class=chev>{ion("chevron-forward", 18, t["sub"])}</span>'
        else:
            trail = ''
        rh += f'<div class=row>{lead}<div class=rt><div class=rp>{r["p"]}</div><div class=rs>{r["s"]}</div></div>{trail}</div>'
    head = f'<div class=eyebrow>{eyebrow}</div><div class=h1>{h1}</div><div class=sub style="margin-bottom:16px">{sub}</div>'
    ctah = f'<div class=cta>{ion(cta_ic,18,"#fff") if cta_ic else ""}{cta}</div>' if cta else ''
    return head + f'<div class=card>{rh}</div>', ctah


def text_screen(t, eyebrow, h1, sections):
    head = f'<div class=eyebrow>{eyebrow}</div><div class=h1>{h1}</div>'
    b = ''.join(f'<div class=card><div class=sec>{s}</div><div class=body>{body}</div></div>' for s, body in sections)
    return head + b, ''


def hero_screen(t, ic, h1, desc, cta, cta2=None):
    b = (f'<div class=hero><div class=heroIc>{ion(ic,44,"#fff")}</div>'
         f'<div class=h1>{h1}</div><div class=sub style="max-width:300px">{desc}</div></div>')
    f = f'<div class=cta>{cta}</div>'
    if cta2:
        b += f'<div style="position:absolute;left:20px;right:20px;bottom:86px"><div class=cta2>{cta2}</div></div>'
    return b, f


def form_screen(t, eyebrow, h1, fields, cta, cta_ic=None):
    head = f'<div class=eyebrow>{eyebrow}</div><div class=h1 style="margin-bottom:18px">{h1}</div>'
    fh = ''
    for lab, val, ph, ic in fields:
        glyph = ion(ic, 18, t['sub']) if ic else ''
        fh += f'<div class=field><div class=lab>{lab}</div><div class="inp {"ph" if ph else ""}">{glyph}{val}</div></div>'
    return head + fh, f'<div class=cta>{ion(cta_ic,18,"#fff") if cta_ic else ""}{cta}</div>'


def toggles_screen(t, eyebrow, h1, items):
    head = f'<div class=eyebrow>{eyebrow}</div><div class=h1 style="margin-bottom:16px">{h1}</div>'
    rh = ''.join(
        f'<div class=row><div class=icon>{ion(ic,18,t["mint"])}</div><div class=rt><div class=rp>{lab}</div>'
        f'<div class=rs>{sub}</div></div><div class="toggle {"" if on else "off"}"></div></div>'
        for lab, sub, on, ic in items)
    return head + f'<div class=card>{rh}</div>', ''


# ─────────── the 25 screens (REAL Ionicons names) ───────────
def screens(t):
    av = lambda x: {'i': x, 'av': True}
    return {
        'activity_attendees': list_screen(t, 'Participants', 'Inscrits', '12 participants confirmés', [
            {**av('LM'), 'p': 'Lina Moreau', 's': 'Confirmée', 'pill': 'Hôte', 'pc': 'ok'},
            {**av('YT'), 'p': 'Yanis Touré', 's': 'Confirmé'},
            {**av('SC'), 'p': 'Sofia Caron', 's': "Liste d'attente", 'pill': 'Attente', 'pc': 'warn'},
            {**av('RB'), 'p': 'Rayan Benali', 's': 'Confirmé'},
            {**av('EM'), 'p': 'Emma Martin', 's': 'Confirmée'},
        ]),
        'activity_leaderboard': list_screen(t, 'Classement', 'Leaderboard', 'Cette semaine · 5 km', [
            {'i': 'trophy', 'p': 'Yanis Touré', 's': '18:42 · record', 'pill': '1er', 'pc': 'ok'},
            {'i': 'medal', 'p': 'Lina Moreau', 's': '19:05', 'pill': '2e'},
            {'i': 'medal', 'p': 'Sofia Caron', 's': '19:38', 'pill': '3e'},
            {'i': 'person', 'p': 'Toi', 's': '20:11', 'pill': '+0:33', 'pc': 'warn'},
            {'i': 'person', 'p': 'Rayan Benali', 's': '20:47'},
        ]),
        'blocked_region': hero_screen(t, 'globe-outline', 'Indisponible dans ta région', "Ce contenu n'est pas accessible depuis ta localisation actuelle pour des raisons réglementaires.", "Retour à l'accueil"),
        'blocked_users': list_screen(t, 'Confidentialité', 'Comptes bloqués', '3 comptes bloqués', [
            {**av('JD'), 'p': '@jdupont', 's': 'Bloqué le 2 juin', 'pill': 'Débloquer', 'pc': 'dng'},
            {**av('MK'), 'p': '@mkali', 's': 'Bloqué le 28 mai', 'pill': 'Débloquer', 'pc': 'dng'},
            {**av('TP'), 'p': '@t.petit', 's': 'Bloqué le 19 mai', 'pill': 'Débloquer', 'pc': 'dng'},
        ]),
        'coach_journal': list_screen(t, 'Coaching', 'Journal du coach', 'Notes de séances', [
            {'i': 'create-outline', 'p': 'Séance jambes', 's': '10 juin · "Bonne progression sur les squats"', 'chev': True},
            {'i': 'create-outline', 'p': 'Cardio fractionné', 's': '7 juin · "Augmenter l\'intensité"', 'chev': True},
            {'i': 'create-outline', 'p': 'Mobilité', 's': '3 juin · "Travailler les hanches"', 'chev': True},
        ]),
        'data_export': (
            '<div class=eyebrow>Tes données</div><div class=h1>Exporter mes données</div>'
            '<div class=sub style="margin-bottom:16px">Reçois une copie de toutes tes données Smuppy (profil, posts, activités) au format ZIP.</div>'
            f'<div class=card style="padding:16px"><div class=rp>Dernière demande</div><div class=rs style="margin-top:6px">Aucune demande en cours.</div></div>'
            f'<div class=card style="padding:16px"><div class=rp>Inclus dans l\'export</div><div class=rs style="margin-top:6px">Profil · Posts · Peaks · Activités · Messages · Paiements</div></div>',
            f'<div class=cta>{ion("download-outline",18,"#fff")}Demander l\'export</div>'),
        'dispute_center': list_screen(t, 'Litiges', 'Centre de litiges', '2 litiges en cours', [
            {'i': 'alert-circle-outline', 'p': 'Séance non honorée', 's': 'Ouvert le 8 juin', 'pill': 'En cours', 'pc': 'warn'},
            {'i': 'checkmark-circle-outline', 'p': 'Remboursement pack', 's': 'Résolu le 1 juin', 'pill': 'Résolu', 'pc': 'ok'},
        ], cta='Ouvrir un litige', cta_ic='add'),
        'help': list_screen(t, 'Support', "Centre d'aide", "Comment pouvons-nous t'aider ?", [
            {'i': 'rocket-outline', 'p': 'Premiers pas', 's': 'Configurer ton compte', 'chev': True},
            {'i': 'card-outline', 'p': 'Paiements & abonnements', 's': 'Factures, remboursements', 'chev': True},
            {'i': 'lock-closed-outline', 'p': 'Compte & sécurité', 's': 'Mot de passe, 2FA', 'chev': True},
            {'i': 'megaphone-outline', 'p': 'Signaler un problème', 's': 'Bug, contenu, utilisateur', 'chev': True},
        ]),
        'kyc_company': form_screen(t, 'Vérification', 'Informations entreprise', [
            ('Raison sociale', 'Smuppy Fitness SARL', False, 'business-outline'),
            ("Numéro d'enregistrement", 'FR 123 456 789', False, 'document-text-outline'),
            ('Pays', 'France', False, 'flag-outline'),
            ('Adresse du siège', '12 rue du Sport, Paris', False, 'location-outline'),
        ], 'Continuer la vérification', cta_ic='shield-checkmark-outline'),
        'match_page': (
            '<div class=eyebrow>Match</div><div class=h1>Match amical</div>'
            '<div class=sub style="margin-bottom:16px">Aujourd\'hui · 18:30 · Stade Léo Lagrange</div>'
            f'<div class=card style="padding:18px;display:flex;align-items:center;justify-content:space-around;text-align:center">'
            f'<div><div class=av style="width:64px;height:64px;border-radius:18px;margin:0 auto 8px;font-size:18px">RC</div><div class=rp>Racing C.</div></div>'
            f'<div class=big>2 – 1</div>'
            f'<div><div class=av style="width:64px;height:64px;border-radius:18px;margin:0 auto 8px;font-size:18px">OF</div><div class=rp>Olympic F.</div></div></div>'
            f'<div class=card style="padding:16px"><div class=rp>Composition</div><div class=rs style="margin-top:6px">11 joueurs · 3 remplaçants</div></div>',
            f'<div class=cta>{ion("football-outline",18,"#fff")}Rejoindre le match</div>'),
        'muted_users': list_screen(t, 'Confidentialité', 'Comptes en sourdine', '2 comptes masqués', [
            {**av('AL'), 'p': '@a.legrand', 's': 'En sourdine', 'pill': 'Réactiver', 'pc': 'warn'},
            {**av('NB'), 'p': '@nadia.b', 's': 'En sourdine', 'pill': 'Réactiver', 'pc': 'warn'},
        ]),
        'my_subscriptions': list_screen(t, 'Abonnements', 'Mes abonnements', '2 abonnements actifs', [
            {**av('CF'), 'p': 'Coach Fit Pro', 's': '14,90 €/mois · renouvelle le 15', 'pill': 'Actif', 'pc': 'ok'},
            {**av('YG'), 'p': 'Yoga Studio', 's': '9,90 €/mois · renouvelle le 22', 'pill': 'Actif', 'pc': 'ok'},
        ], cta='Gérer les abonnements', cta_ic='settings-outline'),
        'payout_onboarding': hero_screen(t, 'cash-outline', 'Configure tes virements', 'Connecte ton compte Stripe pour recevoir tes gains de créateur directement sur ton compte bancaire.', 'Connecter Stripe', 'En savoir plus'),
        'peak_viewer': None,  # special, built below
        'premium_plan': (
            '<div class=eyebrow>Premium</div><div class=h1>Passe au Premium</div>'
            '<div class=sub style="margin-bottom:16px">Débloque tout le potentiel de Smuppy.</div>'
            f'<div class=featcard>'
            f'<div style="display:flex;justify-content:space-between;align-items:center">'
            f'<div class=av style="width:52px;height:52px;border-radius:15px">{ion("diamond",24,"#fff")}</div>'
            f'<div class=big style="font-size:26px">99 €<span style="font-size:14px;color:{t["sub"]}">/mois</span></div></div>'
            f'<div class=rp style="font-size:17px;margin-top:14px">Créateur Pro</div>'
            f'<div style="font-size:14px;color:{t["sub"]};line-height:26px;margin-top:8px">'
            f'{ion("checkmark",15,t["mint"])} Monétisation activités &amp; channels<br>'
            f'{ion("checkmark",15,t["mint"])} Statistiques avancées<br>'
            f'{ion("checkmark",15,t["mint"])} Badge vérifié<br>'
            f'{ion("checkmark",15,t["mint"])} Virements automatiques</div></div>',
            '<div class=cta>Choisir ce plan</div>'),
        'prescription_preferences': toggles_screen(t, 'Préférences', 'Mes prescriptions', [
            ('Rappels de séance', 'Notifications avant chaque séance', True, 'notifications-outline'),
            ('Plan hebdomadaire', 'Recevoir le programme le lundi', True, 'calendar-outline'),
            ('Conseils du coach', 'Astuces personnalisées', False, 'bulb-outline'),
            ('Suivi nutrition', 'Rappels repas', False, 'nutrition-outline'),
        ]),
        'prescriptions': list_screen(t, 'Mon suivi', 'Prescriptions', 'Plans actifs de ton coach', [
            {'i': 'barbell-outline', 'p': 'Renforcement haut du corps', 's': '3×/semaine · 4 semaines', 'pill': 'Actif', 'pc': 'ok'},
            {'i': 'walk-outline', 'p': 'Endurance run', 's': '2×/semaine · 6 semaines', 'pill': 'Actif', 'pc': 'ok'},
            {'i': 'body-outline', 'p': 'Mobilité & récup', 's': 'Terminé', 'pill': 'Fini'},
        ]),
        'sound_usage': list_screen(t, 'Audio', 'Sons utilisés', 'Pistes de tes peaks', [
            {'i': 'musical-notes-outline', 'p': 'Summer Vibes', 's': 'Utilisé dans 3 peaks', 'chev': True},
            {'i': 'musical-notes-outline', 'p': 'Workout Energy', 's': 'Utilisé dans 2 peaks', 'chev': True},
            {'i': 'musical-notes-outline', 'p': 'Calm Morning', 's': 'Utilisé dans 1 peak', 'chev': True},
        ]),
        'suggest_spot': form_screen(t, 'Contribuer', 'Suggérer un spot', [
            ('Nom du spot', 'Parc de la Villette', False, 'pin-outline'),
            ('Type', 'Course à pied', False, 'walk-outline'),
            ('Localisation', 'Paris 19e', False, 'location-outline'),
            ('Note', 'Boucle de 3 km éclairée', True, 'create-outline'),
        ], 'Envoyer la suggestion', cta_ic='paper-plane-outline'),
        'terms_policies': text_screen(t, 'Légal', 'Conditions & règles', [
            ("Conditions d'utilisation", 'En utilisant Smuppy, tu acceptes nos conditions générales. Le service est fourni pour un usage personnel et sportif…'),
            ('Politique de confidentialité', 'Nous protégeons tes données conformément au RGPD et à la Loi 25. Tu peux exporter ou supprimer tes données à tout moment…'),
            ('Règles communautaires', 'Respect, bienveillance et authenticité. Tout contenu haineux ou trompeur est interdit…'),
        ]),
        'verified_badge': hero_screen(t, 'shield-checkmark', 'Badge vérifié', "Le badge vérifié confirme l'authenticité de ton compte créateur ou business. Réservé aux comptes Pro éligibles.", 'Demander la vérification'),
        'video_recorder': None,  # special, below
        'waiting_room': (
            f'<div class=hero><div class=heroIc style="background:{t["high"]};box-shadow:none">{ion("hourglass-outline",44,t["mint"])}</div>'
            f'<div class=h1>Le live va bientôt commencer</div>'
            f'<div class=sub style="max-width:300px">Coach Fit Pro démarre dans quelques instants. Reste connecté !</div>'
            f'<div class=big style="margin-top:24px;color:{t["mint"]};text-shadow:0 0 18px {GLOW}">02:14</div></div>',
            "<div class=cta>Quitter la salle d'attente</div>"),
        'webview': (
            f'<div style="height:44px;display:flex;align-items:center;gap:10px;padding:0 14px;background:{t["high"]};border-radius:14px;margin-bottom:14px">'
            f'{ion("lock-closed",14,t["sub"])}<span style="font-size:13px;color:{t["sub"]}">smuppy.com/aide</span>'
            f'<span style="margin-left:auto">{ion("reload",16,t["sub"])}</span></div>'
            f'<div class=card style="height:560px;display:flex;align-items:center;justify-content:center;color:{t["sub"]};font-size:14px">Contenu web chargé…</div>', ''),
        'weekly_stats': (
            '<div class=eyebrow>Statistiques</div><div class=h1>Ta semaine</div>'
            '<div class=sub style="margin-bottom:16px">Du 3 au 9 juin</div>'
            f'<div class=card style="padding:18px"><div style="display:flex;justify-content:space-between;text-align:center">'
            f'<div><div class=rs>Distance</div><div class=big style="font-size:26px">24,6</div><div class=rs>km</div></div>'
            f'<div><div class=rs>Séances</div><div class=big style="font-size:26px">5</div><div class=rs>&nbsp;</div></div>'
            f'<div><div class=rs>Calories</div><div class=big style="font-size:26px">3.2k</div><div class=rs>&nbsp;</div></div></div></div>'
            f'<div class=card style="padding:18px"><div class=rp style="margin-bottom:10px">Activité par jour</div>'
            + ''.join(f'<div class=bar><i style="width:{w}%"></i></div>' for w in [40, 70, 30, 90, 55, 80, 20]) + '</div>',
            ''),
    }


def special(t, key):
    if key == 'peak_viewer':
        return (f'<div style="position:absolute;inset:0;background:{MINT_GRAD};display:flex;align-items:flex-end">'
                f'<div style="padding:24px;width:100%"><div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">'
                f'<div class=av style="background:rgba(255,255,255,.25);box-shadow:none">YT</div><div><div class=rp style="color:#fff">@yanis.t</div>'
                f'<div class=rs style="color:rgba(255,255,255,.85)">il y a 2 h</div></div></div>'
                f'<div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:18px">Séance run matinale · 5 km en 22 min</div>'
                f'<div style="display:flex;gap:20px;color:#fff;font-weight:700;align-items:center">'
                f'{ion("heart",22,"#fff")} 248&nbsp;&nbsp;{ion("eye",22,"#fff")} 1.2k</div></div></div>')
    if key == 'video_recorder':
        return (f'<div style="position:absolute;inset:0;background:#000;display:flex;flex-direction:column;justify-content:space-between;padding:24px">'
                f'<div style="display:flex;justify-content:space-between;align-items:center;color:#fff">'
                f'<span style="background:{t["danger"]};padding:6px 12px;border-radius:999px;font-size:12px;font-weight:700">● REC 0:08</span>'
                f'{ion("flash-outline",24,"#fff")}</div>'
                f'<div style="display:flex;align-items:center;justify-content:center;gap:44px">'
                f'{ion("images-outline",26,"#fff")}'
                f'<div style="width:74px;height:74px;border-radius:999px;border:5px solid #fff;background:{t["danger"]}"></div>'
                f'{ion("camera-reverse-outline",26,"#fff")}</div></div>')
    return ''


NAVT = {
    'activity_attendees': 'Participants', 'activity_leaderboard': 'Classement', 'blocked_region': '',
    'blocked_users': 'Comptes bloqués', 'coach_journal': 'Journal', 'data_export': 'Mes données',
    'dispute_center': 'Litiges', 'help': 'Aide', 'kyc_company': 'Vérification', 'match_page': 'Match',
    'muted_users': 'Sourdine', 'my_subscriptions': 'Abonnements', 'payout_onboarding': '',
    'peak_viewer': '', 'premium_plan': 'Premium', 'prescription_preferences': 'Préférences',
    'prescriptions': 'Prescriptions', 'sound_usage': 'Sons', 'suggest_spot': 'Suggérer',
    'terms_policies': 'Légal', 'verified_badge': '', 'video_recorder': '', 'waiting_room': '',
    'webview': 'Aide', 'weekly_stats': 'Statistiques',
}
FULLSCREEN = {'peak_viewer', 'video_recorder'}


def render():
    n = 0
    for dark in (False, True):
        t = theme(dark)
        sc = screens(t)
        for key in NAVT:
            if key in FULLSCREEN:
                body = special(t, key)
                html = (f"<!doctype html><html><head><meta charset=utf-8>"
                        f'<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel=stylesheet>'
                        f"<style>{css(t)}</style></head><body>{body}</body></html>")
            else:
                body, footer = sc[key]
                html = page(t, NAVT[key], body, footer)
            suf = 'dark' if dark else 'light'
            hp = TMP / f'{key}_{suf}.html'
            hp.write_text(html)
            out = OUT / f'{key}_v2_{suf}.png'
            subprocess.run([CHROME, '--headless', '--disable-gpu', '--hide-scrollbars',
                            f'--screenshot={out}', f'--window-size={W},{H}',
                            '--virtual-time-budget=2600', '--force-device-scale-factor=2',
                            str(hp)], capture_output=True)
            n += 1
    print(f'rendered {n} PNG → {OUT}')


if __name__ == '__main__':
    render()
