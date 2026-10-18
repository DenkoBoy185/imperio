/**
 * ============================================================================
 * IMPERIO MULTI-LANGUAGE ENGINE (ES / EN / JA) v1.0
 * ============================================================================
 * Traduce instantáneamente el 100% del Atlas del Imperio (HTML estático +
 * todas las APIs dinámicas: Honda CB250R, 47 Prefecturas, 384 Citas, OPEX/CAPEX,
 * Matriz 168H, Telemetría de 10 Segmentos y Dossiers) entre:
 *   - 🇪🇸 Español (Original 100% sin pérdida)
 *   - 🇺🇸 English (Executive & Tactical English)
 *   - 🇯🇵 日本語 (Natural Japanese — ideal para あやめ y 千秋-san)
 *
 * Arquitectura de 3 Capas:
 *   1. Diccionario Curado de Dominio (Instantáneo 0ms para navegación, KPIs y cabeceras)
 *   2. Motor Neuronal por Lotes (Google GTX API con caché persistente en localStorage)
 *   3. MutationObserver Reactivo (Traduce automáticamente cualquier modal, ruta OSRM
 *      o tarjeta generada dinámicamente por las APIs en vivo)
 */
(function () {
  'use strict';

  const STORAGE_KEY_LANG = 'imperio_active_lang_v1';
  const STORAGE_CACHE_EN = 'imperio_i18n_cache_en_v1';
  const STORAGE_CACHE_JA = 'imperio_i18n_cache_ja_v1';

  let currentLang = localStorage.getItem(STORAGE_KEY_LANG) || 'es';
  let isTranslating = false;
  let observerTimer = null;

  const memCache = {
    en: loadCache(STORAGE_CACHE_EN),
    ja: loadCache(STORAGE_CACHE_JA)
  };

  function loadCache(key) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : {};
    } catch (_) {
      return {};
    }
  }

  function saveCache(lang) {
    try {
      const key = lang === 'en' ? STORAGE_CACHE_EN : STORAGE_CACHE_JA;
      localStorage.setItem(key, JSON.stringify(memCache[lang]));
    } catch (_) {}
  }

  // ==========================================================================
  // 1. DICCIONARIO EXACTO CURADO (0ms Instantáneo para UI, Menús y Títulos)
  // ==========================================================================
  const EXACT_DICT = {
    'Índice': { en: 'Index', ja: '目次' },
    'ATLAS IMPERIO': { en: 'EMPIRE ATLAS', ja: '帝国アトラス' },
    'Dossiers Complementarios': { en: 'Complementary Dossiers', ja: '補足ドシエ一覧' },
    '🇹🇭 Plan': { en: '🇹🇭 Plan', ja: '🇹🇭 計画' },
    '🥊 Camp': { en: '🥊 Camp', ja: '🥊 合宿' },
    '👕 Ropa': { en: '👕 Gear', ja: '👕 衣装' },
    '🇹🇭 Plan Maestro ↗': { en: '🇹🇭 Master Plan ↗', ja: '🇹🇭 マスタープラン ↗' },
    '🥊 Campamento ↗': { en: '🥊 Fight Camp ↗', ja: '🥊 ファイトキャンプ ↗' },
    '👕 Guardarropa ↗': { en: '👕 Wardrobe ↗', ja: '👕 ワードローブ ↗' },

    // Sidebar Groups & Links
    '01 · Mando Central & Finanzas': { en: '01 · Central Command & Finance', ja: '01 · 統括司令部＆財務' },
    '02 · Nuestro Hogar, Moto & 168H': { en: '02 · Our Home, CB250R & 168H', ja: '02 · 2LDK自宅・CB250R・168時間' },
    '03 · Universo あやめ & Citas': { en: '03 · あやめ Universe & Dates', ja: '03 · あやめの世界＆デート計画' },
    '04 · Campaña MMA 6-0 & Show': { en: '04 · 6-0 MMA Campaign & Walkout', ja: '04 · MMA 6戦無敗＆入場演出' },
    '05 · Biología Carnívora & Seúl': { en: '05 · Carnivore Biology & Seoul', ja: '05 · 超肉食ダイエット＆ソウル医療' },
    '06 · Futuro Capitán O-3 Okinawa': { en: '06 · Future Captain O-3 Okinawa', ja: '06 · 沖縄・嘉手納基地 大尉(O-3)計画' },

    // Topbar Domain Pills
    'Finanzas & Reloj': { en: 'Finance & Clock', ja: '財務＆時計' },
    'Hogar & 168H': { en: 'Home & 168H', ja: '自宅＆168時間' },
    'あやめ & Citas': { en: 'あやめ & Dates', ja: 'あやめ＆デート' },
    'MMA 6-0': { en: 'MMA 6-0', ja: 'MMA 6-0' },
    'Carnívoro & Seúl': { en: 'Carnivore & Seoul', ja: '肉食＆ソウル' },
    'Okinawa O-3': { en: 'Okinawa O-3', ja: '沖縄 O-3' },

    // Common Buttons & Table Headers
    '📍 Trazar Ruta': { en: '📍 Trace Route', ja: '📍 ルート描画' },
    '📍 Trazar Ruta en Mapa': { en: '📍 Trace Route on Map', ja: '📍 マップでルート表示' },
    '🌓 Cambiar Capa Mapa': { en: '🌓 Toggle Map Layer', ja: '🌓 マップ表示切替' },
    'Punto de Salida:': { en: 'Departure Base:', ja: '出発拠点:' },
    'Categoría / Destino': { en: 'Category / Destination', ja: 'カテゴリー / 目的地' },
    'Horario en Matriz 168H': { en: '168H Matrix Slot', ja: '168時間スケジュール枠' },
    'Distancia': { en: 'Distance', ja: '距離' },
    '🏍️ CB250R': { en: '🏍️ CB250R', ja: '🏍️ CB250R' },
    '🚆 Tren/Pie': { en: '🚆 Train/Walk', ja: '🚆 電車/徒歩' },
    '⚡ Ahorro (I/V)': { en: '⚡ Saved (R/T)', ja: '⚡ 短縮時間(往復)' },
    '⛽ Gasolina (Ida)': { en: '⛽ Fuel (1-Way)', ja: '⛽ ガソリン(片道)' },
    '🅿️ Parking Moto (駐輪場)': { en: '🅿️ Bike Parking (駐輪場)', ja: '🅿️ バイク駐輪場' },
    'Acción': { en: 'Action', ja: '操作' },
    'Web ↗': { en: 'Web ↗', ja: '公式サイト ↗' },

    // Mobile Bottom Dock & Quick-Jump Sheet
    'Finanzas': { en: 'Finance', ja: '財務' },
    'Moto/168h': { en: 'CB250R/168h', ja: 'バイク/週間' },
    'あやめ/47': { en: 'あやめ/47', ja: 'あやめ/47県' },
    'Seúl/Bio': { en: 'Seoul/Bio', ja: '韓国/肉食' },
    'Salto/Menú': { en: 'Jump/Menu', ja: '移動/目次' },
    'Atlas Central': { en: 'Main Atlas', ja: 'メイン画面' },
    'Plan Maestro': { en: 'Master Plan', ja: 'マスター計画' },
    'Campamento': { en: 'Fight Camp', ja: '合宿計画' },
    'Guardarropa': { en: 'Wardrobe', ja: '衣装・装備' },
    'Vista Tablas': { en: 'Card Tables', ja: '表カード切替' },
    '⚡ Centro de Control Móvil': { en: '⚡ Mobile Control Center', ja: '⚡ モバイル操作センター' },
    'Salto Rápido & Opciones de Vista': { en: 'Quick Jump & View Options', ja: 'クイック移動＆表示設定' },
    'Tablas: Modo Tarjetas Móvil': { en: 'Tables: Mobile Card Mode', ja: '表をスマホカード表示に切替' },
    'Abrir Índice Completo': { en: 'Open Full Sidebar Index', ja: '全目次メニューを開く' },
    '↔ Desliza la tabla o apílala en tarjetas': { en: '↔ Swipe table or stack as mobile cards', ja: '↔ 横スクロールまたはカード表示に切替' },
    '📱 Vista Tarjetas': { en: '📱 Card View', ja: '📱 カード表示' },
    '📊 Vista Tabla': { en: '📊 Table View', ja: '📊 テーブル表示' },
    '⛶ Expandir Mapa': { en: '⛶ Expand Map', ja: '⛶ マップ拡大' },
    '✕ Contraer Mapa': { en: '✕ Collapse Map', ja: '✕ マップ縮小' },
    '▸ Expandir': { en: '▸ Expand', ja: '▸ 展開する' }
  };

  // Pre-seed memory cache with exact dictionary entries
  Object.keys(EXACT_DICT).forEach((esText) => {
    memCache.en[esText] = EXACT_DICT[esText].en;
    memCache.ja[esText] = EXACT_DICT[esText].ja;
  });

  // ==========================================================================
  // 2. INYECCIÓN DEL BOTÓN MULTI-IDIOMA EN LA BARRA SUPERIOR Y SIDEBAR
  // ==========================================================================
  function injectStylesAndButtons() {
    if (!document.getElementById('imperio-i18n-styles')) {
      const style = document.createElement('style');
      style.id = 'imperio-i18n-styles';
      style.textContent = `
        .imperio-lang-switcher {
          display: inline-flex;
          align-items: center;
          gap: 4px;
          background: rgba(15, 23, 42, 0.92);
          border: 1px solid rgba(212, 168, 83, 0.45);
          padding: 3px 5px;
          border-radius: 999px;
          box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
          z-index: 1001;
          flex-shrink: 0;
        }
        .imperio-lang-btn {
          background: transparent;
          border: 1px solid transparent;
          color: #9ca3af;
          font-size: 0.72rem;
          font-weight: 800;
          padding: 4px 9px;
          border-radius: 999px;
          cursor: pointer;
          transition: all 0.16s ease;
          display: inline-flex;
          align-items: center;
          gap: 4px;
          line-height: 1;
          white-space: nowrap;
        }
        .imperio-lang-btn:hover {
          color: #ffffff;
          background: rgba(255, 255, 255, 0.08);
        }
        .imperio-lang-btn.active {
          background: linear-gradient(135deg, #d4a853 0%, #f59e0b 100%);
          color: #090d16;
          border-color: #fde68a;
          box-shadow: 0 2px 8px rgba(245, 158, 11, 0.4);
        }
        .imperio-lang-status {
          font-size: 0.66rem;
          color: #38bdf8;
          font-weight: 700;
          padding: 0 6px;
          display: none;
        }
        .imperio-lang-status.visible {
          display: inline-block;
        }
        @media (max-width: 768px) {
          .imperio-lang-btn {
            padding: 4px 7px;
            font-size: 0.68rem;
          }
        }
      `;
      document.head.appendChild(style);
    }

    const switcherHTML = `
      <div class="imperio-lang-switcher" role="group" aria-label="Selector de Idioma / Language / 言語選択">
        <button type="button" class="imperio-lang-btn" data-lang="es" title="Español (Original)">🇪🇸 ES</button>
        <button type="button" class="imperio-lang-btn" data-lang="en" title="Translate everything to English">🇺🇸 EN</button>
        <button type="button" class="imperio-lang-btn" data-lang="ja" title="すべて日本語に翻訳 (あやめ用)">🇯🇵 日本語</button>
        <span class="imperio-lang-status" id="imperio-lang-status">⚡...</span>
      </div>
    `;

    // 1. Mount in top-command-bar
    const topBar = document.querySelector('.top-command-bar');
    if (topBar && !document.getElementById('topbar-lang-mount')) {
      const wrap = document.createElement('div');
      wrap.id = 'topbar-lang-mount';
      wrap.style.display = 'flex';
      wrap.style.alignItems = 'center';
      wrap.style.gap = '8px';
      wrap.innerHTML = switcherHTML;
      topBar.appendChild(wrap);
    } else if (!topBar && !document.getElementById('floating-lang-mount')) {
      // Fallback for standalone dossier pages without .top-command-bar
      const floatWrap = document.createElement('div');
      floatWrap.id = 'floating-lang-mount';
      floatWrap.style.position = 'fixed';
      floatWrap.style.top = '14px';
      floatWrap.style.right = '16px';
      floatWrap.style.zIndex = '9999';
      floatWrap.innerHTML = switcherHTML;
      document.body.appendChild(floatWrap);
    }

    // 2. Also mount in sidebar-footer if not already present
    const sidebarFooter = document.querySelector('.sidebar-footer');
    if (sidebarFooter && !document.getElementById('sidebar-lang-mount')) {
      const sideWrap = document.createElement('div');
      sideWrap.id = 'sidebar-lang-mount';
      sideWrap.style.marginBottom = '6px';
      sideWrap.style.display = 'flex';
      sideWrap.style.justifyContent = 'center';
      sideWrap.innerHTML = switcherHTML;
      sidebarFooter.insertBefore(sideWrap, sidebarFooter.firstChild);
    }

    document.querySelectorAll('.imperio-lang-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-lang');
        setLanguage(target);
      });
    });

    updateActiveButtons();
  }

  function updateActiveButtons() {
    document.querySelectorAll('.imperio-lang-btn').forEach((btn) => {
      const lang = btn.getAttribute('data-lang');
      if (lang === currentLang) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    document.documentElement.lang = currentLang;
  }

  function setStatusIndicator(show, text) {
    const el = document.getElementById('imperio-lang-status');
    if (!el) return;
    if (show) {
      el.textContent = text || '⚡...';
      el.classList.add('visible');
    } else {
      el.classList.remove('visible');
    }
  }

  // ==========================================================================
  // 3. RECOLECCIÓN Y RESTAURACIÓN DE NODOS DE TEXTO Y ATRIBUTOS
  // ==========================================================================
  const SKIP_TAGS = new Set([
    'SCRIPT',
    'STYLE',
    'NOSCRIPT',
    'CODE',
    'PRE',
    'SVG',
    'PATH',
    'AUDIO',
    'VIDEO',
    'IFRAME'
  ]);

  function shouldTranslateText(str) {
    if (!str) return false;
    const trimmed = str.trim();
    if (trimmed.length < 2) return false;
    // Skip pure numbers, currency figures, coordinates, dates, or symbols
    if (/^[0-9¥$€%,.\-+/:;()[\]\s~•|↗⚡⏱️🥊🥩🌸💑🏟️🦖🟢🟡🔴⚫🔵🏠🏙️🌓🔍🧭🅿️⛽🚆🏍️👑🇹🇭👕🌐]+$/u.test(trimmed)) {
      return false;
    }
    // Must contain at least two Latin letters to warrant translation from Spanish
    if (!/[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]{2,}/.test(trimmed)) {
      return false;
    }
    return true;
  }

  function collectTranslatableNodes(root) {
    const nodes = [];
    const walker = document.createTreeWalker(
      root || document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode(node) {
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          if (SKIP_TAGS.has(parent.tagName)) return NodeFilter.FILTER_REJECT;
          if (parent.closest('.imperio-lang-switcher')) return NodeFilter.FILTER_REJECT;
          const orig = node.__imperioOrigES !== undefined ? node.__imperioOrigES : node.nodeValue;
          if (!shouldTranslateText(orig)) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    let curr;
    while ((curr = walker.nextNode())) {
      if (curr.__imperioOrigES === undefined) {
        curr.__imperioOrigES = curr.nodeValue;
      }
      nodes.push(curr);
    }
    return nodes;
  }

  function collectTranslatableAttributes(root) {
    const items = [];
    const container = root || document.body;
    if (!container || !container.querySelectorAll) return items;
    container.querySelectorAll('[placeholder], [title]').forEach((el) => {
      if (el.closest('.imperio-lang-switcher')) return;
      ['placeholder', 'title'].forEach((attr) => {
        const val = el.getAttribute(attr);
        if (!val) return;
        const propKey = '__imperioOrigAttr_' + attr;
        if (el[propKey] === undefined) {
          el[propKey] = val;
        }
        if (shouldTranslateText(el[propKey])) {
          items.push({ el, attr, orig: el[propKey] });
        }
      });
    });
    return items;
  }

  function restoreSpanish(root) {
    const textNodes = collectTranslatableNodes(root);
    textNodes.forEach((node) => {
      if (node.__imperioOrigES !== undefined && node.nodeValue !== node.__imperioOrigES) {
        node.nodeValue = node.__imperioOrigES;
      }
    });

    const attrItems = collectTranslatableAttributes(root);
    attrItems.forEach(({ el, attr, orig }) => {
      if (el.getAttribute(attr) !== orig) {
        el.setAttribute(attr, orig);
      }
    });
  }

  // ==========================================================================
  // 4. MOTOR DE TRADUCCIÓN POR LOTES (GOOGLE GTX API + POST-PROCESAMIENTO)
  // ==========================================================================
  function postProcessTranslation(text, lang) {
    if (!text) return text;
    let out = text;
    if (lang === 'ja') {
      // Ensure Ayame is always rendered in hiragana あやめ as preferred
      out = out.replace(/アヤメ/g, 'あやめ').replace(/Ayame/gi, 'あやめ');
    }
    return out;
  }

  async function translateBatchGTX(strings, targetLang) {
    // Combine strings with a newline separator that Google GTX preserves
    const SEP = '\n ||| \n';
    const joined = strings.join(SEP);
    const url =
      'https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=' +
      encodeURIComponent(targetLang) +
      '&dt=t&q=' +
      encodeURIComponent(joined);

    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      if (Array.isArray(data) && Array.isArray(data[0])) {
        const fullTranslated = data[0].map((part) => (part && part[0]) || '').join('');
        const splitParts = fullTranslated.split(/\s*\|\|\|\s*/);
        if (splitParts.length === strings.length) {
          return splitParts.map((s) => postProcessTranslation(s.trim(), targetLang));
        }
      }
    } catch (_) {}

    // Fallback: translate individually in parallel if delimiter split mismatched
    const results = await Promise.all(
      strings.map(async (str) => {
        try {
          const u =
            'https://translate.googleapis.com/translate_a/single?client=gtx&sl=es&tl=' +
            encodeURIComponent(targetLang) +
            '&dt=t&q=' +
            encodeURIComponent(str);
          const r = await fetch(u);
          if (!r.ok) return str;
          const d = await r.json();
          if (Array.isArray(d) && Array.isArray(d[0])) {
            return postProcessTranslation(
              d[0].map((p) => (p && p[0]) || '').join('').trim(),
              targetLang
            );
          }
        } catch (_) {}
        return str;
      })
    );
    return results;
  }

  async function applyLanguageToDOM(lang, root) {
    if (lang === 'es') {
      restoreSpanish(root);
      return;
    }

    const cache = memCache[lang];
    const textNodes = collectTranslatableNodes(root);
    const attrItems = collectTranslatableAttributes(root);

    const missingSet = new Set();

    // First pass: apply cached translations immediately (0ms) and collect uncached
    textNodes.forEach((node) => {
      const orig = node.__imperioOrigES;
      const trimmed = orig.trim();
      if (cache[trimmed]) {
        const leading = orig.match(/^\s*/)[0];
        const trailing = orig.match(/\s*$/)[0];
        const nextVal = leading + cache[trimmed] + trailing;
        if (node.nodeValue !== nextVal) {
          node.nodeValue = nextVal;
        }
      } else {
        missingSet.add(trimmed);
      }
    });

    attrItems.forEach(({ el, attr, orig }) => {
      const trimmed = orig.trim();
      if (cache[trimmed]) {
        if (el.getAttribute(attr) !== cache[trimmed]) {
          el.setAttribute(attr, cache[trimmed]);
        }
      } else {
        missingSet.add(trimmed);
      }
    });

    const missingList = Array.from(missingSet);
    if (missingList.length === 0) return;

    isTranslating = true;
    setStatusIndicator(
      true,
      lang === 'ja' ? '🇯🇵 翻訳中...' : '🇺🇸 Translating...'
    );

    // Chunk missing strings into batches of 18 (safe URL length for GET)
    const BATCH_SIZE = 18;
    const batches = [];
    for (let i = 0; i < missingList.length; i += BATCH_SIZE) {
      batches.push(missingList.slice(i, i + BATCH_SIZE));
    }

    // Run up to 4 batches concurrently for rapid page translation
    const CONCURRENCY = 4;
    for (let i = 0; i < batches.length; i += CONCURRENCY) {
      if (currentLang !== lang) break; // User switched language mid-flight
      const slice = batches.slice(i, i + CONCURRENCY);
      await Promise.all(
        slice.map(async (batch) => {
          const translatedArr = await translateBatchGTX(batch, lang);
          batch.forEach((origTrimmed, idx) => {
            const trans = translatedArr[idx];
            if (trans) {
              cache[origTrimmed] = trans;
            }
          });
        })
      );

      // Progressive DOM update after each concurrent wave
      textNodes.forEach((node) => {
        const orig = node.__imperioOrigES;
        const trimmed = orig.trim();
        if (cache[trimmed]) {
          const leading = orig.match(/^\s*/)[0];
          const trailing = orig.match(/\s*$/)[0];
          const nextVal = leading + cache[trimmed] + trailing;
          if (node.nodeValue !== nextVal) {
            node.nodeValue = nextVal;
          }
        }
      });

      attrItems.forEach(({ el, attr, orig }) => {
        const trimmed = orig.trim();
        if (cache[trimmed] && el.getAttribute(attr) !== cache[trimmed]) {
          el.setAttribute(attr, cache[trimmed]);
        }
      });
    }

    saveCache(lang);
    isTranslating = false;
    setStatusIndicator(false);
  }

  async function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem(STORAGE_KEY_LANG, lang);
    updateActiveButtons();
    await applyLanguageToDOM(lang, document.body);
  }

  // ==========================================================================
  // 5. OBSERVADOR DE MUTACIONES PARA WIDGETS Y APIS DINÁMICAS
  // ==========================================================================
  function setupMutationObserver() {
    const observer = new MutationObserver((mutations) => {
      if (currentLang === 'es' || isTranslating) return;
      let hasNewElements = false;
      for (const m of mutations) {
        if (m.addedNodes && m.addedNodes.length > 0) {
          hasNewElements = true;
          break;
        }
      }
      if (!hasNewElements) return;

      if (observerTimer) clearTimeout(observerTimer);
      observerTimer = setTimeout(() => {
        if (currentLang !== 'es') {
          applyLanguageToDOM(currentLang, document.body);
        }
      }, 180);
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true
    });
  }

  function boot() {
    injectStylesAndButtons();
    setupMutationObserver();
    if (currentLang !== 'es') {
      // Translate initial view + re-check after dynamic APIs finish booting
      applyLanguageToDOM(currentLang, document.body);
      setTimeout(() => applyLanguageToDOM(currentLang, document.body), 900);
      setTimeout(() => applyLanguageToDOM(currentLang, document.body), 2200);
    }
  }

  // Expose global helper in case user or other scripts invoke it
  window.setImperioLanguage = setLanguage;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
