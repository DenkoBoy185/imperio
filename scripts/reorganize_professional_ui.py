#!/usr/bin/env python3
"""
Reorganizes and upgrades C:\\Users\\Bruno\\.gemini\\antigravity\\scratch\\imperio\\index.html
into a true Linear/Stripe/Bloomberg-grade Executive Command Center UI:
- Single-line, zero-overlap Sticky Top Navbar (no fixed mobile button overlapping pills, no 3-row rainbow button wrap)
- Uniform, calm, high-contrast Sidebar & Segmented Pillar Navigation
- Dedicated #live-fx-anchor inside Pillar I so live-prices.js never injects above the navbar
- All 19 sections grouped cleanly into 6 Thematic Master Domains.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "index.html"


def extract_section(html: str, sec_id: str) -> str:
    pattern = re.compile(
        rf'(<section\s+id="{re.escape(sec_id)}"[^>]*>.*?</section>)',
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        raise ValueError(f"Section #{sec_id} not found!")
    return m.group(1)


def main():
    raw = INDEX_FILE.read_text(encoding="utf-8")

    # Extract all sections cleanly
    sec_hero = extract_section(raw, "hero")
    sec_ayame_protocol = extract_section(raw, "ayame-protocol")
    sec_floor_plan = extract_section(raw, "floor-plan")
    sec_capex = extract_section(raw, "capex")
    sec_motorcycle = extract_section(raw, "motorcycle")
    sec_dojos = extract_section(raw, "dojos")
    sec_combat = extract_section(raw, "combat")
    sec_supplements = extract_section(raw, "supplements")
    sec_japanese = extract_section(raw, "japanese")
    sec_extremis = extract_section(raw, "extremis")
    sec_opex = extract_section(raw, "opex")
    sec_matrix = extract_section(raw, "matrix")
    sec_ayame_radar = extract_section(raw, "ayame-radar")
    sec_ayame_dates = extract_section(raw, "ayame-dates")
    sec_restaurants = extract_section(raw, "restaurants")
    sec_mma_roadmap = extract_section(raw, "mma-6-0-roadmap")
    sec_walkout_godzilla = extract_section(raw, "walkout-godzilla-mothra")
    sec_ayame_24_expediciones = extract_section(raw, "ayame-24-expediciones")
    sec_okinawa_captain = extract_section(raw, "okinawa-captain")

    # Ensure #hero has the countdown block and #live-fx-anchor exactly once
    sec_hero = re.sub(
        r'<!-- RELOJ TÁCTICO EN TIEMPO REAL.*?</section>',
        '</section>',
        sec_hero,
        flags=re.DOTALL,
    )
    sec_hero = re.sub(
        r'<div id="live-fx-anchor"></div>\s*</section>',
        '</section>',
        sec_hero,
        flags=re.DOTALL,
    )

    countdown_and_fx_block = """
            <!-- RELOJ TÁCTICO EN TIEMPO REAL (SINCRONIZADO CON HORA DE JAPÓN JST) -->
            <div class="countdown-banner">
              <div class="countdown-banner-header">
                <span>⏱️ CRONÓMETRO TÁCTICO EN TIEMPO REAL • HUSO HORARIO DE JAPÓN (JST / UTC+9)</span>
                <span class="badge-pill-gold">CAMPAÑA INVICTA 6-0 (77 KG) → CAPITÁN O-3 OKINAWA</span>
              </div>
              <div id="imperio-live-countdowns" class="countdown-grid">
                <div class="countdown-card">
                  <div class="cd-label">01 · OPERACIÓN JAPÓN (OCT 2027)</div>
                  <div id="cd-oct-2027" class="cd-timer">--d --h --m --s</div>
                  <div class="cd-sub">Expedición #1: Ginza Kimono &amp; Base Tokio</div>
                </div>
                <div class="countdown-card">
                  <div class="cd-label">02 · PELEA #1 DEBUT 77 KG (ABR 2028)</div>
                  <div id="cd-apr-2028" class="cd-timer">--d --h --m --s</div>
                  <div class="cd-sub">KROSS×OVER / JMMAF • Inicio del 6-0</div>
                </div>
                <div class="countdown-card">
                  <div class="cd-label">03 · 6ª PELEA: GODZILLA &amp; MOTHRA (SEP 2029)</div>
                  <div id="cd-sep-2029" class="cd-timer" style="color:var(--gold);">--d --h --m --s</div>
                  <div class="cd-sub">Retiro Invicto 6-0 + Helicóptero Privado</div>
                </div>
                <div class="countdown-card">
                  <div class="cd-label">04 · FASE CAPITÁN O-3 OKINAWA (OCT 2029)</div>
                  <div id="cd-oct-2029" class="cd-timer">--d --h --m --s</div>
                  <div class="cd-sub">Kadena Air Base + Hogar Frente al Mar con あやめ</div>
                </div>
              </div>
            </div>

            <!-- ANCLAJE DEDICADO PARA EL MOTOR DE DIVISAS EN VIVO (USD / JPY / KRW / THB) -->
            <div id="live-fx-anchor"></div>
    """

    sec_hero_upgraded = sec_hero.replace(
        "</section>",
        countdown_and_fx_block + "\n        </section>",
    )

    new_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ATLAS DEL IMPERIO — Bruno & あやめ (2027–2029+)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@500;700;900&family=Noto+Serif+JP:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #080a0f;
            --bg-surface: #0d1117;
            --bg-card: #121721;
            --bg-card-hover: #171e2b;
            --gold: #d4a853;
            --amber: #eab308;
            --sakura: #f472b6;
            --crimson: #ef4444;
            --emerald: #22c55e;
            --cyan: #38bdf8;
            --purple: #a78bfa;
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --border: #21262d;
            --border-subtle: rgba(255, 255, 255, 0.07);
            --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-head: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'Orbitron', monospace;
            --font-jp: 'Noto Serif JP', serif;
            --accent-gradient: linear-gradient(135deg, #e5c158, #d4a853);
            --sidebar-width: 264px;
            --topbar-height: 58px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            scroll-behavior: smooth;
        }}

        body {{
            font-family: var(--font-body);
            background-color: var(--bg-base);
            color: var(--text-main);
            line-height: 1.6;
            display: flex;
            min-height: 100vh;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }}

        /* Top Scroll Progress Bar */
        #progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--gold), #f59e0b);
            z-index: 10000;
            width: 0%;
            transition: width 0.1s;
        }}

        /* =====================================================================
           SIDEBAR NAVIGATION (CLEAN, MONOCHROME-GOLD EXECUTIVE HIERARCHY)
           ===================================================================== */
        .sidebar {{
            width: var(--sidebar-width);
            background: #0b0e14;
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            z-index: 1100;
            transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        body.sidebar-collapsed .sidebar {{
            transform: translateX(-100%);
        }}

        .sidebar-header {{
            height: var(--topbar-height);
            padding: 0 1.15rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
        }}

        .sidebar-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .sidebar-crest {{
            width: 28px;
            height: 28px;
            border-radius: 7px;
            background: rgba(212, 168, 83, 0.14);
            border: 1px solid rgba(212, 168, 83, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.9rem;
        }}

        .sidebar-header h1 {{
            font-size: 0.84rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            line-height: 1.15;
        }}

        .sidebar-sub {{
            font-size: 0.66rem;
            color: var(--text-muted);
            font-weight: 500;
            display: block;
        }}

        .nav-links {{
            list-style: none;
            padding: 0.6rem 0.65rem 1.5rem 0.65rem;
            overflow-y: auto;
            flex-grow: 1;
        }}

        .nav-links::-webkit-scrollbar {{
            width: 4px;
        }}
        .nav-links::-webkit-scrollbar-thumb {{
            background: #21262d;
            border-radius: 4px;
        }}

        .nav-group-label {{
            font-size: 0.64rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #6e7681;
            padding: 0.85rem 0.6rem 0.35rem 0.6rem;
            margin-top: 0.25rem;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
        }}
        .nav-group-label:first-child {{
            border-top: none;
            margin-top: 0;
            padding-top: 0.35rem;
        }}

        .nav-links li a {{
            display: flex;
            align-items: center;
            gap: 9px;
            padding: 0.44rem 0.65rem;
            color: #9ca3af;
            text-decoration: none;
            font-size: 0.78rem;
            font-weight: 500;
            border-radius: 7px;
            transition: all 0.15s ease;
            margin-bottom: 1px;
        }}

        .nav-links li a .nav-num {{
            font-size: 0.66rem;
            font-weight: 700;
            color: #6e7681;
            min-width: 18px;
            font-variant-numeric: tabular-nums;
        }}

        .nav-links li a:hover {{
            color: #f3f4f6;
            background: rgba(255, 255, 255, 0.04);
            text-decoration: none;
        }}

        .nav-links li a.active {{
            color: #ffffff;
            background: rgba(212, 168, 83, 0.12);
            font-weight: 600;
        }}

        .nav-links li a.active .nav-num {{
            color: var(--gold);
        }}

        .sidebar-footer {{
            padding: 0.75rem 0.85rem;
            border-top: 1px solid var(--border);
            background: rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex-shrink: 0;
        }}

        .sidebar-footer-title {{
            font-size: 0.62rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.9px;
            color: #6e7681;
            margin-bottom: 2px;
        }}

        .sidebar-ext-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 5px;
        }}

        .sidebar-ext-btn {{
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 5px 4px;
            font-size: 0.68rem;
            font-weight: 600;
            color: #c9d1d9;
            background: #131822;
            border: 1px solid var(--border);
            border-radius: 6px;
            text-decoration: none;
            transition: all 0.15s;
        }}
        .sidebar-ext-btn:hover {{
            border-color: var(--gold);
            color: var(--gold);
            text-decoration: none;
        }}

        /* =====================================================================
           MAIN CONTENT & SINGLE-ROW STICKY COMMAND HEADER (ZERO OVERLAP)
           ===================================================================== */
        .main-content {{
            margin-left: var(--sidebar-width);
            padding: 0 2.5rem 4rem 2.5rem;
            width: calc(100% - var(--sidebar-width));
            max-width: 1600px;
            transition: margin-left 0.25s cubic-bezier(0.4, 0, 0.2, 1), width 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        body.sidebar-collapsed .main-content {{
            margin-left: 0;
            width: 100%;
        }}

        .top-command-bar {{
            position: sticky;
            top: 0;
            z-index: 1000;
            height: var(--topbar-height);
            background: rgba(8, 10, 15, 0.92);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            margin: 0 -2.5rem 2rem -2.5rem;
            padding: 0 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }}

        .topbar-left {{
            display: flex;
            align-items: center;
            gap: 10px;
            min-width: 0;
            flex: 1;
        }}

        .sidebar-toggle-btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            height: 34px;
            padding: 0 11px;
            border-radius: 7px;
            background: #121721;
            border: 1px solid var(--border);
            color: #e6edf3;
            font-family: var(--font-body);
            font-size: 0.76rem;
            font-weight: 600;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.15s ease;
        }}

        .sidebar-toggle-btn:hover {{
            border-color: var(--gold);
            color: var(--gold);
            background: rgba(212, 168, 83, 0.08);
        }}

        /* Segmented Single-Row Pillar Bar */
        .domain-pills-nav {{
            display: flex;
            align-items: center;
            gap: 4px;
            background: #0d1117;
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 3px;
            overflow-x: auto;
            scrollbar-width: none;
            white-space: nowrap;
        }}

        .domain-pills-nav::-webkit-scrollbar {{
            display: none;
        }}

        .domain-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            height: 28px;
            padding: 0 11px;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 600;
            text-decoration: none;
            color: #9ca3af;
            border: 1px solid transparent;
            transition: all 0.15s ease;
            flex-shrink: 0;
        }}

        .domain-pill .pill-num {{
            font-size: 0.66rem;
            font-weight: 700;
            color: var(--gold);
            opacity: 0.85;
        }}

        .domain-pill:hover,
        .domain-pill.active {{
            color: #ffffff;
            background: #171e2b;
            border-color: rgba(212, 168, 83, 0.35);
            text-decoration: none;
        }}

        /* Right Dossier Links Group */
        .external-dossiers {{
            display: flex;
            align-items: center;
            gap: 6px;
            flex-shrink: 0;
            padding-left: 10px;
            border-left: 1px solid var(--border);
        }}

        .dossier-chip {{
            display: inline-flex;
            align-items: center;
            gap: 5px;
            height: 30px;
            padding: 0 10px;
            border-radius: 7px;
            font-size: 0.73rem;
            font-weight: 600;
            color: #c9d1d9;
            background: #121721;
            border: 1px solid var(--border);
            text-decoration: none;
            white-space: nowrap;
            transition: all 0.15s ease;
        }}

        .dossier-chip:hover {{
            border-color: var(--gold);
            color: #ffffff;
            background: #171e2b;
            text-decoration: none;
        }}

        /* =====================================================================
           MASTER DOMAIN BANNERS (ARCHITECTURAL DIVIDERS)
           ===================================================================== */
        .domain-banner {{
            position: relative;
            overflow: hidden;
            border-radius: 14px;
            padding: 24px 28px;
            margin: 3rem 0 1.6rem 0;
            border: 1px solid var(--border);
            border-left: 4px solid var(--gold);
            background: linear-gradient(180deg, #111620 0%, #0c1017 100%);
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
            scroll-margin-top: 76px;
        }}

        .domain-banner:first-of-type {{
            margin-top: 0.25rem;
        }}

        .domain-banner::after {{
            content: attr(data-kanji);
            position: absolute;
            right: 24px;
            bottom: -12px;
            font-family: var(--font-jp);
            font-size: 4.8rem;
            font-weight: 700;
            color: rgba(255, 255, 255, 0.025);
            pointer-events: none;
            user-select: none;
        }}

        .domain-eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: var(--gold);
            background: rgba(212, 168, 83, 0.1);
            border: 1px solid rgba(212, 168, 83, 0.28);
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 10px;
        }}

        .domain-banner h2 {{
            font-size: 1.4rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 6px;
            letter-spacing: -0.01em;
        }}

        .domain-banner p {{
            color: var(--text-muted);
            font-size: 0.88rem;
            max-width: 920px;
            margin-bottom: 14px;
        }}

        .domain-sublinks {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}

        .domain-sublinks a {{
            font-size: 0.74rem;
            font-weight: 600;
            padding: 5px 11px;
            border-radius: 6px;
            background: rgba(255, 255, 255, 0.035);
            border: 1px solid var(--border);
            color: #c9d1d9;
            text-decoration: none;
            transition: all 0.15s;
        }}

        .domain-sublinks a:hover {{
            border-color: var(--gold);
            color: var(--gold);
            background: rgba(212, 168, 83, 0.08);
            text-decoration: none;
        }}

        /* =====================================================================
           SECTION CONTAINERS, TYPOGRAPHY & CARDS
           ===================================================================== */
        section {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.75rem 2rem;
            margin-bottom: 1.75rem;
            scroll-margin-top: 76px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22);
        }}

        h2.section-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 1.1rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid var(--border);
            letter-spacing: -0.01em;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
        }}

        h3 {{
            color: var(--text-main);
            margin-top: 1.1rem;
            margin-bottom: 0.7rem;
            font-size: 0.98rem;
            font-weight: 700;
        }}

        /* Hero & Countdown Banner */
        .hero-subtitle {{
            text-align: center;
            color: var(--gold);
            font-size: 0.95rem;
            margin-bottom: 1.4rem;
            letter-spacing: 0.8px;
            font-weight: 600;
        }}

        .hero {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
            gap: 0.9rem;
            margin-bottom: 1.4rem;
        }}

        .stat-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1.1rem 0.95rem;
            text-align: center;
            transition: border-color 0.2s, transform 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-2px);
            border-color: rgba(212, 168, 83, 0.5);
        }}

        .stat-value {{
            font-family: var(--font-mono);
            font-size: 1.4rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }}

        .stat-label {{
            font-size: 0.72rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.6px;
            font-weight: 600;
        }}

        .countdown-banner {{
            background: #10151f;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 16px 18px;
            margin-top: 0.5rem;
            margin-bottom: 1rem;
        }}

        .countdown-banner-header {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--gold);
            letter-spacing: 0.8px;
            text-transform: uppercase;
        }}

        .badge-pill-gold {{
            background: rgba(212, 168, 83, 0.12);
            border: 1px solid rgba(212, 168, 83, 0.35);
            color: var(--gold);
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 0.68rem;
            font-weight: 700;
        }}

        .countdown-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 10px;
        }}

        .countdown-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 12px 14px;
            text-align: left;
        }}

        .cd-label {{
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}

        .cd-timer {{
            font-family: var(--font-mono);
            font-size: 1.12rem;
            font-weight: 800;
            color: #ffffff;
            margin: 5px 0 3px 0;
        }}

        .cd-sub {{
            font-size: 0.72rem;
            color: var(--text-muted);
        }}

        /* Floor Plan */
        .floor-plan-img {{
            max-height: 72vh;
            width: auto;
            max-width: 100%;
            border-radius: 10px;
            border: 1px solid var(--border);
            box-shadow: 0 12px 28px rgba(0,0,0,0.5);
            display: block;
            margin: 0 auto 1.5rem auto;
        }}

        .plan-tab {{
            padding: 7px 13px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-family: var(--font-body);
            font-size: 0.78rem;
            font-weight: 600;
            border-radius: 7px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .plan-tab:hover {{
            border-color: var(--gold);
            color: var(--text-main);
        }}
        .plan-tab.active {{
            background: var(--gold);
            color: #080a0f;
            border-color: var(--gold);
            font-weight: 700;
        }}

        /* Cards & Accordions */
        .room-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            margin-bottom: 1rem;
            overflow: hidden;
        }}

        .room-header {{
            padding: 1rem 1.25rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255,255,255,0.015);
            transition: background 0.2s;
        }}

        .room-header:hover {{
            background: rgba(255,255,255,0.04);
        }}

        .room-title {{
            font-size: 0.92rem;
            font-weight: 700;
            color: #ffffff;
        }}

        .room-subtotal {{
            font-weight: 700;
            color: var(--gold);
            font-size: 0.86rem;
        }}

        .room-content {{
            padding: 0 1.25rem;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.35s ease-out, padding 0.35s ease;
        }}

        .room-content.open {{
            padding: 1.15rem 1.25rem;
            max-height: 6000px;
            overflow: auto;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 0.75rem;
            font-size: 0.82rem;
        }}

        th, td {{
            padding: 0.7rem 0.85rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }}

        th {{
            font-size: 0.72rem;
            color: var(--text-muted);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            background: rgba(0,0,0,0.28);
            position: sticky;
            top: 0;
        }}

        tr:hover td {{
            background: rgba(255,255,255,0.02);
        }}

        a {{
            color: var(--gold);
            text-decoration: none;
            transition: color 0.15s;
        }}

        a:hover {{
            color: #f3f4f6;
            text-decoration: underline;
        }}

        .btn-link {{
            display: inline-block;
            background: rgba(212, 168, 83, 0.12);
            border: 1px solid rgba(212, 168, 83, 0.35);
            color: var(--gold);
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            text-decoration: none;
            white-space: nowrap;
        }}

        .btn-link:hover {{
            background: var(--gold);
            color: var(--bg-base);
            text-decoration: none;
        }}

        /* Grid Cards */
        .grid-cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.1rem;
        }}

        .item-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1.25rem;
            position: relative;
            transition: border-color 0.2s;
        }}

        .item-card:hover {{
            border-color: rgba(212, 168, 83, 0.45);
        }}

        .item-card h4 {{
            color: #ffffff;
            margin-bottom: 0.45rem;
            font-size: 0.94rem;
            font-weight: 700;
        }}

        .item-card .price {{
            font-family: var(--font-mono);
            font-size: 1.08rem;
            color: var(--gold);
            margin: 0.7rem 0;
            font-weight: 700;
        }}

        .badge {{
            position: absolute;
            top: 0.9rem;
            right: 0.9rem;
            background: rgba(212, 168, 83, 0.15);
            border: 1px solid rgba(212, 168, 83, 0.4);
            color: var(--gold);
            padding: 0.18rem 0.55rem;
            border-radius: 6px;
            font-size: 0.68rem;
            font-weight: 700;
        }}

        /* OPEX Donut & Legend */
        .chart-container,
        .opex-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 2.5rem;
            align-items: center;
            background: var(--bg-card);
            padding: 1.75rem 2rem;
            border-radius: 10px;
            border: 1px solid var(--border);
            margin-bottom: 1.5rem;
        }}

        .donut-chart {{
            width: 210px;
            height: 210px;
            border-radius: 50%;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 8px 24px rgba(0,0,0,0.45);
            flex-shrink: 0;
        }}

        .donut-inner,
        .donut-hole {{
            width: 146px;
            height: 146px;
            background-color: var(--bg-card);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 10px;
        }}

        .donut-inner span {{
            font-family: var(--font-mono);
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-main);
            line-height: 1.3;
        }}

        .chart-legend {{
            list-style: none;
            flex: 1;
            min-width: 260px;
        }}

        .chart-legend li {{
            margin-bottom: 0.6rem;
            display: flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 0.85rem;
            color: var(--text-main);
        }}

        .legend-color {{
            width: 12px;
            height: 12px;
            border-radius: 3px;
            flex-shrink: 0;
        }}

        /* Tabs for 168h Matrix */
        .tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-bottom: 1.1rem;
        }}

        .tab-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.55rem 1rem;
            cursor: pointer;
            font-family: var(--font-body);
            font-size: 0.78rem;
            font-weight: 600;
            border-radius: 7px;
            transition: all 0.15s;
        }}

        .tab-btn.active, .tab-btn:hover {{
            background: rgba(212, 168, 83, 0.14);
            color: var(--gold);
            border-color: var(--gold);
        }}

        .tab-content {{
            display: none;
            animation: fadeIn 0.25s;
        }}

        .tab-content.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        #back-to-top {{
            position: fixed;
            bottom: 1.75rem;
            right: 1.75rem;
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--gold);
            width: 42px;
            height: 42px;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            font-size: 1.1rem;
            opacity: 0;
            pointer-events: none;
            transition: all 0.2s;
            z-index: 999;
            box-shadow: 0 6px 16px rgba(0,0,0,0.45);
        }}

        #back-to-top.visible {{
            opacity: 1;
            pointer-events: auto;
        }}

        #back-to-top:hover {{
            border-color: var(--gold);
            background: #171e2b;
            text-decoration: none;
        }}

        @media (max-width: 1180px) {{
            .sidebar {{
                transform: translateX(-100%);
            }}
            body.sidebar-open .sidebar {{
                transform: translateX(0);
                box-shadow: 20px 0 50px rgba(0,0,0,0.75);
            }}
            .main-content {{
                margin-left: 0;
                width: 100%;
                padding: 0 1.25rem 3rem 1.25rem;
            }}
            .top-command-bar {{
                margin: 0 -1.25rem 1.5rem -1.25rem;
                padding: 0 1rem;
            }}
            .external-dossiers {{
                display: none;
            }}
        }}
    </style>
</head>
<body>

    <div id="progress-bar"></div>

    <!-- ==================== EXECUTIVE SIDEBAR ==================== -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-brand">
                <div class="sidebar-crest">👑</div>
                <div>
                    <h1>ATLAS IMPERIO</h1>
                    <span class="sidebar-sub">Bruno &amp; あやめ • 2027–2029+</span>
                </div>
            </div>
        </div>

        <ul class="nav-links">
            <div class="nav-group-label">01 · Mando Central &amp; Finanzas</div>
            <li><a href="#hero"><span class="nav-num">1.1</span> Panel Ejecutivo &amp; Reloj JST</a></li>
            <li><a href="#opex"><span class="nav-num">1.2</span> Presupuesto Mensual (OPEX)</a></li>
            <li><a href="#capex"><span class="nav-num">1.3</span> Capital &amp; Muebles (CAPEX)</a></li>

            <div class="nav-group-label">02 · Nuestro Hogar, Moto &amp; 168H</div>
            <li><a href="#floor-plan"><span class="nav-num">2.1</span> Hogar 2LDK con あやめ</a></li>
            <li><a href="#motorcycle"><span class="nav-num">2.2</span> Honda CBR (Regla Conbini)</a></li>
            <li><a href="#japanese"><span class="nav-num">2.3</span> Clases de Japonés 1-a-1</a></li>
            <li><a href="#matrix"><span class="nav-num">2.4</span> Matriz Semanal 168 Horas</a></li>

            <div class="nav-group-label">03 · Universo あやめ &amp; Citas</div>
            <li><a href="#ayame-protocol"><span class="nav-num">3.1</span> Protocolo Clínico &amp; 22:30</a></li>
            <li><a href="#ayame-radar"><span class="nav-num">3.2</span> API Radar Ikebukuro &amp; Japón</a></li>
            <li><a href="#ayame-24-expediciones"><span class="nav-num">3.3</span> 24 Expediciones (8 Regiones)</a></li>
            <li><a href="#ayame-dates"><span class="nav-num">3.4</span> 384 Citas Semanales (2 Años)</a></li>

            <div class="nav-group-label">04 · Campaña MMA 6-0 &amp; Show</div>
            <li><a href="#mma-6-0-roadmap"><span class="nav-num">4.1</span> Ruta Invicta 6-0 &amp; Doble Llave</a></li>
            <li><a href="#walkout-godzilla-mothra"><span class="nav-num">4.2</span> Entrada Godzilla &amp; Mothra</a></li>
            <li><a href="#dojos"><span class="nav-num">4.3</span> Fighter's Flow + Hayato Suzuki</a></li>
            <li><a href="#combat"><span class="nav-num">4.4</span> Equipo YOKKAO &amp; Venum Pro</a></li>

            <div class="nav-group-label">05 · Biología Carnívora &amp; Seúl</div>
            <li><a href="#restaurants"><span class="nav-num">5.1</span> Carnicerías 24h &amp; Steaks</a></li>
            <li><a href="#supplements"><span class="nav-num">5.2</span> Suplementos &amp; Articulaciones</a></li>
            <li><a href="#extremis"><span class="nav-num">5.3</span> Proyecto Extremis (Seúl)</a></li>

            <div class="nav-group-label">06 · Futuro Capitán O-3 Okinawa</div>
            <li><a href="#okinawa-captain"><span class="nav-num">6.1</span> Kadena O-3 &amp; Casa Kanagawa</a></li>
        </ul>

        <div class="sidebar-footer">
            <div class="sidebar-footer-title">Dossiers Complementarios</div>
            <div class="sidebar-ext-grid">
                <a href="plan/" class="sidebar-ext-btn">🇹🇭 Plan</a>
                <a href="campamento/" class="sidebar-ext-btn">🥊 Camp</a>
                <a href="guardarropa/" class="sidebar-ext-btn">👕 Ropa</a>
            </div>
        </div>
    </aside>

    <!-- ==================== MAIN CONTENT ==================== -->
    <main class="main-content">

        <!-- SINGLE-ROW STICKY TOP COMMAND BAR (ZERO OVERLAP) -->
        <header class="top-command-bar">
            <div class="topbar-left">
                <button class="sidebar-toggle-btn" onclick="toggleSidebar()" title="Mostrar / Ocultar Índice Lateral">
                    <span>☰</span>
                    <span>Índice</span>
                </button>

                <nav class="domain-pills-nav" aria-label="Pilares del Imperio">
                    <a href="#domain-1" class="domain-pill active"><span class="pill-num">I</span> Finanzas &amp; Reloj</a>
                    <a href="#domain-2" class="domain-pill"><span class="pill-num">II</span> Hogar &amp; 168H</a>
                    <a href="#domain-3" class="domain-pill"><span class="pill-num">III</span> あやめ &amp; Citas</a>
                    <a href="#domain-4" class="domain-pill"><span class="pill-num">IV</span> MMA 6-0</a>
                    <a href="#domain-5" class="domain-pill"><span class="pill-num">V</span> Carnívoro &amp; Seúl</a>
                    <a href="#domain-6" class="domain-pill"><span class="pill-num">VI</span> Okinawa O-3</a>
                </nav>
            </div>

            <div class="external-dossiers">
                <a href="plan/" class="dossier-chip">🇹🇭 Plan Maestro ↗</a>
                <a href="campamento/" class="dossier-chip">🥊 Campamento ↗</a>
                <a href="guardarropa/" class="dossier-chip">👕 Guardarropa ↗</a>
            </div>
        </header>

        <!-- =====================================================================
             PILAR I: MANDO CENTRAL, RELOJ TÁCTICO & FINANZAS DEL IMPERIO
             ===================================================================== -->
        <div id="domain-1" class="domain-banner" data-kanji="統括">
            <span class="domain-eyebrow">PILAR 01 / 06 • MANDO CENTRAL, CRONÓMETRO JAPÓN &amp; ARQUITECTURA FINANCIERA</span>
            <h2>I. Centro de Mando Ejecutivo, OPEX Mensual &amp; CAPEX Funcional</h2>
            <p>
                Resumen estratégico de tu Imperio en Tokio, relojes regresivos en tiempo real (JST) hacia cada hito clave y presupuestos 100% reales conectados en vivo a la API de divisas (<code>USD / JPY / KRW / THB</code>).
            </p>
            <div class="domain-sublinks">
                <a href="#hero">1.1 KPIs &amp; Reloj Táctico JST</a>
                <a href="#opex">1.2 Presupuesto Mensual (OPEX)</a>
                <a href="#capex">1.3 Equipamiento por Cuarto (CAPEX)</a>
            </div>
        </div>

{sec_hero_upgraded}

{sec_opex}

{sec_capex}

        <!-- =====================================================================
             PILAR II: NUESTRO HOGAR COMPARTIDO, MOVILIDAD & AGENDA 168H
             ===================================================================== -->
        <div id="domain-2" class="domain-banner" data-kanji="日常">
            <span class="domain-eyebrow">PILAR 02 / 06 • CONVIVENCIA CON あやめ, REGLA DEL CONBINI (HONDA CBR) &amp; MATRIZ 168H</span>
            <h2>II. Nuestro Hogar Compartido, Movilidad Táctica &amp; Horario 168 Horas</h2>
            <p>
                Distribución arquitectónica del departamento 2LDK donde vives con <strong>あやめ</strong>, nuestros <strong>2 gatitos y 2 chinchillas</strong>, tu traslado diario en <strong>Honda CBR</strong> sin depender del tren, clases de japonés y la matriz de 168 horas semanales que protege su sueño sagrado a las <strong>22:30 hrs</strong>.
            </p>
            <div class="domain-sublinks">
                <a href="#floor-plan">2.1 Plano 2LDK (Cuarto あやめ + Cuarto Bruno)</a>
                <a href="#motorcycle">2.2 Moto Honda CBR &amp; Tiempos</a>
                <a href="#japanese">2.3 Clases de Japonés</a>
                <a href="#matrix">2.4 Matriz 168H (Lunes a Domingo)</a>
            </div>
        </div>

{sec_floor_plan}

{sec_motorcycle}

{sec_japanese}

{sec_matrix}

        <!-- =====================================================================
             PILAR III: UNIVERSO あやめ — BIENESTAR, RADAR API, 24 EXPEDICIONES & 384 CITAS
             ===================================================================== -->
        <div id="domain-3" class="domain-banner" data-kanji="愛姫">
            <span class="domain-eyebrow">PILAR 03 / 06 • SANTUARIO DE BIENESTAR, API EN VIVO DE IKEBUKURO/JAPÓN &amp; CALENDARIO DE 2 AÑOS</span>
            <h2>III. Universo あやめ: Salud Mental, Radar API en Vivo, 24 Expediciones &amp; 384 Citas</h2>
            <p>
                Todo lo diseñado para cuidar y hacer feliz a <strong>あやめ</strong> en un solo lugar: su seguimiento clínico en Kanda (Dra. Nishimatsu + <em>haco</em>), el <strong>Radar API en vivo de Ikebukuro y Japón</strong>, el <strong>Mapa de Conquista de las 24 Expediciones Nacionales</strong> y las <strong>384 Citas Semanales Únicas</strong> regresando siempre juntos a nuestro hogar.
            </p>
            <div class="domain-sublinks">
                <a href="#ayame-protocol">3.1 Protocolo Clínico &amp; Regla 22:30</a>
                <a href="#ayame-radar">3.2 API Radar Ikebukuro &amp; Japón</a>
                <a href="#ayame-24-expediciones">3.3 24 Expediciones (8 Regiones)</a>
                <a href="#ayame-dates">3.4 384 Citas Semanales (96 Semanas)</a>
            </div>
        </div>

{sec_ayame_protocol}

{sec_ayame_radar}

{sec_ayame_24_expediciones}

{sec_ayame_dates}

        <!-- =====================================================================
             PILAR IV: CAMPAÑA MMA INVICTA (6-0), DOJO & ENTRADA «GODZILLA & MOTHRA»
             ===================================================================== -->
        <div id="domain-4" class="domain-banner" data-kanji="無敗">
            <span class="domain-eyebrow">PILAR 04 / 06 • CIRCUITO JAPONÉS 77 KG, CANDADO DOBLE LLAVE &amp; SHOW DE RETIRO 6-0</span>
            <h2>IV. Campaña MMA Invicta (6-0), Producción «Godzilla &amp; Mothra» &amp; Arsenal</h2>
            <p>
                Tu carrera competitiva completa en Japón: las <strong>6 peleas hacia el retiro invicto (6-0)</strong> protegidas por el candado de Doble Llave con <strong>あやめ</strong>, la producción escénica de 70 segundos (<strong>«Ginza 1954: Godzilla &amp; Mothra 1961»</strong> con el kimono de seda real), tu cuartel general en <strong>FIGHTER'S FLOW</strong> con Hayato Suzuki y tu equipo tricolor <strong>YOKKAO + Venum Pro Boxing</strong>.
            </p>
            <div class="domain-sublinks">
                <a href="#mma-6-0-roadmap">4.1 Ruta Invicta 6-0 &amp; Doble Llave</a>
                <a href="#walkout-godzilla-mothra">4.2 Entrada Godzilla 1954 &amp; Kimono Mothra</a>
                <a href="#dojos">4.3 Fighter's Flow + 1-a-1 Hayato Suzuki</a>
                <a href="#combat">4.4 Shorts YOKKAO &amp; Guantes Venum Pro</a>
            </div>
        </div>

{sec_mma_roadmap}

{sec_walkout_godzilla}

{sec_dojos}

{sec_combat}

        <!-- =====================================================================
             PILAR V: BIOLOGÍA HIPER-CARNÍVORA, SUPLEMENTOS & PROYECTO EXTREMIS
             ===================================================================== -->
        <div id="domain-5" class="domain-banner" data-kanji="肉体">
            <span class="domain-eyebrow">PILAR 05 / 06 • DIETA DE FILETES PUROS (0 ALCOHOL 🚫🍺 / 0 MANGO 🚫🥭), SUPLEMENTOS &amp; CIRUGÍAS SEÚL</span>
            <h2>V. Nutrición Hiper-Carnívora, Suplementación &amp; Proyecto Extremis</h2>
            <p>
                Tu motor biológico para mantener <strong>77 kg fibrosos de pelea</strong>: mapa de carnicerías mayoristas 24h y steakhouses a pasos de casa, protocolo de suplementación articular y el presupuesto médico real de <strong>Proyecto Extremis en Seúl</strong> (VBT/ASC espinal sin fusión, rinoplastia funcional + bichectomía, visión SMILE Pro / LASEK, dental y FUE).
            </p>
            <div class="domain-sublinks">
                <a href="#restaurants">5.1 Carnicerías 24h &amp; Steakhouses</a>
                <a href="#supplements">5.2 Suplementos &amp; Recuperación</a>
                <a href="#extremis">5.3 Proyecto Extremis (Seúl)</a>
            </div>
        </div>

{sec_restaurants}

{sec_supplements}

{sec_extremis}

        <!-- =====================================================================
             PILAR VI: FUTURO IMPERIAL — CAPITÁN O-3 EN OKINAWA & LEGADO FAMILIAR
             ===================================================================== -->
        <div id="domain-6" class="domain-banner" data-kanji="沖縄">
            <span class="domain-eyebrow">PILAR 06 / 06 • TRANSICIÓN POST-SEPTIEMBRE 2029: KADENA AIR BASE &amp; CASA BIFAMILIAR KANAGAWA</span>
            <h2>VI. Operación Okinawa: Fase Capitán (O-3) junto a あやめ &amp; Legado Familiar</h2>
            <p>
                La siguiente etapa tras retirarte invicto (<strong>6-0</strong>) en Tokio: tu servicio como Oficial Capitán en <strong>Kadena Air Base (Okinawa)</strong> viviendo frente al mar turquesa con <strong>あやめ</strong> y nuestros gatitos, y la consolidación de la casa de dos generaciones (<strong>二世帯住宅</strong>) para <strong>千秋-san</strong> en Kanagawa.
            </p>
            <div class="domain-sublinks">
                <a href="#okinawa-captain">6.1 Kadena Air Base (O-3) &amp; Casa Kanagawa</a>
                <a href="plan/">🇹🇭 Ver Plan Maestro de Viajes ↗</a>
                <a href="campamento/">🥊 Ver Dossier de Campamento ↗</a>
            </div>
        </div>

{sec_okinawa_captain}

    </main>

    <a href="#" id="back-to-top" title="Subir al inicio">↑</a>

    <script>
        // Scroll Progress Bar & Active Navigation Highlight
        window.addEventListener('scroll', () => {{
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
            document.getElementById('progress-bar').style.width = scrolled + '%';

            const btt = document.getElementById('back-to-top');
            if (winScroll > 500) {{
                btt.classList.add('visible');
            }} else {{
                btt.classList.remove('visible');
            }}

            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('.nav-links li a');
            let current = '';
            sections.forEach(section => {{
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 140) {{
                    current = section.getAttribute('id');
                }}
            }});

            navLinks.forEach(link => {{
                link.classList.remove('active');
                const href = link.getAttribute('href') || '';
                if (href.startsWith('#') && href.substring(1) === current) {{
                    link.classList.add('active');
                }}
            }});

            // Highlight active Pillar in the top segmented bar
            const domains = document.querySelectorAll('.domain-banner');
            const domainPills = document.querySelectorAll('.domain-pill');
            let currentDomain = 'domain-1';
            domains.forEach(d => {{
                if (pageYOffset >= d.offsetTop - 160) {{
                    currentDomain = d.getAttribute('id');
                }}
            }});
            domainPills.forEach(pill => {{
                pill.classList.toggle('active', pill.getAttribute('href') === '#' + currentDomain);
            }});
        }});

        function toggleSidebar() {{
            if (window.innerWidth <= 1180) {{
                document.body.classList.toggle('sidebar-open');
            }} else {{
                document.body.classList.toggle('sidebar-collapsed');
            }}
        }}

        function toggleRoom(element) {{
            const content = element.nextElementSibling;
            if (content.classList.contains('open')) {{
                content.classList.remove('open');
                content.style.maxHeight = '0';
            }} else {{
                content.classList.add('open');
                content.style.maxHeight = content.scrollHeight + 'px';
            }}
        }}

        function openTab(evt, tabName) {{
            const tabcontent = document.getElementsByClassName("tab-content");
            for (let i = 0; i < tabcontent.length; i++) {{
                tabcontent[i].classList.remove("active");
            }}
            const tablinks = document.getElementsByClassName("tab-btn");
            for (let i = 0; i < tablinks.length; i++) {{
                tablinks[i].classList.remove("active");
            }}
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }}

        function showPlan(planName, btn) {{
            const plans = ['general','ayame','denkoboy','ldk','bathroom','madori'];
            plans.forEach(p => {{
                const el = document.getElementById('plan-' + p);
                if (el) el.style.display = 'none';
            }});
            document.getElementById('plan-' + planName).style.display = 'block';
            document.querySelectorAll('.plan-tab').forEach(t => t.classList.remove('active'));
            btn.classList.add('active');
        }}
    </script>
    <script src="assets/ayame-events-api.js?v=3"></script>
    <script src="assets/citas-ayame.js?v=3"></script>
    <script src="assets/live-prices.js?v=3"></script>
</body>
</html>
"""

    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print(f"[OK] Rebuilt index.html with single-row zero-overlap navbar & executive design ({len(new_html):,} bytes)")


if __name__ == "__main__":
    main()
