#!/usr/bin/env python3
"""
build_payments_v2.py — Full PAYMENT surface V2 (founder jun03 decision).

Two opposite money directions, both covered:
  A. BUY premium (user pays, IAP Apple/Google) — restyle V2:
       premium_plans  (Pro Creator $99.99 / Pro Business $49, real prices)
       premium_success (post-purchase → links into payout onboarding = entry #1)
       verified_badge  ($14.99/mo add-on subscription)
  B. RECEIVE money (creator payout, Stripe Connect KYC) — surface the buried flow:
       payout_start    (not_started)   ← KYC maquette #1 state 1
       payout_pending  (in_progress)   ← KYC maquette #1 state 2
       payout_verified (verified)      ← KYC maquette #1 state 3
       channel_payout_banner           ← KYC maquette #2 (banner in creator-config)
       payout_gate_sheet               ← KYC maquette #3 (inline gate bottom-sheet)
       kyc_company                     ← business company KYC (founder: company for pro_business)

Real prices = src/config/iap-products.ts SUBSCRIPTION_PRICES (single source of truth):
  Pro Creator 9999 ($99.99/mo) · Pro Business 4900 ($49/mo) · Verified 1499 ($14.99/mo)
Connect states = connect.ts get-status chargesEnabled/payoutsEnabled.
business_type: individual (personal/pro_creator) · company (pro_business) — connect.ts:190 caveat resolved.

V2 foundation: mint #33A089 (95% UI) · gradient #41AD96→#2C95A0 · Plus Jakarta Sans · dark #000.
Regenerate: python3 build_payments_v2.py   (writes <screen>_<theme>/code.html under OUT)
"""
from pathlib import Path

OUT = Path('/tmp/smuppy-v2-recovery/maquettes/payments_v2')
MINT = '#33A089'
MINT_HI = '#5BB8A6'
MINT_DEEP = '#176A5A'
GRAD_A = '#41AD96'
GRAD_B = '#2C95A0'
WARN = '#E8A33D'   # amber for "config needed"
WARN_BG_D = 'rgba(232,163,61,0.12)'
WARN_BG_L = 'rgba(232,163,61,0.10)'


def theme(dark: bool) -> dict:
    if dark:
        return dict(
            page='#000000', card='#14141A', card_inner='#0F0F14',
            text='#F1F4F6', sub='#8B8B95', section='#6B6B75',
            header='rgba(10,10,12,0.85)', border='rgba(255,255,255,0.06)',
            input_bg='rgba(255,255,255,0.04)', input_border='rgba(255,255,255,0.10)',
            back='#F1F4F6', html='dark', warn_bg=WARN_BG_D, dim='0.5',
        )
    return dict(
        page='#F6F8FA', card='#FFFFFF', card_inner='#FAFBFC',
        text='#0F172A', sub='#64748B', section='#94A3B8',
        header='rgba(255,255,255,0.92)', border='#EEF1F4',
        input_bg='#FFFFFF', input_border='#E5E9EB',
        back='#0E1116', html='light', warn_bg=WARN_BG_L, dim='0.06',
    )


def base_css(t: dict) -> str:
    return f'''
  :root {{
    --mint:{MINT}; --mint-hi:{MINT_HI}; --mint-deep:{MINT_DEEP};
    --grad-a:{GRAD_A}; --grad-b:{GRAD_B}; --warn:{WARN};
    --page:{t['page']}; --card:{t['card']}; --card-inner:{t['card_inner']};
    --text:{t['text']}; --sub:{t['sub']}; --section:{t['section']};
    --border:{t['border']}; --input-bg:{t['input_bg']}; --input-border:{t['input_border']};
    --warn-bg:{t['warn_bg']}; --back:{t['back']};
  }}
  * {{ box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-tap-highlight-color:transparent; margin:0; padding:0; }}
  html {{ background:var(--page); }}
  html, body {{ max-width:100%; overflow-x:hidden; }}
  body {{
    width:393px; height:852px; overflow:hidden; background:var(--page); color:var(--text);
    font-family:'Plus Jakarta Sans',-apple-system,system-ui,sans-serif; font-size:15px; line-height:1.5; position:relative;
  }}
  .scroll {{ height:852px; overflow-y:auto; overflow-x:hidden; }}
  .scroll::-webkit-scrollbar {{ display:none; }}
  .topbar {{ display:grid; grid-template-columns:40px 1fr 40px; align-items:center; padding:54px 16px 10px; }}
  .iconbtn {{ width:40px; height:40px; border:none; background:transparent; display:flex; align-items:center; justify-content:center; cursor:pointer; }}
  .topbar h2 {{ text-align:center; font-size:16px; font-weight:800; color:var(--text); }}
  .pad {{ padding:0 20px; }}
  .gbtn {{ width:100%; padding:16px 0; border:none; border-radius:16px; background:linear-gradient(135deg,var(--grad-a),var(--grad-b));
    color:#fff; font-family:inherit; font-size:15.5px; font-weight:700; cursor:pointer; box-shadow:0 8px 24px rgba(51,160,137,0.28); }}
  .gbtn:disabled {{ background:var(--input-bg); color:var(--sub); box-shadow:none; cursor:not-allowed; }}
  .obtn {{ width:100%; padding:15px 0; border:1.5px solid var(--mint); border-radius:16px; background:transparent;
    color:var(--mint); font-family:inherit; font-size:15px; font-weight:700; cursor:pointer; }}
  .ghostbtn {{ width:100%; padding:13px 0; border:none; border-radius:14px; background:transparent; color:var(--sub);
    font-family:inherit; font-size:14px; font-weight:600; cursor:pointer; }}
  /* Hero icon — DS "shadow contour" : all-around halo (0 0, no offset) + subtle lift + inset rim. */
  .hero-ic {{ width:84px; height:84px; border-radius:26px; display:flex; align-items:center; justify-content:center;
    background:linear-gradient(135deg,var(--grad-a),var(--grad-b)); margin:8px auto 0;
    box-shadow:0 0 32px rgba(51,160,137,0.32), 0 8px 22px rgba(51,160,137,0.20), inset 0 0 0 1px rgba(255,255,255,0.08);
    filter:drop-shadow(0 0 8px rgba(51,160,137,0.22)); }}
  .h1 {{ font-size:24px; font-weight:800; letter-spacing:-.02em; text-align:center; margin-top:18px; }}
  .lead {{ font-size:14px; font-weight:500; color:var(--sub); text-align:center; margin-top:9px; line-height:1.55; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:20px; padding:16px; }}
  .row {{ display:flex; align-items:center; gap:13px; }}
  .step {{ display:flex; align-items:flex-start; gap:13px; padding:13px 0; border-bottom:1px solid var(--border); }}
  .step:last-child {{ border-bottom:none; }}
  .step-ic {{ width:34px; height:34px; border-radius:12px; flex-shrink:0; display:flex; align-items:center; justify-content:center; }}
  .step-tx h4 {{ font-size:14px; font-weight:700; color:var(--text); }}
  .step-tx p {{ font-size:12.5px; font-weight:500; color:var(--sub); margin-top:2px; }}
  .pill {{ display:inline-flex; align-items:center; gap:5px; padding:4px 11px; border-radius:999px; font-size:11px; font-weight:800; }}
  .secure {{ display:flex; align-items:center; justify-content:center; gap:6px; font-size:11.5px; font-weight:600; color:var(--sub); margin-top:16px; }}
  /* warning banner (KYC #2) */
  .banner {{ display:flex; align-items:center; gap:12px; margin:0 20px 14px; padding:13px 14px; border-radius:16px;
    background:var(--warn-bg); border:1px solid rgba(232,163,61,0.30); }}
  .banner-ic {{ width:34px; height:34px; border-radius:11px; background:rgba(232,163,61,0.18); display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
  .banner-tx {{ flex:1; }}
  .banner-tx h4 {{ font-size:13px; font-weight:800; color:var(--warn); }}
  .banner-tx p {{ font-size:11.5px; font-weight:500; color:var(--sub); margin-top:1px; }}
  .banner-cta {{ padding:7px 13px; border:none; border-radius:999px; background:var(--warn); color:#1a1205; font-size:12px; font-weight:800; cursor:pointer; flex-shrink:0; }}
  /* plan cards */
  .plan {{ position:relative; border:1.5px solid var(--border); border-radius:22px; padding:18px; background:var(--card); margin-bottom:13px; }}
  .plan-on {{ border-color:var(--mint); box-shadow:0 0 0 3px rgba(51,160,137,0.14),0 10px 30px rgba(51,160,137,0.12); }}
  .plan-top {{ display:flex; justify-content:space-between; align-items:flex-start; }}
  .plan-name {{ font-size:17px; font-weight:800; }}
  .plan-price b {{ font-size:26px; font-weight:800; letter-spacing:-.02em; }}
  .plan-price span {{ font-size:13px; font-weight:600; color:var(--sub); }}
  .plan-tag {{ position:absolute; top:-10px; right:16px; padding:4px 12px; border-radius:999px; font-size:10.5px; font-weight:800;
    background:linear-gradient(135deg,var(--grad-a),var(--grad-b)); color:#fff; }}
  .feat {{ display:flex; align-items:center; gap:9px; margin-top:10px; font-size:13px; font-weight:500; color:var(--text); }}
  .feat ion-icon {{ color:var(--mint); font-size:17px; flex-shrink:0; }}
  .bignum {{ font-size:40px; font-weight:800; letter-spacing:-.03em; text-align:center; }}
  /* bottom gate sheet */
  .scrim {{ position:absolute; inset:0; background:rgba(0,0,0,.55); display:flex; align-items:flex-end; z-index:50; }}
  .sheet {{ width:100%; background:var(--card); border-radius:26px 26px 0 0; padding:10px 22px 30px; box-shadow:0 -10px 40px rgba(0,0,0,.4); }}
  .handle {{ width:38px; height:4px; border-radius:999px; background:var(--input-border); margin:0 auto 16px; }}
  .field {{ width:100%; padding:14px 15px; border-radius:14px; background:var(--input-bg); border:1px solid var(--input-border);
    color:var(--text); font-family:inherit; font-size:14.5px; font-weight:600; margin-top:10px; }}
  .label {{ font-size:12px; font-weight:800; color:var(--section); letter-spacing:.04em; text-transform:uppercase; margin:16px 0 0; }}
  .iaprow {{ display:flex; align-items:center; justify-content:space-between; padding:14px; border-radius:16px; background:var(--input-bg); border:1px solid var(--input-border); margin-top:14px; }}
'''


def doc(name: str, title: str, dark: bool, css_extra: str, body: str) -> None:
    t = theme(dark)
    html = f'''<!DOCTYPE html>
<html class="{t['html']}" lang="fr"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<title>Smuppy V2 — {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<style>{base_css(t)}{css_extra}</style>
</head><body>
{body}
</body></html>'''
    d = OUT / f'{name}_{"dark" if dark else "light"}'
    d.mkdir(parents=True, exist_ok=True)
    (d / 'code.html').write_text(html, encoding='utf-8')


def back_topbar(title: str) -> str:
    return (f'<div class="topbar"><button class="iconbtn" aria-label="Retour">'
            f'<ion-icon name="arrow-back" style="font-size:24px;color:var(--back)"></ion-icon></button>'
            f'<h2>{title}</h2><span></span></div>')


def secure_line() -> str:
    return ('<div class="secure"><ion-icon name="lock-closed" style="font-size:13px;color:var(--mint)"></ion-icon>'
            'Paiements sécurisés par <b style="color:var(--text);margin-left:3px">Stripe</b></div>')


# ============================================================ A. BUY PREMIUM
# Account-type-specific (mirrors PlatformSubscriptionScreen.tsx:124 — a Pro Creator
# ONLY sees the $99.99 plan, a Pro Business ONLY the $49 plan; never a side-by-side
# picker). One screen per account type → zero confusion, zero duplicate plan.
def _premium_screen(name: str, title_word: str, role_sub: str, price: str,
                    feats: list, cta: str, dark: bool) -> None:
    feat_html = ''.join(f'<div class="feat"><ion-icon name="checkmark-circle"></ion-icon>{f}</div>' for f in feats)
    body = f'''<div class="scroll">
  {back_topbar("Passer Premium")}
  <div class="pad" style="text-align:center">
    <div class="hero-ic"><ion-icon name="rocket" style="font-size:40px;color:#fff"></ion-icon></div>
    <div class="h1">Deviens {title_word} Premium</div>
    <div class="lead">{role_sub}</div>
  </div>
  <div class="pad" style="margin-top:22px">
    <div class="plan plan-on">
      <span class="plan-tag">{title_word.upper()}</span>
      <div class="plan-top">
        <div><div class="plan-name">{title_word} Premium</div>
          <div style="font-size:12.5px;color:var(--sub);font-weight:600;margin-top:2px">Abonnement mensuel · annulable</div></div>
        <div class="plan-price" style="text-align:right"><b>{price}</b><span>/mois</span></div>
      </div>
      {feat_html}
    </div>
  </div>
  <div class="pad" style="margin-top:8px">
    <button class="gbtn">{cta} · {price}/mois</button>
    {secure_line()}
    <p style="font-size:11px;color:var(--sub);text-align:center;margin-top:12px;line-height:1.5">
      Facturé via l'App Store. Renouvellement auto, annulable dans les Réglages. <u>Restaurer mes achats</u></p>
  </div>
  <div style="height:30px"></div>
</div>'''
    doc(name, name.replace('_', ' ').title().replace(' ', ''), dark, '', body)


def screen_premium_creator(dark: bool) -> None:
    _premium_screen(
        'premium_creator', 'Pro Creator',
        'Débloque la monétisation : abonnements de chaîne, lives PPV, sessions 1:1, pourboires.',
        '$99.99', [
            'Abonnements de chaîne (tu fixes le prix)',
            'Lives payants (PPV) + sessions 1:1',
            'Pourboires Smups + cashout Stripe',
            'Statistiques avancées',
        ], 'Devenir Pro Creator Premium', dark)


def screen_premium_business(dark: bool) -> None:
    _premium_screen(
        'premium_business', 'Pro Business',
        'Pour les salles, coachs et studios : réservations, agenda et gestion des membres.',
        '$49', [
            'Réservations + agenda en ligne',
            'Tableau de bord business',
            'Gestion des membres & abonnements',
            'Encaissement Stripe (compte entreprise)',
        ], 'Devenir Pro Business Premium', dark)


def _premium_success(name: str, role_word: str, payout_line: str, dark: bool) -> None:
    body = f'''<div class="scroll">
  <div style="height:96px"></div>
  <div class="pad" style="text-align:center">
    <div class="hero-ic" style="width:96px;height:96px;border-radius:30px"><ion-icon name="trophy" style="font-size:46px;color:#fff"></ion-icon></div>
    <div class="h1" style="font-size:26px">Tu es {role_word} ! 🎉</div>
    <div class="lead">Ton abonnement est actif. Dernière étape pour <b style="color:var(--text)">encaisser tes revenus</b> : configure tes paiements (2 min).</div>
  </div>
  <div class="pad" style="margin-top:26px">
    <div class="card" style="background:linear-gradient(135deg,rgba(51,160,137,0.10),rgba(44,149,160,0.06));border-color:rgba(51,160,137,0.25)">
      <div class="row">
        <div class="step-ic" style="background:rgba(51,160,137,0.16)"><ion-icon name="card" style="font-size:19px;color:var(--mint)"></ion-icon></div>
        <div style="flex:1"><h4 style="font-size:14.5px;font-weight:800">Configurer mes paiements</h4>
          <p style="font-size:12.5px;color:var(--sub);font-weight:500;margin-top:2px">{payout_line}</p></div>
        <ion-icon name="chevron-forward" style="font-size:20px;color:var(--sub)"></ion-icon>
      </div>
    </div>
  </div>
  <div class="pad" style="position:absolute;bottom:34px;left:0;right:0">
    <button class="gbtn">Configurer maintenant</button>
    <button class="ghostbtn" style="margin-top:6px">Plus tard</button>
  </div>
</div>'''
    doc(name, name.replace('_', ' ').title().replace(' ', ''), dark, '', body)


def screen_premium_success_creator(dark: bool) -> None:
    _premium_success('premium_success_creator', 'Pro Creator', 'Identité + compte bancaire via Stripe', dark)


def screen_premium_success_business(dark: bool) -> None:
    _premium_success('premium_success_business', 'Pro Business', 'Infos entreprise + compte bancaire pro via Stripe', dark)


def screen_verified_badge(dark: bool) -> None:
    body = f'''<div class="scroll">
  {back_topbar("Compte vérifié")}
  <div class="pad" style="text-align:center">
    <div class="hero-ic" style="background:linear-gradient(135deg,#3B82F6,#2563EB);{hero_contour('59,130,246')}">
      <ion-icon name="checkmark-circle" style="font-size:46px;color:#fff"></ion-icon></div>
    <div class="h1">Le badge vérifié</div>
    <div class="lead">Confirme ton identité et obtiens le badge bleu. Plus de confiance, plus de visibilité.</div>
  </div>
  <div class="pad" style="margin-top:22px">
    <div class="card">
      <div class="feat"><ion-icon name="shield-checkmark" style="color:#3B82F6"></ion-icon>Badge bleu sur ton profil & tes posts</div>
      <div class="feat"><ion-icon name="trending-up" style="color:#3B82F6"></ion-icon>Priorité dans la recherche & Xplorer</div>
      <div class="feat"><ion-icon name="lock-closed" style="color:#3B82F6"></ion-icon>Protection anti-usurpation du nom</div>
      <div class="feat"><ion-icon name="ribbon" style="color:#3B82F6"></ion-icon>Accès aux fonctionnalités créateur avancées</div>
    </div>
    <div class="card" style="margin-top:13px;display:flex;align-items:center;justify-content:space-between">
      <div><div style="font-size:14px;font-weight:800">Abonnement mensuel</div>
        <div style="font-size:12px;color:var(--sub);font-weight:600">Annulable à tout moment</div></div>
      <div style="text-align:right"><b style="font-size:24px;font-weight:800">$14.99</b><span style="font-size:13px;color:var(--sub);font-weight:600">/mois</span></div>
    </div>
  </div>
  <div class="pad" style="margin-top:18px">
    <button class="gbtn" style="background:linear-gradient(135deg,#3B82F6,#2563EB);box-shadow:0 8px 24px rgba(59,130,246,0.3)">Obtenir le badge · $14.99/mois</button>
    {secure_line()}
  </div>
  <div style="height:24px"></div>
</div>'''
    doc('verified_badge', 'VerifiedBadge', dark, '', body)


# ============================================================ B. RECEIVE (Connect KYC)
def hero_contour(rgba: str) -> str:
    """DS 'shadow contour' for a hero icon in any accent — all-around halo + lift + inset rim."""
    return (f'box-shadow:0 0 32px rgba({rgba},0.32), 0 8px 22px rgba({rgba},0.20), '
            f'inset 0 0 0 1px rgba(255,255,255,0.08); filter:drop-shadow(0 0 8px rgba({rgba},0.22))')


def payout_intro(emoji_ic: str, grad: str, rgba: str = '51,160,137') -> str:
    return (f'<div class="hero-ic" style="background:{grad};{hero_contour(rgba)}">'
            f'<ion-icon name="{emoji_ic}" style="font-size:40px;color:#fff"></ion-icon></div>')


def screen_payout_start(dark: bool) -> None:
    body = f'''<div class="scroll">
  {back_topbar("Mes paiements")}
  <div class="pad" style="text-align:center">
    {payout_intro("wallet", "linear-gradient(135deg,var(--grad-a),var(--grad-b))")}
    <div class="h1">Configure tes paiements</div>
    <div class="lead">Pour encaisser tes abonnements, lives et pourboires, vérifie ton identité et ajoute ton compte bancaire. 2 minutes, via Stripe.</div>
  </div>
  <div class="pad" style="margin-top:22px">
    <div class="card">
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="person" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Ton identité</h4><p>Nom, date de naissance, pièce d'identité</p></div></div>
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="business" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Ton compte bancaire</h4><p>IBAN pour recevoir tes virements</p></div></div>
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="cash" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Et c'est tout</h4><p>Virements automatiques chaque semaine</p></div></div>
    </div>
  </div>
  <div class="pad" style="margin-top:18px">
    <button class="gbtn">Commencer la configuration</button>
    {secure_line()}
    <p style="font-size:11px;color:var(--sub);text-align:center;margin-top:10px">Tu seras redirigé vers Stripe, notre partenaire de paiement.</p>
  </div>
  <div style="height:24px"></div>
</div>'''
    doc('payout_start', 'PayoutStart', dark, '', body)


def screen_payout_pending(dark: bool) -> None:
    body = f'''<div class="scroll">
  {back_topbar("Mes paiements")}
  <div class="pad" style="text-align:center">
    {payout_intro("hourglass", "linear-gradient(135deg,#E8A33D,#D98520)", "232,163,61")}
    <div class="h1">Vérification en cours</div>
    <div class="lead">Stripe vérifie tes informations. Ça prend généralement quelques minutes, parfois jusqu'à 24 h.</div>
  </div>
  <div class="pad" style="margin-top:22px">
    <div class="card">
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="checkmark-circle" style="font-size:18px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Identité</h4><p>Vérifiée</p></div>
        <span class="pill" style="margin-left:auto;background:rgba(51,160,137,0.14);color:var(--mint)">OK</span></div>
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="checkmark-circle" style="font-size:18px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Compte bancaire</h4><p>Ajouté</p></div>
        <span class="pill" style="margin-left:auto;background:rgba(51,160,137,0.14);color:var(--mint)">OK</span></div>
      <div class="step"><div class="step-ic" style="background:var(--warn-bg)"><ion-icon name="hourglass" style="font-size:16px;color:var(--warn)"></ion-icon></div>
        <div class="step-tx"><h4>Revue finale</h4><p>En cours de vérification par Stripe</p></div>
        <span class="pill" style="margin-left:auto;background:var(--warn-bg);color:var(--warn)">En revue</span></div>
    </div>
    <p style="font-size:12px;color:var(--sub);text-align:center;margin-top:16px">On te notifie dès que tu peux encaisser. Tu peux continuer à publier en attendant.</p>
  </div>
  <div class="pad" style="margin-top:16px">
    <button class="obtn"><ion-icon name="refresh" style="font-size:17px;vertical-align:middle;margin-right:6px"></ion-icon>Rafraîchir le statut</button>
  </div>
</div>'''
    doc('payout_pending', 'PayoutPending', dark, '', body)


def screen_payout_verified(dark: bool) -> None:
    body = f'''<div class="scroll">
  {back_topbar("Mes paiements")}
  <div class="pad">
    <div class="card" style="background:linear-gradient(135deg,var(--grad-a),var(--grad-b));border:none;text-align:center;padding:24px 16px;box-shadow:0 14px 38px rgba(51,160,137,0.3)">
      <div style="display:inline-flex;align-items:center;gap:6px;padding:5px 13px;border-radius:999px;background:rgba(255,255,255,0.2);color:#fff;font-size:11.5px;font-weight:800">
        <ion-icon name="checkmark-circle" style="font-size:14px"></ion-icon>VÉRIFIÉ · TU PEUX ENCAISSER</div>
      <div style="color:rgba(255,255,255,0.85);font-size:12.5px;font-weight:600;margin-top:16px">Solde disponible</div>
      <div class="bignum" style="color:#fff;margin-top:2px">$248.50</div>
      <div style="color:rgba(255,255,255,0.8);font-size:12px;font-weight:500;margin-top:4px">+$32.00 en attente · prochain virement vendredi</div>
    </div>
  </div>
  <div class="pad" style="margin-top:14px">
    <button class="gbtn"><ion-icon name="arrow-down-circle" style="font-size:18px;vertical-align:middle;margin-right:6px"></ion-icon>Retirer maintenant</button>
  </div>
  <div class="pad" style="margin-top:13px">
    <div class="card" style="padding:6px 16px">
      <div class="row" style="padding:13px 0;border-bottom:1px solid var(--border)">
        <ion-icon name="stats-chart" style="font-size:19px;color:var(--mint)"></ion-icon>
        <span style="flex:1;font-size:14px;font-weight:600">Tableau de bord Stripe</span>
        <ion-icon name="open-outline" style="font-size:17px;color:var(--sub)"></ion-icon></div>
      <div class="row" style="padding:13px 0;border-bottom:1px solid var(--border)">
        <ion-icon name="business" style="font-size:19px;color:var(--mint)"></ion-icon>
        <span style="flex:1;font-size:14px;font-weight:600">Compte bancaire</span>
        <span style="font-size:13px;color:var(--sub);font-weight:600">•••• 4291</span></div>
      <div class="row" style="padding:13px 0">
        <ion-icon name="time" style="font-size:19px;color:var(--mint)"></ion-icon>
        <span style="flex:1;font-size:14px;font-weight:600">Historique des virements</span>
        <ion-icon name="chevron-forward" style="font-size:18px;color:var(--sub)"></ion-icon></div>
    </div>
    {secure_line()}
  </div>
  <div style="height:24px"></div>
</div>'''
    doc('payout_verified', 'PayoutVerified', dark, '', body)


def screen_payout_gate_sheet(dark: bool) -> None:
    """KYC #3 — inline gate bottom-sheet over a dimmed Go-Live screen."""
    body = f'''<div class="scroll" style="filter:blur(1px)">
  {back_topbar("Démarrer un live")}
  <div class="pad">
    <div class="card" style="aspect-ratio:9/12;display:flex;align-items:center;justify-content:center;background:var(--card-inner)">
      <ion-icon name="videocam" style="font-size:54px;color:var(--sub);opacity:.5"></ion-icon>
    </div>
    <div class="label">Type de live</div>
    <div class="iaprow"><div style="font-size:14px;font-weight:700">Live payant (PPV)</div>
      <div style="font-size:14px;font-weight:800;color:var(--mint)">$4.99</div></div>
  </div>
</div>
<div class="scrim">
  <div class="sheet">
    <div class="handle"></div>
    <div style="text-align:center">
      <div class="step-ic" style="width:56px;height:56px;border-radius:18px;background:var(--warn-bg);margin:0 auto 14px">
        <ion-icon name="card" style="font-size:26px;color:var(--warn)"></ion-icon></div>
      <h3 style="font-size:19px;font-weight:800">Termine ta config paiements</h3>
      <p style="font-size:13.5px;color:var(--sub);font-weight:500;margin-top:8px;line-height:1.5">
        Pour lancer un live payant et recevoir l'argent, vérifie d'abord ton identité et ton compte bancaire.</p>
    </div>
    <div style="margin-top:20px">
      <button class="gbtn">Configurer mes paiements</button>
      <button class="ghostbtn" style="margin-top:4px">Plus tard</button>
    </div>
  </div>
</div>'''
    doc('payout_gate_sheet', 'PayoutGateSheet', dark, '', body)


def screen_kyc_company(dark: bool) -> None:
    """Business company KYC (founder: company for pro_business)."""
    body = f'''<div class="scroll">
  {back_topbar("Paiements business")}
  <div class="pad" style="text-align:center">
    {payout_intro("business", "linear-gradient(135deg,var(--grad-a),var(--grad-b))")}
    <div class="h1">Vérifie ton entreprise</div>
    <div class="lead">Ton compte Pro Business encaisse au nom de ta société. Stripe a besoin des infos légales de l'entreprise.</div>
  </div>
  <div class="pad" style="margin-top:20px">
    <span class="pill" style="background:rgba(51,160,137,0.12);color:var(--mint)"><ion-icon name="briefcase" style="font-size:12px"></ion-icon>TYPE : ENTREPRISE (COMPANY)</span>
    <div class="card" style="margin-top:12px;padding:6px 14px">
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="document-text" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>N° d'immatriculation</h4><p>SIRET / registre du commerce</p></div></div>
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="person-circle" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Représentant légal</h4><p>Identité du dirigeant + bénéficiaires</p></div></div>
      <div class="step"><div class="step-ic" style="background:rgba(51,160,137,0.14)"><ion-icon name="business" style="font-size:17px;color:var(--mint)"></ion-icon></div>
        <div class="step-tx"><h4>Compte bancaire pro</h4><p>IBAN au nom de l'entreprise</p></div></div>
    </div>
    <div class="card" style="margin-top:12px;display:flex;gap:10px;align-items:flex-start;background:var(--warn-bg);border-color:rgba(232,163,61,0.25)">
      <ion-icon name="information-circle" style="font-size:18px;color:var(--warn);flex-shrink:0;margin-top:1px"></ion-icon>
      <p style="font-size:12px;color:var(--sub);font-weight:500">Créateur individuel ? Repasse en Pro Creator pour une vérification simplifiée (particulier).</p>
    </div>
  </div>
  <div class="pad" style="margin-top:18px">
    <button class="gbtn">Vérifier mon entreprise</button>
    {secure_line()}
  </div>
  <div style="height:24px"></div>
</div>'''
    doc('kyc_company', 'KycCompany', dark, '', body)


SCREENS = [
    screen_premium_creator, screen_premium_business,
    screen_premium_success_creator, screen_premium_success_business,
    screen_verified_badge,
    screen_payout_start, screen_payout_pending, screen_payout_verified,
    screen_payout_gate_sheet, screen_kyc_company,
]
# NOTE: the "configure ta chaîne" payout banner is NOT a separate screen here —
# it lives ON the real channel-setup screen (build_creator_config_v2.py
# screen_channel) to avoid duplicating an existing screen (directive #8/#22).


def main() -> None:
    n = 0
    for fn in SCREENS:
        for dark in (True, False):
            fn(dark)
            n += 1
    print(f'✅ {n} files written → {OUT}')
    print('Screens:', ', '.join(fn.__name__.replace('screen_', '') for fn in SCREENS))


if __name__ == '__main__':
    main()
