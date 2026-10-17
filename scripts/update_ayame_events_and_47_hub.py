#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the upgraded assets/ayame-events-api.js (v5.0) combining:
1. Real-Time Ikebukuro + Tokyo + 8 Regions Event & Weather Radar (#ayame-radar-hub)
2. Full 24-Month / 47-Prefecture (Zenkoku Seiha 全国制覇) Interactive Itinerary,
   Live Weather per Prefecture, Itemized Cost Tracker (JPY + Live USD),
   and 1-Click Multi-Angle Booking Hub (#ayame-24-expediciones)
3. Real-Time JST Tactical Countdown Timers (#imperio-live-countdowns)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVENTS_FEED_PATH = ROOT / "assets" / "ayame-events-feed.json"
PREF_47_FEED_PATH = ROOT / "assets" / "prefectures-47-feed.json"
OUT_JS_PATH = ROOT / "assets" / "ayame-events-api.js"


def main():
    events_feed = json.loads(EVENTS_FEED_PATH.read_text(encoding="utf-8"))
    pref_47_feed = json.loads(PREF_47_FEED_PATH.read_text(encoding="utf-8"))

    events_json_str = json.dumps(events_feed, ensure_ascii=False, indent=2)
    pref_47_json_str = json.dumps(pref_47_feed, ensure_ascii=False, indent=2)

    js_code = f"""/**
 * Atlas del Imperio — Motor Multi-API en Tiempo Real para あやめ (v5.0)
 * 1. Radar de Eventos, Lugares y Clima en Ikebukuro, Tokio y Japón (#ayame-radar-hub)
 * 2. Códice Maestro de 24 Meses y las 47 Prefecturas de Japón (Zenkoku Seiha 全国制覇)
 *    con Clima en Vivo por Prefectura, Desglose de Costos Multi-Ángulo (JPY/USD)
 *    y Central de Reservas 1-Click (#ayame-24-expediciones)
 * 3. Cronómetro Táctico en Tiempo Real sincronizado con Japón JST (#imperio-live-countdowns)
 */
(function () {{
  const INITIAL_FEED = {events_json_str};
  const INITIAL_47_FEED = {pref_47_json_str};

  const CITIES_COORDS = {{
    ikebukuro: {{ name: "Ikebukuro / Asakusabashi (Tokio)", region: "Kanto", lat: 35.7295, lon: 139.7109 }},
    sapporo: {{ name: "Sapporo / Hakodate", region: "Hokkaido", lat: 43.0618, lon: 141.3545 }},
    sendai: {{ name: "Sendai / Ginzan Onsen", region: "Tohoku", lat: 38.2682, lon: 140.8694 }},
    kanazawa: {{ name: "Kanazawa / Shirakawa-go", region: "Chubu & Hokuriku", lat: 36.5613, lon: 136.6562 }},
    kyoto: {{ name: "Kioto / Kobe / Osaka", region: "Kansai", lat: 35.0116, lon: 135.7681 }},
    hiroshima: {{ name: "Miyajima / Izumo / Tottori", region: "Chugoku", lat: 34.3853, lon: 132.4553 }},
    matsuyama: {{ name: "Matsuyama (Dogo Onsen)", region: "Shikoku", lat: 33.8392, lon: 132.7656 }},
    fukuoka: {{ name: "Fukuoka / Beppu / Ibusuki", region: "Kyushu", lat: 33.5904, lon: 130.4017 }},
    okinawa: {{ name: "Naha / Isla Ishigaki", region: "Okinawa", lat: 26.2124, lon: 127.6809 }}
  }};

  let liveRateJpy = INITIAL_FEED.usd_jpy_rate || 158.08;
  let weatherState = JSON.parse(JSON.stringify(INITIAL_FEED.cities_weather || {{}}));
  let holidaysState = JSON.parse(JSON.stringify(INITIAL_FEED.upcoming_jp_holidays || []));
  let pref47Data = JSON.parse(JSON.stringify(INITIAL_47_FEED));
  let monthWeatherMap = {{}};
  let lastSyncTime = new Date().toLocaleTimeString();

  function getActiveRate() {{
    if (window.IMPERIO_LIVE_RATES && window.IMPERIO_LIVE_RATES.JPY) {{
      return Number(window.IMPERIO_LIVE_RATES.JPY);
    }}
    return liveRateJpy || 158.08;
  }}

  function fmtJpy(n) {{
    return "¥" + Math.round(n).toLocaleString("en-US");
  }}

  function fmtUsd(jpy) {{
    return "$" + Math.round(jpy / getActiveRate()).toLocaleString("en-US");
  }}

  function evaluateAyameComfort(temp, rain, hum) {{
    if (rain > 2.0) {{
      return "☔ Lluvia detectada: Priorizar Ruta Techada (Sunshine City / Planetario MANTEN / Sastrería)";
    }}
    if (temp >= 29 || (temp >= 26 && hum >= 75)) {{
      return "🌡️ Calor/Humedad: Priorizar Brisa Marina, Acuario Nocturno o Tren Suite Climatizado";
    }}
    if (temp <= 9) {{
      return "❄️ Fresco Invernal: Ideal para Onsen Privado (Kashikiri) y Abrigo Suave";
    }}
    return "🌸 Clima Perfecto para あやめ (Brisa Suave y Cero Fatiga)";
  }}

  async function refreshLiveApis() {{
    // 1. Live FX Rate
    try {{
      const fxRes = await fetch("https://open.er-api.com/v6/latest/USD", {{ cache: "no-store" }});
      if (fxRes.ok) {{
        const fxData = await fxRes.json();
        if (fxData && fxData.rates && fxData.rates.JPY) {{
          liveRateJpy = Number(fxData.rates.JPY);
        }}
      }}
    }} catch (_) {{}}

    // 2. Open-Meteo Batch Weather for the 9 Radar Hubs
    try {{
      const keys = Object.keys(CITIES_COORDS);
      const lats = keys.map((k) => CITIES_COORDS[k].lat).join(",");
      const lons = keys.map((k) => CITIES_COORDS[k].lon).join(",");
      const url = `https://api.open-meteo.com/v1/forecast?latitude=${{lats}}&longitude=${{lons}}&current=temperature_2m,relative_humidity_2m,precipitation&timezone=Asia%2FTokyo`;
      const wRes = await fetch(url, {{ cache: "no-store" }});
      if (wRes.ok) {{
        const wData = await wRes.json();
        const list = Array.isArray(wData) ? wData : [wData];
        keys.forEach((k, idx) => {{
          const cur = (list[idx] && list[idx].current) || {{}};
          const temp = cur.temperature_2m !== undefined ? cur.temperature_2m : 18.0;
          const hum = cur.relative_humidity_2m !== undefined ? cur.relative_humidity_2m : 60;
          const rain = cur.precipitation !== undefined ? cur.precipitation : 0.0;
          weatherState[k] = {{
            name: CITIES_COORDS[k].name,
            region: CITIES_COORDS[k].region,
            temp_c: temp,
            humidity: hum,
            rain_mm: rain,
            ayame_status: evaluateAyameComfort(temp, rain, hum)
          }};
        }});
      }}
    }} catch (_) {{}}

    // 3. Open-Meteo Batch Weather for the 24 Monthly Expeditions (47 Prefectures)
    try {{
      const months = pref47Data.itinerary_24_months || [];
      if (months.length > 0) {{
        const lats = months.map((m) => m.lat).join(",");
        const lons = months.map((m) => m.lon).join(",");
        const url24 = `https://api.open-meteo.com/v1/forecast?latitude=${{lats}}&longitude=${{lons}}&current=temperature_2m,relative_humidity_2m,precipitation&timezone=Asia%2FTokyo`;
        const res24 = await fetch(url24, {{ cache: "no-store" }});
        if (res24.ok) {{
          const data24 = await res24.json();
          const list24 = Array.isArray(data24) ? data24 : [data24];
          months.forEach((m, i) => {{
            const cur = (list24[i] && list24[i].current) || {{}};
            if (cur.temperature_2m !== undefined) {{
              monthWeatherMap[m.month_num] = {{
                temp_c: cur.temperature_2m,
                humidity: cur.relative_humidity_2m || 65,
                rain_mm: cur.precipitation || 0
              }};
            }}
          }});
        }}
      }}
    }} catch (_) {{}}

    // 4. Nager.Date Japan Public Holidays
    try {{
      const hRes = await fetch("https://date.nager.at/api/v3/NextPublicHolidays/JP", {{ cache: "no-store" }});
      if (hRes.ok) {{
        const hData = await hRes.json();
        if (Array.isArray(hData) && hData.length > 0) {{
          holidaysState = hData.slice(0, 6);
        }}
      }}
    }} catch (_) {{}}

    lastSyncTime = new Date().toLocaleTimeString();
  }}

  // =========================================================================
  // MODULE 1: RADAR EN TIEMPO REAL DE IKEBUKURO, TOKIO Y JAPÓN (#ayame-radar-hub)
  // =========================================================================
  function initAyameRadar() {{
    const root = document.getElementById("ayame-radar-hub");
    if (!root) return;

    let activeZone = "all";
    let searchTerm = "";
    const savedFavs = JSON.parse(localStorage.getItem("imperio_ayame_radar_favs_v1") || "{{}}");

    function renderWeatherAndHolidays() {{
      const wGrid = document.getElementById("ayame-live-weather-grid");
      const hStrip = document.getElementById("ayame-live-holidays-strip");
      if (wGrid) {{
        wGrid.innerHTML = Object.keys(weatherState)
          .map((k) => {{
            const w = weatherState[k];
            const isIkb = k === "ikebukuro";
            return `
              <div style="background:${{isIkb ? "rgba(244,114,182,0.14)" : "rgba(0,0,0,0.38)"}}; border:1px solid ${{isIkb ? "#f472b6" : "rgba(255,255,255,0.12)"}}; border-radius:8px; padding:9px 11px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                  <span style="font-size:0.72rem; font-weight:700; color:${{isIkb ? "#f9a8d4" : "#93c5fd"}}; text-transform:uppercase;">${{w.region}}</span>
                  <span style="font-size:0.84rem; font-weight:800; color:#fff;">🌡️ ${{w.temp_c}}°C · 💧 ${{w.humidity}}%</span>
                </div>
                <div style="font-size:0.8rem; font-weight:700; color:#f3f4f6; margin-top:2px;">${{w.name}}</div>
                <div style="font-size:0.7rem; color:#a7f3d0; margin-top:3px;">${{w.ayame_status}}</div>
              </div>
            `;
          }})
          .join("");
      }}

      if (hStrip) {{
        hStrip.innerHTML =
          `<span style="font-size:0.74rem; color:#fde047; font-weight:700;">🎌 Próximos Días Festivos en Japón (Nager.Date API — Evitar multitudes con あやめ):</span>` +
          holidaysState
            .map(
              (h) =>
                `<span style="background:rgba(234,179,8,0.15); border:1px solid rgba(234,179,8,0.4); color:#fef08a; padding:2px 8px; border-radius:999px; font-size:0.71rem;">📅 ${{h.date}}: ${{h.localName}} (${{h.name}})</span>`
            )
            .join("");
      }}
    }}

    function renderPlaces() {{
      const gridEl = document.getElementById("ayame-radar-places-grid");
      if (!gridEl) return;

      const q = searchTerm.trim().toLowerCase();
      const filtered = (INITIAL_FEED.events_and_places || []).filter((item) => {{
        if (activeZone === "favs" && !savedFavs[item.id]) return false;
        if (activeZone !== "all" && activeZone !== "favs" && item.zone !== activeZone) return false;
        if (!q) return true;
        return (
          item.title.toLowerCase().includes(q) ||
          item.region.toLowerCase().includes(q) ||
          item.category.toLowerCase().includes(q) ||
          item.ayame_standard.toLowerCase().includes(q) ||
          item.diet_note.toLowerCase().includes(q)
        );
      }});

      gridEl.innerHTML = filtered
        .map((item) => {{
          const isFav = !!savedFavs[item.id];
          const zoneColor =
            item.zone === "ikebukuro"
              ? "#f472b6"
              : item.zone === "tokio"
              ? "#38bdf8"
              : "#f0b90b";
          return `
            <div style="background:#161b22; border:1px solid #30363d; border-top:3px solid ${{zoneColor}}; border-radius:10px; padding:16px; display:flex; flex-direction:column; justify-content:space-between;">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px; margin-bottom:6px;">
                  <span style="font-size:0.72rem; font-weight:700; color:${{zoneColor}}; text-transform:uppercase;">📍 ${{item.region}} · ${{item.category}}</span>
                  <button data-fav-id="${{item.id}}" style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.2); color:${{isFav ? "#f472b6" : "#9ca3af"}}; border-radius:6px; padding:2px 8px; font-size:0.72rem; cursor:pointer;">
                    ${{isFav ? "💖 En Lista de あやめ" : "🤍 Guardar"}}
                  </button>
                </div>
                <h4 style="color:#fff; font-size:0.98rem; margin:4px 0 8px;">${{item.title}}</h4>
                <p style="color:#d1d5db; font-size:0.82rem; line-height:1.45; margin-bottom:8px;">✨ <strong>Estándar あやめ:</strong> ${{item.ayame_standard}}</p>
                <div style="font-size:0.76rem; color:#9ca3af; margin-bottom:4px;">⚡ <strong>Energía:</strong> <span style="color:#a7f3d0;">${{item.energy_level}}</span></div>
                <div style="font-size:0.76rem; color:#9ca3af; margin-bottom:4px;">🏠 <strong>Regreso Juntos a Casa:</strong> <span style="color:#fbcfe8;">${{item.return_home}}</span></div>
                <div style="font-size:0.76rem; color:#9ca3af; margin-bottom:4px;">🥊 <strong>Sincronía MMA:</strong> <span style="color:#fde68a;">${{item.fight_zone}}</span></div>
                <div style="font-size:0.76rem; color:#9ca3af; margin-bottom:10px;">🥩 <strong>Protocolo Carnívoro:</strong> ${{item.diet_note}}</div>
              </div>
              <div style="display:flex; justify-content:space-between; align-items:center; padding-top:10px; border-top:1px solid rgba(255,255,255,0.08);">
                <div>
                  <span style="font-size:0.92rem; font-weight:800; color:#fff;">${{fmtJpy(item.price_jpy)}}</span>
                  <span style="font-size:0.78rem; font-weight:700; color:#4ade80; background:rgba(34,197,94,0.14); border:1px solid rgba(74,222,128,0.35); padding:2px 6px; border-radius:5px; margin-left:4px;">⚡ ${{fmtUsd(item.price_jpy)}} USD</span>
                </div>
                <a href="${{item.url}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.74rem;">🔗 Agendar / Sitio Oficial ↗</a>
              </div>
            </div>
          `;
        }})
        .join("");

      gridEl.querySelectorAll("button[data-fav-id]").forEach((btn) => {{
        btn.addEventListener("click", () => {{
          const id = btn.getAttribute("data-fav-id");
          if (savedFavs[id]) delete savedFavs[id];
          else savedFavs[id] = true;
          localStorage.setItem("imperio_ayame_radar_favs_v1", JSON.stringify(savedFavs));
          renderPlaces();
        }});
      }});
    }}

    root.innerHTML = `
      <div style="background:linear-gradient(135deg, rgba(244,114,182,0.12), rgba(56,189,248,0.08)); border:1px solid rgba(244,114,182,0.4); border-radius:12px; padding:18px; margin-bottom:18px;">
        <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:10px; margin-bottom:12px;">
          <div>
            <span style="background:rgba(34,197,94,0.2); color:#4ade80; border:1px solid #22c55e; padding:3px 10px; border-radius:999px; font-size:0.72rem; font-weight:700;">
              🛰️ 3 APIs CONECTADAS EN VIVO (Open-Meteo Japan + Nager.Date Festivos JP + FX USD/JPY)
            </span>
            <h3 style="color:#fff; margin:8px 0 4px; font-size:1.25rem;">🌸 Radar en Tiempo Real de Ikebukuro, Tokio y las 8 Regiones de Japón para あやめ</h3>
            <p style="color:#d1d5db; font-size:0.82rem; margin:0;">
              🏠 <strong>Regla de Hogar Compartido:</strong> Vivimos juntos con nuestros <strong>2 gatitos y 2 chinchillas</strong>. Regresar a casa es <strong>regresar juntos a nuestro hogar antes de las 21:00 hrs</strong> para bañarnos a las 21:15 y dormir abrazados a las <strong>22:30 hrs</strong>.
            </p>
          </div>
          <button id="btn-refresh-ayame-radar" class="plan-tab active" style="cursor:pointer; font-size:0.78rem;">🔄 Sincronizar Clima & Eventos API Ahora</button>
        </div>

        <div id="ayame-live-weather-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:8px; margin-bottom:12px;"></div>
        <div id="ayame-live-holidays-strip" style="display:flex; flex-wrap:wrap; gap:6px; align-items:center; padding-top:8px; border-top:1px solid rgba(255,255,255,0.1);"></div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:8px; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <button class="plan-tab radar-zone-btn active" data-zone="all">🌟 Todo el Radar (${{INITIAL_FEED.events_and_places.length}} Experiencias)</button>
          <button class="plan-tab radar-zone-btn" data-zone="ikebukuro" style="border-color:#f472b6; color:#f9a8d4;">🦉 Ikebukuro VIP & Otome Road (8)</button>
          <button class="plan-tab radar-zone-btn" data-zone="tokio" style="border-color:#38bdf8; color:#7dd3fc;">👘 Tokio: Costura, Cruceros & Gala (4)</button>
          <button class="plan-tab radar-zone-btn" data-zone="japon" style="border-color:#f0b90b; color:#fde68a;">🗾 Todo Japón: 8 Regiones & Trenes Suite (10)</button>
          <button class="plan-tab radar-zone-btn" data-zone="favs">💖 Guardados de あやめ</button>
        </div>
        <input id="ayame-radar-search" type="search" placeholder="🔍 Buscar Ikebukuro, planetario, kimono, onsen, gatos, Wagyu..." style="background:rgba(0,0,0,0.5); border:1px solid rgba(255,255,255,0.22); color:#fff; padding:7px 12px; border-radius:6px; min-width:280px; font-size:0.82rem;">
      </div>

      <div id="ayame-radar-places-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:16px;"></div>
    `;

    renderWeatherAndHolidays();
    renderPlaces();

    root.querySelectorAll(".radar-zone-btn").forEach((btn) => {{
      btn.addEventListener("click", () => {{
        root.querySelectorAll(".radar-zone-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeZone = btn.getAttribute("data-zone");
        renderPlaces();
      }});
    }});

    const sInput = document.getElementById("ayame-radar-search");
    if (sInput) {{
      sInput.addEventListener("input", (e) => {{
        searchTerm = e.target.value || "";
        renderPlaces();
      }});
    }}

    const refreshBtn = document.getElementById("btn-refresh-ayame-radar");
    if (refreshBtn) {{
      refreshBtn.addEventListener("click", async () => {{
        refreshBtn.textContent = "⏳ Actualizando APIs en vivo...";
        await refreshLiveApis();
        renderWeatherAndHolidays();
        renderPlaces();
        if (typeof window.renderZenkoku47Hub === "function") window.renderZenkoku47Hub();
        refreshBtn.textContent = "✅ APIs Sincronizadas (" + lastSyncTime + ")";
      }});
    }}
  }}

  // =========================================================================
  // MODULE 2: EL GRAN ITINERARIO DE 24 MESES Y LAS 47 PREFECTURAS (#ayame-24-expediciones)
  // =========================================================================
  function initZenkokuSeiha47Hub() {{
    const sec = document.getElementById("ayame-24-expediciones");
    if (!sec) return;

    const savedMonths = JSON.parse(localStorage.getItem("imperio_zenkoku_47_months_v1") || "{{}}");
    let activePhase = "all";
    let activeZone = "all";
    let activeRegion = "all";
    let searchQuery = "";
    let showAll47Pills = false;

    // Collect all 47 prefectures in order #01 to #47 from the 24 months
    const all47List = [];
    (pref47Data.itinerary_24_months || []).forEach((m) => {{
      (m.prefectures_conquered || []).forEach((pStr) => {{
        const match = pStr.match(/#(\\d+)\\s+(.+)/);
        if (match) {{
          all47List.push({{
            num: parseInt(match[1], 10),
            code: "#" + match[1],
            name: match[2],
            label: pStr,
            monthNum: m.month_num,
            monthId: m.id,
            dateLabel: m.date_label
          }});
        }}
      }});
    }});
    all47List.sort((a, b) => a.num - b.num);

    function renderHub() {{
      const months = pref47Data.itinerary_24_months || [];
      const grandTotalJpy = (pref47Data.summary && pref47Data.summary.grand_total_jpy) || 5594200;

      // Calculate conquered counts
      let conqueredMonthsCount = 0;
      const conqueredPrefsSet = new Set();
      let spentJpy = 0;

      months.forEach((m) => {{
        if (savedMonths[m.id]) {{
          conqueredMonthsCount++;
          spentJpy += m.total_jpy || 0;
          (m.prefectures_conquered || []).forEach((p) => conqueredPrefsSet.add(p));
        }}
      }});

      const conqueredPrefsCount = conqueredPrefsSet.size;
      const pct47 = Math.round((conqueredPrefsCount / 47) * 100);

      // Filter months
      const q = searchQuery.trim().toLowerCase();
      const filteredMonths = months.filter((m) => {{
        if (activePhase !== "all" && String(m.phase) !== activePhase) return false;
        if (activeZone !== "all" && m.zone_color !== activeZone) return false;
        if (activeRegion !== "all" && m.region !== activeRegion) return false;
        if (!q) return true;
        const hay = [
          m.title,
          m.date_label,
          m.region_label,
          m.fight_sync,
          m.ikebukuro_shortcut,
          m.cat_protocol,
          m.nutrition_77kg,
          m.ayame_treat,
          ...(m.prefectures_conquered || []),
          ...(m.schedule || [])
        ]
          .join(" ")
          .toLowerCase();
        return hay.includes(q);
      }});

      // Build 47 Prefecture Stamp Rally badges
      const stampBadgesHtml = all47List
        .map((p) => {{
          const isConquered = conqueredPrefsSet.has(p.label);
          return `
            <span
              data-jump-month="${{p.monthId}}"
              title="Conquistada en Mes ${{String(p.monthNum).padStart(2, "0")}} (${{p.dateLabel}}) — Clic para ir al itinerario"
              style="cursor:pointer; padding:3px 9px; border-radius:999px; font-size:0.72rem; font-weight:700; transition:all 0.15s; border:1px solid ${{
                isConquered ? "#22c55e" : "rgba(255,255,255,0.14)"
              }}; background:${{
                isConquered ? "rgba(34,197,94,0.22)" : "rgba(255,255,255,0.04)"
              }}; color:${{isConquered ? "#4ade80" : "#9ca3af"}};"
            >
              ${{isConquered ? "✅ " : "🗾 "}}${{p.label}}
            </span>
          `;
        }})
        .join("");

      const zoneColors = {{
        yellow: {{ border: "#d29922", bg: "rgba(210,153,34,0.14)", text: "#fde68a" }},
        red: {{ border: "#f85149", bg: "rgba(248,81,73,0.14)", text: "#fca5a5" }},
        green: {{ border: "#2ea043", bg: "rgba(46,160,67,0.14)", text: "#86efac" }},
        gold: {{ border: "#f0b90b", bg: "rgba(240,185,11,0.18)", text: "#fef08a" }}
      }};

      const cardsHtml = filteredMonths
        .map((m) => {{
          const zc = zoneColors[m.zone_color] || zoneColors.yellow;
          const isDone = !!savedMonths[m.id];
          const w = monthWeatherMap[m.month_num];
          const weatherPill = w
            ? `<span style="background:rgba(56,189,248,0.14); border:1px solid rgba(56,189,248,0.35); color:#7dd3fc; padding:2px 8px; border-radius:999px; font-size:0.7rem; font-weight:700;">🌡️ Clima Hoy: ${{w.temp_c}}°C · 💧 ${{w.humidity}}%</span>`
            : `<span style="background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.25); color:#7dd3fc; padding:2px 8px; border-radius:999px; font-size:0.7rem;">🛰️ Open-Meteo Ready</span>`;

          const prefsPills = (m.prefectures_conquered || [])
            .map((p) => {{
              const isNew = !p.includes("Base");
              return `<span style="background:${{
                isNew ? "rgba(240,185,11,0.16)" : "rgba(148,163,184,0.14)"
              }}; border:1px solid ${{
                isNew ? "#f0b90b" : "rgba(148,163,184,0.3)"
              }}; color:${{
                isNew ? "#fef08a" : "#cbd5e1"
              }}; padding:2px 8px; border-radius:6px; font-size:0.72rem; font-weight:700;">🗾 ${{p}}</span>`;
            }})
            .join("");

          const scheduleHtml = (m.schedule || [])
            .map(
              (line) =>
                `<li style="margin-bottom:5px; color:#e5e7eb; font-size:0.8rem; line-height:1.45;">${{line}}</li>`
            )
            .join("");

          const c = m.costs_jpy || {{}};
          const b = m.booking_links || {{}};

          return `
            <div id="card-${{m.id}}" class="exp-47-card" style="background:#0d1117; border:1px solid ${{
              isDone ? "#22c55e" : "#30363d"
            }}; border-top:4px solid ${{zc.border}}; border-radius:12px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:${{
              isDone ? "0 0 0 2px rgba(34,197,94,0.35), 0 10px 26px rgba(0,0,0,0.45)" : "0 6px 20px rgba(0,0,0,0.35)"
            }};">
              <div>
                <!-- ENCABEZADO DEL MES -->
                <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px;">
                  <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;">
                    <span style="background:${{zc.bg}}; border:1px solid ${{zc.border}}; color:${{zc.text}}; padding:2px 9px; border-radius:999px; font-size:0.71rem; font-weight:800;">
                      MES ${{String(m.month_num).padStart(2, "0")}} • ${{m.date_label.toUpperCase()}}
                    </span>
                    <span style="font-size:0.72rem; color:#9ca3af; font-weight:700;">${{m.zone_badge}}</span>
                    ${{weatherPill}}
                  </div>
                  <label style="display:inline-flex; align-items:center; gap:6px; background:${{
                    isDone ? "rgba(34,197,94,0.2)" : "rgba(255,255,255,0.06)"
                  }}; border:1px solid ${{
                    isDone ? "#22c55e" : "rgba(255,255,255,0.2)"
                  }}; color:${{
                    isDone ? "#4ade80" : "#d1d5db"
                  }}; padding:3px 10px; border-radius:8px; font-size:0.74rem; font-weight:700; cursor:pointer;">
                    <input type="checkbox" data-check-month="${{m.id}}" ${{isDone ? "checked" : ""}} style="cursor:pointer;">
                    ${{isDone ? "✅ Conquistado" : "Sellar Mes"}}
                  </label>
                </div>

                <!-- TÍTULO Y PREFECTURAS -->
                <h3 style="color:#ffffff; font-size:1.08rem; margin:6px 0 8px; line-height:1.35;">${{m.title}}</h3>
                <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px;">
                  ${{prefsPills}}
                  <span style="background:rgba(167,139,250,0.14); border:1px solid rgba(167,139,250,0.35); color:#ddd6fe; padding:2px 8px; border-radius:6px; font-size:0.71rem; font-weight:600;">
                    ⏱️ ${{m.duration}} · ${{m.region_label}}
                  </span>
                </div>

                <!-- LOGÍSTICA TÁCTICA: ATAJO IKEBUKURO + GATITOS + MMA -->
                <div style="background:rgba(22,27,34,0.9); border:1px solid #21262d; border-radius:8px; padding:10px 12px; margin-bottom:10px; font-size:0.76rem;">
                  <div style="margin-bottom:4px; color:#93c5fd;">🚀 <strong>Ruta / Atajo desde Ikebukuro:</strong> <span style="color:#e5e7eb;">${{m.ikebukuro_shortcut}}</span></div>
                  <div style="margin-bottom:4px; color:#f9a8d4;">🐱 <strong>Protocolo Gatitos de あやめ:</strong> <span style="color:#e5e7eb;">${{m.cat_protocol}}</span></div>
                  <div style="color:#fde047;">🥊 <strong>Sincronía Campamento (77 kg):</strong> <span style="color:#e5e7eb;">${{m.fight_sync}}</span></div>
                </div>

                <!-- ITINERARIO HORARIO POR HORARIO / DÍA POR DÍA -->
                <div style="margin-bottom:10px;">
                  <div style="font-size:0.73rem; font-weight:800; color:#f0b90b; text-transform:uppercase; letter-spacing:0.04em; margin-bottom:5px;">
                    📋 Itinerario Táctico Paso a Paso:
                  </div>
                  <ul style="margin:0; padding-left:18px;">
                    ${{scheduleHtml}}
                  </ul>
                </div>

                <!-- NUTRICIÓN 77 KG & MIMO PARA AYAME -->
                <div style="background:rgba(16,185,129,0.07); border:1px solid rgba(16,185,129,0.25); border-radius:8px; padding:9px 11px; margin-bottom:12px; font-size:0.75rem;">
                  <div style="margin-bottom:4px; color:#6ee7b7;">🥩 <strong>Nutrición 77 kg (0 Alcohol 🚫🍺):</strong> <span style="color:#ecfdf5;">${{m.nutrition_77kg}}</span></div>
                  <div style="color:#fbcfe8;">🌸 <strong>Mimo & Estándar de あやめ (0 Mango 🚫🥭):</strong> <span style="color:#fdf2f8;">${{m.ayame_treat}}</span></div>
                </div>
              </div>

              <!-- DESGLOSE FINANCIERO MULTI-ÁNGULO + BOTONES DE RESERVA 1-CLICK -->
              <div>
                <div style="background:#161b22; border:1px solid #30363d; border-radius:8px; padding:10px; margin-bottom:10px;">
                  <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px; margin-bottom:6px; padding-bottom:6px; border-bottom:1px solid rgba(255,255,255,0.08);">
                    <span style="font-size:0.73rem; font-weight:700; color:#9ca3af; text-transform:uppercase;">💰 Desglose Real en Vivo (Mes ${{String(m.month_num).padStart(2, "0")}})</span>
                    <div>
                      <span style="font-size:1rem; font-weight:800; color:#fff;">${{fmtJpy(m.total_jpy)}} JPY</span>
                      <span style="font-size:0.8rem; font-weight:800; color:#4ade80; background:rgba(34,197,94,0.16); border:1px solid rgba(74,222,128,0.4); padding:2px 7px; border-radius:5px; margin-left:5px;">
                        ⚡ ${{fmtUsd(m.total_jpy)}} USD Hoy
                      </span>
                    </div>
                  </div>
                  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(115px, 1fr)); gap:6px; font-size:0.7rem; color:#d1d5db;">
                    <div>🚄 Transp: <strong>${{fmtJpy(c.transporte || 0)}}</strong> (${{fmtUsd(c.transporte || 0)}})</div>
                    <div>♨️ Hotel: <strong>${{fmtJpy(c.hospedaje || 0)}}</strong> (${{fmtUsd(c.hospedaje || 0)}})</div>
                    <div>👘 Activ/Telas: <strong>${{fmtJpy(c.actividades_telas || 0)}}</strong> (${{fmtUsd(c.actividades_telas || 0)}})</div>
                    <div>🥩 Comida: <strong>${{fmtJpy(c.gastronomia || 0)}}</strong> (${{fmtUsd(c.gastronomia || 0)}})</div>
                    <div>🐱 Cat Sitter: <strong>${{fmtJpy(c.cat_sitter || 0)}}</strong> (${{fmtUsd(c.cat_sitter || 0)}})</div>
                  </div>
                </div>

                <!-- 5 BOTONES DE RESERVA E INVESTIGACIÓN DIRECTA -->
                <div style="display:flex; flex-wrap:wrap; gap:6px;">
                  <a href="${{b.transport_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.72rem; padding:4px 9px; background:rgba(56,189,248,0.14); border:1px solid rgba(56,189,248,0.4); color:#7dd3fc; border-radius:6px; text-decoration:none;">
                    🚄 ${{b.transport_name || "Agendar Tren/Vuelo"}} ↗
                  </a>
                  <a href="${{b.activity_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.72rem; padding:4px 9px; background:rgba(244,114,182,0.14); border:1px solid rgba(244,114,182,0.4); color:#f9a8d4; border-radius:6px; text-decoration:none;">
                    🏯 ${{b.activity_name || "Agendar Actividad"}} ↗
                  </a>
                  <a href="${{b.dining_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.72rem; padding:4px 9px; background:rgba(245,158,11,0.14); border:1px solid rgba(245,158,11,0.4); color:#fcd34d; border-radius:6px; text-decoration:none;">
                    🥩 ${{b.dining_name || "Agendar Tabelog"}} ↗
                  </a>
                  ${{
                    b.hotel_url
                      ? `<a href="${{b.hotel_url}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.72rem; padding:4px 9px; background:rgba(167,139,250,0.14); border:1px solid rgba(167,139,250,0.4); color:#ddd6fe; border-radius:6px; text-decoration:none;">♨️ Agendar Ryokan/Hotel ↗</a>`
                      : ""
                  }}
                  <a href="${{b.maps_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.72rem; padding:4px 9px; background:rgba(34,197,94,0.14); border:1px solid rgba(34,197,94,0.4); color:#86efac; border-radius:6px; text-decoration:none;">
                    🗺️ Google Maps ↗
                  </a>
                </div>
              </div>
            </div>
          `;
        }})
        .join("");

      sec.innerHTML = `
        <h2 class="section-title">🗾 Códice Maestro: Las 24 Expediciones Mensuales y las 47 Prefecturas con あやめ (全国制覇 2027–2029)</h2>
        <p style="color:var(--text-muted); margin-bottom:1.1rem;">
          Itinerario completo mes a mes, horario por horario y ruta por ruta para conquistar las <strong>47 Prefecturas de Japón (<em>Zenkoku Seiha</em> / 全国制覇: #01 Tokio a #47 Yamanashi)</strong> en <strong>24 meses junto a あやめ</strong>, sincronizado con tu preparación en <strong>77 kg</strong>, tus <strong>6 combates invictos (6-0)</strong>, la creación artesanal de los atuendos de <strong>Godzilla 1954 &amp; Mothra 1961</strong> y tu transición a <strong>Capitán (O-3) en Okinawa</strong>.
        </p>

        <!-- PARTE I: LOGÍSTICA BASE, 3 ATAJOS DESDE IKEBUKURO Y PROTOCOLO DE GATITOS -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(310px, 1fr)); gap:14px; margin-bottom:18px;">
          <div style="background:#0d1117; border:1px solid #30363d; border-left:4px solid #38bdf8; border-radius:10px; padding:14px;">
            <div style="font-size:0.75rem; font-weight:800; color:#38bdf8; text-transform:uppercase; margin-bottom:6px;">
              🚄 Los 3 «Atajos» de Transporte desde Ikebukuro
            </div>
            <ul style="margin:0; padding-left:16px; font-size:0.78rem; color:#d1d5db; line-height:1.45;">
              <li style="margin-bottom:4px;"><strong>1. Norte y Mar de Japón (Tohoku, Hokkaido, Hokuriku, Nagano):</strong> JR Saikyo o Shonan-Shinjuku desde Ikebukuro hasta <strong>Omiya Station (24 min)</strong> y abordar ahí el Shinkansen sin bajar al centro.</li>
              <li style="margin-bottom:4px;"><strong>2. Oeste (Tokaido Shinkansen — Nagoya, Kioto, Osaka, Kobe, Hiroshima):</strong> Línea <strong>Tokyo Metro Marunouchi</strong> en Ikebukuro (origen de línea, asientos vacíos garantizados) → <strong>16 min exactos a Tokyo Station</strong>.</li>
              <li><strong>3. Destinos Aéreos (Hokkaido, Kyushu, Shikoku, Okinawa):</strong> <strong>Airport Limousine Bus</strong> en Sunshine City / Hotel Metropolitan Ikebukuro directo a la puerta de <strong>Haneda (45 min)</strong>.</li>
            </ul>
          </div>

          <div style="background:#0d1117; border:1px solid #30363d; border-left:4px solid #f472b6; border-radius:10px; padding:14px;">
            <div style="font-size:0.75rem; font-weight:800; color:#f472b6; text-transform:uppercase; margin-bottom:6px;">
              🐱 Protocolo de 3 Niveles para los Gatitos de あやめ
            </div>
            <ul style="margin:0; padding-left:16px; font-size:0.78rem; color:#d1d5db; line-height:1.45;">
              <li style="margin-bottom:4px;"><strong>🏠 Citas de 1 Día (M1, M2, M6, M12, M16):</strong> Alimentadores automáticos y regreso a dormir a casa en Ikebukuro con ellos (<strong>¥0 extra</strong>).</li>
              <li style="margin-bottom:4px;"><strong>♨️ Escapadas de 1 Noche / 30h (M3, M4, M5, M9, M14, M22, M23):</strong> Fuentes continuas de agua y monitoreo por cámara Wi-Fi + visita preventiva.</li>
              <li><strong>✈️ Viajes de 2 a 3 Noches (M7, M8, M10, M11, M13, M15, M17–M21, M24):</strong> <em>Cat Sitter</em> certificada en Tokio con reporte diario de fotos y videos por LINE para que あやめ viaje con cero preocupación.</li>
            </ul>
          </div>

          <div style="background:#0d1117; border:1px solid #30363d; border-left:4px solid #f0b90b; border-radius:10px; padding:14px;">
            <div style="font-size:0.75rem; font-weight:800; color:#f0b90b; text-transform:uppercase; margin-bottom:6px;">
              🥊 Regla del Conbini, Doble Llave y Presupuesto 47 Prefecturas
            </div>
            <ul style="margin:0; padding-left:16px; font-size:0.78rem; color:#d1d5db; line-height:1.45;">
              <li style="margin-bottom:4px;"><strong>🏍️ Honda CBR + YOKKAO &amp; Venum Tricolor:</strong> Traslado diario en minutos al gimnasio y equipo oficial en blanco, rojo y azul rey.</li>
              <li style="margin-bottom:4px;"><strong>🔐 Doble Llave Antirretadores:</strong> Ningún combate extra se acepta sin aprobación unánime de tu <strong>Entrenador en Jefe</strong> y la <strong>Mánager あやめ</strong>.</li>
              <li><strong>💰 Inversión Total 24 Expediciones (47 Prefecturas):</strong> <strong>${{fmtJpy(grandTotalJpy)}} JPY</strong> (<strong style="color:#4ade80;">⚡ ${{fmtUsd(grandTotalJpy)}} USD hoy</strong> · Promedio ${{fmtUsd(grandTotalJpy / 24)}}/mes).</li>
            </ul>
          </div>
        </div>

        <!-- TABLERO INTERACTIVO DE SELLOS DE LAS 47 PREFECTURAS (ZENKOKU SEIHA) -->
        <div style="background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:18px; margin-bottom:20px;">
          <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:10px; margin-bottom:10px;">
            <div>
              <span style="color:#fff; font-weight:800; font-size:1rem;">🏆 Pasaporte Nacional de las 47 Prefecturas (全国制覇 47/47 Stamp Rally)</span>
              <div style="font-size:0.78rem; color:#9ca3af; margin-top:2px;">
                Marca cada mes como completado para iluminar las prefecturas conquistadas junto a あやめ (o haz clic en cualquier prefectura para saltar a su mes).
              </div>
            </div>
            <div style="text-align:right;">
              <div style="font-size:0.9rem; color:#4ade80; font-weight:800;">
                ✅ ${{conqueredPrefsCount}} / 47 Prefecturas (${{pct47}}%) · 🗓️ ${{conqueredMonthsCount}} / 24 Meses
              </div>
              <div style="font-size:0.75rem; color:#d1d5db;">
                Presupuesto Ejecutado: <strong>${{fmtJpy(spentJpy)}}</strong> (${{fmtUsd(spentJpy)}}) de <strong>${{fmtJpy(grandTotalJpy)}}</strong> (⚡ ${{fmtUsd(grandTotalJpy)}} USD)
              </div>
            </div>
          </div>

          <div style="width:100%; height:11px; background:#161b22; border-radius:999px; overflow:hidden; margin-bottom:14px; border:1px solid #30363d;">
            <div style="width:${{pct47}}%; height:100%; background:linear-gradient(90deg, #22c55e, #f0b90b); transition:width 0.35s ease;"></div>
          </div>

          <!-- 47 PÍLDORAS DE PREFECTURAS (#01 A #47) -->
          <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:14px; max-height:${{showAll47Pills ? "none" : "115px"}}; overflow:hidden;">
            ${{stampBadgesHtml}}
          </div>
          <div style="margin-bottom:12px;">
            <button id="btn-toggle-47-pills" class="plan-tab" style="font-size:0.72rem; cursor:pointer;">
              ${{showAll47Pills ? "🔼 Compactar Lista de 47 Prefecturas" : "🔽 Ver / Expandir las 47 Prefecturas Completas (#01 Tokio → #47 Yamanashi)"}}
            </button>
          </div>

          <!-- FILTROS POR FASE, SEMÁFORO, REGIÓN Y BUSCADOR -->
          <div style="display:flex; flex-direction:column; gap:10px; padding-top:12px; border-top:1px solid #21262d;">
            <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
              <span style="font-size:0.74rem; color:#9ca3af; font-weight:700; margin-right:4px;">🍁 Fases:</span>
              <button class="plan-tab z47-phase-btn ${{activePhase === "all" ? "active" : ""}}" data-phase="all">Todas las 4 Fases (24 Meses)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "1" ? "active" : ""}}" data-phase="1">Fase 1: M01–M06 (Despertar &amp; Debut)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "2" ? "active" : ""}}" data-phase="2">Fase 2: M07–M12 (Peleas #1 y #2)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "3" ? "active" : ""}}" data-phase="3">Fase 3: M13–M18 (DEEP #3/#4 &amp; Kyushu)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "4" ? "active" : ""}}" data-phase="4">Fase 4: M19–M24 (Peleas #5/#6 &amp; Gala)</button>
            </div>

            <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px;">
              <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
                <span style="font-size:0.74rem; color:#9ca3af; font-weight:700; margin-right:4px;">🚦 Semáforo:</span>
                <button class="plan-tab z47-zone-btn ${{activeZone === "all" ? "active" : ""}}" data-zone="all">Todas (24)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "yellow" ? "active" : ""}}" data-zone="yellow" style="border-color:#d29922; color:#fde68a;">🟡 Off-Camp 79 kg (8)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "red" ? "active" : ""}}" data-zone="red" style="border-color:#f85149; color:#fca5a5;">🔴 Fight Camp 77 kg (4)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "green" ? "active" : ""}}" data-zone="green" style="border-color:#2ea043; color:#86efac;">🟢 Bono Post-Pelea (11)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "gold" ? "active" : ""}}" data-zone="gold" style="border-color:#f0b90b; color:#fef08a;">👑 Gala 6-0 (1)</button>
              </div>

              <input
                id="z47-search-input"
                type="search"
                value="${{searchQuery.replace(/"/g, "&quot;")}}"
                placeholder="🔍 Buscar prefectura (#01-#47), ciudad, Wagyu, tela, tren..."
                style="background:#161b22; border:1px solid #30363d; color:#fff; padding:6px 12px; border-radius:8px; min-width:270px; font-size:0.8rem;"
              >
            </div>

            <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
              <span style="font-size:0.74rem; color:#9ca3af; font-weight:700; margin-right:4px;">🗾 Región:</span>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "all" ? "active" : ""}}" data-reg="all">8 Regiones (47/47)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "kanto" ? "active" : ""}}" data-reg="kanto">1. Kanto (7)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "tohoku" ? "active" : ""}}" data-reg="tohoku">2. Tohoku (6)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "hokkaido" ? "active" : ""}}" data-reg="hokkaido">3. Hokkaido (1)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "chubu" ? "active" : ""}}" data-reg="chubu">4. Chubu &amp; Hokuriku (9)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "kansai" ? "active" : ""}}" data-reg="kansai">5. Kansai (7)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "chugoku" ? "active" : ""}}" data-reg="chugoku">6. Chugoku (5)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "shikoku" ? "active" : ""}}" data-reg="shikoku">7. Shikoku (4)</button>
              <button class="plan-tab z47-reg-btn ${{activeRegion === "kyushu" ? "active" : ""}}" data-reg="kyushu">8. Kyushu &amp; Okinawa (8)</button>
            </div>
          </div>
        </div>

        <!-- GRID DE LAS 24 EXPEDICIONES MENSUALES DETALLADAS -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(440px, 1fr)); gap:18px;">
          ${{cardsHtml}}
        </div>
      `;

      // Bind interactive events
      const toggleBtn = document.getElementById("btn-toggle-47-pills");
      if (toggleBtn) {{
        toggleBtn.onclick = () => {{
          showAll47Pills = !showAll47Pills;
          renderHub();
        }};
      }}

      sec.querySelectorAll("[data-jump-month]").forEach((badge) => {{
        badge.onclick = () => {{
          const mId = badge.getAttribute("data-jump-month");
          activePhase = "all";
          activeZone = "all";
          activeRegion = "all";
          searchQuery = "";
          renderHub();
          const targetCard = document.getElementById("card-" + mId);
          if (targetCard) {{
            targetCard.scrollIntoView({{ behavior: "smooth", block: "center" }});
            targetCard.style.boxShadow = "0 0 0 3px #f0b90b, 0 12px 32px rgba(240,185,11,0.4)";
          }}
        }};
      }});

      sec.querySelectorAll("input[data-check-month]").forEach((cb) => {{
        cb.onchange = (e) => {{
          const id = cb.getAttribute("data-check-month");
          if (e.target.checked) savedMonths[id] = true;
          else delete savedMonths[id];
          localStorage.setItem("imperio_zenkoku_47_months_v1", JSON.stringify(savedMonths));
          renderHub();
        }};
      }});

      sec.querySelectorAll(".z47-phase-btn").forEach((btn) => {{
        btn.onclick = () => {{
          activePhase = btn.getAttribute("data-phase");
          renderHub();
        }};
      }});

      sec.querySelectorAll(".z47-zone-btn").forEach((btn) => {{
        btn.onclick = () => {{
          activeZone = btn.getAttribute("data-zone");
          renderHub();
        }};
      }});

      sec.querySelectorAll(".z47-reg-btn").forEach((btn) => {{
        btn.onclick = () => {{
          activeRegion = btn.getAttribute("data-reg");
          renderHub();
        }};
      }});

      const searchEl = document.getElementById("z47-search-input");
      if (searchEl) {{
        searchEl.oninput = (e) => {{
          searchQuery = e.target.value || "";
          const pos = searchEl.selectionStart;
          renderHub();
          const nextInput = document.getElementById("z47-search-input");
          if (nextInput) {{
            nextInput.focus();
            try {{
              nextInput.setSelectionRange(pos, pos);
            }} catch (_) {{}}
          }}
        }};
      }}
    }}

    window.renderZenkoku47Hub = renderHub;
    window.onImperioRatesUpdated = function () {{
      renderHub();
    }};

    renderHub();
  }}

  // =========================================================================
  // MODULE 3: CRONÓMETROS TÁCTICOS EN TIEMPO REAL (#imperio-live-countdowns)
  // =========================================================================
  function initImperioCountdowns() {{
    const targets = [
      {{ id: "cd-oct-2027", iso: "2027-10-01T00:00:00+09:00" }},
      {{ id: "cd-apr-2028", iso: "2028-04-15T18:00:00+09:00" }},
      {{ id: "cd-sep-2029", iso: "2029-09-15T19:00:00+09:00" }},
      {{ id: "cd-oct-2029", iso: "2029-10-01T09:00:00+09:00" }}
    ];

    function tick() {{
      const now = Date.now();
      targets.forEach((t) => {{
        const el = document.getElementById(t.id);
        if (!el) return;
        const diff = new Date(t.iso).getTime() - now;
        if (diff <= 0) {{
          el.textContent = "🔥 ¡EN CURSO / CONQUISTADO!";
          return;
        }}
        const days = Math.floor(diff / 86400000);
        const hours = Math.floor((diff % 86400000) / 3600000);
        const mins = Math.floor((diff % 3600000) / 60000);
        const secs = Math.floor((diff % 60000) / 1000);
        el.textContent = `${{days}}d ${{String(hours).padStart(2, "0")}}h ${{String(mins).padStart(2, "0")}}m ${{String(secs).padStart(2, "0")}}s`;
      }});
    }}

    tick();
    setInterval(tick, 1000);
  }}

  async function bootAll() {{
    initAyameRadar();
    initZenkokuSeiha47Hub();
    initImperioCountdowns();
    await refreshLiveApis();
    if (typeof window.renderZenkoku47Hub === "function") {{
      window.renderZenkoku47Hub();
    }}
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", bootAll);
  }} else {{
    bootAll();
  }}
}})();
"""

    OUT_JS_PATH.write_text(js_code, encoding="utf-8")
    print(f"[OK] Built upgraded assets/ayame-events-api.js ({len(js_code):,} bytes)")


if __name__ == "__main__":
    main()
