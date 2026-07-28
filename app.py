from __future__ import annotations

import streamlit as st

APP_NAME = "Barrister Dashboard"

st.set_page_config(page_title=APP_NAME, page_icon="🏁", layout="wide", initial_sidebar_state="collapsed")


def configure_page() -> None:
    st.markdown(
        """
        <style>
        :root {
        :root {
    color-scheme: dark;

    /* -- App background -- */
    --bg-app-1: #08111f;
    --bg-app-2: #0b1627;
    --bg-app-3: #07101c;
    --bg-void: #05070b;
    --bg-void-deep: #02050a;

    /* -- Navy surface steps (cards, badges, nav pills) -- */
    --navy-900: #07101c;
    --navy-850: #0d1927;
    --navy-800: #101d31;
    --navy-750: #102039;
    --navy-700: #112139;
    --navy-650: #14233a;
    --navy-600: #14243a;
    --navy-550: #20314a;
    --navy-500: #192c46;
    --navy-450: #294666;
    --navy-900-rgb: 8,17,31;
    --surface-rgb: 20,34,55;
    --surface-deep-rgb: 13,25,43;
    --surface-card-gradient: linear-gradient(145deg, rgba(var(--surface-rgb),.96), rgba(var(--surface-deep-rgb),.96));
    --surface-card-gradient-alt: linear-gradient(135deg, rgba(var(--surface-rgb),.96), rgba(var(--surface-deep-rgb),.96));

    /* -- Borders -- */
    --border-default: #243751;
    --border-strong: #2b405d;
    --border-strong-alt: #35516f;
    --border-scroll: #38506f;
    --border-form: #263a55;
    --slate-border-rgb: 148,163,184;

    /* -- Text -- */
    --text-primary: #f8fafc;
    --text-primary-rgb: 248,250,252;
    --text-on-accent: #ffffff;
    --text-heading-soft: #f4f8fd;
    --text-secondary-bright: #f1f5fa;
    --text-secondary: #c2cddd;
    --text-secondary-alt: #c9d6e7;
    --text-secondary-alt2: #cbd8e9;
    --text-secondary-dim: #b9c9dc;
    --text-secondary-hover: #d8e3f1;
    --text-tertiary: #aebdd1;
    --text-tertiary-alt: #9fb1c8;
    --text-muted: #8fa1bb;
    --text-muted-alt: #9eb0c8;
    --text-muted-alt2: #91a3bd;
    --text-accent-cyan: #bfe9ff;
    --text-accent-cyan-pale: #e9f4ff;
    --text-accent-cyan-pale2: #eaf6ff;
    --text-accent-cyan-pale3: #eef6ff;
    --text-accent-cyan-pale4: #d9f3ff;
    --text-onlogo: #e6edf7;
    --text-onlogo-alt: #e7eef8;
    --text-pale-slate: #d9e1ec;
    --white-rgb: 255,255,255;
    --ink-rgb: 15,23,42;

    /* -- Accent: teal (primary brand accent) -- */
    --accent-teal: #2dd4bf;
    --accent-teal-rgb: 45,212,191;
    --accent-teal-light: #70ddd1;
    --accent-teal-bright: #77e1d5;
    --accent-teal-deep: #1f8f87;
    --accent-teal-hover: #9ff0e6;
    --accent-teal-badge: #8ce7dc;

    /* -- Accent: blue -- */
    --accent-blue: #38bdf8;
    --accent-blue-rgb: 56,189,248;
    --accent-blue-light-rgb: 125,211,252;
    --accent-blue-deep: #5c8ee8;
    --accent-blue-deep-rgb: 92,142,232;
    --accent-blue-navy: #274f99;
    --accent-blue-pale: #dce5f1;

    /* -- Accent: gold / amber -- */
    --accent-gold: #f5c542;
    --accent-gold-rgb: 245,197,66;
    --accent-gold-soft: #f6d892;
    --accent-gold-pale: #ffe8a3;
    --accent-gold-paler: #fff4bf;
    --accent-gold-paler2: #fff2ad;
    --accent-gold-paler3: #fff0a8;
    --accent-gold-cream: #fff7d6;
    --accent-gold-checkpoint: #f7d38d;
    --accent-gold-dim: #e7c98b;
    --accent-gold-deep: #a66a18;
    --accent-gold-deep2: #9f6417;
    --accent-gold-brown: #7b6340;
    --accent-gold-bg: #2a241b;

    /* -- Accent: coral / red -- */
    --accent-coral: #d85a62;
    --accent-coral-rgb: 216,90,98;
    --accent-coral-deep: #8a2f38;
    --accent-coral-pale: #f6d7da;
    --accent-coral-pale2: #f8c8d7;

    /* -- Accent: purple / pink / orange / success -- */
    --accent-purple: #a78bfa;
    --accent-pink-rgb: 244,114,182;
    --accent-pink-soft-rgb: 244,167,189;
    --accent-orange: #f97316;
    --accent-orange-rgb: 249,115,22;
    --accent-success: #34d399;
    --accent-success-rgb: 52,211,153;
    --accent-success-alt-rgb: 34,197,94;

    /* -- Radii -- */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 15px;
    --radius-xl: 18px;
    --radius-pill: 999px;

    /* -- Motion: one shared easing/duration system for all micro-interactions -- */
    --ease-standard: cubic-bezier(.4,0,.2,1);
    --ease-emphasized: cubic-bezier(.2,.72,.22,1);
    --dur-fast: .15s;
    --dur-base: .18s;
    --dur-slow: .3s;
    --transition-base: transform var(--dur-base) var(--ease-standard), box-shadow var(--dur-base) var(--ease-standard), border-color var(--dur-base) var(--ease-standard);

    /* -- Shadows (neutral black stays literal; only depth is scaled) -- */
    --shadow-card: 0 9px 22px rgba(0,0,0,.14);
    --shadow-elevated: 0 14px 34px rgba(0,0,0,.2);
    --shadow-deep: 0 16px 34px rgba(0,0,0,.18);
}
        }
        .stApp { background: linear-gradient(145deg, var(--bg-app-1) 0%, var(--bg-app-2) 55%, var(--bg-app-3) 100%); }
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"] { height: 0 !important; min-height: 0 !important; background: transparent !important; border-bottom: none !important; visibility: hidden !important; opacity: 0 !important; pointer-events: none !important; }
        [data-testid="stToolbar"] *,
        [data-testid="stStatusWidget"] *,
        button[kind="header"],
        [data-testid="stMainMenu"] { visibility: hidden !important; opacity: 0 !important; pointer-events: none !important; }
        [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stExpandSidebarButton"] { display: none !important; }
        .block-container { max-width: 1480px; padding-top: .75rem; padding-bottom: 2.5rem; }
        h1, h2, h3 { letter-spacing: -0.025em; }
        .section-kicker { color: var(--text-muted); font-size: .64rem; font-weight: 820; letter-spacing: .13em; text-transform: uppercase; margin: .1rem 0 .1rem; }
        .section-title { color: var(--text-primary); font-family: "Inter", "SF Pro Display", "Aptos Display", "Segoe UI", Arial, sans-serif; font-size: clamp(1.32rem, 3vw, 1.9rem); font-weight: 820; letter-spacing: -.04em; text-transform: none; margin: 0 0 .58rem; text-shadow: 0 0 18px rgba(var(--white-rgb),.08), 0 10px 24px rgba(0,0,0,.24); }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_splash_screen() -> None:
    enter_url = "?page=lab"
    st.markdown(
        f"""
        <style>
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stSidebar"],
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stExpandSidebarButton"] {{
            display: none !important;
        }}
        html,
        body,
        [data-testid="stAppViewContainer"],
        [data-testid="stApp"],
        .main,
        .stApp {{
            overflow: hidden !important;
            height: 100vh !important;
            height: 100dvh !important;
            max-height: 100vh !important;
            max-height: 100dvh !important;
            overscroll-behavior: none !important;
            touch-action: none;
        }}
        .stApp {{
            background: var(--bg-void) !important;
        }}
        .block-container {{
            max-width: none !important;
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important;
            padding: 0 !important;
            margin: 0 !important;
        }}

        @keyframes splashOrbDrift {{
            0% {{ transform: translate(0, 0) scale(1); }}
            50% {{ transform: translate(var(--drift-x, 4vw), var(--drift-y, -3vh)) scale(1.08); }}
            100% {{ transform: translate(0, 0) scale(1); }}
        }}
        @keyframes splashRiseIn {{
            from {{ opacity: 0; transform: translateY(14px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes splashWipeReveal {{
            from {{ clip-path: inset(0 100% 0 0); }}
            to {{ clip-path: inset(0 0 0 0); }}
        }}
        @keyframes splashScanGrow {{
            from {{ transform: scaleX(0); opacity: 0; }}
            40% {{ opacity: 1; }}
            to {{ transform: scaleX(1); opacity: .85; }}
        }}
        @keyframes splashGlowPulse {{
            0%, 100% {{ box-shadow: 0 0 0 1px rgba(var(--accent-teal-rgb),.5), 0 0 22px rgba(var(--accent-teal-rgb),.22), 0 10px 26px rgba(0,0,0,.35); }}
            50% {{ box-shadow: 0 0 0 1px rgba(var(--accent-teal-rgb),.75), 0 0 36px rgba(var(--accent-teal-rgb),.4), 0 10px 26px rgba(0,0,0,.35); }}
        }}
        @keyframes splashRoadDraw {{
            from {{ opacity: 0; transform: translateY(-50%) scaleX(0); }}
            to {{ opacity: 1; transform: translateY(-50%) scaleX(1); }}
        }}
        @keyframes splashCarEntrance {{
            0%   {{ transform: translate(-160%, 8px) scale(1); }}
            55%  {{ transform: translate(4%, -21px) scale(1.04); }}
            72%  {{ transform: translate(-2%, -13px) scale(.98); }}
            86%  {{ transform: translate(1%, -17px) scale(1.01); }}
            100% {{ transform: translate(0, -15px) scale(1); }}
        }}
        @keyframes splashCarIdle {{
            0%, 100% {{ transform: translateY(-15px) rotate(0deg); }}
            50% {{ transform: translateY(-18px) rotate(-1deg); }}
        }}
        @keyframes splashCarLaunch {{
            0%   {{ transform: translate(0, -15px) scale(1, 1); }}
            14%  {{ transform: translate(-5%, -14px) scale(.92, 1.07); }}
            100% {{ transform: translate(180%, -10px) scale(1.06, .92); }}
        }}
        @keyframes splashCarTrail {{
            0%   {{ filter: drop-shadow(0 0 0 rgba(var(--accent-teal-rgb),0)); }}
            35%  {{ filter: drop-shadow(-16px 0 10px rgba(var(--accent-teal-rgb),.6)); }}
            100% {{ filter: drop-shadow(-30px 0 16px rgba(var(--accent-teal-rgb),0)); }}
        }}

        .splash-gateway {{
            position: fixed;
            inset: 0;
            width: 100vw;
            height: 100vh;
            height: 100dvh;
            overflow: hidden;
            background: var(--bg-void);
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .splash-orb {{
            position: absolute;
            border-radius: 50%;
            filter: blur(60px);
            pointer-events: none;
            animation: splashOrbDrift var(--drift-dur, 16s) ease-in-out infinite;
            opacity: .5;
        }}
        .splash-orb-a {{
            top: 8%; left: 6%; width: 42vw; height: 42vw;
            background: radial-gradient(circle, rgba(var(--accent-teal-rgb),.30), transparent 70%);
            --drift-x: 5vw; --drift-y: 4vh; --drift-dur: 17s;
        }}
        .splash-orb-b {{
            bottom: 4%; right: 4%; width: 48vw; height: 48vw;
            background: radial-gradient(circle, rgba(var(--accent-blue-rgb),.24), transparent 70%);
            --drift-x: -4vw; --drift-y: -5vh; --drift-dur: 21s;
        }}
        .splash-orb-c {{
            top: 42%; left: 58%; width: 30vw; height: 30vw;
            background: radial-gradient(circle, rgba(var(--accent-pink-rgb),.14), transparent 70%);
            --drift-x: -3vw; --drift-y: 3vh; --drift-dur: 13s;
        }}

        .splash-content {{
            position: relative;
            z-index: 2;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 0 1.4rem;
            max-width: 720px;
        }}
        .splash-road {{
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            width: min(78vw, 460px);
            height: 50px;
            margin: 0 auto .1rem;
        }}
        .splash-road-line {{
            position: absolute;
            left: 0;
            right: 0;
            top: 50%;
            height: 3px;
            transform: translateY(-50%);
            transform-origin: center;
            border-radius: 999px;
            z-index: 0;
            background: repeating-linear-gradient(to right, var(--text-pale-slate) 0 10px, transparent 10px 20px);
            box-shadow: 0 0 14px rgba(var(--accent-teal-rgb),.22);
            animation: splashRoadDraw .5s var(--ease-standard) .05s forwards;
        }}
        .splash-car {{
            position: relative;
            z-index: 1;
            display: inline-block;
            font-size: clamp(1.9rem, 5.4vw, 2.35rem);
            line-height: 1;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent;
            filter: drop-shadow(0 6px 10px rgba(0,0,0,.4));
            animation: splashCarEntrance .82s var(--ease-emphasized) .1s both, splashCarIdle 1.9s ease-in-out .92s infinite;
        }}
        .splash-wordmark {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: .3rem;
        }}
        .splash-word {{
            display: block;
            font-family: "Inter", "SF Pro Display", "Aptos Display", "Segoe UI", Arial, sans-serif;
            color: var(--text-primary);
            animation: splashWipeReveal .55s var(--ease-emphasized) forwards;
            white-space: nowrap;
        }}
        .splash-word-1 {{
            font-size: clamp(2.9rem, 10vw, 5.6rem);
            font-weight: 900;
            letter-spacing: -.03em;
            line-height: .96;
            text-shadow: 0 0 24px rgba(var(--accent-teal-rgb),.3), 0 0 60px rgba(var(--accent-teal-rgb),.16), 0 14px 30px rgba(0,0,0,.4);
            animation-delay: .9s;
        }}
        .splash-word-2 {{
            font-size: clamp(1.05rem, 3.4vw, 1.8rem);
            font-weight: 700;
            letter-spacing: .38em;
            color: var(--text-secondary);
            padding-left: .38em;
            animation-delay: 1.18s;
        }}
        .splash-scanline {{
            width: min(60vw, 320px);
            height: 2px;
            margin: 1.05rem 0 1.5rem;
            border-radius: 999px;
            background: linear-gradient(90deg, transparent, var(--accent-teal) 50%, transparent);
            transform-origin: center;
            animation: splashScanGrow .7s var(--ease-standard) 1.42s forwards;
        }}
        .splash-enter-btn {{
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 148px;
            padding: .85rem 1.9rem;
            border-radius: var(--radius-pill);
            border: 1px solid rgba(var(--accent-teal-rgb),.5);
            background: linear-gradient(135deg, rgba(var(--accent-teal-rgb),.16), rgba(var(--surface-rgb),.7));
            color: var(--text-primary) !important;
            font-family: "Inter", "SF Pro Display", "Segoe UI", Arial, sans-serif;
            font-size: .92rem;
            font-weight: 800;
            letter-spacing: .1em;
            text-decoration: none !important;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent;
            animation: splashRiseIn .55s var(--ease-emphasized) 1.62s forwards, splashGlowPulse 2.6s ease-in-out 2.2s infinite;
            transition: transform .18s var(--ease-standard), background .18s var(--ease-standard);
        }}
        .splash-enter-btn:hover {{
            transform: translateY(-2px);
            background: linear-gradient(135deg, rgba(var(--accent-teal-rgb),.26), rgba(var(--surface-rgb),.82));
        }}
        .splash-enter-btn:active {{
            transform: translateY(0) scale(.97);
        }}
        .splash-gateway.curtain-close .splash-content {{
            transition: opacity .3s ease, transform .3s ease;
            opacity: 0;
            transform: scale(.98);
        }}
        .splash-gateway.curtain-close .splash-road {{
            transition: opacity .3s ease;
            opacity: 0;
        }}
        .splash-gateway.curtain-close .splash-car {{
            animation: splashCarLaunch .5s cubic-bezier(.55,0,.85,.35) forwards, splashCarTrail .5s ease-out forwards;
        }}

        .splash-gateway::before,
        .splash-gateway::after {{
            content: "";
            position: fixed;
            top: 0;
            bottom: 0;
            width: 51vw;
            z-index: 9999;
            pointer-events: none;
            background:
                radial-gradient(circle at 50% 18%, rgba(var(--accent-blue-rgb),.10), transparent 35%),
                linear-gradient(145deg, var(--bg-app-1) 0%, var(--bg-app-2) 55%, var(--bg-app-3) 100%);
            box-shadow: inset 0 0 42px rgba(var(--accent-blue-rgb),.14);
            transition: transform .6s cubic-bezier(.76,0,.18,1);
        }}
        .splash-gateway::before {{
            left: 0;
            transform: translateX(-101%);
            border-right: 1px solid rgba(var(--accent-teal-rgb),.4);
            box-shadow: inset -18px 0 30px -18px rgba(var(--accent-teal-rgb),0), inset 0 0 42px rgba(var(--accent-blue-rgb),.14);
        }}
        .splash-gateway::after {{
            right: 0;
            transform: translateX(101%);
            border-left: 1px solid rgba(var(--accent-teal-rgb),.4);
            transition-delay: .04s;
        }}
        .splash-gateway.curtain-close::before,
        .splash-gateway.curtain-close::after {{
            transform: translateX(0);
        }}
        .splash-gateway.curtain-close::before {{
            box-shadow: inset -18px 0 30px -18px rgba(var(--accent-teal-rgb),.55), inset 0 0 42px rgba(var(--accent-blue-rgb),.14);
            transition: transform .6s cubic-bezier(.76,0,.18,1), box-shadow .5s ease .32s;
        }}
        </style>
        <div class="splash-gateway" aria-label="Barrister Dashboard splash screen">
            <div class="splash-orb splash-orb-a"></div>
            <div class="splash-orb splash-orb-b"></div>
            <div class="splash-orb splash-orb-c"></div>
            <div class="splash-content">
                <div class="splash-road">
                    <div class="splash-road-line"></div>
                    <div class="splash-car" role="button" tabindex="0" aria-label="Enter lab" onclick="event.preventDefault(); const gate=this.closest('.splash-gateway'); if(gate){{gate.classList.add('curtain-close');}} setTimeout(()=>{{window.location.href='{enter_url}';}},640);" onkeydown="if(event.key==='Enter'||event.key===' '){{this.click();}}">🏎️</div>
                </div>
                <div class="splash-wordmark">
                    <span class="splash-word splash-word-1">BARRISTER</span>
                    <span class="splash-word splash-word-2">DASHBOARD</span>
                </div>
                <div class="splash-scanline"></div>
                <a class="splash-enter-btn" href="{enter_url}" target="_self" aria-label="Enter lab" onclick="event.preventDefault(); const gate=this.closest('.splash-gateway'); if(gate){{gate.classList.add('curtain-close');}} setTimeout(()=>{{window.location.href=this.href;}},640);">ENTER</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_testing_lab() -> None:
    st.markdown(
        '<div class="page-nav"><a href="?page=lab" target="_self" class="active">Lab</a>'
        '<a href="?page=exec" target="_self">Executive &rarr;</a></div>'
        '<style>.page-nav a { color: var(--text-muted); text-decoration: none; font-size: .68rem; font-weight: 800; letter-spacing: .05em; text-transform: uppercase; padding: .4rem .8rem; border-radius: 999px; border: 1px solid rgba(var(--slate-border-rgb),.28); margin-right: .5rem; display: inline-block; }'
        '.page-nav a.active { color: var(--accent-teal); border-color: rgba(var(--accent-teal-rgb),.5); }</style>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section-kicker">ANIMATION LAB</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">TESTING</div>', unsafe_allow_html=True)
    st.caption("Four different animation techniques. Tap a demo to play it, tap again to reset and replay.")

    st.markdown(
        """
        <style>
        .lab-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: .8rem; margin: .6rem 0 1rem; }
        @media (max-width: 700px) { .lab-grid { grid-template-columns: 1fr; } }
        .lab-card { position: relative; border: 1px solid rgba(var(--slate-border-rgb),.24); border-radius: var(--radius-lg); background: var(--surface-card-gradient); padding: .95rem 1rem 1.1rem; overflow: hidden; }
        .lab-card-title { color: var(--text-primary); font-size: .82rem; font-weight: 800; letter-spacing: .01em; margin-bottom: .15rem; }
        .lab-card-use { color: var(--text-muted); font-size: .64rem; line-height: 1.4; margin-bottom: .75rem; }
        .lab-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
        .lab-stage-label { display: block; cursor: pointer; -webkit-tap-highlight-color: transparent; }
        .lab-stage { position: relative; height: 108px; display: flex; align-items: center; justify-content: center; border-radius: 12px; background: rgba(var(--navy-900-rgb),.5); border: 1px solid rgba(var(--slate-border-rgb),.16); overflow: hidden; }
        .lab-play-hint { position: absolute; bottom: 6px; right: 9px; font-size: .5rem; font-weight: 800; letter-spacing: .05em; color: var(--accent-teal); opacity: .8; }
        .lab-play-hint::before { content: "▶ PLAY"; }
        .lab-toggle:checked ~ .lab-stage-label .lab-play-hint::before { content: "↺ RESET"; }

        /* 1. 3D FLIP */
        .lab-flip-inner { width: 96px; height: 72px; position: relative; transform-style: preserve-3d; transition: transform .6s cubic-bezier(.4,.2,.2,1); }
        .lab-toggle:checked ~ .lab-stage-label .lab-flip-inner { transform: rotateY(180deg); }
        .lab-flip-face { position: absolute; inset: 0; backface-visibility: hidden; -webkit-backface-visibility: hidden; display: flex; align-items: center; justify-content: center; border-radius: 10px; font-size: 1.6rem; font-weight: 900; color: var(--text-primary); }
        .lab-flip-front { background: linear-gradient(145deg, rgba(45,212,191,.28), rgba(45,212,191,.08)); border: 1px solid rgba(var(--accent-teal-rgb),.4); }
        .lab-flip-back { transform: rotateY(180deg); background: linear-gradient(145deg, rgba(56,189,248,.28), rgba(56,189,248,.08)); border: 1px solid rgba(var(--accent-blue-rgb),.4); font-size: 1rem; }

        /* 2. COUNT-UP -- plain JS, not a CSS trick. Reliability over cleverness. */
        .lab-count-num { font-size: 2.4rem; font-weight: 900; color: var(--text-primary); }

        /* 3. CELEBRATION BURST -- transition on the base rule, value just changes on :checked */
        .lab-burst-core { width: 34px; height: 34px; border-radius: 50%; background: radial-gradient(circle, var(--accent-gold), rgba(245,197,66,0)); transform: scale(0); opacity: 0; transition: transform .45s cubic-bezier(.34,1.56,.64,1), opacity .25s ease; }
        .lab-toggle:checked ~ .lab-stage-label .lab-burst-core { transform: scale(1); opacity: .9; }
        .lab-burst-particle { position: absolute; top: 50%; left: 50%; width: 6px; height: 6px; border-radius: 50%; background: var(--accent-teal); opacity: 1; transform: translate(-50%, -50%) translate(0, 0) scale(1); transition: transform .75s ease-out, opacity .75s ease-out; }
        .lab-toggle:checked ~ .lab-stage-label .lab-burst-particle { opacity: 0; transform: translate(-50%, -50%) translate(var(--bx), var(--by)) scale(.4); }

        /* 4. PROGRESS RING -- same proven pattern: transition always present, only the value moves */
        .lab-ring-track { stroke: rgba(var(--slate-border-rgb),.25); }
        .lab-ring-fill { stroke: var(--accent-purple); stroke-linecap: round; stroke-dasharray: 226; stroke-dashoffset: 226; transform-origin: center; transform: rotate(-90deg); transition: stroke-dashoffset 1.1s cubic-bezier(.3,.7,.3,1); }
        .lab-toggle:checked ~ .lab-stage-label .lab-ring-fill { stroke-dashoffset: 40; }
        .lab-ring-label { position: absolute; font-size: 1.05rem; font-weight: 900; color: var(--text-primary); opacity: 0; transition: opacity .4s ease .7s; }
        .lab-toggle:checked ~ .lab-stage-label .lab-ring-label { opacity: 1; }
        </style>
        <div class="lab-grid">
            <div class="lab-card">
                <div class="lab-card-title">1 · 3D Flip</div>
                <div class="lab-card-use">Reveal a second stat behind a number — already live on Exec KPIs.</div>
                <input type="checkbox" id="lab1" class="lab-toggle">
                <label for="lab1" class="lab-stage-label">
                    <div class="lab-stage">
                        <div class="lab-flip-inner">
                            <div class="lab-flip-face lab-flip-front">76</div>
                            <div class="lab-flip-face lab-flip-back">EVENTS</div>
                        </div>
                        <span class="lab-play-hint"></span>
                    </div>
                </label>
            </div>
            <div class="lab-card">
                <div class="lab-card-title">2 · Count-Up</div>
                <div class="lab-card-use">A KPI counts up from 0 on reveal instead of just appearing — good for first paint of a page.</div>
                <input type="checkbox" id="lab2" class="lab-toggle" onchange="
                    var el = this.closest('.lab-card').querySelector('.lab-count-num');
                    if (this.checked) {
                        var start = null; var dur = 1200; var target = 76;
                        function step(ts) {
                            if (!start) { start = ts; }
                            var p = Math.min((ts - start) / dur, 1);
                            var eased = 1 - Math.pow(1 - p, 3);
                            el.textContent = Math.round(eased * target);
                            if (p < 1) { requestAnimationFrame(step); }
                        }
                        requestAnimationFrame(step);
                    } else {
                        el.textContent = '';
                    }
                ">
                <label for="lab2" class="lab-stage-label">
                    <div class="lab-stage">
                        <div class="lab-count-num"></div>
                        <span class="lab-play-hint"></span>
                    </div>
                </label>
            </div>
            <div class="lab-card">
                <div class="lab-card-title">3 · Celebration Burst</div>
                <div class="lab-card-use">A milestone moment — new record, streak hit, first visit for a client.</div>
                <input type="checkbox" id="lab3" class="lab-toggle">
                <label for="lab3" class="lab-stage-label">
                    <div class="lab-stage">
                        <div class="lab-burst-core"></div>
                        """
        + "".join(
            f'<div class="lab-burst-particle" style="--bx:{bx}px; --by:{by}px; transition-delay:{0.05 + index * 0.02:.2f}s;"></div>'
            for index, (bx, by) in enumerate(
                [(46, -8), (-44, -12), (30, 34), (-32, 32), (10, -46), (-10, 46), (48, 20), (-48, -20)]
            )
        )
        + """
                        <span class="lab-play-hint"></span>
                    </div>
                </label>
            </div>
            <div class="lab-card">
                <div class="lab-card-title">4 · Progress Ring</div>
                <div class="lab-card-use">Goal or milestone progress — a Hall of Fame achievement closing in on target.</div>
                <input type="checkbox" id="lab4" class="lab-toggle">
                <label for="lab4" class="lab-stage-label">
                    <div class="lab-stage">
                        <svg width="86" height="86" viewBox="0 0 86 86">
                            <circle class="lab-ring-track" cx="43" cy="43" r="36" fill="none" stroke-width="7"></circle>
                            <circle class="lab-ring-fill" cx="43" cy="43" r="36" fill="none" stroke-width="7"></circle>
                        </svg>
                        <div class="lab-ring-label">82%</div>
                        <span class="lab-play-hint"></span>
                    </div>
                </label>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )



def render_executive_page() -> None:
    """Executive Summary page.
Rendered as a single st.markdown(unsafe_allow_html=True) string.
Environment constraints honoured here:
  - no <script> (stripped by dangerouslySetInnerHTML); interactivity is pure CSS :checked
  - every :checked selector is a *sibling* chain verified against the literal nesting below
  - _compact() guarantees no blank line survives into the markup (CommonMark code-block trap)
  - no element's visibility depends on an animation completing; base state is the final state
  - no percentage heights on flex items in a column container; bar heights are computed px
Swap EXEC_DATA below for the live query result; field names match the data layer.
"""
    d = {
        "career_events": 76,
        "career_revenue": 14300,
        "unique_clients": 30,
        "repeat_clients": 20,
        "first_time_clients": 10,
        "current_streak": 6,
        "best_streak": 14,
        "weekly": [
            {"label": "W1", "events": 5, "revenue": 520, "is_record": False},
            {"label": "W2", "events": 7, "revenue": 690, "is_record": False},
            {"label": "W3", "events": 13, "revenue": 1240, "is_record": True},
            {"label": "W4", "events": 8, "revenue": 830, "is_record": False},
            {"label": "W5", "events": 9, "revenue": 910, "is_record": False},
            {"label": "W6", "events": 7, "revenue": 480, "is_record": False},
        ],
        "monthly": [
            {"label": "APR", "events": 9, "revenue": 1680, "is_record": False},
            {"label": "MAY", "events": 14, "revenue": 2540, "is_record": False},
            {"label": "JUN", "events": 17, "revenue": 3120, "is_record": False},
            {"label": "JUL", "events": 21, "revenue": 3970, "is_record": True},
        ],
        "weekday": [
            {"label": "MON", "events": 5, "revenue": 640, "is_record": False},
            {"label": "TUE", "events": 17, "revenue": 2180, "is_record": True},
            {"label": "WED", "events": 12, "revenue": 1490, "is_record": False},
            {"label": "THU", "events": 9, "revenue": 1120, "is_record": False},
            {"label": "FRI", "events": 14, "revenue": 1760, "is_record": False},
        ],
        "clients": [
            {"name": "Macy's", "events": 12, "revenue": 2140},
            {"name": "Bloomingdale's", "events": 9, "revenue": 1620},
            {"name": "Hampton Inn", "events": 7, "revenue": 1180},
            {"name": "Davis Polk & Wardwell", "events": 6, "revenue": 980},
            {"name": "Dunkin", "events": 5, "revenue": 720},
        ],
        "sectors": [
            {"name": "Retail", "pct": 42, "color": "var(--accent-coral)"},
            {"name": "Hospitality", "pct": 24, "color": "var(--accent-blue)"},
            {"name": "Legal", "pct": 18, "color": "var(--accent-gold)"},
            {"name": "Government", "pct": 10, "color": "var(--accent-purple)"},
            {"name": "Food Service", "pct": 6, "color": "var(--accent-success)"},
        ],
        "milestones": [
            {"name": "First 50 Events", "detail": "Achieved", "pct": 100, "done": True},
            {"name": "5 Jurisdictions", "detail": "Achieved", "pct": 100, "done": True},
            {"name": "10-Day Streak", "detail": "Achieved", "pct": 100, "done": True},
            {"name": "$25,000 Career Revenue", "detail": "$14.3k of $25k", "pct": 57, "done": False},
            {"name": "100 Career Events", "detail": "76 of 100", "pct": 76, "done": False},
        ],
    }

    def esc(value) -> str:
        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def money(value) -> str:
        value = float(value)
        if abs(value) >= 1000:
            text = f"${value / 1000:.1f}k"
            return text.replace(".0k", "k")
        return f"${value:,.0f}"

    def fmt(value, metric: str) -> str:
        return money(value) if metric == "revenue" else f"{value:,.0f}"

    def axis_ceiling(peak: float):
        if peak <= 0:
            return 1, 4
        for step in (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75,
                     100, 125, 150, 200, 250, 300, 400, 500, 600, 750,
                     1000, 1250, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000):
            if step * 4 >= peak:
                return step, step * 4
        return 25000, 100000

    def compact(markup: str) -> str:
        return "\n".join(line.strip() for line in markup.splitlines() if line.strip())

    plot_h, bar_max, bar_min = 132, 112, 5

    def chart(series, metric: str, view_id: str) -> str:
        values = [row[metric] for row in series]
        peak = max(values) if values else 0
        step, top = axis_ceiling(peak)
        grid = []
        for level_index in range(4, -1, -1):
            level = step * level_index
            y = min(plot_h - 1, plot_h - round((level / top) * bar_max))
            css_class = "exec-grid-line is-base" if level_index == 0 else "exec-grid-line"
            grid.append(f'<div class="{css_class}" style="top:{y}px"></div>')
            if level_index in (0, 2, 4):
                grid.append(f'<span class="exec-grid-tag" style="top:{y}px">{esc(fmt(level, metric))}</span>')
        bars, axis = [], []
        for index, row in enumerate(series):
            value = row[metric]
            height = max(bar_min, round(value / top * bar_max)) if value > 0 else 3
            record = " is-record" if row["is_record"] else ""
            delay = f"{0.06 + index * 0.05:.2f}s"
            bars.append(
                f'<div class="exec-bar-col{record}">'
                f'<div class="exec-bar-value">{esc(fmt(value, metric))}</div>'
                f'<div class="exec-bar-shape{record}" style="height:{height}px;animation-delay:{delay}"></div>'
                f"</div>"
            )
            axis.append(f'<span>{esc(row["label"])}</span>')
        best = max(series, key=lambda row: row[metric]) if series else None
        foot = ""
        if best is not None:
            total = sum(values)
            average = total / len(values)
            foot = (
                '<div class="exec-trend-foot">'
                f'<span>Peak <strong>{esc(best["label"])}</strong> &middot; {esc(fmt(best[metric], metric))}</span>'
                f'<span>Average <strong>{esc(fmt(round(average), metric))}</strong></span>'
                f'<span>Total <strong>{esc(fmt(total, metric))}</strong></span>'
                "</div>"
            )
        return (
            f'<div class="exec-trend-view" id="{view_id}">'
            f'<div class="exec-plot">{"".join(grid)}<div class="exec-bar-row">{"".join(bars)}</div></div>'
            f'<div class="exec-axis">{"".join(axis)}</div>{foot}</div>'
        )

    weekly, monthly, weekday = d["weekly"], d["monthly"], d["weekday"]
    clients, sectors = d["clients"], d["milestones"] and d["sectors"]
    top_client = clients[0]
    best_month = max(monthly, key=lambda row: row["events"])
    avg_per_event = round(d["career_revenue"] / max(1, d["career_events"]))
    repeat_rate = round(d["repeat_clients"] / max(1, d["unique_clients"]) * 100)
    month_delta = monthly[-1]["events"] - monthly[-2]["events"] if len(monthly) > 1 else 0
    achieved = sum(1 for m in d["milestones"] if m["done"])
    in_progress = len(d["milestones"]) - achieved

    spark_w, spark_h = 320.0, 44.0
    spark_values = [row["revenue"] for row in weekly]
    low, high = min(spark_values), max(spark_values)
    span = (high - low) or 1
    points = []
    for index, value in enumerate(spark_values):
        x = (spark_w * index / (len(spark_values) - 1)) if len(spark_values) > 1 else spark_w / 2
        y = spark_h - 4 - ((value - low) / span) * (spark_h - 11)
        points.append((round(x, 1), round(y, 1)))
    spark_line = " ".join(f"{x},{y}" for x, y in points)
    spark_area = f"{points[0][0]},{spark_h} {spark_line} {points[-1][0]},{spark_h}"
    last_x, last_y = points[-1]

    stops, running = [], 0
    for sector in sectors:
        stops.append(f'{sector["color"]} {running}% {running + sector["pct"]}%')
        running += sector["pct"]
    donut = f"conic-gradient(from -90deg, {', '.join(stops)})"

    css = """
<style>
.page-nav { display: flex; gap: .5rem; margin-bottom: .8rem; }
.page-nav a { color: var(--text-muted) !important; text-decoration: none !important; font-size: .68rem; font-weight: 800; letter-spacing: .05em; text-transform: uppercase; padding: .4rem .8rem; border-radius: 999px; border: 1px solid rgba(var(--slate-border-rgb),.28); transition: color .18s ease, border-color .18s ease; }
.page-nav a:hover { color: var(--text-primary) !important; border-color: rgba(var(--accent-teal-rgb),.5); }
.page-nav a.active { color: var(--accent-teal) !important; border-color: rgba(var(--accent-teal-rgb),.5); }
@keyframes execRiseIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
@keyframes execAuraDrift { from { transform: translate3d(-7%, 0, 0) scale(1.04); } to { transform: translate3d(7%, 0, 0) scale(1.16); } }
@keyframes execPulse { 0%, 100% { opacity: .35; transform: scale(1); } 50% { opacity: 1; transform: scale(1.55); } }
@keyframes execSparkDraw { from { stroke-dashoffset: 900; } to { stroke-dashoffset: 0; } }
@keyframes execBarGrow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes execTickerScroll { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.exec-hero { position: relative; overflow: hidden; border-radius: 22px; border: 1px solid rgba(var(--slate-border-rgb),.22); margin: 0 0 .9rem; background: radial-gradient(120% 140% at 10% -15%, rgba(var(--accent-teal-rgb),.17), transparent 55%), radial-gradient(95% 130% at 100% 0%, rgba(var(--accent-blue-rgb),.14), transparent 62%), linear-gradient(165deg, rgba(16,29,49,.96), rgba(6,13,24,.985)); box-shadow: 0 26px 60px rgba(0,0,0,.45), inset 0 1px 0 rgba(var(--white-rgb),.06); animation: execRiseIn .55s var(--ease-emphasized) both; }
.exec-hero-aura { position: absolute; left: -25%; right: -25%; top: -60%; height: 200%; pointer-events: none; opacity: .85; background: radial-gradient(closest-side, rgba(var(--accent-teal-rgb),.2), transparent 72%); animation: execAuraDrift 15s ease-in-out infinite alternate; }
.exec-hero-mesh { position: absolute; inset: 0; pointer-events: none; opacity: .45; background-image: linear-gradient(rgba(var(--slate-border-rgb),.09) 1px, transparent 1px), linear-gradient(90deg, rgba(var(--slate-border-rgb),.09) 1px, transparent 1px); background-size: 34px 34px; -webkit-mask-image: radial-gradient(125% 95% at 50% 0%, #000 18%, transparent 80%); mask-image: radial-gradient(125% 95% at 50% 0%, #000 18%, transparent 80%); }
.exec-hero-inner { position: relative; z-index: 2; padding: 1rem 1.05rem 1.1rem; }
.exec-hero-radio { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
.exec-hero-top { display: flex; align-items: center; justify-content: space-between; gap: .6rem; }
.exec-hero-eyebrow { display: inline-flex; align-items: center; gap: .42rem; font-size: .56rem; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; color: var(--text-tertiary); }
.exec-hero-pulse { width: 6px; height: 6px; border-radius: 50%; flex: 0 0 auto; background: var(--accent-teal); box-shadow: 0 0 10px rgba(var(--accent-teal-rgb),.9); animation: execPulse 2.4s ease-in-out infinite; }
.exec-hero-badge { display: inline-flex; align-items: center; gap: .3rem; padding: .26rem .55rem; border-radius: 999px; white-space: nowrap; border: 1px solid rgba(var(--accent-gold-rgb),.45); background: rgba(var(--accent-gold-rgb),.12); color: var(--accent-gold-pale); font-size: .53rem; font-weight: 900; letter-spacing: .07em; text-transform: uppercase; }
.exec-hero-stage { position: relative; min-height: 112px; display: flex; align-items: flex-end; margin: .5rem 0 .2rem; }
.exec-hero-figure { display: none; width: 100%; align-items: flex-end; gap: .55rem; }
#figEvents { display: flex; }
#heroRevenue:checked ~ .exec-hero-stage #figEvents, #heroClients:checked ~ .exec-hero-stage #figEvents { display: none; }
#heroEvents:checked ~ .exec-hero-stage #figEvents { display: flex; }
#heroRevenue:checked ~ .exec-hero-stage #figRevenue { display: flex; }
#heroClients:checked ~ .exec-hero-stage #figClients { display: flex; }
.exec-hero-numwrap { flex: 0 0 auto; filter: drop-shadow(0 12px 26px rgba(var(--accent-teal-rgb),.24)); }
.exec-hero-number { display: block; font-family: "Inter", "SF Pro Display", "Segoe UI", Arial, sans-serif; font-size: clamp(3.5rem, 21vw, 6.2rem); font-weight: 900; line-height: .8; letter-spacing: -.055em; color: var(--text-primary); }
.exec-hero-number.is-wide { font-size: clamp(2.5rem, 14vw, 4.6rem); letter-spacing: -.045em; }
@supports (-webkit-background-clip: text) { .exec-hero-number { background-image: linear-gradient(168deg, #ffffff 4%, var(--accent-teal-hover) 44%, var(--accent-teal) 74%, var(--accent-blue) 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; } }
.exec-hero-meta { display: flex; flex-direction: column; gap: .16rem; padding-bottom: .5rem; min-width: 0; }
.exec-hero-unit { font-size: .78rem; font-weight: 900; letter-spacing: .01em; color: var(--text-secondary-bright); }
.exec-hero-sub { font-size: .58rem; font-weight: 600; line-height: 1.35; color: var(--text-muted); }
.exec-hero-delta { display: inline-flex; align-self: flex-start; align-items: center; gap: .25rem; margin-top: .28rem; padding: .18rem .45rem; border-radius: 6px; font-size: .54rem; font-weight: 900; letter-spacing: .04em; border: 1px solid rgba(var(--accent-success-rgb),.3); background: rgba(var(--accent-success-rgb),.13); color: var(--accent-success); }
.exec-hero-seg { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .28rem; padding: .25rem; margin: .55rem 0 .8rem; border-radius: 12px; border: 1px solid rgba(var(--slate-border-rgb),.2); background: rgba(var(--navy-900-rgb),.55); }
.exec-hero-seg-btn { display: block; text-align: center; padding: .42rem .2rem; border-radius: 9px; cursor: pointer; -webkit-tap-highlight-color: transparent; font-size: .57rem; font-weight: 800; letter-spacing: .07em; text-transform: uppercase; color: var(--text-muted); background: transparent; box-shadow: 0 0 0 0 rgba(var(--accent-teal-rgb),0); transition: background .24s var(--ease-standard), color .24s var(--ease-standard), box-shadow .24s var(--ease-standard); }
#heroEvents:checked ~ .exec-hero-seg label[for="heroEvents"], #heroRevenue:checked ~ .exec-hero-seg label[for="heroRevenue"], #heroClients:checked ~ .exec-hero-seg label[for="heroClients"] { background: linear-gradient(135deg, rgba(var(--accent-teal-rgb),.3), rgba(var(--accent-teal-rgb),.1)); color: var(--text-primary); box-shadow: 0 0 0 1px rgba(var(--accent-teal-rgb),.45); }
.exec-hero-spark { display: block; width: 100%; height: 46px; overflow: visible; }
.exec-spark-line { fill: none; stroke: var(--accent-teal); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; vector-effect: non-scaling-stroke; stroke-dasharray: 900; stroke-dashoffset: 0; animation: execSparkDraw 1.4s var(--ease-emphasized) .2s both; }
.exec-spark-tick { stroke: var(--accent-teal-hover); stroke-width: 2; stroke-linecap: round; vector-effect: non-scaling-stroke; }
.exec-spark-caption { display: flex; align-items: center; justify-content: space-between; gap: .5rem; margin: .1rem 0 .8rem; font-size: .53rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted); }
.exec-spark-caption strong { color: var(--accent-teal); font-weight: 900; }
.exec-hero-rail { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid rgba(var(--slate-border-rgb),.18); padding-top: .75rem; }
.exec-hero-cell { position: relative; display: flex; flex-direction: column; align-items: center; gap: .18rem; padding: 0 .25rem; min-width: 0; }
.exec-hero-cell + .exec-hero-cell::before { content: ""; position: absolute; left: 0; top: 8%; bottom: 8%; width: 1px; background: rgba(var(--slate-border-rgb),.18); }
.exec-hero-cell-val { font-size: 1.02rem; font-weight: 900; line-height: 1; color: var(--text-primary); text-align: center; }
.exec-hero-cell-lab { font-size: .49rem; font-weight: 800; letter-spacing: .09em; text-transform: uppercase; color: var(--text-muted); text-align: center; }
.exec-kpi-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: .55rem; margin: 0 0 1rem; }
@media (max-width: 700px) { .exec-kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.exec-flip { position: relative; height: 100px; perspective: 900px; -webkit-tap-highlight-color: transparent; animation: execRiseIn .5s var(--ease-emphasized) both; }
.exec-flip-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
.exec-flip-label { display: block; width: 100%; height: 100%; cursor: pointer; }
.exec-flip-inner { position: relative; width: 100%; height: 100%; transform-style: preserve-3d; transform: rotateY(0deg); transition: transform .55s cubic-bezier(.4,.2,.2,1); }
.exec-flip-toggle:checked ~ .exec-flip-label .exec-flip-inner { transform: rotateY(180deg); }
.exec-flip-face { position: absolute; inset: 0; overflow: hidden; backface-visibility: hidden; -webkit-backface-visibility: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .2rem; text-align: center; border-radius: 12px; padding: .55rem; border: 1px solid rgba(var(--slate-border-rgb),.18); box-shadow: 0 14px 34px rgba(0,0,0,.2); }
.exec-flip-front { background: radial-gradient(circle at 50% 0%, rgba(var(--white-rgb),.06), transparent 46%), linear-gradient(145deg, rgba(21,36,58,.9), rgba(8,18,32,.94)); }
.exec-flip-back { transform: rotateY(180deg); border-color: rgba(var(--accent-teal-rgb),.32); background: radial-gradient(circle at 50% 0%, rgba(var(--accent-teal-rgb),.1), transparent 55%), linear-gradient(145deg, rgba(13,25,43,.96), rgba(8,18,32,.98)); }
.exec-kpi-icon { font-size: 1.1rem; }
.exec-kpi-label { font-size: .55rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted); }
.exec-kpi-value { font-size: 1.35rem; font-weight: 900; line-height: 1.05; color: var(--text-primary); }
.exec-kpi-value.is-text { font-size: .92rem; }
.exec-kpi-back-title { font-size: .49rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--accent-teal); }
.exec-kpi-back-row { font-size: .8rem; font-weight: 800; color: var(--text-primary); }
.exec-kpi-back-row span { display: block; font-size: .53rem; font-weight: 600; color: var(--text-secondary-dim); }
.exec-tap-hint { position: absolute; bottom: 4px; right: 7px; font-size: .45rem; font-weight: 800; letter-spacing: .04em; color: var(--accent-teal); opacity: .75; }
.exec-tap-hint::before { content: "tap"; }
.exec-section { position: relative; overflow: hidden; border: 1px solid rgba(var(--slate-border-rgb),.22); border-radius: var(--radius-lg); background: var(--surface-card-gradient); margin-bottom: .65rem; animation: execRiseIn .5s var(--ease-emphasized) both; }
.exec-section-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
.exec-section-head { display: flex; align-items: center; justify-content: space-between; gap: .6rem; padding: .8rem .95rem; cursor: pointer; -webkit-tap-highlight-color: transparent; }
.exec-section-title-group { display: flex; flex-direction: column; gap: .12rem; min-width: 0; }
.exec-section-name { color: var(--text-primary); font-size: .82rem; font-weight: 800; }
.exec-section-teaser { color: var(--text-muted); font-size: .63rem; }
.exec-section-chevron { flex: 0 0 auto; color: var(--accent-teal); font-size: .78rem; transform: rotate(0deg); transition: transform .3s var(--ease-standard); }
.exec-section-toggle:checked ~ .exec-section-head .exec-section-chevron { transform: rotate(180deg); }
.exec-section-body-wrap { display: grid; grid-template-rows: 0fr; transition: grid-template-rows .42s cubic-bezier(.3,.7,.3,1); }
.exec-section-toggle:checked ~ .exec-section-body-wrap { grid-template-rows: 1fr; }
.exec-section-body { min-height: 0; overflow: hidden; padding: 0 .95rem .95rem; }
.exec-trend-panel { position: relative; }
.exec-lever-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
.exec-lever-row { display: flex; flex-wrap: wrap; gap: .35rem; margin-bottom: .4rem; }
.exec-lever-row.is-metric { margin-bottom: .85rem; }
.exec-lever-label { display: inline-block; padding: .32rem .74rem; border-radius: 999px; cursor: pointer; -webkit-tap-highlight-color: transparent; border: 1px solid rgba(var(--slate-border-rgb),.3); background: rgba(var(--surface-rgb),.4); color: var(--text-muted); font-size: .58rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; transition: background .22s var(--ease-standard), color .22s var(--ease-standard), border-color .22s var(--ease-standard); }
#trendWeekly:checked ~ .exec-lever-row label[for="trendWeekly"], #trendMonthly:checked ~ .exec-lever-row label[for="trendMonthly"], #trendWeekday:checked ~ .exec-lever-row label[for="trendWeekday"], #metEvents:checked ~ .exec-lever-row label[for="metEvents"], #metRevenue:checked ~ .exec-lever-row label[for="metRevenue"] { background: linear-gradient(135deg, rgba(var(--accent-teal-rgb),.28), rgba(var(--accent-teal-rgb),.1)); color: var(--text-primary); border-color: rgba(var(--accent-teal-rgb),.55); }
.exec-trend-view { display: none; }
#viewWeeklyEvents { display: block; }
#trendMonthly:checked ~ .exec-trend-views #viewWeeklyEvents, #trendWeekday:checked ~ .exec-trend-views #viewWeeklyEvents, #metRevenue:checked ~ .exec-trend-views #viewWeeklyEvents { display: none; }
#trendWeekly:checked ~ #metEvents:checked ~ .exec-trend-views #viewWeeklyEvents, #trendWeekly:checked ~ #metRevenue:checked ~ .exec-trend-views #viewWeeklyRevenue, #trendMonthly:checked ~ #metEvents:checked ~ .exec-trend-views #viewMonthlyEvents, #trendMonthly:checked ~ #metRevenue:checked ~ .exec-trend-views #viewMonthlyRevenue, #trendWeekday:checked ~ #metEvents:checked ~ .exec-trend-views #viewWeekdayEvents, #trendWeekday:checked ~ #metRevenue:checked ~ .exec-trend-views #viewWeekdayRevenue { display: block; }
.exec-plot { position: relative; height: 132px; padding-left: 32px; }
.exec-grid-line { position: absolute; left: 32px; right: 0; height: 1px; background: rgba(var(--slate-border-rgb),.13); }
.exec-grid-line.is-base { background: rgba(var(--slate-border-rgb),.34); }
.exec-grid-tag { position: absolute; left: 0; width: 28px; text-align: right; transform: translateY(-50%); font-size: .45rem; font-weight: 800; letter-spacing: .02em; color: var(--text-muted-alt2); }
.exec-bar-row { position: absolute; left: 32px; right: 0; top: 0; bottom: 0; display: flex; align-items: flex-end; gap: .38rem; }
.exec-bar-col { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: .2rem; }
.exec-bar-value { font-size: .5rem; font-weight: 900; line-height: 1.1; white-space: nowrap; color: var(--text-secondary); }
.exec-bar-col.is-record .exec-bar-value { color: var(--accent-gold-pale); }
.exec-bar-col.is-record .exec-bar-value::before { content: "\\2605 "; }
.exec-bar-shape { width: 100%; max-width: 30px; border-radius: 6px 6px 2px 2px; transform-origin: bottom center; transform: scaleY(1); background: linear-gradient(180deg, var(--accent-teal), rgba(var(--accent-teal-rgb),.3)); box-shadow: inset 0 0 0 1px rgba(var(--accent-teal-rgb),.2); animation: execBarGrow .55s var(--ease-emphasized) both; }
.exec-bar-shape.is-record { background: linear-gradient(180deg, var(--accent-gold), rgba(var(--accent-gold-rgb),.32)); box-shadow: 0 0 14px rgba(var(--accent-gold-rgb),.35); }
.exec-axis { display: flex; gap: .38rem; margin-top: .4rem; padding-left: 32px; }
.exec-axis span { flex: 1 1 0; min-width: 0; text-align: center; font-size: .52rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; color: var(--text-muted); }
.exec-trend-foot { display: flex; flex-wrap: wrap; gap: .3rem .9rem; margin-top: .7rem; padding-top: .6rem; border-top: 1px solid rgba(var(--slate-border-rgb),.14); font-size: .57rem; color: var(--text-muted); }
.exec-trend-foot strong { color: var(--text-primary); font-weight: 800; }
.exec-podium { display: flex; align-items: flex-end; gap: .45rem; margin-bottom: .85rem; }
.exec-podium-slot { flex: 1 1 0; min-width: 0; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: .22rem; padding: .55rem .3rem .5rem; border-radius: 12px 12px 0 0; border: 1px solid rgba(var(--slate-border-rgb),.24); border-bottom: 2px solid rgba(var(--slate-border-rgb),.3); background: linear-gradient(180deg, rgba(var(--surface-rgb),.7), rgba(var(--navy-900-rgb),.5)); }
.exec-podium-slot.rank-1 { border-color: rgba(var(--accent-gold-rgb),.42); border-bottom-color: rgba(var(--accent-gold-rgb),.5); box-shadow: 0 0 26px rgba(var(--accent-gold-rgb),.12); }
.exec-podium-medal { font-size: 1.25rem; }
.exec-podium-name { font-size: .61rem; font-weight: 800; color: var(--text-primary); text-align: center; line-height: 1.2; }
.exec-podium-stat { font-size: .55rem; color: var(--text-muted); text-align: center; }
.exec-rank-row { display: grid; grid-template-columns: 1.15rem 1fr auto; align-items: center; gap: .55rem; padding: .48rem 0; border-top: 1px solid rgba(var(--slate-border-rgb),.14); }
.exec-rank-num { font-size: .66rem; font-weight: 800; color: var(--text-muted); }
.exec-rank-main { min-width: 0; }
.exec-rank-name { font-size: .7rem; font-weight: 700; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.exec-rank-track { height: 4px; margin-top: .3rem; border-radius: 999px; overflow: hidden; background: rgba(var(--slate-border-rgb),.18); }
.exec-rank-fill { height: 4px; border-radius: 999px; background: linear-gradient(90deg, var(--accent-teal), var(--accent-blue)); }
.exec-rank-stat { font-size: .64rem; font-weight: 800; color: var(--accent-teal); white-space: nowrap; }
.exec-donut-wrap { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }
.exec-donut { position: relative; width: 132px; height: 132px; border-radius: 50%; flex: 0 0 auto; }
.exec-donut::after { content: ""; position: absolute; inset: 20px; border-radius: 50%; background: linear-gradient(160deg, rgba(16,29,49,.99), rgba(8,17,31,1)); }
.exec-donut-core { position: absolute; inset: 0; z-index: 2; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .05rem; }
.exec-donut-core-val { font-size: 1.15rem; font-weight: 900; line-height: 1; color: var(--text-primary); }
.exec-donut-core-lab { font-size: .46rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: var(--text-muted); }
.exec-legend { display: flex; flex-direction: column; gap: .34rem; flex: 1 1 150px; min-width: 150px; }
.exec-legend-row { display: flex; align-items: center; gap: .45rem; font-size: .66rem; color: var(--text-secondary); }
.exec-legend-dot { width: 8px; height: 8px; border-radius: 2px; flex: 0 0 auto; }
.exec-legend-row strong { margin-left: auto; color: var(--text-primary); font-weight: 800; }
.exec-milestone { margin-bottom: .8rem; }
.exec-milestone:last-child { margin-bottom: 0; }
.exec-milestone-head { display: flex; align-items: center; justify-content: space-between; gap: .6rem; margin-bottom: .3rem; }
.exec-milestone-name { font-size: .69rem; font-weight: 800; color: var(--text-primary); }
.exec-milestone-name.is-done::before { content: "\\2713  "; color: var(--accent-success); }
.exec-milestone-detail { font-size: .57rem; color: var(--text-muted); white-space: nowrap; }
.exec-progress-track { height: 7px; border-radius: 999px; overflow: hidden; background: rgba(var(--slate-border-rgb),.2); }
.exec-progress-fill { height: 7px; border-radius: 999px; background: linear-gradient(90deg, var(--accent-teal), var(--accent-blue)); }
.exec-progress-fill.is-done { background: linear-gradient(90deg, var(--accent-success), var(--accent-teal)); }
.exec-ticker { position: relative; overflow: hidden; height: 36px; display: flex; align-items: center; margin: 0 0 1rem; border-radius: var(--radius-md); border: 1px solid rgba(var(--slate-border-rgb),.24); background: linear-gradient(90deg, rgba(var(--navy-900-rgb),.7), rgba(var(--surface-rgb),.5)); }
.exec-ticker::before, .exec-ticker::after { content: ""; position: absolute; top: 0; bottom: 0; width: 24px; z-index: 1; pointer-events: none; }
.exec-ticker::before { left: 0; background: linear-gradient(90deg, rgba(var(--navy-900-rgb),.9), transparent); }
.exec-ticker::after { right: 0; background: linear-gradient(270deg, rgba(var(--navy-900-rgb),.9), transparent); }
.exec-ticker-track { display: flex; align-items: center; gap: 1.8rem; width: max-content; padding: 0 1rem; animation: execTickerScroll 24s linear infinite; }
.exec-ticker-item { flex: 0 0 auto; display: flex; align-items: center; gap: .3rem; white-space: nowrap; font-size: .62rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; color: var(--text-secondary); }
.exec-ticker-item strong { color: var(--text-primary); font-weight: 900; }
@media (prefers-reduced-motion: reduce) { .exec-hero, .exec-hero-aura, .exec-hero-pulse, .exec-flip, .exec-section, .exec-bar-shape, .exec-spark-line, .exec-ticker-track { animation: none !important; } }
</style>
"""

    ticker_items = [
        f'&#127937; <strong>{d["career_events"]}</strong> career events',
        f'&#128176; career <strong>{money(d["career_revenue"])}</strong>',
        f'&#129309; <strong>{d["unique_clients"]}</strong> clients &middot; {repeat_rate}% repeat',
        f'&#128293; <strong>{d["current_streak"]}</strong>-day streak',
        f'&#127942; best month <strong>{esc(best_month["label"])}</strong> &middot; {best_month["events"]} events',
    ]
    ticker = "".join(f'<span class="exec-ticker-item">{item}</span>' for item in ticker_items * 2)

    figures = [
        ("figEvents", f'{d["career_events"]}', "", "Events worked",
         "Career total across every jurisdiction",
         f'&#9650; +{month_delta} vs last month' if month_delta > 0 else f'{month_delta} vs last month'),
        ("figRevenue", money(d["career_revenue"]), " is-wide", "Revenue booked",
         f'{money(avg_per_event)} average per event',
         f'&#9650; {money(monthly[-1]["revenue"])} this month'),
        ("figClients", f'{d["unique_clients"]}', "", "Client roster",
         f'{d["repeat_clients"]} repeat &middot; {d["first_time_clients"]} first-time',
         f'&#9650; {repeat_rate}% come back'),
    ]
    figure_html = "".join(
        f'<div class="exec-hero-figure" id="{fid}">'
        f'<div class="exec-hero-numwrap"><span class="exec-hero-number{wide}">{value}</span></div>'
        f'<div class="exec-hero-meta"><div class="exec-hero-unit">{unit}</div>'
        f'<div class="exec-hero-sub">{sub}</div><span class="exec-hero-delta">{delta}</span></div></div>'
        for fid, value, wide, unit, sub, delta in figures
    )

    rail = [
        (f'{d["current_streak"]}', "Day streak"),
        (esc(best_month["label"]), "Best month"),
        (money(avg_per_event), "Avg / event"),
    ]
    rail_html = "".join(
        f'<div class="exec-hero-cell"><div class="exec-hero-cell-val">{value}</div>'
        f'<div class="exec-hero-cell-lab">{label}</div></div>'
        for value, label in rail
    )

    hero = (
        '<div class="exec-hero"><div class="exec-hero-aura"></div><div class="exec-hero-mesh"></div>'
        '<div class="exec-hero-inner">'
        '<input type="radio" name="heroMetric" id="heroEvents" class="exec-hero-radio" checked>'
        '<input type="radio" name="heroMetric" id="heroRevenue" class="exec-hero-radio">'
        '<input type="radio" name="heroMetric" id="heroClients" class="exec-hero-radio">'
        '<div class="exec-hero-top"><div class="exec-hero-eyebrow"><span class="exec-hero-pulse"></span>Career to date</div>'
        f'<div class="exec-hero-badge">&#9733; {esc(best_month["label"])} record month</div></div>'
        f'<div class="exec-hero-stage">{figure_html}</div>'
        '<div class="exec-hero-seg">'
        '<label for="heroEvents" class="exec-hero-seg-btn">Events</label>'
        '<label for="heroRevenue" class="exec-hero-seg-btn">Revenue</label>'
        '<label for="heroClients" class="exec-hero-seg-btn">Clients</label></div>'
        f'<svg class="exec-hero-spark" viewBox="0 0 {int(spark_w)} {int(spark_h)}" preserveAspectRatio="none" aria-hidden="true">'
        '<defs><linearGradient id="execSparkFill" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0%" stop-color="rgba(45,212,191,.34)"></stop>'
        '<stop offset="100%" stop-color="rgba(45,212,191,0)"></stop></linearGradient></defs>'
        f'<polygon points="{spark_area}" fill="url(#execSparkFill)"></polygon>'
        f'<polyline class="exec-spark-line" points="{spark_line}"></polyline>'
        f'<line class="exec-spark-tick" x1="{last_x}" y1="{last_y}" x2="{last_x}" y2="{spark_h}"></line></svg>'
        f'<div class="exec-spark-caption"><span>Revenue &middot; last {len(weekly)} weeks</span>'
        f'<span>Latest <strong>{money(weekly[-1]["revenue"])}</strong></span></div>'
        f'<div class="exec-hero-rail">{rail_html}</div>'
        "</div></div>"
    )

    kpis = [
        ("k1", "&#128200;", "Repeat Rate", f"{repeat_rate}%", "Loyalty",
         f'{d["repeat_clients"]}', f'of {d["unique_clients"]} clients returned'),
        ("k2", "&#128506;", "Sectors", f'{len(sectors)}', "Widest",
         esc(sectors[0]["name"]), f'{sectors[0]["pct"]}% of all events'),
        ("k3", "&#128293;", "Best Streak", f'{d["best_streak"]}', "Current",
         f'{d["current_streak"]} days', "consecutive working days"),
        ("k4", "&#127942;", "Top Client", esc(top_client["name"]), "Booked",
         f'{top_client["events"]}', f'events &middot; {money(top_client["revenue"])}'),
    ]
    kpi_html = "".join(
        f'<div class="exec-flip" style="animation-delay:{0.04 + index * 0.06:.2f}s">'
        f'<input type="checkbox" id="{cid}" class="exec-flip-toggle">'
        f'<label for="{cid}" class="exec-flip-label"><div class="exec-flip-inner">'
        f'<div class="exec-flip-face exec-flip-front"><div class="exec-kpi-icon">{icon}</div>'
        f'<div class="exec-kpi-label">{label}</div>'
        f'<div class="exec-kpi-value{" is-text" if not str(value)[:1].isdigit() and not str(value)[:1] == "$" else ""}">{value}</div>'
        f'<span class="exec-tap-hint"></span></div>'
        f'<div class="exec-flip-face exec-flip-back"><div class="exec-kpi-back-title">{back_title}</div>'
        f'<div class="exec-kpi-back-row">{back_value}<span>{back_sub}</span></div>'
        f'<span class="exec-tap-hint"></span></div></div></label></div>'
        for index, (cid, icon, label, value, back_title, back_value, back_sub) in enumerate(kpis)
    )

    charts = "".join([
        chart(weekly, "events", "viewWeeklyEvents"),
        chart(weekly, "revenue", "viewWeeklyRevenue"),
        chart(monthly, "events", "viewMonthlyEvents"),
        chart(monthly, "revenue", "viewMonthlyRevenue"),
        chart(weekday, "events", "viewWeekdayEvents"),
        chart(weekday, "revenue", "viewWeekdayRevenue"),
    ])
    trends = (
        '<div class="exec-section" style="animation-delay:.26s">'
        '<input type="checkbox" id="secTrend" class="exec-section-toggle" checked>'
        '<label for="secTrend" class="exec-section-head"><div class="exec-section-title-group">'
        '<div class="exec-section-name">Performance Trends</div>'
        f'<div class="exec-section-teaser">Weekly / monthly / weekday &middot; events or revenue</div></div>'
        '<span class="exec-section-chevron">&#9662;</span></label>'
        '<div class="exec-section-body-wrap"><div class="exec-section-body"><div class="exec-trend-panel">'
        '<input type="radio" name="trendview" id="trendWeekly" class="exec-lever-toggle" checked>'
        '<input type="radio" name="trendview" id="trendMonthly" class="exec-lever-toggle">'
        '<input type="radio" name="trendview" id="trendWeekday" class="exec-lever-toggle">'
        '<input type="radio" name="trendmetric" id="metEvents" class="exec-lever-toggle" checked>'
        '<input type="radio" name="trendmetric" id="metRevenue" class="exec-lever-toggle">'
        '<div class="exec-lever-row">'
        '<label for="trendWeekly" class="exec-lever-label">Weekly</label>'
        '<label for="trendMonthly" class="exec-lever-label">Monthly</label>'
        '<label for="trendWeekday" class="exec-lever-label">Weekday</label></div>'
        '<div class="exec-lever-row is-metric">'
        '<label for="metEvents" class="exec-lever-label">Events</label>'
        '<label for="metRevenue" class="exec-lever-label">Revenue</label></div>'
        f'<div class="exec-trend-views">{charts}</div>'
        "</div></div></div></div>"
    )

    podium_order = [1, 0, 2]
    podium_heights = {0: 112, 1: 94, 2: 82}
    medals = {0: "&#129351;", 1: "&#129352;", 2: "&#129353;"}
    podium = "".join(
        f'<div class="exec-podium-slot rank-{position + 1}" style="height:{podium_heights[position]}px">'
        f'<div class="exec-podium-medal">{medals[position]}</div>'
        f'<div class="exec-podium-name">{esc(clients[position]["name"])}</div>'
        f'<div class="exec-podium-stat">{clients[position]["events"]} events</div></div>'
        for position in podium_order
        if position < len(clients)
    )
    peak_client_events = max(row["events"] for row in clients) or 1
    rank_rows = "".join(
        f'<div class="exec-rank-row"><span class="exec-rank-num">{index + 1}</span>'
        f'<div class="exec-rank-main"><div class="exec-rank-name">{esc(row["name"])}</div>'
        f'<div class="exec-rank-track"><div class="exec-rank-fill" style="width:{max(4, round(row["events"] / peak_client_events * 100))}%"></div></div></div>'
        f'<span class="exec-rank-stat">{row["events"]} &middot; {money(row["revenue"])}</span></div>'
        for index, row in enumerate(clients[3:], start=3)
    )
    leaderboard = (
        '<div class="exec-section" style="animation-delay:.32s">'
        '<input type="checkbox" id="secClients" class="exec-section-toggle">'
        '<label for="secClients" class="exec-section-head"><div class="exec-section-title-group">'
        '<div class="exec-section-name">Client Leaderboard</div>'
        f'<div class="exec-section-teaser">{esc(top_client["name"])} leads at {top_client["events"]} events</div></div>'
        '<span class="exec-section-chevron">&#9662;</span></label>'
        '<div class="exec-section-body-wrap"><div class="exec-section-body">'
        f'<div class="exec-podium">{podium}</div>{rank_rows}</div></div></div>'
    )

    legend = "".join(
        f'<div class="exec-legend-row"><span class="exec-legend-dot" style="background:{sector["color"]}"></span>'
        f'{esc(sector["name"])}<strong>{sector["pct"]}%</strong></div>'
        for sector in sectors
    )
    territory = (
        '<div class="exec-section" style="animation-delay:.38s">'
        '<input type="checkbox" id="secTerritory" class="exec-section-toggle">'
        '<label for="secTerritory" class="exec-section-head"><div class="exec-section-title-group">'
        '<div class="exec-section-name">Territory &amp; Sectors</div>'
        f'<div class="exec-section-teaser">{len(sectors)} sectors &middot; {esc(sectors[0]["name"])} leads at {sectors[0]["pct"]}%</div></div>'
        '<span class="exec-section-chevron">&#9662;</span></label>'
        '<div class="exec-section-body-wrap"><div class="exec-section-body"><div class="exec-donut-wrap">'
        f'<div class="exec-donut" style="background:{donut}">'
        f'<div class="exec-donut-core"><div class="exec-donut-core-val">{d["career_events"]}</div>'
        '<div class="exec-donut-core-lab">Events</div></div></div>'
        f'<div class="exec-legend">{legend}</div></div></div></div></div>'
    )

    milestone_rows = "".join(
        f'<div class="exec-milestone"><div class="exec-milestone-head">'
        f'<span class="exec-milestone-name{" is-done" if row["done"] else ""}">{esc(row["name"])}</span>'
        f'<span class="exec-milestone-detail">{esc(row["detail"])}</span></div>'
        f'<div class="exec-progress-track"><div class="exec-progress-fill{" is-done" if row["done"] else ""}" '
        f'style="width:{max(3, min(100, row["pct"]))}%"></div></div></div>'
        for row in d["milestones"]
    )
    fame = (
        '<div class="exec-section" style="animation-delay:.44s">'
        '<input type="checkbox" id="secFame" class="exec-section-toggle">'
        '<label for="secFame" class="exec-section-head"><div class="exec-section-title-group">'
        '<div class="exec-section-name">Hall of Fame</div>'
        f'<div class="exec-section-teaser">{achieved} achieved &middot; {in_progress} in progress</div></div>'
        '<span class="exec-section-chevron">&#9662;</span></label>'
        f'<div class="exec-section-body-wrap"><div class="exec-section-body">{milestone_rows}</div></div></div>'
    )

    st.markdown(
        compact(
            css
            + '<div class="page-nav"><a href="?page=lab" target="_self">&larr; Lab</a>'
            '<a href="?page=exec" target="_self" class="active">Executive</a></div>'
            '<div class="section-kicker">DEMO DATA &middot; STRUCTURE PREVIEW</div>'
            '<div class="section-title">EXECUTIVE SUMMARY</div>'
            + hero
            + f'<div class="exec-ticker"><div class="exec-ticker-track">{ticker}</div></div>'
            + f'<div class="exec-kpi-grid">{kpi_html}</div>'
            + trends
            + leaderboard
            + territory
            + fame
        ),
        unsafe_allow_html=True,
    )

def main() -> None:
    configure_page()
    has_route_context = bool(dict(st.query_params))
    if not has_route_context:
        render_splash_screen()
        return
    if st.query_params.get("page", "lab") == "exec":
        render_executive_page()
    else:
        render_testing_lab()


if __name__ == "__main__":
    main()
