"""Smuppy V2 — AUTH category canonical maquettes (Sprint P0).
13 screens × 2 themes = 26 HTML maquettes at 393×852 device format.

Uses REAL SmuppyLogo SVG paths from src/components/SmuppyLogo.tsx
+ REAL i18n texts from src/i18n/locales/fr/auth.json
"""

import json
from pathlib import Path

MINT = '#33A089'
MINT_HI = '#41AD96'
MINT_DEEP = '#2C95A0'
DANGER = '#EF4444'

OUT_DIR = Path('/tmp/smuppy-v2-recovery/maquettes/harmonized')

# ─── Real SVG paths from src/components/SmuppyLogo.tsx ─────────
_PATHS = json.loads(Path('/tmp/smuppy_paths.json').read_text())
ICON_BG_PATH = _PATHS['icon_bg']
ICON_S_PATH = _PATHS['icon_s']
TEXT_PATH = _PATHS['text']

# ─── Real i18n texts from src/i18n/locales/fr/auth.json ────────
i18n_auth = json.loads(Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/auth.json').read_text())
i18n_common = json.loads(Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/common.json').read_text()) if Path('/Users/noussaier/smuppy-mobile/src/i18n/locales/fr/common.json').exists() else {}


def theme(dark: bool) -> dict:
    if dark:
        return dict(
            page='#000000', card='#14141A', text='#F1F4F6', sub='#8B8B95',
            section='#6B6B75', header='rgba(10,10,12,0.85)',
            border='rgba(255,255,255,0.06)',
            input_bg='rgba(255,255,255,0.04)', input_border='rgba(255,255,255,0.10)',
            back='#F1F4F6', html='dark', tog_off='#2E2E38', dim_shadow='0.5',
            hero_overlay_top='rgba(0,0,0,0.10)', hero_overlay_bot='rgba(0,0,0,0.85)',
            social_bg='#14141A',
        )
    return dict(
        page='#F6F8FA', card='#FFFFFF', text='#0F172A', sub='#64748B',
        section='#94A3B8', header='rgba(255,255,255,0.92)', border='#EEF1F4',
        input_bg='#FFFFFF', input_border='#E5E9EB',
        back='#0E1116', html='light', tog_off='#E2E8F0', dim_shadow='0.06',
        hero_overlay_top='rgba(255,255,255,0.0)', hero_overlay_bot='rgba(0,0,0,0.45)',
        social_bg='#FFFFFF',
    )


# ─── Logo helpers (real SVG paths) ─────────────────────────────


def smuppy_icon(size: int = 50, variant: str = 'gradient') -> str:
    """Real SmuppyIcon SVG — 74x74 viewBox."""
    if variant == 'gradient':
        bg_fill = 'url(#iconBgG)'; s_fill = 'url(#iconSDk)'
    elif variant == 'dark':
        bg_fill = '#0A252F'; s_fill = 'url(#iconSGr)'
    else:  # white
        bg_fill = 'white'; s_fill = 'url(#iconSDk)'
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 74 74" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="iconBgG" x1="0" y1="0" x2="57.9282" y2="80.0519" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0EBF8A"/><stop offset="1" stop-color="#2C95A0"/>
    </linearGradient>
    <linearGradient id="iconSDk" x1="3.00305" y1="36.9755" x2="50.033" y2="35.7238" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#134456"/><stop offset="0.701923" stop-color="#0A252F"/>
    </linearGradient>
    <linearGradient id="iconSGr" x1="18" y1="16" x2="55" y2="58" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0EBF8A"/><stop offset="1" stop-color="#2C95A0"/>
    </linearGradient>
  </defs>
  <path d="{ICON_BG_PATH}" fill="{bg_fill}"/>
  <path d="{ICON_S_PATH}" fill="{s_fill}"/>
</svg>'''


def smuppy_text(width: int = 120, variant: str = 'gradient') -> str:
    """Real SmuppyText SVG — 215x46 viewBox."""
    h = width * 46 / 215
    if variant == 'white':
        fill = 'white'
    elif variant == 'dark':
        fill = 'url(#textDkG)'
    else:
        fill = 'url(#textG)'
    return f'''<svg width="{width}" height="{h}" viewBox="0 0 215 46" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="textG" x1="0" y1="0" x2="11.5723" y2="74.4849" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0EBF8A"/><stop offset="1" stop-color="#2C95A0"/>
    </linearGradient>
    <linearGradient id="textDkG" x1="-87.1345" y1="22.9746" x2="177.596" y2="-13.1995" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#134456"/><stop offset="0.701923" stop-color="#0A252F"/>
    </linearGradient>
  </defs>
  <path d="{TEXT_PATH}" fill="{fill}"/>
</svg>'''


def smuppy_full(icon_size: int = 36, text_width: int = 100, dark: bool = True) -> str:
    """Icon + text horizontal. Logo VERT en dark, NOIR en light (founder jun03)."""
    variant = 'gradient' if dark else 'dark'
    return (f'<span class="smuppy-full">'
            f'{smuppy_icon(icon_size, variant)}'
            f'{smuppy_text(text_width, variant)}'
            f'</span>')


def smuppy_stacked(icon_size: int = 80, text_width: int = 150, dark: bool = True) -> str:
    """Icon above text. Logo VERT en dark, NOIR en light (founder jun03)."""
    variant = 'gradient' if dark else 'dark'
    return (f'<div class="smuppy-stacked">'
            f'{smuppy_icon(icon_size, variant)}'
            f'{smuppy_text(text_width, variant)}'
            f'</div>')


# ─── UI atoms ────────────────────────────────────────────────


def primary_cta(label: str) -> str:
    return f'<button class="cta-primary"><span>{label}</span></button>'


def ghost_cta(label: str) -> str:
    return f'<button class="cta-ghost">{label}</button>'


def social_btn(provider: str, label: str) -> str:
    if provider == 'google':
        ic = '<span class="social-ic" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg></span>'
    else:  # apple
        ic = '<span class="social-ic" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/></svg></span>'
    return f'<button class="social-btn">{ic}<span>{label}</span></button>'


def input_field(label: str, value: str = '', placeholder: str = '', focused: bool = False, error: str = None, icon: str = None, trailing: str = None) -> str:
    focus_cls = ' v2-input-focus' if focused else ''
    err_cls = ' v2-input-error' if error else ''
    err_html = f'<div class="v2-input-err">{error}</div>' if error else ''
    icon_html = f'<ion-icon name="{icon}" class="v2-input-icon"></ion-icon>' if icon else ''
    trail_html = f'<span class="v2-input-trail">{trailing}</span>' if trailing else ''
    pad_cls = ' has-icon' if icon else ''
    val_or_ph = (f'<span class="v2-input-value">{value}</span>'
                 if value else f'<span class="v2-input-placeholder">{placeholder}</span>')
    return f'''<label class="v2-input-label">
  <span class="v2-input-lbl-txt">{label}</span>
  <div class="v2-input{focus_cls}{err_cls}{pad_cls}">
    {icon_html}{val_or_ph}{trail_html}
  </div>
  {err_html}
</label>'''


def back_button() -> str:
    return '''<button class="v2-back" aria-label="Retour">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
</button>'''


def close_button() -> str:
    return '''<button class="v2-back" aria-label="Fermer">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
</button>'''


def onb_header(step: int, total: int, back: bool = True) -> str:
    pct = (step / total) * 100
    back_html = back_button() if back else '<span style="width:40px"></span>'
    return f'''<header class="onb-header">
  {back_html}
  <div class="onb-progress"><div class="onb-progress-bar" style="width:{pct}%"></div></div>
  <div class="onb-step">{step}/{total}</div>
</header>'''


def code_input(filled: list = None) -> str:
    """6-digit OTP code input grid. `filled` = list of chars for each cell."""
    filled = filled or []
    cells = ''
    for i in range(6):
        if i < len(filled):
            cells += f'<div class="code-cell code-cell-filled">{filled[i]}</div>'
        elif i == len(filled):
            cells += '<div class="code-cell code-cell-focus"><span class="code-cursor"></span></div>'
        else:
            cells += '<div class="code-cell"></div>'
    return f'<div class="code-grid">{cells}</div>'


# ─── i18n shortcuts ────────────────────────────────────────────

def t(*keys):
    """Lookup i18n key path."""
    d = i18n_auth
    for k in keys:
        d = d.get(k, '?')
    return d


# ─── SCREEN BODIES ──────────────────────────────────────────


def screen_welcome(th: dict) -> str:
    return f'''<div class="welcome-bg">
  <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=900&h=1700&fit=crop&q=80" alt="" class="welcome-hero-img"/>
  <div class="welcome-overlay"></div>
</div>
<div class="welcome-content">
  <div class="welcome-top-spacer"></div>
  <div class="welcome-brand">
    <div class="welcome-title">{t('welcome','title')}</div>
    {smuppy_stacked(icon_size=88, text_width=180, dark=th['html']=='dark')}
    <p class="welcome-tagline">{t('welcome','tagline').replace(chr(10), '<br/>')}</p>
  </div>
  <div class="welcome-stats">
    <div class="welcome-stat"><span class="welcome-stat-num">10K+</span><span class="welcome-stat-lbl">{t('welcome','statAthletes').lower()}</span></div>
    <div class="welcome-stat-divider"></div>
    <div class="welcome-stat"><span class="welcome-stat-num">50K+</span><span class="welcome-stat-lbl">{t('welcome','statPeaks').lower()}</span></div>
    <div class="welcome-stat-divider"></div>
    <div class="welcome-stat"><span class="welcome-stat-num">1K+</span><span class="welcome-stat-lbl">{t('welcome','statGyms').lower()}</span></div>
  </div>
  <div class="welcome-actions">
    {primary_cta(t('welcome','createAccount'))}
    {ghost_cta(t('welcome','logIn'))}
    <p class="welcome-tos">En continuant tu acceptes nos <b>Conditions</b> &amp; <b>Politique</b></p>
  </div>
</div>'''


def screen_login(th: dict) -> str:
    return f'''<header class="auth-topbar"><span style="width:40px"></span><span style="width:40px"></span></header>
<main class="auth-main">
  <div class="auth-brand-row">{smuppy_full(icon_size=36, text_width=110, dark=th['html']=='dark')}</div>
  <h1 class="auth-title">{t('login','title')}</h1>
  <p class="auth-sub">{t('login','subtitle')}</p>

  <div class="auth-form">
    {input_field(t('login','emailLabel'), value='sara.khan@yoga.co', icon='mail-outline')}
    {input_field(t('login','passwordLabel'), value='••••••••••', icon='lock-closed-outline', trailing='<button class="v2-input-trail-btn">'+t('login','showPassword')+'</button>')}

    <div class="auth-row-between">
      <label class="auth-remember">
        <span class="auth-checkbox auth-checkbox-on"><ion-icon name="checkmark" style="font-size:14px;color:#fff"></ion-icon></span>
        Se souvenir de moi
      </label>
      <button class="auth-link">{t('login','forgotPassword')}</button>
    </div>

    {primary_cta(t('login','logIn'))}
  </div>

  <div class="auth-divider">
    <span class="auth-divider-line"></span>
    <span class="auth-divider-txt">ou continuer avec</span>
    <span class="auth-divider-line"></span>
  </div>

  <div class="auth-social">
    {social_btn('google', 'Google')}
    {social_btn('apple', 'Apple')}
  </div>

  <p class="auth-footer">
    {t('login','noAccount')}
    <button class="auth-link auth-link-strong">{t('login','signUp')}</button>
  </p>
</main>'''


def screen_signup(th: dict) -> str:
    return f'''<header class="auth-topbar"><span style="width:40px"></span><span style="width:40px"></span></header>
<main class="auth-main">
  <div class="auth-brand-row">{smuppy_full(icon_size=36, text_width=110, dark=th['html']=='dark')}</div>
  <h1 class="auth-title">{t('signup','title')}</h1>
  <p class="auth-sub">{t('signup','subtitle')}</p>

  <div class="auth-form">
    {input_field(t('signup','emailLabel'), value='ton@email.com', icon='mail-outline')}
    {input_field(t('signup','passwordLabel'), value='••••••••••••', icon='lock-closed-outline', trailing='<button class="v2-input-trail-btn">'+t('signup','showPassword').replace('Afficher le mot de passe','Afficher')+'</button>')}

    <div class="auth-pwd-strength">
      <div class="auth-pwd-strength-bar"><div class="auth-pwd-strength-fill auth-pwd-strength-strong" style="width:90%"></div></div>
      <span class="auth-pwd-strength-lbl">Mot de passe fort</span>
    </div>

    <p class="auth-pwd-must">{t('signup','passwordMustContain')}</p>
    <div class="auth-pwd-reqs">
      <div class="auth-pwd-req auth-pwd-req-ok"><ion-icon name="checkmark-circle" style="font-size:14px;color:{MINT}"></ion-icon> 10+ caractères</div>
      <div class="auth-pwd-req auth-pwd-req-ok"><ion-icon name="checkmark-circle" style="font-size:14px;color:{MINT}"></ion-icon> 1 majuscule</div>
      <div class="auth-pwd-req auth-pwd-req-ok"><ion-icon name="checkmark-circle" style="font-size:14px;color:{MINT}"></ion-icon> 1 chiffre</div>
      <div class="auth-pwd-req"><ion-icon name="ellipse-outline" style="font-size:14px;color:var(--sub)"></ion-icon> 1 caractère spécial</div>
    </div>

    <label class="auth-remember auth-terms">
      <span class="auth-checkbox auth-checkbox-on"><ion-icon name="checkmark" style="font-size:14px;color:#fff"></ion-icon></span>
      <span>{t('signup','agreeTermsPrefix')}<b>{t('signup','termsAndConditions')}</b> &amp; la <b>{t('signup','privacyPolicy')}</b></span>
    </label>

    {primary_cta(t('signup','getStarted'))}
  </div>

  <div class="auth-divider">
    <span class="auth-divider-line"></span>
    <span class="auth-divider-txt">ou continuer avec</span>
    <span class="auth-divider-line"></span>
  </div>

  <div class="auth-social">
    {social_btn('google', 'Google')}
    {social_btn('apple', 'Apple')}
  </div>

  <p class="auth-footer">
    {t('signup','alreadyHaveAccount')}
    <button class="auth-link auth-link-strong">{t('signup','logIn')}</button>
  </p>
</main>'''


def screen_forgot_password(th: dict) -> str:
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main auth-main-tight">
  <div class="auth-brand-row">{smuppy_full(icon_size=36, text_width=110, dark=th['html']=='dark')}</div>
  <div class="auth-icon-circle">
    <ion-icon name="lock-closed" style="font-size:30px;color:{MINT}"></ion-icon>
  </div>
  <h1 class="auth-title">{t('forgotPassword','title')}</h1>
  <p class="auth-sub">{t('forgotPassword','subtitle')}</p>

  <div class="auth-form">
    {input_field(t('forgotPassword','emailLabel'), placeholder=t('forgotPassword','emailPlaceholder'), icon='mail-outline')}
    {primary_cta(t('forgotPassword','sendLink'))}
  </div>

  <p class="auth-footer">
    Tu te souviens ?
    <button class="auth-link auth-link-strong">Se connecter</button>
  </p>
</main>'''


def screen_check_email(th: dict) -> str:
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main auth-main-tight">
  <div class="auth-icon-circle">
    <ion-icon name="mail-open" style="font-size:30px;color:{MINT}"></ion-icon>
  </div>
  <h1 class="auth-title">{t('checkEmail','title')}</h1>
  <p class="auth-sub">{t('checkEmail','subtitle')}<br/><b style="color:var(--text)">s***@yoga.co</b></p>

  <div class="auth-steps">
    <div class="auth-step"><span class="auth-step-num">1</span><span>{t('checkEmail','step1')}</span></div>
    <div class="auth-step"><span class="auth-step-num">2</span><span>{t('checkEmail','step2')}</span></div>
    <div class="auth-step"><span class="auth-step-num">3</span><span>{t('checkEmail','step3')}</span></div>
  </div>

  <div class="auth-form">
    {primary_cta(t('checkEmail','iHaveCode'))}
    <button class="auth-link-row">{t('checkEmail','resendCodeIn').format(seconds=27)}</button>
  </div>

  <p class="auth-footer">
    <button class="auth-link auth-link-strong">{t('checkEmail','backToLogin')}</button>
  </p>
</main>'''


def screen_verify_code(th: dict) -> str:
    return f'''{onb_header(2, 3, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{t('verifyCode','title')}</h1>
  <p class="auth-sub">{t('verifyCode','subtitle')}<br/><b style="color:var(--text)">ton@email.com</b></p>

  {code_input(filled=['4','7','2'])}

  <div class="auth-form">
    {primary_cta(t('verifyCode','enterCode'))}
    <button class="auth-link-row">{t('verifyCode','resendCode')}</button>
  </div>

  <p class="auth-sub auth-sub-small">{t('verifyCode','noCode')}</p>
</main>'''


def screen_reset_code(th: dict) -> str:
    return f'''{onb_header(2, 4, back=True)}
<main class="auth-main auth-main-onb">
  <h1 class="auth-title">{t('resetCode','title')}</h1>
  <p class="auth-sub">{t('resetCode','subtitle')}<br/><b style="color:var(--text)">s***@yoga.co</b></p>

  {code_input(filled=['4','7','2','9'])}

  <div class="auth-form">
    {primary_cta('Vérifier le code')}
    <button class="auth-link-row">{t('resetCode','resendCode')}</button>
  </div>

  <p class="auth-sub auth-sub-small">{t('resetCode','noCode')}</p>
</main>'''


def screen_new_password(th: dict) -> str:
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main">
  <div class="auth-icon-circle">
    <ion-icon name="key" style="font-size:30px;color:{MINT}"></ion-icon>
  </div>
  <h1 class="auth-title">{t('newPassword','title')}</h1>
  <p class="auth-sub">{t('newPassword','subtitle')}</p>

  <div class="auth-form">
    {input_field(t('newPassword','title').replace('Créer un ','').capitalize(), value='••••••••••••', icon='lock-closed-outline')}

    <div class="auth-pwd-strength">
      <div class="auth-pwd-strength-bar"><div class="auth-pwd-strength-fill auth-pwd-strength-strong" style="width:85%"></div></div>
      <span class="auth-pwd-strength-lbl">Mot de passe fort</span>
    </div>

    {input_field(t('newPassword','confirmLabel'), value='••••••••••••', icon='lock-closed-outline')}
    <p class="auth-helper auth-helper-ok"><ion-icon name="checkmark-circle" style="font-size:14px;color:{MINT}"></ion-icon> {t('newPassword','passwordsMatch')}</p>

    {primary_cta(t('newPassword','resetPassword'))}
  </div>
</main>'''


def screen_password_success(th: dict) -> str:
    return f'''<div class="success-wrap">
  <div class="success-confetti"></div>
  <div class="success-check">
    <div class="success-check-ring"></div>
    <ion-icon name="checkmark" class="success-check-icon"></ion-icon>
  </div>
  <h1 class="success-title">{t('passwordSuccess','title')}</h1>
  <p class="success-body">{t('passwordSuccess','subtitle')}</p>
  <div class="success-loader">
    <span class="success-spinner"></span>
    <span>{t('passwordSuccess','entering')}</span>
  </div>
</div>'''


def screen_email_verification_pending(th: dict) -> str:
    return f'''<header class="auth-topbar">{close_button()}<span style="width:40px"></span></header>
<main class="auth-main auth-main-tight">
  <div class="auth-icon-circle">
    <ion-icon name="mail" style="font-size:30px;color:{MINT}"></ion-icon>
  </div>
  <h1 class="auth-title">{t('verifyEmail','title')}</h1>
  <p class="auth-sub">{t('verifyEmail','subtitle')}<br/><b style="color:var(--text)">ton@email.com</b></p>

  <div class="auth-steps">
    <p class="auth-step-prelude">{t('verifyEmail','toContinue')}</p>
    <div class="auth-step"><span class="auth-step-num">1</span><span>{t('verifyEmail','step1')}</span></div>
    <div class="auth-step"><span class="auth-step-num">2</span><span>{t('verifyEmail','step2')}</span></div>
    <div class="auth-step"><span class="auth-step-num">3</span><span>{t('verifyEmail','step3')}</span></div>
  </div>

  <div class="auth-form">
    {primary_cta(t('verifyEmail','iVerified'))}
    <button class="auth-link-row">{t('verifyEmail','resendEmail')}</button>
  </div>

  <button class="auth-link auth-link-small">{t('verifyEmail','signOutDifferent')}</button>
</main>'''


def screen_mfa_enroll_prompt(th: dict) -> str:
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main">
  <div class="auth-icon-circle auth-icon-circle-lg">
    <ion-icon name="shield-checkmark" style="font-size:38px;color:{MINT}"></ion-icon>
  </div>
  <h1 class="auth-title auth-title-lg">{t('mfa','enrollPrompt','title')}</h1>
  <p class="auth-sub">{t('mfa','enrollPrompt','body')}</p>

  <div class="auth-mfa-apps">
    <p class="auth-mfa-apps-label">Apps compatibles</p>
    <div class="auth-mfa-app-row">
      <span class="auth-mfa-app">Google Authenticator</span>
      <span class="auth-mfa-app">Authy</span>
    </div>
    <div class="auth-mfa-app-row">
      <span class="auth-mfa-app">1Password</span>
      <span class="auth-mfa-app">Bitwarden</span>
    </div>
  </div>

  <div class="auth-form">
    {primary_cta(t('mfa','enrollPrompt','ctaActivate'))}
    {ghost_cta(t('mfa','enrollPrompt','ctaLater'))}
  </div>
</main>'''


def screen_mfa_enroll_qr(th: dict) -> str:
    qr_url = 'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=otpauth://totp/Smuppy:sara&secret=ABCDEFGHIJKLMNOP&issuer=Smuppy'
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main">
  <h1 class="auth-title">{t('mfa','enrollQR','title')}</h1>
  <p class="auth-sub">{t('mfa','enrollQR','scanInstruction')}</p>

  <div class="auth-qr-frame">
    <img src="{qr_url}" alt="QR" class="auth-qr-img"/>
  </div>

  <div class="auth-manual">
    <p class="auth-manual-label">{t('mfa','enrollQR','manualCodeLabel')}</p>
    <div class="auth-manual-code">
      <span class="auth-manual-code-val">ABCD EFGH IJKL MNOP</span>
      <button class="auth-manual-copy"><ion-icon name="copy-outline" style="font-size:16px"></ion-icon> {t('mfa','enrollQR','copyCode')}</button>
    </div>
  </div>

  <p class="auth-step-prelude">{t('mfa','enrollQR','codeLabel')}</p>
  {code_input(filled=['8','1','5'])}

  <div class="auth-form">
    {primary_cta(t('mfa','enrollQR','verify'))}
  </div>
</main>'''


def screen_mfa_enroll_backup_codes(th: dict) -> str:
    codes = ['8X4P-2WJN', 'KM7R-9DLZ', 'B6FT-1QCV', 'PH3A-NXG2', 'YE5W-6JMU', 'RS2L-DKB7']
    code_list = ''.join(f'<div class="auth-backup-code"><span class="auth-backup-num">{i+1}.</span><span class="auth-backup-val">{c}</span></div>' for i, c in enumerate(codes))
    return f'''<header class="auth-topbar">{back_button()}<span style="width:40px"></span></header>
<main class="auth-main">
  <h1 class="auth-title">{t('mfa','backupCodes','title')}</h1>
  <p class="auth-sub auth-warn"><ion-icon name="warning" style="font-size:16px;color:#F59E0B;vertical-align:middle"></ion-icon> {t('mfa','backupCodes','warning')}</p>

  <div class="auth-backup-grid">
    {code_list}
  </div>

  <div class="auth-backup-actions">
    <button class="auth-backup-btn"><ion-icon name="copy-outline" style="font-size:16px"></ion-icon> {t('mfa','backupCodes','copyAll')}</button>
    <button class="auth-backup-btn"><ion-icon name="share-outline" style="font-size:16px"></ion-icon> {t('mfa','backupCodes','share')}</button>
  </div>

  <label class="auth-remember auth-terms">
    <span class="auth-checkbox auth-checkbox-on"><ion-icon name="checkmark" style="font-size:14px;color:#fff"></ion-icon></span>
    {t('mfa','backupCodes','confirmLabel')}
  </label>

  <div class="auth-form">
    {primary_cta(t('mfa','backupCodes','continue'))}
  </div>
</main>'''


SCREENS = {
    'auth_welcome_v2': ('Welcome', screen_welcome),
    'auth_login_v2': ('Login', screen_login),
    'auth_signup_v2': ('Signup', screen_signup),
    'auth_forgot_password_v2': ('ForgotPassword', screen_forgot_password),
    'auth_check_email_v2': ('CheckEmail', screen_check_email),
    'auth_verify_code_v2': ('VerifyCode', screen_verify_code),
    'auth_reset_code_v2': ('ResetCode', screen_reset_code),
    'auth_new_password_v2': ('NewPassword', screen_new_password),
    'auth_password_success_v2': ('PasswordSuccess', screen_password_success),
    'auth_email_verification_pending_v2': ('EmailVerificationPending', screen_email_verification_pending),
    'auth_mfa_enroll_prompt_v2': ('MFAEnrollPrompt', screen_mfa_enroll_prompt),
    'auth_mfa_enroll_qr_v2': ('MFAEnrollQR', screen_mfa_enroll_qr),
    'auth_mfa_enroll_backup_codes_v2': ('MFAEnrollBackupCodes', screen_mfa_enroll_backup_codes),
}


def build(key: str, dark: bool) -> str:
    th = theme(dark)
    title, fn = SCREENS[key]
    body = fn(th)
    return f'''<!DOCTYPE html>
<html class="{th['html']}" lang="fr"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<title>Smuppy V2 — {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
<style>
  :root {{
    --mint: {MINT}; --mint-hi: {MINT_HI}; --mint-deep: {MINT_DEEP};
    --page: {th['page']}; --card: {th['card']};
    --text: {th['text']}; --sub: {th['sub']}; --section: {th['section']};
    --border: {th['border']};
    --input-bg: {th['input_bg']}; --input-border: {th['input_border']};
    --back: {th['back']};
  }}
  * {{ box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-tap-highlight-color:transparent; }}
  html {{ background:var(--page); }}
  html, body {{ max-width:100%; overflow-x:hidden; }}
  body {{
    margin:0; width:393px; height:852px; overflow:hidden;
    background:var(--page); color:var(--text);
    font-family:'Plus Jakarta Sans',-apple-system,system-ui,sans-serif;
    font-size:15px; line-height:1.5; position:relative;
  }}

  /* ── Smuppy logos (real SVG paths) ──────────────────────── */
  .smuppy-full {{ display:inline-flex; align-items:center; gap:8px;
    filter:drop-shadow(0 0 18px rgba(51,160,137,0.15)); }}
  .smuppy-stacked {{ display:flex; flex-direction:column; align-items:center; gap:12px;
    filter:drop-shadow(0 0 24px rgba(51,160,137,0.225)); }}

  /* ── Back/Close ───────────────────────────────────────────── */
  .v2-back {{ width:40px; height:40px; border:none; background:transparent;
    border-radius:999px; color:var(--back);
    display:flex; align-items:center; justify-content:center;
    cursor:pointer; transition:background .15s ease; }}
  .v2-back:active {{ background:rgba(51,160,137,0.1); }}

  /* ── Welcome ──────────────────────────────────────────────── */
  .welcome-bg {{ position:absolute; inset:0; z-index:1; }}
  .welcome-hero-img {{ width:100%; height:100%; object-fit:cover; }}
  .welcome-overlay {{ position:absolute; inset:0;
    background:linear-gradient(180deg, {th['hero_overlay_top']} 0%, rgba(0,0,0,0.4) 50%, {th['hero_overlay_bot']} 100%); }}
  .welcome-content {{ position:absolute; inset:0; z-index:5;
    display:flex; flex-direction:column;
    padding:60px 24px 36px env(safe-area-inset-bottom,36px); }}
  .welcome-top-spacer {{ flex:1; }}
  .welcome-brand {{ text-align:center; margin-bottom:36px; }}
  .welcome-title {{ font-size:18px; font-weight:600; color:#fff;
    opacity:.85; margin-bottom:10px; letter-spacing:.02em;
    text-shadow:0 2px 8px rgba(0,0,0,.4); }}
  .welcome-tagline {{ color:#fff; font-size:14px; font-weight:500;
    margin:14px 0 0; text-shadow:0 2px 8px rgba(0,0,0,.4); opacity:.95; line-height:1.45;
    max-width:300px; margin-left:auto; margin-right:auto; }}
  .welcome-stats {{ display:flex; align-items:center; justify-content:center; gap:18px;
    margin:0 0 28px; padding:14px 18px; border-radius:18px;
    background:rgba(20,20,26,.55);
    -webkit-backdrop-filter:blur(20px); backdrop-filter:blur(20px);
    border:1px solid rgba(51,160,137,0.25);
    box-shadow:0 0 24px rgba(51,160,137,0.18); }}
  .welcome-stat {{ display:flex; flex-direction:column; align-items:center; gap:2px; }}
  .welcome-stat-num {{ font-size:18px; font-weight:800; color:var(--mint); letter-spacing:-.02em; }}
  .welcome-stat-lbl {{ font-size:10px; font-weight:600; color:#fff;
    text-transform:lowercase; letter-spacing:.06em; opacity:.85; }}
  .welcome-stat-divider {{ width:1px; height:24px; background:rgba(255,255,255,.18); }}
  .welcome-actions {{ display:flex; flex-direction:column; gap:12px; }}
  .welcome-tos {{ text-align:center; font-size:11px; color:#fff;
    opacity:.75; margin:14px 0 0; font-weight:500; line-height:1.4; }}
  .welcome-tos b {{ font-weight:700; color:#fff; opacity:1;
    text-decoration:underline; text-underline-offset:2px; }}

  /* ── CTAs ─────────────────────────────────────────────────── */
  .cta-primary {{ display:flex; align-items:center; justify-content:center;
    width:100%; height:54px; border:none; border-radius:999px;
    background:linear-gradient(135deg, var(--mint-hi) 0%, var(--mint-deep) 100%);
    color:#fff; font-family:inherit; font-size:15px; font-weight:800;
    cursor:pointer; transition:transform .15s ease;
    box-shadow:0 8px 24px rgba(51,160,137,0.225),
               0 0 0 1px rgba(255,255,255,.08) inset; letter-spacing:.01em; }}
  .cta-primary:active {{ transform:scale(.98); }}
  .cta-ghost {{ display:flex; align-items:center; justify-content:center;
    width:100%; height:52px; border-radius:999px;
    background:transparent; color:#fff;
    border:1.5px solid rgba(255,255,255,.35);
    font-family:inherit; font-size:15px; font-weight:700; cursor:pointer;
    -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px); }}
  .cta-ghost:active {{ background:rgba(255,255,255,.10); }}

  /* ── Auth scaffolding ─────────────────────────────────────── */
  .auth-topbar {{ position:absolute; top:0; left:0; right:0; z-index:10;
    height:52px; padding:0 12px;
    display:flex; align-items:center; justify-content:space-between; }}
  .auth-main {{ padding:62px 24px 24px; height:100%; overflow-y:auto; }}
  .auth-main-tight {{ padding-top:62px; }}
  .auth-main-onb {{ padding-top:74px; }}
  .auth-brand-row {{ display:flex; justify-content:center; margin-bottom:14px; }}
  .auth-icon-circle {{ width:64px; height:64px; border-radius:999px;
    background:rgba(51,160,137,0.12);
    border:1.5px solid rgba(51,160,137,0.15);
    display:flex; align-items:center; justify-content:center;
    margin:8px auto 14px;
    box-shadow:0 0 24px rgba(51,160,137,0.25),
               0 0 0 1px rgba(51,160,137,0.1) inset;
    filter:drop-shadow(0 0 10px rgba(51,160,137,0.15)); }}
  .auth-icon-circle-lg {{ width:80px; height:80px; }}
  .auth-title {{ font-size:24px; font-weight:800; letter-spacing:-.02em;
    color:var(--text); margin:6px 0 6px; text-align:center; }}
  .auth-title-lg {{ font-size:22px; }}
  .auth-sub {{ font-size:13.5px; font-weight:500; color:var(--sub);
    text-align:center; margin:0 0 22px; line-height:1.45;
    padding:0 8px; }}
  .auth-sub-small {{ font-size:12px; margin-top:14px; }}
  .auth-warn {{ background:rgba(245,158,11,.08); border:1px solid rgba(245,158,11,.20);
    border-radius:14px; padding:11px 14px; margin:0 -2px 18px;
    color:var(--sub); font-size:12px; line-height:1.4; }}

  /* ── Inputs ───────────────────────────────────────────────── */
  .v2-input-label {{ display:block; margin-bottom:12px; }}
  .v2-input-lbl-txt {{ display:block; font-size:11px; font-weight:700;
    color:var(--sub); margin:0 0 6px 4px;
    text-transform:uppercase; letter-spacing:.08em; }}
  .v2-input {{ position:relative; display:flex; align-items:center;
    height:50px; padding:0 16px; border-radius:14px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    transition:.18s ease; }}
  .v2-input.has-icon {{ padding-left:42px; }}
  .v2-input-icon {{ position:absolute; left:14px; top:50%; transform:translateY(-50%);
    font-size:18px; color:var(--sub); }}
  .v2-input-value {{ color:var(--text); font-size:15px; font-weight:500; }}
  .v2-input-placeholder {{ color:var(--sub); font-size:15px; font-weight:500; opacity:.7; }}
  .v2-input-trail {{ margin-left:auto; }}
  .v2-input-trail-btn {{ border:none; background:transparent; cursor:pointer;
    color:var(--mint); font-family:inherit; font-size:12px; font-weight:700; padding:0; }}
  .v2-input.v2-input-focus {{ border-color:rgba(51,160,137,0.225);
    box-shadow:0 0 16px rgba(51,160,137,0.25),
               0 0 0 1px rgba(51,160,137,0.15) inset; }}
  .v2-input-err {{ font-size:12px; color:{DANGER}; margin:5px 0 0 4px; font-weight:600; }}

  .auth-form {{ display:flex; flex-direction:column; gap:0; margin-bottom:14px; }}
  .auth-form .cta-primary {{ margin-top:10px; }}
  .auth-form .cta-ghost {{ margin-top:8px; color:var(--text);
    border-color:var(--input-border); }}

  /* ── Row + remember + link ────────────────────────────────── */
  .auth-row-between {{ display:flex; align-items:center; justify-content:space-between;
    margin:4px 4px 18px; }}
  .auth-remember {{ display:flex; align-items:center; gap:8px;
    font-size:13px; font-weight:600; color:var(--text); cursor:pointer; }}
  .auth-checkbox {{ width:18px; height:18px; border-radius:6px;
    border:1.5px solid var(--input-border); background:var(--input-bg);
    display:inline-flex; align-items:center; justify-content:center; flex-shrink:0; }}
  .auth-checkbox.auth-checkbox-on {{ background:var(--mint); border-color:var(--mint);
    box-shadow:0 0 12px rgba(51,160,137,0.2); }}
  .auth-link {{ border:none; background:transparent; cursor:pointer;
    color:var(--mint); font-family:inherit; font-size:13px; font-weight:700; padding:0; }}
  .auth-link-strong {{ font-weight:800; }}
  .auth-link-small {{ font-size:12px; display:block; text-align:center; margin:14px auto 0; }}
  .auth-link-row {{ display:block; margin:12px auto 0;
    border:none; background:transparent; cursor:pointer;
    color:var(--mint); font-family:inherit; font-size:13px; font-weight:700; text-align:center; padding:8px 0; }}

  /* ── Password strength + reqs ─────────────────────────────── */
  .auth-pwd-strength {{ display:flex; align-items:center; gap:8px; margin:6px 4px 10px; }}
  .auth-pwd-strength-bar {{ flex:1; height:5px; border-radius:999px;
    background:var(--input-border); overflow:hidden; }}
  .auth-pwd-strength-fill {{ height:100%; border-radius:999px;
    background:linear-gradient(90deg, var(--mint-hi) 0%, var(--mint-deep) 100%);
    box-shadow:0 0 8px rgba(51,160,137,0.2); }}
  .auth-pwd-strength-lbl {{ font-size:11px; font-weight:700; color:var(--mint); letter-spacing:.02em; }}
  .auth-pwd-must {{ font-size:11px; font-weight:700; color:var(--sub);
    margin:0 4px 8px; text-transform:uppercase; letter-spacing:.06em; }}
  .auth-pwd-reqs {{ display:grid; grid-template-columns:1fr 1fr; gap:6px 12px;
    margin:0 4px 14px; }}
  .auth-pwd-req {{ display:flex; align-items:center; gap:6px;
    font-size:12px; font-weight:500; color:var(--sub); }}
  .auth-pwd-req.auth-pwd-req-ok {{ color:var(--text); }}
  .auth-helper {{ font-size:11.5px; margin:4px 4px 6px;
    display:inline-flex; align-items:center; gap:5px; font-weight:600; }}
  .auth-helper-ok {{ color:var(--mint); }}

  /* ── Terms ────────────────────────────────────────────────── */
  .auth-terms {{ align-items:flex-start; margin:4px 4px 18px;
    font-size:12px; line-height:1.4; }}
  .auth-terms .auth-checkbox {{ margin-top:1px; }}
  .auth-terms b {{ font-weight:700; color:var(--mint); }}

  /* ── Divider ──────────────────────────────────────────────── */
  .auth-divider {{ display:flex; align-items:center; gap:12px; margin:18px 0 12px; }}
  .auth-divider-line {{ flex:1; height:1px; background:var(--border); }}
  .auth-divider-txt {{ font-size:11px; font-weight:600; color:var(--sub); text-transform:lowercase; }}

  /* ── Social ───────────────────────────────────────────────── */
  .auth-social {{ display:flex; gap:10px; margin-bottom:14px; }}
  .social-btn {{ flex:1; display:flex; align-items:center; justify-content:center; gap:8px;
    height:48px; border-radius:14px;
    background:{th['social_bg']}; border:1px solid var(--input-border);
    color:var(--text); font-family:inherit; font-size:14px; font-weight:700;
    cursor:pointer; transition:.15s ease;
    box-shadow:0 2px 8px rgba(0,0,0,{th['dim_shadow']}); }}
  .social-btn:hover {{ border-color:rgba(51,160,137,0.15); }}
  .social-ic {{ display:flex; align-items:center; justify-content:center; }}

  /* ── Footer link ──────────────────────────────────────────── */
  .auth-footer {{ text-align:center; font-size:12.5px; font-weight:500;
    color:var(--sub); margin:8px 0 0; }}
  .auth-footer .auth-link {{ margin-left:4px; }}

  /* ── Onb header ───────────────────────────────────────────── */
  .onb-header {{ position:absolute; top:0; left:0; right:0; z-index:10;
    height:56px; padding:0 14px;
    display:flex; align-items:center; gap:12px;
    background:var(--header);
    -webkit-backdrop-filter:blur(20px) saturate(180%);
    backdrop-filter:blur(20px) saturate(180%); }}
  .onb-progress {{ flex:1; height:4px; border-radius:999px;
    background:var(--input-border); overflow:hidden; }}
  .onb-progress-bar {{ height:100%; border-radius:999px;
    background:linear-gradient(90deg, var(--mint-hi) 0%, var(--mint-deep) 100%);
    box-shadow:0 0 8px rgba(51,160,137,0.2); transition:width .3s ease; }}
  .onb-step {{ font-size:12px; font-weight:700; color:var(--sub);
    min-width:30px; text-align:right; }}

  /* ── Steps list ───────────────────────────────────────────── */
  .auth-steps {{ background:var(--card); border:1px solid rgba(51,160,137,0.15);
    border-radius:18px; padding:14px 16px; margin:0 0 18px;
    box-shadow:0 0 20px rgba(51,160,137,0.08); }}
  .auth-step-prelude {{ font-size:12px; font-weight:700; color:var(--sub);
    margin:0 0 10px; text-transform:uppercase; letter-spacing:.06em; }}
  .auth-step {{ display:flex; align-items:flex-start; gap:12px;
    font-size:13px; font-weight:500; color:var(--text);
    margin-bottom:10px; line-height:1.4; }}
  .auth-step:last-child {{ margin-bottom:0; }}
  .auth-step-num {{ flex-shrink:0; width:24px; height:24px; border-radius:999px;
    background:rgba(51,160,137,0.14); color:var(--mint);
    font-size:12px; font-weight:800;
    display:inline-flex; align-items:center; justify-content:center;
    border:1px solid rgba(51,160,137,0.15); }}

  /* ── Code input ───────────────────────────────────────────── */
  .code-grid {{ display:flex; gap:8px; justify-content:center; margin:8px 0 22px; }}
  .code-cell {{ width:48px; height:60px; border-radius:14px;
    background:var(--input-bg); border:1.5px solid var(--input-border);
    display:flex; align-items:center; justify-content:center;
    font-size:24px; font-weight:800; color:var(--text);
    letter-spacing:.02em; transition:.18s ease; }}
  .code-cell-filled {{ border-color:rgba(51,160,137,0.225);
    background:rgba(51,160,137,0.06); color:var(--mint);
    box-shadow:0 0 14px rgba(51,160,137,0.18); }}
  .code-cell-focus {{ border-color:rgba(51,160,137,0.275);
    box-shadow:0 0 18px rgba(51,160,137,0.15),
               0 0 0 1px rgba(51,160,137,0.2) inset; }}
  .code-cursor {{ width:2px; height:24px; background:var(--mint);
    border-radius:999px; animation:cursor-blink 1s infinite;
    box-shadow:0 0 6px rgba(51,160,137,0.25); }}
  @keyframes cursor-blink {{ 0%,49% {{ opacity:1; }} 50%,100% {{ opacity:0; }} }}

  /* ── Success screen (PasswordSuccess) ─────────────────────── */
  .success-wrap {{ position:absolute; inset:0; padding:0 24px;
    display:flex; flex-direction:column; align-items:center; justify-content:center; }}
  .success-confetti {{ position:absolute; inset:0; pointer-events:none;
    background:radial-gradient(circle at 30% 25%, rgba(51,160,137,0.15) 0%, transparent 30%),
               radial-gradient(circle at 75% 70%, rgba(0,179,199,.10) 0%, transparent 32%); }}
  .success-check {{ position:relative; width:120px; height:120px;
    border-radius:999px; background:rgba(51,160,137,0.1);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 0 60px rgba(51,160,137,0.225),
               0 0 0 2px rgba(51,160,137,0.175) inset;
    margin-bottom:26px; }}
  .success-check-ring {{ position:absolute; inset:-12px; border-radius:999px;
    border:2px solid rgba(51,160,137,0.2);
    box-shadow:0 0 24px rgba(51,160,137,0.15); }}
  .success-check-icon {{ font-size:62px; color:var(--mint);
    filter:drop-shadow(0 0 12px rgba(51,160,137,0.3)); }}
  .success-title {{ font-size:26px; font-weight:800; margin:0 0 6px;
    color:var(--text); letter-spacing:-.02em; text-align:center; }}
  .success-body {{ font-size:14px; font-weight:500; color:var(--sub);
    text-align:center; margin:0 0 30px; max-width:280px; line-height:1.45; }}
  .success-loader {{ display:flex; align-items:center; gap:10px;
    font-size:13px; font-weight:600; color:var(--sub); }}
  .success-spinner {{ width:18px; height:18px; border-radius:999px;
    border:2.5px solid rgba(51,160,137,0.18);
    border-top-color:var(--mint);
    animation:spin .8s linear infinite; }}
  @keyframes spin {{ 100% {{ transform:rotate(360deg); }} }}

  /* ── MFA apps ─────────────────────────────────────────────── */
  .auth-mfa-apps {{ background:var(--card); border:1px solid rgba(51,160,137,0.18);
    border-radius:18px; padding:14px 16px; margin:0 0 22px;
    box-shadow:0 0 20px rgba(51,160,137,0.08); }}
  .auth-mfa-apps-label {{ font-size:11px; font-weight:700; color:var(--sub);
    margin:0 0 10px; text-transform:uppercase; letter-spacing:.06em; }}
  .auth-mfa-app-row {{ display:flex; gap:8px; margin-bottom:8px; }}
  .auth-mfa-app-row:last-child {{ margin-bottom:0; }}
  .auth-mfa-app {{ flex:1; padding:8px 12px; border-radius:10px;
    background:var(--input-bg); border:1px solid var(--input-border);
    font-size:12px; font-weight:600; color:var(--text); text-align:center; }}

  /* ── MFA QR ───────────────────────────────────────────────── */
  .auth-qr-frame {{ width:200px; height:200px; margin:0 auto 18px;
    padding:12px; border-radius:20px;
    background:#fff;
    box-shadow:0 8px 24px rgba(0,0,0,{th['dim_shadow']}),
               0 0 24px rgba(51,160,137,0.2),
               0 0 0 1.5px rgba(51,160,137,0.15); }}
  .auth-qr-img {{ width:100%; height:100%; display:block; }}
  .auth-manual {{ margin:0 0 18px; padding:12px 14px;
    background:var(--card); border:1px dashed rgba(51,160,137,0.15);
    border-radius:14px; }}
  .auth-manual-label {{ font-size:11px; font-weight:700; color:var(--sub);
    margin:0 0 8px; text-transform:uppercase; letter-spacing:.06em; }}
  .auth-manual-code {{ display:flex; align-items:center; justify-content:space-between; gap:10px; }}
  .auth-manual-code-val {{ font-family:'Courier New',monospace;
    font-size:14px; font-weight:700; color:var(--text); letter-spacing:.08em; }}
  .auth-manual-copy {{ display:inline-flex; align-items:center; gap:4px;
    padding:6px 10px; border:none; border-radius:8px;
    background:rgba(51,160,137,0.12); color:var(--mint);
    font-family:inherit; font-size:11px; font-weight:700; cursor:pointer; }}

  /* ── Backup codes ─────────────────────────────────────────── */
  .auth-backup-grid {{ display:grid; grid-template-columns:1fr 1fr;
    gap:8px; margin:0 0 18px; }}
  .auth-backup-code {{ display:flex; align-items:center; gap:8px;
    padding:11px 12px; border-radius:12px;
    background:var(--input-bg); border:1px solid var(--input-border); }}
  .auth-backup-num {{ font-size:10px; font-weight:700; color:var(--sub);
    min-width:14px; }}
  .auth-backup-val {{ font-family:'Courier New',monospace;
    font-size:13px; font-weight:700; color:var(--text); letter-spacing:.04em; }}
  .auth-backup-actions {{ display:flex; gap:10px; margin-bottom:18px; }}
  .auth-backup-btn {{ flex:1; display:inline-flex; align-items:center; justify-content:center; gap:6px;
    padding:11px 14px; border-radius:12px;
    background:var(--input-bg); border:1px solid rgba(51,160,137,0.15);
    color:var(--mint); font-family:inherit; font-size:12px; font-weight:700;
    cursor:pointer; box-shadow:0 0 14px rgba(51,160,137,0.1); }}
</style>
</head>
<body>
{body}
</body></html>'''


def write_all() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 0
    for key in SCREENS.keys():
        for dark in (True, False):
            theme_str = 'dark' if dark else 'light'
            screen_dir = OUT_DIR / f'{key}_{theme_str}'
            screen_dir.mkdir(parents=True, exist_ok=True)
            html = build(key, dark)
            (screen_dir / 'code.html').write_text(html)
            n += 1
    print(f'  built {n} AUTH HTML maquettes')


if __name__ == '__main__':
    write_all()
