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

    # Upgrade #opex with an Interactive SVG Donut Chart + 4 Dataset Modes + Live Piece Inspector
    interactive_opex_widget = """            <div class="opex-interactive-shell" id="opex-explorer">
                <!-- BARRA SUPERIOR DE MODO DE PRESUPUESTO -->
                <div class="opex-toolbar">
                    <div class="opex-toolbar-left">
                        <span class="opex-eyebrow">📊 EXPLORADOR INTERACTIVO DE PRESUPUESTO</span>
                        <span class="opex-hint">Haz clic en cualquier segmento del anillo, tarjeta o fila de la tabla para inspeccionar cada pieza</span>
                    </div>
                    <div class="opex-mode-tabs" role="tablist">
                        <button type="button" class="opex-mode-btn active" data-mode="oro" onclick="setOpexMode('oro')">
                            ⚡ Efectivo Plan Oro (¥736.8K)
                        </button>
                        <button type="button" class="opex-mode-btn" data-mode="suzuki" onclick="setOpexMode('suzuki')">
                            🥊 + 1-a-1 Hayato Suzuki (¥796.8K)
                        </button>
                        <button type="button" class="opex-mode-btn" data-mode="nominal" onclick="setOpexMode('nominal')">
                            📋 Nominal Completo (¥844.3K)
                        </button>
                        <button type="button" class="opex-mode-btn" data-mode="capex" onclick="setOpexMode('capex')">
                            🛋️ CAPEX por Cuarto (¥2.36M)
                        </button>
                    </div>
                </div>

                <!-- CUERPO PRINCIPAL: DONA SVG INTERACTIVA + INSPECTOR DE PIEZA + LISTA SELECCIONABLE -->
                <div class="opex-explorer-grid">
                    <!-- COLUMNA IZQUIERDA: DONA SVG + TARJETA DE DETALLE DE LA PIEZA ACTIVA -->
                    <div class="opex-Stage-col">
                        <div class="opex-svg-wrap">
                            <svg id="opex-donut-svg" viewBox="0 0 260 260" class="opex-donut-svg" aria-label="Gráfico interactivo de presupuesto">
                                <circle cx="130" cy="130" r="96" fill="none" stroke="#181f2c" stroke-width="34"></circle>
                                <g id="opex-svg-slices" transform="rotate(-90 130 130)"></g>
                            </svg>
                            <div class="opex-donut-center" id="opex-donut-center" onclick="selectOpexSlice('all')" title="Clic para volver al total general">
                                <span class="opex-center-tag" id="opex-center-tag">TOTAL MENSUAL</span>
                                <div class="opex-center-jpy" id="opex-center-jpy">¥736,880</div>
                                <div class="opex-center-usd" id="opex-center-usd">~$5,013 USD</div>
                                <span class="opex-center-pct" id="opex-center-pct">100% · 10 Partidas</span>
                            </div>
                        </div>

                        <!-- TARJETA INSPECTORA DE LA PIEZA SELECCIONADA -->
                        <div class="opex-inspector-card" id="opex-inspector-card">
                            <div class="opex-insp-header">
                                <div class="opex-insp-title-wrap">
                                    <span class="opex-insp-dot" id="opex-insp-dot" style="background:#d4a853;"></span>
                                    <h4 id="opex-insp-title">Vista General del Presupuesto</h4>
                                </div>
                                <button type="button" class="opex-reset-btn" id="opex-reset-btn" onclick="selectOpexSlice('all')" style="display:none;">
                                    ↺ Ver Todo (100%)
                                </button>
                            </div>
                            <p class="opex-insp-desc" id="opex-insp-desc">
                                Selecciona cualquier partida a la derecha o directamente en el gráfico circular para desglosar su costo diario, semanal, mensual, anual y qué incluye exactamente.
                            </p>
                            <div class="opex-insp-metrics">
                                <div class="opex-metric-box">
                                    <span class="lbl" id="opex-m1-lbl">Costo Diario</span>
                                    <strong class="val" id="opex-m1-val">¥24,563 / día</strong>
                                    <small class="sub" id="opex-m1-sub">~$167 USD/día</small>
                                </div>
                                <div class="opex-metric-box">
                                    <span class="lbl" id="opex-m2-lbl">Costo Semanal</span>
                                    <strong class="val" id="opex-m2-val">¥170,049 / sem</strong>
                                    <small class="sub" id="opex-m2-sub">~$1,157 USD/sem</small>
                                </div>
                                <div class="opex-metric-box">
                                    <span class="lbl" id="opex-m3-lbl">Impacto Anual</span>
                                    <strong class="val" id="opex-m3-val">¥8,842,560 / año</strong>
                                    <small class="sub" id="opex-m3-sub">~$60,153 USD/año</small>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- COLUMNA DERECHA: SELECTOR INTERACTIVO DE CADA PIEZA DEL PRESUPUESTO -->
                    <div class="opex-slices-list-col">
                        <div class="opex-list-header">
                            <span>Partida del Presupuesto (Clic para inspeccionar)</span>
                            <span>Monto &amp; %</span>
                        </div>
                        <div id="opex-slices-list" class="opex-slices-list"></div>
                    </div>
                </div>
            </div>"""

    sec_opex = re.sub(
        r'<div class="(?:chart-container|opex-interactive-shell)"[\s\S]*?(?=<h4>Desglose Mensual Definitivo</h4>)',
        interactive_opex_widget + "\n\n            ",
        sec_opex,
        count=1,
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

        /* =====================================================================
           INTERACTIVE SVG DONUT & BUDGET PIECE EXPLORER (#opex)
           ===================================================================== */
        .opex-interactive-shell {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.4rem 1.5rem;
            margin-bottom: 1.6rem;
        }}

        .opex-toolbar {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding-bottom: 1rem;
            margin-bottom: 1.25rem;
            border-bottom: 1px solid var(--border);
        }}

        .opex-toolbar-left {{
            display: flex;
            flex-direction: column;
            gap: 2px;
        }}

        .opex-eyebrow {{
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--gold);
            letter-spacing: 0.8px;
            text-transform: uppercase;
        }}

        .opex-hint {{
            font-size: 0.76rem;
            color: var(--text-muted);
        }}

        .opex-mode-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            background: #0b0e14;
            padding: 4px;
            border-radius: 9px;
            border: 1px solid var(--border);
        }}

        .opex-mode-btn {{
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-muted);
            padding: 6px 11px;
            border-radius: 6px;
            font-family: var(--font-body);
            font-size: 0.73rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            white-space: nowrap;
        }}

        .opex-mode-btn:hover {{
            color: #ffffff;
            background: rgba(255, 255, 255, 0.04);
        }}

        .opex-mode-btn.active {{
            background: rgba(212, 168, 83, 0.15);
            border-color: rgba(212, 168, 83, 0.45);
            color: var(--gold);
            font-weight: 700;
        }}

        .opex-explorer-grid {{
            display: grid;
            grid-template-columns: 380px 1fr;
            gap: 1.5rem;
            align-items: start;
        }}

        .opex-Stage-col {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1rem;
        }}

        .opex-svg-wrap {{
            position: relative;
            width: 260px;
            height: 260px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .opex-donut-svg {{
            width: 100%;
            height: 100%;
            overflow: visible;
        }}

        .opex-slice-arc {{
            cursor: pointer;
            transition: stroke-width 0.22s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.22s ease, filter 0.22s ease;
        }}

        .opex-slice-arc:hover {{
            stroke-width: 40px !important;
            filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.25));
        }}

        .opex-donut-center {{
            position: absolute;
            width: 154px;
            height: 154px;
            border-radius: 50%;
            background: radial-gradient(circle at center, #131924 0%, #0c1017 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 12px;
            cursor: pointer;
            box-shadow: inset 0 0 18px rgba(0, 0, 0, 0.6);
            transition: border-color 0.2s;
        }}

        .opex-donut-center:hover {{
            border-color: rgba(212, 168, 83, 0.45);
        }}

        .opex-center-tag {{
            font-size: 0.62rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            color: var(--text-muted);
            max-width: 132px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .opex-center-jpy {{
            font-family: var(--font-mono);
            font-size: 1.22rem;
            font-weight: 800;
            color: #ffffff;
            margin: 3px 0 1px 0;
            line-height: 1.15;
        }}

        .opex-center-usd {{
            font-size: 0.75rem;
            font-weight: 700;
            color: #4ade80;
        }}

        .opex-center-pct {{
            margin-top: 4px;
            font-size: 0.66rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 999px;
            background: rgba(212, 168, 83, 0.14);
            color: var(--gold);
            border: 1px solid rgba(212, 168, 83, 0.3);
        }}

        /* Inspector Card */
        .opex-inspector-card {{
            width: 100%;
            background: #0d1117;
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1rem 1.1rem;
        }}

        .opex-insp-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            margin-bottom: 6px;
        }}

        .opex-insp-title-wrap {{
            display: flex;
            align-items: center;
            gap: 8px;
            min-width: 0;
        }}

        .opex-insp-dot {{
            width: 11px;
            height: 11px;
            border-radius: 3px;
            flex-shrink: 0;
        }}

        .opex-insp-header h4 {{
            font-size: 0.88rem;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            line-height: 1.25;
        }}

        .opex-reset-btn {{
            background: rgba(212, 168, 83, 0.12);
            border: 1px solid rgba(212, 168, 83, 0.35);
            color: var(--gold);
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 0.68rem;
            font-weight: 700;
            cursor: pointer;
            flex-shrink: 0;
        }}

        .opex-reset-btn:hover {{
            background: var(--gold);
            color: #080a0f;
        }}

        .opex-insp-desc {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-bottom: 10px;
            line-height: 1.45;
        }}

        .opex-insp-metrics {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }}

        .opex-metric-box {{
            background: #121721;
            border: 1px solid var(--border);
            border-radius: 7px;
            padding: 7px 8px;
            display: flex;
            flex-direction: column;
        }}

        .opex-metric-box .lbl {{
            font-size: 0.62rem;
            text-transform: uppercase;
            color: var(--text-muted);
            font-weight: 700;
            letter-spacing: 0.4px;
        }}

        .opex-metric-box .val {{
            font-size: 0.78rem;
            color: #ffffff;
            margin-top: 2px;
            font-variant-numeric: tabular-nums;
        }}

        .opex-metric-box .sub {{
            font-size: 0.66rem;
            color: #4ade80;
            font-weight: 600;
        }}

        /* Right-hand Selectable Slices List */
        .opex-slices-list-col {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}

        .opex-list-header {{
            display: flex;
            justify-content: space-between;
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            color: var(--text-muted);
            padding: 0 6px 4px 6px;
        }}

        .opex-slices-list {{
            display: flex;
            flex-direction: column;
            gap: 5px;
        }}

        .opex-slice-row {{
            display: flex;
            flex-direction: column;
            gap: 5px;
            padding: 8px 11px;
            border-radius: 8px;
            background: #0d1117;
            border: 1px solid var(--border);
            cursor: pointer;
            transition: all 0.15s ease;
            text-align: left;
            width: 100%;
            color: var(--text-main);
            font-family: var(--font-body);
        }}

        .opex-slice-row:hover {{
            border-color: rgba(212, 168, 83, 0.45);
            background: #141a26;
        }}

        .opex-slice-row.active {{
            border-color: var(--gold);
            background: rgba(212, 168, 83, 0.10);
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
        }}

        .opex-slice-row.dimmed {{
            opacity: 0.48;
        }}

        .opex-slice-top {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
        }}

        .opex-slice-name {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            color: #ffffff;
        }}

        .opex-slice-swatch {{
            width: 10px;
            height: 10px;
            border-radius: 3px;
            flex-shrink: 0;
        }}

        .opex-slice-figures {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-shrink: 0;
            font-variant-numeric: tabular-nums;
        }}

        .opex-slice-jpy {{
            font-size: 0.82rem;
            font-weight: 700;
            color: #ffffff;
        }}

        .opex-slice-usd {{
            font-size: 0.72rem;
            color: #4ade80;
            font-weight: 600;
        }}

        .opex-slice-pct {{
            font-size: 0.68rem;
            font-weight: 700;
            padding: 1px 6px;
            border-radius: 5px;
            background: rgba(255, 255, 255, 0.06);
            color: var(--gold);
            min-width: 44px;
            text-align: right;
        }}

        .opex-slice-bar-bg {{
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 999px;
            overflow: hidden;
        }}

        .opex-slice-bar-fill {{
            height: 100%;
            border-radius: 999px;
            transition: width 0.35s ease;
        }}

        tr.opex-row-highlighted td {{
            background: rgba(212, 168, 83, 0.14) !important;
        }}

        @media (max-width: 960px) {{
            .opex-explorer-grid {{
                grid-template-columns: 1fr;
            }}
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
            <li><a href="#ayame-24-expediciones"><span class="nav-num">3.3</span> 24 Meses · 47 Prefecturas (全国制覇)</a></li>
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
        // =====================================================================
        // INTERACTIVE SVG DONUT & BUDGET PIECE EXPLORER ENGINE
        // =====================================================================
        const OPEX_DATASETS = {{
            oro: {{
                label: "TOTAL EFECTIVO",
                subtitle: "OPEX Mensual Efectivo (Plan Oro con Free Rent & haco quincenal)",
                isMonthly: true,
                items: [
                    {{ id: "renta", rowIdx: 1, icon: "🏢", name: "1. Renta Urbanex Asakusabashi (Efectivo Free Rent)", short: "Renta Urbanex", jpy: 266580, color: "#d4a853", desc: "Unidad 303 (3LDK) en Urbanex Asakusabashi Front (柳橋1-13-6). Renta nominal ¥289,000 promediada a ¥266,580/mes con Free Rent, 0 Depósito, 0 Reikin e Internet Fibra Gratis." }},
                    {{ id: "diamante", rowIdx: 3, icon: "💜", name: "2. Diamante あやめ (Telas Nippori & Bienestar)", short: "Diamante あやめ", jpy: 200000, color: "#a78bfa", desc: "Fondo mensual sagrado dedicado al bienestar de あやめ, sedas y telas en Nippori/Asakusabashi (incluyendo sus creaciones textiles y gustos personales)." }},
                    {{ id: "carnivora", rowIdx: 2, icon: "🥩", name: "3. Dieta Hiper-Carnívora (Hanamasa 24h & Little Butcher)", short: "Dieta Carnívora", jpy: 95000, color: "#f59e0b", desc: "500–600g diarios de cortes de res Grass-Fed comprados en Niku no Hanamasa 24h (a 3 min) y Little Butcher (a 30m), huevos y arroz. Estrictamente 0 alcohol 🚫🍺 y 0 mango 🚫🥭." }},
                    {{ id: "servicios", rowIdx: 10, icon: "⚡", name: "4. Servicios, 2 Gatos, 2 Chinchillas & NHI", short: "Servicios & Mascotas", jpy: 42000, color: "#38bdf8", desc: "Luz, agua, gas, clima 24/7 e insumos premium para nuestros 2 gatitos y 2 chinchillas, más el Seguro Nacional de Salud (NHI)." }},
                    {{ id: "suscripciones", rowIdx: 9, icon: "📱", name: "5. Suscripciones, IA & eSIM", short: "IA, Cloud & eSIM", jpy: 34500, color: "#60a5fa", desc: "Herramientas de ingeniería de software, IA avanzada (Gemini/Claude), servidores y líneas móviles de alta velocidad en Japón." }},
                    {{ id: "salud_mental", rowIdx: 4, icon: "🌸", name: "6. Salud Mental あやめ (Dra. Nishimatsu + haco)", short: "Salud Mental あやめ", jpy: 27000, color: "#f472b6", desc: "1 consulta/mes con la Dra. Yoshiko Nishimatsu en Ai Clinic Kanda (¥1,500–¥2,000 con NHI) + sesiones quincenales de terapia somática en Counseling Room haco." }},
                    {{ id: "mma", rowIdx: 5, icon: "🥊", name: "7. Gimnasio MMA FIGHTER'S FLOW (Plan Oro)", short: "Fighter's Flow MMA", jpy: 25300, color: "#ef4444", desc: "Membresía Oro ilimitada en FIGHTER'S FLOW (Takadanobaba): MMA, Wrestling, Boxeo, Kickboxing y Sparring rumbo al 6-0 en 77 kg." }},
                    {{ id: "japones", rowIdx: 8, icon: "🇯🇵", name: "8. Clases de Japonés 1-a-1 (JLPT N3/N2)", short: "Clases Japonés", jpy: 25000, color: "#22c55e", desc: "3 sesiones privadas por semana enfocadas en fluidez conversacional con あやめ, su familia (千秋-san) y entrevistas en el ring." }},
                    {{ id: "transporte", rowIdx: 7, icon: "🚆", name: "9. Transporte JR & Metro (Suica 定期券)", short: "Transporte JR/Moto", jpy: 12000, color: "#14b8a6", desc: "Pase Suica para traslados en días de lluvia y salidas a Kanda/Nippori/Ikebukuro complementando tu Honda CBR." }},
                    {{ id: "suplementos", rowIdx: 6, icon: "🧬", name: "10. Suplementos Esenciales & Articulaciones", short: "Suplementos", jpy: 9500, color: "#eab308", desc: "Creatina monohidratada, Omega-3, Vitamina D3+K2, Glicinato de Magnesio, Zinc y electrolitos Pocari Sweat para el corte limpio a 77 kg." }}
                ]
            }},
            suzuki: {{
                label: "CON 1-A-1 SUZUKI",
                subtitle: "OPEX Efectivo + Pack 5 Sesiones Privadas 1-a-1 con Hayato Suzuki",
                isMonthly: true,
                items: [
                    {{ id: "renta", rowIdx: 1, icon: "🏢", name: "1. Renta Urbanex Asakusabashi (Efectivo Free Rent)", short: "Renta Urbanex", jpy: 266580, color: "#d4a853", desc: "Unidad 303 (3LDK) en Urbanex Asakusabashi Front con Free Rent aplicado (¥266,580/mes efectivo)." }},
                    {{ id: "diamante", rowIdx: 3, icon: "💜", name: "2. Diamante あやめ (Telas Nippori & Bienestar)", short: "Diamante あやめ", jpy: 200000, color: "#a78bfa", desc: "Presupuesto mensual íntegro dedicado a la felicidad, telas y bienestar de あやめ." }},
                    {{ id: "carnivora", rowIdx: 2, icon: "🥩", name: "3. Dieta Hiper-Carnívora (Hanamasa 24h & Little Butcher)", short: "Dieta Carnívora", jpy: 95000, color: "#f59e0b", desc: "500–600g/día de filetes Grass-Fed, huevos y arroz. 0 alcohol 🚫🍺, 0 mango 🚫🥭." }},
                    {{ id: "mma", rowIdx: 5, icon: "🥊", name: "4. FIGHTER'S FLOW Oro (¥25.3K) + 5 Clases 1-a-1 Hayato Suzuki (¥60K)", short: "MMA + Hayato Suzuki", jpy: 85300, color: "#ef4444", desc: "Membresía Oro ilimitada + Pack mensual de 5 sesiones privadas 1-a-1 de grappling/MMA con el campeón invicto Hayato Suzuki." }},
                    {{ id: "servicios", rowIdx: 10, icon: "⚡", name: "5. Servicios, 2 Gatos, 2 Chinchillas & NHI", short: "Servicios & Mascotas", jpy: 42000, color: "#38bdf8", desc: "Luz, agua, gas, insumos para nuestros 2 gatitos y 2 chinchillas + Seguro Nacional de Salud." }},
                    {{ id: "suscripciones", rowIdx: 9, icon: "📱", name: "6. Suscripciones, IA & eSIM", short: "IA, Cloud & eSIM", jpy: 34500, color: "#60a5fa", desc: "Stack de desarrollo, IA y conectividad móvil." }},
                    {{ id: "salud_mental", rowIdx: 4, icon: "🌸", name: "7. Salud Mental あやめ (Dra. Nishimatsu + haco)", short: "Salud Mental あやめ", jpy: 27000, color: "#f472b6", desc: "Seguimiento en Ai Clinic Kanda + sesiones quincenales en Counseling Room haco." }},
                    {{ id: "japones", rowIdx: 8, icon: "🇯🇵", name: "8. Clases de Japonés 1-a-1 (JLPT N3/N2)", short: "Clases Japonés", jpy: 25000, color: "#22c55e", desc: "3 sesiones semanales 1-a-1 de japonés." }},
                    {{ id: "transporte", rowIdx: 7, icon: "🚆", name: "9. Transporte JR & Metro (Suica 定期券)", short: "Transporte JR/Moto", jpy: 12000, color: "#14b8a6", desc: "Pase Suica mensual complementario a tu Honda CBR." }},
                    {{ id: "suplementos", rowIdx: 6, icon: "🧬", name: "10. Suplementos Esenciales & Articulaciones", short: "Suplementos", jpy: 9500, color: "#eab308", desc: "Creatina, Omega-3, D3, Magnesio/Zinc y electrolitos." }}
                ]
            }},
            nominal: {{
                label: "NOMINAL COMPLETO",
                subtitle: "OPEX Nominal Mes Completo (Sin Free Rent, haco Semanal + 1-a-1 Suzuki)",
                isMonthly: true,
                items: [
                    {{ id: "renta", rowIdx: 1, icon: "🏢", name: "1. Renta Nominal Urbanex Asakusabashi (303 3LDK)", short: "Renta Nominal", jpy: 289000, color: "#d4a853", desc: "Renta mensual nominal completa en meses posteriores al periodo de Free Rent (incluye 管理費 e internet fibra gratis)." }},
                    {{ id: "diamante", rowIdx: 3, icon: "💜", name: "2. Diamante あやめ (Telas Nippori & Bienestar)", short: "Diamante あやめ", jpy: 200000, color: "#a78bfa", desc: "Presupuesto dedicado a su felicidad, telas de alta costura y tranquilidad." }},
                    {{ id: "carnivora", rowIdx: 2, icon: "🥩", name: "3. Dieta Hiper-Carnívora (Hanamasa 24h & Little Butcher)", short: "Dieta Carnívora", jpy: 95000, color: "#f59e0b", desc: "500–600g/día de cortes de res Grass-Fed, huevos y arroz." }},
                    {{ id: "mma", rowIdx: 5, icon: "🥊", name: "4. FIGHTER'S FLOW Oro + Pack 1-a-1 Hayato Suzuki", short: "MMA + Hayato Suzuki", jpy: 85300, color: "#ef4444", desc: "Plan Miembro Oro (¥25,300) + Pack 5 sesiones privadas 1-a-1 (¥60,000)." }},
                    {{ id: "salud_mental", rowIdx: 4, icon: "🌸", name: "5. Salud Mental あやめ (Fase Inicial Semanal haco)", short: "Salud Mental Semanal", jpy: 52000, color: "#f472b6", desc: "Dra. Nishimatsu en Ai Clinic Kanda + 4 sesiones mensuales (1 por semana) en Counseling Room haco durante la fase inicial." }},
                    {{ id: "servicios", rowIdx: 10, icon: "⚡", name: "6. Servicios, 2 Gatos, 2 Chinchillas & NHI", short: "Servicios & Mascotas", jpy: 42000, color: "#38bdf8", desc: "Suministros eléctricos, gas, agua, mascotas y seguro médico." }},
                    {{ id: "suscripciones", rowIdx: 9, icon: "📱", name: "7. Suscripciones, IA & eSIM", short: "IA, Cloud & eSIM", jpy: 34500, color: "#60a5fa", desc: "Suscripciones de software, IA y telefonía móvil." }},
                    {{ id: "japones", rowIdx: 8, icon: "🇯🇵", name: "8. Clases de Japonés 1-a-1 (JLPT N3/N2)", short: "Clases Japonés", jpy: 25000, color: "#22c55e", desc: "3 sesiones privadas por semana." }},
                    {{ id: "transporte", rowIdx: 7, icon: "🚆", name: "9. Transporte JR & Metro (Suica 定期券)", short: "Transporte JR/Moto", jpy: 12000, color: "#14b8a6", desc: "Pase mensual Suica." }},
                    {{ id: "suplementos", rowIdx: 6, icon: "🧬", name: "10. Suplementos Esenciales & Articulaciones", short: "Suplementos", jpy: 9500, color: "#eab308", desc: "Stack completo de suplementación deportiva." }}
                ]
            }},
            capex: {{
                label: "TOTAL CAPEX CASA",
                subtitle: "Inversión Única de Equipamiento Funcional por Cuarto (Nitori / Amazon.co.jp)",
                isMonthly: false,
                items: [
                    {{ id: "capex_bruno", rowIdx: -1, icon: "💻", name: "1. Cuarto de Bruno: Setup Ingeniería/Stream Intacto + Cama Nitori", short: "Cuarto Bruno & Setup", jpy: 1084140, color: "#d4a853", desc: "Setup completo de Ingeniería y Streaming intacto (¥985,160) + cama Nitori con cajones, colchón Pocket Coil y ropa de cama funcional (¥98,980)." }},
                    {{ id: "capex_ayame", rowIdx: -1, icon: "🌸", name: "2. Cuarto de あやめ: Setup Gaming/Costura Intacto + Recámara Nitori", short: "Cuarto あやめ & Costura", jpy: 699410, color: "#f472b6", desc: "Setup de Gaming y Taller de Costura de あやめ intacto (¥586,440) + cama Nitori, colchón Pocket Coil, tocador con espejo LED y cortinas blackout para dormir a las 22:30 (¥112,970)." }},
                    {{ id: "capex_ldk", rowIdx: -1, icon: "🍳", name: "3. Sala-Comedor-Cocina (LDK) + Electrodomésticos (Refri 282L Hanamasa)", short: "Sala, Cocina & Refri", jpy: 358860, color: "#f59e0b", desc: "Refrigerador Hisense 282L para guardar los filetes de Hanamasa, sofá cama Nitori, mesa de comedor, microondas Sharp, arrocera Tiger y sartenes de hierro fundido Lodge." }},
                    {{ id: "capex_bath", rowIdx: -1, icon: "🧺", name: "4. Lavandería, Baño, Entrada & Limpieza (Lavadora 8kg + Dyson/ Anker)", short: "Lavadora & Baño", jpy: 122790, color: "#38bdf8", desc: "Lavadora automática de 8kg (indispensable para lavar gear de MMA a diario), aspiradora inalámbrica, rack de entrada y báscula inteligente de corte de peso." }},
                    {{ id: "capex_pets", rowIdx: -1, icon: "🐾", name: "5. Santuario para Nuestros 2 Gatitos y 2 Chinchillas", short: "Santuario Mascotas", jpy: 94990, color: "#22c55e", desc: "Jaula de doble piso SANKO Easy Home 80 High para las 2 chinchillas, torre rascador de madera Nitori, areneros cerrados, fuentes de agua y climatización segura." }}
                ]
            }}
        }};

        let currentOpexMode = "oro";
        let currentSelectedSlice = "all";

        function getActiveJpyRate() {{
            const rateCard = document.querySelector("#imperio-live-banner .imperio-live-card .val");
            if (rateCard) {{
                const m = rateCard.textContent.match(/¥([0-9.]+)/);
                if (m) return parseFloat(m[1]);
            }}
            return 147.0;
        }}

        function fmtYen(n) {{
            return "¥" + Math.round(n).toLocaleString("en-US");
        }}

        function fmtUsdVal(jpy) {{
            const rate = getActiveJpyRate();
            return "~$" + Math.round(jpy / rate).toLocaleString("en-US") + " USD";
        }}

        function setOpexMode(mode) {{
            if (!OPEX_DATASETS[mode]) return;
            currentOpexMode = mode;
            currentSelectedSlice = "all";
            document.querySelectorAll(".opex-mode-btn").forEach(btn => {{
                btn.classList.toggle("active", btn.getAttribute("data-mode") === mode);
            }});
            renderOpexExplorer();
        }}

        function selectOpexSlice(sliceId) {{
            if (currentSelectedSlice === sliceId && sliceId !== "all") {{
                currentSelectedSlice = "all";
            }} else {{
                currentSelectedSlice = sliceId;
            }}
            renderOpexExplorer();
        }}

        function renderOpexExplorer() {{
            const ds = OPEX_DATASETS[currentOpexMode];
            const svgGroup = document.getElementById("opex-svg-slices");
            const listContainer = document.getElementById("opex-slices-list");
            if (!svgGroup || !listContainer || !ds) return;

            const totalJpy = ds.items.reduce((acc, it) => acc + it.jpy, 0);
            const r = 96;
            const circumference = 2 * Math.PI * r;
            const gapPx = 2.5;

            svgGroup.innerHTML = "";
            listContainer.innerHTML = "";

            let accumFraction = 0;

            ds.items.forEach((item) => {{
                const frac = item.jpy / totalJpy;
                const pctText = (frac * 100).toFixed(1) + "%";
                const segLength = Math.max(2, frac * circumference - gapPx);
                const dashOffset = -accumFraction * circumference;
                accumFraction += frac;

                const isSelected = currentSelectedSlice === item.id;
                const isDimmed = currentSelectedSlice !== "all" && !isSelected;

                // 1. SVG Donut Arc
                const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                circle.setAttribute("cx", "130");
                circle.setAttribute("cy", "130");
                circle.setAttribute("r", String(r));
                circle.setAttribute("fill", "none");
                circle.setAttribute("stroke", item.color);
                circle.setAttribute("stroke-width", isSelected ? "40" : "32");
                circle.setAttribute("stroke-dasharray", `${{segLength}} ${{circumference}}`);
                circle.setAttribute("stroke-dashoffset", String(dashOffset));
                circle.setAttribute("class", "opex-slice-arc");
                circle.style.opacity = isDimmed ? "0.32" : "1";
                if (isSelected) {{
                    circle.style.filter = `drop-shadow(0 0 10px ${{item.color}}88)`;
                }}
                circle.addEventListener("click", () => selectOpexSlice(item.id));
                svgGroup.appendChild(circle);

                // 2. Right-hand Selector Card
                const rowBtn = document.createElement("button");
                rowBtn.type = "button";
                rowBtn.className = "opex-slice-row" + (isSelected ? " active" : "") + (isDimmed ? " dimmed" : "");
                rowBtn.innerHTML = `
                    <div class="opex-slice-top">
                        <div class="opex-slice-name">
                            <span class="opex-slice-swatch" style="background:${{item.color}};"></span>
                            <span>${{item.icon}} ${{item.name}}</span>
                        </div>
                        <div class="opex-slice-figures">
                            <span class="opex-slice-jpy">${{fmtYen(item.jpy)}}</span>
                            <span class="opex-slice-usd">${{fmtUsdVal(item.jpy)}}</span>
                            <span class="opex-slice-pct">${{pctText}}</span>
                        </div>
                    </div>
                    <div class="opex-slice-bar-bg">
                        <div class="opex-slice-bar-fill" style="width:${{(frac * 100).toFixed(1)}}%; background:${{item.color}};"></div>
                    </div>
                `;
                rowBtn.addEventListener("click", () => selectOpexSlice(item.id));
                listContainer.appendChild(rowBtn);
            }});

            // 3. Update Center HUD & Inspector Card
            const activeItem = ds.items.find(i => i.id === currentSelectedSlice) || null;
            const centerTag = document.getElementById("opex-center-tag");
            const centerJpy = document.getElementById("opex-center-jpy");
            const centerUsd = document.getElementById("opex-center-usd");
            const centerPct = document.getElementById("opex-center-pct");

            const inspDot = document.getElementById("opex-insp-dot");
            const inspTitle = document.getElementById("opex-insp-title");
            const inspDesc = document.getElementById("opex-insp-desc");
            const resetBtn = document.getElementById("opex-reset-btn");

            const m1Lbl = document.getElementById("opex-m1-lbl");
            const m1Val = document.getElementById("opex-m1-val");
            const m1Sub = document.getElementById("opex-m1-sub");
            const m2Lbl = document.getElementById("opex-m2-lbl");
            const m2Val = document.getElementById("opex-m2-val");
            const m2Sub = document.getElementById("opex-m2-sub");
            const m3Lbl = document.getElementById("opex-m3-lbl");
            const m3Val = document.getElementById("opex-m3-val");
            const m3Sub = document.getElementById("opex-m3-sub");

            if (!activeItem) {{
                centerTag.textContent = ds.label;
                centerJpy.textContent = fmtYen(totalJpy);
                centerUsd.textContent = fmtUsdVal(totalJpy);
                centerPct.textContent = `100% · ${{ds.items.length}} Partidas`;

                inspDot.style.background = "#d4a853";
                inspTitle.textContent = ds.subtitle;
                inspDesc.textContent = "Haz clic en cualquier segmento del anillo o en cualquiera de las partidas de la derecha para aislar su peso en el presupuesto y ver su costo diario, semanal y anual.";
                resetBtn.style.display = "none";

                if (ds.isMonthly) {{
                    m1Lbl.textContent = "Costo Diario";
                    m1Val.textContent = fmtYen(totalJpy / 30) + " / día";
                    m1Sub.textContent = fmtUsdVal(totalJpy / 30);

                    m2Lbl.textContent = "Costo Semanal";
                    m2Val.textContent = fmtYen((totalJpy * 12) / 52) + " / sem";
                    m2Sub.textContent = fmtUsdVal((totalJpy * 12) / 52);

                    m3Lbl.textContent = "Total Anual (12m)";
                    m3Val.textContent = fmtYen(totalJpy * 12) + " / año";
                    m3Sub.textContent = fmtUsdVal(totalJpy * 12);
                }} else {{
                    m1Lbl.textContent = "Setups Intactos";
                    m1Val.textContent = "¥1,571,600";
                    m1Sub.textContent = fmtUsdVal(1571600);

                    m2Lbl.textContent = "Muebles & Línea Blanca";
                    m2Val.textContent = "¥788,590";
                    m2Sub.textContent = fmtUsdVal(788590);

                    m3Lbl.textContent = "Amortizado 24 Meses";
                    m3Val.textContent = fmtYen(totalJpy / 24) + " / mes";
                    m3Sub.textContent = fmtUsdVal(totalJpy / 24);
                }}
            }} else {{
                const pct = ((activeItem.jpy / totalJpy) * 100).toFixed(1) + "%";
                centerTag.textContent = activeItem.icon + " " + activeItem.short;
                centerJpy.textContent = fmtYen(activeItem.jpy);
                centerUsd.textContent = fmtUsdVal(activeItem.jpy);
                centerPct.textContent = pct + " del Total";

                inspDot.style.background = activeItem.color;
                inspTitle.textContent = activeItem.icon + " " + activeItem.name;
                inspDesc.textContent = activeItem.desc;
                resetBtn.style.display = "inline-block";

                if (ds.isMonthly) {{
                    m1Lbl.textContent = "Costo Diario";
                    m1Val.textContent = fmtYen(activeItem.jpy / 30) + " / día";
                    m1Sub.textContent = fmtUsdVal(activeItem.jpy / 30);

                    m2Lbl.textContent = "Costo Semanal";
                    m2Val.textContent = fmtYen((activeItem.jpy * 12) / 52) + " / sem";
                    m2Sub.textContent = fmtUsdVal((activeItem.jpy * 12) / 52);

                    m3Lbl.textContent = "Impacto Anual (12m)";
                    m3Val.textContent = fmtYen(activeItem.jpy * 12) + " / año";
                    m3Sub.textContent = fmtUsdVal(activeItem.jpy * 12);
                }} else {{
                    m1Lbl.textContent = "Peso del CAPEX";
                    m1Val.textContent = pct;
                    m1Sub.textContent = "de ¥2,360,190";

                    m2Lbl.textContent = "Inversión en USD";
                    m2Val.textContent = fmtUsdVal(activeItem.jpy);
                    m2Sub.textContent = "Pago único inicial";

                    m3Lbl.textContent = "Costo por Día (2 Años)";
                    m3Val.textContent = fmtYen(activeItem.jpy / 730) + " / día";
                    m3Sub.textContent = fmtUsdVal(activeItem.jpy / 730);
                }}
            }}

            // 4. Sync highlight with the OPEX table rows below
            const opexTable = document.querySelector("#opex table");
            if (opexTable) {{
                const rows = opexTable.querySelectorAll("tr");
                rows.forEach((tr, idx) => {{
                    tr.classList.toggle("opex-row-highlighted", Boolean(activeItem && activeItem.rowIdx === idx));
                }});
            }}
        }}

        document.addEventListener("DOMContentLoaded", () => {{
            // Make OPEX breakdown table rows clickable to select the corresponding slice
            const opexTable = document.querySelector("#opex table");
            if (opexTable) {{
                const rows = opexTable.querySelectorAll("tr");
                rows.forEach((tr, idx) => {{
                    if (idx >= 1 && idx <= 10) {{
                        tr.style.cursor = "pointer";
                        tr.title = "Clic para resaltar esta partida en el gráfico circular";
                        tr.addEventListener("click", () => {{
                            if (currentOpexMode === "capex") currentOpexMode = "oro";
                            const ds = OPEX_DATASETS[currentOpexMode];
                            const found = ds.items.find(it => it.rowIdx === idx);
                            if (found) selectOpexSlice(found.id);
                        }});
                    }}
                }});
            }}
            renderOpexExplorer();
            // Re-render once live FX rates finish loading so USD figures match the live API rate
            setTimeout(renderOpexExplorer, 1200);
        }});

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
    <script src="assets/ayame-events-api.js?v=5"></script>
    <script src="assets/citas-ayame.js?v=5"></script>
    <script src="assets/live-prices.js?v=5"></script>
</body>
</html>
"""

    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print(f"[OK] Rebuilt index.html with Interactive SVG Budget Explorer ({len(new_html):,} bytes)")


if __name__ == "__main__":
    main()
