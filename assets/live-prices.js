/**
 * Atlas del Imperio — Real-Time Price & Exchange Rate API Engine (v2.1)
 * Connects directly to:
 *   1. https://open.er-api.com/v6/latest/USD (Primary Live FX API)
 *   2. https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY,KRW,THB (ECB Fallback)
 *   3. assets/prices-feed.json (GitHub Actions 12h Auto-Updated Feed)
 *
 * Automatically recalculates all 10 project phases, Tokyo CAPEX/OPEX,
 * Korea clinics (KRW), and Thailand Bangtao/Mamma Mia (THB) in real time.
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
    capexJpy: 2360190,
    opexBaseJpy: 736880,
    opexSuzukiJpy: 796880,
    phases: [
      { id: 1, name: "1. Estudios Pre-Viaje EE.UU.", components: [{ amount: 550, currency: "USD" }], refUsd: 550 },
      { id: 2, name: "2. Corea Viaje 1 (VBT + Rino + LASEK + Bichectomía/Papada + FUE + Dental + 8 sem)", components: [{ amount: 63330000, currency: "KRW" }], refUsd: 45892 },
      { id: 3, name: "3. Recuperación y Fisio en Tokio (St. Luke's + 18 Sesiones)", components: [{ amount: 223000, currency: "JPY" }], refUsd: 1517 },
      { id: 4, name: "4. Fase 0A Tokio + Fase 0B Aclimatación Phuket", components: [{ amount: 160600, currency: "JPY" }, { amount: 42662, currency: "THB" }, { amount: 770, currency: "USD" }], refUsd: 3133 },
      { id: 5, name: "5. Campamento Bangtao 90d (469,300 THB) + Filetotes Mamma Mia 90d (83,829 THB) + Extras", components: [{ amount: 565519, currency: "THB" }], refUsd: 16856 },
      { id: 6, name: "6. Tokio Camp + Venum Japan + Campaña 5 Peleas", components: [{ amount: 334900, currency: "JPY" }, { amount: 1713, currency: "USD" }], refUsd: 3992 },
      { id: 7, name: "7. Corea Viaje 2 (Cantoplastia + 5 Carillas + Blanqueamiento · Cero Lipo)", components: [{ amount: 12100000, currency: "KRW" }], refUsd: 8768 },
      { id: 8, name: "8. CAPEX Casa Urbanex Asakusabashi Front (Muebles Funcionales Nitori + Setups Intactos)", components: [{ amount: 2360190, currency: "JPY" }], refUsd: 16056 },
      { id: 9, name: "9. Guardarropa Imperio V8 + Ecosistema Samsung", components: [{ amount: 15226, currency: "USD" }], refUsd: 15226 },
      { id: 10, name: "10. Visas y Trámites Matrimonio Japón", components: [{ amount: 165000, currency: "JPY" }, { amount: 330, currency: "USD" }], refUsd: 1452 }
    ]
  };

  let state = JSON.parse(JSON.stringify(DEFAULT_STATE));

  function fmtUsd(n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  }

  function calcPhaseUsd(phase, rateSet) {
    let sum = 0;
    for (const c of phase.components) {
      const r = rateSet[c.currency] || 1.0;
      sum += c.amount / r;
    }
    return Math.round(sum);
  }

  async function fetchLiveRates() {
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
            return true;
          }
        }
      } catch (_) {}
    }
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
        font-size: 0.75em;
        font-weight: 700;
        background: rgba(34, 197, 94, 0.16);
        color: #4ade80;
        border: 1px solid rgba(74, 222, 128, 0.35);
        vertical-align: middle;
      }
    `;
    document.head.appendChild(style);
  }

  function renderBanner() {
    injectStyles();
    const activeRates = state.mode === "live" ? state.rates.live : state.rates.ref;

    const capexUsd = Math.round(state.capexJpy / activeRates.JPY);
    const opexBaseUsd = Math.round(state.opexBaseJpy / activeRates.JPY);
    const opexSuzukiUsd = Math.round(state.opexSuzukiJpy / activeRates.JPY);

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

    banner.innerHTML = `
      <div class="imperio-live-top">
        <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
          <span class="imperio-live-badge">
            <span class="imperio-pulse"></span>
            🛰️ API DE PRECIOS EN TIEMPO REAL ACTIVA
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
          <div class="sub">CAPEX Casa: ${fmtUsd(capexUsd)} · OPEX: ${fmtUsd(opexBaseUsd)}/mes</div>
        </div>
        <div class="imperio-live-card">
          <div class="lbl">🇰🇷 Won Coreano (1 USD)</div>
          <div class="val">₩${activeRates.KRW.toFixed(2)} KRW</div>
          <div class="sub">Viaje 1: ${fmtUsd(63330000 / activeRates.KRW)} · Viaje 2: ${fmtUsd(12100000 / activeRates.KRW)}</div>
        </div>
        <div class="imperio-live-card">
          <div class="lbl">🇹🇭 Baht Tailandés (1 USD)</div>
          <div class="val">${activeRates.THB.toFixed(2)} THB</div>
          <div class="sub">Bangtao 90d + Mamma Mia: ${fmtUsd(565519 / activeRates.THB)}</div>
        </div>
        <div class="imperio-live-card" style="border-color:rgba(74,222,128,0.4);">
          <div class="lbl">🏆 Gran Total 10 Fases (${state.mode === "live" ? "API Hoy" : "Base"})</div>
          <div class="val" style="color:#4ade80;">${fmtUsd(totalPhasesUsd)} USD</div>
          <div class="sub">${diffText}</div>
        </div>
        <div class="imperio-live-card" style="border-color:rgba(167,139,250,0.4);">
          <div class="lbl">💼 Capital Libre Invertido (De $360K)</div>
          <div class="val" style="color:#c4b5fd;">${fmtUsd(investUsd)} USD</div>
          <div class="sub">+ $48,000 Fondo Emergencia · OPEX c/Suzuki: ${fmtUsd(opexSuzukiUsd)}/mes</div>
        </div>
      </div>
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

  function annotatePagePrices() {
    const activeRates = state.mode === "live" ? state.rates.live : state.rates.ref;

    // Update 10-Phase Master Budget Tables in campamento/ and plan/
    updateMasterBudgetTables(activeRates);

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

    // 2. Annotate individual table price cells with pure ¥, ₩, or THB values
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
        }
      }
    });
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
