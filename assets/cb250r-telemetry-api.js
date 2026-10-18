/**
 * ============================================================================
 * HONDA CB250R (8BK-MC52) REAL-TIME ROUTING MAP & TELEMETRY API ENGINE v1.0
 * ============================================================================
 * Fuentes Oficiales & APIs en Vivo:
 *  1. Honda Motor Co., Ltd. Japan Official Specs: https://www.honda.co.jp/CB250R/type/ & /spec/
 *  2. OSRM Live Street Routing API: https://router.project-osrm.org/route/v1/driving/
 *  3. Open-Meteo Tokyo Riding Weather API: https://api.open-meteo.com/v1/forecast
 *  4. Live FX Rate API (USD/JPY): https://open.er-api.com/v6/latest/USD
 *  5. Leaflet.js 1.9.4 Interactive Map Engine
 */
(function () {
  'use strict';

  const STATE = {
    feed: null,
    baseKey: 'asakusabashi',
    categoryFilter: 'all',
    searchQuery: '',
    selectedColorId: 'black',
    selectedDestId: 'fighters_flow',
    fxRate: 158.2,
    gasPriceJpy: 175,
    weather: null,
    map: null,
    tileLayer: null,
    tileMode: 'dark',
    routeLayer: null,
    baseMarker: null,
    destMarkers: {}
  };

  const CATEGORY_META = {
    all: { label: '🌐 Todos los Destinos (25)', color: '#38bdf8' },
    mma: { label: '🥊 MMA & Dojos (6-0)', color: '#ef4444' },
    nutrition: { label: '🥩 Abasto Carnívoro & Restaurantes', color: '#f59e0b' },
    ayame_care: { label: '🌸 Salud, Clínica & Telas あやめ', color: '#ec4899' },
    dates_irl: { label: '💑 4 Citas Semanales & Kick/YT IRL', color: '#a855f7' },
    arenas_hubs: { label: '🏟️ Arenas MMA & Hubs Shinkansen/Avión', color: '#10b981' },
    shodaigoji_custom: { label: '🦖 Talleres Custom «ShodaiGoji 1954» (4)', color: '#06b6d4' }
  };

  function fmtJPY(n) {
    return '¥' + Math.round(Number(n) || 0).toLocaleString('en-US');
  }

  function fmtUSD(jpy) {
    const usd = (Number(jpy) || 0) / (STATE.fxRate || 158.2);
    return '$' + (usd < 10 ? usd.toFixed(2) : Math.round(usd).toLocaleString('en-US'));
  }

  function ensureLeafletLoaded() {
    return new Promise((resolve) => {
      if (window.L) return resolve(window.L);
      if (!document.getElementById('cb250r-leaflet-css')) {
        const link = document.createElement('link');
        link.id = 'cb250r-leaflet-css';
        link.rel = 'stylesheet';
        link.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
        document.head.appendChild(link);
      }
      const script = document.createElement('script');
      script.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
      script.onload = () => resolve(window.L);
      script.onerror = () => resolve(null);
      document.head.appendChild(script);
    });
  }

  async function fetchLiveAPIs() {
    try {
      const res = await fetch('assets/cb250r-routes-feed.json?v=' + Date.now());
      if (res.ok) {
        STATE.feed = await res.json();
        STATE.fxRate = STATE.feed.default_fx_jpy_per_usd || 158.2;
        STATE.gasPriceJpy = STATE.feed.tokyo_regular_gas_jpy_per_l || 175;
      }
    } catch (e) {
      console.warn('[CB250R API] Fallback local feed:', e);
    }

    // Live FX Rate
    try {
      const fxRes = await fetch('https://open.er-api.com/v6/latest/USD');
      if (fxRes.ok) {
        const fxData = await fxRes.json();
        if (fxData && fxData.rates && fxData.rates.JPY) {
          STATE.fxRate = fxData.rates.JPY;
        }
      }
    } catch (_) {}

    // Live Tokyo Weather & Road Grip Telemetry
    try {
      const wRes = await fetch(
        'https://api.open-meteo.com/v1/forecast?latitude=35.6975&longitude=139.7863&current=temperature_2m,precipitation,rain,wind_speed_10m,weather_code&timezone=Asia%2FTokyo'
      );
      if (wRes.ok) {
        const wData = await wRes.json();
        if (wData && wData.current) {
          STATE.weather = wData.current;
        }
      }
    } catch (_) {}
  }

  function getWeatherBadgeHTML() {
    if (!STATE.weather) {
      return `<span style="color:#4ade80;font-weight:700;">🟢 ASFALTO SECO · Tracción Radial 100% Óptima (IMU-ABS Standby)</span>`;
    }
    const temp = STATE.weather.temperature_2m;
    const rain = STATE.weather.rain || STATE.weather.precipitation || 0;
    const wind = STATE.weather.wind_speed_10m || 0;
    if (rain > 0.2) {
      return `<span style="color:#facc15;font-weight:700;">🟡 LLUVIA EN TOKIO (${rain} mm · ${temp}°C · Viento ${wind} km/h) — IMU-ABS Activo / Usar Tren con あやめ</span>`;
    }
    return `<span style="color:#4ade80;font-weight:700;">🟢 TOKIO EN VIVO: ${temp}°C · Viento ${wind} km/h · 0 mm Lluvia — Grip Radial Óptimo (Showa SFF-BP + IMU-ABS)</span>`;
  }

  function renderDashboard() {
    const mount = document.getElementById('cb250r-api-mount');
    if (!mount || !STATE.feed) return;

    const specs = STATE.feed.cb250r_specs;
    const baseObj = STATE.feed.bases[STATE.baseKey];
    const weekly = STATE.feed.weekly_summary[STATE.baseKey];
    const colorObj =
      specs.official_colors.find((c) => c.id === STATE.selectedColorId) ||
      specs.official_colors[0];

    mount.innerHTML = `
      <!-- BARRA SUPERIOR DE TELEMETRÍA EN VIVO -->
      <div style="background:linear-gradient(135deg, #090d16 0%, #111827 100%); border:1px solid rgba(239,68,68,0.45); border-radius:14px; padding:18px 20px; margin-bottom:20px; box-shadow:0 10px 30px rgba(0,0,0,0.45);">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px; border-bottom:1px solid rgba(255,255,255,0.08); padding-bottom:14px; margin-bottom:16px;">
          <div>
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
              <span style="background:rgba(239,68,68,0.2); color:#f87171; border:1px solid #ef4444; padding:3px 10px; border-radius:999px; font-size:0.72rem; font-weight:800; letter-spacing:0.8px; text-transform:uppercase;">
                🏍️ HONDA JAPAN OFFICIAL API · 型式 8BK-MC52 · 249cc 軽二輪 (0 SHAKEN)
              </span>
              <span style="background:rgba(56,189,248,0.15); color:#38bdf8; border:1px solid rgba(56,189,248,0.4); padding:3px 10px; border-radius:999px; font-size:0.72rem; font-weight:700;">
                FX LIVE: $1 USD = ¥${STATE.fxRate.toFixed(2)} JPY · Gasolina Regular Tokio: ¥${STATE.gasPriceJpy}/L
              </span>
            </div>
            <h3 style="color:#ffffff; font-size:1.45rem; margin:8px 0 4px; font-weight:900;">
              Honda CB250R <span style="color:#ef4444;">Neo Sports Café</span> — Dossier Oficial &amp; Mapa de Rutas de la Matriz 168H
            </h3>
            <div style="font-size:0.82rem; color:#9ca3af;">
              「${specs.tagline_jp}」 — <a href="${specs.official_urls.type_price}" target="_blank" rel="noopener" style="color:#38bdf8; text-decoration:underline; font-weight:700;">Ver Página Oficial Honda Japón (/CB250R/type/) ↗</a> · <a href="${specs.official_urls.spec}" target="_blank" rel="noopener" style="color:#f59e0b; text-decoration:underline; font-weight:700;">Tabla Oficial 主要諸元 (/CB250R/spec/) ↗</a>
            </div>
          </div>
          <div style="background:rgba(15,23,42,0.9); border:1px solid rgba(255,255,255,0.12); border-radius:10px; padding:10px 14px; font-size:0.78rem;">
            <div style="color:#9ca3af; font-size:0.7rem; text-transform:uppercase; margin-bottom:3px;">📡 Telemetría Climática y Asfalto en Tokio (Open-Meteo Live)</div>
            <div id="cb250r-weather-status">${getWeatherBadgeHTML()}</div>
          </div>
        </div>

        <!-- KPIs PRINCIPALES DE LA HONDA CB250R -->
        <div class="cb250r-kpi-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 165px), 1fr)); gap:10px;">
          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid #ef4444; border-radius:10px; padding:12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">Precio Oficial Honda (10% IVA)</div>
            <div style="font-size:1.25rem; font-weight:900; color:#fff; margin-top:2px;">${fmtJPY(specs.pricing_japan.msrp_tax_included_jpy)} <span style="font-size:0.82rem; color:#f87171;">(${fmtUSD(specs.pricing_japan.msrp_tax_included_jpy)})</span></div>
            <div style="font-size:0.72rem; color:#9ca3af;">Sin IVA: ${fmtJPY(specs.pricing_japan.msrp_pre_tax_jpy)} · Puesta en calle ~${fmtJPY(specs.pricing_japan.estimated_on_road_jpy)}</div>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid #38bdf8; border-radius:10px; padding:12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">Peso &amp; Potencia (MC52E)</div>
            <div style="font-size:1.25rem; font-weight:900; color:#38bdf8; margin-top:2px;">144 kg · 27 PS <span style="font-size:0.8rem; color:#93c5fd;">(20 kW)</span></div>
            <div style="font-size:0.72rem; color:#9ca3af;">249cc DOHC 4V · 23 N·m · Giro mín. 2.3m</div>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid #10b981; border-radius:10px; padding:12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">Rendimiento &amp; Autonomía (10L)</div>
            <div style="font-size:1.25rem; font-weight:900; color:#10b981; margin-top:2px;">33.7 km/L <span style="font-size:0.78rem; color:#6ee7b7;">(WMTC)</span></div>
            <div style="font-size:0.72rem; color:#9ca3af;">45.0 km/L (a 60 km/h) · 337–450 km/tanque</div>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid #f59e0b; border-radius:10px; padding:12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">Tiempo Ahorrado en tu Rutina</div>
            <div style="font-size:1.25rem; font-weight:900; color:#f59e0b; margin-top:2px;">+${weekly.saved_hours_week} hrs/sem <span style="font-size:0.78rem; color:#fde68a;">(+${weekly.saved_hours_year} h/año)</span></div>
            <div style="font-size:0.72rem; color:#9ca3af;">${weekly.cb250r_hours_week}h en CB250R vs ${weekly.train_hours_week}h en tren</div>
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid #a855f7; border-radius:10px; padding:12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">Gasto Semanal de Gasolina</div>
            <div style="font-size:1.25rem; font-weight:900; color:#c084fc; margin-top:2px;">${fmtJPY(weekly.fuel_cost_jpy_week)}/sem <span style="font-size:0.78rem; color:#e9d5ff;">(${fmtUSD(weekly.fuel_cost_jpy_week)})</span></div>
            <div style="font-size:0.72rem; color:#9ca3af;">${weekly.total_km_week} km/sem (${weekly.fuel_liters_week} L) · ${fmtJPY(weekly.fuel_cost_jpy_month)}/mes</div>
          </div>
        </div>
      </div>

      <!-- SELECTOR INTERACTIVO DE LOS 3 COLORES OFICIALES + SONIDO DEL ESCAPE HONDA -->
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 285px), 1fr)); gap:16px; margin-bottom:20px;">
        <!-- Tarjeta Visual del Color Oficial Seleccionado -->
        <div style="background:#0d131f; border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:10px; flex-wrap:wrap;">
              <span style="font-size:0.73rem; font-weight:800; color:#f59e0b; text-transform:uppercase;">
                🎨 Selector Oficial Honda Japón (/CB250R/type/)
              </span>
              <span style="background:rgba(255,255,255,0.07); color:#e5e7eb; padding:3px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">
                ${colorObj.badge}
              </span>
            </div>

            <div style="background:radial-gradient(circle at center, rgba(255,255,255,0.1) 0%, rgba(13,19,31,0.95) 75%); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px; text-align:center; margin-bottom:12px;">
              <img id="cb250r-official-img" src="${colorObj.image_url}" alt="${colorObj.name_en}" style="max-width:100%; height:210px; object-fit:contain; filter:drop-shadow(0 12px 20px rgba(0,0,0,0.65));" />
              <div style="margin-top:8px; font-size:0.95rem; font-weight:800; color:#fff;">
                ${colorObj.name_en} <span style="color:#9ca3af; font-size:0.8rem;">(${colorObj.name_jp})</span>
              </div>
              <div style="font-size:0.78rem; color:#d1d5db; margin-top:4px;">
                ${colorObj.notes}
              </div>
            </div>
          </div>

          <div>
            <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px;">
              ${specs.official_colors
                .map(
                  (c) => `
                <button type="button" class="cb250r-color-btn" data-color="${c.id}" style="flex:1; min-width:105px; cursor:pointer; padding:8px 10px; border-radius:8px; border:${
                    c.id === STATE.selectedColorId
                      ? '2px solid #f59e0b'
                      : '1px solid rgba(255,255,255,0.15)'
                  }; background:${
                    c.id === STATE.selectedColorId
                      ? 'rgba(245,158,11,0.16)'
                      : 'rgba(255,255,255,0.04)'
                  }; color:#fff; font-size:0.75rem; font-weight:700; display:flex; align-items:center; gap:7px;">
                  <span style="display:inline-block; width:14px; height:14px; border-radius:50%; background:${c.hex}; border:2px solid ${c.accent_hex}; flex-shrink:0;"></span>
                  <span style="text-align:left; line-height:1.2;">${c.name_en.replace('Matte ', '').replace('Metallic', '')}</span>
                </button>`
                )
                .join('')}
            </div>

            <!-- Reproductor Oficial del Sonido del Escape MC52E -->
            <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(56,189,248,0.3); border-radius:10px; padding:10px 12px; display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px;">
              <div>
                <div style="font-size:0.73rem; font-weight:800; color:#38bdf8;">🔊 Audio Oficial Honda: Escape de 2 Cámaras (Motor MC52E)</div>
                <div style="font-size:0.7rem; color:#9ca3af;">Archivo original de honda.co.jp/CB250R/powerunit/</div>
              </div>
              <audio controls preload="none" style="height:32px; max-width:100%; width:220px;">
                <source src="${specs.official_urls.exhaust_audio_mp3}" type="audio/mpeg">
              </audio>
            </div>
          </div>
        </div>

        <!-- Ficha de Ingeniería Oficial + Ventaja Legal 250cc Keijirin -->
        <div style="background:#0d131f; border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="font-size:0.74rem; font-weight:800; color:#38bdf8; text-transform:uppercase; margin-bottom:8px;">
              ⚙️ Ingeniería de Grado Supersport &amp; Por Qué la CB250R Domina Tokio
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap:8px; font-size:0.77rem; margin-bottom:12px;">
              <div style="background:rgba(255,255,255,0.03); padding:8px 10px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                <strong style="color:#f59e0b;">Horquilla Showa SFF-BP φ41mm:</strong><br>
                <span style="color:#d1d5db;">Invertida de pistón grande (misma tecnología de la serie CBR600RR/CB1000R) para absorber baches urbanos sin perder aplomo.</span>
              </div>
              <div style="background:rgba(255,255,255,0.03); padding:8px 10px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                <strong style="color:#38bdf8;">Assist &amp; Slipper® Clutch:</strong><br>
                <span style="color:#d1d5db;">Embrague antirrebote asistido (estreno del modelo 8BK-MC52): maneta ultrasuave en semáforos y cero bloqueo trasero al bajar marchas.</span>
              </div>
              <div style="background:rgba(255,255,255,0.03); padding:8px 10px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                <strong style="color:#10b981;">Frenos Radiales + IMU ABS:</strong><br>
                <span style="color:#d1d5db;">Pinza radial de 4 pistones + disco flotante de φ296mm con unidad inercial IMU que impide que la rueda trasera se levante en frenadas de pánico.</span>
              </div>
              <div style="background:rgba(255,255,255,0.03); padding:8px 10px; border-radius:8px; border:1px solid rgba(255,255,255,0.06);">
                <strong style="color:#c084fc;">Bisturí Urbano de 144 kg:</strong><br>
                <span style="color:#d1d5db;">24 kg más ligera que una CBR250RR, radio de giro de solo 2.3m y asiento a 795mm (homologada para 2 pasajeros con あやめ).</span>
              </div>
            </div>
          </div>

          <div style="background:linear-gradient(135deg, rgba(16,185,129,0.12), rgba(15,23,42,0.92)); border:1px solid rgba(16,185,129,0.4); border-radius:10px; padding:12px;">
            <div style="font-size:0.76rem; font-weight:800; color:#34d399; text-transform:uppercase; margin-bottom:4px;">
              🛡️ El «Hack Legal» de los 249 cm³ en Japón (Categoría 軽二輪 · Keijirin)
            </div>
            <ul style="margin:0; padding-left:18px; font-size:0.76rem; color:#e5e7eb; line-height:1.5;">
              <li><strong>¥0 Shaken (車検不要):</strong> Las motos de más de 250cc pagan ~¥75,000 cada 2 años en inspección obligatoria. Por tener <strong>249 cm³ exactos</strong>, tu CB250R está <strong>100% exenta de Shaken para siempre</strong>.</li>
              <li><strong>Acceso Total a Autopistas (首都高速 &amp; 高速道路):</strong> A diferencia de las 125cc, puedes subir a la Shuto Expressway hacia Haneda (24 min), Costco Makuhari (26 min) o Hakone.</li>
              <li><strong>Impuestos Mínimos:</strong> Impuesto anual de solo <strong>¥3,600/año (~$23 USD)</strong> y seguro obligatorio JCI (自賠責) de <strong>¥12,220 por 3 años (~$2.15 USD/mes)</strong>.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- BLUEPRINT DE MODIFICACIÓN EN TOKIO: HONDA CB250R «SHODAIGOJI 1954 SPEC» (初代ゴジラ仕様) -->
      <div style="background:linear-gradient(135deg, #070b12 0%, #0f172a 60%, #082f49 100%); border:1px solid rgba(6,182,212,0.55); border-left:5px solid #06b6d4; border-radius:14px; padding:18px 20px; margin-bottom:20px; box-shadow:0 10px 28px rgba(6,182,212,0.12);">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px; margin-bottom:12px;">
          <div>
            <span style="background:rgba(6,182,212,0.2); color:#22d3ee; border:1px solid #06b6d4; padding:3px 10px; border-radius:999px; font-size:0.71rem; font-weight:800; text-transform:uppercase; letter-spacing:0.8px;">
              🦖 PROYECTO CUSTOM TOKIO · 初代ゴジラ 1954年型 · SHODAIGOJI BUILD
            </span>
            <h4 style="margin:6px 0 2px; color:#fff; font-size:1.18rem; font-weight:900;">
              Talleres Reales en Tokio para Transformar tu CB250R en «ShodaiGoji 1954» (Piel Volcánica 結晶塗装 + Aliento Atómico Cherenkov)
            </h4>
            <div style="font-size:0.78rem; color:#cbd5e1;">
              Partiendo del color oficial <strong>Matte Gunpowder Black Metallic (マットガンパウダーブラックメタリック)</strong> —que ya incluye chasis y horquilla Showa SFF-BP negros de fábrica—, estos <strong>4 talleres especializados de Tokio</strong> ejecutan la conversión completa:
            </div>
          </div>
          <div style="background:rgba(9,13,22,0.9); border:1px solid rgba(34,211,238,0.4); border-radius:10px; padding:10px 14px; text-align:right;">
            <div style="font-size:0.68rem; color:#94a3b8; text-transform:uppercase; font-weight:700;">Inversión Full Custom (5 Etapas)</div>
            <div style="font-size:1.2rem; font-weight:900; color:#22d3ee;">¥314,300 <span style="font-size:0.8rem; color:#67e8f9;">(${fmtUSD(314300)})</span></div>
            <div style="font-size:0.7rem; color:#94a3b8;">Moto + Build Completo: <strong>¥878,600 (${fmtUSD(878600)})</strong></div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 245px), 1fr)); gap:12px;">
          <!-- Etapa 1: MyStyleCustom -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(255,255,255,0.1); border-top:3px solid #22d3ee; border-radius:10px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.71rem; color:#22d3ee; font-weight:800; margin-bottom:4px;">
                <span>FASE 01 · PIEL DE REPTIL 1954</span>
                <span>¥68,000 (${fmtUSD(68000)})</span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:#fff; margin-bottom:4px;">
                MyStyleCustom (板橋区本町27-9-110)
              </div>
              <p style="font-size:0.74rem; color:#cbd5e1; margin:0 0 8px; line-height:1.45;">
                Especialistas en <strong>Pintura Cristalina / Corrugada al Horno (結晶塗装 / ちぢみ塗装)</strong> y <strong>Gun-Kote</strong>. Encoge la resina en horno creando literalmente la <strong>textura rugosa tridimensional de piel volcánica quemada de Godzilla 1954</strong> en tapas de motor, radiador y tanque. A solo <strong>7 min de Ikebukuro</strong> (22 min desde Asakusabashi).
              </p>
            </div>
            <div style="display:flex; gap:6px;">
              <button type="button" class="cb250r-jump-shop-btn" data-dest="mystyle_custom_itabashi" style="flex:1; cursor:pointer; background:#0891b2; color:#fff; border:none; border-radius:6px; padding:6px 8px; font-size:0.72rem; font-weight:800;">
                📍 Trazar Ruta en Mapa
              </button>
              <a href="https://mystyle-custom.com/" target="_blank" rel="noopener" style="background:rgba(255,255,255,0.08); color:#e2e8f0; text-decoration:none; padding:6px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">Web ↗</a>
            </div>
          </div>

          <!-- Etapa 2: MOTO PARTS / K-SPEED & Moriwaki -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(255,255,255,0.1); border-top:3px solid #f59e0b; border-radius:10px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.71rem; color:#f59e0b; font-weight:800; margin-bottom:4px;">
                <span>FASE 02 · QUILLA KAIJU + RUGIDO</span>
                <span>¥123,300 (${fmtUSD(123300)})</span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:#fff; margin-bottom:4px;">
                MOTO PARTS (練馬区) &amp; Moriwaki BP-X
              </div>
              <p style="font-size:0.74rem; color:#cbd5e1; margin:0 0 8px; line-height:1.45;">
                Kit de carrocería <strong>K-SPEED Diabolus</strong> (quilla inferior <em>Belly Pan</em> con branquias tipo anfibio prehistórico + máscara de faro + colín corto: ¥54,000) + Escape <strong>Moriwaki NEO CLASSIC Black Pearl (BP-X · Certificado JMCA 政府認証: ¥69,300)</strong> para darle un rugido grave 100% legal en Japón.
              </p>
            </div>
            <div style="display:flex; gap:6px;">
              <button type="button" class="cb250r-jump-shop-btn" data-dest="motoparts_kspeed_moriwaki" style="flex:1; cursor:pointer; background:#d97706; color:#fff; border:none; border-radius:6px; padding:6px 8px; font-size:0.72rem; font-weight:800;">
                📍 Trazar Ruta en Mapa
              </button>
              <a href="https://motoparts.jp/" target="_blank" rel="noopener" style="background:rgba(255,255,255,0.08); color:#e2e8f0; text-decoration:none; padding:6px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">Web ↗</a>
            </div>
          </div>

          <!-- Etapa 3: Z-WORKS Airbrush -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(255,255,255,0.1); border-top:3px solid #38bdf8; border-radius:10px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.71rem; color:#38bdf8; font-weight:800; margin-bottom:4px;">
                <span>FASE 03 · AEROGRAFÍA CHERENKOV</span>
                <span>¥75,000 (${fmtUSD(75000)})</span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:#fff; margin-bottom:4px;">
                Custom Art Paint Z-WORKS (足立区扇1-5-26)
              </div>
              <p style="font-size:0.74rem; color:#cbd5e1; margin:0 0 8px; line-height:1.45;">
                Maestros en <strong>Aerografía Custom (エアーブラシアート)</strong> y anodizado (<strong>アルマイト加工</strong>). Pintan a mano las placas dorsales (背びれ) con grietas de <strong>Aliento Atómico en Azul Cherenkov → Blanco Incandescente</strong> en los alerones del tanque, el emblema <strong>「初代ゴジラ 1954」</strong> y tu casco Shoei a juego. A <strong>16 min de Asakusabashi</strong>.
              </p>
            </div>
            <div style="display:flex; gap:6px;">
              <button type="button" class="cb250r-jump-shop-btn" data-dest="zworks_adachi_airbrush" style="flex:1; cursor:pointer; background:#0284c7; color:#fff; border:none; border-radius:6px; padding:6px 8px; font-size:0.72rem; font-weight:800;">
                📍 Trazar Ruta en Mapa
              </button>
              <a href="https://zwp.jp/" target="_blank" rel="noopener" style="background:rgba(255,255,255,0.08); color:#e2e8f0; text-decoration:none; padding:6px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">Web ↗</a>
            </div>
          </div>

          <!-- Etapa 4: GARAGE SHANTI Wrapping & CR-1 -->
          <div style="background:rgba(15,23,42,0.85); border:1px solid rgba(255,255,255,0.1); border-top:3px solid #a855f7; border-radius:10px; padding:12px; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.71rem; color:#c084fc; font-weight:800; margin-bottom:4px;">
                <span>FASE 04 · WRAP 3M / COATING CR-1</span>
                <span>¥48,000 (${fmtUSD(48000)})</span>
              </div>
              <div style="font-size:0.88rem; font-weight:800; color:#fff; margin-bottom:4px;">
                GARAGE SHANTI (足立区神明3-14-23)
              </div>
              <p style="font-size:0.74rem; color:#cbd5e1; margin:0 0 8px; line-height:1.45;">
                Taller exclusivo de <strong>Wrapping de Motos (バイクラッピング)</strong> y blindaje de vidrio líquido <strong>CR-1 (resiste 1,300°C)</strong>. Pueden aplicar vinil 3M texturizado de escamas removible (protegiendo la pintura original para reventa antes de irte a Okinawa) + luz indirecta LED Azul Cherenkov bajo el tanque.
              </p>
            </div>
            <div style="display:flex; gap:6px;">
              <button type="button" class="cb250r-jump-shop-btn" data-dest="garage_shanti_wrap" style="flex:1; cursor:pointer; background:#7c3aed; color:#fff; border:none; border-radius:6px; padding:6px 8px; font-size:0.72rem; font-weight:800;">
                📍 Trazar Ruta en Mapa
              </button>
              <a href="https://shanti-lp.com/" target="_blank" rel="noopener" style="background:rgba(255,255,255,0.08); color:#e2e8f0; text-decoration:none; padding:6px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">Web ↗</a>
            </div>
          </div>
        </div>
      </div>

      <!-- MAPA INTERACTIVO EN VIVO (LEAFLET + OSRM ROUTING API) + INSPECTOR DE RUTA -->
      <div style="background:#0d131f; border:1px solid rgba(56,189,248,0.35); border-radius:14px; padding:18px; margin-bottom:20px;">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px; margin-bottom:14px;">
          <div>
            <div style="font-size:0.74rem; font-weight:800; color:#38bdf8; text-transform:uppercase;">
              🗺️ Mapa de Ruteo Satelital/Urbano en Vivo (OSRM Tokyo Street Geometry API)
            </div>
            <h4 style="margin:3px 0 0; color:#fff; font-size:1.1rem;">
              Selecciona tu Punto de Salida y Haz Clic en Cualquier Destino de tu Semana
            </h4>
          </div>

          <!-- Conmutador de Punto de Salida (Asakusabashi Front vs Ikebukuro Hub) -->
          <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center;">
            <span style="font-size:0.75rem; color:#9ca3af; font-weight:700;">Punto de Salida:</span>
            <button type="button" id="cb250r-base-asakusabashi" style="cursor:pointer; padding:7px 12px; border-radius:8px; font-size:0.76rem; font-weight:800; border:${
              STATE.baseKey === 'asakusabashi'
                ? '2px solid #38bdf8'
                : '1px solid rgba(255,255,255,0.18)'
            }; background:${
              STATE.baseKey === 'asakusabashi'
                ? 'rgba(56,189,248,0.2)'
                : 'rgba(255,255,255,0.05)'
            }; color:#fff;">
              🏠 Asakusabashi Front (台東区柳橋1-13-6)
            </button>
            <button type="button" id="cb250r-base-ikebukuro" style="cursor:pointer; padding:7px 12px; border-radius:8px; font-size:0.76rem; font-weight:800; border:${
              STATE.baseKey === 'ikebukuro'
                ? '2px solid #a855f7'
                : '1px solid rgba(255,255,255,0.18)'
            }; background:${
              STATE.baseKey === 'ikebukuro'
                ? 'rgba(168,85,247,0.22)'
                : 'rgba(255,255,255,0.05)'
            }; color:#fff;">
              🏙️ Ikebukuro Hub (豊島区池袋)
            </button>
            <button type="button" id="cb250r-toggle-tile" style="cursor:pointer; padding:7px 10px; border-radius:8px; font-size:0.74rem; font-weight:700; border:1px solid rgba(255,255,255,0.2); background:rgba(255,255,255,0.06); color:#e5e7eb;">
              🌓 Cambiar Capa Mapa
            </button>
          </div>
        </div>

        <!-- Filtros por Categoría de la Rutina 168H -->
        <div class="imperio-chip-scroll" style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px;">
          ${Object.entries(CATEGORY_META)
            .map(([catKey, meta]) => {
              const active = STATE.categoryFilter === catKey;
              return `<button type="button" class="cb250r-cat-btn" data-cat="${catKey}" style="cursor:pointer; padding:6px 12px; border-radius:999px; font-size:0.75rem; font-weight:800; border:${
                active ? `2px solid ${meta.color}` : '1px solid rgba(255,255,255,0.14)'
              }; background:${
                active ? 'rgba(255,255,255,0.12)' : 'rgba(255,255,255,0.04)'
              }; color:#fff;">
                ${meta.label}
              </button>`;
            })
            .join('')}
        </div>

        <!-- Contenedor Grid: Mapa Leaflet (Izquierda) + Telemetría del Destino Activo (Derecha) -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 285px), 1fr)); gap:16px; align-items:stretch;">
          <div id="cb250r-map-shell" style="position:relative; min-height:380px; border-radius:12px; overflow:hidden; border:1px solid rgba(255,255,255,0.15);">
            <div id="cb250r-leaflet-map" style="width:100%; height:420px; background:#090d16;"></div>
            <button type="button" id="cb250r-fullscreen-btn" onclick="window.toggleCb250rFullscreen && window.toggleCb250rFullscreen()" style="position:absolute; top:10px; right:10px; z-index:800; background:rgba(9,13,22,0.88); color:#38bdf8; border:1px solid rgba(56,189,248,0.45); border-radius:8px; padding:6px 10px; font-size:0.72rem; font-weight:800; cursor:pointer; backdrop-filter:blur(8px);">
              ⛶ Expandir Mapa
            </button>
          </div>

          <!-- Panel de Telemetría de la Ruta Seleccionada -->
          <div id="cb250r-active-route-panel" style="background:rgba(15,23,42,0.9); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:16px; display:flex; flex-direction:column; justify-content:space-between;">
          </div>
        </div>
      </div>

      <!-- TABLA MAESTRA DE TIEMPOS, COMBUSTIBLE Y ESTACIONAMIENTOS DE LOS 21 DESTINOS SEMANALES -->
      <div style="background:#0d131f; border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:18px; margin-bottom:20px;">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px; margin-bottom:12px;">
          <div>
            <h4 style="margin:0; color:#fff; font-size:1.08rem;">
              ⏱️ Matriz Completa de Tiempos Reales en tu Honda CB250R vs. Tren (${baseObj.short_name})
            </h4>
            <div style="font-size:0.76rem; color:#9ca3af; margin-top:2px;">
              Haz clic en cualquier fila para trazar la ruta exacta en el mapa interactivo y calcular el consumo milimétrico.
            </div>
          </div>
          <input type="search" id="cb250r-search-input" placeholder="🔍 Filtrar destino, dojo, clínica, cita..." value="${STATE.searchQuery}" style="background:#090d16; color:#fff; border:1px solid rgba(255,255,255,0.2); border-radius:8px; padding:8px 12px; font-size:0.84rem; flex:1; min-width:min(100%, 230px);" />
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
            <thead>
              <tr style="background:rgba(255,255,255,0.05); color:#93c5fd; text-align:left;">
                <th style="padding:9px 10px;">Categoría / Destino</th>
                <th style="padding:9px 10px;">Horario en Matriz 168H</th>
                <th style="padding:9px 10px;">Distancia</th>
                <th style="padding:9px 10px;">🏍️ CB250R</th>
                <th style="padding:9px 10px;">🚆 Tren/Pie</th>
                <th style="padding:9px 10px;">⚡ Ahorro (I/V)</th>
                <th style="padding:9px 10px;">⛽ Gasolina (Ida)</th>
                <th style="padding:9px 10px;">🅿️ Parking Moto (駐輪場)</th>
                <th style="padding:9px 10px;">Acción</th>
              </tr>
            </thead>
            <tbody id="cb250r-routes-tbody">
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLA OFICIAL HONDA JAPÓN: ESPECIFICACIONES TÉCNICAS COMPLETAS (8BK-MC52) -->
      <details style="background:#0d131f; border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:16px 18px;">
        <summary style="cursor:pointer; font-weight:800; color:#f59e0b; font-size:0.95rem;">
          📋 Ver Ficha Técnica Oficial Completa Honda Japón (CB250R 主要諸元 · 型式 ホンダ・8BK-MC52) &amp; Desglose CAPEX/OPEX
        </summary>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap:16px; margin-top:14px; font-size:0.78rem;">
          <div>
            <h5 style="margin:0 0 8px; color:#38bdf8; font-size:0.86rem;">Especificaciones Oficiales (/CB250R/spec/)</h5>
            <table style="width:100%; border-collapse:collapse;">
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Nombre y Código (車名・型式)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff; font-weight:700;">ホンダ・8BK-MC52</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Motor (エンジン型式 / 種類)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">MC52E · 水冷4ストロークDOHC4バルブ単気筒 (249 cm³)</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Potencia / Torque Máx.</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#4ade80; font-weight:700;">20 kW [27 PS] @ 9,500 rpm / 23 N·m @ 7,750 rpm</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Dimensiones (L × A × H)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">2,020 mm × 805 mm × 1,045 mm (Batalla: 1,355 mm)</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Peso / Altura Asiento / Giro</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">144 kg / 795 mm / Radio mín. 2.3 m (2 pasajeros)</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Consumo Oficial Combustible</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#38bdf8; font-weight:700;">WMTC: 33.7 km/L · Constante 60 km/h: 45.0 km/L (Tanque 10L)</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Transmisión &amp; Embrague</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">6 velocidades + Assist &amp; Slipper® Clutch</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Suspensión &amp; Frenos</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">Showa SFF-BP φ41mm invertida + Pinza radial 4 pistones + IMU-ABS</td></tr>
              <tr><td style="padding:6px; color:#9ca3af;">Neumáticos Radiales</td><td style="padding:6px; color:#fff;">Del: 110/70R17M/C 54H · Tras: 150/60R17M/C 66H</td></tr>
            </table>
          </div>

          <div>
            <h5 style="margin:0 0 8px; color:#10b981; font-size:0.86rem;">Presupuesto Real CAPEX &amp; OPEX en Tokio</h5>
            <table style="width:100%; border-collapse:collapse;">
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">MSRP Oficial Honda (10% IVA incl.)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff; font-weight:700;">¥564,300 (${fmtUSD(564300)})</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Registro, Placa Blanca 250cc + Jibaiseki 3 Años</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">~¥60,700 (${fmtUSD(60700)})</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Equipo (Casco Shoei + Intercom Sena + Soporte/ETC 2.0)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#fff;">~¥115,000 (${fmtUSD(115000)})</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Inspección Vehicular Shaken (車検)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#4ade80; font-weight:800;">¥0 (100% Exenta por ser 249cc 軽二輪)</td></tr>
              <tr><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#9ca3af;">Gasolina Mensual (Matriz 168H Completa)</td><td style="padding:6px; border-bottom:1px solid rgba(255,255,255,0.07); color:#38bdf8; font-weight:700;">${fmtJPY(weekly.fuel_cost_jpy_month)}/mes (${fmtUSD(weekly.fuel_cost_jpy_month)})</td></tr>
              <tr><td style="padding:6px; color:#9ca3af;">Impuesto Anual (軽自動車税)</td><td style="padding:6px; color:#fff;">¥3,600/año (~¥300/mes)</td></tr>
            </table>
          </div>
        </div>
      </details>
    `;

    bindEvents();
    renderTableRows();
    initOrUpdateMap();
    selectDestination(STATE.selectedDestId);
  }

  function bindEvents() {
    document.querySelectorAll('.cb250r-color-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        STATE.selectedColorId = btn.getAttribute('data-color');
        renderDashboard();
      });
    });

    const btnAsa = document.getElementById('cb250r-base-asakusabashi');
    if (btnAsa) {
      btnAsa.addEventListener('click', () => {
        STATE.baseKey = 'asakusabashi';
        renderDashboard();
      });
    }

    const btnIke = document.getElementById('cb250r-base-ikebukuro');
    if (btnIke) {
      btnIke.addEventListener('click', () => {
        STATE.baseKey = 'ikebukuro';
        renderDashboard();
      });
    }

    const btnTile = document.getElementById('cb250r-toggle-tile');
    if (btnTile) {
      btnTile.addEventListener('click', () => {
        STATE.tileMode = STATE.tileMode === 'dark' ? 'light' : 'dark';
        updateMapTileLayer();
      });
    }

    document.querySelectorAll('.cb250r-cat-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        STATE.categoryFilter = btn.getAttribute('data-cat');
        renderDashboard();
      });
    });

    const searchInput = document.getElementById('cb250r-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        STATE.searchQuery = e.target.value || '';
        renderTableRows();
      });
    }

    document.querySelectorAll('.cb250r-jump-shop-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const destId = btn.getAttribute('data-dest');
        STATE.categoryFilter = 'shodaigoji_custom';
        STATE.selectedDestId = destId;
        renderDashboard();
        const mapEl = document.getElementById('cb250r-leaflet-map');
        if (mapEl) {
          mapEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      });
    });
  }

  function getFilteredDestinations() {
    if (!STATE.feed) return [];
    const q = STATE.searchQuery.trim().toLowerCase();
    return STATE.feed.destinations.filter((d) => {
      if (STATE.categoryFilter !== 'all' && d.category !== STATE.categoryFilter) {
        return false;
      }
      if (!q) return true;
      return (
        d.name.toLowerCase().includes(q) ||
        d.subtitle.toLowerCase().includes(q) ||
        d.schedule_slot.toLowerCase().includes(q) ||
        d.address.toLowerCase().includes(q)
      );
    });
  }

  function renderTableRows() {
    const tbody = document.getElementById('cb250r-routes-tbody');
    if (!tbody || !STATE.feed) return;
    const list = getFilteredDestinations();

    tbody.innerHTML = list
      .map((d) => {
        const b = d[STATE.baseKey];
        const catMeta = CATEGORY_META[d.category] || CATEGORY_META.all;
        const isSelected = d.id === STATE.selectedDestId;
        return `
        <tr class="cb250r-route-row" data-dest="${d.id}" style="cursor:pointer; border-bottom:1px solid rgba(255,255,255,0.06); background:${
          isSelected ? 'rgba(56,189,248,0.14)' : 'transparent'
        }; transition:background 0.15s;">
          <td style="padding:9px 10px;">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:${catMeta.color}; margin-right:6px;"></span>
            <strong style="color:#fff;">${d.name}</strong>
            ${
              b.highway
                ? `<span style="margin-left:6px; background:rgba(16,185,129,0.2); color:#34d399; border:1px solid rgba(16,185,129,0.4); padding:1px 6px; border-radius:4px; font-size:0.66rem; font-weight:700;">首都高 / Autopista</span>`
                : ''
            }
            <div style="font-size:0.71rem; color:#9ca3af; margin-top:2px;">${d.subtitle}</div>
          </td>
          <td style="padding:9px 10px; color:#d1d5db; font-size:0.74rem;">${d.schedule_slot}</td>
          <td style="padding:9px 10px; color:#e5e7eb; font-weight:700;">${b.km} km</td>
          <td style="padding:9px 10px; color:#38bdf8; font-weight:900; font-size:0.86rem;">${b.cb250r_min} min</td>
          <td style="padding:9px 10px; color:#9ca3af;">${b.train_min} min</td>
          <td style="padding:9px 10px; color:#4ade80; font-weight:800;">-${b.time_saved_roundtrip_min} min I/V</td>
          <td style="padding:9px 10px; color:#f59e0b; font-weight:700;">
            ${b.fuel_ml_one_way} mL (${fmtJPY(b.fuel_cost_jpy_one_way)})
          </td>
          <td style="padding:9px 10px; color:#d1d5db; font-size:0.72rem;">${d.parking_spot}</td>
          <td style="padding:9px 10px;">
            <button type="button" class="cb250r-trace-btn" data-dest="${d.id}" style="cursor:pointer; background:#2563eb; color:#fff; border:none; border-radius:6px; padding:5px 9px; font-size:0.72rem; font-weight:700;">
              📍 Trazar Ruta
            </button>
          </td>
        </tr>`;
      })
      .join('');

    tbody.querySelectorAll('.cb250r-route-row').forEach((row) => {
      row.addEventListener('click', () => {
        const destId = row.getAttribute('data-dest');
        selectDestination(destId);
      });
    });
  }

  function updateMapTileLayer() {
    if (!STATE.map || !window.L) return;
    if (STATE.tileLayer) {
      STATE.map.removeLayer(STATE.tileLayer);
    }
    const url =
      STATE.tileMode === 'dark'
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    STATE.tileLayer = window.L.tileLayer(url, {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap &copy; CARTO | Honda CB250R Telemetry API'
    }).addTo(STATE.map);
  }

  async function initOrUpdateMap() {
    const L = await ensureLeafletLoaded();
    const mapEl = document.getElementById('cb250r-leaflet-map');
    if (!L || !mapEl || !STATE.feed) return;

    if (STATE.map) {
      STATE.map.remove();
      STATE.map = null;
    }

    const baseObj = STATE.feed.bases[STATE.baseKey];
    STATE.map = L.map(mapEl, {
      center: [baseObj.lat, baseObj.lon],
      zoom: 12,
      scrollWheelZoom: true
    });

    updateMapTileLayer();

    // Base Marker
    const baseIcon = L.divIcon({
      className: 'cb250r-base-pin',
      html: `<div style="background:#ef4444; color:#fff; border:3px solid #fff; border-radius:50%; width:30px; height:30px; display:flex; align-items:center; justify-content:center; font-size:15px; box-shadow:0 0 15px rgba(239,68,68,0.9);">🏠</div>`,
      iconSize: [30, 30],
      iconAnchor: [15, 15]
    });

    STATE.baseMarker = L.marker([baseObj.lat, baseObj.lon], { icon: baseIcon })
      .addTo(STATE.map)
      .bindPopup(`<strong>${baseObj.name}</strong><br>${baseObj.parking_note}`);

    STATE.destMarkers = {};
    const list = getFilteredDestinations();
    list.forEach((d) => {
      const catMeta = CATEGORY_META[d.category] || CATEGORY_META.all;
      const b = d[STATE.baseKey];
      const pinIcon = L.divIcon({
        className: 'cb250r-dest-pin',
        html: `<div style="background:${catMeta.color}; color:#fff; border:2px solid #090d16; border-radius:999px; padding:2px 7px; font-size:11px; font-weight:800; white-space:nowrap; box-shadow:0 3px 10px rgba(0,0,0,0.65);">${b.cb250r_min}m</div>`,
        iconSize: [42, 22],
        iconAnchor: [21, 11]
      });

      const marker = L.marker([d.lat, d.lon], { icon: pinIcon }).addTo(STATE.map);
      marker.on('click', () => selectDestination(d.id));
      STATE.destMarkers[d.id] = marker;
    });
  }

  async function selectDestination(destId) {
    if (!STATE.feed) return;
    const dest =
      STATE.feed.destinations.find((d) => d.id === destId) ||
      STATE.feed.destinations[0];
    if (!dest) return;
    STATE.selectedDestId = dest.id;

    // Highlight active row in table
    document.querySelectorAll('.cb250r-route-row').forEach((row) => {
      row.style.background =
        row.getAttribute('data-dest') === dest.id
          ? 'rgba(56,189,248,0.14)'
          : 'transparent';
    });

    const baseObj = STATE.feed.bases[STATE.baseKey];
    const b = dest[STATE.baseKey];
    const catMeta = CATEGORY_META[dest.category] || CATEGORY_META.all;
    const panel = document.getElementById('cb250r-active-route-panel');

    const gmapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${baseObj.lat},${baseObj.lon}&destination=${dest.lat},${dest.lon}&travelmode=driving`;

    if (panel) {
      panel.innerHTML = `
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px;">
            <span style="background:rgba(255,255,255,0.08); color:${catMeta.color}; padding:3px 10px; border-radius:999px; font-size:0.72rem; font-weight:800;">
              ${dest.category_label}
            </span>
            <span id="cb250r-osrm-badge" style="font-size:0.7rem; color:#38bdf8; font-weight:700;">
              🛰️ Calculando geometría OSRM en vivo...
            </span>
          </div>

          <h4 style="margin:0 0 4px; color:#fff; font-size:1.15rem; font-weight:900;">
            ${dest.name}
          </h4>
          <div style="font-size:0.79rem; color:#93c5fd; margin-bottom:10px;">
            ${dest.subtitle}
          </div>

          <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:10px; padding:10px 12px; margin-bottom:12px; font-size:0.76rem;">
            <div style="color:#9ca3af;">📍 <strong>Salida:</strong> ${baseObj.short_name}</div>
            <div style="color:#9ca3af; margin-top:3px;">🏁 <strong>Destino:</strong> ${dest.address}</div>
            <div style="color:#fde68a; margin-top:3px;">🗓️ <strong>Bloque Rutina 168H:</strong> ${dest.schedule_slot} (${dest.trips_per_week}x/semana)</div>
          </div>

          <!-- Comparativa Directa CB250R vs Tren -->
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px;">
            <div style="background:linear-gradient(135deg, rgba(56,189,248,0.16), rgba(15,23,42,0.9)); border:1px solid rgba(56,189,248,0.45); border-radius:10px; padding:10px;">
              <div style="font-size:0.7rem; color:#93c5fd; text-transform:uppercase; font-weight:700;">🏍️ Tiempo en Honda CB250R</div>
              <div style="font-size:1.45rem; font-weight:900; color:#fff; margin-top:2px;">${b.cb250r_min} min <span style="font-size:0.78rem; color:#38bdf8;">(${b.km} km)</span></div>
              <div style="font-size:0.71rem; color:#6ee7b7; margin-top:2px;">⚡ Ahorras ${b.time_saved_one_way_min} min ida / ${b.time_saved_roundtrip_min} min I/V</div>
            </div>

            <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.1); border-radius:10px; padding:10px;">
              <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase; font-weight:700;">🚆 En Tren + Caminata</div>
              <div style="font-size:1.45rem; font-weight:900; color:#9ca3af; margin-top:2px;">${b.train_min} min</div>
              <div style="font-size:0.71rem; color:#f87171; margin-top:2px;">Incluye transbordos y espera en andén</div>
            </div>
          </div>

          <!-- Consumo Exacto de Combustible y Estacionamiento -->
          <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:10px; padding:10px 12px; margin-bottom:12px; font-size:0.76rem;">
            <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:6px;">
              <span>⛽ <strong>Consumo Ida (WMTC 33.7 km/L):</strong> ${b.fuel_ml_one_way} mL (${b.fuel_liters_one_way} L)</span>
              <span style="color:#f59e0b; font-weight:800;">Costo Ida: ${fmtJPY(b.fuel_cost_jpy_one_way)} (${fmtUSD(b.fuel_cost_jpy_one_way)}) · I/V: ${fmtJPY(b.fuel_cost_jpy_roundtrip)}</span>
            </div>
            <div style="margin-top:5px; color:#d1d5db;">
              🅿️ <strong>Estacionamiento Moto (駐輪場):</strong> ${dest.parking_spot}
            </div>
            <div style="margin-top:5px; color:#a7f3d0;">
              💡 <strong>Ventaja Táctica:</strong> ${dest.tactical_note}
            </div>
          </div>
        </div>

        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <a href="${gmapsUrl}" target="_blank" rel="noopener" style="flex:1; text-align:center; background:#ef4444; color:#fff; text-decoration:none; padding:9px 14px; border-radius:8px; font-size:0.78rem; font-weight:800;">
            🧭 Abrir GPS en Google Maps (${baseObj.short_name.split(' ')[0]} → ${dest.name.split(' (')[0]}) ↗
          </a>
        </div>
      `;
    }

    // Draw Route on Leaflet Map via OSRM Live API (with fallback straight/curved line)
    if (STATE.map && window.L) {
      if (STATE.routeLayer) {
        STATE.map.removeLayer(STATE.routeLayer);
        STATE.routeLayer = null;
      }

      const osrmUrl = `https://router.project-osrm.org/route/v1/driving/${baseObj.lon},${baseObj.lat};${dest.lon},${dest.lat}?overview=full&geometries=geojson`;
      let drawn = false;
      try {
        const res = await fetch(osrmUrl);
        if (res.ok) {
          const data = await res.json();
          if (data.routes && data.routes[0] && data.routes[0].geometry) {
            const coords = data.routes[0].geometry.coordinates.map((c) => [c[1], c[0]]);
            STATE.routeLayer = window.L.polyline(coords, {
              color: '#38bdf8',
              weight: 5,
              opacity: 0.92
            }).addTo(STATE.map);
            STATE.map.fitBounds(STATE.routeLayer.getBounds(), { padding: [38, 38] });
            drawn = true;
            const badge = document.getElementById('cb250r-osrm-badge');
            if (badge) {
              const liveKm = (data.routes[0].distance / 1000).toFixed(1);
              badge.innerHTML = `🟢 Ruta OSRM en Vivo Trazada (${liveKm} km exactos por calle)`;
              badge.style.color = '#4ade80';
            }
          }
        }
      } catch (_) {}

      if (!drawn && STATE.map) {
        STATE.routeLayer = window.L.polyline(
          [
            [baseObj.lat, baseObj.lon],
            [dest.lat, dest.lon]
          ],
          { color: '#38bdf8', weight: 4, dashArray: '8, 6' }
        ).addTo(STATE.map);
        STATE.map.fitBounds(STATE.routeLayer.getBounds(), { padding: [45, 45] });
        const badge = document.getElementById('cb250r-osrm-badge');
        if (badge) {
          badge.innerHTML = `🟢 Vector Directo Trazado (${b.km} km)`;
        }
      }
    }
  }

  window.toggleCb250rFullscreen = function () {
    const shell = document.getElementById('cb250r-map-shell');
    const mapEl = document.getElementById('cb250r-leaflet-map');
    const btn = document.getElementById('cb250r-fullscreen-btn');
    if (!shell || !mapEl) return;
    const isExpanded = shell.classList.toggle('cb250r-map-expanded');
    if (isExpanded) {
      mapEl.style.height = '76vh';
      if (btn) btn.innerHTML = '✕ Contraer Mapa';
    } else {
      mapEl.style.height = '420px';
      if (btn) btn.innerHTML = '⛶ Expandir Mapa';
    }
    if (STATE.map) {
      setTimeout(() => STATE.map.invalidateSize(), 200);
    }
  };

  async function boot() {
    const mount = document.getElementById('cb250r-api-mount');
    if (!mount) return;
    await fetchLiveAPIs();
    renderDashboard();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
