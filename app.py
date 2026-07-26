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
            max-height: 100vh !important;
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
            from {{ opacity: 0; transform: scaleX(0); }}
            to {{ opacity: 1; transform: scaleX(1); }}
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
            overflow: hidden;
            background: var(--bg-void);
            display: flex;
            align-items: center;
            justify-content: center;
            padding-bottom: 20vh;
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
            transform: translateY(-50%) scaleX(0);
            transform-origin: center;
            border-radius: 999px;
            z-index: 0;
            opacity: 0;
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
            transform: scaleX(0);
            opacity: 0;
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
            opacity: 0;
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

        /* 2. COUNT-UP */
        @property --lab-count { syntax: '<integer>'; inherits: false; initial-value: 0; }
        .lab-count-num { --lab-count: 0; font-size: 2.4rem; font-weight: 900; color: var(--text-primary); counter-reset: labcount var(--lab-count); }
        .lab-count-num::after { content: counter(labcount); }
        .lab-toggle:checked ~ .lab-stage-label .lab-count-num { animation: labCountUp 1.4s cubic-bezier(.2,.7,.3,1) forwards; }
        @keyframes labCountUp { to { --lab-count: 76; } }

        /* 3. CELEBRATION BURST */
        .lab-burst-core { width: 34px; height: 34px; border-radius: 50%; background: radial-gradient(circle, var(--accent-gold), rgba(245,197,66,0)); transform: scale(0); }
        .lab-toggle:checked ~ .lab-stage-label .lab-burst-core { animation: labBurstCore .5s ease-out forwards; }
        @keyframes labBurstCore { 0% { transform: scale(0); opacity: 1; } 60% { transform: scale(1.4); opacity: 1; } 100% { transform: scale(1); opacity: .9; } }
        .lab-burst-particle { position: absolute; top: 50%; left: 50%; width: 6px; height: 6px; border-radius: 50%; background: var(--accent-teal); opacity: 0; transform: translate(-50%, -50%); }
        .lab-toggle:checked ~ .lab-stage-label .lab-burst-particle { animation: labBurstFly .8s ease-out forwards; animation-delay: .1s; }
        @keyframes labBurstFly { 0% { opacity: 1; transform: translate(-50%, -50%) translate(0, 0) scale(1); } 100% { opacity: 0; transform: translate(-50%, -50%) translate(var(--bx), var(--by)) scale(.4); } }

        /* 4. PROGRESS RING */
        .lab-ring-track { stroke: rgba(var(--slate-border-rgb),.25); }
        .lab-ring-fill { stroke: var(--accent-purple); stroke-linecap: round; stroke-dasharray: 226; stroke-dashoffset: 226; transform-origin: center; transform: rotate(-90deg); transition: none; }
        .lab-toggle:checked ~ .lab-stage-label .lab-ring-fill { animation: labRingFill 1.3s cubic-bezier(.3,.7,.3,1) forwards; }
        @keyframes labRingFill { to { stroke-dashoffset: 40; } }
        .lab-ring-label { position: absolute; font-size: 1.05rem; font-weight: 900; color: var(--text-primary); opacity: 0; }
        .lab-toggle:checked ~ .lab-stage-label .lab-ring-label { animation: labRiseIn .4s ease .9s forwards; }
        @keyframes labRiseIn { to { opacity: 1; } }
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
                <input type="checkbox" id="lab2" class="lab-toggle">
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
            f'<div class="lab-burst-particle" style="--bx:{bx}px; --by:{by}px; animation-delay:{0.08 + index * 0.015:.2f}s;"></div>'
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



def main() -> None:
    configure_page()
    has_route_context = bool(dict(st.query_params))
    if not has_route_context:
        render_splash_screen()
        return
    render_testing_lab()


if __name__ == "__main__":
    main()
