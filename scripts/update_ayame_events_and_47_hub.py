#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the upgraded assets/ayame-events-api.js (v6.0) combining:
1. Real-Time Ikebukuro + Tokyo + 8 Regions Event & Weather Radar (#ayame-radar-hub)
2. Full 24-Month / 47-Prefecture (Zenkoku Seiha 全国制覇) Interactive Itinerary,
   Step-by-Step Arrival Blueprint (Train/Shinkansen/Airport),
   National Geisha (Hanamachi / Geigi / Maiko / Ozashiki) Atlas,
   YouTube & Kick IRL Video Production Plan (+$15,000+/mo target),
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
 * Atlas del Imperio — Motor Multi-API en Tiempo Real para あやめ (v6.0)
 * 1. Radar de Eventos, Lugares y Clima en Ikebukuro, Tokio y Japón (#ayame-radar-hub)
 * 2. Códice Maestro de 24 Meses, 47 Prefecturas (Zenkoku Seiha 全国制覇),
 *    Mapeo Desde Bajar del Tren/Aeropuerto, Ruta Nacional de Geishas (Hanamachi)
 *    y Plan de Rodaje YouTube + Kick IRL (#ayame-24-expediciones)
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

  let liveRateJpy = INITIAL_FEED.usd_jpy_rate || (INITIAL_47_FEED.meta && INITIAL_47_FEED.meta.fx_rates && INITIAL_47_FEED.meta.fx_rates.JPY) || 158.08;
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
    return "¥" + Math.round(n || 0).toLocaleString("en-US");
  }}

  function fmtUsd(jpy) {{
    return "$" + Math.round((jpy || 0) / getActiveRate()).toLocaleString("en-US");
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
      const months = pref47Data.months_24 || pref47Data.itinerary_24_months || [];
      if (months.length > 0) {{
        const lats = months
          .map((m) => (m.prefectures && m.prefectures[0] ? m.prefectures[0].lat : 35.7295))
          .join(",");
        const lons = months
          .map((m) => (m.prefectures && m.prefectures[0] ? m.prefectures[0].lon : 139.7109))
          .join(",");
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
    const root = document.getElementById("ayame-radar-hub") || document.getElementById("ayame-radar-container");
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
  // MODULE 2: EL GRAN ITINERARIO DE 24 MESES, 47 PREFECTURAS, GEISHAS & YOUTUBE/KICK (#ayame-24-expediciones)
  // =========================================================================
  function initZenkokuSeiha47Hub() {{
    const sec = document.getElementById("ayame-24-expediciones");
    if (!sec) return;

    const savedMonths = JSON.parse(localStorage.getItem("imperio_zenkoku_47_months_v1") || "{{}}");
    let activePhase = "all";
    let activeZone = "all";
    let activeRegion = "all";
    let searchQuery = "";
    let showAll47Pills = true;
    let showGeishaAtlas = false;

    const ZONE_MAP = {{
      AMARILLA: "yellow",
      ROJA: "red",
      VERDE: "green",
      DORADA: "gold",
      yellow: "yellow",
      red: "red",
      green: "green",
      gold: "gold"
    }};

    function normalizeMonth(m) {{
      const mId = m.id || "mes-" + String(m.month_num).padStart(2, "0");
      const zColor = ZONE_MAP[m.zone_code] || ZONE_MAP[m.zone_color] || "yellow";
      let phaseNum = "1";
      if (m.month_num >= 1 && m.month_num <= 6) phaseNum = "1";
      else if (m.month_num >= 7 && m.month_num <= 12) phaseNum = "2";
      else if (m.month_num >= 13 && m.month_num <= 18) phaseNum = "3";
      else phaseNum = "4";

      const prefs = Array.isArray(m.prefectures) ? m.prefectures : [];
      const regionsSet = new Set();
      prefs.forEach((p) => {{
        const r = (p.region || "").toLowerCase();
        if (r.includes("kanto")) regionsSet.add("kanto");
        if (r.includes("tohoku")) regionsSet.add("tohoku");
        if (r.includes("hokkaido")) regionsSet.add("hokkaido");
        if (r.includes("chubu") || r.includes("hokuriku")) regionsSet.add("chubu");
        if (r.includes("kansai")) regionsSet.add("kansai");
        if (r.includes("chugoku")) regionsSet.add("chugoku");
        if (r.includes("shikoku")) regionsSet.add("shikoku");
        if (r.includes("kyushu") || r.includes("okinawa")) regionsSet.add("kyushu");
      }});
      if (regionsSet.size === 0) {{
        regionsSet.add("kanto");
      }}

      return {{
        raw: m,
        id: mId,
        month_num: m.month_num,
        date_label: m.date_label || "",
        title: m.title || `Mes ${{String(m.month_num).padStart(2, "0")}} (${{m.date_label}})`,
        phaseNum: phaseNum,
        zone_color: zColor,
        zone_badge: m.zone_badge || "",
        duration: m.duration || "",
        shortcut: m.shortcut || m.ikebukuro_shortcut || "",
        cat_protocol: m.cat_protocol || "",
        fight_sync: m.fight_sync || m.zone_badge || "",
        arrival_blueprint: m.arrival_blueprint || "",
        geisha_experience: m.geisha_experience || "",
        geisha_url: m.geisha_url || "https://www.japan.travel/en/",
        geisha_label: m.geisha_label || "🏮 Guía Hanamachi & Cultura",
        video_production_plan: m.video_production_plan || "",
        nutrition_bruno: m.nutrition_bruno || m.nutrition_77kg || "",
        antojo_ayame: m.antojo_ayame || m.ayame_treat || "",
        prefectures: prefs,
        regions: Array.from(regionsSet),
        schedule: Array.isArray(m.schedule) ? m.schedule : [],
        costs_jpy: m.costs_jpy || {{}},
        booking_angles: m.booking_angles || m.booking_links || {{}},
        total_jpy: m.total_jpy || 0
      }};
    }}

    // Collect all 47 prefectures in order #01 to #47
    const all47List = (pref47Data.prefectures_47 || []).map((p) => ({{
      num: p.num,
      code: "#" + String(p.num).padStart(2, "0"),
      name: p.name,
      kanji: p.kanji || "",
      region: p.region || "",
      activity: p.activity || "",
      label: `#${{String(p.num).padStart(2, "0")}} ${{p.name}} (${{p.kanji || ""}})`,
      monthNum: p.month_num,
      monthId: "mes-" + String(p.month_num).padStart(2, "0"),
      dateLabel: p.date_label || ""
    }}));
    all47List.sort((a, b) => a.num - b.num);

    const geishaAtlas = pref47Data.geisha_districts_atlas || [];

    function renderHub() {{
      const rawMonths = pref47Data.months_24 || pref47Data.itinerary_24_months || [];
      const months = rawMonths.map(normalizeMonth);
      const grandTotalJpy =
        (pref47Data.meta && pref47Data.meta.total_campaign_jpy) ||
        (pref47Data.summary && pref47Data.summary.grand_total_jpy) ||
        5594200;

      // Calculate conquered counts
      let conqueredMonthsCount = 0;
      const conqueredPrefsNums = new Set();
      let spentJpy = 0;

      months.forEach((m) => {{
        if (savedMonths[m.id]) {{
          conqueredMonthsCount++;
          spentJpy += m.total_jpy || 0;
          m.prefectures.forEach((p) => conqueredPrefsNums.add(p.num));
        }}
      }});

      const conqueredPrefsCount = conqueredPrefsNums.size;
      const pct47 = Math.round((conqueredPrefsCount / 47) * 100);

      // Filter months
      const q = searchQuery.trim().toLowerCase();
      const filteredMonths = months.filter((m) => {{
        if (activePhase !== "all" && m.phaseNum !== activePhase) return false;
        if (activeZone !== "all" && m.zone_color !== activeZone) return false;
        if (activeRegion !== "all" && !m.regions.includes(activeRegion)) return false;
        if (!q) return true;

        const prefText = m.prefectures
          .map((p) => `#${{String(p.num).padStart(2, "0")}} ${{p.name}} ${{p.kanji}} ${{p.region}} ${{p.activity}}`)
          .join(" ");
        const schedText = m.schedule
          .map((s) => (typeof s === "string" ? s : `${{s.time || ""}} ${{s.detail || ""}}`))
          .join(" ");

        const hay = [
          m.title,
          m.date_label,
          m.zone_badge,
          m.shortcut,
          m.cat_protocol,
          m.fight_sync,
          m.arrival_blueprint,
          m.geisha_experience,
          m.video_production_plan,
          m.nutrition_bruno,
          m.antojo_ayame,
          prefText,
          schedText
        ]
          .join(" ")
          .toLowerCase();
        return hay.includes(q);
      }});

      // Build 47 Prefecture Stamp Rally badges
      const stampBadgesHtml = all47List
        .map((p) => {{
          const isConquered = conqueredPrefsNums.has(p.num);
          return `
            <span
              data-jump-month="${{p.monthId}}"
              title="Mes ${{String(p.monthNum).padStart(2, "0")}} (${{p.dateLabel}}): ${{p.activity}} — Clic para saltar a su tarjeta"
              style="cursor:pointer; padding:4px 10px; border-radius:999px; font-size:0.72rem; font-weight:700; transition:all 0.15s; border:1px solid ${{
                isConquered ? "#22c55e" : "rgba(240,185,11,0.32)"
              }}; background:${{
                isConquered ? "rgba(34,197,94,0.22)" : "rgba(15,23,42,0.85)"
              }}; color:${{isConquered ? "#4ade80" : "#e2e8f0"}};"
            >
              ${{isConquered ? "✅ " : "🗾 "}}<strong style="color:#f0b90b;">${{p.code}}</strong> ${{p.name}} <small style="color:#94a3b8;">(${{p.kanji}} · M${{String(p.monthNum).padStart(2, "0")}})</small>
            </span>
          `;
        }})
        .join("");

      // Build Geisha Districts Atlas cards
      const geishaAtlasHtml = geishaAtlas
        .map((g) => {{
          const mId = "mes-" + String(g.month_num).padStart(2, "0");
          return `
            <div style="background:#111827; border:1px solid rgba(244,114,182,0.32); border-left:3px solid #f472b6; border-radius:9px; padding:10px 12px; display:flex; flex-direction:column; justify-content:space-between; gap:6px;">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:center; gap:6px; margin-bottom:3px;">
                  <span style="font-size:0.68rem; font-weight:800; color:#f9a8d4; text-transform:uppercase;">Mes ${{String(g.month_num).padStart(2, "0")}} · ${{g.city}}</span>
                  <button data-jump-month="${{mId}}" style="background:rgba(240,185,11,0.16); border:1px solid #f0b90b; color:#fef08a; border-radius:5px; padding:1px 7px; font-size:0.67rem; font-weight:700; cursor:pointer;">Ir al Mes ↘</button>
                </div>
                <div style="font-size:0.8rem; font-weight:800; color:#fff; margin-bottom:4px;">👘 ${{g.name}}</div>
                <div style="font-size:0.73rem; color:#cbd5e1; line-height:1.4;">${{g.highlight}}</div>
              </div>
              <div>
                <a href="${{g.url}}" target="_blank" rel="noopener" style="font-size:0.7rem; color:#7dd3fc; text-decoration:none; font-weight:700;">🔗 Sitio Oficial / Reserva ↗</a>
              </div>
            </div>
          `;
        }})
        .join("");

      const zoneColors = {{
        yellow: {{ border: "#d29922", bg: "rgba(210,153,34,0.14)", text: "#fde68a" }},
        red: {{ border: "#f85149", bg: "rgba(248,81,73,0.14)", text: "#fca5a5" }},
        green: {{ border: "#2ea043", bg: "rgba(46,160,67,0.14)", text: "#86efac" }},
        gold: {{ border: "#f0b90b", bg: "rgba(240,185,11,0.18)", text: "#fef08a" }}
      }};

      const cardsHtml =
        filteredMonths.length === 0
          ? `<div style="grid-column:1/-1; background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:28px; text-align:center; color:#cbd5e1;">
               No se encontraron meses con ese filtro. <button id="btn-reset-z47-filters" class="plan-tab active" style="margin-left:10px; cursor:pointer;">🔄 Mostrar los 24 Meses y 47 Prefecturas</button>
             </div>`
          : filteredMonths
              .map((m) => {{
                const zc = zoneColors[m.zone_color] || zoneColors.yellow;
                const isDone = !!savedMonths[m.id];
                const w = monthWeatherMap[m.month_num];
                const weatherPill = w
                  ? `<span style="background:rgba(56,189,248,0.14); border:1px solid rgba(56,189,248,0.35); color:#7dd3fc; padding:2px 8px; border-radius:999px; font-size:0.7rem; font-weight:700;">🌡️ Clima Hoy: ${{w.temp_c}}°C · 💧 ${{w.humidity}}%</span>`
                  : `<span style="background:rgba(56,189,248,0.1); border:1px solid rgba(56,189,248,0.25); color:#7dd3fc; padding:2px 8px; border-radius:999px; font-size:0.7rem;">🛰️ Open-Meteo Ready</span>`;

                const prefsPills =
                  m.prefectures.length > 0
                    ? m.prefectures
                        .map(
                          (p) =>
                            `<span style="background:rgba(240,185,11,0.16); border:1px solid #f0b90b; color:#fef08a; padding:3px 9px; border-radius:6px; font-size:0.73rem; font-weight:800;" title="${{p.activity}}">🗾 #${{String(p.num).padStart(2, "0")}} ${{p.name}} (${{p.kanji}}) · ${{p.region}}</span>`
                        )
                        .join("")
                    : `<span style="background:rgba(148,163,184,0.14); border:1px solid rgba(148,163,184,0.35); color:#e2e8f0; padding:3px 9px; border-radius:6px; font-size:0.72rem; font-weight:700;">🏟️ Sede Base Tokio (Ikebukuro / Ginza / Korakuen / Bahía)</span>`;

                const prefActivitiesHtml =
                  m.prefectures.length > 0
                    ? `<div style="margin-bottom:10px; display:flex; flex-direction:column; gap:4px;">` +
                      m.prefectures
                        .map(
                          (p) =>
                            `<div style="font-size:0.75rem; color:#fde68a; background:rgba(240,185,11,0.07); border-left:3px solid #f0b90b; padding:4px 8px; border-radius:4px;">✨ <strong>#${{String(p.num).padStart(2, "0")}} ${{p.name}}:</strong> <span style="color:#f8fafc;">${{p.activity}}</span></div>`
                        )
                        .join("") +
                      `</div>`
                    : "";

                const scheduleHtml = m.schedule
                  .map((s) => {{
                    if (typeof s === "string") {{
                      return `<li style="margin-bottom:6px; color:#e5e7eb; font-size:0.79rem; line-height:1.45;">${{s}}</li>`;
                    }}
                    return `<li style="margin-bottom:6px; color:#e5e7eb; font-size:0.79rem; line-height:1.45;"><strong style="color:#f0b90b;">${{s.time}}:</strong> ${{s.detail}}</li>`;
                  }})
                  .join("");

                const c = m.costs_jpy || {{}};
                const b = m.booking_angles || {{}};
                const tot = Math.max(1, m.total_jpy || 1);
                const pTr = (((c.transporte || 0) / tot) * 100).toFixed(1);
                const pHo = (((c.hospedaje || 0) / tot) * 100).toFixed(1);
                const pAc = (((c.actividades_telas || 0) / tot) * 100).toFixed(1);
                const pGa = (((c.gastronomia || 0) / tot) * 100).toFixed(1);
                const pCs = (((c.cat_sitter || 0) / tot) * 100).toFixed(1);

                return `
                  <div id="card-${{m.id}}" class="exp-47-card" style="background:linear-gradient(180deg, #0f172a 0%, #090d16 100%); border:1px solid ${{
                    isDone ? "#10b981" : "rgba(148,163,184,0.22)"
                  }}; border-top:4px solid ${{zc.border}}; border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:${{
                    isDone ? "0 0 0 2px rgba(16,185,129,0.35), 0 12px 28px rgba(0,0,0,0.5)" : "0 10px 26px rgba(0,0,0,0.4)"
                  }}; font-variant-numeric:tabular-nums;">
                    <div>
                      <!-- ENCABEZADO DEL MES -->
                      <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px;">
                        <div style="display:flex; flex-wrap:wrap; align-items:center; gap:6px;">
                          <span style="background:${{zc.bg}}; border:1px solid ${{zc.border}}; color:${{zc.text}}; padding:2px 9px; border-radius:6px; font-size:0.7rem; font-weight:800; font-family:ui-monospace,monospace;">
                            API /mes-${{String(m.month_num).padStart(2, "0")}} • ${{m.date_label.toUpperCase()}}
                          </span>
                          <span style="font-size:0.72rem; color:#cbd5e1; font-weight:700;">${{m.zone_badge}}</span>
                          ${{weatherPill}}
                        </div>
                        <label style="display:inline-flex; align-items:center; gap:6px; background:${{
                          isDone ? "rgba(16,185,129,0.2)" : "rgba(255,255,255,0.05)"
                        }}; border:1px solid ${{
                          isDone ? "#10b981" : "rgba(148,163,184,0.25)"
                        }}; color:${{
                          isDone ? "#34d399" : "#cbd5e1"
                        }}; padding:3px 10px; border-radius:8px; font-size:0.73rem; font-weight:700; cursor:pointer;">
                          <input type="checkbox" data-check-month="${{m.id}}" ${{isDone ? "checked" : ""}} style="cursor:pointer;">
                          ${{isDone ? "✅ Sellado" : "Sellar Mes"}}
                        </label>
                      </div>

                      <!-- TÍTULO Y PREFECTURAS -->
                      <h3 style="color:#f8fafc; font-size:1.05rem; font-weight:800; margin:6px 0 8px; line-height:1.35;">${{m.title}}</h3>
                      <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:8px;">
                        ${{prefsPills}}
                        <span style="background:rgba(167,139,250,0.12); border:1px solid rgba(167,139,250,0.32); color:#ddd6fe; padding:3px 8px; border-radius:6px; font-size:0.7rem; font-weight:600;">
                          ⏱️ ${{m.duration}}
                        </span>
                      </div>
                      ${{prefActivitiesHtml}}

                      <!-- 1. LOGÍSTICA DESDE IKEBUKURO + PROTOCOLO GATITOS + MMA -->
                      <div style="background:rgba(15,23,42,0.82); border:1px solid rgba(148,163,184,0.18); border-radius:9px; padding:10px 12px; margin-bottom:10px; font-size:0.75rem; line-height:1.45;">
                        <div style="margin-bottom:4px; color:#7dd3fc;">🚀 <strong>Atajo desde Ikebukuro:</strong> <span style="color:#f1f5f9;">${{m.shortcut}}</span></div>
                        <div style="margin-bottom:4px; color:#f9a8d4;">🐱 <strong>Protocolo 2 Gatitos y 2 Chinchillas:</strong> <span style="color:#f1f5f9;">${{m.cat_protocol}}</span></div>
                        <div style="color:#fde047;">🥊 <strong>Sincronía Campaña 6-0 (77 kg):</strong> <span style="color:#f1f5f9;">${{m.fight_sync}}</span></div>
                      </div>

                      <!-- 2. MAPEO REAL PASO A PASO DESDE BAJAR DEL TREN / SHINKANSEN / AEROPUERTO -->
                      ${{
                        m.arrival_blueprint
                          ? `<div style="background:rgba(56,189,248,0.08); border:1px solid rgba(56,189,248,0.3); border-left:3px solid #38bdf8; border-radius:8px; padding:9px 11px; margin-bottom:10px; font-size:0.75rem; color:#e0f2fe; line-height:1.45;">
                               ${{m.arrival_blueprint}}
                             </div>`
                          : ""
                      }}

                      <!-- 3. MAPEO DE GEISHAS (HANAMACHI / GEIGI / MAIKO) & CULTURA EXCLUSIVA -->
                      ${{
                        m.geisha_experience
                          ? `<div style="background:rgba(244,114,182,0.09); border:1px solid rgba(244,114,182,0.34); border-left:3px solid #f472b6; border-radius:8px; padding:9px 11px; margin-bottom:10px; font-size:0.75rem; color:#fce7f3; line-height:1.45;">
                               ${{m.geisha_experience}}
                             </div>`
                          : ""
                      }}

                      <!-- 4. ITINERARIO HORARIO POR HORARIO / DÍA POR DÍA -->
                      <div style="margin-bottom:10px; background:rgba(0,0,0,0.28); border:1px solid rgba(255,255,255,0.07); border-radius:8px; padding:10px 12px;">
                        <div style="font-size:0.71rem; font-weight:800; color:#f0b90b; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:6px;">
                          📋 Itinerario Táctico Horario por Horario:
                        </div>
                        <ul style="margin:0; padding-left:18px;">
                          ${{scheduleHtml}}
                        </ul>
                      </div>

                      <!-- 5. ÁNGULO DE RODAJE YOUTUBE & KICK IRL (+15K USD/MES) -->
                      ${{
                        m.video_production_plan
                          ? `<div style="background:rgba(168,85,247,0.09); border:1px solid rgba(168,85,247,0.34); border-left:3px solid #a855f7; border-radius:8px; padding:9px 11px; margin-bottom:10px; font-size:0.74rem; color:#f3e8ff; line-height:1.45;">
                               ${{m.video_production_plan}}
                             </div>`
                          : ""
                      }}

                      <!-- 6. NUTRICIÓN 77 KG & MIMO PARA AYAME -->
                      <div style="background:rgba(16,185,129,0.07); border:1px solid rgba(16,185,129,0.24); border-radius:9px; padding:9px 11px; margin-bottom:12px; font-size:0.74rem; line-height:1.45;">
                        <div style="margin-bottom:4px; color:#6ee7b7;">🥩 <strong>Nutrición Hiper-Carnívora Bruno (0 Alcohol 🚫🍺):</strong> <span style="color:#ecfdf5;">${{m.nutrition_bruno}}</span></div>
                        <div style="color:#fbcfe8;">🌸 <strong>Antojo &amp; Arte Textil de あやめ (0 Mango 🚫🥭):</strong> <span style="color:#fdf2f8;">${{m.antojo_ayame}}</span></div>
                      </div>
                    </div>

                    <!-- DESGLOSE FINANCIERO MULTI-ÁNGULO + BARRA PROPORCIONAL + RESERVA 1-CLICK -->
                    <div>
                      <div style="background:rgba(15,23,42,0.9); border:1px solid rgba(148,163,184,0.18); border-radius:10px; padding:11px; margin-bottom:10px;">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px; margin-bottom:6px;">
                          <span style="font-size:0.7rem; font-weight:700; color:#94a3b8; text-transform:uppercase; letter-spacing:0.04em;">💰 Telemetría de Costos (5 Rubros)</span>
                          <div>
                            <span style="font-size:0.98rem; font-weight:800; color:#f8fafc;">${{fmtJpy(m.total_jpy)}} JPY</span>
                            <span style="font-size:0.78rem; font-weight:800; color:#34d399; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.38); padding:2px 7px; border-radius:5px; margin-left:5px;">
                              ⚡ ${{fmtUsd(m.total_jpy)}} USD
                            </span>
                          </div>
                        </div>
                        <div style="display:flex; width:100%; height:6px; border-radius:999px; overflow:hidden; background:#090d16; margin-bottom:8px;">
                          <div style="width:${{pTr}}%; background:#38bdf8;" title="Transporte: ${{pTr}}%"></div>
                          <div style="width:${{pHo}}%; background:#a78bfa;" title="Hospedaje: ${{pHo}}%"></div>
                          <div style="width:${{pAc}}%; background:#f472b6;" title="Actividades & Telas: ${{pAc}}%"></div>
                          <div style="width:${{pGa}}%; background:#f59e0b;" title="Gastronomía: ${{pGa}}%"></div>
                          <div style="width:${{pCs}}%; background:#22c55e;" title="Cat Sitter: ${{pCs}}%"></div>
                        </div>
                        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(115px, 1fr)); gap:6px; font-size:0.69rem; color:#cbd5e1;">
                          <div><span style="color:#38bdf8;">●</span> Transp: <strong>${{fmtJpy(c.transporte || 0)}}</strong> (${{fmtUsd(c.transporte || 0)}})</div>
                          <div><span style="color:#a78bfa;">●</span> Hotel: <strong>${{fmtJpy(c.hospedaje || 0)}}</strong> (${{fmtUsd(c.hospedaje || 0)}})</div>
                          <div><span style="color:#f472b6;">●</span> Telas/Act: <strong>${{fmtJpy(c.actividades_telas || 0)}}</strong> (${{fmtUsd(c.actividades_telas || 0)}})</div>
                          <div><span style="color:#f59e0b;">●</span> Comida: <strong>${{fmtJpy(c.gastronomia || 0)}}</strong> (${{fmtUsd(c.gastronomia || 0)}})</div>
                          <div><span style="color:#22c55e;">●</span> Sitter: <strong>${{fmtJpy(c.cat_sitter || 0)}}</strong> (${{fmtUsd(c.cat_sitter || 0)}})</div>
                        </div>
                      </div>

                      <!-- 6 BOTONES DE RESERVA E INVESTIGACIÓN DIRECTA -->
                      <div style="display:flex; flex-wrap:wrap; gap:6px;">
                        <a href="${{b.transport_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(56,189,248,0.14); border:1px solid rgba(56,189,248,0.4); color:#7dd3fc; border-radius:6px; text-decoration:none;">
                          ${{b.transport_label || b.transport_name || "🚄 Agendar Tren/Vuelo"}} ↗
                        </a>
                        <a href="${{b.activity_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(244,114,182,0.14); border:1px solid rgba(244,114,182,0.4); color:#f9a8d4; border-radius:6px; text-decoration:none;">
                          ${{b.activity_label || b.activity_name || "🏯 Agendar Actividad"}} ↗
                        </a>
                        <a href="${{m.geisha_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(236,72,153,0.16); border:1px solid rgba(236,72,153,0.45); color:#fbcfe8; border-radius:6px; text-decoration:none;">
                          ${{m.geisha_label || "👘 Distrito Geishas / Cultura"}} ↗
                        </a>
                        <a href="${{b.dining_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(245,158,11,0.14); border:1px solid rgba(245,158,11,0.4); color:#fcd34d; border-radius:6px; text-decoration:none;">
                          ${{b.dining_label || b.dining_name || "🥩 Agendar Tabelog"}} ↗
                        </a>
                        ${{
                          b.hotel_url
                            ? `<a href="${{b.hotel_url}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(167,139,250,0.14); border:1px solid rgba(167,139,250,0.4); color:#ddd6fe; border-radius:6px; text-decoration:none;">${{b.hotel_label || "♨️ Agendar Ryokan/Hotel"}} ↗</a>`
                            : ""
                        }}
                        <a href="${{b.maps_url || "#"}}" target="_blank" rel="noopener" class="btn-link" style="font-size:0.71rem; padding:4px 9px; background:rgba(34,197,94,0.14); border:1px solid rgba(34,197,94,0.4); color:#86efac; border-radius:6px; text-decoration:none;">
                          🗺️ Ruta Google Maps ↗
                        </a>
                      </div>
                    </div>
                  </div>
                `;
              }})
              .join("");

      sec.innerHTML = `
        <h2 class="section-title">🗾 Códice Maestro API: Las 24 Expediciones Mensuales, 47 Prefecturas (全国制覇), Ruta de Geishas (花街) &amp; Rodaje YouTube/Kick</h2>
        <p style="color:var(--text-muted); margin-bottom:1.1rem;">
          Mapeo 100% real mes a mes, horario por horario y ruta por ruta desde que bajas del <strong>Shinkansen / Tren de Lujo / Aeropuerto</strong> para conquistar las <strong>47 Prefecturas de Japón (<em>Zenkoku Seiha</em> / 全国制覇: #01 Tokio a #47 Yamanashi)</strong> y los <strong>distritos históricos de Geishas (<em>Hanamachi</em> / <em>Geigi</em> / <em>Maiko</em>)</strong> junto a <strong>あやめ</strong>, diseñado para vivir actividades únicas y grabar contenido épico para tu meta de <strong>+$15,000+ USD/mes en YouTube y Kick</strong> sin chocar con tus <strong>6 combates (77 kg)</strong> ni su sueño sagrado de las <strong>22:30 hrs</strong>.
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
              <li style="margin-bottom:4px;"><strong>🏠 Citas de 1 Día (M1, M2, M6, M7, M15):</strong> Alimentadores automáticos y regreso a dormir a casa en Ikebukuro con ellos (<strong>¥0 extra</strong>).</li>
              <li style="margin-bottom:4px;"><strong>♨️ Escapadas de 1 Noche / 30h (M5, M12, M14, M22, M23):</strong> Fuentes continuas de agua y monitoreo en vivo por cámara Wi-Fi.</li>
              <li><strong>✈️ Viajes de 2 a 3 Noches (M3, M4, M8–M11, M13, M16–M21):</strong> <em>Cat Sitter</em> certificada en Tokio con reporte diario de fotos y videos por LINE para que あやめ viaje con cero preocupación.</li>
            </ul>
          </div>

          <div style="background:#0d1117; border:1px solid #30363d; border-left:4px solid #f0b90b; border-radius:10px; padding:14px;">
            <div style="font-size:0.75rem; font-weight:800; color:#f0b90b; text-transform:uppercase; margin-bottom:6px;">
              🎥 Motor YouTube + Kick (+$15K/mes) &amp; Campaña 6-0
            </div>
            <ul style="margin:0; padding-left:16px; font-size:0.78rem; color:#d1d5db; line-height:1.45;">
              <li style="margin-bottom:4px;"><strong>🎬 Cada Expedición = 1 Mega-Video YouTube + Streams IRL en Kick:</strong> Los viajes financian y multiplican tu canal hacia los <strong>+$15,000+ USD/mes</strong> mostrando el Japón imperial real (Geishas, Shinkansen Suite, Wagyu A5 y MMA).</li>
              <li style="margin-bottom:4px;"><strong>🔐 Doble Llave Antirretadores:</strong> Ningún combate extra se acepta sin aprobación unánime de tu <strong>Entrenador en Jefe</strong> y la <strong>Mánager あやめ</strong>.</li>
              <li><strong>💰 Inversión Total 24 Expediciones (47 Prefecturas):</strong> <strong>${{fmtJpy(grandTotalJpy)}} JPY</strong> (<strong style="color:#4ade80;">⚡ ${{fmtUsd(grandTotalJpy)}} USD hoy</strong> · Promedio ${{fmtUsd(grandTotalJpy / 24)}}/mes).</li>
            </ul>
          </div>
        </div>

        <!-- TABLERO INTERACTIVO DE SELLOS DE LAS 47 PREFECTURAS (ZENKOKU SEIHA) + ATLAS DE GEISHAS -->
        <div style="background:#0d1117; border:1px solid #30363d; border-radius:12px; padding:18px; margin-bottom:20px;">
          <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:10px; margin-bottom:10px;">
            <div>
              <span style="color:#fff; font-weight:800; font-size:1rem;">🏆 Pasaporte Nacional de las 47 Prefecturas (全国制覇 47/47 Stamp Rally) &amp; Ruta de Geishas (花街)</span>
              <div style="font-size:0.78rem; color:#9ca3af; margin-top:2px;">
                Haz clic en cualquier prefectura (<code>#01 Tokio</code> a <code>#47 Yamanashi</code>) para saltar directamente al itinerario de ese mes, o marca cada mes como sellado.
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
          <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:12px; max-height:${{showAll47Pills ? "none" : "120px"}}; overflow:hidden;">
            ${{stampBadgesHtml}}
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:12px;">
            <button id="btn-toggle-47-pills" class="plan-tab" style="font-size:0.73rem; cursor:pointer;">
              ${{showAll47Pills ? "🔼 Compactar Píldoras de 47 Prefecturas" : "🔽 Expandir las 47 Prefecturas Completas (#01 Tokio → #47 Yamanashi)"}}
            </button>
            <button id="btn-toggle-geisha-atlas" class="plan-tab" style="font-size:0.73rem; cursor:pointer; border-color:#f472b6; color:#f9a8d4; background:rgba(244,114,182,0.12);">
              ${{showGeishaAtlas ? "👘 Ocultar Directorio de los 24 Distritos de Geishas (Hanamachi)" : "👘🏮 Abrir Directorio Completo de Geishas, Maiko y Casas de Té (24 Meses)"}}
            </button>
          </div>

          ${{
            showGeishaAtlas
              ? `<div style="background:rgba(244,114,182,0.06); border:1px solid rgba(244,114,182,0.3); border-radius:10px; padding:14px; margin-bottom:14px;">
                   <div style="font-size:0.84rem; font-weight:800; color:#f9a8d4; margin-bottom:8px;">
                     👘🏮 Mapa Nacional de Geishas (Hanamachi / Geigi / Maiko / Ozashiki) y Artes Escénicas Reales en tus 24 Expediciones
                   </div>
                   <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(275px, 1fr)); gap:10px;">
                     ${{geishaAtlasHtml}}
                   </div>
                 </div>`
              : ""
          }}

          <!-- FILTROS POR FASE, SEMÁFORO, REGIÓN Y BUSCADOR -->
          <div style="display:flex; flex-direction:column; gap:10px; padding-top:12px; border-top:1px solid #21262d;">
            <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
              <span style="font-size:0.74rem; color:#9ca3af; font-weight:700; margin-right:4px;">🍁 Fases:</span>
              <button class="plan-tab z47-phase-btn ${{activePhase === "all" ? "active" : ""}}" data-phase="all">Todas las 4 Fases (24 Meses)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "1" ? "active" : ""}}" data-phase="1">Fase 1: M01–M06 (Despertar &amp; Camp #1)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "2" ? "active" : ""}}" data-phase="2">Fase 2: M07–M12 (Peleas #1 y #2)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "3" ? "active" : ""}}" data-phase="3">Fase 3: M13–M18 (Kanazawa, DEEP #3/#4 &amp; Kyushu)</button>
              <button class="plan-tab z47-phase-btn ${{activePhase === "4" ? "active" : ""}}" data-phase="4">Fase 4: M19–M24 (Kioto Gion, #47 Fuji &amp; Retiro 6-0)</button>
            </div>

            <div style="display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:8px;">
              <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
                <span style="font-size:0.74rem; color:#9ca3af; font-weight:700; margin-right:4px;">🚦 Semáforo:</span>
                <button class="plan-tab z47-zone-btn ${{activeZone === "all" ? "active" : ""}}" data-zone="all">Todas (24)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "yellow" ? "active" : ""}}" data-zone="yellow" style="border-color:#d29922; color:#fde68a;">🟡 Off-Camp 79 kg (11)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "red" ? "active" : ""}}" data-zone="red" style="border-color:#f85149; color:#fca5a5;">🔴 Fight Camp 77 kg (3)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "green" ? "active" : ""}}" data-zone="green" style="border-color:#2ea043; color:#86efac;">🟢 Bono Post-Pelea (9)</button>
                <button class="plan-tab z47-zone-btn ${{activeZone === "gold" ? "active" : ""}}" data-zone="gold" style="border-color:#f0b90b; color:#fef08a;">👑 Gala 6-0 (1)</button>
              </div>

              <input
                id="z47-search-input"
                type="search"
                value="${{searchQuery.replace(/"/g, "&quot;")}}"
                placeholder="🔍 Buscar prefectura (ej. Kanagawa), Geisha, Gion, Shinkansen, Wagyu..."
                style="background:#161b22; border:1px solid #30363d; color:#fff; padding:6px 12px; border-radius:8px; min-width:300px; font-size:0.8rem;"
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
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(460px, 1fr)); gap:18px;">
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

      const geishaBtn = document.getElementById("btn-toggle-geisha-atlas");
      if (geishaBtn) {{
        geishaBtn.onclick = () => {{
          showGeishaAtlas = !showGeishaAtlas;
          renderHub();
        }};
      }}

      const resetBtn = document.getElementById("btn-reset-z47-filters");
      if (resetBtn) {{
        resetBtn.onclick = () => {{
          activePhase = "all";
          activeZone = "all";
          activeRegion = "all";
          searchQuery = "";
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
    print(f"[OK] Built upgraded assets/ayame-events-api.js v6.0 ({len(js_code):,} bytes)")


if __name__ == "__main__":
    main()
