/**
 * ============================================================================
 * ATLAS DEL IMPERIO — EXECUTIVE & MOBILE-FIRST NATIVE UX CONTROLLER (v2.0)
 * ============================================================================
 * Features:
 *  1. 2-Deck Glassmorphic Mobile Header (Menu + JST Live Clock + ES/EN/JA + Swipeable Pillar Ribbon)
 *  2. Native iOS/Android Sticky Bottom Navigation Dock (.imperio-mobile-dock)
 *  3. Quick-Jump Bottom Sheet (#imperio-quick-sheet) for 1-Tap Access to all 18 Sections & 3 Dossiers
 *  4. Slide-Over Sidebar Drawer Backdrop + Auto-Close on Link Tap
 *  5. Smart Responsive Table Scroller + `data-label` Auto-Injector + 1-Tap Stacked Mobile Cards Toggle
 *  6. Collapsible Section Headers for Effortless Mobile Scanning
 */
(function () {
  'use strict';

  const IS_MAIN_ATLAS = Boolean(document.getElementById('sidebar') && document.querySelector('.top-command-bar'));

  // ==========================================================================
  // 1. SIDEBAR DRAWER BACKDROP & AUTO-CLOSE ON MOBILE
  // ==========================================================================
  function initSidebarMobileUX() {
    const sidebar = document.getElementById('sidebar');
    if (!sidebar) return;

    // Organize sidebar-header so brand + close button sit on top row, language switcher below
    const header = sidebar.querySelector('.sidebar-header');
    const brand = sidebar.querySelector('.sidebar-brand');
    if (header && brand && !header.querySelector('.sidebar-header-top')) {
      const topRow = document.createElement('div');
      topRow.className = 'sidebar-header-top';
      header.insertBefore(topRow, brand);
      topRow.appendChild(brand);

      const closeBtn = document.createElement('button');
      closeBtn.type = 'button';
      closeBtn.className = 'sidebar-close-btn';
      closeBtn.setAttribute('aria-label', 'Cerrar menú lateral');
      closeBtn.innerHTML = '✕';
      closeBtn.addEventListener('click', () => {
        document.body.classList.remove('sidebar-open');
      });
      topRow.appendChild(closeBtn);
    }

    // Create backdrop if missing
    if (!document.getElementById('imperio-sidebar-backdrop')) {
      const backdrop = document.createElement('div');
      backdrop.id = 'imperio-sidebar-backdrop';
      backdrop.addEventListener('click', () => {
        document.body.classList.remove('sidebar-open');
      });
      document.body.appendChild(backdrop);
    }

    // Close sidebar automatically when tapping any nav link on mobile/tablet
    sidebar.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 1180) {
          document.body.classList.remove('sidebar-open');
        }
      });
    });
  }

  // ==========================================================================
  // 2. RESTRUCTURE TOP COMMAND BAR FOR ZERO-OVERLAP MOBILE LAYOUT
  // ==========================================================================
  function initTopbarMobileUX() {
    const topbar = document.querySelector('.top-command-bar');
    if (!topbar) return;

    const topbarLeft = topbar.querySelector('.topbar-left');
    const toggleBtn = topbar.querySelector('.sidebar-toggle-btn');
    const pillsNav = topbar.querySelector('.domain-pills-nav');
    const langMount = document.getElementById('topbar-lang-mount');

    if (topbarLeft && toggleBtn && pillsNav && !topbar.querySelector('.imperio-mobile-topbar-row1')) {
      const row1 = document.createElement('div');
      row1.className = 'imperio-mobile-topbar-row1';

      // Left cluster: toggle button + live JST mini badge
      const leftCluster = document.createElement('div');
      leftCluster.style.cssText = 'display:flex;align-items:center;gap:8px;min-width:0;';
      leftCluster.appendChild(toggleBtn);

      const jstBadge = document.createElement('span');
      jstBadge.id = 'imperio-topbar-jst-clock';
      jstBadge.style.cssText =
        'display:inline-flex;align-items:center;gap:4px;padding:4px 8px;border-radius:6px;background:rgba(212,168,83,0.12);border:1px solid rgba(212,168,83,0.35);color:#f5c451;font-size:0.7rem;font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap;';
      jstBadge.textContent = '🇯🇵 --:-- JST';
      leftCluster.appendChild(jstBadge);

      row1.appendChild(leftCluster);

      // Right cluster on Row 1: Language Switcher + Desktop External Dossiers
      const rightContainer = langMount ? langMount.parentElement : null;
      if (rightContainer) {
        row1.appendChild(rightContainer);
      }

      topbarLeft.insertBefore(row1, pillsNav);

      // Live Tokyo JST Clock updater
      const updateJstClock = () => {
        const now = new Date();
        const utcMs = now.getTime() + now.getTimezoneOffset() * 60000;
        const jst = new Date(utcMs + 9 * 3600000);
        const hh = String(jst.getHours()).padStart(2, '0');
        const mm = String(jst.getMinutes()).padStart(2, '0');
        jstBadge.textContent = `🇯🇵 ${hh}:${mm} JST`;
      };
      updateJstClock();
      setInterval(updateJstClock, 15000);
    }
  }

  // ==========================================================================
  // 3. NATIVE STICKY BOTTOM NAVIGATION DOCK & QUICK-JUMP SHEET
  // ==========================================================================
  function initMobileBottomDock() {
    if (document.getElementById('imperio-mobile-dock')) return;

    const dock = document.createElement('nav');
    dock.id = 'imperio-mobile-dock';
    dock.className = 'imperio-mobile-dock';
    dock.setAttribute('aria-label', 'Navegación Rápida Móvil');

    if (IS_MAIN_ATLAS) {
      dock.innerHTML = `
        <a href="#domain-1" class="imperio-dock-item active" data-dock-domain="domain-1">
          <span class="dock-icon">📊</span>
          <span>Finanzas</span>
        </a>
        <a href="#domain-2" class="imperio-dock-item" data-dock-domain="domain-2">
          <span class="dock-icon">🏍️</span>
          <span>Moto/168h</span>
        </a>
        <a href="#domain-3" class="imperio-dock-item" data-dock-domain="domain-3">
          <span class="dock-icon">🌸</span>
          <span>あやめ/47</span>
        </a>
        <a href="#domain-4" class="imperio-dock-item" data-dock-domain="domain-4">
          <span class="dock-icon">🥊</span>
          <span>MMA 6-0</span>
        </a>
        <a href="#domain-5" class="imperio-dock-item" data-dock-domain="domain-5">
          <span class="dock-icon">🥩</span>
          <span>Seúl/Bio</span>
        </a>
        <button type="button" class="imperio-dock-item" id="imperio-open-quick-sheet-btn">
          <span class="dock-icon">⚡</span>
          <span>Salto/Menú</span>
        </button>
      `;
      document.body.appendChild(dock);

      // Build Quick-Jump Bottom Sheet
      const sheetBackdrop = document.createElement('div');
      sheetBackdrop.id = 'imperio-quick-sheet-backdrop';
      const sheet = document.createElement('div');
      sheet.id = 'imperio-quick-sheet';
      sheet.innerHTML = `
        <div class="quick-sheet-handle"></div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <div>
            <div style="font-size:0.68rem;font-weight:800;color:#d4a853;text-transform:uppercase;letter-spacing:0.8px;">⚡ Centro de Control Móvil</div>
            <div style="font-size:0.95rem;font-weight:800;color:#fff;">Salto Rápido &amp; Opciones de Vista</div>
          </div>
          <button type="button" id="imperio-close-quick-sheet-btn" style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.16);color:#fff;width:32px;height:32px;border-radius:8px;font-weight:800;cursor:pointer;">✕</button>
        </div>

        <!-- Controles Globales de Experiencia Móvil -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px;">
          <button type="button" id="qs-toggle-all-tables-btn" class="quick-sheet-btn" style="border-color:rgba(56,189,248,0.45);background:rgba(56,189,248,0.1);">
            <span>📱</span>
            <span>Tablas: Modo Tarjetas Móvil</span>
          </button>
          <button type="button" id="qs-open-full-sidebar-btn" class="quick-sheet-btn" style="border-color:rgba(212,168,83,0.45);background:rgba(212,168,83,0.1);">
            <span>☰</span>
            <span>Abrir Índice Completo</span>
          </button>
        </div>

        <div style="font-size:0.68rem;font-weight:800;color:#9ca3af;text-transform:uppercase;letter-spacing:0.7px;margin-bottom:6px;">
          📍 Saltar a Sección Clave (18 Secciones)
        </div>
        <div class="quick-sheet-grid">
          <a href="#hero" class="quick-sheet-btn qs-nav-link">⏱️ 1.1 Reloj JST &amp; KPIs</a>
          <a href="#opex" class="quick-sheet-btn qs-nav-link">📊 1.2 OPEX Mensual</a>
          <a href="#capex" class="quick-sheet-btn qs-nav-link">🛋️ 1.3 CAPEX Cuartos</a>
          <a href="#floor-plan" class="quick-sheet-btn qs-nav-link">🏠 2.1 Hogar 2LDK</a>
          <a href="#motorcycle" class="quick-sheet-btn qs-nav-link">🏍️ 2.2 Honda CB250R API</a>
          <a href="#matrix" class="quick-sheet-btn qs-nav-link">🗓️ 2.4 Matriz 168 Horas</a>
          <a href="#ayame-protocol" class="quick-sheet-btn qs-nav-link">💜 3.1 Protocolo あやめ</a>
          <a href="#ayame-radar" class="quick-sheet-btn qs-nav-link">🛰️ 3.2 Radar Ikebukuro</a>
          <a href="#ayame-24-expediciones" class="quick-sheet-btn qs-nav-link">🗾 3.3 47 Prefecturas</a>
          <a href="#ayame-dates" class="quick-sheet-btn qs-nav-link">🌸 3.4 384 Citas (2 Años)</a>
          <a href="#mma-6-0-roadmap" class="quick-sheet-btn qs-nav-link">🏆 4.1 Ruta Invicta 6-0</a>
          <a href="#walkout-godzilla-mothra" class="quick-sheet-btn qs-nav-link">🦖 4.2 Godzilla &amp; Mothra</a>
          <a href="#dojos" class="quick-sheet-btn qs-nav-link">🥋 4.3 Fighter's Flow</a>
          <a href="#combat" class="quick-sheet-btn qs-nav-link">🥊 4.4 Equipo Yokkao/Venum</a>
          <a href="#restaurants" class="quick-sheet-btn qs-nav-link">🥩 5.1 Carnicerías 24h</a>
          <a href="#extremis" class="quick-sheet-btn qs-nav-link">🇰🇷 5.3 Proyecto Extremis</a>
          <a href="#okinawa-captain" class="quick-sheet-btn qs-nav-link" style="grid-column:span 2;">✈️ 6.1 Capitán O-3 Okinawa &amp; Casa Kanagawa</a>
        </div>

        <div style="font-size:0.68rem;font-weight:800;color:#9ca3af;text-transform:uppercase;letter-spacing:0.7px;margin-bottom:6px;">
          📂 Dossiers Complementarios
        </div>
        <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:8px;">
          <a href="plan/" class="quick-sheet-btn" style="justify-content:center;">🇹🇭 Plan</a>
          <a href="campamento/" class="quick-sheet-btn" style="justify-content:center;">🥊 Camp</a>
          <a href="guardarropa/" class="quick-sheet-btn" style="justify-content:center;">👕 Ropa</a>
        </div>
      `;

      document.body.appendChild(sheetBackdrop);
      document.body.appendChild(sheet);

      const closeQuickSheet = () => {
        sheet.classList.remove('open');
        sheetBackdrop.classList.remove('open');
      };
      const openQuickSheet = () => {
        sheet.classList.add('open');
        sheetBackdrop.classList.add('open');
      };

      document.getElementById('imperio-open-quick-sheet-btn').addEventListener('click', openQuickSheet);
      document.getElementById('imperio-close-quick-sheet-btn').addEventListener('click', closeQuickSheet);
      sheetBackdrop.addEventListener('click', closeQuickSheet);

      sheet.querySelectorAll('.qs-nav-link').forEach((a) => {
        a.addEventListener('click', closeQuickSheet);
      });

      const fullSidebarBtn = document.getElementById('qs-open-full-sidebar-btn');
      if (fullSidebarBtn) {
        fullSidebarBtn.addEventListener('click', () => {
          closeQuickSheet();
          document.body.classList.add('sidebar-open');
        });
      }

      const toggleTablesBtn = document.getElementById('qs-toggle-all-tables-btn');
      if (toggleTablesBtn) {
        toggleTablesBtn.addEventListener('click', () => {
          const active = document.body.classList.toggle('imperio-global-cards-tables');
          toggleTablesBtn.style.background = active ? 'rgba(34,197,94,0.22)' : 'rgba(56,189,248,0.1)';
          toggleTablesBtn.style.borderColor = active ? '#22c55e' : 'rgba(56,189,248,0.45)';
          closeQuickSheet();
        });
      }
    } else {
      // Complementary Dossiers (plan/, campamento/, guardarropa/)
      const path = window.location.pathname;
      const isPlan = path.includes('/plan');
      const isCamp = path.includes('/campamento');
      const isRopa = path.includes('/guardarropa');

      dock.innerHTML = `
        <a href="../index.html" class="imperio-dock-item">
          <span class="dock-icon">👑</span>
          <span>Atlas Central</span>
        </a>
        <a href="../plan/" class="imperio-dock-item ${isPlan ? 'active' : ''}">
          <span class="dock-icon">🇹🇭</span>
          <span>Plan Maestro</span>
        </a>
        <a href="../campamento/" class="imperio-dock-item ${isCamp ? 'active' : ''}">
          <span class="dock-icon">🥊</span>
          <span>Campamento</span>
        </a>
        <a href="../guardarropa/" class="imperio-dock-item ${isRopa ? 'active' : ''}">
          <span class="dock-icon">👕</span>
          <span>Guardarropa</span>
        </a>
        <button type="button" class="imperio-dock-item" id="dossier-cards-toggle-btn">
          <span class="dock-icon">📱</span>
          <span>Vista Tablas</span>
        </button>
      `;
      document.body.appendChild(dock);

      const btn = document.getElementById('dossier-cards-toggle-btn');
      if (btn) {
        btn.addEventListener('click', () => {
          const active = document.body.classList.toggle('imperio-global-cards-tables');
          btn.classList.toggle('active', active);
        });
      }
    }
  }

  // ==========================================================================
  // 4. SMART TABLE SCROLLER & STACKED MOBILE CARDS ENGINE
  // ==========================================================================
  function enhanceTable(table) {
    if (!table || table.dataset.imperioMobileEnhanced === '1') return;
    table.dataset.imperioMobileEnhanced = '1';

    // 1. Stamp data-label on each <td> from <th> headers
    const headers = [];
    const headerRow = table.querySelector('thead tr') || table.querySelector('tr');
    if (headerRow) {
      headerRow.querySelectorAll('th').forEach((th) => {
        headers.push((th.textContent || '').trim());
      });
    }

    if (headers.length > 0) {
      table.querySelectorAll('tbody tr, tr').forEach((tr) => {
        if (tr.querySelector('th')) return;
        tr.querySelectorAll('td').forEach((td, idx) => {
          if (!td.getAttribute('data-label') && headers[idx]) {
            td.setAttribute('data-label', headers[idx]);
          }
        });
      });
    }

    // 2. Wrap in .imperio-table-scroller if not already inside one
    const parent = table.parentElement;
    if (!parent) return;

    let scroller = parent.classList.contains('imperio-table-scroller') ? parent : null;
    if (!scroller) {
      scroller = document.createElement('div');
      scroller.className = 'imperio-table-scroller';
      parent.insertBefore(scroller, table);
      scroller.appendChild(table);
    }

    // 3. Add mobile toolbar above tables with >= 4 columns
    if (headers.length >= 4 && !scroller.previousElementSibling?.classList?.contains('imperio-table-toolbar')) {
      const toolbar = document.createElement('div');
      toolbar.className = 'imperio-table-toolbar';
      toolbar.innerHTML = `
        <span class="imperio-table-hint">↔ Desliza la tabla o apílala en tarjetas</span>
        <button type="button" class="imperio-table-view-btn">📱 Vista Tarjetas</button>
      `;
      const btn = toolbar.querySelector('.imperio-table-view-btn');
      btn.addEventListener('click', () => {
        const isCards = table.classList.toggle('imperio-mobile-cards-active');
        btn.classList.toggle('active', isCards);
        btn.textContent = isCards ? '📊 Vista Tabla' : '📱 Vista Tarjetas';
      });
      scroller.parentElement.insertBefore(toolbar, scroller);
    }
  }

  function enhanceAllTables() {
    document.querySelectorAll('table').forEach((tbl) => {
      // Refresh data-labels on dynamic tables (like CB250R or 384 dates)
      const headers = [];
      const headerRow = tbl.querySelector('thead tr') || tbl.querySelector('tr');
      if (headerRow) {
        headerRow.querySelectorAll('th').forEach((th) => {
          headers.push((th.textContent || '').trim());
        });
      }
      if (headers.length > 0) {
        tbl.querySelectorAll('tbody tr, tr').forEach((tr) => {
          if (tr.querySelector('th')) return;
          tr.querySelectorAll('td').forEach((td, idx) => {
            if (headers[idx]) {
              td.setAttribute('data-label', headers[idx]);
            }
          });
        });
      }
      enhanceTable(tbl);
    });
  }

  // ==========================================================================
  // 5. SECTION COLLAPSE / EXPAND BUTTONS & SCROLL SPY SYNC
  // ==========================================================================
  function initCollapsibleSections() {
    if (!IS_MAIN_ATLAS) return;
    document.querySelectorAll('section').forEach((sec) => {
      const title = sec.querySelector('h2.section-title');
      if (!title || title.querySelector('.imperio-sec-collapse-btn')) return;

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'imperio-sec-collapse-btn';
      btn.title = 'Colapsar / Expandir esta sección';
      btn.innerHTML = '▾';
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const collapsed = sec.classList.toggle('imperio-sec-collapsed');
        btn.innerHTML = collapsed ? '▸ Expandir' : '▾';
      });
      title.appendChild(btn);
    });
  }

  function initScrollSpyMobileSync() {
    if (!IS_MAIN_ATLAS) return;
    let lastDomain = '';

    window.addEventListener(
      'scroll',
      () => {
        const domains = document.querySelectorAll('.domain-banner');
        let currentDomain = 'domain-1';
        const scrollY = window.pageYOffset || document.documentElement.scrollTop;

        domains.forEach((d) => {
          if (scrollY >= d.offsetTop - 180) {
            currentDomain = d.getAttribute('id');
          }
        });

        if (currentDomain !== lastDomain) {
          lastDomain = currentDomain;

          // Sync bottom dock active state
          document.querySelectorAll('.imperio-dock-item[data-dock-domain]').forEach((item) => {
            item.classList.toggle('active', item.getAttribute('data-dock-domain') === currentDomain);
          });

          // Smoothly center active pill in the top horizontal ribbon on mobile
          const activePill = document.querySelector(`.domain-pill[href="#${currentDomain}"]`);
          const navContainer = document.querySelector('.domain-pills-nav');
          if (activePill && navContainer && navContainer.scrollWidth > navContainer.clientWidth) {
            const targetScrollLeft =
              activePill.offsetLeft - navContainer.clientWidth / 2 + activePill.clientWidth / 2;
            navContainer.scrollTo({ left: Math.max(0, targetScrollLeft), behavior: 'smooth' });
          }
        }
      },
      { passive: true }
    );
  }

  // ==========================================================================
  // 6. BOOT & REACTIVE MUTATION OBSERVER FOR DYNAMIC APIS
  // ==========================================================================
  function bootMobileUX() {
    initSidebarMobileUX();
    initTopbarMobileUX();
    initMobileBottomDock();
    initCollapsibleSections();
    enhanceAllTables();
    initScrollSpyMobileSync();

    // Observe dynamic DOM injections (CB250R, 47 Prefectures, 384 Dates, Telemetry Terminals)
    let debounceTimer = null;
    const obs = new MutationObserver(() => {
      if (debounceTimer) clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        enhanceAllTables();
        initCollapsibleSections();
      }, 250);
    });
    obs.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootMobileUX);
  } else {
    bootMobileUX();
  }
})();
