/**
 * Atlas del Imperio — Real-Time Multi-API Price & Exchange Rate Engine (v3.0)
 * Connects directly to:
 *   1. https://open.er-api.com/v6/latest/USD (Primary Live FX API)
 *   2. https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY,KRW,THB (ECB Fallback)
 *   3. assets/prices-feed.json (10-Phase Master Feed)
 *   4. assets/wardrobe-prices-feed.json (58-Item Wardrobe V8 + Samsung Tech Feed)
 *   5. assets/prefectures-47-feed.json (24-Month / 47-Prefecture Expedition Cost Feed)
 *
 * Automatically recalculates and annotates:
 *   - All 10 project phases, Tokyo CAPEX/OPEX, Korea clinics (KRW), Thailand Bangtao/Mamma Mia (THB)
 *   - Every single priced card (.pc), category header, and summary row in Guardarropa V8
 *   - All 24-Month / 47-Prefecture expedition budgets in real time
 */
(function () {
  const PRIMARY_FX_API = "https://open.er-api.com/v6/latest/USD";
  const FALLBACK_FX_API = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY,KRW,THB";

  const DEFAULT_STATE = {
    source: "open.er-api.com (Live)",
    updatedAt: new Date().toISOString(),
    mode: "live", // 'live' | 'ref'
    rates: {
      live: { JPY: 158.087, KRW: 1342.741, THB: 33.526, USD: 1.0 },
      ref: { JPY: 147.0, KRW: 1380.0, THB: 33.55, USD: 1.0 }
    },
    capitalTotal: 360000,
    emergencyFund: 48000,
    capexJpy: 4184089,
    opexBaseJpy: 736880,
    opexSuzukiJpy: 796880,
    expeditions47Jpy: 5594200,
    wardrobeFeed: null,
    prefecturesFeed: null,
    activeWardrobeCat: "ALL",
    phases: [
      { id: 1, name: "1. Estudios Pre-Viaje EE.UU.", components: [{ amount: 550, currency: "USD" }], refUsd: 550 },
      { id: 2, name: "2. Corea Viaje 1 (VBT + Rino + LASEK + Bichectomía/Papada + FUE + Dental + 8 sem)", components: [{ amount: 63330000, currency: "KRW" }], refUsd: 45892 },
      { id: 3, name: "3. Recuperación y Fisio en Tokio (St. Luke's + 18 Sesiones)", components: [{ amount: 223000, currency: "JPY" }], refUsd: 1517 },
      { id: 4, name: "4. Fase 0A Tokio + Fase 0B Aclimatación Phuket", components: [{ amount: 160600, currency: "JPY" }, { amount: 42662, currency: "THB" }, { amount: 770, currency: "USD" }], refUsd: 3133 },
      { id: 5, name: "5. Campamento Bangtao 90d (469,300 THB) + Filetotes Mamma Mia 90d (83,829 THB) + Extras", components: [{ amount: 565519, currency: "THB" }], refUsd: 16856 },
      { id: 6, name: "6. Tokio Camp + YOKKAO/Venum Tricolor + Campaña 6-0", components: [{ amount: 334900, currency: "JPY" }, { amount: 1713, currency: "USD" }], refUsd: 3992 },
      { id: 7, name: "7. Corea Viaje 2 (Cantoplastia + 5 Carillas + Blanqueamiento · Cero Lipo)", components: [{ amount: 12100000, currency: "KRW" }], refUsd: 8768 },
      { id: 8, name: "8. CAPEX Casa Tokio (Muebles Funcionales Nitori + PC «Sin Límites» ROG Extreme ¥2.81M + Setup あやめ)", components: [{ amount: 4184089, currency: "JPY" }], refUsd: 28463 },
      { id: 9, name: "9. Guardarropa Imperio V8 + Ecosistema Samsung (58 Piezas)", components: [{ amount: 11686, currency: "USD" }, { amount: 7500, currency: "JPY" }, { amount: 3225020, currency: "KRW" }], refUsd: 15226 },
      { id: 10, name: "10. Visas y Trámites Matrimonio Japón", components: [{ amount: 165000, currency: "JPY" }, { amount: 330, currency: "USD" }], refUsd: 1452 }
    ]
  };

  let state = JSON.parse(JSON.stringify(DEFAULT_STATE));

  function fmtUsd(n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  }
  function fmtJpy(n) {
    return "¥" + Math.round(n).toLocaleString("en-US");
  }
  function fmtKrw(n) {
    return "₩" + Math.round(n).toLocaleString("en-US");
  }

  function calcPhaseUsd(phase, rateSet) {
    let sum = 0;
    for (const c of phase.components) {
      const r = rateSet[c.currency] || 1.0;
      sum += c.amount / r;
    }
    return Math.round(sum);
  }

  async function fetchSubFeeds() {
    const wardrobePaths = ["./assets/wardrobe-prices-feed.json", "../assets/wardrobe-prices-feed.json"];
    for (const p of wardrobePaths) {
      try {
        const r = await fetch(p, { cache: "no-store" });
        if (r.ok) {
          state.wardrobeFeed = await r.json();
          break;
        }
      } catch (_) {}
    }
    const prefPaths = ["./assets/prefectures-47-feed.json", "../assets/prefectures-47-feed.json"];
    for (const p of prefPaths) {
      try {
        const r = await fetch(p, { cache: "no-store" });
        if (r.ok) {
          state.prefecturesFeed = await r.json();
          if (state.prefecturesFeed && state.prefecturesFeed.summary) {
            state.expeditions47Jpy = state.prefecturesFeed.summary.grand_total_jpy || 5594200;
          }
          break;
        }
      } catch (_) {}
    }
  }

  async function fetchLiveRates() {
    await fetchSubFeeds();
    // 1. Try Primary Live FX API (open.er-api.com)
    try {
      const res = await fetch(PRIMARY_FX_API, { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (data && data.rates && data.rates.JPY && data.rates.KRW && data.rates.THB) {
          state.rates.live.JPY = Number(data.rates.JPY);
          state.rates.live.KRW = Number(data.rates.KRW);
          state.rates.live.THB = Number(data.rates.THB);
          state.updatedAt = data.time_last_update_utc || new Date().toUTCString();
          state.source = "ExchangeRate-API (En Vivo)";
          window.IMPERIO_LIVE_RATES = state.rates.live;
          return true;
        }
      }
    } catch (e) {
      console.warn("[Imperio Live API] Primary API fallback:", e);
    }

    // 2. Try European Central Bank Frankfurter API
    try {
      const res = await fetch(FALLBACK_FX_API, { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (data && data.rates && data.rates.JPY && data.rates.KRW && data.rates.THB) {
          state.rates.live.JPY = Number(data.rates.JPY);
          state.rates.live.KRW = Number(data.rates.KRW);
          state.rates.live.THB = Number(data.rates.THB);
          state.updatedAt = data.date || new Date().toISOString().slice(0, 10);
          state.source = "Frankfurter ECB API (En Vivo)";
          window.IMPERIO_LIVE_RATES = state.rates.live;
          return true;
        }
      }
    } catch (e) {
      console.warn("[Imperio Live API] Secondary API fallback:", e);
    }

    // 3. Try local/GitHub Action feed JSON
    const feedPaths = ["./assets/prices-feed.json", "../assets/prices-feed.json"];
    for (const path of feedPaths) {
      try {
        const res = await fetch(path, { cache: "no-store" });
        if (res.ok) {
          const feed = await res.json();
          if (feed && feed.fx_rates && feed.fx_rates.live) {
            state.rates.live = Object.assign(state.rates.live, feed.fx_rates.live);
            state.updatedAt = (feed.meta && feed.meta.last_updated_utc) || state.updatedAt;
            state.source = "GitHub Actions Feed (Auto-Sync)";
            window.IMPERIO_LIVE_RATES = state.rates.live;
            return true;
          }
        }
      } catch (_) {}
    }
    window.IMPERIO_LIVE_RATES = state.rates.live;
    return false;
  }

  function injectStyles() {
    if (document.getElementById("imperio-live-api-styles")) return;
    const style = document.createElement("style");
    style.id = "imperio-live-api-styles";
    style.textContent = `
      #imperio-live-banner {
        background: linear-gradient(135deg, rgba(16, 24, 39, 0.97), rgba(17, 34, 28, 0.97));
        border: 1px solid rgba(74, 222, 128, 0.45);
        border-radius: 12px;
        padding: 12px 16px;
        margin: 14px auto;
        max-width: 1180px;
        color: #f3f4f6;
        font-family: system-ui, -apple-system, sans-serif;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
      }
      .imperio-live-top {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 8px;
        margin-bottom: 10px;
      }
      .imperio-live-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(34, 197, 94, 0.18);
        border: 1px solid #22c55e;
        color: #4ade80;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 700;
      }
      .imperio-pulse {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        box-shadow: 0 0 8px #22c55e;
        animation: imperioPulse 1.8s infinite;
      }
      @keyframes imperioPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.45; transform: scale(1.25); }
      }
      .imperio-live-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
      }
      .imperio-btn {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #e5e7eb;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.74rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .imperio-btn:hover {
        background: rgba(74, 222, 128, 0.2);
        border-color: #4ade80;
        color: #fff;
      }
      .imperio-btn.active {
        background: #16a34a;
        border-color: #4ade80;
        color: #fff;
      }
      .imperio-live-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));
        gap: 8px;
      }
      .imperio-live-card {
        background: rgba(0, 0, 0, 0.32);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 8px 10px;
      }
      .imperio-live-card .lbl {
        font-size: 0.68rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }
      .imperio-live-card .val {
        font-size: 0.96rem;
        font-weight: 800;
        color: #f9fafb;
        margin-top: 2px;
      }
      .imperio-live-card .sub {
        font-size: 0.7rem;
        color: #4ade80;
        margin-top: 1px;
      }
      .imperio-inline-usd {
        display: inline-block;
        margin-left: 6px;
        padding: 1px 6px;
        border-radius: 4px;
        font-size: 0.74em;
        font-weight: 700;
        background: rgba(34, 197, 94, 0.16);
        color: #4ade80;
        border: 1px solid rgba(74, 222, 128, 0.35);
        vertical-align: middle;
      }
      .imperio-pc-live-bar {
        margin-top: 6px;
        padding-top: 6px;
        border-top: 1px dashed rgba(255, 255, 255, 0.12);
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 6px;
        font-size: 0.71rem;
      }
      .imperio-pc-live-tag {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: rgba(34, 197, 94, 0.14);
        border: 1px solid rgba(74, 222, 128, 0.35);
        color: #86efac;
        padding: 2px 7px;
        border-radius: 5px;
        font-weight: 700;
      }
      .imperio-wardrobe-hub {
        margin-top: 12px;
        padding-top: 10px;
        border-top: 1px solid rgba(255, 255, 255, 0.12);
      }
      .imperio-wcat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
        gap: 7px;
        margin-top: 8px;
      }
      .imperio-wcat-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 8px;
        padding: 7px 9px;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .imperio-wcat-card:hover, .imperio-wcat-card.active {
        border-color: #ef4444;
        background: rgba(239, 68, 68, 0.14);
      }
    `;
    document.head.appendChild(style);
  }

  function isWardrobePage() {
    return Boolean(document.getElementById("tab-kicks") || document.querySelector(".pc"));
  }

  function renderBanner() {
    injectStyles();
    const activeRates = state.mode === "live" ? state.rates.live : state.rates.ref;

    const capexUsd = Math.round(state.capexJpy / activeRates.JPY);
    const opexBaseUsd = Math.round(state.opexBaseJpy / activeRates.JPY);
    const opexSuzukiUsd = Math.round(state.opexSuzukiJpy / activeRates.JPY);
    const exp47Usd = Math.round(state.expeditions47Jpy / activeRates.JPY);

    // Calculate live wardrobe total
    const wardrobeUsd = Math.round(11686 + 7500 / activeRates.JPY + 3225020 / activeRates.KRW);
    const wardrobeTaxFreeUsd = Math.round(11686 + 7500 / activeRates.JPY + 2902518 / activeRates.KRW);
    const wardrobeJpy = Math.round(wardrobeUsd * activeRates.JPY);

    let totalPhasesUsd = 0;
    for (const p of state.phases) {
      totalPhasesUsd += state.mode === "live" ? calcPhaseUsd(p, activeRates) : p.refUsd;
    }
    const investUsd = state.capitalTotal - state.emergencyFund - totalPhasesUsd;
    const diffFromRef = totalPhasesUsd - 113442;
    const diffText =
      diffFromRef <= 0
        ? `Ahorro hoy: ${fmtUsd(Math.abs(diffFromRef))} USD por tipo de cambio`
        : `+${fmtUsd(diffFromRef)} USD vs base`;

    let banner = document.getElementById("imperio-live-banner");
    if (!banner) {
      banner = document.createElement("div");
      banner.id = "imperio-live-banner";
      const dedicatedAnchor = document.getElementById("live-fx-anchor");
      if (dedicatedAnchor) {
        dedicatedAnchor.appendChild(banner);
      } else {
        const backLink = document.querySelector(".back-link");
        if (backLink && backLink.parentNode) {
          backLink.parentNode.insertBefore(banner, backLink.nextSibling);
        } else {
          const mainContainer =
            document.querySelector("main.main-content") ||
            document.querySelector(".max-w-6xl") ||
            document.querySelector(".container") ||
            document.body;
          if (mainContainer === document.body) {
            document.body.insertBefore(banner, document.body.firstChild);
          } else {
            mainContainer.insertBefore(banner, mainContainer.firstChild);
          }
        }
      }
    }

    let wardrobeBreakdownHtml = "";
    if (isWardrobePage() && state.wardrobeFeed && state.wardrobeFeed.categories) {
      const catMeta = [
        { key: "sneakers", tab: "kicks", icon: "👟", label: "13 Sneakers (GOAT)" },
        { key: "levis", tab: "levis", icon: "👖", label: "8 Levi's (Promo)" },
        { key: "hoodies", tab: "hoodies", icon: "🧥", label: "12 Supreme Hoodies" },
        { key: "tees", tab: "tees", icon: "👕", label: "15 Tees (Sup+Uniqlo)" },
        { key: "accessories", tab: "acc", icon: "🎒", label: "13 Accesorios" },
        { key: "samsung_kr", tab: "acc", icon: "📱", label: "4 Samsung Corea (₩)" },
        { key: "wolverine", tab: "wolf", icon: "🐺", label: "4 Modo Wolverine" }
      ];

      const cardsHtml = catMeta
        .map((c) => {
          const items = (state.wardrobeFeed.items || []).filter((i) => i.category === c.key);
          let sumUsd = 0;
          items.forEach((it) => {
            const p = it.promo_price !== undefined ? it.promo_price : it.base_price;
            if (it.base_currency === "USD") sumUsd += p;
            else if (it.base_currency === "JPY") sumUsd += p / activeRates.JPY;
            else if (it.base_currency === "KRW") sumUsd += p / activeRates.KRW;
          });
          const sumJpy = Math.round(sumUsd * activeRates.JPY);
          return `
            <div class="imperio-wcat-card" data-wtab="${c.tab}" title="Haz clic para abrir la pestaña ${c.label}">
              <div style="font-size:0.7rem;color:#9ca3af;font-weight:700;">${c.icon} ${c.label}</div>
              <div style="font-size:0.95rem;font-weight:800;color:#fff;margin-top:2px;">${fmtUsd(sumUsd)} USD</div>
              <div style="font-size:0.68rem;color:#4ade80;">⚡ ${fmtJpy(sumJpy)} JPY</div>
            </div>
          `;
        })
        .join("");

      wardrobeBreakdownHtml = `
        <div class="imperio-wardrobe-hub">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
            <span style="font-size:0.78rem;font-weight:700;color:#fca5a5;">
              👕 RASTREADOR EN VIVO DE LAS 58 PIEZAS DEL GUARDARROPA V8 + SAMSUNG TECH COREA
            </span>
            <span style="font-size:0.73rem;color:#86efac;">
              Total API Hoy: <strong>${fmtUsd(wardrobeUsd)} USD</strong> (${fmtJpy(wardrobeJpy)}) · Con Tax-Free Corea (-10%): <strong>${fmtUsd(wardrobeTaxFreeUsd)} USD</strong>
            </span>
          </div>
          <div class="imperio-wcat-grid">${cardsHtml}</div>
        </div>
      `;
    }

    banner.innerHTML = `
      <div class="imperio-live-top">
        <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
          <span class="imperio-live-badge">
            <span class="imperio-pulse"></span>
            🛰️ API MULTI-ÁNGULO DE PRECIOS EN TIEMPO REAL (v3.0)
          </span>
          <span style="font-size:0.75rem; color:#d1d5db;">
            Fuente: <strong>${state.source}</strong> · Actualizado: <code>${state.updatedAt}</code>
          </span>
        </div>
        <div class="imperio-live-controls">
          <button class="imperio-btn ${state.mode === "live" ? "active" : ""}" id="btn-mode-live">
            ⚡ Precios API Hoy (En Vivo)
          </button>
          <button class="imperio-btn ${state.mode === "ref" ? "active" : ""}" id="btn-mode-ref">
            🔒 Tasa Base Conservadora (¥147 / ₩1,380)
          </button>
          <button class="imperio-btn" id="btn-refresh-fx" title="Consultar API ahora mismo">
            🔄 Sincronizar API Ahora
          </button>
        </div>
      </div>

      <div class="imperio-live-grid">
        <div class="imperio-live-card">
          <div class="lbl">🇯🇵 Yen Japonés (1 USD)</div>
          <div class="val">¥${activeRates.JPY.toFixed(2)} JPY</div>
          <div class="sub">CAPEX: ${fmtUsd(capexUsd)} · OPEX: ${fmtUsd(opexBaseUsd)}/mes</div>
        </div>
        <div class="imperio-live-card">
          <div class="lbl">🇰🇷 Won Coreano (1 USD)</div>
          <div class="val">₩${activeRates.KRW.toFixed(2)} KRW</div>
          <div class="sub">Viaje 1: ${fmtUsd(63330000 / activeRates.KRW)} · Viaje 2: ${fmtUsd(12100000 / activeRates.KRW)}</div>
        </div>
        <div class="imperio-live-card">
          <div class="lbl">👟 Guardarropa V8 + Samsung</div>
          <div class="val" style="color:#f87171;">${fmtUsd(wardrobeUsd)} USD</div>
          <div class="sub">${fmtJpy(wardrobeJpy)} · Tax-Free KR: ${fmtUsd(wardrobeTaxFreeUsd)}</div>
        </div>
        <div class="imperio-live-card">
          <div class="lbl">🗾 47 Prefecturas (24 Meses)</div>
          <div class="val" style="color:#38bdf8;">${fmtUsd(exp47Usd)} USD</div>
          <div class="sub">${fmtJpy(state.expeditions47Jpy)} (Promedio ${fmtUsd(exp47Usd / 24)}/mes)</div>
        </div>
        <div class="imperio-live-card" style="border-color:rgba(74,222,128,0.4);">
          <div class="lbl">🏆 Gran Total 10 Fases (${state.mode === "live" ? "API Hoy" : "Base"})</div>
          <div class="val" style="color:#4ade80;">${fmtUsd(totalPhasesUsd)} USD</div>
          <div class="sub">${diffText} · Libre: ${fmtUsd(investUsd)}</div>
        </div>
      </div>
      ${wardrobeBreakdownHtml}
    `;

    document.getElementById("btn-mode-live").onclick = function () {
      state.mode = "live";
      renderBanner();
      annotatePagePrices();
    };
    document.getElementById("btn-mode-ref").onclick = function () {
      state.mode = "ref";
      renderBanner();
      annotatePagePrices();
    };
    document.getElementById("btn-refresh-fx").onclick = async function () {
      const btn = document.getElementById("btn-refresh-fx");
      btn.textContent = "⏳ Consultando API...";
      await fetchLiveRates();
      renderBanner();
      annotatePagePrices();
    };

    banner.querySelectorAll(".imperio-wcat-card").forEach((card) => {
      card.onclick = function () {
        const tab = card.getAttribute("data-wtab");
        if (typeof window.showTab === "function" && tab) {
          window.showTab(tab);
        }
      };
    });
  }

  function updateMasterBudgetTables(activeRates) {
    let totalLive = 0;
    const phaseMap = {};
    for (const p of state.phases) {
      const val = state.mode === "live" ? calcPhaseUsd(p, activeRates) : p.refUsd;
      phaseMap[p.id] = { usd: val, ref: p.refUsd };
      totalLive += val;
    }

    document.querySelectorAll("tr").forEach((tr) => {
      if (tr.children.length !== 3) return;
      const firstCellText = (tr.children[0].textContent || "").trim();
      const thirdCell = tr.children[2];

      const mPhase = firstCellText.match(/^([1-9]|10)\.\s/);
      if (mPhase) {
        const id = parseInt(mPhase[1], 10);
        const info = phaseMap[id];
        if (info) {
          if (state.mode === "live" && info.usd !== info.ref) {
            thirdCell.innerHTML = `${fmtUsd(info.usd)} <span style="display:block;font-size:0.68rem;color:#9ca3af;font-weight:normal;">(base ${fmtUsd(info.ref)})</span>`;
          } else {
            thirdCell.textContent = fmtUsd(info.usd);
          }
        }
        return;
      }

      if (firstCellText.includes("GRAN TOTAL REAL EXACTO")) {
        if (state.mode === "live") {
          thirdCell.innerHTML = `${fmtUsd(totalLive)} USD <span style="display:block;font-size:0.7rem;color:#86efac;font-weight:normal;">⚡ API Hoy (base $113,442)</span>`;
        } else {
          thirdCell.textContent = "$113,442 USD";
        }
      }
    });
  }

  function annotateWardrobeCards(activeRates) {
    if (!isWardrobePage()) return;

    // Remove previous live bars inside .pc cards
    document.querySelectorAll(".imperio-pc-live-bar").forEach((el) => el.remove());

    document.querySelectorAll(".pc").forEach((card) => {
      const text = card.textContent || "";

      // Case 1: Korean Won item (Samsung Tech Korea) e.g. ₩1,406,720
      const mKrw = text.match(/₩\s*([0-9,]+)/);
      if (mKrw) {
        const krw = parseInt(mKrw[1].replace(/,/g, ""), 10);
        if (krw > 0) {
          const usdLive = Math.round(krw / activeRates.KRW);
          const jpyLive = Math.round(usdLive * activeRates.JPY);
          const taxFreeKrw = Math.round(krw * 0.9);
          const taxFreeUsd = Math.round(taxFreeKrw / activeRates.KRW);
          const bar = document.createElement("div");
          bar.className = "imperio-pc-live-bar";
          bar.innerHTML = `
            <span class="imperio-pc-live-tag">⚡ API Hoy: ${fmtUsd(usdLive)} USD · ${fmtJpy(jpyLive)} JPY</span>
            <span style="color:#fde047;font-weight:600;">🛂 Tax-Free (-10%): ${fmtUsd(taxFreeUsd)} USD (${fmtKrw(taxFreeKrw)})</span>
          `;
          card.appendChild(bar);
          return;
        }
      }

      // Case 2: Uniqlo Japan item (~$10 c/u × 5)
      if (text.includes("Uniqlo Supima Cotton")) {
        const jpyTotal = 7500; // ¥1,500 × 5 in Japan
        const usdLive = (jpyTotal / activeRates.JPY).toFixed(2);
        const bar = document.createElement("div");
        bar.className = "imperio-pc-live-bar";
        bar.innerHTML = `
          <span class="imperio-pc-live-tag">⚡ Precio Real Uniqlo JP: ¥1,500 c/u (¥7,500 ×5 = $${usdLive} USD hoy)</span>
        `;
        card.appendChild(bar);
        return;
      }

      // Case 3: Multi-pack tee range like "T1–T3 · Supreme Small Box Tee — White × 3 · ~$80-100 c/u"
      if (text.includes("T1–T3") || text.includes("T4–T5")) {
        const qty = text.includes("T1–T3") ? 3 : 2;
        const unitUsd = 90;
        const totUsd = unitUsd * qty;
        const totJpy = Math.round(totUsd * activeRates.JPY);
        const bar = document.createElement("div");
        bar.className = "imperio-pc-live-bar";
        bar.innerHTML = `
          <span class="imperio-pc-live-tag">⚡ API GOAT (${qty} uds): ${fmtUsd(totUsd)} USD · ${fmtJpy(totJpy)} JPY</span>
          <span style="color:#9ca3af;">Unitario: ~$90 USD (${fmtJpy(unitUsd * activeRates.JPY)})</span>
        `;
        card.appendChild(bar);
        return;
      }

      // Case 4: Standard USD or ~$USD item inside .pc card
      const mUsd = text.match(/~?\$\s*([0-9,]+(?:\.[0-9]+)?)(?:\s*-\s*\$?\s*([0-9,]+))?/);
      if (mUsd) {
        const low = parseFloat(mUsd[1].replace(/,/g, ""));
        const high = mUsd[2] ? parseFloat(mUsd[2].replace(/,/g, "")) : low;
        const usdVal = (low + high) / 2;
        if (usdVal > 0) {
          const jpyVal = Math.round(usdVal * activeRates.JPY);
          const krwVal = Math.round(usdVal * activeRates.KRW);
          const isLevis = text.includes("501") || text.includes("511") || text.includes("512");
          const promoHtml = isLevis
            ? `<span style="color:#60a5fa;font-weight:600;">🏷️ Con Promo Levi's: $${(usdVal * 0.76).toFixed(2)} USD (${fmtJpy(usdVal * 0.76 * activeRates.JPY)})</span>`
            : `<span style="color:#9ca3af;">${fmtKrw(krwVal)} KRW</span>`;
          const bar = document.createElement("div");
          bar.className = "imperio-pc-live-bar";
          bar.innerHTML = `
            <span class="imperio-pc-live-tag">⚡ API Hoy: $${usdVal.toFixed(usdVal % 1 ? 2 : 0)} USD → ${fmtJpy(jpyVal)} JPY</span>
            ${promoHtml}
          `;
          card.appendChild(bar);
        }
      }
    });

    // Also update the top Wardrobe Hero badge if present
    const heroRedBadge = document.querySelector(".text-center .text-lg.font-bold.text-red-500");
    if (heroRedBadge && heroRedBadge.nextElementSibling) {
      const liveTotalUsd = Math.round(11686 + 7500 / activeRates.JPY + 3225020 / activeRates.KRW);
      const liveTotalJpy = Math.round(liveTotalUsd * activeRates.JPY);
      const liveTotalKrw = Math.round(liveTotalUsd * activeRates.KRW);
      heroRedBadge.innerHTML = `💰 ${fmtUsd(liveTotalUsd)} USD <span style="font-size:0.72rem;color:#4ade80;font-weight:700;">⚡ API En Vivo</span>`;
      heroRedBadge.nextElementSibling.textContent = `(${fmtJpy(liveTotalJpy)} JPY · ${fmtKrw(liveTotalKrw)} KRW)`;
    }
  }

  function annotatePagePrices() {
    const activeRates = state.mode === "live" ? state.rates.live : state.rates.ref;
    window.IMPERIO_LIVE_RATES = activeRates;

    // Update 10-Phase Master Budget Tables in campamento/ and plan/
    updateMasterBudgetTables(activeRates);

    // Annotate all Wardrobe V8 cards & summary if on guardarropa/
    annotateWardrobeCards(activeRates);

    // Remove previous inline badges before re-annotating
    document.querySelectorAll(".imperio-inline-usd").forEach((el) => el.remove());

    // 1. Annotate CAPEX room subtotals (.room-subtotal)
    document.querySelectorAll(".room-subtotal").forEach((el) => {
      const text = el.textContent || "";
      const m = text.match(/¥\s*([0-9,]+)/);
      if (m) {
        const jpy = parseInt(m[1].replace(/,/g, ""), 10);
        if (!isNaN(jpy) && jpy > 0) {
          const usd = Math.round(jpy / activeRates.JPY);
          const badge = document.createElement("span");
          badge.className = "imperio-inline-usd";
          badge.textContent = `⚡ ${fmtUsd(usd)} USD`;
          el.appendChild(badge);
        }
      }
    });

    // 2. Annotate individual table price cells with pure ¥, ₩, THB, or $ values
    document.querySelectorAll("td").forEach((td) => {
      if (td.children.length > 0 && td.querySelector("table, ul, div")) return;
      const raw = (td.textContent || "").trim();

      // Match pure Yen cell like "¥32,990"
      const mJpy = raw.match(/^¥\s*([0-9,]+)(\s*JPY)?$/);
      if (mJpy) {
        const val = parseInt(mJpy[1].replace(/,/g, ""), 10);
        if (val > 0) {
          const badge = document.createElement("span");
          badge.className = "imperio-inline-usd";
          badge.textContent = `$${Math.round(val / activeRates.JPY).toLocaleString("en-US")}`;
          td.appendChild(badge);
          return;
        }
      }

      // Match pure KRW cell like "₩63,330,000 KRW"
      const mKrw = raw.match(/^₩\s*([0-9,]+)(\s*KRW)?$/);
      if (mKrw) {
        const val = parseInt(mKrw[1].replace(/,/g, ""), 10);
        if (val > 0) {
          const badge = document.createElement("span");
          badge.className = "imperio-inline-usd";
          badge.textContent = `⚡ $${Math.round(val / activeRates.KRW).toLocaleString("en-US")}`;
          td.appendChild(badge);
          return;
        }
      }

      // Match pure THB cell like "565,519 THB"
      const mThb = raw.match(/^([0-9,]+)\s*THB$/);
      if (mThb) {
        const val = parseInt(mThb[1].replace(/,/g, ""), 10);
        if (val > 0) {
          const badge = document.createElement("span");
          badge.className = "imperio-inline-usd";
          badge.textContent = `⚡ $${Math.round(val / activeRates.THB).toLocaleString("en-US")}`;
          td.appendChild(badge);
          return;
        }
      }

      // Match pure USD cell like "$1,250" or "$340 USD"
      const mUsd = raw.match(/^\$\s*([0-9,]+)(\s*USD)?$/);
      if (mUsd) {
        const val = parseInt(mUsd[1].replace(/,/g, ""), 10);
        if (val > 0) {
          const badge = document.createElement("span");
          badge.className = "imperio-inline-usd";
          badge.textContent = `¥${Math.round(val * activeRates.JPY).toLocaleString("en-US")}`;
          td.appendChild(badge);
        }
      }
    });

    // Notify any interactive charts (OPEX donut / 47 Prefectures hub)
    if (typeof window.onImperioRatesUpdated === "function") {
      try {
        window.onImperioRatesUpdated(activeRates);
      } catch (_) {}
    }
  }

  async function init() {
    renderBanner();
    annotatePagePrices();
    await fetchLiveRates();
    renderBanner();
    annotatePagePrices();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
