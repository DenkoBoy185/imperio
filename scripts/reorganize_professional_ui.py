#!/usr/bin/env python3
"""
Reorganizes and upgrades C:\\Users\\Bruno\\.gemini\\antigravity\\scratch\\imperio\\index.html
into a world-class professional 6-Domain Information Architecture & Luxury Executive UI,
grouping all related sections logically while preserving 100% of existing tables, cards, and scripts.
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

    # Extract all existing sections cleanly
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

    # Build the 4 clean, modularized sections from #imperio-mega-documento so each sits in its proper domain!
    countdown_block = """
            <!-- RELOJ TÁCTICO EN TIEMPO REAL (SINCRONIZADO CON HORA DE JAPÓN JST) -->
            <div class="countdown-banner">
              <div class="countdown-banner-header">
                <span>⏱️ RELOJ TÁCTICO EN TIEMPO REAL • SINCRONIZADO CON HORA DE JAPÓN (JST)</span>
                <span class="badge-pill-gold">OBJETIVO INVICTO 6-0 (77 KG) → CAPITÁN O-3 OKINAWA</span>
              </div>
              <div id="imperio-live-countdowns" class="countdown-grid">
                <div class="countdown-card" style="border-top-color:#d29922;">
                  <div class="cd-label" style="color:#fbbf24;">🗾 INICIO OPERACIÓN JAPÓN (OCT 2027)</div>
                  <div id="cd-oct-2027" class="cd-timer">--d --h --m --s</div>
                  <div class="cd-sub">Expedición #1: Ginza Kimono &amp; Base Tokio</div>
                </div>
                <div class="countdown-card" style="border-top-color:#3fb950;">
                  <div class="cd-label" style="color:#4ade80;">🥊 PELEA #1 DEBUT 77 KG (ABR 2028)</div>
                  <div id="cd-apr-2028" class="cd-timer">--d --h --m --s</div>
                  <div class="cd-sub">KROSS×OVER / JMMAF • Inicio del 6-0</div>
                </div>
                <div class="countdown-card" style="border-top-color:#f0b90b;">
                  <div class="cd-label" style="color:#f0b90b;">🦖🦋 6ª PELEA: GODZILLA &amp; MOTHRA (SEP 2029)</div>
                  <div id="cd-sep-2029" class="cd-timer" style="color:#f0b90b;">--d --h --m --s</div>
                  <div class="cd-sub">Retiro Invicto 6-0 + Helicóptero Privado</div>
                </div>
                <div class="countdown-card" style="border-top-color:#58a6ff;">
                  <div class="cd-label" style="color:#60a5fa;">✈️🌺 FASE CAPITÁN O-3 OKINAWA (OCT 2029)</div>
                  <div id="cd-oct-2029" class="cd-timer" style="color:#60a5fa;">--d --h --m --s</div>
                  <div class="cd-sub">Kadena Air Base + Hogar Frente al Mar con あやめ</div>
                </div>
              </div>
            </div>
    """

    # Inject countdown_block inside #hero right after .hero div
    sec_hero_upgraded = sec_hero.replace(
        "</section>",
        countdown_block + "\n        </section>",
    )

    # Dedicated Section: #mma-6-0-roadmap (For Domain IV: MMA 6-0 Campaign)
    sec_mma_roadmap = """        <section id="mma-6-0-roadmap">
            <h2 class="section-title">🥊 Hoja de Ruta Competitiva: La Campaña Invicta (6-0 en 77 kg) &amp; Doble Llave / 6戦無敗計画</h2>
            <p style="color:var(--text-muted); margin-bottom:1.2rem;">
                Estructura táctica diseñada para conquistar <strong>dos coronas de torneo sin obligación de defensa</strong> (<em>DEEP Future King</em> + <em>Campeonato KROSS×OVER / All-Japan</em> = <strong>Doble Campeón 二冠王</strong>) y cerrar con una única <strong>6ª Superpelea Profesional de Retiro</strong> bajo contrato individual (<em>Wan-Matchi Keiyaku</em> / ワンマッチ契約) con entrada teatral completa.
            </p>

            <div class="room-card" style="border-color:rgba(240,185,11,0.4);">
                <div class="room-content open">
                    <table>
                        <thead>
                            <tr>
                                <th>Combate</th>
                                <th>Promoción / Sede Objetivo</th>
                                <th>Fecha</th>
                                <th>Fight Camp (Zona Roja 🔴 6 sem)</th>
                                <th>Estatus / Recompensa Post-Pelea (Zona Verde 🟢)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Pelea #1 (Debut)</strong></td>
                                <td><strong>KROSS×OVER / JMMAF</strong> (Tokio)</td>
                                <td style="color:#58a6ff; font-weight:700;">Abril 2028</td>
                                <td>1 Mar – Abr 2028 (Solo citas en Tokio)</td>
                                <td style="color:#4ade80; font-weight:600;">1-0 • Viaje a Kobe (Wagyu A5), Himeji, Osaka y Okinawa</td>
                            </tr>
                            <tr>
                                <td><strong>Pelea #2</strong></td>
                                <td><strong>Amateur Shooto Regional Kanto</strong></td>
                                <td style="color:#58a6ff; font-weight:700;">Septiembre 2028</td>
                                <td>1 Ago – Sep 2028 (Clima fresco 22°C)</td>
                                <td style="color:#4ade80; font-weight:600;">2-0 • Bahía de Yokohama, Kanazawa (Encargo Kimono Mothra) y Shirakawa-go</td>
                            </tr>
                            <tr>
                                <td><strong>Peleas #3 y #4</strong></td>
                                <td><strong>DEEP Future King Tournament</strong> (2 peleas en 1 noche)</td>
                                <td style="color:#58a6ff; font-weight:700;">Diciembre 2028</td>
                                <td>1 Nov – Dic 2028 (Ryokan en Hakone a 1h)</td>
                                <td style="color:#4ade80; font-weight:600;">4-0 🏆 Campeón #1 • Ruta Completa por Kyushu Norte y Sur (Beppu e Ibusuki)</td>
                            </tr>
                            <tr>
                                <td><strong>Pelea #5</strong></td>
                                <td><strong>Campeonato KROSS×OVER / All-Japan</strong></td>
                                <td style="color:#58a6ff; font-weight:700;">Principios Ago 2029</td>
                                <td>1 Jul – Ago 2029 (Cinco Lagos del Fuji)</td>
                                <td style="color:#4ade80; font-weight:600;">5-0 🏆 Doble Campeón (二冠王) • Pase Directo Estelar</td>
                            </tr>
                            <tr style="background:rgba(240,185,11,0.10);">
                                <td style="color:#f0b90b; font-weight:800;">Pelea #6 (El Retiro)</td>
                                <td><strong>DEEP TOKYO IMPACT / KROSS×OVER CAGE</strong><br><small style="color:var(--text-muted);">(Shinjuku FACE o Korakuen Hall)</small></td>
                                <td style="color:#f0b90b; font-weight:800;">Finales Ago / Sep 2029</td>
                                <td>Mantenimiento continuo post-Pelea #5</td>
                                <td style="color:#f0b90b; font-weight:800;">6-0 👑 Contrato de 1 Pelea (ワンマッチ契約), Entrada Godzilla &amp; Mothra y Retiro en Helicóptero</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="grid-cards" style="grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); margin-top:1rem;">
                        <div class="item-card" style="border-left:4px solid #f85149;">
                            <h4 style="color:#f85149;">🔐 Protocolo «Doble Llave» Antirretadores</h4>
                            <p style="font-size:0.88rem; margin-top:0.4rem;">
                                Ningún reto del público o promotor puede aceptarse en caliente. Todo combate requiere la firma unánime de: <strong>1) El Entrenador en Jefe</strong> (evaluación física y táctica) y <strong>2) La Mánager あやめ</strong> (protección de viajes, salud e ingreso limpio a la Fuerza Aérea). Al terminar la 6ª pelea, los títulos se dejan vacantes en el centro del ring invicto (<strong>6-0</strong>).
                            </p>
                        </div>
                        <div class="item-card" style="border-left:4px solid #38bdf8;">
                            <h4 style="color:#38bdf8;">🏍️ Logística Diaria: La Regla del «Conbini»</h4>
                            <p style="font-size:0.88rem; margin-top:0.4rem;">
                                Siguiendo el consejo estratégico de <strong>あやめ</strong> de no depender del tren todos los días para ir a entrenar, el traslado desde nuestro hogar hacia el gimnasio (<em>FIGHTER'S FLOW</em>) se realiza en tu motocicleta deportiva <strong>Honda CBR</strong>. En el gimnasio y en el calentamiento de vestidor utilizas el conjunto tricolor (azul rey, rojo y blanco) de <strong>Shorts YOKKAO</strong> y <strong>Guantes Venum Pro Boxing</strong>.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

    # Dedicated Section: #walkout-godzilla-mothra (For Domain IV: MMA 6-0 Campaign)
    sec_walkout_godzilla = """        <section id="walkout-godzilla-mothra">
            <h2 class="section-title">🦖🦋 Producción Escénica de la 6ª Pelea: «La Caída de Ginza 1954 &amp; El Vuelo de Mothra 1961» (70 Segundos) / 最終戦入場演出</h2>
            <p style="color:var(--text-muted); margin-bottom:1.2rem;">
                Entrada relámpago de <strong>70 segundos</strong> diseñada para no enfriar el cuerpo antes del combate, sin infringir derechos de Toho (homenaje original sin logotipos registrados y rugido con ajuste de <em>pitch</em> para evitar bloqueos de Content ID en YouTube).
            </p>

            <div class="grid-cards" style="grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); margin-bottom:1.5rem;">
                <div class="item-card" style="border-top:4px solid #9ca3af;">
                    <span style="color:#9ca3af; font-size:0.75rem; font-weight:800; letter-spacing:1px;">EL GUERRERO • ESTÉTICA MONOCROMÁTICA 1954</span>
                    <h3 style="color:#fff; margin:6px 0 10px;">🦖 Bata de Combate «ShodaiGoji 1954»</h3>
                    <ul style="font-size:0.88rem; padding-left:18px; color:var(--text-main);">
                        <li style="margin-bottom:6px;"><strong>Textura y Corte:</strong> Tela pesada en negro ceniza y gris grafito mate con relieve tipo roca volcánica (adquirida en Nippori), manga tres cuartos estilo <em>haori</em> y capucha profunda.</li>
                        <li style="margin-bottom:6px;"><strong>Placas Dorsales Incandescentes:</strong> Tres hileras de aletas dorsales en espuma EVA ultraligera forradas en gris carbón en la base con las puntas y bordes en <strong>blanco hueso incandescente</strong> (el brillo original en blanco y negro de 1954).</li>
                        <li><strong>Efecto en Pasarela:</strong> Bajo reflectores blancos a contraluz y neblina de piso, la figura se ve literalmente salida de una cinta de 1954.</li>
                    </ul>
                </div>

                <div class="item-card" style="border-top:4px solid #f0b90b;">
                    <span style="color:#f0b90b; font-size:0.75rem; font-weight:800; letter-spacing:1px;">LA MÁNAGER • EL ÚNICO DESTELLO DE COLOR SAGRADO</span>
                    <h3 style="color:#fff; margin:6px 0 10px;">🦋 Kimono de Seda a Medida «Mothra 1961» para あやめ</h3>
                    <ul style="font-size:0.88rem; padding-left:18px; color:var(--text-main);">
                        <li style="margin-bottom:6px;"><strong>Las Alas en las Mangas:</strong> Seda 100% pura en marfil y amarillo dorado que se degrada en las mangas hacia naranja tostado, rojo terracota y líneas asimétricas en negro terciopelo. Al levantar los brazos para quitarte la bata en la escalera del ring, las mangas se despliegan como las alas de Mothra.</li>
                        <li style="margin-bottom:6px;"><strong>Cuello y Ojos Celestes:</strong> Cuello interior (<em>han-eri</em>) blanco suave y <em>obi</em> negro profundo con broche central (<em>obidome</em>) de <strong>turquesa o jade azul celeste</strong>.</li>
                        <li style="margin-bottom:6px;"><strong>Tocado Funcional (Kanzashi):</strong> Dos plumas curvas de filigrana en latón bañado en oro mate con cabujones de turquesa en la base (&lt;25 g), unidas a una sola peineta oculta de seguridad anti-enganches.</li>
                        <li><strong>Corte de Esquina:</strong> Confección oculta en dos piezas (<em>nibushiki</em>) para ponerse en 3 minutos y subir las escaleras de la jaula con total seguridad.</li>
                    </ul>
                </div>
            </div>

            <div class="room-card" style="margin-bottom:1.5rem;">
                <div class="room-header" onclick="toggleRoom(this)">
                    <div class="room-title">💎 Presupuesto de Sastrería Real en Japón — Kimono «Mothra 1961» (3 a 5 Meses de Confección)</div>
                    <div class="room-subtotal">¥320,000 – ¥940,000 JPY</div>
                </div>
                <div class="room-content open">
                    <table>
                        <thead>
                            <tr>
                                <th>Componente Artesanal</th>
                                <th>Opción A: Atelier de Diseño en Tokio (Teñido de Estudio)</th>
                                <th>Opción B: Maestro Kaga Yuzen en Kanazawa (Pintado a Mano)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Rollo de Seda Pura (<em>Tango Chirimen</em>) + Diseño de Alas</td>
                                <td>¥150,000 – ¥250,000 JPY (~$1,000 – $1,650 USD)</td>
                                <td>¥350,000 – ¥600,000 JPY (~$2,300 – $4,000 USD)</td>
                            </tr>
                            <tr>
                                <td>Sastrería a Mano (<em>Wasaishi</em>) y Corte Funcional de Esquina</td>
                                <td>¥65,000 – ¥90,000 JPY (~$430 – $600 USD)</td>
                                <td>¥80,000 – ¥110,000 JPY (~$530 – $730 USD)</td>
                            </tr>
                            <tr>
                                <td><em>Obi</em> Negro + Cuello Blanco + Broche Turquesa</td>
                                <td>¥75,000 – ¥110,000 JPY (~$500 – $730 USD)</td>
                                <td>¥100,000 – ¥160,000 JPY (~$660 – $1,050 USD)</td>
                            </tr>
                            <tr>
                                <td>Tocado Doble en Latón Bañado en Oro y Turquesas</td>
                                <td>¥30,000 – ¥45,000 JPY (~$200 – $300 USD)</td>
                                <td>¥45,000 – ¥70,000 JPY (~$300 – $460 USD)</td>
                            </tr>
                            <tr style="background:rgba(46,160,67,0.12); font-weight:bold; color:#4ade80;">
                                <td>INVERSIÓN TOTAL ESTIMADA</td>
                                <td>¥320,000 – ¥495,000 JPY (~$2,130 – $3,280 USD)</td>
                                <td>¥575,000 – ¥940,000 JPY (~$3,790 – $6,240 USD)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="item-card" style="border-left:4px solid var(--gold); background:rgba(212,168,83,0.05);">
                <h4 style="color:var(--gold); margin-bottom:0.6rem;">⏱️ Guion Técnico en Arena: «Ginza 1954 en 70 Segundos»</h4>
                <ol style="font-size:0.9rem; padding-left:20px; color:var(--text-main);">
                    <li style="margin-bottom:8px;"><strong>0:00 – 0:15 (Intro en MP3 + Luz Blanca):</strong> Oscuridad total en la arena con reflectores blancos y humo bajo. El audio pregrabado reproduce las campanadas reales de la Torre del Reloj de Ginza Wako, el reporte de emergencia de radio de 1954 (<em>«¡Godzilla ha aparecido en Ginza 4-Chome!»</em>) y el rugido metálico original.</li>
                    <li style="margin-bottom:8px;"><strong>0:15 – 0:50 (1 Tambor Taiko en Vivo + Efecto Dominó):</strong> Un percusionista de <em>Wadaiko</em> junto a la cortina golpea el tambor marcando tus pasos pesados mientras suena tu tema de entrada. Avanzas a paso firme con la bata de 1954 y 4 bailarines apostados en el pasillo caen hacia atrás como fichas de dominó a tu paso, simulando el derrumbe de Ginza sin ensuciar la lona.</li>
                    <li><strong>0:50 – 1:10 (El Destape en la Escalera):</strong> Llegas caliente a los escalones de la jaula. <strong>あやめ</strong> sube detrás de ti, abre las mangas aladas de Mothra al quitarte la bata de los hombros frente a las cámaras, y entras directo a ganar tu última pelea (<strong>6-0</strong>).</li>
                </ol>
            </div>
        </section>"""

    # Extract the 24 Expeditions grid & tracker from raw
    grid_match = re.search(
        r'(<!-- MAPA DE PROGRESO Y FILTROS DE LAS 8 REGIONES -->.*?</div>\s*</div>\s*)<!-- ================= MÓDULO 4',
        raw,
        re.DOTALL,
    )
    if not grid_match:
        raise ValueError("Could not extract 24 expeditions grid!")
    expeditions_inner = grid_match.group(1)

    sec_ayame_24_expediciones = f"""        <section id="ayame-24-expediciones">
            <h2 class="section-title">🗾 Mapa Nacional: Las 24 Expediciones Mensuales con あやめ (Oct 2027 – Sep 2029) / 全国24遠征マップ</h2>
            <p style="color:var(--text-muted); margin-bottom:1.2rem;">
                Recorrido táctico por más de <strong>30 prefecturas en las 8 regiones de Japón</strong> junto a <strong>あやめ</strong> (1 gran expedición por cada mes durante 2 años), sincronizado con el <strong>Sistema Semáforo de tus 6 Peleas</strong> para que jamás choque con tu corte a 77 kg ni con su descanso sagrado de las <strong>22:30 hrs</strong>.
            </p>
            {expeditions_inner}
        </section>"""

    # Dedicated Section: #okinawa-captain (For Domain VI: Future Captain O-3 in Okinawa)
    sec_okinawa_captain = """        <section id="okinawa-captain">
            <h2 class="section-title">✈️🌺 Operación Okinawa (Post-Septiembre 2029): Nueva Vida como Capitán (O-3) junto a あやめ &amp; Casa Kanagawa / 沖縄大尉フェーズ</h2>
            <p style="color:var(--text-muted); margin-bottom:1.2rem;">
                Tras colgar los guantes invicto (<strong>6-0</strong>) y sin lesiones en septiembre de 2029, inicia tu servicio como <strong>Oficial Capitán (O-3) en Kadena Air Base (Okinawa)</strong>, brindándole a <strong>あやめ</strong> el entorno costero ideal dentro de su propio país junto a nuestros 2 gatitos y 2 chinchillas, mientras consolidan el patrimonio familiar para <strong>千秋-san</strong>.
            </p>

            <div class="grid-cards" style="grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));">
                <div class="item-card" style="border-top:4px solid #38bdf8;">
                    <h4 style="color:#38bdf8; margin-bottom:8px;">🏡 Residencia Frente al Mar con Subsidio OHA</h4>
                    <p style="font-size:0.88rem; color:var(--text-main);">
                        Casa amplia o <em>penthouse</em> frente al océano en <strong>Chatan (Mihama)</strong> o <strong>Yomitan</strong> (explorados juntos en la Expedición #9 de junio 2028), con cuarto de costura con vista al mar turquesa para <strong>あやめ</strong> y terrazas soleadas seguras para nuestros gatitos y chinchillas.
                    </p>
                </div>

                <div class="item-card" style="border-top:4px solid #4ade80;">
                    <h4 style="color:#4ade80; margin-bottom:8px;">🌊 Paz Mental y Cero Choque Cultural</h4>
                    <p style="font-size:0.88rem; color:var(--text-main);">
                        <strong>あやめ</strong> sigue viviendo en Japón con su idioma, su sistema médico, su gastronomía, brisa marina diaria (<em>Uchinaa Time</em>) sin el estrés de los trenes llenos, y a un vuelo doméstico directo de su mamá (<strong>千秋-san</strong>) y sus amigas en Tokio/Kanagawa.
                    </p>
                </div>

                <div class="item-card" style="border-top:4px solid #f0b90b;">
                    <h4 style="color:#f0b90b; margin-bottom:8px;">🎨 Arte Textil Ryukyu Bingata &amp; Movilidad</h4>
                    <p style="font-size:0.88rem; color:var(--text-main);">
                        Acceso directo a los talleres tradicionales del teñido imperial de Okinawa (<em>Ryukyu Bingata</em> y <em>Bashofu</em>) para sus creaciones textiles, con movilidad total en auto familiar climatizado más tu motocicleta deportiva <strong>Honda CBR</strong>.
                    </p>
                </div>

                <div class="item-card" style="border-top:4px solid #f472b6;">
                    <h4 style="color:#f472b6; margin-bottom:8px;">🏠 Legado Familiar: Casa Bifamiliar (二世帯住宅) en Kanagawa</h4>
                    <p style="font-size:0.88rem; color:var(--text-main);">
                        Con el fondo de ahorro mensual acumulado en Tokio más los beneficios de Oficial O-3 (OHA/BAH y VA Loan), queda respaldado el proyecto de la casa de dos generaciones (<strong>二世帯住宅</strong>) en Kanagawa para garantizar la tranquilidad vitalicia de <strong>千秋-san</strong>.
                    </p>
                </div>
            </div>
        </section>"""

    # Build the new professional HTML document
    new_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👑 ATLAS DEL IMPERIO: Bruno & あやめ (2027–2029+) / 帝国の地図</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@500;700;900&family=Noto+Serif+JP:wght@500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #07090e;
            --bg-surface: #0d1117;
            --bg-card: #131822;
            --bg-card-hover: #1a2130;
            --gold: #d4a853;
            --amber: #f0b90b;
            --sakura: #f472b6;
            --crimson: #f85149;
            --emerald: #3fb950;
            --cyan: #38bdf8;
            --purple: #a78bfa;
            --text-main: #e6edf3;
            --text-muted: #8b949e;
            --border: #262c36;
            --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-head: 'Orbitron', sans-serif;
            --font-jp: 'Noto Serif JP', serif;
            --accent-gradient: linear-gradient(135deg, #d4a853, #f0b90b);
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
            background-image:
                radial-gradient(circle at 15% 5%, rgba(212, 168, 83, 0.06), transparent 35%),
                radial-gradient(circle at 85% 25%, rgba(244, 114, 182, 0.05), transparent 35%),
                radial-gradient(circle at 50% 80%, rgba(56, 189, 248, 0.04), transparent 40%);
            color: var(--text-main);
            line-height: 1.65;
            display: flex;
            overflow-x: hidden;
        }}

        /* Top Scroll Progress Bar */
        #progress-bar {{
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--gold), var(--sakura), var(--cyan));
            z-index: 10000;
            width: 0%;
            transition: width 0.1s;
        }}

        /* Professional Grouped Sidebar */
        .sidebar {{
            width: 280px;
            background: rgba(13, 17, 23, 0.96);
            backdrop-filter: blur(16px);
            height: 100vh;
            position: fixed;
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            z-index: 1000;
            transition: transform 0.3s ease;
        }}

        .sidebar-header {{
            padding: 1.4rem 1.2rem;
            border-bottom: 1px solid var(--border);
            background: linear-gradient(180deg, rgba(212,168,83,0.10), transparent);
            text-align: center;
        }}

        .sidebar-header h1 {{
            font-family: var(--font-head);
            font-size: 1.02rem;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 1.8px;
            line-height: 1.35;
        }}

        .sidebar-sub {{
            font-size: 0.72rem;
            color: var(--text-muted);
            margin-top: 4px;
            display: block;
        }}

        .nav-links {{
            list-style: none;
            padding: 0.6rem 0 1.5rem 0;
            overflow-y: auto;
            flex-grow: 1;
        }}

        .nav-links::-webkit-scrollbar {{
            width: 5px;
        }}
        .nav-links::-webkit-scrollbar-thumb {{
            background: #262c36;
            border-radius: 4px;
        }}

        .nav-group-label {{
            font-size: 0.66rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: #6e7681;
            padding: 0.9rem 1.2rem 0.3rem 1.2rem;
            border-top: 1px solid rgba(255,255,255,0.04);
            margin-top: 0.3rem;
        }}
        .nav-group-label:first-child {{
            border-top: none;
            margin-top: 0;
        }}

        .nav-links li a {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 0.52rem 1.2rem;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.8rem;
            font-weight: 500;
            transition: all 0.2s ease;
            border-left: 3px solid transparent;
        }}

        .nav-links li a:hover, .nav-links li a.active {{
            color: #ffffff;
            background: rgba(212, 168, 83, 0.10);
            border-left-color: var(--gold);
            font-weight: 600;
        }}

        /* Main Content Area */
        .main-content {{
            margin-left: 280px;
            padding: 0 3.2rem 4rem 3.2rem;
            width: calc(100% - 280px);
            max-width: 1520px;
        }}

        /* Sticky Top Executive Command Bar */
        .top-command-bar {{
            position: sticky;
            top: 0;
            z-index: 900;
            background: rgba(7, 9, 14, 0.88);
            backdrop-filter: blur(14px);
            border-bottom: 1px solid var(--border);
            margin: 0 -3.2rem 2.2rem -3.2rem;
            padding: 0.7rem 3.2rem;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            justify-content: space-between;
        }}

        .domain-pills-nav {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}

        .domain-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-decoration: none;
            background: rgba(255,255,255,0.04);
            border: 1px solid var(--border);
            color: var(--text-muted);
            transition: all 0.2s ease;
        }}

        .domain-pill:hover {{
            color: #fff;
            border-color: var(--gold);
            background: rgba(212, 168, 83, 0.12);
            text-decoration: none;
        }}

        .external-dossiers {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }}

        /* Master Domain Hero Divider Banners */
        .domain-banner {{
            position: relative;
            overflow: hidden;
            border-radius: 16px;
            padding: 26px 28px;
            margin: 3.2rem 0 1.8rem 0;
            border: 1px solid var(--border);
            background: linear-gradient(135deg, rgba(19, 24, 34, 0.95), rgba(13, 17, 23, 0.98));
            box-shadow: 0 14px 34px rgba(0, 0, 0, 0.45);
        }}

        .domain-banner:first-of-type {{
            margin-top: 0.5rem;
        }}

        .domain-banner::after {{
            content: attr(data-kanji);
            position: absolute;
            right: 24px;
            bottom: -10px;
            font-family: var(--font-jp);
            font-size: 5.2rem;
            font-weight: 700;
            color: rgba(255, 255, 255, 0.03);
            pointer-events: none;
            user-select: none;
        }}

        .domain-eyebrow {{
            display: inline-block;
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1.4px;
            padding: 4px 12px;
            border-radius: 999px;
            margin-bottom: 10px;
        }}

        .domain-banner h2 {{
            font-family: var(--font-head);
            font-size: 1.55rem;
            color: #ffffff;
            margin-bottom: 6px;
            letter-spacing: 0.5px;
        }}

        .domain-banner p {{
            color: var(--text-muted);
            font-size: 0.92rem;
            max-width: 920px;
            margin-bottom: 14px;
        }}

        .domain-sublinks {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .domain-sublinks a {{
            font-size: 0.76rem;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 8px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.12);
            color: var(--text-main);
            text-decoration: none;
            transition: all 0.2s;
        }}

        .domain-sublinks a:hover {{
            border-color: var(--gold);
            color: var(--gold);
            background: rgba(212,168,83,0.1);
        }}

        /* Section Styling */
        section {{
            margin-bottom: 2.8rem;
            scroll-margin-top: 80px;
        }}

        h2.section-title {{
            font-family: var(--font-head);
            font-size: 1.35rem;
            color: var(--gold);
            margin-bottom: 1.2rem;
            padding-bottom: 0.6rem;
            border-bottom: 1px solid var(--border);
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }}

        h3 {{
            font-family: var(--font-head);
            color: var(--text-main);
            margin-top: 1.2rem;
            margin-bottom: 0.8rem;
            font-size: 1.05rem;
        }}

        /* Hero & Countdown Banner */
        .hero-subtitle {{
            text-align: center;
            color: var(--gold);
            font-size: 1.15rem;
            margin-bottom: 1.8rem;
            letter-spacing: 2px;
            font-weight: 600;
        }}

        .hero {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(195px, 1fr));
            gap: 1.1rem;
            margin-bottom: 1.8rem;
        }}

        .stat-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.25rem 1rem;
            text-align: center;
            transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
        }}

        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.45);
            border-color: var(--gold);
        }}

        .stat-value {{
            font-family: var(--font-head);
            font-size: 1.65rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.35rem;
        }}

        .stat-label {{
            font-size: 0.78rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }}

        .countdown-banner {{
            background: linear-gradient(135deg, rgba(240,185,11,0.10), rgba(244,114,182,0.07));
            border: 1px solid rgba(240,185,11,0.38);
            border-radius: 14px;
            padding: 18px 20px;
            margin-top: 0.5rem;
        }}

        .countdown-banner-header {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--amber);
            letter-spacing: 1px;
        }}

        .badge-pill-gold {{
            background: rgba(240,185,11,0.18);
            border: 1px solid var(--amber);
            color: #fde68a;
            padding: 3px 10px;
            border-radius: 999px;
            font-size: 0.7rem;
        }}

        .countdown-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 12px;
        }}

        .countdown-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-top: 3px solid var(--gold);
            border-radius: 10px;
            padding: 12px 14px;
            text-align: center;
        }}

        .cd-label {{
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}

        .cd-timer {{
            font-family: 'Orbitron', monospace;
            font-size: 1.2rem;
            font-weight: 800;
            color: #ffffff;
            margin: 6px 0;
        }}

        .cd-sub {{
            font-size: 0.72rem;
            color: var(--text-muted);
        }}

        /* Floor Plan */
        .floor-plan-img {{
            max-height: 75vh;
            width: auto;
            max-width: 100%;
            border-radius: 12px;
            border: 1px solid var(--border);
            box-shadow: 0 15px 35px rgba(0,0,0,0.65);
            display: block;
            margin: 0 auto 2rem auto;
            transition: transform 0.3s;
        }}
        .floor-plan-img:hover {{
            transform: scale(1.015);
            border-color: var(--gold);
        }}

        .plan-tab {{
            padding: 8px 14px;
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-family: var(--font-body);
            font-size: 0.8rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .plan-tab:hover {{
            border-color: var(--gold);
            color: var(--text-main);
        }}
        .plan-tab.active {{
            background: var(--gold);
            color: #07090e;
            border-color: var(--gold);
            font-weight: 700;
        }}

        /* Cards & Accordions */
        .room-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            margin-bottom: 1.25rem;
            overflow: hidden;
            box-shadow: 0 6px 18px rgba(0,0,0,0.28);
        }}

        .room-header {{
            padding: 1.15rem 1.4rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255,255,255,0.02);
            transition: background 0.25s;
        }}

        .room-header:hover {{
            background: rgba(255,255,255,0.05);
        }}

        .room-title {{
            font-family: var(--font-head);
            font-size: 0.98rem;
            color: var(--amber);
        }}

        .room-subtotal {{
            font-weight: 700;
            color: var(--text-main);
            font-size: 0.9rem;
        }}

        .room-content {{
            padding: 0 1.4rem;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease-out, padding 0.4s ease;
        }}

        .room-content.open {{
            padding: 1.3rem 1.4rem;
            max-height: 6000px;
            overflow: auto;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
            font-size: 0.84rem;
        }}

        th, td {{
            padding: 0.75rem 0.85rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }}

        th {{
            font-family: var(--font-head);
            font-size: 0.75rem;
            color: var(--gold);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            background: rgba(0,0,0,0.35);
            position: sticky;
            top: 0;
        }}

        tr:hover td {{
            background: rgba(255,255,255,0.025);
        }}

        a {{
            color: var(--gold);
            text-decoration: none;
            transition: color 0.2s;
        }}

        a:hover {{
            color: var(--amber);
            text-decoration: underline;
        }}

        .btn-link {{
            display: inline-block;
            background: rgba(212, 168, 83, 0.14);
            border: 1px solid var(--gold);
            color: var(--gold);
            padding: 0.28rem 0.65rem;
            border-radius: 6px;
            font-size: 0.78rem;
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
            grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
            gap: 1.25rem;
        }}

        .item-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.35rem;
            position: relative;
            transition: border-color 0.25s, transform 0.25s;
        }}

        .item-card:hover {{
            border-color: rgba(212, 168, 83, 0.55);
        }}

        .item-card h4 {{
            font-family: var(--font-head);
            color: var(--gold);
            margin-bottom: 0.5rem;
            font-size: 0.98rem;
        }}

        .item-card .price {{
            font-family: var(--font-head);
            font-size: 1.15rem;
            color: var(--text-main);
            margin: 0.8rem 0;
            font-weight: 700;
        }}

        .badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: var(--accent-gradient);
            color: var(--bg-base);
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            font-size: 0.7rem;
            font-weight: 800;
            font-family: var(--font-head);
        }}

        /* OPEX Donut */
        .opex-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 2.5rem;
            align-items: center;
        }}

        .donut-chart-container {{
            flex: 1;
            min-width: 280px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .donut-chart {{
            width: 240px;
            height: 240px;
            border-radius: 50%;
            background: conic-gradient(
                #4CAF50 0% 36.4%,
                #FF9800 36.4% 49.3%,
                #F44336 49.3% 76.5%,
                #9C27B0 76.5% 84.4%,
                #2196F3 84.4% 89.8%,
                #00BCD4 89.8% 95.3%,
                #E91E63 95.3% 98.0%,
                #607D8B 98.0% 100%
            );
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 24px rgba(0,0,0,0.5);
        }}

        .donut-hole {{
            width: 155px;
            height: 155px;
            background-color: var(--bg-base);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 10px;
        }}

        .opex-table-container {{
            flex: 2;
            min-width: 320px;
        }}

        /* Tabs for 168h Matrix */
        .tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.2rem;
        }}

        .tab-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.7rem 1.2rem;
            cursor: pointer;
            font-family: var(--font-head);
            font-size: 0.78rem;
            border-radius: 8px;
            transition: all 0.25s;
        }}

        .tab-btn.active, .tab-btn:hover {{
            background: rgba(212, 168, 83, 0.14);
            color: var(--gold);
            border-color: var(--gold);
        }}

        .tab-content {{
            display: none;
            animation: fadeIn 0.35s;
        }}

        .tab-content.active {{
            display: block;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        #back-to-top {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--bg-card);
            border: 1px solid var(--gold);
            color: var(--gold);
            width: 46px;
            height: 46px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            text-decoration: none;
            font-size: 1.3rem;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s;
            z-index: 999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
        }}

        #back-to-top.visible {{
            opacity: 1;
            pointer-events: auto;
        }}

        #back-to-top:hover {{
            background: var(--gold);
            color: var(--bg-base);
        }}

        .mobile-toggle {{
            display: none;
            position: fixed;
            top: 0.85rem;
            left: 0.85rem;
            z-index: 1001;
            background: var(--bg-card);
            border: 1px solid var(--gold);
            color: var(--gold);
            padding: 0.45rem 0.75rem;
            border-radius: 6px;
            cursor: pointer;
            font-family: var(--font-head);
            font-size: 0.78rem;
        }}

        @media (max-width: 1024px) {{
            .sidebar {{
                transform: translateX(-100%);
            }}
            .sidebar.open {{
                transform: translateX(0);
            }}
            .main-content {{
                margin-left: 0;
                width: 100%;
                padding: 0 1.4rem 3rem 1.4rem;
            }}
            .top-command-bar {{
                margin: 0 -1.4rem 1.5rem -1.4rem;
                padding: 0.7rem 1.4rem 0.7rem 5.5rem;
            }}
            .mobile-toggle {{
                display: block;
            }}
        }}
    </style>
</head>
<body>

    <div id="progress-bar"></div>

    <button class="mobile-toggle" onclick="toggleSidebar()">☰ IMPERIO</button>

    <!-- ==================== GROUPED PROFESSIONAL SIDEBAR ==================== -->
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <h1>👑 ATLAS DEL IMPERIO</h1>
            <span class="sidebar-sub">帝国の地図 • Bruno &amp; あやめ (6-0 → O-3)</span>
        </div>
        <ul class="nav-links">
            <div class="nav-group-label">I. Mando Central &amp; Finanzas</div>
            <li><a href="#hero">👑 Panel Ejecutivo &amp; Reloj JST</a></li>
            <li><a href="#opex">💴 Presupuesto Mensual (OPEX)</a></li>
            <li><a href="#capex">🛋️ Capital &amp; Muebles (CAPEX)</a></li>

            <div class="nav-group-label">II. Nuestro Hogar, Moto &amp; 168H</div>
            <li><a href="#floor-plan">🏡 Hogar 2LDK con あやめ</a></li>
            <li><a href="#motorcycle">🏍️ Honda CBR (Regla Conbini)</a></li>
            <li><a href="#japanese">🇯🇵 Clases de Japonés 1-a-1</a></li>
            <li><a href="#matrix">⏱️ Matriz Semanal 168 Horas</a></li>

            <div class="nav-group-label" style="color:#f472b6;">III. Universo あやめ &amp; Citas</div>
            <li><a href="#ayame-protocol" style="color:#f9a8d4;">🌸 Protocolo Clínico &amp; 22:30</a></li>
            <li><a href="#ayame-radar" style="color:#7dd3fc;">🛰️ API Radar Ikebukuro &amp; Japón</a></li>
            <li><a href="#ayame-24-expediciones" style="color:#fde68a;">🗾 24 Expediciones (8 Regiones)</a></li>
            <li><a href="#ayame-dates" style="color:#f472b6;">💕 384 Citas Semanales (2 Años)</a></li>

            <div class="nav-group-label" style="color:#f0b90b;">IV. Campaña MMA 6-0 &amp; Show</div>
            <li><a href="#mma-6-0-roadmap" style="color:#fcd34d;">🥊 Ruta Invicta 6-0 &amp; Doble Llave</a></li>
            <li><a href="#walkout-godzilla-mothra" style="color:#fb923c;">🦖🦋 Entrada Godzilla &amp; Mothra</a></li>
            <li><a href="#dojos">🦅 Fighter's Flow + Hayato Suzuki</a></li>
            <li><a href="#combat">🥊 Equipo YOKKAO &amp; Venum Pro</a></li>

            <div class="nav-group-label" style="color:#4ade80;">V. Biología Carnívora &amp; Extremis</div>
            <li><a href="#restaurants">🥩 Carnicerías 24h &amp; Steaks</a></li>
            <li><a href="#supplements">💊 Suplementos &amp; Articulaciones</a></li>
            <li><a href="#extremis">🧬 Proyecto Extremis (Seúl)</a></li>

            <div class="nav-group-label" style="color:#38bdf8;">VI. Futuro Capitán O-3 Okinawa</div>
            <li><a href="#okinawa-captain" style="color:#60a5fa;">✈️🌺 Kadena O-3 &amp; Casa Kanagawa</a></li>

            <div class="nav-group-label">Dossiers Especializados</div>
            <li><a href="plan/" style="color:#22c55e;font-weight:700;">🇹🇭 Plan Maestro Tailandia/Seúl ↗</a></li>
            <li><a href="campamento/" style="color:#f59e0b;font-weight:700;">🥊 Dossier de Campamento ↗</a></li>
            <li><a href="guardarropa/" style="color:#ef4444;font-weight:700;">👕 Guardarropa Imperio ↗</a></li>
        </ul>
    </aside>

    <!-- ==================== MAIN CONTENT ==================== -->
    <main class="main-content">

        <!-- STICKY TOP COMMAND BAR -->
        <div class="top-command-bar">
            <div class="domain-pills-nav">
                <a href="#domain-1" class="domain-pill">👑 I. Mando &amp; Finanzas</a>
                <a href="#domain-2" class="domain-pill">🏡 II. Hogar, CBR &amp; 168H</a>
                <a href="#domain-3" class="domain-pill" style="border-color:rgba(244,114,182,0.4); color:#f9a8d4;">🌸 III. Universo あやめ &amp; Citas</a>
                <a href="#domain-4" class="domain-pill" style="border-color:rgba(240,185,11,0.4); color:#fde68a;">🥊 IV. MMA 6-0 &amp; Godzilla/Mothra</a>
                <a href="#domain-5" class="domain-pill" style="border-color:rgba(74,222,128,0.4); color:#86efac;">🥩 V. Dieta Carnívora &amp; Extremis</a>
                <a href="#domain-6" class="domain-pill" style="border-color:rgba(56,189,248,0.4); color:#7dd3fc;">✈️ VI. Capitán Okinawa O-3</a>
            </div>
            <div class="external-dossiers">
                <a href="plan/" class="btn-link" style="border-color:#22c55e; color:#4ade80;">🇹🇭 Plan Maestro</a>
                <a href="campamento/" class="btn-link" style="border-color:#f59e0b; color:#fbbf24;">🥊 Campamento</a>
                <a href="guardarropa/" class="btn-link" style="border-color:#ef4444; color:#f87171;">👕 Guardarropa</a>
            </div>
        </div>

        <!-- =====================================================================
             PILAR I: MANDO CENTRAL, RELOJ TÁCTICO & FINANZAS DEL IMPERIO
             ===================================================================== -->
        <div id="domain-1" class="domain-banner" data-kanji="統括" style="border-left: 5px solid var(--gold);">
            <span class="domain-eyebrow" style="background:rgba(212,168,83,0.16); color:var(--gold); border:1px solid rgba(212,168,83,0.4);">
                PILAR I • MANDO CENTRAL, CRONÓMETRO JAPÓN &amp; ARQUITECTURA FINANCIERA
            </span>
            <h2>👑 I. Centro de Mando Ejecutivo, OPEX Mensual &amp; CAPEX Funcional</h2>
            <p>
                Resumen estratégico de tu Imperio en Tokio, relojes regresivos en tiempo real (JST) hacia cada hito clave y presupuestos 100% reales conectados en vivo a la API de divisas (<code>USD / JPY / KRW / THB</code>).
            </p>
            <div class="domain-sublinks">
                <a href="#hero">📊 KPIs &amp; Reloj Táctico JST</a>
                <a href="#opex">💴 Presupuesto Mensual (OPEX)</a>
                <a href="#capex">🛋️ Equipamiento por Cuarto (CAPEX)</a>
            </div>
        </div>

{sec_hero_upgraded}

{sec_opex}

{sec_capex}

        <!-- =====================================================================
             PILAR II: NUESTRO HOGAR COMPARTIDO, MOVILIDAD & AGENDA 168H
             ===================================================================== -->
        <div id="domain-2" class="domain-banner" data-kanji="日常" style="border-left: 5px solid #a78bfa;">
            <span class="domain-eyebrow" style="background:rgba(167,139,250,0.16); color:#c4b5fd; border:1px solid rgba(167,139,250,0.4);">
                PILAR II • CONVIVENCIA CON あやめ, REGLA DEL CONBINI (HONDA CBR) &amp; MATRIZ 168H
            </span>
            <h2>🏡 II. Nuestro Hogar Compartido, Movilidad Táctica &amp; Horario 168 Horas</h2>
            <p>
                Distribución arquitectónica del departamento 2LDK donde vives con <strong>あやめ</strong>, nuestros <strong>2 gatitos y 2 chinchillas</strong>, tu traslado diario en <strong>Honda CBR</strong> sin depender del tren, clases de japonés y la matriz de 168 horas semanales que protege su sueño sagrado a las <strong>22:30 hrs</strong>.
            </p>
            <div class="domain-sublinks">
                <a href="#floor-plan">📐 Plano 2LDK (Cuarto あやめ + Cuarto Bruno)</a>
                <a href="#motorcycle">🏍️ Moto Honda CBR &amp; Tiempos</a>
                <a href="#japanese">🇯🇵 Clases de Japonés</a>
                <a href="#matrix">🗓️ Matriz 168H (Lunes a Domingo)</a>
            </div>
        </div>

{sec_floor_plan}

{sec_motorcycle}

{sec_japanese}

{sec_matrix}

        <!-- =====================================================================
             PILAR III: UNIVERSO あやめ — BIENESTAR, RADAR API, 24 EXPEDICIONES & 384 CITAS
             ===================================================================== -->
        <div id="domain-3" class="domain-banner" data-kanji="愛姫" style="border-left: 5px solid var(--sakura);">
            <span class="domain-eyebrow" style="background:rgba(244,114,182,0.16); color:#f9a8d4; border:1px solid rgba(244,114,182,0.45);">
                PILAR III • SANTUARIO DE BIENESTAR, API EN VIVO DE IKEBUKURO/JAPÓN &amp; CALENDARIO DE 2 AÑOS
            </span>
            <h2>🌸 III. Universo あやめ: Salud Mental, Radar API en Vivo, 24 Expediciones &amp; 384 Citas</h2>
            <p>
                Todo lo diseñado para cuidar y hacer feliz a <strong>あやめ</strong> en un solo lugar: su seguimiento clínico en Kanda (Dra. Nishimatsu + <em>haco</em>), el <strong>Radar API en vivo de Ikebukuro y Japón</strong>, el <strong>Mapa de Conquista de las 24 Expediciones Nacionales</strong> y las <strong>384 Citas Semanales Únicas</strong> regresando siempre juntos a nuestro hogar.
            </p>
            <div class="domain-sublinks">
                <a href="#ayame-protocol">🩺 Protocolo Clínico &amp; Regla 22:30</a>
                <a href="#ayame-radar">🛰️ API Radar Ikebukuro &amp; Japón</a>
                <a href="#ayame-24-expediciones">🗾 24 Expediciones (8 Regiones)</a>
                <a href="#ayame-dates">💕 384 Citas Semanales (96 Semanas)</a>
            </div>
        </div>

{sec_ayame_protocol}

{sec_ayame_radar}

{sec_ayame_24_expediciones}

{sec_ayame_dates}

        <!-- =====================================================================
             PILAR IV: CAMPAÑA MMA INVICTA (6-0), DOJO & ENTRADA «GODZILLA & MOTHRA»
             ===================================================================== -->
        <div id="domain-4" class="domain-banner" data-kanji="無敗" style="border-left: 5px solid var(--crimson);">
            <span class="domain-eyebrow" style="background:rgba(248,81,73,0.16); color:#fca5a5; border:1px solid rgba(248,81,73,0.45);">
                PILAR IV • CIRCUITO JAPONÉS 77 KG, CANDADO DOBLE LLAVE &amp; SHOW DE RETIRO 6-0
            </span>
            <h2>🥊 IV. Campaña MMA Invicta (6-0), Producción «Godzilla &amp; Mothra» &amp; Arsenal</h2>
            <p>
                Tu carrera competitiva completa en Japón: las <strong>6 peleas hacia el retiro invicto (6-0)</strong> protegidas por el candado de Doble Llave con <strong>あやめ</strong>, la producción escénica de 70 segundos (<strong>«Ginza 1954: Godzilla &amp; Mothra 1961»</strong> con el kimono de seda real), tu cuartel general en <strong>FIGHTER'S FLOW</strong> con Hayato Suzuki y tu equipo tricolor <strong>YOKKAO + Venum Pro Boxing</strong>.
            </p>
            <div class="domain-sublinks">
                <a href="#mma-6-0-roadmap">🏆 Ruta Invicta 6-0 &amp; Doble Llave</a>
                <a href="#walkout-godzilla-mothra">🦖🦋 Entrada Godzilla 1954 &amp; Kimono Mothra</a>
                <a href="#dojos">🦅 Fighter's Flow + 1-a-1 Hayato Suzuki</a>
                <a href="#combat">🥊 Shorts YOKKAO &amp; Guantes Venum Pro</a>
            </div>
        </div>

{sec_mma_roadmap}

{sec_walkout_godzilla}

{sec_dojos}

{sec_combat}

        <!-- =====================================================================
             PILAR V: BIOLOGÍA HIPER-CARNÍVORA, SUPLEMENTOS & PROYECTO EXTREMIS
             ===================================================================== -->
        <div id="domain-5" class="domain-banner" data-kanji="肉体" style="border-left: 5px solid var(--emerald);">
            <span class="domain-eyebrow" style="background:rgba(63,185,80,0.16); color:#86efac; border:1px solid rgba(63,185,80,0.45);">
                PILAR V • DIETA DE FILETES PUROS (0 ALCOHOL 🚫🍺 / 0 MANGO 🚫🥭), SUPLEMENTOS &amp; CIRUGÍAS SEÚL
            </span>
            <h2>🥩 V. Nutrición Hiper-Carnívora, Suplementación &amp; Proyecto Extremis</h2>
            <p>
                Tu motor biológico para mantener <strong>77 kg fibrosos de pelea</strong>: mapa de carnicerías mayoristas 24h y steakhouses a pasos de casa, protocolo de suplementación articular y el presupuesto médico real de <strong>Proyecto Extremis en Seúl</strong> (VBT/ASC espinal sin fusión, rinoplastia funcional + bichectomía, visión SMILE Pro / LASEK, dental y FUE).
            </p>
            <div class="domain-sublinks">
                <a href="#restaurants">🥩 Carnicerías 24h &amp; Steakhouses</a>
                <a href="#supplements">💊 Suplementos &amp; Recuperación</a>
                <a href="#extremis">🧬 Proyecto Extremis (Seúl)</a>
            </div>
        </div>

{sec_restaurants}

{sec_supplements}

{sec_extremis}

        <!-- =====================================================================
             PILAR VI: FUTURO IMPERIAL — CAPITÁN O-3 EN OKINAWA & LEGADO FAMILIAR
             ===================================================================== -->
        <div id="domain-6" class="domain-banner" data-kanji="沖縄" style="border-left: 5px solid var(--cyan);">
            <span class="domain-eyebrow" style="background:rgba(56,189,248,0.16); color:#7dd3fc; border:1px solid rgba(56,189,248,0.45);">
                PILAR VI • TRANSICIÓN POST-SEPTIEMBRE 2029: KADENA AIR BASE &amp; CASA BIFAMILIAR KANAGAWA
            </span>
            <h2>✈️🌺 VI. Operación Okinawa: Fase Capitán (O-3) junto a あやめ &amp; Legado Familiar</h2>
            <p>
                La siguiente etapa tras retirarte invicto (<strong>6-0</strong>) en Tokio: tu servicio como Oficial Capitán en <strong>Kadena Air Base (Okinawa)</strong> viviendo frente al mar turquesa con <strong>あやめ</strong> y nuestros gatitos, y la consolidación de la casa de dos generaciones (<strong>二世帯住宅</strong>) para <strong>千秋-san</strong> en Kanagawa.
            </p>
            <div class="domain-sublinks">
                <a href="#okinawa-captain">✈️🌺 Kadena Air Base (O-3) &amp; Casa Kanagawa</a>
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
                if (pageYOffset >= sectionTop - 130) {{
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
        }});

        function toggleSidebar() {{
            document.getElementById('sidebar').classList.toggle('open');
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
    <script src="assets/ayame-events-api.js?v=2"></script>
    <script src="assets/citas-ayame.js?v=2"></script>
    <script src="assets/live-prices.js?v=2"></script>
</body>
</html>
"""

    INDEX_FILE.write_text(new_html, encoding="utf-8")
    print(f"[OK] Reorganized index.html into 6 Thematic Master Domains ({len(new_html):,} bytes)")


if __name__ == "__main__":
    main()
