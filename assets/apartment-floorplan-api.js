/**
 * URBANEX ASAKUSABASHI FRONT — INTERACTIVE ARCHITECTURAL CAD & SMART-HOME FLOOR PLAN API v1.0
 * Reformulates all 6 apartment maps (#floor-plan) with interactive SVG CAD blueprints,
 * clickable equipment/furniture/PC/pet nodes, real-time CAPEX & USD/JPY synchronization,
 * 10GbE LAN + Wi-Fi 7 mesh overlay, 60A electrical load telemetry, and the new
 * ASUS #dreampclist Workstation in the Living Room (LDK 12.7帖).
 */
(function () {
  "use strict";

  const ROOM_TABS = [
    {
      id: "general",
      label: "🏠 全体 / Mapa General CAD (2SLDK 50.18m²)",
      badge: "Planta Completa + 2 Estaciones PC",
      legacyImg: "assets/plan_general.png?v=2"
    },
    {
      id: "ldk",
      label: "🛋️ LDK (12.7帖) + 🆕 PC de Sala (#dreampclist) + チンチラ (1.4帖)",
      badge: "Sala AI / ProArt + Cocina Carnívora",
      legacyImg: "assets/plan_ldk.jpg?v=2"
    },
    {
      id: "denkoboy",
      label: "💻 Bed Room 2: デンコボーイ司令室 (4.0帖 · ROG «Sin Límites»)",
      badge: "Torre ¥2.80M + Dual OLED 240Hz",
      legacyImg: "assets/plan_room2_denkoboy.jpg?v=2"
    },
    {
      id: "ayame",
      label: "🌸 Bed Room 1: あやめの部屋 & アトリエ (3.8帖 + WIC)",
      badge: "Sueño 22:30 + Taller Textil",
      legacyImg: "assets/plan_room1_ayame.jpg?v=2"
    },
    {
      id: "bathroom",
      label: "🚿 水回り & 玄関 / Baño (1317), Lavadora 8kg & Entrada",
      badge: "Lavadora MMA + Barrera Gatos",
      legacyImg: "assets/plan_bathroom.jpg?v=2"
    },
    {
      id: "madori",
      label: "📐 間取り図 Oficial RF12 + Red 10GbE & Carga Eléctrica (60A)",
      badge: "1301 (2SLDK) vs 303 (3LDK)",
      legacyImg: "assets/plan_madori_real.png?v=2"
    }
  ];

  const state = {
    activeTab: "ldk", // Start on LDK or General; user can click any tab, and showPlan() bridges to this API
    selectedNodeId: "node_sala_pc",
    salaPcMode: "ai_starter", // "ai_starter" (¥334,400) | "creator_extreme" (¥2,190,960) | "both" (¥2,525,360)
    showNetworkOverlay: true,
    showPowerOverlay: false,
    showReferenceImage: false,
    jpyRate: 147.0
  };

  function detectJpyRate() {
    const rateCard = document.querySelector("#imperio-live-banner .imperio-live-card .val");
    if (rateCard) {
      const m = rateCard.textContent.match(/¥([0-9.]+)/);
      if (m) {
        const parsed = parseFloat(m[1]);
        if (parsed > 90 && parsed < 250) {
          state.jpyRate = parsed;
          return;
        }
      }
    }
  }

  function fmtYen(n) {
    return "¥" + Math.round(n).toLocaleString("en-US");
  }

  function fmtUsd(jpy) {
    return "~$" + Math.round(jpy / (state.jpyRate || 147)).toLocaleString("en-US") + " USD";
  }

  function getSalaPcConfig() {
    if (state.salaPcMode === "creator_extreme") {
      return {
        id: "node_sala_pc",
        shortLabel: "🎬 PC Sala: Content Creator Extreme (ProArt)",
        title: "🎬 Estación de Sala (LDK 12.7帖): ASUS #dreampclist Content Creator Extreme + ProArt OLED",
        jpy: 2190960,
        towerJpy: 1952960,
        monitorJpy: 238000,
        watts: 880,
        lan: "10GbE RJ45 + Dual USB4 (40Gbps) + Wi-Fi 7",
        zone: "LDK (12.7帖) · Esquina Noreste de Estudio",
        color: "#d4a853",
        katabanSummary: "Ryzen 9 9950X3D (o Core Ultra 9 285K) + PROART X870E-CREATOR WIFI + ROG-ASTRAL-RTX5090-O32G + 64GB/128GB DDR5 + PROART LC 420 (Noctua) + 8TB NVMe (SN8100 Gen5 + 990 PRO Gen4) + PROART-1200P + PROART PA602 WOOD + Monitor ProArt PA32UCDM (¥238K)",
        desc: "Estación de estudio profesional ubicada en la Sala (LDK 12.7帖) con gabinete ProArt PA602 con ruedas integradas, refrigeración Noctua ultra silenciosa y red de 10 Gbps conectada directo al cuarto de Bruno para edición 8K RAW en DaVinci/Premiere, render 3D y flujos pesados de IA.",
        specs: [
          "CPU: AMD Ryzen 9 9950X3D (¥109,980) o Intel Core Ultra 9 285K (¥92,800)",
          "M/B: ASUS ProArt X870E-CREATOR WIFI 10GbE + Dual USB4 (¥89,800)",
          "GPU: ASUS ROG Astral RTX 5090 32GB OC (¥1,199,800) o ProArt RTX 5080 (¥480,000)",
          "RAM & SSD: 64GB DDR5-6000 CL30 (¥123,800) + 8TB NVMe Gen5/Gen4 (¥267,980)",
          "AIO, PSU & Case: ProArt LC 420 Noctua (¥46,800) + ProArt 1200W (¥72,000) + ProArt PA602 Wood (¥42,800)",
          "Monitor en Sala: ASUS ProArt Display OLED PA32UCDM 31.5\" 4K 240Hz ΔE<1 (¥238,000) o PA32KCX 8K (¥650,000)"
        ]
      };
    }
    if (state.salaPcMode === "both") {
      return {
        id: "node_sala_pc",
        shortLabel: "⚡ Dual PC Sala: AI Starter + Creator Extreme",
        title: "⚡ Doble Estación en Sala (LDK 12.7帖): AI Starter (AMD) + Content Creator Extreme (ProArt)",
        jpy: 2525360,
        towerJpy: 2287360,
        monitorJpy: 238000,
        watts: 1230,
        lan: "Switch 10GbE (2 puertos 10G + 4 puertos 2.5G) + Wi-Fi 7",
        zone: "LDK (12.7帖) · Pared Norte Completa (Servidor IA + Estudio 8K)",
        color: "#a855f7",
        katabanSummary: "AI Starter AMD (Ryzen 7 9700X + Prime B850 + RTX 5060 Ti 16GB = ¥334,400) + Content Creator Extreme (9950X3D + ProArt X870E + RTX 5090 + PA32UCDM = ¥2,190,960)",
        desc: "Configuración combinada en la Sala (LDK 12.7帖): el AI Starter AMD corre 24/7 como servidor local de LLMs (Ollama / DeepSeek / Llama / MuseTree) con bajo consumo (65W CPU), mientras la ProArt Content Creator Extreme procesa video 8K y VFX.",
        specs: [
          "Nodo 1 (Servidor IA 24/7): Ryzen 7 9700X + Prime B850-PLUS WIFI + RTX 5060 Ti 16GB GDDR7 (¥334,400)",
          "Nodo 2 (Estudio 8K): Ryzen 9 9950X3D + ProArt X870E-CREATOR + RTX 5090 32GB + 8TB NVMe (¥1,952,960)",
          "Pantalla de Estudio: ASUS ProArt Display OLED PA32UCDM 31.5\" 4K 240Hz ΔE<1 (¥238,000)",
          "Red Local: Enlace 10GbE directo con la Torre «Sin Límites» del Cuarto de Bruno (4.0帖)"
        ]
      };
    }
    // Default: AI Starter (AMD)
    return {
      id: "node_sala_pc",
      shortLabel: "🤖 PC Sala: AI Starter AMD (#dreampclist)",
      title: "🤖 Estación de Sala (LDK 12.7帖): ASUS #dreampclist AI Starter (Versión AMD) — IA Local, LLMs & Productividad",
      jpy: 334400,
      towerJpy: 334400,
      monitorJpy: 0,
      watts: 350,
      lan: "2.5GbE LAN + Wi-Fi 6E/7 (ASUS AI Networking II)",
      zone: "LDK (12.7帖) · Esquina Noreste junto a TV 55\" 4K y Toma Fibra",
      color: "#38bdf8",
      katabanSummary: "Ryzen 7 9700X (100-100001404WOF) + PRIME B850-PLUS WIFI + PRIME-RTX5060TI-O16G (16GB GDDR7) + 32GB DDR5-6000 CL30 + PRIME LC 360 ARGB + 2TB NVMe Gen4 + Prime 750G + PRIME AP202 TG / ProArt PA401",
      desc: "Ubicada estratégicamente en la Sala (LDK 12.7帖) para ejecutar modelos de lenguaje locales (Llama / DeepSeek en LM Studio y Ollama), generación de imágenes con Stable Diffusion, ASUS AI Advisor y MuseTree, además de conectarse por HDMI 2.1 a la TV 4K de 55\" o servir como nodo de IA por red local para tu cuarto.",
      specs: [
        "CPU: AMD Ryzen 7 9700X (Zen 5 con AVX-512 nativo de 512 bits · 65W TDP) — $319 USD / ¥53,800",
        "M/B: ASUS Prime B850-PLUS WIFI (o TUF B850-PLUS WIFI · PCIe 5.0 x16 · ASUS AI Advisor) — $189–$219 / ¥37,800",
        "GPU: ASUS Prime / TUF GeForce RTX 5060 Ti 16GB GDDR7 (Blackwell FP4 Tensor 5.ª Gen) — $479–$599 / ¥96,800",
        "RAM: 32 GB (2x16GB) DDR5-6000 CL30 AMD EXPO (Corsair / T-Force) — $480–$520 / ¥62,000",
        "AIO & SSD: ASUS Prime LC 360 ARGB (¥19,800) + SSD NVMe PCIe 4.0 2TB ~7,000 MB/s (¥25,800)",
        "PSU & Case: ASUS Prime 750W Gold ATX 3.1 (¥19,800) + Gabinete compacto Prime AP202 TG / ProArt PA401 (¥18,600)"
      ]
    };
  }

  function getAllNodes() {
    const salaPc = getSalaPcConfig();
    return {
      node_sala_pc: salaPc,
      node_bruno_pc: {
        id: "node_bruno_pc",
        shortLabel: "🔥 Torre «Sin Límites» ROG (¥2,809,059)",
        title: "💻 Bed Room 2 (4.0帖): Configuración «Sin Límites» (Nivel 3: Extreme Tope Absoluto · Full ASUS ROG)",
        jpy: 2809059,
        watts: 950,
        lan: "10GbE LAN + Wi-Fi 7 (ROG Crosshair X870E Dark Hero)",
        zone: "Bed Room 2: デンコボーイ司令室 (4.0帖 / ~6.5 m²)",
        color: "#ef4444",
        katabanSummary: "Ryzen 9 9950X3D + ROG CROSSHAIR X870E DARK HERO + ROG-ASTRAL-RTX5090-O32G-GAMING + 2x PG32UCDM3 (4K 240Hz OLED) + 2x AAS01 + M702 AZOTH EXTREME (US Layout) + P718 HARPE ACE EXTREME",
        desc: "Tu centro de mando principal para dirigir tu empresa (08:00–10:30 JST), stremear en Kick y grabar para YouTube (+$15,000 USD/mes). Equipada con la RTX 5090 Astral OC, 8TB NVMe (Gen5 + Gen4) y doble monitor OLED 4K 240Hz.",
        specs: [
          "Torre ROG «Sin Límites»: Ryzen 9 9950X3D + Crosshair X870E Dark Hero + ROG Astral RTX 5090 32GB = ¥2,106,644",
          "Doble Monitor OLED: 2x ASUS ROG Swift OLED PG32UCDM3 (DP 2.1a 80Gbps) + 2x Brazos ROG AAS01 = ¥486,840",
          "Periféricos ROG US Layout: Azoth Extreme US (¥89,800) + Harpe Ace Extreme Carbon (¥45,800) + Delta II + Carnyx = ¥215,575",
          "Muebles Comando: Escritorio Sanwa Direct 140×60cm (¥14,800) + Silla Nitori Queto VBT (¥24,990) + Cama Doble Nitori (¥34,990)"
        ]
      },
      node_ayame_gaming: {
        id: "node_ayame_gaming",
        shortLabel: "🎮 Zona Gaming あやめ + TV 55\" 4K (¥666,240)",
        title: "🎮 Zona Gaming de あやめ en Sala (LDK 12.7帖): ROG Zephyrus G16 White + PS5 Pro + Switch 2 + TV 55\" 4K",
        jpy: 666240,
        watts: 320,
        lan: "Wi-Fi 7 + HDMI 2.1 VRR 120Hz",
        zone: "LDK (12.7帖) · Centro de Entretenimiento frente al Sofá Nitori N-Shield",
        color: "#f472b6",
        katabanSummary: "ROG Zephyrus G16 White (¥350,000) + PlayStation 5 Pro (¥137,980) + Nintendo Switch 2 (¥59,980) + Logicool G735 White & DualSense Pink (¥38,480) + Smart TV 55\" 4K REGZA/Hisense (¥79,800)",
        desc: "El rincón sagrado de juegos de あやめ en la sala para disfrutar Kingdom Hearts, Final Fantasy y Blue Archive desde el sofá anti-arañazos Nitori N-Shield junto a nuestros 2 gatitos.",
        specs: [
          "Laptop Principal: ASUS ROG Zephyrus G16 White Edition OLED — ¥350,000",
          "Consolas: Sony PlayStation 5 Pro (¥137,980) + Nintendo Switch 2 (¥59,980)",
          "Audio & Control: Headset Logicool G735 White + DualSense Nova Pink — ¥38,480",
          "Pantalla Sala: Smart TV 55\" 4K UHD (REGZA / Hisense 55E6K) + Mueble TV Nitori — ¥79,800"
        ]
      },
      node_ldk_sofa_dining: {
        id: "node_ldk_sofa_dining",
        shortLabel: "🛋️ Sofá N-Shield + Comedor Nitori + Clima (¥164,480)",
        title: "🛋️ Sala-Comedor Funcional Nitori (LDK 12.7帖): Sofá N-Shield Anti-Arañazos + Mesa 4 Sillas + Purificador & Robot",
        jpy: 164480,
        watts: 110,
        lan: "IoT Wi-Fi 2.4GHz (Anker Eufy + Sharp KC-S50)",
        zone: "LDK (12.7帖) · Zona Social & Comedor de Citas de Miércoles",
        color: "#fbbf24",
        katabanSummary: "Nitori N-Shield 3人掛け (¥59,990) + Nitori ダイニングテーブル 4点セット (¥29,990) + Anker Eufy Robot Vacuum (¥34,800) + Sharp Plasmacluster KC-S50 (¥22,800) + Alfombra & 3x LED Techo (¥16,900)",
        desc: "Mobiliario 100% funcional de Nitori resistente a las uñas de los 2 gatitos (tela sintética N-Shield), comedor para las cenas carnívoras y las Citas #1 de Miércoles en Casa con あやめ.",
        specs: [
          "Sofá 3 Personas: Nitori N-Shield 傷・汚れに強い合成皮革 (Anti-arañazos de gato) — ¥59,990",
          "Comedor: Mesa Nitori + 4 Sillas (ダイニングテーブル 4点セット) — ¥29,990",
          "Limpieza Automática: Robot Aspirador + Fregado Anker Eufy Clean / Xiaomi S20+ — ¥34,800",
          "Aire Puro: Purificador + Humidificador Sharp Plasmacluster KC-S50 (¥22,800) + Alfombra & 3 Plafones LED (¥16,900)"
        ]
      },
      node_kitchen_carnivore: {
        id: "node_kitchen_carnivore",
        shortLabel: "🥩 Cocina Carnívora + Refri 282L Hanamasa (¥133,100)",
        title: "🍳 Cocina Hiper-Carnívora (LDK): Refrigerador 282L (Filetes Hanamasa) + Sartén Lodge 10.25\" + Zojirushi IH",
        jpy: 133100,
        watts: 1350,
        lan: "Circuito Dedicado Cocina 20A",
        zone: "LDK · Cocina Integral de 3 Quemadores con Campana Extractora",
        color: "#f97316",
        katabanSummary: "Hisense/Iris Ohyama 282L 冷凍冷蔵庫 (¥59,800) + Lodge 10.25\" Cast Iron & T-fal 9pz (¥16,800) + Zojirushi IH 5.5合 (¥18,800) + Sharp Oven 18L & T-fal Kettle (¥22,800) + Gyuto Seki Magoroku (¥14,900)",
        desc: "Diseñada para sellar 500–600g diarios de filetes Grass-Fed de Niku no Hanamasa (a 3 min) y Little Butcher (a 30m) con la técnica 3–2.5–4 min en hierro fundido Lodge. Cero alcohol 🚫🍺 y cero mango 🚫🥭.",
        specs: [
          "Refrigerador 282L: Hisense / Iris Ohyama 282L con gran congelador para carne de Hanamasa — ¥59,800",
          "Cocción Steaks: Sartén Hierro Fundido Lodge 10.25\" + Set 9 Pz T-fal Ingenio IH — ¥16,800",
          "Carbohidratos Pre-Entreno: Arrocera Zojirushi IH 5.5合 (象印 極め炊き) — ¥18,800",
          "Horno & Cuchillería: Microondas Sharp 18L + Hervidor T-fal (¥22,800) + Cuchillo Gyuto 関孫六 Seki Magoroku (¥14,900)"
        ]
      },
      node_chinchillas: {
        id: "node_chinchillas",
        shortLabel: "🐹 Store Room 1.4帖: Santuario 2 Chinchillas (¥66,420)",
        title: "🐹 Store Room (納戸 1.4帖 / ~2.3 m²): Santuario Climatizado para Nuestras 2 Chinchillas",
        jpy: 66420,
        watts: 210,
        lan: "SwitchBot Termómetro/Higrómetro BLE + Wi-Fi",
        zone: "Store Room (1.4帖) anexo al LDK · Temperatura controlada 18–21°C y humedad <50%",
        color: "#22c55e",
        katabanSummary: "SANKO Easy Home 60 High Mesh (¥18,500) + SANKO Metal Silent 38cm (¥7,980) + SANKO Play Bath (¥4,300) + Casitas Madera (¥8,700) + Oxbow/Timothy (¥8,940) + SwitchBot & Deshumidificador Sharp (¥18,000)",
        desc: "El Store Room de 1.4帖 anexo a la sala se convierte en una suite exclusiva y silenciosa para las 2 chinchillas, protegida de corrientes de aire, con monitoreo térmico SwitchBot y deshumidificador Sharp continuo.",
        specs: [
          "Jaula: SANKO Easy Home 60 High Mesh (三晃商会 イージーホーム60 ハイメッシュ) — ¥18,500",
          "Ejercicio & Baño Volcánico: Rueda SANKO Metal Silent 38cm (¥7,980) + SANKO Play Bath & Arena ×3 (¥4,300)",
          "Refugio & Nutrición: 2 Casitas de Madera SANKO (¥8,700) + Heno Timothy + Pellets Oxbow + Bebedero vidrio (¥8,940)",
          "Control Climático: Termómetro/Higrómetro SwitchBot + Deshumidificador Compacto Sharp — ¥18,000"
        ]
      },
      node_cats: {
        id: "node_cats",
        shortLabel: "🐱🐱 Circuito 2 Gatos + Barrera Entrada (¥75,980)",
        title: "🐱🐱 Santuario Funcional para Nuestros 2 Gatitos (LDK + Pasillo + Entrada Segura)",
        jpy: 75980,
        watts: 15,
        lan: "Dispensador Automático PETLIBRO Dual + Fuente Inox",
        zone: "LDK (Torre Mwpo + Hamacas de Ventana) + Lavabo (2x Kao Nyantomo) + Puerta (Noboren Nyan)",
        color: "#14b8a6",
        katabanSummary: "Torre Mwpo/Iris Ohyama (¥9,800) + Hamacas Ventana & Camas Nitori (¥7,980) + 2x Kao Nyantomo + 1x Inox XL (¥11,800) + PETLIBRO Dual + Fuente Inox (¥12,800) + Barrera Noboren Nyan 3 (¥18,800) + 2x Richell M (¥14,800)",
        desc: "Equipamiento 100% higiénico y seguro para nuestros 2 gatitos: regla 2N+1 de areneros (2 Kao Nyantomo doble rejilla + 1 acero inoxidable XL), torre rascador alta junto al balcón y barrera piso-a-techo en el Genkan.",
        specs: [
          "Verticalidad: Torre Rascador Alta Estabilidad Mwpo / Iris Ohyama (¥9,800) + Hamacas de ventana y camas Nitori (¥7,980)",
          "Higiene Cero Olor: 2x Areneros Doble Rejilla Kao ニャンとも清潔トイレ + 1x Arenero Acero Inox XL — ¥11,800",
          "Hidratación & Comida: Comedero Doble PETLIBRO 4L + Fuente Acero Inox 2.5L — ¥12,800",
          "Seguridad Anti-Escape: Barrera のぼれんニャン バリアフリー3 (¥18,800) + 2 Transportines Richell M (¥14,800)"
        ]
      },
      node_ayame_room: {
        id: "node_ayame_room",
        shortLabel: "🌸 Bed Room 1 (3.8帖 + WIC): Cuarto & Taller あやめ (¥114,440)",
        title: "🌸 Bed Room 1 (3.8帖 + Walk-In Closet): Santuario de Sueño 22:30 & Taller de Costura de あやめ",
        jpy: 114440,
        watts: 85,
        lan: "Cero Pantallas después de las 21:00 JST · Silencio Absoluto 22:30",
        zone: "Bed Room 1 (3.8帖 / ~6.2 m²) + Walk-In Closet (WIC)",
        color: "#ec4899",
        katabanSummary: "Cama Semi-Double Nitori + Pocket Coil (¥32,990) + Sábanas/Edredón/Almohadas (¥11,740) + Tocador LED Nitori (¥12,990) + Espejo & Rack (¥8,980) + Cortinas Blackout 1級 (¥9,960) + Máquina Brother/JUKI (¥29,800) + Maniquí Torso 9号 (¥7,980)",
        desc: "El refugio de paz de あやめ. Incluye cortinas Blackout de 1.er grado para garantizar oscuridad total a las 22:30 hrs, su tocador con luz LED y su taller textil donde confecciona las batas de Godzilla 1954, Mothra 1961 y el kimono de Wakamo.",
        specs: [
          "Descanso Sagrado 22:30: Cama Semi-Double Nitori con cajones + Colchón Pocket Coil (¥32,990) + Cortinas Blackout 1級 (¥9,960)",
          "Ropa de Cama Hotel Style: Sábanas Bedsure + Edredón All-Season (¥8,260) + 2 Almohadas Nitori Hotel Style (¥3,480)",
          "Belleza & WIC: Tocador Nitori con Espejo LED (¥12,990) + Espejo Cuerpo Entero & Rack (¥8,980) + Walk-In Closet integrado",
          "Taller Textil Imperial: Máquina de Coser Computarizada Brother / JUKI (¥29,800) + Maniquí Torso 9号 (¥7,980)"
        ]
      },
      node_bathroom_entrance: {
        id: "node_bathroom_entrance",
        shortLabel: "🚿 Baño 1317 + Lavadora 8kg MMA + Genkan (¥49,800+)",
        title: "🚿 Zona Húmeda (水回り) & Entrada (玄関 + SIC): Baño 1317 (21:15 hrs), Lavadora 8kg & Barrera Anti-Escape",
        jpy: 49800,
        watts: 420,
        lan: " extractor 24h + Calentador Automático Ofuro (追い焚き)",
        zone: "Pasillo Oeste · Baño 1317 + Lavabo + WC Bidet + Genkan con SIC",
        color: "#60a5fa",
        katabanSummary: "Lavadora Automática 8kg Hisense/Iris Ohyama (¥49,800 incluido en LDK) + Baño 1317 Ofuro (Ritual 21:15 con あやめ) + Shoes-In Closet (Casco Honda CB250R & Guantes Yokkao)",
        desc: "Infraestructura sanitaria japonesa independiente: bañera 1317 con calentador automático para el baño caliente de las 21:15 hrs con あやめ, lavadora automática de 8kg para lavar tus rashguards y shorts de Fighter's Flow a diario, y Shoes-In Closet para el equipo de tu Honda CB250R.",
        specs: [
          "Lavandería Diaria MMA: Lavadora Automática 8kg Hisense / Iris Ohyama (¥49,800) con toma de agua e impermeabilización",
          "Ritual Nocturno 21:15 JST: Baño 1317 con tina profunda Ofuro y secador de ropa en techo (浴室乾燥機)",
          "Sanitario Independiente: WC con Washlet térmico + Lavabo independiente (独立洗面台) con espacio para 2 areneros Kao Nyantomo",
          "Genkan + SIC: Shoes-In Closet para tus 6 pares de Air Jordan 1 US 13, casco Shoei/Arai de la CB250R y barrera Noboren Nyan 3"
        ]
      }
    };
  }

  function computeApartmentSummary() {
    const salaPc = getSalaPcConfig();
    const baseCapexWithoutSalaPc = 4184089; // Ayame 114,440 + Bruno Muebles 104,570 + ROG Sin Límites 2,809,059 + Gaming Ayame 586,440 + Chinchillas 66,420 + Gatos 75,980 + LDK 294,080 + Cocina 133,100
    const totalWithSalaPc = baseCapexWithoutSalaPc + salaPc.jpy;
    const peakWatts = 950 + salaPc.watts + 320 + 1350 + 420; // Bruno PC + Sala PC + TV/PS5 + Kitchen IH + Washer
    const breakerAmps = Math.round(peakWatts / 100);
    return {
      baseCapexWithoutSalaPc,
      salaPcJpy: salaPc.jpy,
      totalWithSalaPc,
      peakWatts,
      breakerAmps
    };
  }

  function renderGeneralBlueprintSVG() {
    const salaPc = getSalaPcConfig();
    const sel = state.selectedNodeId;
    const netLine = state.showNetworkOverlay ? `
      <!-- 10GbE LAN + Wi-Fi 7 Mesh Overlay -->
      <path d="M 455 185 L 455 245 L 555 245 L 555 295" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="7 4"/>
      <circle cx="455" cy="185" r="6" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
      <circle cx="555" cy="295" r="6" fill="#38bdf8" stroke="#fff" stroke-width="1.5"/>
      <rect x="420" y="226" width="155" height="20" rx="5" fill="#0c1424" stroke="#38bdf8" stroke-width="1"/>
      <text x="497" y="239" fill="#7dd3fc" font-size="9.5" font-weight="800" text-anchor="middle">⚡ Enlace Directo 10GbE LAN + Wi-Fi 7</text>
    ` : "";

    const pwrOverlay = state.showPowerOverlay ? `
      <g opacity="0.95">
        <rect x="35" y="18" width="215" height="22" rx="5" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1.2"/>
        <text x="142" y="33" fill="#fde047" font-size="10" font-weight="800" text-anchor="middle">⚡ Tablero 60A (6,000W) · 3 Circuitos Separados</text>
      </g>
    ` : "";

    return `
      <svg viewBox="0 0 860 540" class="fp-cad-svg" role="img" aria-label="Plano CAD Interactivo Urbanex Asakusabashi Front 2SLDK 50.18m²">
        <defs>
          <pattern id="cadGrid" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(148,163,184,0.08)" stroke-width="1"/>
          </pattern>
          <filter id="glowGold" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="0" stdDeviation="4" flood-color="#d4a853" flood-opacity="0.65"/>
          </filter>
        </defs>

        <!-- Background Grid -->
        <rect x="0" y="0" width="860" height="540" rx="12" fill="#080c14"/>
        <rect x="0" y="0" width="860" height="540" rx="12" fill="url(#cadGrid)"/>

        <!-- Title Header inside Blueprint -->
        <text x="24" y="28" fill="#d4a853" font-size="12" font-weight="800" font-family="monospace">URBANEX ASAKUSABASHI FRONT · 1301号室 (2SLDK 50.18m²) / 303号室 (3LDK 50.95m²) · CAD API v1.0</text>
        <text x="836" y="28" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="end" font-family="monospace">台東区柳橋1-13-6 · 浅草橋駅 徒歩1分 (80m)</text>

        <!-- Outer Apartment Walls -->
        <rect x="24" y="42" width="760" height="468" fill="#0d131f" stroke="#64748b" stroke-width="4" rx="4"/>

        <!-- ==================== ZONE 1: ENTRANCE, BATHROOM 1317, WASHER 8KG & WC (LEFT / WEST) ==================== -->
        <g class="fp-zone ${sel === "node_bathroom_entrance" ? "fp-zone-active" : ""}" data-node-id="node_bathroom_entrance" style="cursor:pointer;">
          <rect x="28" y="46" width="210" height="255" fill="rgba(56, 189, 248, 0.07)" stroke="#38bdf8" stroke-width="2"/>
          <text x="38" y="66" fill="#7dd3fc" font-size="12" font-weight="800">🚿 水回り &amp; 玄関 (Zona Húmeda)</text>
          <!-- Genkan + SIC -->
          <rect x="36" y="76" width="90" height="62" fill="#111827" stroke="#475569" stroke-width="1.5" rx="4"/>
          <text x="81" y="96" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">玄関 Genkan</text>
          <text x="81" y="111" fill="#94a3b8" font-size="8.5" text-anchor="middle">+ SIC (Casco CB250R</text>
          <text x="81" y="123" fill="#94a3b8" font-size="8.5" text-anchor="middle">&amp; 6 Jordan 1 US13)</text>
          <!-- Washer 8kg -->
          <rect x="134" y="76" width="96" height="62" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
          <text x="182" y="96" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">🧺 Lavadora 8kg</text>
          <text x="182" y="111" fill="#e2e8f0" font-size="8.5" text-anchor="middle">Gear MMA Diario</text>
          <text x="182" y="124" fill="#4ade80" font-size="9" font-weight="700" text-anchor="middle">¥49,800</text>
          <!-- Bath 1317 -->
          <rect x="36" y="146" width="115" height="92" fill="#0c192c" stroke="#60a5fa" stroke-width="1.5" rx="4"/>
          <text x="93" y="168" fill="#93c5fd" font-size="11" font-weight="800" text-anchor="middle">🛁 Baño 1317</text>
          <text x="93" y="184" fill="#e2e8f0" font-size="9" text-anchor="middle">Ofuro Caliente 21:15</text>
          <text x="93" y="198" fill="#f9a8d4" font-size="8.5" text-anchor="middle">Bruno &amp; あやめ</text>
          <text x="93" y="214" fill="#64748b" font-size="8" text-anchor="middle">浴室乾燥機 (Secador)</text>
          <!-- WC + Lavabo -->
          <rect x="157" y="146" width="73" height="92" fill="#111827" stroke="#475569" stroke-width="1.5" rx="4"/>
          <text x="193" y="168" fill="#cbd5e1" font-size="9.5" font-weight="700" text-anchor="middle">🚽 WC Bidet</text>
          <text x="193" y="186" fill="#cbd5e1" font-size="9" text-anchor="middle">独立洗面台</text>
          <text x="193" y="204" fill="#2dd4bf" font-size="8" text-anchor="middle">2x Areneros</text>
          <text x="193" y="216" fill="#2dd4bf" font-size="8" text-anchor="middle">Kao Nyantomo</text>
          <!-- Pet Gate -->
          <rect x="36" y="246" width="194" height="44" fill="rgba(20,184,166,0.14)" stroke="#14b8a6" stroke-width="1.5" rx="4"/>
          <text x="133" y="264" fill="#5eead4" font-size="9.5" font-weight="800" text-anchor="middle">🛡️ Barrera のぼれんニャン 3 (¥18,800)</text>
          <text x="133" y="279" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Anti-escape Piso a Techo en Pasillo</text>
        </g>

        <!-- ==================== ZONE 2: BED ROOM 1 — AYAME SANCTUARY & SEWING ATELIER (BOTTOM LEFT) ==================== -->
        <g class="fp-zone ${sel === "node_ayame_room" ? "fp-zone-active" : ""}" data-node-id="node_ayame_room" style="cursor:pointer;">
          <rect x="28" y="305" width="275" height="201" fill="rgba(236, 72, 153, 0.08)" stroke="#ec4899" stroke-width="2.2"/>
          <text x="38" y="325" fill="#f9a8d4" font-size="12.5" font-weight="800">🌸 Bed Room 1: あやめの部屋 (3.8帖 + WIC)</text>
          <text x="295" y="325" fill="#4ade80" font-size="11" font-weight="800" text-anchor="end">¥114,440</text>
          <!-- Semi-Double Bed -->
          <rect x="38" y="336" width="122" height="88" fill="#1f122b" stroke="#f472b6" stroke-width="1.6" rx="5"/>
          <text x="99" y="358" fill="#fbcfe8" font-size="10" font-weight="800" text-anchor="middle">🛏️ Cama Semi-Double</text>
          <text x="99" y="373" fill="#e2e8f0" font-size="8.5" text-anchor="middle">Nitori Pocket Coil</text>
          <text x="99" y="387" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">🌙 Regla Sagrada 22:30</text>
          <text x="99" y="401" fill="#4ade80" font-size="8.5" text-anchor="middle">¥32,990 + Ropa ¥11.7K</text>
          <!-- Sewing Atelier (Brother/JUKI + Torso 9号) -->
          <rect x="168" y="336" width="125" height="88" fill="#231433" stroke="#c084fc" stroke-width="1.6" rx="5"/>
          <text x="230" y="356" fill="#e9d5ff" font-size="10" font-weight="800" text-anchor="middle">🧵 Taller Textil あやめ</text>
          <text x="230" y="371" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Brother/JUKI (¥29,800)</text>
          <text x="230" y="384" fill="#cbd5e1" font-size="8.5" text-anchor="middle">+ Maniquí Torso 9号 (¥7,980)</text>
          <text x="230" y="399" fill="#f9a8d4" font-size="8" font-weight="700" text-anchor="middle">Batas Godzilla &amp; Mothra</text>
          <!-- WIC + Vanity + Blackout -->
          <rect x="38" y="432" width="122" height="64" fill="#181224" stroke="#a855f7" stroke-width="1.4" rx="4"/>
          <text x="99" y="452" fill="#d8b4fe" font-size="9.5" font-weight="800" text-anchor="middle">👗 Walk-In Closet (WIC)</text>
          <text x="99" y="467" fill="#cbd5e1" font-size="8.5" text-anchor="middle">+ Tocador LED (¥12,990)</text>
          <text x="99" y="481" fill="#cbd5e1" font-size="8" text-anchor="middle">+ Espejo Cuerpo Entero</text>
          <rect x="168" y="432" width="125" height="64" fill="#141824" stroke="#64748b" stroke-width="1.4" rx="4"/>
          <text x="230" y="454" fill="#f8fafc" font-size="9.5" font-weight="700" text-anchor="middle">🌑 Cortinas Blackout 1級</text>
          <text x="230" y="470" fill="#94a3b8" font-size="8.5" text-anchor="middle">Oscuridad 100% (¥9,960)</text>
          <text x="230" y="484" fill="#4ade80" font-size="8" text-anchor="middle">Silencio Total 22:30 hrs</text>
        </g>

        <!-- ==================== ZONE 3: BED ROOM 2 — DENKOBOY COMMAND CENTER (TOP CENTER) ==================== -->
        <g class="fp-zone ${sel === "node_bruno_pc" ? "fp-zone-active" : ""}" data-node-id="node_bruno_pc" style="cursor:pointer;">
          <rect x="242" y="46" width="265" height="255" fill="rgba(239, 68, 68, 0.09)" stroke="#ef4444" stroke-width="2.4"/>
          <text x="252" y="66" fill="#fca5a5" font-size="12" font-weight="800">💻 Bed Room 2: 司令室 (4.0帖)</text>
          <text x="499" y="66" fill="#fde047" font-size="11" font-weight="800" text-anchor="end">¥2,913,629</text>

          <!-- ROG SIN LÍMITES DESK -->
          <rect x="252" y="76" width="245" height="122" fill="#1c1118" stroke="#ef4444" stroke-width="2" rx="6"/>
          <text x="374" y="95" fill="#fde047" font-size="10.5" font-weight="900" text-anchor="middle">🔥 TORRE «SIN LÍMITES» ROG EXTREME</text>
          <text x="374" y="111" fill="#f8fafc" font-size="9" font-weight="700" text-anchor="middle">Ryzen 9 9950X3D + ROG Astral RTX 5090 32GB</text>
          <text x="374" y="125" fill="#7dd3fc" font-size="8.5" text-anchor="middle">2x OLED 31.5" 4K 240Hz (PG32UCDM3) + 2x Brazos AAS01</text>
          <text x="374" y="139" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Azoth Extreme (US Layout) + Harpe Carbon + Carnyx</text>
          <text x="374" y="154" fill="#cbd5e1" font-size="8" text-anchor="middle">Escritorio Sanwa 140cm + Silla Nitori Queto VBT</text>
          <rect x="284" y="163" width="180" height="24" rx="4" fill="rgba(239,68,68,0.25)" stroke="#ef4444" stroke-width="1"/>
          <text x="374" y="179" fill="#4ade80" font-size="10" font-weight="900" text-anchor="middle">PC: ¥2,809,059 + Muebles: ¥104,570</text>

          <!-- Bruno Double Bed -->
          <rect x="252" y="206" width="245" height="84" fill="#111827" stroke="#64748b" stroke-width="1.5" rx="5"/>
          <text x="374" y="229" fill="#e2e8f0" font-size="10" font-weight="700" text-anchor="middle">🛏️ Cama Doble Nitori + Pocket Coil (¥34,990)</text>
          <text x="374" y="246" fill="#94a3b8" font-size="8.5" text-anchor="middle">CEO Deep Work (08:00–10:30) · Stream Kick (10:30–12:30)</text>
          <text x="374" y="261" fill="#4ade80" font-size="8.5" font-weight="700" text-anchor="middle">Meta Ingresos: +$15,000+ USD/mes (Kick + YouTube)</text>
          <text x="374" y="276" fill="#cbd5e1" font-size="8" text-anchor="middle">Clóset Integrado + Cortinas Blackout 1級 (¥4,990)</text>
        </g>

        <!-- ==================== ZONE 4: STORE ROOM 1.4帖 — CHINCHILLA SANCTUARY ==================== -->
        <g class="fp-zone ${sel === "node_chinchillas" ? "fp-zone-active" : ""}" data-node-id="node_chinchillas" style="cursor:pointer;">
          <rect x="307" y="305" width="142" height="98" fill="rgba(34, 197, 94, 0.1)" stroke="#22c55e" stroke-width="2"/>
          <text x="378" y="324" fill="#86efac" font-size="10.5" font-weight="800" text-anchor="middle">🐹 Store Room (1.4帖)</text>
          <text x="378" y="340" fill="#f8fafc" font-size="9" font-weight="700" text-anchor="middle">Santuario 2 Chinchillas</text>
          <text x="378" y="354" fill="#cbd5e1" font-size="8" text-anchor="middle">SANKO Easy Home 60 High</text>
          <text x="378" y="367" fill="#cbd5e1" font-size="8" text-anchor="middle">Rueda 38cm + Deshumidif.</text>
          <text x="378" y="381" fill="#38bdf8" font-size="8" font-weight="700" text-anchor="middle">SwitchBot 18–21°C / &lt;50%</text>
          <text x="378" y="395" fill="#4ade80" font-size="9.5" font-weight="800" text-anchor="middle">¥66,420</text>
        </g>

        <!-- ==================== ZONE 5: CARNIVORE KITCHEN (TOP RIGHT LDK) ==================== -->
        <g class="fp-zone ${sel === "node_kitchen_carnivore" ? "fp-zone-active" : ""}" data-node-id="node_kitchen_carnivore" style="cursor:pointer;">
          <rect x="511" y="46" width="269" height="122" fill="rgba(249, 115, 22, 0.09)" stroke="#f97316" stroke-width="2"/>
          <text x="521" y="66" fill="#fdba74" font-size="11.5" font-weight="800">🍳 Cocina Hiper-Carnívora (キッチン)</text>
          <text x="772" y="66" fill="#4ade80" font-size="10.5" font-weight="800" text-anchor="end">¥133,100</text>
          <rect x="521" y="75" width="122" height="82" fill="#18130f" stroke="#f97316" stroke-width="1.4" rx="4"/>
          <text x="582" y="94" fill="#fed7aa" font-size="9.5" font-weight="800" text-anchor="middle">🥩 Refri 282L Hanamasa</text>
          <text x="582" y="109" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Hisense 282L (¥59,800)</text>
          <text x="582" y="123" fill="#cbd5e1" font-size="8" text-anchor="middle">500–600g/día Res Grass-Fed</text>
          <text x="582" y="137" fill="#fca5a5" font-size="8" font-weight="700" text-anchor="middle">0 Alcohol 🚫🍺 · 0 Mango 🚫🥭</text>
          <rect x="651" y="75" width="121" height="82" fill="#18130f" stroke="#fb923c" stroke-width="1.4" rx="4"/>
          <text x="711" y="94" fill="#fed7aa" font-size="9.5" font-weight="800" text-anchor="middle">🔥 Lodge 10.25" + IH</text>
          <text x="711" y="109" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Sellado 3–2.5–4 (¥16,800)</text>
          <text x="711" y="123" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Zojirushi IH 5.5合 (¥18,800)</text>
          <text x="711" y="137" fill="#cbd5e1" font-size="8" text-anchor="middle">Horno Sharp + Gyuto 関孫六</text>
        </g>

        <!-- ==================== ZONE 6: LDK (12.7帖) + NEW SALA PC WORKSTATION (#DREAMPCLIST) ==================== -->
        <rect x="453" y="172" width="327" height="334" fill="rgba(212, 168, 83, 0.05)" stroke="#d4a853" stroke-width="2.2"/>
        <text x="463" y="191" fill="#fde047" font-size="12" font-weight="900">🛋️ Living Dining (LDK 12.7帖 / ~20.6m²)</text>

        <!-- NEW! ESTACIÓN DE TRABAJO ASUS #DREAMPCLIST EN LA SALA -->
        <g class="fp-zone ${sel === "node_sala_pc" ? "fp-zone-active" : ""}" data-node-id="node_sala_pc" style="cursor:pointer;" filter="url(#glowGold)">
          <rect x="463" y="200" width="307" height="114" fill="rgba(56, 189, 248, 0.16)" stroke="${salaPc.color}" stroke-width="2.8" rx="7"/>
          <rect x="471" y="207" width="124" height="16" rx="4" fill="${salaPc.color}"/>
          <text x="533" y="218" fill="#080c14" font-size="8.5" font-weight="900" text-anchor="middle">🆕 ESTACIÓN PC EN SALA</text>
          <text x="762" y="219" fill="#fde047" font-size="11" font-weight="900" text-anchor="end">${fmtYen(salaPc.jpy)} (${fmtUsd(salaPc.jpy)})</text>
          <text x="616" y="238" fill="#ffffff" font-size="10.5" font-weight="900" text-anchor="middle">${salaPc.shortLabel}</text>
          <text x="616" y="254" fill="#bae6fd" font-size="8.5" font-weight="700" text-anchor="middle">
            ${state.salaPcMode === "ai_starter"
              ? "AMD Ryzen 7 9700X (AVX-512 65W) + ASUS Prime B850-PLUS WIFI + RTX 5060 Ti 16GB GDDR7"
              : (state.salaPcMode === "creator_extreme"
                  ? "Ryzen 9 9950X3D + ASUS ProArt X870E-CREATOR (10GbE) + RTX 5090 32GB + ProArt OLED"
                  : "Dual Sala: AI Starter AMD (¥334,400) + Content Creator Extreme ProArt (¥2,190,960)")}
          </text>
          <text x="616" y="269" fill="#e2e8f0" font-size="8.2" text-anchor="middle">
            ${state.salaPcMode === "ai_starter"
              ? "32GB DDR5-6000 CL30 + Prime LC 360 + 2TB NVMe + Prime 750G + Chasis Compacto AP202 / PA401"
              : "8TB NVMe (Gen5 SN8100 + Gen4 990 PRO) + ProArt LC 420 Noctua + ProArt PA602 con Ruedas"}
          </text>
          <text x="616" y="285" fill="#4ade80" font-size="8.5" font-weight="800" text-anchor="middle">
            🔌 Conectada por 10GbE LAN + Wi-Fi 7 al Cuarto de Bruno · LLMs Locales (Ollama/DeepSeek) &amp; Render 8K
          </text>
          <text x="616" y="303" fill="#fde047" font-size="8" font-weight="700" text-anchor="middle">
            👆 Haz clic aquí o usa el selector superior para alternar entre AI Starter AMD y Content Creator Extreme
          </text>
        </g>

        <!-- AYAME GAMING ZONE + 55" 4K TV IN SALA -->
        <g class="fp-zone ${sel === "node_ayame_gaming" ? "fp-zone-active" : ""}" data-node-id="node_ayame_gaming" style="cursor:pointer;">
          <rect x="463" y="322" width="152" height="90" fill="rgba(244, 114, 182, 0.1)" stroke="#f472b6" stroke-width="1.8" rx="6"/>
          <text x="539" y="340" fill="#f9a8d4" font-size="9.5" font-weight="800" text-anchor="middle">🎮 Gaming あやめ + TV 55"</text>
          <text x="539" y="355" fill="#e2e8f0" font-size="8.2" text-anchor="middle">ROG Zephyrus G16 (¥350K)</text>
          <text x="539" y="368" fill="#e2e8f0" font-size="8.2" text-anchor="middle">PS5 Pro (¥138K) + Switch 2</text>
          <text x="539" y="381" fill="#cbd5e1" font-size="8" text-anchor="middle">TV 55" 4K REGZA (¥79.8K)</text>
          <text x="539" y="398" fill="#4ade80" font-size="9" font-weight="800" text-anchor="middle">¥586,440 + TV ¥79.8K</text>
        </g>

        <!-- LDK SOFA N-SHIELD + DINING TABLE -->
        <g class="fp-zone ${sel === "node_ldk_sofa_dining" ? "fp-zone-active" : ""}" data-node-id="node_ldk_sofa_dining" style="cursor:pointer;">
          <rect x="621" y="322" width="149" height="90" fill="rgba(251, 191, 36, 0.09)" stroke="#fbbf24" stroke-width="1.8" rx="6"/>
          <text x="695" y="340" fill="#fde047" font-size="9.5" font-weight="800" text-anchor="middle">🛋️ Sofá N-Shield &amp; Comedor</text>
          <text x="695" y="355" fill="#e2e8f0" font-size="8.2" text-anchor="middle">Sofá 3P Anti-Uñas (¥59,990)</text>
          <text x="695" y="368" fill="#e2e8f0" font-size="8.2" text-anchor="middle">Mesa + 4 Sillas (¥29,990)</text>
          <text x="695" y="381" fill="#cbd5e1" font-size="8" text-anchor="middle">Anker Robot + Sharp KC-S50</text>
          <text x="695" y="398" fill="#4ade80" font-size="9" font-weight="800" text-anchor="middle">LDK Total: ¥294,080</text>
        </g>

        <!-- CAT SANCTUARY IN LDK -->
        <g class="fp-zone ${sel === "node_cats" ? "fp-zone-active" : ""}" data-node-id="node_cats" style="cursor:pointer;">
          <rect x="307" y="410" width="142" height="90" fill="rgba(20, 184, 166, 0.1)" stroke="#14b8a6" stroke-width="1.8" rx="6"/>
          <text x="378" y="429" fill="#5eead4" font-size="9.5" font-weight="800" text-anchor="middle">🐱🐱 Santuario 2 Gatos</text>
          <text x="378" y="444" fill="#e2e8f0" font-size="8" text-anchor="middle">Torre Mwpo Alta (¥9,800)</text>
          <text x="378" y="457" fill="#e2e8f0" font-size="8" text-anchor="middle">PETLIBRO Dual + Fuente Inox</text>
          <text x="378" y="470" fill="#cbd5e1" font-size="8" text-anchor="middle">Hamacas Ventana + Richell M</text>
          <text x="378" y="486" fill="#4ade80" font-size="9" font-weight="800" text-anchor="middle">¥75,980</text>

          <rect x="463" y="420" width="307" height="78" fill="rgba(20, 184, 166, 0.08)" stroke="#14b8a6" stroke-width="1.5" rx="6"/>
          <text x="616" y="442" fill="#5eead4" font-size="10" font-weight="800" text-anchor="middle">☀️ Ventanal Panorámico Sur/Este + Hamacas Solares para los 2 Gatitos</text>
          <text x="616" y="459" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Torre Rascador Mwpo junto al balcón · Comedero Automático Doble PETLIBRO · Purificador Sharp Plasmacluster</text>
          <text x="616" y="476" fill="#94a3b8" font-size="8" text-anchor="middle">Citas de Miércoles en Casa (19:00–21:00 JST) + Mimos con los gatitos a las 22:00 JST</text>
        </g>

        <!-- BALCONY (RIGHT EDGE) -->
        <rect x="788" y="42" width="52" height="468" fill="#0b111c" stroke="#475569" stroke-width="2" stroke-dasharray="6 4" rx="4"/>
        <text x="814" y="276" fill="#94a3b8" font-size="11" font-weight="800" text-anchor="middle" transform="rotate(90 814 276)">🌤️ BALCÓN EXTERIOR (バルコニー) · Luz Natural &amp; Ventilación</text>

        ${netLine}
        ${pwrOverlay}
      </svg>
    `;
  }

  function renderLdkDetailedSVG() {
    const salaPc = getSalaPcConfig();
    const sel = state.selectedNodeId;
    return `
      <svg viewBox="0 0 860 520" class="fp-cad-svg" role="img" aria-label="Plano CAD Detallado de la Sala LDK 12.7帖 con la nueva PC ASUS #dreampclist">
        <rect x="0" y="0" width="860" height="520" rx="12" fill="#070b12"/>
        <text x="24" y="28" fill="#38bdf8" font-size="12.5" font-weight="900" font-family="monospace">ZOOM ARQUITECTÓNICO: SALA-COMEDOR-COCINA (LDK 12.7帖 / ~20.6m²) + ESTACIÓN PC #DREAMPCLIST + STORE ROOM (1.4帖)</text>

        <!-- Main LDK Frame -->
        <rect x="20" y="42" width="760" height="456" fill="#0d1422" stroke="#d4a853" stroke-width="3" rx="6"/>

        <!-- 1. NEW SALA PC WORKSTATION (#DREAMPCLIST) — TOP LEFT / CENTER OF LDK -->
        <g class="fp-zone ${sel === "node_sala_pc" ? "fp-zone-active" : ""}" data-node-id="node_sala_pc" style="cursor:pointer;">
          <rect x="34" y="56" width="435" height="190" fill="rgba(56, 189, 248, 0.14)" stroke="${salaPc.color}" stroke-width="3" rx="8"/>
          <rect x="46" y="66" width="195" height="20" rx="4" fill="${salaPc.color}"/>
          <text x="143" y="80" fill="#06090f" font-size="9.5" font-weight="900" text-anchor="middle">🆕 ESTACIÓN PC DE SALA (LDK 12.7帖)</text>
          <text x="455" y="81" fill="#fde047" font-size="13" font-weight="900" text-anchor="end">${fmtYen(salaPc.jpy)}</text>

          <text x="46" y="104" fill="#ffffff" font-size="11.5" font-weight="900">${salaPc.shortLabel} (${fmtUsd(salaPc.jpy)})</text>
          <text x="46" y="122" fill="#bae6fd" font-size="9.2" font-weight="700">
            ${state.salaPcMode === "ai_starter"
              ? "• CPU: AMD Ryzen 7 9700X (Zen 5 AVX-512 512-bit · 65W) — ¥53,800 ($319 USD)"
              : "• CPU: AMD Ryzen 9 9950X3D (16C/32T · ¥109,980) o Intel Core Ultra 9 285K (24C Quick Sync · ¥92,800)"}
          </text>
          <text x="46" y="138" fill="#e2e8f0" font-size="9">
            ${state.salaPcMode === "ai_starter"
              ? "• M/B & GPU: ASUS Prime B850-PLUS WIFI (¥37,800) + RTX 5060 Ti 16GB GDDR7 FP4 (¥96,800)"
              : "• M/B & GPU: ASUS ProArt X870E-CREATOR 10GbE (¥89,800) + ROG Astral RTX 5090 32GB (¥1,199,800)"}
          </text>
          <text x="46" y="154" fill="#e2e8f0" font-size="9">
            ${state.salaPcMode === "ai_starter"
              ? "• RAM & SSD: 32GB DDR5-6000 CL30 EXPO (¥62,000) + 2TB NVMe Gen4 7,000MB/s (¥25,800)"
              : "• RAM & SSD: 64GB/128GB DDR5 (¥123,800) + 8TB NVMe (4TB SN8100 Gen5 + 4TB 990 PRO Gen4 = ¥267,980)"}
          </text>
          <text x="46" y="170" fill="#e2e8f0" font-size="9">
            ${state.salaPcMode === "ai_starter"
              ? "• AIO, PSU & Case: Prime LC 360 ARGB (¥19,800) + Prime 750W Gold ATX 3.1 (¥19,800) + Prime AP202 / PA401 (¥18,600)"
              : "• AIO, PSU & Case: ProArt LC 420 Noctua (¥46,800) + ProArt 1200W (¥72,000) + ProArt PA602 Wood c/Ruedas (¥42,800)"}
          </text>
          <text x="46" y="188" fill="#4ade80" font-size="9" font-weight="800">
            ${state.salaPcMode === "ai_starter"
              ? "🤖 Rol en la Sala: Servidor de LLMs Locales (Ollama/DeepSeek/Llama), Stable Diffusion, MuseTree & Salida HDMI 2.1 a TV 55\""
              : "🎬 Rol en la Sala: Estación ProArt 8K RAW + Monitor ASUS ProArt PA32UCDM 4K 240Hz OLED ΔE<1 (¥238,000) / PA32KCX 8K"}
          </text>

          <!-- Visual Desk & Tower Icon inside LDK -->
          <rect x="46" y="200" width="410" height="36" rx="5" fill="#091322" stroke="#38bdf8" stroke-width="1.2"/>
          <text x="251" y="222" fill="#7dd3fc" font-size="9.5" font-weight="800" text-anchor="middle">
            🔌 Toma ONT Fibra Gratis + Switch 10GbE LAN ↔ Conectada a Bed Room 2 («Sin Límites» ROG)
          </text>
        </g>

        <!-- 2. CARNIVORE KITCHEN & 282L FRIDGE (TOP RIGHT OF LDK) -->
        <g class="fp-zone ${sel === "node_kitchen_carnivore" ? "fp-zone-active" : ""}" data-node-id="node_kitchen_carnivore" style="cursor:pointer;">
          <rect x="483" y="56" width="283" height="190" fill="rgba(249, 115, 22, 0.1)" stroke="#f97316" stroke-width="2.2" rx="8"/>
          <text x="497" y="80" fill="#fdba74" font-size="12" font-weight="900">🍳 Cocina Hiper-Carnívora (¥133,100)</text>
          <text x="497" y="102" fill="#f8fafc" font-size="9.5" font-weight="700">• Refrigerador 282L Hisense/Iris Ohyama: ¥59,800</text>
          <text x="497" y="118" fill="#cbd5e1" font-size="8.8">  (Gran congelador para filetes de Niku no Hanamasa 24h)</text>
          <text x="497" y="136" fill="#f8fafc" font-size="9.5" font-weight="700">• Sartén Hierro Fundido Lodge 10.25\" + T-fal 9pz: ¥16,800</text>
          <text x="497" y="152" fill="#cbd5e1" font-size="8.8">  (Sellado perfecto 3–2.5–4 min · 500–600g res/día)</text>
          <text x="497" y="170" fill="#f8fafc" font-size="9.5" font-weight="700">• Arrocera Zojirushi IH 5.5合 (極め炊き): ¥18,800</text>
          <text x="497" y="188" fill="#f8fafc" font-size="9.5" font-weight="700">• Microondas/Horno Sharp 18L + T-fal Kettle: ¥22,800</text>
          <text x="497" y="206" fill="#f8fafc" font-size="9.5" font-weight="700">• Cuchillo Gyuto 関孫六 + Tabla + Vajilla: ¥14,900</text>
          <text x="497" y="228" fill="#4ade80" font-size="9" font-weight="800">🥩 Little Butcher a 30m · Niku no Hanamasa 24h a 3 min</text>
        </g>

        <!-- 3. STORE ROOM 1.4帖 — CHINCHILLAS (BOTTOM LEFT) -->
        <g class="fp-zone ${sel === "node_chinchillas" ? "fp-zone-active" : ""}" data-node-id="node_chinchillas" style="cursor:pointer;">
          <rect x="34" y="260" width="215" height="224" fill="rgba(34, 197, 94, 0.1)" stroke="#22c55e" stroke-width="2.2" rx="8"/>
          <text x="141" y="284" fill="#86efac" font-size="11.5" font-weight="900" text-anchor="middle">🐹 Store Room (納戸 1.4帖)</text>
          <text x="141" y="302" fill="#ffffff" font-size="10" font-weight="800" text-anchor="middle">Santuario 2 Chinchillas (¥66,420)</text>
          <text x="46" y="324" fill="#e2e8f0" font-size="8.8">• Jaula SANKO Easy Home 60 High: ¥18,500</text>
          <text x="46" y="342" fill="#e2e8f0" font-size="8.8">• Rueda SANKO 38cm Metal Silent: ¥7,980</text>
          <text x="46" y="360" fill="#e2e8f0" font-size="8.8">• SANKO Play Bath + Arena ×3: ¥4,300</text>
          <text x="46" y="378" fill="#e2e8f0" font-size="8.8">• 2x Casitas Madera SANKO: ¥8,700</text>
          <text x="46" y="396" fill="#e2e8f0" font-size="8.8">• Heno Timothy + Oxbow + Vidrio: ¥8,940</text>
          <text x="46" y="414" fill="#38bdf8" font-size="8.8" font-weight="700">• SwitchBot + Deshumidif. Sharp: ¥18,000</text>
          <rect x="46" y="430" width="190" height="40" rx="5" fill="#0b1f17" stroke="#22c55e" stroke-width="1"/>
          <text x="141" y="447" fill="#4ade80" font-size="8.5" font-weight="800" text-anchor="middle">🌡️ Clima Fijo 18–21°C · Humedad &lt;50%</text>
          <text x="141" y="461" fill="#cbd5e1" font-size="8" text-anchor="middle">Aislado del ruido y sin corrientes</text>
        </g>

        <!-- 4. AYAME GAMING SETUP + 55" 4K TV (BOTTOM CENTER) -->
        <g class="fp-zone ${sel === "node_ayame_gaming" ? "fp-zone-active" : ""}" data-node-id="node_ayame_gaming" style="cursor:pointer;">
          <rect x="261" y="260" width="250" height="224" fill="rgba(244, 114, 182, 0.1)" stroke="#f472b6" stroke-width="2.2" rx="8"/>
          <text x="386" y="284" fill="#f9a8d4" font-size="11.5" font-weight="900" text-anchor="middle">🎮 Zona Gaming あやめ + TV 55\" 4K</text>
          <text x="386" y="302" fill="#fde047" font-size="10.5" font-weight="800" text-anchor="middle">Setup Gaming: ¥586,440 + TV: ¥79,800</text>
          <text x="273" y="324" fill="#e2e8f0" font-size="9">• ROG Zephyrus G16 White OLED: ¥350,000</text>
          <text x="273" y="342" fill="#e2e8f0" font-size="9">• Sony PlayStation 5 Pro: ¥137,980</text>
          <text x="273" y="360" fill="#e2e8f0" font-size="9">• Nintendo Switch 2: ¥59,980</text>
          <text x="273" y="378" fill="#e2e8f0" font-size="9">• Logicool G735 White + DualSense Pink: ¥38,480</text>
          <text x="273" y="396" fill="#38bdf8" font-size="9" font-weight="700">• Smart TV 55\" 4K UHD + Mueble Nitori: ¥79,800</text>
          <rect x="273" y="416" width="226" height="54" rx="5" fill="#1f122b" stroke="#f472b6" stroke-width="1.2"/>
          <text x="386" y="436" fill="#fbcfe8" font-size="9" font-weight="800" text-anchor="middle">👑 Kingdom Hearts · Final Fantasy · Blue Archive</text>
          <text x="386" y="454" fill="#cbd5e1" font-size="8.2" text-anchor="middle">Conectada también a la PC de Sala por HDMI 2.1</text>
        </g>

        <!-- 5. SOFA NITORI N-SHIELD + DINING TABLE + CAT TOWER (BOTTOM RIGHT) -->
        <g class="fp-zone ${sel === "node_ldk_sofa_dining" ? "fp-zone-active" : ""}" data-node-id="node_ldk_sofa_dining" style="cursor:pointer;">
          <rect x="523" y="260" width="243" height="224" fill="rgba(251, 191, 36, 0.09)" stroke="#fbbf24" stroke-width="2.2" rx="8"/>
          <text x="644" y="284" fill="#fde047" font-size="11.5" font-weight="900" text-anchor="middle">🛋️ Sala Nitori + Comedor + Gatos</text>
          <text x="535" y="308" fill="#e2e8f0" font-size="8.8">• Sofá 3P Nitori N-Shield Anti-Arañazos: ¥59,990</text>
          <text x="535" y="326" fill="#e2e8f0" font-size="8.8">• Mesa Comedor Nitori + 4 Sillas: ¥29,990</text>
          <text x="535" y="344" fill="#e2e8f0" font-size="8.8">• Robot Aspirador/Fregado Anker Eufy: ¥34,800</text>
          <text x="535" y="362" fill="#e2e8f0" font-size="8.8">• Purificador Sharp Plasmacluster KC-S50: ¥22,800</text>
          <text x="535" y="380" fill="#e2e8f0" font-size="8.8">• Alfombra Lavable + 3x LED Techo Nitori: ¥16,900</text>
          <text x="535" y="398" fill="#5eead4" font-size="8.8" font-weight="700">• Torre Gatos Mwpo (¥9,800) + PETLIBRO (¥12,800)</text>
          <rect x="535" y="416" width="218" height="54" rx="5" fill="#17201c" stroke="#14b8a6" stroke-width="1.2"/>
          <text x="644" y="436" fill="#5eead4" font-size="9" font-weight="800" text-anchor="middle">🐱🐱 Hamacas Solares en Ventanal del Balcón</text>
          <text x="644" y="454" fill="#cbd5e1" font-size="8.2" text-anchor="middle">Cita #1 de Miércoles en Casa con あやめ</text>
        </g>

        <!-- Balcony Strip -->
        <rect x="786" y="42" width="54" height="456" fill="#0b111c" stroke="#475569" stroke-width="2" stroke-dasharray="6 4" rx="4"/>
        <text x="813" y="270" fill="#94a3b8" font-size="11" font-weight="800" text-anchor="middle" transform="rotate(90 813 270)">🌤️ BALCÓN PANORÁMICO (バルコニー)</text>
      </svg>
    `;
  }

  function renderDenkoBoyRoomSVG() {
    return `
      <svg viewBox="0 0 860 460" class="fp-cad-svg" role="img" aria-label="Plano CAD Bed Room 2 DenkoBoy Command Center 4.0帖">
        <rect x="0" y="0" width="860" height="460" rx="12" fill="#080b12"/>
        <text x="24" y="28" fill="#ef4444" font-size="12.5" font-weight="900" font-family="monospace">BED ROOM 2: デンコボーイ司令室 (4.0帖 / ~6.5m²) — CONFIGURACIÓN «SIN LÍMITES» (NIVEL 3: EXTREME TOPE ABSOLUTO · ¥2,809,059)</text>

        <rect x="24" y="42" width="812" height="398" fill="#101420" stroke="#ef4444" stroke-width="3" rx="8"/>

        <!-- Desk & ROG Sin Límites Rig -->
        <g class="fp-zone fp-zone-active" data-node-id="node_bruno_pc" style="cursor:pointer;">
          <rect x="42" y="60" width="490" height="240" fill="#1a1018" stroke="#ef4444" stroke-width="2.5" rx="8"/>
          <text x="287" y="86" fill="#fde047" font-size="13" font-weight="900" text-anchor="middle">🔥 ESTACIÓN PRINCIPAL «SIN LÍMITES» (¥2,809,059 JPY / ~$19,109 USD)</text>
          <text x="58" y="112" fill="#ffffff" font-size="10" font-weight="700">1. Torre Full ASUS ROG (¥2,106,644):</text>
          <text x="58" y="129" fill="#cbd5e1" font-size="9">• CPU: AMD Ryzen 9 9950X3D BOX (¥109,980) · M/B: ROG Crosshair X870E Dark Hero (¥138,000)</text>
          <text x="58" y="145" fill="#fca5a5" font-size="9" font-weight="700">• GPU: ASUS ROG Astral GeForce RTX 5090 32GB GDDR7 OC (ROG-ASTRAL-RTX5090-O32G-GAMING · ¥1,199,800)</text>
          <text x="58" y="161" fill="#cbd5e1" font-size="9">• AIO: ROG Ryuo IV SLC 360 ARGB AMOLED 2K (¥52,980) · RAM: G.Skill 64GB DDR5-6000 CL30 (¥123,800)</text>
          <text x="58" y="177" fill="#cbd5e1" font-size="9">• SSDs (8TB): WD_Black SN8100 4TB Gen5 14,900MB/s (¥139,980) + Samsung 990 PRO 4TB Gen4 (¥128,000)</text>
          <text x="58" y="193" fill="#cbd5e1" font-size="9">• PSU &amp; Case: ROG Thor 1200W Platinum III GaN (¥80,524) + ROG Cronox GR801 LCD 9.2" (¥105,980) + 6x Eurux (¥27,600)</text>

          <text x="58" y="217" fill="#7dd3fc" font-size="10" font-weight="700">2. Doble Pantalla OLED 4K 240Hz (¥486,840): 2x PG32UCDM3 (¥429,840) + 2x Brazos ROG AAS01 (¥57,000)</text>
          <text x="58" y="237" fill="#4ade80" font-size="10" font-weight="700">3. Periféricos ROG US Layout (¥215,575): Azoth Extreme US (¥89,800) + Harpe Carbon (¥45,800) + Delta II + Carnyx</text>
          <text x="58" y="257" fill="#fde047" font-size="9.5" font-weight="700">4. Escritorio &amp; Silla Columna VBT: Sanwa Direct 140×60cm (¥14,800) + Nitori Queto Ergonómica (¥24,990) + Quntis LED (¥11,460)</text>
          <text x="58" y="280" fill="#38bdf8" font-size="9" font-weight="800">⚡ Conectada por cable Cat8 10GbE LAN directo a la Estación ASUS #dreampclist de la Sala (LDK 12.7帖)</text>
        </g>

        <!-- Double Bed & Closet in Bruno's Room -->
        <rect x="550" y="60" width="268" height="240" fill="#111827" stroke="#64748b" stroke-width="2" rx="8"/>
        <text x="684" y="92" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">🛏️ Zona de Descanso &amp; Clóset</text>
        <text x="566" y="120" fill="#e2e8f0" font-size="9.5">• Cama Doble Nitori + Pocket Coil: ¥34,990</text>
        <text x="566" y="140" fill="#e2e8f0" font-size="9.5">• Sábanas Kumori 4pz + Edredón D: ¥9,860</text>
        <text x="566" y="160" fill="#e2e8f0" font-size="9.5">• 2x Almohadas Nitori Hotel Style: ¥3,480</text>
        <text x="566" y="180" fill="#e2e8f0" font-size="9.5">• Cortinas Blackout 1級 Nitori: ¥4,990</text>
        <text x="566" y="210" fill="#fde047" font-size="9.5" font-weight="700">📦 Clóset Empotrado (Guardarropa XL):</text>
        <text x="566" y="228" fill="#cbd5e1" font-size="8.8">  12 Hoodies Billabong XL, 8 Jeans Levi's</text>
        <text x="566" y="244" fill="#cbd5e1" font-size="8.8">  36×32, Batas Custom ShodaiGoji 1954</text>
        <text x="566" y="260" fill="#cbd5e1" font-size="8.8">  &amp; Colección Yokkao / Venum Pro</text>

        <!-- Production Schedule Banner at Bottom of Room 2 -->
        <rect x="42" y="316" width="776" height="106" fill="rgba(56, 189, 248, 0.09)" stroke="#38bdf8" stroke-width="1.8" rx="8"/>
        <text x="430" y="340" fill="#38bdf8" font-size="11.5" font-weight="900" text-anchor="middle">⏱️ OPERACIÓN DIARIA EN EL COMMAND CENTER (META OBLIGATORIA: +$15,000+ USD/MES EN KICK &amp; YOUTUBE + EMPRESA)</text>
        <text x="430" y="362" fill="#f8fafc" font-size="9.5" text-anchor="middle">• 08:00–10:30 JST (Lun–Vie): Sprint CEO &amp; Ingeniería de tu Empresa ($8,500–$10,000+ USD/mes)</text>
        <text x="430" y="381" fill="#4ade80" font-size="9.5" font-weight="700" text-anchor="middle">• 10:30–12:30 JST (Lun–Vie): Stream en Vivo por Kick (Prime Time LatAm/USA · $8,500+/mes) + Edición YouTube 19:30–21:00 ($6,500+/mes)</text>
        <text x="430" y="402" fill="#f9a8d4" font-size="9.5" font-weight="700" text-anchor="middle">• 21:00 JST: Cámaras 100% Apagadas · 21:15 Baño caliente con あやめ · 22:30 hrs Sueño Sagrado</text>
      </svg>
    `;
  }

  function renderAyameRoomSVG() {
    return `
      <svg viewBox="0 0 860 440" class="fp-cad-svg" role="img" aria-label="Plano CAD Bed Room 1 Cuarto y Taller Textil de Ayame 3.8帖 + WIC">
        <rect x="0" y="0" width="860" height="440" rx="12" fill="#090812"/>
        <text x="24" y="28" fill="#f472b6" font-size="12.5" font-weight="900" font-family="monospace">BED ROOM 1: あやめの部屋 &amp; アトリエ (3.8帖 + WALK-IN CLOSET · CAPEX FUNCIONAL: ¥114,440)</text>

        <rect x="24" y="42" width="812" height="378" fill="#140f1d" stroke="#ec4899" stroke-width="3" rx="8"/>

        <!-- Semi-Double Bed & 22:30 Sleep Sanctuary -->
        <rect x="42" y="60" width="370" height="220" fill="#1f142e" stroke="#f472b6" stroke-width="2" rx="8"/>
        <text x="227" y="88" fill="#fbcfe8" font-size="12" font-weight="900" text-anchor="middle">🛏️ Santuario de Sueño Sagrado (22:30 JST)</text>
        <text x="58" y="114" fill="#f8fafc" font-size="9.5" font-weight="700">• Cama Semi-Double Nitori + Colchón Pocket Coil: ¥32,990</text>
        <text x="58" y="134" fill="#e2e8f0" font-size="9.5">• Sábanas Bedsure 3pz + Edredón All-Season SD: ¥8,260</text>
        <text x="58" y="154" fill="#e2e8f0" font-size="9.5">• 2x Almohadas Nitori Hotel Style Memory Foam: ¥3,480</text>
        <text x="58" y="174" fill="#fde047" font-size="9.5" font-weight="700">• Cortinas Blackout 1級 Nitori + Mesa de Noche: ¥9,960</text>
        <text x="58" y="198" fill="#cbd5e1" font-size="8.8">  (Bloqueo del 99.99% de luz solar y ruido exterior para proteger</text>
        <text x="58" y="214" fill="#cbd5e1" font-size="8.8">  la estabilidad emocional y el descanso de あやめ con la Dra. Nishimatsu)</text>
        <text x="58" y="244" fill="#4ade80" font-size="9.5" font-weight="800">🌙 Regla de Oro: 21:15 Ofuro · 22:00 Gatitos · 22:30 Dormir</text>

        <!-- Sewing Atelier & WIC -->
        <rect x="430" y="60" width="388" height="220" fill="#211530" stroke="#c084fc" stroke-width="2" rx="8"/>
        <text x="624" y="88" fill="#e9d5ff" font-size="12" font-weight="900" text-anchor="middle">🧵 Taller Textil Imperial &amp; Walk-In Closet (WIC)</text>
        <text x="446" y="114" fill="#f8fafc" font-size="9.5" font-weight="700">• Máquina de Coser Computarizada Brother / JUKI: ¥29,800</text>
        <text x="446" y="134" fill="#f8fafc" font-size="9.5" font-weight="700">• Maniquí de Costura Profesional (洋裁用トルソー 9号): ¥7,980</text>
        <text x="446" y="154" fill="#e2e8f0" font-size="9.5">• Tocador Funcional Nitori + Espejo LED: ¥12,990</text>
        <text x="446" y="174" fill="#e2e8f0" font-size="9.5">• Espejo Cuerpo Entero + Rack de Prendas Nitori: ¥8,980</text>
        <text x="446" y="200" fill="#f9a8d4" font-size="9" font-weight="700">👘 Creaciones de Alta Costura de あやめ (Telas de Nippori):</text>
        <text x="446" y="218" fill="#cbd5e1" font-size="8.8">  1) Kimono carmesí de Wakamo (Blue Archive)</text>
        <text x="446" y="234" fill="#cbd5e1" font-size="8.8">  2) Haori de Godzilla 1954 (ShodaiGoji) + Vestido de Mothra 1961</text>
        <text x="446" y="250" fill="#cbd5e1" font-size="8.8">     para su entrada juntos en tu 6.ª Pelea del 6-0 (Sep 2029)</text>

        <!-- Bottom Wellness & Nippori Connection -->
        <rect x="42" y="296" width="776" height="104" fill="rgba(244, 114, 182, 0.09)" stroke="#f472b6" stroke-width="1.6" rx="8"/>
        <text x="430" y="322" fill="#f9a8d4" font-size="11" font-weight="900" text-anchor="middle">💜 CONEXIÓN DIRECTA CON SU BIENESTAR Y CREATIVIDAD (OPEX MENSUAL DEDICADO: ¥200,000 + SALUD MENTAL ¥27K–¥52K)</text>
        <text x="430" y="344" fill="#e2e8f0" font-size="9.2" text-anchor="middle">• A 5 min en tu Honda CB250R (4 min en tren) de Ai Clinic Kanda (Dra. Yoshiko Nishimatsu) y Counseling Room haco</text>
        <text x="430" y="364" fill="#e2e8f0" font-size="9.2" text-anchor="middle">• A 11 min en moto (10 min JR) de Nippori Fabric Town (日暮里繊維街 · 90+ tiendas de sedas, brocados Nishijin-ori y terciopelo)</text>
        <text x="430" y="384" fill="#4ade80" font-size="9.2" font-weight="700" text-anchor="middle">• Y cuando quiere editar patrones digitales o usar IA generativa (MuseTree), tiene la nueva PC ASUS #dreampclist en la Sala (LDK)</text>
      </svg>
    `;
  }

  function renderBathroomEntranceSVG() {
    return `
      <svg viewBox="0 0 860 430" class="fp-cad-svg" role="img" aria-label="Plano CAD Zona Húmeda Baño 1317 Lavadora 8kg y Entrada Segura">
        <rect x="0" y="0" width="860" height="430" rx="12" fill="#070c14"/>
        <text x="24" y="28" fill="#38bdf8" font-size="12.5" font-weight="900" font-family="monospace">ZONA HÚMEDA &amp; ENTRADA SEGURA (水回り・玄関・SIC): BAÑO 1317, LAVADORA 8KG MMA, ARENEROS &amp; BARRERA GATOS</text>

        <rect x="24" y="42" width="812" height="368" fill="#0d1524" stroke="#38bdf8" stroke-width="2.5" rx="8"/>

        <!-- 1. Genkan + SIC + Pet Gate -->
        <rect x="42" y="60" width="250" height="330" fill="#111827" stroke="#14b8a6" stroke-width="2" rx="8"/>
        <text x="167" y="88" fill="#5eead4" font-size="11.5" font-weight="900" text-anchor="middle">🚪 1. 玄関 Genkan + SIC + Barrera</text>
        <text x="56" y="114" fill="#f8fafc" font-size="9.2" font-weight="700">• Shoes-In Closet (SIC):</text>
        <text x="56" y="132" fill="#cbd5e1" font-size="8.6">  Espacio cerrado para tus 6 pares de</text>
        <text x="56" y="147" fill="#cbd5e1" font-size="8.6">  Air Jordan 1 High OG (Talla US 13),</text>
        <text x="56" y="162" fill="#cbd5e1" font-size="8.6">  casco integral y chamarra de tu</text>
        <text x="56" y="177" fill="#cbd5e1" font-size="8.6">  Honda CB250R ShodaiGoji.</text>
        <rect x="56" y="200" width="222" height="170" rx="6" fill="rgba(20,184,166,0.12)" stroke="#14b8a6" stroke-width="1.5"/>
        <text x="167" y="224" fill="#5eead4" font-size="10" font-weight="800" text-anchor="middle">🛡️ Barrera のぼれんニャン 3</text>
        <text x="167" y="242" fill="#4ade80" font-size="10" font-weight="800" text-anchor="middle">¥18,800 JPY</text>
        <text x="167" y="262" fill="#e2e8f0" font-size="8.5" text-anchor="middle">Barrera piso-a-techo sin taladrar</text>
        <text x="167" y="278" fill="#e2e8f0" font-size="8.5" text-anchor="middle">que impide al 100% que los 2 gatitos</text>
        <text x="167" y="294" fill="#e2e8f0" font-size="8.5" text-anchor="middle">salgan al corredor cuando llegas</text>
        <text x="167" y="310" fill="#e2e8f0" font-size="8.5" text-anchor="middle">con bolsas de carne de Hanamasa</text>
        <text x="167" y="326" fill="#e2e8f0" font-size="8.5" text-anchor="middle">o tu maleta de Fighter's Flow.</text>

        <!-- 2. Powder Room, 8kg Washing Machine & Cat Litter Zone -->
        <rect x="308" y="60" width="250" height="330" fill="#111827" stroke="#38bdf8" stroke-width="2" rx="8"/>
        <text x="433" y="88" fill="#7dd3fc" font-size="11.5" font-weight="900" text-anchor="middle">🧺 2. Lavandería MMA 8kg &amp; Lavabo</text>
        <text x="322" y="114" fill="#f8fafc" font-size="9.2" font-weight="700">• Lavadora Automática 8kg:</text>
        <text x="322" y="132" fill="#4ade80" font-size="9.5" font-weight="800">  Hisense / Iris Ohyama 8kg (¥49,800)</text>
        <text x="322" y="150" fill="#cbd5e1" font-size="8.6">  Indispensable en Japón (los deptos</text>
        <text x="322" y="165" fill="#cbd5e1" font-size="8.6">  se entregan sin lavadora). Lava a</text>
        <text x="322" y="180" fill="#cbd5e1" font-size="8.6">  diario tus shorts Yokkao XL, vendas y</text>
        <text x="322" y="195" fill="#cbd5e1" font-size="8.6">  rashguards tras entrenar con Suzuki.</text>
        <rect x="322" y="215" width="222" height="155" rx="6" fill="rgba(56,189,248,0.1)" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="433" y="238" fill="#7dd3fc" font-size="9.8" font-weight="800" text-anchor="middle">🐱 Higiene Gatuna 2N+1 (¥11,800)</text>
        <text x="433" y="258" fill="#e2e8f0" font-size="8.5" text-anchor="middle">• 2x Kao ニャンとも清潔トイレ</text>
        <text x="433" y="274" fill="#e2e8f0" font-size="8.5" text-anchor="middle">  (Doble rejilla con pellets de pino</text>
        <text x="433" y="290" fill="#e2e8f0" font-size="8.5" text-anchor="middle">  y tapete absorbente cero olor)</text>
        <text x="433" y="308" fill="#e2e8f0" font-size="8.5" text-anchor="middle">• + 1x Arenero Acero Inoxidable XL</text>
        <text x="433" y="326" fill="#4ade80" font-size="8.5" font-weight="700" text-anchor="middle">Ventilación Continua 24 Horas</text>

        <!-- 3. Unit Bath 1317 & Independent WC -->
        <rect x="574" y="60" width="244" height="330" fill="#111827" stroke="#60a5fa" stroke-width="2" rx="8"/>
        <text x="696" y="88" fill="#93c5fd" font-size="11.5" font-weight="900" text-anchor="middle">🛁 3. Baño 1317 (Ofuro) &amp; WC</text>
        <text x="588" y="114" fill="#f8fafc" font-size="9.2" font-weight="700">• Tina Japonesa 1317 (130×170cm):</text>
        <text x="588" y="132" fill="#f9a8d4" font-size="9" font-weight="700">  Ritual Sagrado 21:15 JST con あやめ</text>
        <text x="588" y="150" fill="#cbd5e1" font-size="8.6">  Recuperación muscular post-sparring</text>
        <text x="588" y="165" fill="#cbd5e1" font-size="8.6">  y relajación parasimpática antes</text>
        <text x="588" y="180" fill="#cbd5e1" font-size="8.6">  de dormir a las 22:30 hrs.</text>
        <text x="588" y="205" fill="#f8fafc" font-size="9.2" font-weight="700">• 浴室乾燥機 (Secador en Techo):</text>
        <text x="588" y="223" fill="#cbd5e1" font-size="8.6">  Convierte el baño en cámara de</text>
        <text x="588" y="238" fill="#cbd5e1" font-size="8.6">  secado tibio para tu equipo de MMA</text>
        <text x="588" y="253" fill="#cbd5e1" font-size="8.6">  en días de lluvia o invierno.</text>
        <text x="588" y="278" fill="#f8fafc" font-size="9.2" font-weight="700">• WC Independiente con Washlet:</text>
        <text x="588" y="296" fill="#cbd5e1" font-size="8.6">  Separado del área de ducha al</text>
        <text x="588" y="311" fill="#cbd5e1" font-size="8.6">  100% (estándar japonés バストイレ別).</text>
      </svg>
    `;
  }

  function renderMadoriEngineeringSVG() {
    const salaPc = getSalaPcConfig();
    const sum = computeApartmentSummary();
    return `
      <svg viewBox="0 0 860 440" class="fp-cad-svg" role="img" aria-label="Comparativa Arquitectónica RF12 Unidad 1301 vs 303 y Topología 10GbE">
        <rect x="0" y="0" width="860" height="440" rx="12" fill="#070a10"/>
        <text x="24" y="28" fill="#d4a853" font-size="12.5" font-weight="900" font-family="monospace">INGENIERÍA DEL DEPARTAMENTO (RF12): UNIDAD 1301 (2SLDK) VS 303 (3LDK) + TOPOLOGÍA 10GbE LAN &amp; CARGA 60A</text>

        <!-- Left Card: Unit 303 vs Unit 1301 -->
        <rect x="24" y="44" width="400" height="182" fill="#0f172a" stroke="#d4a853" stroke-width="2" rx="8"/>
        <text x="40" y="70" fill="#fde047" font-size="11.5" font-weight="900">🏢 Comparativa Oficial RF12 — Urbanex Asakusabashi Front</text>
        <text x="40" y="92" fill="#4ade80" font-size="9.5" font-weight="800">• Opción A — Unidad 303 (3LDK · 50.95 m² · Piso 3):</text>
        <text x="40" y="108" fill="#e2e8f0" font-size="8.8">  Renta ¥269,000 + ¥20,000 管理費 = ¥289,000/mes</text>
        <text x="40" y="123" fill="#86efac" font-size="8.8" font-weight="700">  Con 2 meses Free Rent → Costo Efectivo: ¥266,580/mes</text>
        <text x="40" y="147" fill="#38bdf8" font-size="9.5" font-weight="800">• Opción B — Unidad 1301 (2SLDK · 50.18 m² · Piso 13):</text>
        <text x="40" y="163" fill="#e2e8f0" font-size="8.8">  Renta ¥310,000 + ¥20,000 管理費 = ¥330,000/mes</text>
        <text x="40" y="178" fill="#7dd3fc" font-size="8.8" font-weight="700">  Con 3 meses Free Rent → Costo Efectivo: ¥288,750/mes</text>
        <text x="40" y="204" fill="#cbd5e1" font-size="8.5">✅ Ambas con: 0 Depósito · 0 Reikin · 0 Comisión · Fibra Gratis · Pet-Friendly</text>

        <!-- Right Card: 10GbE Network Topology between Bruno's Room and Living Room PC -->
        <rect x="438" y="44" width="398" height="182" fill="#0f172a" stroke="#38bdf8" stroke-width="2" rx="8"/>
        <text x="454" y="70" fill="#7dd3fc" font-size="11.5" font-weight="900">🌐 Topología de Red 10GbE LAN + Wi-Fi 7 (Cuarto ↔ Sala)</text>
        <text x="454" y="92" fill="#f8fafc" font-size="9" font-weight="700">1. Nodo Central (Bed Room 2 · 4.0帖): Torre «Sin Límites» ROG</text>
        <text x="454" y="108" fill="#cbd5e1" font-size="8.5">   ROG Crosshair X870E Dark Hero (LAN 5G/2.5G + Wi-Fi 7) + RTX 5090 32GB</text>
        <text x="454" y="130" fill="#f8fafc" font-size="9" font-weight="700">2. Nodo de Sala (LDK 12.7帖): ${salaPc.shortLabel}</text>
        <text x="454" y="146" fill="#cbd5e1" font-size="8.5">   Conectada junto al ONT de Fibra Óptica del edificio mediante Switch 10GbE.</text>
        <text x="454" y="168" fill="#4ade80" font-size="8.8" font-weight="700">⚡ Flujo Dual sin pérdida de FPS en tus Streams de Kick (10:30–12:30 JST):</text>
        <text x="454" y="184" fill="#cbd5e1" font-size="8.4">   La PC de la Sala puede correr inferencia LLM local (Ollama/DeepSeek) o</text>
        <text x="454" y="199" fill="#cbd5e1" font-size="8.4">   renderizar tus videos 4K/8K de YouTube mientras tu PC principal stremea.</text>

        <!-- Bottom Card: Electrical Telemetry (60A / 6,000W) & CAPEX Synchronization -->
        <rect x="24" y="240" width="812" height="176" fill="#111827" stroke="#22c55e" stroke-width="2" rx="8"/>
        <text x="40" y="266" fill="#4ade80" font-size="11.5" font-weight="900">⚡ Telemetría de Carga Eléctrica (Breaker 60A = 6,000W) &amp; Resumen CAPEX Sincronizado</text>
        <text x="40" y="290" fill="#e2e8f0" font-size="9.2">• Circuito 1 (Bed Room 2 · 20A): Torre ROG «Sin Límites» RTX 5090 + 2x OLED (~950W pico en carga extrema)</text>
        <text x="40" y="310" fill="#e2e8f0" font-size="9.2">• Circuito 2 (Sala LDK · 20A): ${salaPc.shortLabel} (~${salaPc.watts}W) + TV 55\" 4K &amp; PS5 Pro de あやめ (~320W)</text>
        <text x="40" y="330" fill="#e2e8f0" font-size="9.2">• Circuito 3 (Cocina &amp; Clima · 20A): Refri 282L + Zojirushi IH + Microondas Sharp + Deshumidificador Chinchillas (~1,560W)</text>
        <text x="40" y="354" fill="#fde047" font-size="10" font-weight="800">
          🔋 Demanda Pico Simultánea Estimada: ~${sum.peakWatts.toLocaleString("en-US")}W (${sum.breakerAmps}A de 60A disponibles → Margen seguro del ${Math.round(100 - (sum.peakWatts / 6000) * 100)}%)
        </text>
        <text x="40" y="380" fill="#38bdf8" font-size="10" font-weight="900">
          💰 CAPEX Base Casa (c/Torre «Sin Límites»): ${fmtYen(sum.baseCapexWithoutSalaPc)} + Estación PC de Sala (${fmtYen(sum.salaPcJpy)}) = ${fmtYen(sum.totalWithSalaPc)} (${fmtUsd(sum.totalWithSalaPc)})
        </text>
        <text x="40" y="400" fill="#94a3b8" font-size="8.5">
          Nota: Los planos estáticos antiguos mostraban un CAPEX desactualizado de ¥2,849,139 (con una PC de ¥680,000). Esta API CAD mantiene todos los cuartos 100% sincronizados.
        </text>
      </svg>
    `;
  }

  function renderActiveBlueprintSVG() {
    switch (state.activeTab) {
      case "general":
        return renderGeneralBlueprintSVG();
      case "ldk":
        return renderLdkDetailedSVG();
      case "denkoboy":
        return renderDenkoBoyRoomSVG();
      case "ayame":
        return renderAyameRoomSVG();
      case "bathroom":
        return renderBathroomEntranceSVG();
      case "madori":
        return renderMadoriEngineeringSVG();
      default:
        return renderGeneralBlueprintSVG();
    }
  }

  function injectStyles() {
    if (document.getElementById("imperio-floorplan-api-styles")) return;
    const st = document.createElement("style");
    st.id = "imperio-floorplan-api-styles";
    st.textContent = `
      .fp-api-shell {
        background: linear-gradient(165deg, rgba(13, 18, 28, 0.98) 0%, rgba(8, 11, 18, 0.99) 100%);
        border: 1px solid rgba(212, 168, 83, 0.42);
        border-radius: 14px;
        padding: 18px;
        margin-top: 12px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55);
      }
      .fp-top-controls {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        justify-content: space-between;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.32);
        border-radius: 10px;
        padding: 11px 14px;
        margin-bottom: 12px;
      }
      .fp-btn-pill {
        background: rgba(30, 41, 59, 0.85);
        color: #cbd5e1;
        border: 1px solid rgba(148, 163, 184, 0.3);
        border-radius: 8px;
        padding: 6px 11px;
        font-size: 0.75rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.16s ease;
      }
      .fp-btn-pill:hover {
        border-color: #38bdf8;
        color: #fff;
      }
      .fp-btn-pill.active {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.28), rgba(212, 168, 83, 0.22));
        border-color: #38bdf8;
        color: #fff;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.28);
      }
      .fp-tabs-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
        gap: 8px;
        margin-bottom: 14px;
      }
      .fp-tab-card {
        background: rgba(17, 24, 39, 0.9);
        border: 1px solid rgba(148, 163, 184, 0.24);
        border-radius: 9px;
        padding: 9px 12px;
        text-align: left;
        cursor: pointer;
        color: #e2e8f0;
        transition: all 0.16s ease;
      }
      .fp-tab-card:hover {
        border-color: #d4a853;
        transform: translateY(-1px);
      }
      .fp-tab-card.active {
        background: linear-gradient(135deg, rgba(212, 168, 83, 0.22), rgba(56, 189, 248, 0.15));
        border-color: #d4a853;
        box-shadow: 0 0 14px rgba(212, 168, 83, 0.25);
      }
      .fp-tab-card .fp-tab-title {
        font-size: 0.8rem;
        font-weight: 800;
        color: #fff;
      }
      .fp-tab-card .fp-tab-badge {
        font-size: 0.69rem;
        color: #38bdf8;
        font-weight: 700;
        margin-top: 2px;
      }
      .fp-main-stage {
        display: grid;
        grid-template-columns: 1.55fr 1fr;
        gap: 14px;
        align-items: start;
      }
      @media (max-width: 1024px) {
        .fp-main-stage {
          grid-template-columns: 1fr;
        }
      }
      .fp-canvas-box {
        background: #070b12;
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 12px;
        padding: 10px;
        overflow: hidden;
      }
      .fp-cad-svg {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 8px;
      }
      .fp-zone {
        transition: opacity 0.15s ease, filter 0.15s ease;
      }
      .fp-zone:hover {
        filter: brightness(1.18);
      }
      .fp-zone-active rect:first-of-type {
        stroke-width: 3.4px !important;
      }
      .fp-inspector-box {
        background: rgba(15, 22, 34, 0.96);
        border: 1px solid rgba(212, 168, 83, 0.4);
        border-radius: 12px;
        padding: 14px;
      }
      .fp-node-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 12px;
      }
      .fp-node-pill {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(148, 163, 184, 0.28);
        color: #cbd5e1;
        border-radius: 7px;
        padding: 5px 9px;
        font-size: 0.72rem;
        font-weight: 700;
        cursor: pointer;
      }
      .fp-node-pill.active {
        border-color: #fde047;
        color: #fde047;
        background: rgba(212, 168, 83, 0.18);
      }
      .fp-spec-list {
        list-style: none;
        padding: 0;
        margin: 10px 0 0 0;
      }
      .fp-spec-list li {
        font-size: 0.78rem;
        color: #e2e8f0;
        padding: 5px 0;
        border-bottom: 1px dashed rgba(148, 163, 184, 0.16);
        line-height: 1.45;
      }
    `;
    document.head.appendChild(st);
  }

  function renderFloorPlanApp() {
    const mount = document.getElementById("apartment-floorplan-api-mount");
    if (!mount) return;
    detectJpyRate();
    injectStyles();

    const nodes = getAllNodes();
    const activeNode = nodes[state.selectedNodeId] || nodes.node_sala_pc;
    const salaPc = getSalaPcConfig();
    const summary = computeApartmentSummary();
    const activeTabObj = ROOM_TABS.find(t => t.id === state.activeTab) || ROOM_TABS[0];

    mount.innerHTML = `
      <div class="fp-api-shell">
        <!-- HEADER & LIVE TELEMETRY BAR -->
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
          <div>
            <span style="display:inline-block; background:rgba(56,189,248,0.18); border:1px solid #38bdf8; color:#7dd3fc; font-size:0.7rem; font-weight:800; padding:3px 9px; border-radius:999px; letter-spacing:0.05em;">
              📐 API CAD INTERACTIVA v1.0 · URBANEX ASAKUSABASHI FRONT (2SLDK 50.18m² / 3LDK 50.95m²)
            </span>
            <h3 style="margin:6px 0 2px 0; color:#f8fafc; font-size:1.06rem;">
              🏠 Mapeo Arquitectónico en Vivo por Habitación + 🆕 Estación de Sala ASUS <code>#dreampclist</code> (LDK 12.7帖)
            </h3>
            <p style="margin:0; font-size:0.79rem; color:#94a3b8;">
              Todos los planos del departamento reformulados por API con costos sincronizados al yen, topología de red <strong>10GbE LAN + Wi-Fi 7</strong> y la nueva estación de trabajo ASUS en la <strong>Sala (LDK 12.7帖)</strong>.
            </p>
          </div>
          <div style="text-align:right; font-size:0.75rem; color:#cbd5e1;">
            <div>CAPEX Base Casa + ROG «Sin Límites»: <strong style="color:#fde047;">${fmtYen(summary.baseCapexWithoutSalaPc)}</strong></div>
            <div>+ Estación PC en Sala (LDK 12.7帖): <strong style="color:#38bdf8;">${fmtYen(summary.salaPcJpy)}</strong></div>
            <div>Total Integrado c/Sala PC: <strong style="color:#4ade80;">${fmtYen(summary.totalWithSalaPc)} (${fmtUsd(summary.totalWithSalaPc)})</strong></div>
          </div>
        </div>

        <!-- SELECTOR DE LA ESTACIÓN PC EN LA SALA (LDK 12.7帖) & OVERLAYS -->
        <div class="fp-top-controls">
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <span style="font-size:0.75rem; font-weight:800; color:#38bdf8;">🛋️ Configurar Estación PC de la Sala (LDK 12.7帖):</span>
            <button type="button" class="fp-btn-pill ${state.salaPcMode === "ai_starter" ? "active" : ""}" data-sala-mode="ai_starter">
              🤖 1. AI Starter AMD (¥334,400 / ~$2,230 USD)
            </button>
            <button type="button" class="fp-btn-pill ${state.salaPcMode === "creator_extreme" ? "active" : ""}" data-sala-mode="creator_extreme">
              🎬 2. Content Creator Extreme ProArt (¥2,190,960 c/OLED)
            </button>
            <button type="button" class="fp-btn-pill ${state.salaPcMode === "both" ? "active" : ""}" data-sala-mode="both">
              ⚡ Ambas en Sala (¥2,525,360)
            </button>
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:6px; align-items:center;">
            <button type="button" class="fp-btn-pill ${state.showNetworkOverlay ? "active" : ""}" id="fp-toggle-net">
              🌐 Red 10GbE LAN
            </button>
            <button type="button" class="fp-btn-pill ${state.showPowerOverlay ? "active" : ""}" id="fp-toggle-pwr">
              ⚡ Carga 60A (${summary.peakWatts}W)
            </button>
            <button type="button" class="fp-btn-pill ${state.showReferenceImage ? "active" : ""}" id="fp-toggle-refimg">
              🖼️ ${state.showReferenceImage ? "Ocultar Lámina Clásica" : "Ver Lámina Clásica Referencia"}
            </button>
          </div>
        </div>

        <!-- 6 PESTAÑAS DE MAPAS ARQUITECTÓNICOS DEL APARTAMENTO -->
        <div class="fp-tabs-grid">
          ${ROOM_TABS.map(t => `
            <button type="button" class="fp-tab-card ${state.activeTab === t.id ? "active" : ""}" data-fp-tab="${t.id}">
              <div class="fp-tab-title">${t.label}</div>
              <div class="fp-tab-badge">${t.badge}</div>
            </button>
          `).join("")}
        </div>

        <!-- ESCENARIO PRINCIPAL: PLANO SVG CAD INTERACTIVO (IZQUIERDA) + INSPECTOR DE NODO (DERECHA) -->
        <div class="fp-main-stage">
          <div class="fp-canvas-box">
            ${renderActiveBlueprintSVG()}
            ${state.showReferenceImage ? `
              <div style="margin-top:12px; padding-top:10px; border-top:1px solid rgba(148,163,184,0.2);">
                <div style="font-size:0.75rem; color:#94a3b8; margin-bottom:6px; font-weight:700;">
                  🖼️ Lámina arquitectónica de referencia original (${activeTabObj.label}):
                </div>
                <img src="${activeTabObj.legacyImg}" alt="${activeTabObj.label}" style="width:100%; border-radius:8px; border:1px solid rgba(255,255,255,0.12);">
              </div>
            ` : ""}
          </div>

          <!-- INSPECTOR DE ZONA / NODO SELECCIONADO -->
          <div class="fp-inspector-box">
            <div style="font-size:0.7rem; font-weight:800; color:#d4a853; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:6px;">
              🔍 INSPECTOR DE ZONA DEL APARTAMENTO (CLIC EN EL MAPA O EN LOS BOTONES)
            </div>
            <div class="fp-node-pills">
              ${Object.values(nodes).map(n => `
                <button type="button" class="fp-node-pill ${state.selectedNodeId === n.id ? "active" : ""}" data-select-node="${n.id}">
                  ${n.shortLabel}
                </button>
              `).join("")}
            </div>

            <div style="background:rgba(8,12,20,0.9); border-left:4px solid ${activeNode.color}; border-radius:8px; padding:12px;">
              <div style="font-size:0.72rem; color:#38bdf8; font-weight:700;">📍 ${activeNode.zone}</div>
              <h4 style="margin:4px 0 6px 0; color:#ffffff; font-size:0.96rem; line-height:1.35;">${activeNode.title}</h4>
              <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom:8px;">
                <span style="font-family:'Orbitron',monospace; font-size:1.15rem; font-weight:900; color:#fde047;">${fmtYen(activeNode.jpy)}</span>
                <span style="font-size:0.8rem; font-weight:800; color:#4ade80;">${fmtUsd(activeNode.jpy)}</span>
                <span style="font-size:0.72rem; background:rgba(56,189,248,0.15); color:#7dd3fc; padding:2px 7px; border-radius:5px; font-weight:700;">⚡ ~${activeNode.watts}W</span>
              </div>
              <p style="font-size:0.79rem; color:#cbd5e1; margin:0 0 8px 0; line-height:1.48;">
                ${activeNode.desc}
              </p>
              <div style="font-size:0.72rem; color:#94a3b8; background:#06090f; padding:7px 9px; border-radius:6px; border:1px solid rgba(148,163,184,0.2); font-family:monospace; margin-bottom:8px;">
                <strong style="color:#fca5a5;">Códigos / Equipamiento Clave:</strong><br>
                ${activeNode.katabanSummary}
              </div>
              <div style="font-size:0.72rem; color:#fde047; font-weight:700;">📋 Desglose Técnico en esta Zona:</div>
              <ul class="fp-spec-list">
                ${(activeNode.specs || []).map(s => `<li>${s}</li>`).join("")}
              </ul>
              <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                <span style="font-size:0.72rem; color:#94a3b8;">🌐 Red: <strong style="color:#e2e8f0;">${activeNode.lan}</strong></span>
                <a href="#rog-sin-limites-card" style="font-size:0.75rem; font-weight:800; color:#4ade80; text-decoration:underline;">
                  Ver Tabla de Códigos 型番 en CAPEX ↗
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    // Bind events
    mount.querySelectorAll("[data-fp-tab]").forEach(btn => {
      btn.addEventListener("click", () => {
        const tabId = btn.getAttribute("data-fp-tab") || "general";
        state.activeTab = tabId;
        if (tabId === "ldk") state.selectedNodeId = "node_sala_pc";
        if (tabId === "denkoboy") state.selectedNodeId = "node_bruno_pc";
        if (tabId === "ayame") state.selectedNodeId = "node_ayame_room";
        if (tabId === "bathroom") state.selectedNodeId = "node_bathroom_entrance";
        renderFloorPlanApp();
      });
    });

    mount.querySelectorAll("[data-sala-mode]").forEach(btn => {
      btn.addEventListener("click", () => {
        const mode = btn.getAttribute("data-sala-mode") || "ai_starter";
        state.salaPcMode = mode;
        state.selectedNodeId = "node_sala_pc";
        if (typeof window.setImperioSalaStationMode === "function") {
          window.setImperioSalaStationMode(mode);
        }
        renderFloorPlanApp();
      });
    });

    mount.querySelectorAll("[data-node-id]").forEach(el => {
      el.addEventListener("click", () => {
        const nid = el.getAttribute("data-node-id");
        if (nid) {
          state.selectedNodeId = nid;
          renderFloorPlanApp();
        }
      });
    });

    mount.querySelectorAll("[data-select-node]").forEach(btn => {
      btn.addEventListener("click", () => {
        const nid = btn.getAttribute("data-select-node");
        if (nid) {
          state.selectedNodeId = nid;
          renderFloorPlanApp();
        }
      });
    });

    const netBtn = document.getElementById("fp-toggle-net");
    if (netBtn) netBtn.addEventListener("click", () => { state.showNetworkOverlay = !state.showNetworkOverlay; renderFloorPlanApp(); });

    const pwrBtn = document.getElementById("fp-toggle-pwr");
    if (pwrBtn) pwrBtn.addEventListener("click", () => { state.showPowerOverlay = !state.showPowerOverlay; renderFloorPlanApp(); });

    const refBtn = document.getElementById("fp-toggle-refimg");
    if (refBtn) refBtn.addEventListener("click", () => { state.showReferenceImage = !state.showReferenceImage; renderFloorPlanApp(); });
  }

  // Listen for updates from the ROG / #dreampclist API in #capex
  window.addEventListener("imperio:asus-station-updated", e => {
    if (e && e.detail && e.detail.salaStationMode) {
      if (state.salaPcMode !== e.detail.salaStationMode) {
        state.salaPcMode = e.detail.salaStationMode;
        renderFloorPlanApp();
      }
    }
  });

  // Override legacy showPlan() so any existing buttons also drive the interactive CAD API
  window.showPlan = function (planName, btn) {
    state.activeTab = planName || "general";
    if (planName === "ldk") state.selectedNodeId = "node_sala_pc";
    if (planName === "denkoboy") state.selectedNodeId = "node_bruno_pc";
    if (planName === "ayame") state.selectedNodeId = "node_ayame_room";
    if (planName === "bathroom") state.selectedNodeId = "node_bathroom_entrance";
    renderFloorPlanApp();
    if (btn) {
      document.querySelectorAll(".plan-tab").forEach(t => t.classList.remove("active"));
      btn.classList.add("active");
    }
  };

  function init() {
    renderFloorPlanApp();
    setTimeout(renderFloorPlanApp, 1200);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
