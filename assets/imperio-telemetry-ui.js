/**
 * Atlas del Imperio — Enterprise Multi-Segment Telemetry UI Engine (v4.0)
 * Mounts a dedicated, interactive Bloomberg/Linear-grade API Terminal inside each
 * of the 6 Master Pillars (#domain-1 through #domain-6), connected in real time to:
 *   - assets/imperio-segments-api.json
 *   - Live FX API (open.er-api.com / Frankfurter ECB)
 *   - Live Tokyo Time (JST / UTC+9) for the 168-Hour Matrix & 22:30 Sleep Rule
 */
(function () {
  let FEED = null;

  function getRates() {
    if (window.IMPERIO_LIVE_RATES && window.IMPERIO_LIVE_RATES.JPY) {
      return window.IMPERIO_LIVE_RATES;
    }
    if (FEED && FEED.meta && FEED.meta.live_fx) {
      return FEED.meta.live_fx;
    }
    return { USD: 1.0, JPY: 158.087, KRW: 1342.741, THB: 33.526 };
  }

  function fmtUsd(n) {
    return "$" + Math.round(n).toLocaleString("en-US");
  }
  function fmtJpy(n) {
    return "¥" + Math.round(n).toLocaleString("en-US");
  }
  function fmtKrw(n) {
    return "₩" + Math.round(n).toLocaleString("en-US");
  }
  function fmtThb(n) {
    return Math.round(n).toLocaleString("en-US") + " THB";
  }

  function injectTelemetryStyles() {
    if (document.getElementById("imperio-seg-telemetry-css")) return;
    const st = document.createElement("style");
    st.id = "imperio-seg-telemetry-css";
    st.textContent = `
      .seg-api-terminal {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.94) 0%, rgba(9, 13, 22, 0.98) 100%);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 14px;
        padding: 18px 20px;
        margin: 0 0 26px 0;
        box-shadow: 0 14px 34px rgba(0, 0, 0, 0.42), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        color: #e2e8f0;
        font-variant-numeric: tabular-nums;
      }
      .seg-term-header {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        padding-bottom: 12px;
        margin-bottom: 14px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.14);
      }
      .seg-term-title-group {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-wrap: wrap;
      }
      .seg-endpoint-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.38);
        color: #34d399;
        padding: 3px 9px;
        border-radius: 6px;
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.03em;
      }
      .seg-endpoint-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 8px #10b981;
      }
      .seg-term-title {
        font-size: 0.96rem;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.01em;
        margin: 0;
      }
      .seg-term-meta {
        font-size: 0.72rem;
        color: #94a3b8;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      }
      .seg-kpi-strip {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
        gap: 10px;
        margin-bottom: 14px;
      }
      .seg-kpi-box {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 10px;
        padding: 10px 12px;
        transition: border-color 0.15s ease;
      }
      .seg-kpi-box:hover {
        border-color: rgba(212, 168, 83, 0.45);
      }
      .seg-kpi-lbl {
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
      }
      .seg-kpi-val {
        font-size: 1.08rem;
        font-weight: 800;
        color: #f8fafc;
        margin-top: 3px;
      }
      .seg-kpi-sub {
        font-size: 0.71rem;
        color: #34d399;
        margin-top: 2px;
      }
      .seg-table-wrap {
        overflow-x: auto;
        border: 1px solid rgba(148, 163, 184, 0.14);
        border-radius: 10px;
        background: rgba(9, 13, 22, 0.65);
      }
      .seg-data-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.78rem;
      }
      .seg-data-table th {
        background: rgba(30, 41, 59, 0.65);
        color: #cbd5e1;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        font-size: 0.68rem;
        padding: 9px 12px;
        text-align: left;
        border-bottom: 1px solid rgba(148, 163, 184, 0.16);
      }
      .seg-data-table td {
        padding: 9px 12px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.08);
        color: #e2e8f0;
      }
      .seg-data-table tr:last-child td {
        border-bottom: none;
      }
      .seg-data-table tr:hover td {
        background: rgba(255, 255, 255, 0.025);
      }
      .seg-action-chip {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 3px 9px;
        border-radius: 6px;
        font-size: 0.71rem;
        font-weight: 700;
        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.35);
        color: #7dd3fc;
        text-decoration: none;
        transition: all 0.15s ease;
      }
      .seg-action-chip:hover {
        background: rgba(56, 189, 248, 0.24);
        color: #fff;
      }
      .seg-key-toggle {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.76rem;
        font-weight: 700;
        cursor: pointer;
        border: 1px solid rgba(148, 163, 184, 0.25);
        background: rgba(15, 23, 42, 0.8);
        color: #cbd5e1;
        transition: all 0.15s ease;
      }
      .seg-key-toggle.unlocked {
        background: rgba(16, 185, 129, 0.18);
        border-color: #10b981;
        color: #6ee7b7;
      }
    `;
    document.head.appendChild(st);
  }

  function ensureMountAfter(domainId, terminalId) {
    const dom = document.getElementById(domainId);
    if (!dom) return null;
    let el = document.getElementById(terminalId);
    if (!el) {
      el = document.createElement("div");
      el.id = terminalId;
      el.className = "seg-api-terminal";
      dom.parentNode.insertBefore(el, dom.nextSibling);
    }
    return el;
  }

  // =========================================================================
  // SEGMENT 1 TERMINAL: FINANZAS, DIVISAS, CAPEX POR CUARTO & RUNWAY
  // =========================================================================
  function renderSegment1(rates) {
    const el = ensureMountAfter("domain-1", "seg-terminal-1");
    if (!el || !FEED || !FEED.segment_1_finanzas) return;
    const s1 = FEED.segment_1_finanzas;

    const capexRoomsList = s1.capex_rooms || [];
    const capexTotalJpy = capexRoomsList.reduce((acc, r) => acc + (Number(r.jpy) || 0), 0) || 4518489;
    const capexLiveUsd = Math.round(capexTotalJpy / rates.JPY);
    const capexBaseUsd = Math.round(capexTotalJpy / 147.0);
    const opexOroUsd = Math.round(s1.opex_modes.oro_effective_jpy / rates.JPY);
    const opexSuzukiUsd = Math.round(s1.opex_modes.suzuki_1on1_jpy / rates.JPY);

    const rowsHtml = capexRoomsList
      .map((r) => {
        const usdLive = Math.round(r.jpy / rates.JPY);
        const pct = ((r.jpy / capexTotalJpy) * 100).toFixed(1);
        return `
          <tr>
            <td><strong>${r.name}</strong></td>
            <td>${r.items} piezas</td>
            <td style="font-weight:700; color:#f8fafc;">${fmtJpy(r.jpy)}</td>
            <td style="font-weight:700; color:#34d399;">⚡ ${fmtUsd(usdLive)} USD</td>
            <td>${pct}%</td>
            <td><a href="${r.url}" target="_blank" rel="noopener" class="seg-action-chip">🛒 ${r.store} ↗</a></td>
          </tr>
        `;
      })
      .join("");

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-01-finanzas</span>
          <h3 class="seg-term-title">${s1.title}</h3>
        </div>
        <span class="seg-term-meta">FX Live: 1 USD = ¥${rates.JPY.toFixed(2)} · ₩${rates.KRW.toFixed(1)} · ${rates.THB.toFixed(2)} THB</span>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box" style="border-color:rgba(34,197,94,0.45);">
          <div class="seg-kpi-lbl">🟢🔴 Meta YouTube + Kick</div>
          <div class="seg-kpi-val" style="color:#4ade80;">+$15,000+ / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(15000 * rates.JPY)}/mes (Kick $8.5K + YT $6.5K)</div>
        </div>
        <div class="seg-kpi-box" style="border-color:rgba(56,189,248,0.45);">
          <div class="seg-kpi-lbl">🏢 Dueño de Empresa + Stream</div>
          <div class="seg-kpi-val" style="color:#7dd3fc;">$25,000+ / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(25000 * rates.JPY)}/mes (Empresa $10K + YT/Kick $15K)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🏦 Capital Total & Reserva</div>
          <div class="seg-kpi-val">$360,000 USD</div>
          <div class="seg-kpi-sub">Fondo Intocable: $48,000 USD (10m OPEX)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🛋️ CAPEX Funcional (${capexRoomsList.length} Áreas)</div>
          <div class="seg-kpi-val">${fmtUsd(capexLiveUsd)} USD</div>
          <div class="seg-kpi-sub">${fmtJpy(capexTotalJpy)} (Ahorro FX: ${fmtUsd(Math.max(0, capexBaseUsd - capexLiveUsd))})</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">⚡ OPEX Mensual Efectivo (Oro)</div>
          <div class="seg-kpi-val">${fmtUsd(opexOroUsd)} / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(s1.opex_modes.oro_effective_jpy)}/mes (Con Free Rent)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🥊 OPEX + 1-a-1 Hayato Suzuki</div>
          <div class="seg-kpi-val">${fmtUsd(opexSuzukiUsd)} / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(s1.opex_modes.suzuki_1on1_jpy)}/mes (5 sesiones privadas)</div>
        </div>
      </div>

      <div class="seg-table-wrap">
        <table class="seg-data-table">
          <thead>
            <tr>
              <th>Habitación / Zona del Departamento</th>
              <th>Inventario</th>
              <th>Presupuesto (JPY)</th>
              <th>Conversión API Hoy (USD)</th>
              <th>Peso CAPEX</th>
              <th>Proveedor Directo</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>
      </div>
    `;
  }

  // =========================================================================
  // SEGMENT 2 TERMINAL: HOGAR, HONDA CBR, MASCOTAS & RELOJ 168H JST EN VIVO
  // =========================================================================
  function getJstNowInfo(blocks) {
    const now = new Date();
    const utcMs = now.getTime() + now.getTimezoneOffset() * 60000;
    const jstDate = new Date(utcMs + 9 * 3600000);
    const hrs = jstDate.getHours();
    const mins = jstDate.getMinutes();
    const secs = jstDate.getSeconds();
    const decHour = hrs + mins / 60;

    let activeBlock = blocks[0];
    for (const b of blocks) {
      if (decHour >= b.start && decHour < b.end) {
        activeBlock = b;
        break;
      }
    }

    // Time until 22:30 JST sleep rule
    let sleepTargetDec = 22.5;
    let diffHours = sleepTargetDec - decHour;
    if (diffHours < 0) diffHours += 24;
    const remH = Math.floor(diffHours);
    const remM = Math.floor((diffHours - remH) * 60);

    const timeStr = `${String(hrs).padStart(2, "0")}:${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")} JST`;
    return { timeStr, activeBlock, sleepCountdown: `${remH}h ${remM}m para las 22:30 JST` };
  }

  function renderSegment2(rates) {
    const el = ensureMountAfter("domain-2", "seg-terminal-2");
    if (!el || !FEED || !FEED.segment_2_hogar_cbr) return;
    const s2 = FEED.segment_2_hogar_cbr;
    const jstInfo = getJstNowInfo(s2.schedule_168h_blocks || []);

    const routesHtml = (s2.cbr_routes || [])
      .map((r) => {
        const savedMin = r.train_min - r.cbr_min;
        return `
          <tr>
            <td><strong>${r.dest}</strong></td>
            <td>${r.purpose}</td>
            <td>${r.km} km</td>
            <td style="color:#34d399; font-weight:700;">🏍️ ${r.cbr_min} min (vs 🚆 ${r.train_min}m · Ahorras ${savedMin}m)</td>
            <td>¥${r.fuel_jpy} (~$${(r.fuel_jpy / rates.JPY).toFixed(2)})</td>
            <td><a href="${r.url}" target="_blank" rel="noopener" class="seg-action-chip">🗺️ Ruta GPS ↗</a></td>
          </tr>
        `;
      })
      .join("");

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-02-hogar-cbr-168h</span>
          <h3 class="seg-term-title">${s2.title}</h3>
        </div>
        <span class="seg-term-meta" id="seg2-live-jst-clock">🕒 Hora Tokio: ${jstInfo.timeStr} · ${jstInfo.sleepCountdown}</span>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box" style="border-color:rgba(56,189,248,0.4);">
          <div class="seg-kpi-lbl">🕒 Bloque Activo en Tokio (Matriz 168H)</div>
          <div class="seg-kpi-val" id="seg2-active-block-lbl" style="font-size:0.9rem; color:#7dd3fc;">${jstInfo.activeBlock.label}</div>
          <div class="seg-kpi-sub" id="seg2-active-block-sub" style="color:#cbd5e1;">${jstInfo.activeBlock.detail}</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🏍️ Honda CB250R (8BK-MC52 · 249cc)</div>
          <div class="seg-kpi-val">33.7 km/L · 144 kg · 27 PS</div>
          <div class="seg-kpi-sub"><a href="https://www.honda.co.jp/CB250R/type/" target="_blank" rel="noopener" style="color:#38bdf8;text-decoration:underline;">MSRP ¥564,300 · 0 Shaken (Oficial Honda) ↗</a></div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🐾 Clima 2 Gatitos & 2 Chinchillas</div>
          <div class="seg-kpi-val">20.5°C · 45% HR</div>
          <div class="seg-kpi-sub">Insumos: ¥18,500/mes (${fmtUsd(18500 / rates.JPY)})</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🐱 Cat Sitter Certificada (3 Niveles)</div>
          <div class="seg-kpi-val">¥0 / ¥4K / ¥14K</div>
          <div class="seg-kpi-sub"><a href="${s2.pets_telemetry.booking_url}" target="_blank" rel="noopener" style="color:#34d399;text-decoration:underline;">Agendar Olive Sitter Tokio ↗</a></div>
        </div>
      </div>

      <div class="seg-table-wrap">
        <table class="seg-data-table">
          <thead>
            <tr>
              <th>Destino Frecuente desde Casa</th>
              <th>Propósito Táctico</th>
              <th>Distancia</th>
              <th>Tiempo Honda CB250R vs Tren</th>
              <th>Gasolina (Ida · 33.7 km/L)</th>
              <th>Navegación</th>
            </tr>
          </thead>
          <tbody>
            ${routesHtml}
          </tbody>
        </table>
      </div>
    `;
  }

  // =========================================================================
  // SEGMENT 3 TERMINAL: UNIVERSO AYAME (CLÍNICA NHI + ALTA COSTURA GODZILLA/MOTHRA)
  // =========================================================================
  function renderSegment3(rates) {
    const el = ensureMountAfter("domain-3", "seg-terminal-3");
    if (!el || !FEED || !FEED.segment_3_ayame_universe) return;
    const s3 = FEED.segment_3_ayame_universe;

    const totalCraftJpy = (s3.godzilla_mothra_craft_stages || []).reduce((a, b) => a + b.cost_jpy, 0);
    const craftRows = (s3.godzilla_mothra_craft_stages || [])
      .map((st) => {
        return `
          <tr>
            <td><strong>${st.stage}</strong></td>
            <td>${st.milestone}</td>
            <td style="color:#f9a8d4;">${st.piece}</td>
            <td style="font-weight:700;">${fmtJpy(st.cost_jpy)}</td>
            <td style="color:#34d399; font-weight:700;">⚡ ${fmtUsd(st.cost_jpy / rates.JPY)} USD</td>
          </tr>
        `;
      })
      .join("");

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-03-ayame-craft-47</span>
          <h3 class="seg-term-title">${s3.title}</h3>
        </div>
        <span class="seg-term-meta">NHI Cobertura 70% Activa · Regla Sagrada 22:30 JST</span>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🏥 Ai Clinic Kanda (Dra. Nishimatsu)</div>
          <div class="seg-kpi-val">¥2,000 / mes</div>
          <div class="seg-kpi-sub">⚡ ${fmtUsd(2000 / rates.JPY)} USD (Con Seguro NHI 30%)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🌸 Counseling Room haco (Quincenal)</div>
          <div class="seg-kpi-val">¥25,000 / mes</div>
          <div class="seg-kpi-sub">⚡ ${fmtUsd(25000 / rates.JPY)} USD (Terapia Somática)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">💜 Fondo Mensual Diamante あやめ</div>
          <div class="seg-kpi-val">¥200,000 / mes</div>
          <div class="seg-kpi-sub">⚡ ${fmtUsd(200000 / rates.JPY)} USD (Telas Nippori & Gustos)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">👘 Alta Costura Godzilla & Mothra</div>
          <div class="seg-kpi-val">${fmtJpy(totalCraftJpy)}</div>
          <div class="seg-kpi-sub">⚡ ${fmtUsd(totalCraftJpy / rates.JPY)} USD en 6 Etapas Regionales</div>
        </div>
      </div>

      <div class="seg-table-wrap">
        <table class="seg-data-table">
          <thead>
            <tr>
              <th>Etapa Regional (2027–2029)</th>
              <th>Hito Textil y Artesanal en Japón</th>
              <th>Pieza del Show «Ginza 1954»</th>
              <th>Costo (JPY)</th>
              <th>API Hoy (USD)</th>
            </tr>
          </thead>
          <tbody>
            ${craftRows}
          </tbody>
        </table>
      </div>
    `;
  }

  // =========================================================================
  // SEGMENT 4 TERMINAL: CAMPAÑA MMA 6-0, CANDADO DOBLE LLAVE & ARSENAL TRICOLOR
  // =========================================================================
  let keyCoachUnlocked = true;
  let keyAyameUnlocked = true;

  function renderSegment4(rates) {
    const el = ensureMountAfter("domain-4", "seg-terminal-4");
    if (!el || !FEED || !FEED.segment_4_mma_campaign) return;
    const s4 = FEED.segment_4_mma_campaign;

    const nowMs = Date.now();
    const boutsRows = (s4.bouts || [])
      .map((b) => {
        const campDays = Math.max(0, Math.ceil((new Date(b.camp_start).getTime() - nowMs) / 86400000));
        const fightDays = Math.max(0, Math.ceil((new Date(b.date_iso).getTime() - nowMs) / 86400000));
        return `
          <tr>
            <td><strong>${b.bout}</strong></td>
            <td>${b.org}</td>
            <td><code>${b.camp_start}</code> (Faltan <strong>${campDays}d</strong>)</td>
            <td><code>${b.date_iso}</code> (Faltan <strong>${fightDays}d</strong>)</td>
            <td style="color:#fbbf24; font-weight:700;">🏆 ${b.target_record}</td>
            <td style="color:#34d399;">${b.reward_trip}</td>
          </tr>
        `;
      })
      .join("");

    const bothUnlocked = keyCoachUnlocked && keyAyameUnlocked;

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-04-mma-6-0</span>
          <h3 class="seg-term-title">${s4.title}</h3>
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center;">
          <button type="button" id="btn-key-coach" class="seg-key-toggle ${keyCoachUnlocked ? "unlocked" : ""}">
            ${keyCoachUnlocked ? "🔑 Llave 1: Entrenador (APROBADO)" : "🔒 Llave 1: Entrenador (EN REVISIÓN)"}
          </button>
          <button type="button" id="btn-key-ayame" class="seg-key-toggle ${keyAyameUnlocked ? "unlocked" : ""}">
            ${keyAyameUnlocked ? "🔑 Llave 2: Mánager あやめ (APROBADO)" : "🔒 Llave 2: Mánager あやめ (BLOQUEADO)"}
          </button>
          <span style="padding:4px 10px; border-radius:6px; font-size:0.73rem; font-weight:800; background:${
            bothUnlocked ? "rgba(16,185,129,0.2)" : "rgba(239,68,68,0.22)"
          }; border:1px solid ${bothUnlocked ? "#10b981" : "#ef4444"}; color:${bothUnlocked ? "#6ee7b7" : "#fca5a5"};">
            ${bothUnlocked ? "✅ CONTRATO AUTORIZADO (DOBLE LLAVE ACTIVA)" : "⛔ CONTRATO RECHAZADO POR PROTOCOLO DOBLE LLAVE"}
          </span>
        </div>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">⚖️ Control de Peso Táctico</div>
          <div class="seg-kpi-val">79.0 kg → 77.0 kg</div>
          <div class="seg-kpi-sub">Corte limpio de -2.0 kg (Cero deshidratación extrema)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🥊 FIGHTER'S FLOW + Suzuki</div>
          <div class="seg-kpi-val">${fmtUsd(85300 / rates.JPY)} / mes</div>
          <div class="seg-kpi-sub">¥25,300 Oro + ¥60,000 Pack 5 Clases 1-a-1</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🩳 Kit Tricolor YOKKAO + Venum</div>
          <div class="seg-kpi-val">$620 USD (${fmtJpy(620 * rates.JPY)})</div>
          <div class="seg-kpi-sub">Blanco, Rojo y Azul Rey (Shorts + Guantes Pro)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🇹🇭 Campamento Bangtao 90 Días</div>
          <div class="seg-kpi-val">${fmtUsd(469300 / rates.THB)} USD</div>
          <div class="seg-kpi-sub">469,300 THB (${fmtJpy((469300 / rates.THB) * rates.JPY)})</div>
        </div>
      </div>

      <div class="seg-table-wrap">
        <table class="seg-data-table">
          <thead>
            <tr>
              <th>Bloque Competitivo</th>
              <th>Promoción / Torneo (Tokio)</th>
              <th>Inicio Fight Camp (6 Sem)</th>
              <th>Fecha del Combate</th>
              <th>Récord Objetivo</th>
              <th>Expedición Bono Post-Pelea con あやめ</th>
            </tr>
          </thead>
          <tbody>
            ${boutsRows}
          </tbody>
        </table>
      </div>
    `;

    const b1 = document.getElementById("btn-key-coach");
    const b2 = document.getElementById("btn-key-ayame");
    if (b1) {
      b1.onclick = () => {
        keyCoachUnlocked = !keyCoachUnlocked;
        renderSegment4(getRates());
      };
    }
    if (b2) {
      b2.onclick = () => {
        keyAyameUnlocked = !keyAyameUnlocked;
        renderSegment4(getRates());
      };
    }
  }

  // =========================================================================
  // SEGMENT 5 TERMINAL: BIOLOGÍA HIPER-CARNÍVORA & CLÍNICAS SEÚL (KRW -> USD)
  // =========================================================================
  function renderSegment5(rates) {
    const el = ensureMountAfter("domain-5", "seg-terminal-5");
    if (!el || !FEED || !FEED.segment_5_carnivora_seul) return;
    const s5 = FEED.segment_5_carnivora_seul;

    const clinicsRows = (s5.seoul_clinics || [])
      .map((c) => {
        const usdLive = Math.round(c.krw / rates.KRW);
        const jpyLive = Math.round(usdLive * rates.JPY);
        return `
          <tr>
            <td><span style="color:#93c5fd; font-weight:700;">${c.trip}</span></td>
            <td><strong>${c.clinic}</strong></td>
            <td>${c.procedure}</td>
            <td style="font-weight:700;">${fmtKrw(c.krw)}</td>
            <td style="color:#34d399; font-weight:700;">⚡ ${fmtUsd(usdLive)} USD (${fmtJpy(jpyLive)})</td>
            <td><a href="${c.url}" target="_blank" rel="noopener" class="seg-action-chip">🏥 Clínica Oficial ↗</a></td>
          </tr>
        `;
      })
      .join("");

    const v1TotalKrw = 63330000;
    const v2TotalKrw = 12100000;

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-05-carnivora-extremis</span>
          <h3 class="seg-term-title">${s5.title}</h3>
        </div>
        <span class="seg-term-meta">Regla Estricta: 0 Alcohol 🚫🍺 · 0 Mango 🚫🥭 · 201g Proteína/Día</span>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🥩 Hanamasa 24h + Huevos (Tokio)</div>
          <div class="seg-kpi-val">${fmtUsd(95000 / rates.JPY)} / mes</div>
          <div class="seg-kpi-sub">¥95,000/mes · 550g Res Grass-Fed + 6 Huevos/día</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🍽️ Mamma Mia Steakhouse (Phuket 90d)</div>
          <div class="seg-kpi-val">${fmtUsd(83829 / rates.THB)} Total 90d</div>
          <div class="seg-kpi-sub">83,829 THB (931 THB/día por 2 Filetotes)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🇰🇷 Seúl Viaje 1 (VBT + Rino + LASEK + FUE)</div>
          <div class="seg-kpi-val">${fmtUsd(v1TotalKrw / rates.KRW)} USD</div>
          <div class="seg-kpi-sub">${fmtKrw(v1TotalKrw)} (Ahorro hoy vs base: ${fmtUsd(Math.max(0, 45892 - v1TotalKrw / rates.KRW))})</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🇰🇷 Seúl Viaje 2 (Cantoplastia + Carillas)</div>
          <div class="seg-kpi-val">${fmtUsd(v2TotalKrw / rates.KRW)} USD</div>
          <div class="seg-kpi-sub">${fmtKrw(v2TotalKrw)} (Cero Lipo · Abdomen en Bangtao)</div>
        </div>
      </div>

      <div class="seg-table-wrap">
        <table class="seg-data-table">
          <thead>
            <tr>
              <th>Fase Médica</th>
              <th>Hospital / Clínica en Seúl</th>
              <th>Procedimiento Quirúrgico / Clínico</th>
              <th>Presupuesto (KRW)</th>
              <th>Conversión API Hoy (USD / JPY)</th>
              <th>Portal / Consulta</th>
            </tr>
          </thead>
          <tbody>
            ${clinicsRows}
          </tbody>
        </table>
      </div>
    `;
  }

  // =========================================================================
  // SEGMENT 6 TERMINAL: OPERACIÓN OKINAWA CAPITÁN O-3 & CASA KANAGAWA
  // =========================================================================
  function renderSegment6(rates) {
    const el = ensureMountAfter("domain-6", "seg-terminal-6");
    if (!el || !FEED || !FEED.segment_6_okinawa_captain) return;
    const s6 = FEED.segment_6_okinawa_captain;
    const c = s6.captain_o3_compensation;
    const totalJpy = Math.round(c.total_monthly_comp_usd * rates.JPY);

    el.innerHTML = `
      <div class="seg-term-header">
        <div class="seg-term-title-group">
          <span class="seg-endpoint-pill"><span class="seg-endpoint-dot"></span>GET /api/v4/seg-06-okinawa-o3</span>
          <h3 class="seg-term-title">${s6.title}</h3>
        </div>
        <span class="seg-term-meta">Transición Post-Septiembre 2029 (Tras Retiro Invicto 6-0)</span>
      </div>

      <div class="seg-kpi-strip">
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🎖️ Sueldo Base Capitán (O-3 USAF)</div>
          <div class="seg-kpi-val">${fmtUsd(c.monthly_base_pay_usd)} / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(c.monthly_base_pay_usd * rates.JPY)} JPY/mes</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🌊 OHA Vivienda Okinawa (Libre Impuestos)</div>
          <div class="seg-kpi-val">${fmtUsd(c.monthly_oha_housing_usd)} / mes</div>
          <div class="seg-kpi-sub">${fmtJpy(c.monthly_oha_housing_usd * rates.JPY)} para casa frente al mar en Chatan/Yomitan</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">💵 Compensación Total Mensual O-3</div>
          <div class="seg-kpi-val" style="color:#34d399;">${fmtUsd(c.total_monthly_comp_usd)} / mes</div>
          <div class="seg-kpi-sub">⚡ ${fmtJpy(totalJpy)} JPY/mes (Incluye COLA/BAS Okinawa)</div>
        </div>
        <div class="seg-kpi-box">
          <div class="seg-kpi-lbl">🏡 Casa Bifamiliar 二世帯住宅 (Kanagawa)</div>
          <div class="seg-kpi-val">Hogar para 千秋-san</div>
          <div class="seg-kpi-sub"><a href="${s6.kanagawa_nisetai.search_url}" target="_blank" rel="noopener" style="color:#7dd3fc;text-decoration:underline;">Explorar SUUMO Kanagawa ↗</a></div>
        </div>
      </div>
    `;
  }

  function renderAllTerminals() {
    injectTelemetryStyles();
    const rates = getRates();
    renderSegment1(rates);
    renderSegment2(rates);
    renderSegment3(rates);
    renderSegment4(rates);
    renderSegment5(rates);
    renderSegment6(rates);
  }

  async function bootTelemetry() {
    const paths = ["./assets/imperio-segments-api.json", "../assets/imperio-segments-api.json"];
    for (const p of paths) {
      try {
        const res = await fetch(p, { cache: "no-store" });
        if (res.ok) {
          FEED = await res.json();
          break;
        }
      } catch (_) {}
    }
    if (!FEED) return;

    renderAllTerminals();

    // Update JST clock & active 168H block every second
    setInterval(() => {
      if (!FEED || !FEED.segment_2_hogar_cbr) return;
      const clockEl = document.getElementById("seg2-live-jst-clock");
      const lblEl = document.getElementById("seg2-active-block-lbl");
      const subEl = document.getElementById("seg2-active-block-sub");
      if (clockEl && lblEl && subEl) {
        const info = getJstNowInfo(FEED.segment_2_hogar_cbr.schedule_168h_blocks || []);
        clockEl.textContent = `🕒 Hora Tokio: ${info.timeStr} · ${info.sleepCountdown}`;
        lblEl.textContent = info.activeBlock.label;
        subEl.textContent = info.activeBlock.detail;
      }
    }, 1000);

    // Hook into live rate updates
    const prevHook = window.onImperioRatesUpdated;
    window.onImperioRatesUpdated = function (newRates) {
      if (typeof prevHook === "function") prevHook(newRates);
      renderAllTerminals();
    };

    // Synchronize with ASUS #dreampclist Sala PC station selector
    window.addEventListener("imperio:asus-station-updated", function (ev) {
      if (!FEED || !FEED.segment_1_finanzas || !Array.isArray(FEED.segment_1_finanzas.capex_rooms)) return;
      const d = (ev && ev.detail) || {};
      const room = FEED.segment_1_finanzas.capex_rooms.find((r) => r.id === "ldk_sala_pc_dreampclist");
      if (room && d.salaTotalJpy) {
        room.jpy = d.salaTotalJpy;
        room.name =
          d.salaStationMode === "creator_extreme"
            ? "Estación PC de Sala (LDK 12.7帖 · ASUS #dreampclist Content Creator Extreme ProArt + Monitor ProArt)"
            : "Estación PC de Sala (LDK 12.7帖 · ASUS #dreampclist AI Starter AMD Ryzen 7 9700X + RTX 5060 Ti 16GB)";
        renderSegment1(getRates());
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootTelemetry);
  } else {
    bootTelemetry();
  }
})();
