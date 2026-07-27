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
    st.markdown(
        """
        <style>
        .page-nav { display: flex; gap: .5rem; margin-bottom: .8rem; }
        .page-nav a { color: var(--text-muted) !important; text-decoration: none !important; font-size: .68rem; font-weight: 800; letter-spacing: .05em; text-transform: uppercase; padding: .4rem .8rem; border-radius: 999px; border: 1px solid rgba(var(--slate-border-rgb),.28); transition: color .18s ease, border-color .18s ease; }
        .page-nav a:hover { color: var(--text-primary) !important; border-color: rgba(var(--accent-teal-rgb),.5); }
        .page-nav a.active { color: var(--accent-teal) !important; border-color: rgba(var(--accent-teal-rgb),.5); }

        @keyframes execTickerScroll { from { transform: translateX(0); } to { transform: translateX(-50%); } }
        .exec-ticker { position: relative; overflow: hidden; border: 1px solid rgba(var(--slate-border-rgb),.24); border-radius: var(--radius-md); background: linear-gradient(90deg, rgba(var(--navy-900-rgb),.7), rgba(var(--surface-rgb),.5)); margin: 0 0 1rem; height: 36px; display: flex; align-items: center; }
        .exec-ticker::before, .exec-ticker::after { content: ""; position: absolute; top: 0; bottom: 0; width: 24px; z-index: 1; pointer-events: none; }
        .exec-ticker::before { left: 0; background: linear-gradient(90deg, rgba(var(--navy-900-rgb),.9), transparent); }
        .exec-ticker::after { right: 0; background: linear-gradient(270deg, rgba(var(--navy-900-rgb),.9), transparent); }
        .exec-ticker-track { display: flex; align-items: center; gap: 1.8rem; width: max-content; padding: 0 1rem; animation: execTickerScroll 22s linear infinite; }
        .exec-ticker-item { flex: 0 0 auto; display: flex; align-items: center; gap: .3rem; font-size: .64rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; color: var(--text-secondary); white-space: nowrap; }
        .exec-ticker-item strong { color: var(--text-primary); font-weight: 900; }
        .exec-ticker-dot { width: 4px; height: 4px; border-radius: 50%; background: rgba(var(--slate-border-rgb),.5); margin-right: .9rem; }

        @keyframes execRiseIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .exec-kpi-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: .6rem; margin: 0 0 1.1rem; }
        @media (max-width: 700px) { .exec-kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
        .exec-flip { position: relative; height: 104px; perspective: 900px; -webkit-tap-highlight-color: transparent; animation: execRiseIn .5s var(--ease-emphasized) both; }
        .exec-flip:nth-child(1) { animation-delay: .02s; } .exec-flip:nth-child(2) { animation-delay: .08s; }
        .exec-flip:nth-child(3) { animation-delay: .14s; } .exec-flip:nth-child(4) { animation-delay: .2s; }
        .exec-flip-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
        .exec-flip-label { display: block; width: 100%; height: 100%; cursor: pointer; }
        .exec-flip-inner { position: relative; width: 100%; height: 100%; transition: transform .55s cubic-bezier(.4,.2,.2,1); transform-style: preserve-3d; }
        .exec-flip-toggle:checked ~ .exec-flip-label .exec-flip-inner { transform: rotateY(180deg); }
        .exec-flip-face { position: absolute; inset: 0; overflow: hidden; backface-visibility: hidden; -webkit-backface-visibility: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .22rem; text-align: center; border-radius: 12px; padding: .6rem; border: 1px solid rgba(var(--slate-border-rgb),.18); box-shadow: 0 14px 34px rgba(0,0,0,.2); }
        .exec-flip-front { background: radial-gradient(circle at 50% 0%, rgba(var(--white-rgb),.06), transparent 46%), linear-gradient(145deg, rgba(21,36,58,.9), rgba(8,18,32,.94)); }
        .exec-flip-back { transform: rotateY(180deg); background: radial-gradient(circle at 50% 0%, rgba(var(--accent-teal-rgb),.1), transparent 55%), linear-gradient(145deg, rgba(13,25,43,.96), rgba(8,18,32,.98)); border-color: rgba(var(--accent-teal-rgb),.32); }
        .exec-kpi-icon { font-size: 1.2rem; }
        .exec-kpi-label { font-size: .58rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted); }
        .exec-kpi-value { font-size: 1.5rem; font-weight: 900; color: var(--text-primary); }
        .exec-kpi-back-title { font-size: .5rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--accent-teal); }
        .exec-kpi-back-row { font-size: .82rem; font-weight: 800; color: var(--text-primary); }
        .exec-kpi-back-row span { display: block; font-size: .54rem; font-weight: 600; color: var(--text-secondary-dim); }
        .exec-tap-hint { position: absolute; bottom: 4px; right: 7px; font-size: .46rem; font-weight: 800; letter-spacing: .04em; color: var(--accent-teal); opacity: .75; }
        .exec-tap-hint::before { content: "tap"; }

        .exec-section { position: relative; border: 1px solid rgba(var(--slate-border-rgb),.22); border-radius: var(--radius-lg); background: var(--surface-card-gradient); margin-bottom: .65rem; overflow: hidden; animation: execRiseIn .5s var(--ease-emphasized) both; }
        .exec-section:nth-of-type(1) { animation-delay: .26s; } .exec-section:nth-of-type(2) { animation-delay: .32s; }
        .exec-section:nth-of-type(3) { animation-delay: .38s; } .exec-section:nth-of-type(4) { animation-delay: .44s; }
        .exec-section-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
        .exec-section-head { display: flex; align-items: center; justify-content: space-between; gap: .6rem; padding: .8rem .95rem; cursor: pointer; -webkit-tap-highlight-color: transparent; }
        .exec-section-title-group { display: flex; flex-direction: column; gap: .12rem; }
        .exec-section-name { color: var(--text-primary); font-size: .82rem; font-weight: 800; }
        .exec-section-teaser { color: var(--text-muted); font-size: .64rem; }
        .exec-section-chevron { color: var(--accent-teal); font-size: .78rem; transition: transform .3s var(--ease-standard); flex: 0 0 auto; }
        .exec-section-toggle:checked ~ .exec-section-head .exec-section-chevron { transform: rotate(180deg); }
        .exec-section-body-wrap { display: grid; grid-template-rows: 0fr; transition: grid-template-rows .42s cubic-bezier(.3,.7,.3,1); }
        .exec-section-toggle:checked ~ .exec-section-body-wrap { grid-template-rows: 1fr; }
        .exec-section-body { min-height: 0; overflow: hidden; padding: 0 .95rem .95rem; }

        .exec-lever-row { display: flex; gap: .4rem; margin-bottom: .8rem; }
        .exec-lever-toggle { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
        .exec-lever-label { padding: .34rem .78rem; border-radius: 999px; border: 1px solid rgba(var(--slate-border-rgb),.3); background: rgba(var(--surface-rgb),.4); color: var(--text-muted); font-size: .6rem; font-weight: 800; letter-spacing: .04em; text-transform: uppercase; cursor: pointer; -webkit-tap-highlight-color: transparent; transition: background .2s ease, color .2s ease, border-color .2s ease; }
        .exec-lever-toggle:checked ~ .exec-lever-label { background: linear-gradient(135deg, rgba(var(--accent-teal-rgb),.28), rgba(var(--accent-teal-rgb),.1)); color: var(--text-primary); border-color: rgba(var(--accent-teal-rgb),.55); }
        .exec-trend-view { display: none; }
        #trendWeekly:checked ~ .exec-trend-panel #viewWeekly,
        #trendMonthly:checked ~ .exec-trend-panel #viewMonthly,
        #trendWeekday:checked ~ .exec-trend-panel #viewWeekday { display: block; }
        .exec-bar-row { display: flex; align-items: flex-end; gap: .5rem; height: 130px; padding: 0 .1rem; }
        .exec-bar-col { flex: 1; display: flex; flex-direction: column; align-items: center; gap: .35rem; height: 100%; justify-content: flex-end; }
        .exec-bar-shape { width: 100%; max-width: 30px; border-radius: 6px 6px 2px 2px; background: linear-gradient(180deg, var(--accent-teal), rgba(45,212,191,.35)); position: relative; }
        .exec-bar-shape.is-record { background: linear-gradient(180deg, var(--accent-gold), rgba(245,197,66,.35)); box-shadow: 0 0 12px rgba(245,197,66,.4); }
        .exec-bar-label { font-size: .52rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: .03em; }

        .exec-podium { display: flex; align-items: flex-end; gap: .5rem; margin-bottom: .9rem; }
        .exec-podium-slot { flex: 1; display: flex; flex-direction: column; align-items: center; gap: .3rem; padding: .7rem .4rem; border-radius: 12px 12px 0 0; border: 1px solid rgba(var(--slate-border-rgb),.24); border-bottom: none; background: linear-gradient(180deg, rgba(var(--surface-rgb),.6), rgba(var(--navy-900-rgb),.5)); }
        .exec-podium-slot.rank-1 { padding-top: 1.1rem; border-color: rgba(var(--accent-gold-rgb),.4); }
        .exec-podium-medal { font-size: 1.3rem; }
        .exec-podium-name { font-size: .64rem; font-weight: 800; color: var(--text-primary); text-align: center; }
        .exec-podium-stat { font-size: .56rem; color: var(--text-muted); }
        .exec-rank-row { display: flex; align-items: center; gap: .6rem; padding: .5rem 0; border-top: 1px solid rgba(var(--slate-border-rgb),.14); font-size: .7rem; }
        .exec-rank-num { color: var(--text-muted); font-weight: 800; width: 1.4rem; }
        .exec-rank-name { flex: 1; color: var(--text-primary); font-weight: 700; }
        .exec-rank-stat { color: var(--accent-teal); font-weight: 800; }

        .exec-donut-wrap { display: flex; align-items: center; gap: 1.1rem; flex-wrap: wrap; }
        .exec-donut { width: 128px; height: 128px; border-radius: 50%; flex: 0 0 auto; position: relative; }
        .exec-donut::after { content: ""; position: absolute; inset: 17px; border-radius: 50%; background: var(--bg-app-2); }
        .exec-legend { display: flex; flex-direction: column; gap: .32rem; flex: 1; min-width: 140px; }
        .exec-legend-row { display: flex; align-items: center; gap: .4rem; font-size: .66rem; color: var(--text-secondary); }
        .exec-legend-dot { width: 8px; height: 8px; border-radius: 2px; flex: 0 0 auto; }
        .exec-legend-row strong { margin-left: auto; color: var(--text-primary); }

        .exec-milestone { margin-bottom: .8rem; }
        .exec-milestone:last-child { margin-bottom: 0; }
        .exec-milestone-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: .3rem; }
        .exec-milestone-name { font-size: .7rem; font-weight: 800; color: var(--text-primary); }
        .exec-milestone-name.is-done::before { content: "\\2713  "; color: var(--accent-success); }
        .exec-milestone-detail { font-size: .58rem; color: var(--text-muted); }
        .exec-progress-track { height: 7px; border-radius: 999px; background: rgba(var(--slate-border-rgb),.2); overflow: hidden; }
        .exec-progress-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--accent-teal), var(--accent-blue)); }
        </style>
        <div class="page-nav"><a href="?page=lab" target="_self">&larr; Lab</a><a href="?page=exec" target="_self" class="active">Executive</a></div>
        <div class="section-kicker">DEMO DATA &middot; STRUCTURE PREVIEW</div>
        <div class="section-title">EXECUTIVE SUMMARY</div>
        <div class="exec-ticker"><div class="exec-ticker-track">
        <span class="exec-ticker-item">&#127937; <strong>76</strong> CAREER EVENTS</span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#128176; THIS WEEK <strong>$480</strong></span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#129309; LATEST <strong>DUNKIN</strong></span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#128293; <strong>6</strong>-DAY STREAK</span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#127937; <strong>76</strong> CAREER EVENTS</span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#128176; THIS WEEK <strong>$480</strong></span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#129309; LATEST <strong>DUNKIN</strong></span><span class="exec-ticker-dot"></span>
        <span class="exec-ticker-item">&#128293; <strong>6</strong>-DAY STREAK</span>
        </div></div>
        <div class="exec-kpi-grid">
        <div class="exec-flip"><input type="checkbox" id="k1" class="exec-flip-toggle"><label for="k1" class="exec-flip-label"><div class="exec-flip-inner">
        <div class="exec-flip-face exec-flip-front"><div class="exec-kpi-icon">&#127937;</div><div class="exec-kpi-label">Career Events</div><div class="exec-kpi-value">76</div><span class="exec-tap-hint"></span></div>
        <div class="exec-flip-face exec-flip-back"><div class="exec-kpi-back-title">Timeline</div><div class="exec-kpi-back-row">100%<span>Completion rate</span></div><span class="exec-tap-hint"></span></div>
        </div></label></div>
        <div class="exec-flip"><input type="checkbox" id="k2" class="exec-flip-toggle"><label for="k2" class="exec-flip-label"><div class="exec-flip-inner">
        <div class="exec-flip-face exec-flip-front"><div class="exec-kpi-icon">&#128176;</div><div class="exec-kpi-label">Revenue</div><div class="exec-kpi-value">$14.3k</div><span class="exec-tap-hint"></span></div>
        <div class="exec-flip-face exec-flip-back"><div class="exec-kpi-back-title">Per Event</div><div class="exec-kpi-back-row">$188<span>Average confirmed</span></div><span class="exec-tap-hint"></span></div>
        </div></label></div>
        <div class="exec-flip"><input type="checkbox" id="k3" class="exec-flip-toggle"><label for="k3" class="exec-flip-label"><div class="exec-flip-inner">
        <div class="exec-flip-face exec-flip-front"><div class="exec-kpi-icon">&#129309;</div><div class="exec-kpi-label">Clients</div><div class="exec-kpi-value">30</div><span class="exec-tap-hint"></span></div>
        <div class="exec-flip-face exec-flip-back"><div class="exec-kpi-back-title">Mix</div><div class="exec-kpi-back-row">20<span>Repeat &middot; 10 first-time</span></div><span class="exec-tap-hint"></span></div>
        </div></label></div>
        <div class="exec-flip"><input type="checkbox" id="k4" class="exec-flip-toggle"><label for="k4" class="exec-flip-label"><div class="exec-flip-inner">
        <div class="exec-flip-face exec-flip-front"><div class="exec-kpi-icon">&#128293;</div><div class="exec-kpi-label">Streak</div><div class="exec-kpi-value">6</div><span class="exec-tap-hint"></span></div>
        <div class="exec-flip-face exec-flip-back"><div class="exec-kpi-back-title">Best Ever</div><div class="exec-kpi-back-row">14<span>Longest streak</span></div><span class="exec-tap-hint"></span></div>
        </div></label></div>
        </div>
        <div class="exec-section">
        <input type="checkbox" id="secTrend" class="exec-section-toggle" checked>
        <label for="secTrend" class="exec-section-head"><div class="exec-section-title-group"><div class="exec-section-name">Performance Trends</div><div class="exec-section-teaser">Weekly / Monthly / Weekday &middot; toggle below</div></div><span class="exec-section-chevron">&#9662;</span></label>
        <div class="exec-section-body-wrap"><div class="exec-section-body">
        <div class="exec-trend-panel">
        <input type="radio" name="trendview" id="trendWeekly" class="exec-lever-toggle" checked><label for="trendWeekly" class="exec-lever-label" style="margin-right:.4rem;display:inline-block;">Weekly</label>
        <input type="radio" name="trendview" id="trendMonthly" class="exec-lever-toggle"><label for="trendMonthly" class="exec-lever-label" style="margin-right:.4rem;display:inline-block;">Monthly</label>
        <input type="radio" name="trendview" id="trendWeekday" class="exec-lever-toggle"><label for="trendWeekday" class="exec-lever-label" style="display:inline-block;">Weekday</label>
        <div style="margin-top:.8rem;">
        <div class="exec-trend-view" id="viewWeekly"><div class="exec-bar-row">
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:38%"></div><div class="exec-bar-label">W1</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:52%"></div><div class="exec-bar-label">W2</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape is-record" style="height:100%"></div><div class="exec-bar-label">W3</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:64%"></div><div class="exec-bar-label">W4</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:71%"></div><div class="exec-bar-label">W5</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:58%"></div><div class="exec-bar-label">W6</div></div>
        </div></div>
        <div class="exec-trend-view" id="viewMonthly"><div class="exec-bar-row">
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:45%"></div><div class="exec-bar-label">APR</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:68%"></div><div class="exec-bar-label">MAY</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:82%"></div><div class="exec-bar-label">JUN</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape is-record" style="height:100%"></div><div class="exec-bar-label">JUL</div></div>
        </div></div>
        <div class="exec-trend-view" id="viewWeekday"><div class="exec-bar-row">
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:30%"></div><div class="exec-bar-label">MON</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape is-record" style="height:100%"></div><div class="exec-bar-label">TUE</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:74%"></div><div class="exec-bar-label">WED</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:56%"></div><div class="exec-bar-label">THU</div></div>
        <div class="exec-bar-col"><div class="exec-bar-shape" style="height:81%"></div><div class="exec-bar-label">FRI</div></div>
        </div></div>
        </div></div>
        </div></div></div>
        <div class="exec-section">
        <input type="checkbox" id="secClients" class="exec-section-toggle">
        <label for="secClients" class="exec-section-head"><div class="exec-section-title-group"><div class="exec-section-name">Client Leaderboard</div><div class="exec-section-teaser">Macy's leads at 12 events</div></div><span class="exec-section-chevron">&#9662;</span></label>
        <div class="exec-section-body-wrap"><div class="exec-section-body">
        <div class="exec-podium">
        <div class="exec-podium-slot rank-2"><div class="exec-podium-medal">&#129352;</div><div class="exec-podium-name">Bloomingdale's</div><div class="exec-podium-stat">9 events</div></div>
        <div class="exec-podium-slot rank-1"><div class="exec-podium-medal">&#129351;</div><div class="exec-podium-name">Macy's</div><div class="exec-podium-stat">12 events</div></div>
        <div class="exec-podium-slot rank-3"><div class="exec-podium-medal">&#129353;</div><div class="exec-podium-name">Hampton Inn</div><div class="exec-podium-stat">7 events</div></div>
        </div>
        <div class="exec-rank-row"><span class="exec-rank-num">4</span><span class="exec-rank-name">Davis Polk &amp; Wardwell</span><span class="exec-rank-stat">6 &middot; $980</span></div>
        <div class="exec-rank-row"><span class="exec-rank-num">5</span><span class="exec-rank-name">Dunkin</span><span class="exec-rank-stat">5 &middot; $720</span></div>
        </div></div></div>
        <div class="exec-section">
        <input type="checkbox" id="secTerritory" class="exec-section-toggle">
        <label for="secTerritory" class="exec-section-head"><div class="exec-section-title-group"><div class="exec-section-name">Territory &amp; Sectors</div><div class="exec-section-teaser">5 sectors &middot; Retail leads at 42%</div></div><span class="exec-section-chevron">&#9662;</span></label>
        <div class="exec-section-body-wrap"><div class="exec-section-body">
        <div class="exec-donut-wrap">
        <div class="exec-donut" style="background:conic-gradient(var(--accent-coral) 0% 42%, var(--accent-blue) 42% 66%, var(--accent-gold) 66% 84%, var(--accent-purple) 84% 94%, var(--accent-success) 94% 100%);"></div>
        <div class="exec-legend">
        <div class="exec-legend-row"><span class="exec-legend-dot" style="background:var(--accent-coral)"></span>Retail<strong>42%</strong></div>
        <div class="exec-legend-row"><span class="exec-legend-dot" style="background:var(--accent-blue)"></span>Hospitality<strong>24%</strong></div>
        <div class="exec-legend-row"><span class="exec-legend-dot" style="background:var(--accent-gold)"></span>Legal<strong>18%</strong></div>
        <div class="exec-legend-row"><span class="exec-legend-dot" style="background:var(--accent-purple)"></span>Government<strong>10%</strong></div>
        <div class="exec-legend-row"><span class="exec-legend-dot" style="background:var(--accent-success)"></span>Food Service<strong>6%</strong></div>
        </div></div>
        </div></div></div>
        <div class="exec-section">
        <input type="checkbox" id="secFame" class="exec-section-toggle">
        <label for="secFame" class="exec-section-head"><div class="exec-section-title-group"><div class="exec-section-name">Hall of Fame</div><div class="exec-section-teaser">3 achieved &middot; 1 in progress</div></div><span class="exec-section-chevron">&#9662;</span></label>
        <div class="exec-section-body-wrap"><div class="exec-section-body">
        <div class="exec-milestone"><div class="exec-milestone-head"><span class="exec-milestone-name is-done">First 50 Events</span><span class="exec-milestone-detail">Achieved</span></div><div class="exec-progress-track"><div class="exec-progress-fill" style="width:100%"></div></div></div>
        <div class="exec-milestone"><div class="exec-milestone-head"><span class="exec-milestone-name is-done">5 Jurisdictions</span><span class="exec-milestone-detail">Achieved</span></div><div class="exec-progress-track"><div class="exec-progress-fill" style="width:100%"></div></div></div>
        <div class="exec-milestone"><div class="exec-milestone-head"><span class="exec-milestone-name is-done">10-Day Streak</span><span class="exec-milestone-detail">Achieved</span></div><div class="exec-progress-track"><div class="exec-progress-fill" style="width:100%"></div></div></div>
        <div class="exec-milestone"><div class="exec-milestone-head"><span class="exec-milestone-name">$25,000 Career Revenue</span><span class="exec-milestone-detail">$14.3k of $25k</span></div><div class="exec-progress-track"><div class="exec-progress-fill" style="width:57%"></div></div></div>
        </div></div></div>
        """,
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
