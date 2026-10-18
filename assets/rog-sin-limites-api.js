/**
 * AKIHABARA ROG «SIN LÍMITES» HARDWARE & KATABAN LIVE PRICE TRACKER API v3.0
 * Tracks exact Japanese retail Kataban (型番) codes, real store links (Kakaku.com,
 * TSUKUMO eX., PC Shop ARK, Yodobashi Camera Akiba, Amazon.co.jp), Yodobashi 10%
 * Gold Point hack, CPU/Switch toggles, and the Akihabara Counter Script.
 */
(function () {
  "use strict";

  const FALLBACK_DATA = {
    meta: {
      api_name: "Akihabara ROG «Sin Límites» Hardware & Kataban Price Tracker API",
      version: "3.0.0-extreme",
      tier: "Nivel 3: Extreme Tope Absoluto (Sin Límites)",
      updated_at: "2026-10-18T06:30:00Z",
      location: "Akihabara Electric Town, Chiyoda-ku, Tokyo (a 4 min / 1.4 km de Urbanex Asakusabashi Front en tu Honda CB250R)"
    },
    tower_components: [
      {
        id: "cpu_9950x3d",
        slot: "cpu",
        option_group: "cpu_choice",
        option_key: "9950x3d",
        is_default: true,
        category: "Procesador (Opción 1: Tope Absoluto 16 Núcleos)",
        name: "AMD Ryzen 9 9950X3D (16C/32T · 144MB 3D V-Cache · 5.7 GHz)",
        kataban: "Ryzen 9 9950X3D BOX",
        kataban_alt: "100-100000719WOF",
        price_doc_jpy: 109980,
        price_live_jpy: 126764,
        price_live_note: "¥109,980 (Base/Promo Set) · ¥126,764 en PC Shop ARK / ¥132,800 en Tsukumo",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/100-100000719WOF/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=Ryzen+9+9950X3D",
          ark: "https://www.ark-pc.co.jp/search/?key=100-100000719WOF",
          amazon: "https://www.amazon.co.jp/s?k=100-100000719WOF"
        }
      },
      {
        id: "cpu_9850x3d",
        slot: "cpu",
        option_group: "cpu_choice",
        option_key: "9850x3d",
        is_default: false,
        category: "Procesador (Opción 2: Puro Gaming 8 Núcleos)",
        name: "AMD Ryzen 7 9850X3D (8C/16T · 3D V-Cache Puro Gaming)",
        kataban: "Ryzen 7 9850X3D BOX",
        kataban_alt: "Ryzen 7 9800X3D BOX",
        price_doc_jpy: 69940,
        price_live_jpy: 69940,
        price_live_note: "¥69,940 en TSUKUMO / PC Shop ARK",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/Ryzen%207%209800X3D%20BOX/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=Ryzen+7+9800X3D",
          ark: "https://www.ark-pc.co.jp/search/?key=9800X3D",
          amazon: "https://www.amazon.co.jp/s?k=Ryzen+7+9800X3D+BOX"
        }
      },
      {
        id: "motherboard",
        slot: "mb",
        category: "Tarjeta Madre",
        name: "ASUS ROG Crosshair X870E Dark Hero (o Edition 20 · Wi-Fi 7 · PCIe 5.0)",
        kataban: "ROG CROSSHAIR X870E DARK HERO",
        kataban_alt: "ROG CROSSHAIR X870E HERO",
        price_doc_jpy: 138000,
        price_live_jpy: 135900,
        price_live_note: "¥138,000 en ARK/Tsukumo · ¡¥135,900 hoy en Kakaku.com!",
        best_store: "Pasokon Koubou / ARK / TSUKUMO",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20CROSSHAIR%20X870E/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG+CROSSHAIR+X870E",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG+CROSSHAIR+X870E",
          amazon: "https://www.amazon.co.jp/s?k=ROG+CROSSHAIR+X870E+HERO"
        }
      },
      {
        id: "gpu_rtx5090",
        slot: "gpu",
        category: "Tarjeta Gráfica (GPU)",
        name: "ASUS ROG Astral GeForce RTX 5090 32GB GDDR7 OC (Quad-Fan · Vapor Chamber)",
        kataban: "ROG-ASTRAL-RTX5090-O32G-GAMING",
        kataban_alt: "90YV0LW0-M0NA00",
        price_doc_jpy: 1199800,
        price_live_jpy: 1234330,
        price_live_note: "¥1,199,800 (TSUKUMO eX. / ARK) · ¥1,234,330 en Kakaku.com",
        best_store: "TSUKUMO eX. / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG-ASTRAL-RTX5090-O32G-GAMING/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG-ASTRAL-RTX5090-O32G-GAMING",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG-ASTRAL-RTX5090-O32G-GAMING",
          amazon: "https://www.amazon.co.jp/s?k=ROG-ASTRAL-RTX5090-O32G-GAMING"
        }
      },
      {
        id: "aio_ryuo4",
        slot: "aio",
        category: "Enfriamiento Líquido (AIO)",
        name: "ASUS ROG Ryuo IV SLC 360 ARGB (Pantalla AMOLED 2K curva)",
        kataban: "ROG RYUO IV SLC 360 ARGB",
        kataban_alt: "90RC0161-M0UAY0",
        price_doc_jpy: 52980,
        price_live_jpy: 52980,
        price_live_note: "¥52,980 en TSUKUMO / Dospara / PC Shop ARK",
        best_store: "TSUKUMO / Dospara",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20RYUO%20IV%20SLC%20360%20ARGB/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG+RYUO+IV+SLC+360",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG+RYUO+IV+SLC+360+ARGB",
          amazon: "https://www.amazon.co.jp/s?k=ROG+RYUO+IV+SLC+360+ARGB"
        }
      },
      {
        id: "ram_gskill_64gb",
        slot: "ram",
        category: "Memoria RAM (64GB EXPO)",
        name: "G.Skill Trident Z5 Neo RGB DDR5-6000 CL30 (2x32GB)",
        kataban: "F5-6000J3040G32GX2-TZ5NR",
        kataban_alt: "DDR5-6000 CL30 32GB×2 EXPO",
        price_doc_jpy: 123800,
        price_live_jpy: 123800,
        price_live_note: "¥123,800 en PC Shop ARK (Distribuidor Oficial G.Skill Akihabara)",
        best_store: "PC Shop ARK",
        store_tags: ["ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/F5-6000J3040G32GX2-TZ5NR/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=F5-6000J3040G32GX2-TZ5NR",
          ark: "https://www.ark-pc.co.jp/search/?key=F5-6000J3040G32GX2-TZ5NR",
          amazon: "https://www.amazon.co.jp/s?k=F5-6000J3040G32GX2-TZ5NR"
        }
      },
      {
        id: "ssd1_sn8100_4tb",
        slot: "ssd1",
        category: "SSD Principal (PCIe 5.0)",
        name: "WD_Black SN8100 4TB NVMe M.2 PCIe Gen 5 (14,900 MB/s)",
        kataban: "WDS400T1X0M",
        kataban_alt: "WD_BLACK SN8100 4TB",
        price_doc_jpy: 139980,
        price_live_jpy: 139980,
        price_live_note: "¥139,980 en PC Shop ARK / Amazon.co.jp",
        best_store: "PC Shop ARK / Amazon.co.jp",
        store_tags: ["ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/WDS400T1X0M/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=WDS400T1X0M",
          ark: "https://www.ark-pc.co.jp/search/?key=WDS400T1X0M",
          amazon: "https://www.amazon.co.jp/s?k=WDS400T1X0M"
        }
      },
      {
        id: "ssd2_990pro_4tb",
        slot: "ssd2",
        category: "SSD Secundario (Juegos)",
        name: "Samsung 990 PRO 4TB PCIe Gen 4",
        kataban: "MZ-V9P4T0B-IT",
        kataban_alt: "990 PRO 4TB 国内正規保証品",
        price_doc_jpy: 128000,
        price_live_jpy: 128000,
        price_live_note: "¥128,000 en TSUKUMO / Yodobashi (¥166,980 en ARK)",
        best_store: "TSUKUMO / Yodobashi",
        store_tags: ["tsukumo", "yodobashi", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/MZ-V9P4T0B-IT/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=MZ-V9P4T0B-IT",
          ark: "https://www.ark-pc.co.jp/search/?key=MZ-V9P4T0B-IT",
          amazon: "https://www.amazon.co.jp/s?k=MZ-V9P4T0B-IT"
        }
      },
      {
        id: "psu_thor3_1200w",
        slot: "psu",
        category: "Fuente de Poder (PSU)",
        name: "ASUS ROG Thor 1200W Platinum III (GaN + OLED)",
        kataban: "ROG-THOR-1200P3-GAMING",
        kataban_alt: "1200W ATX 3.1 Platinum III",
        price_doc_jpy: 80524,
        price_live_jpy: 80524,
        price_live_note: "¥80,524 exacto verificado en Kakaku.com / TSUKUMO / Amazon.co.jp",
        best_store: "TSUKUMO / Amazon.co.jp",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG-THOR-1200P3-GAMING/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG-THOR-1200P3-GAMING",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG-THOR-1200P3-GAMING",
          amazon: "https://www.amazon.co.jp/s?k=ROG-THOR-1200P3-GAMING"
        }
      },
      {
        id: "case_cronox_gr801",
        slot: "case",
        category: "Gabinete (Chassis)",
        name: "ASUS ROG Cronox Full-Tower (Cristal Curvo + LCD 9.2\")",
        kataban: "ROG CRONOX GR801 CURVE TG SCREEN ARGB BLACK",
        kataban_alt: "ROG CRONOX ARGB BLACK",
        price_doc_jpy: 105980,
        price_live_jpy: 105980,
        price_live_note: "¥105,980 exacto verificado en Kakaku.com / TSUKUMO / Pasokon Koubou",
        best_store: "TSUKUMO / Pasokon Koubou",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20CRONOX/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG+CRONOX",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG+CRONOX",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+CRONOX"
        }
      },
      {
        id: "fans_eurux_gr120",
        slot: "fans",
        category: "Ventiladores Extra (x2 packs)",
        name: "ASUS ROG Eurux GR120 ARGB (Conexión magnética en cadena · x2 packs)",
        kataban: "ROG EURUX GR120 ARGB 3PK",
        kataban_alt: "ROG EURUX GR120 ARGB 3PK × 2",
        price_doc_jpy: 27600,
        price_live_jpy: 27600,
        price_live_note: "¥27,600 (x2 packs en TSUKUMO)",
        best_store: "TSUKUMO",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20EURUX%20GR120/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ROG+EURUX+GR120",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG+EURUX+GR120",
          amazon: "https://www.amazon.co.jp/s?k=ROG+EURUX+GR120+ARGB"
        }
      }
    ],
    display_system: [
      {
        id: "monitors_pg32ucdm3",
        slot: "monitors",
        category: "2x Monitores 31.5\" 4K 240Hz",
        name: "2x ASUS ROG Swift OLED PG32UCDM3 (Gen 3 Tandem QD-OLED · DP 2.1a UHBR20 80Gbps + BlackShield)",
        kataban: "PG32UCDM3",
        kataban_alt: "PG32UCDM3 × 2台 (¥214,920 c/u)",
        price_doc_jpy: 429840,
        price_live_jpy: 339600,
        gold_points_10pct: 42984,
        price_live_note: "¥429,840 (¥214,920 c/u) · ¡En Yodobashi.com hoy ¥169,800 c/u (¥339,600 el par) + 10% en puntos Gold Point!",
        best_store: "Yodobashi / Bic Camera (dan 10% en puntos)",
        store_tags: ["yodobashi", "kakaku", "tsukumo"],
        links: {
          kakaku: "https://kakaku.com/search_results/PG32UCDM3/",
          yodobashi: "https://www.yodobashi.com/?word=PG32UCDM3",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PG32UCDM",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Swift+OLED+PG32UCDM"
        }
      },
      {
        id: "arms_aas01",
        slot: "arms",
        category: "2x Brazos de Monitor ROG",
        name: "2x ASUS ROG Ergo Monitor Arm (Soporte mecánico con Aura Sync)",
        kataban: "ROG ERGO MONITOR ARM AAS01",
        kataban_alt: "AAS01 × 2台 (¥28,500 c/u)",
        price_doc_jpy: 57000,
        price_live_jpy: 57000,
        gold_points_10pct: 5700,
        price_live_note: "¥57,000 (¥28,500 c/u) + ¥5,700 en puntos Gold Point en Yodobashi",
        best_store: "Amazon.co.jp / Yodobashi",
        store_tags: ["yodobashi", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20ERGO%20MONITOR%20ARM%20AAS01/",
          yodobashi: "https://www.yodobashi.com/?word=ROG+ERGO+MONITOR+ARM+AAS01",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=AAS01",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Ergo+Monitor+Arm+AAS01"
        }
      }
    ],
    peripherals: [
      {
        id: "kb_azoth_extreme_us",
        slot: "keyboard",
        category: "Teclado (US Layout / 英語配列)",
        name: "ASUS ROG Azoth Extreme (Aluminio CNC + Fibra de Carbono + OLED táctil · US Layout)",
        kataban: "M702 AZOTH EXTREME/NXSW/US/PBT",
        kataban_alt: "M702 AZOTH EXTREME/NXSM/US/PBT",
        price_doc_jpy: 89800,
        price_live_jpy: 106033,
        price_live_note: "¥89,800 (Base) · ¥106,033 en Kakaku / ¥116,960 en Yodobashi (+10% pts). ¡Exigir US Layout!",
        best_store: "PC Shop ARK / TSUKUMO / Yodobashi",
        store_tags: ["ark", "tsukumo", "yodobashi", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/M702%20AZOTH%20EXTREME/",
          yodobashi: "https://www.yodobashi.com/?word=M702+AZOTH+EXTREME",
          ark: "https://www.ark-pc.co.jp/search/?key=AZOTH+EXTREME",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Azoth+Extreme+US"
        }
      },
      {
        id: "mouse_harpe_extreme",
        slot: "mouse",
        category: "Mouse (Fibra de Carbono)",
        name: "ASUS ROG Harpe Ace Extreme (47g, Fibra de Carbono, 8000Hz Wireless)",
        kataban: "P718 ROG HARPE ACE EXTREME",
        kataban_alt: "ROG/HARPE/ACE/EX",
        price_doc_jpy: 45800,
        price_live_jpy: 45800,
        free_with_yodobashi_points: true,
        price_live_note: "¥45,800 exacto en ARK/Kakaku (¥46,100 Yodobashi) — ¡GRATIS (¥0) con los ~¥48,680 puntos de los 2 monitores!",
        best_store: "Yodobashi (Gratis con Puntos) / ARK",
        store_tags: ["yodobashi", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/P718%20ROG%20HARPE%20ACE%20EXTREME/",
          yodobashi: "https://www.yodobashi.com/?word=P718+ROG+HARPE+ACE+EXTREME",
          ark: "https://www.ark-pc.co.jp/search/?key=P718+ROG+HARPE+ACE+EXTREME",
          amazon: "https://www.amazon.co.jp/s?k=P718+ROG+HARPE+ACE+EXTREME"
        }
      },
      {
        id: "pad_moonstone_glass",
        slot: "pad_glass",
        category: "Mousepad de Cristal",
        name: "ASUS ROG Moonstone Ace L (Cristal templado 9H negro · 500×400mm)",
        kataban: "NH04 ROG MOONSTONE ACE L/BLK",
        kataban_alt: "ROG-MOONSTONE/ACE/L",
        price_doc_jpy: 13800,
        price_live_jpy: 17600,
        price_live_note: "¥13,800 (Base) · ¥17,600 en Yodobashi.com (+1,760 pts)",
        best_store: "TSUKUMO / Yodobashi / ARK",
        store_tags: ["yodobashi", "tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/NH04%20ROG%20MOONSTONE%20ACE%20L/",
          yodobashi: "https://www.yodobashi.com/?word=NH04+ROG+MOONSTONE+ACE+L",
          ark: "https://www.ark-pc.co.jp/search/?key=MOONSTONE+ACE+L",
          amazon: "https://www.amazon.co.jp/s?k=ROG+Moonstone+Ace+L"
        }
      },
      {
        id: "pad_hone_xxl",
        slot: "pad_xxl",
        category: "Mousepad de Escritorio XXL",
        name: "ASUS ROG Hone Ace XXL (Para debajo del teclado y el cristal · 900×400mm)",
        kataban: "90MP0390-BPUA00",
        kataban_alt: "ROG HONE ACE XXL",
        price_doc_jpy: 6480,
        price_live_jpy: 6480,
        price_live_note: "¥6,480 exacto verificado en Amazon.co.jp / TSUKUMO",
        best_store: "Amazon.co.jp / TSUKUMO",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/90MP0390-BPUA00/",
          yodobashi: "https://www.yodobashi.com/?word=ROG+Hone+Ace+XXL",
          ark: "https://www.ark-pc.co.jp/search/?key=90MP0390-BPUA00",
          amazon: "https://www.amazon.co.jp/s?k=90MP0390-BPUA00"
        }
      },
      {
        id: "headset_delta2",
        slot: "headset",
        category: "Audífonos Wireless",
        name: "ASUS ROG Delta II (DualFlow Audio 2.4GHz + Bluetooth simultáneo)",
        kataban: "ROGDELTA2",
        kataban_alt: "ROG DELTA II",
        price_doc_jpy: 32895,
        price_live_jpy: 32895,
        price_live_note: "¥32,895 exacto verificado en Amazon.co.jp / Kakaku.com",
        best_store: "Amazon.co.jp / TSUKUMO / Yodobashi",
        store_tags: ["tsukumo", "yodobashi", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20Delta%20II/",
          yodobashi: "https://www.yodobashi.com/?word=ROG+Delta+II",
          ark: "https://www.ark-pc.co.jp/search/?key=ROGDELTA2",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Delta+II"
        }
      },
      {
        id: "mic_carnyx_blk",
        slot: "mic",
        category: "Micrófono de Estudio",
        name: "ASUS ROG Carnyx (Condensador 25mm, 192kHz/24-bit, Negro)",
        kataban: "ROG CARNYX/BLK",
        kataban_alt: "C501 ROG CARNYX",
        price_doc_jpy: 26800,
        price_live_jpy: 24980,
        price_live_note: "¥26,800 (Base) · ¡Hoy ¥24,980 en Yodobashi.com (+2,498 pts)!",
        best_store: "Yodobashi / TSUKUMO",
        store_tags: ["yodobashi", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG%20CARNYX/",
          yodobashi: "https://www.yodobashi.com/?word=ROG+CARNYX",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG+CARNYX",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Carnyx"
        }
      }
    ],
    counter_script: {
      ja: "すみません、俺はこのリストのパーツでハイエンドPCを一式組みたいです。在庫の確認と、CPUとマザーボードのセット割引が使えるか教えてください。あと、キーボードは日本語配列ではなく、必ず英語配列（US配列）でお願いします。",
      romaji: "Sumimasen, ore wa kono risuto no pātsu de haiendo PC o isshiki kumitai desu. Zaiko no kakunin to, CPU to mazābōdo no setto waribiki ga tsukaeru ka oshiete kudasai. Ato, kībōdo wa nihongo hairetsu dewa naku, kanarazu eigo hairetsu (US hairetsu) de onegaishimasu.",
      es: "«Disculpe, quiero armar una PC de gama alta completa con las piezas de esta lista. Por favor, confirme la disponibilidad de stock y dígame si se puede aplicar el descuento por paquete de CPU y tarjeta madre. Además, el teclado no lo quiero con distribución japonesa, sino estrictamente con distribución en inglés (US layout), por favor.»",
      assembly_addon_ja: "また、店舗の「組立代行サービス（配線整理・動作チェック込み）」をお願いした場合の工賃と納期も教えてください。",
      assembly_addon_romaji: "Mata, tenpo no 'kumitate daikō sābisu (haisen seiri・dōsa chekku komi)' o onegai shita baai no kōchin to nōki mo oshiete kudasai.",
      assembly_addon_es: "«Además, por favor dígame el costo de mano de obra y el tiempo de entrega si solicito el servicio de ensamblaje profesional de la tienda (incluyendo gestión limpia de cables y prueba de funcionamiento).»"
    }
  };

  const state = {
    data: FALLBACK_DATA,
    cpuChoice: "9950x3d", // "9950x3d" | "9850x3d"
    kbSwitch: "NXSW",     // "NXSW" (Snow) | "NXSM" (Storm)
    yodobashiHack: false,
    assemblyService: false, // false = DIY (¥0), true = 組立代行サービス (+¥22,000)
    storeFilter: "all",
    searchQuery: "",
    jpyRate: 147.0
  };

  function detectLiveJpyRate() {
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
    fetch("https://open.er-api.com/v6/latest/USD")
      .then(r => r.json())
      .then(d => {
        if (d && d.rates && d.rates.JPY) {
          state.jpyRate = d.rates.JPY;
          renderApp();
        }
      })
      .catch(() => {});
  }

  function fmtYen(n) {
    return "¥" + Math.round(n).toLocaleString("en-US");
  }

  function fmtUsd(jpy) {
    return "$" + Math.round(jpy / (state.jpyRate || 147)).toLocaleString("en-US") + " USD";
  }

  function copyText(text, btnEl) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).catch(() => {});
    } else {
      const ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
    }
    if (btnEl) {
      const orig = btnEl.innerHTML;
      btnEl.innerHTML = "✅ Copiado";
      btnEl.style.borderColor = "#22c55e";
      btnEl.style.color = "#4ade80";
      setTimeout(() => {
        btnEl.innerHTML = orig;
        btnEl.style.borderColor = "";
        btnEl.style.color = "";
      }, 1500);
    }
  }

  function speakJapanese(text) {
    if (!("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "ja-JP";
    u.rate = 0.94;
    window.speechSynthesis.speak(u);
  }

  function computeTotals() {
    const d = state.data;
    const towerItems = d.tower_components.filter(it => {
      if (it.option_group === "cpu_choice") {
        return it.option_key === state.cpuChoice;
      }
      return true;
    });

    const towerSubtotal = towerItems.reduce((acc, it) => acc + it.price_doc_jpy, 0);
    const displaySubtotal = d.display_system.reduce((acc, it) => acc + it.price_doc_jpy, 0);
    const periphSubtotal = d.peripherals.reduce((acc, it) => acc + it.price_doc_jpy, 0);

    let grossTotal = towerSubtotal + displaySubtotal + periphSubtotal;
    const assemblyCost = state.assemblyService ? 22000 : 0;
    const hackMouseSavings = state.yodobashiHack ? 45800 : 0;
    const hackSetSavings = state.yodobashiHack ? 16500 : 0;
    const totalHackSavings = hackMouseSavings + hackSetSavings;
    const netTotal = grossTotal + assemblyCost - totalHackSavings;

    return {
      towerSubtotal,
      displaySubtotal,
      periphSubtotal,
      grossTotal,
      assemblyCost,
      totalHackSavings,
      netTotal
    };
  }

  function buildKatabanCounterList() {
    const cpuLine = state.cpuChoice === "9950x3d"
      ? "・CPU: AMD Ryzen 9 9950X3D BOX (100-100000719WOF)"
      : "・CPU: AMD Ryzen 7 9850X3D BOX";
    const kbCode = state.kbSwitch === "NXSW"
      ? "ASUS M702 AZOTH EXTREME/NXSW/US/PBT (ROG NX Snow Switch)"
      : "ASUS M702 AZOTH EXTREME/NXSM/US/PBT (ROG NX Storm Switch)";
    const assemblyLine = state.assemblyService
      ? "\n【オプション】\n・組立代行サービス（配線整理・BIOS更新・動作チェック一式）"
      : "";

    return [
      "【PC本体パーツ】",
      cpuLine,
      "・M/B: ASUS ROG CROSSHAIR X870E DARK HERO",
      "・GPU: ASUS ROG-ASTRAL-RTX5090-O32G-GAMING",
      "・AIO: ASUS ROG RYUO IV SLC 360 ARGB",
      "・RAM: G.Skill F5-6000J3040G32GX2-TZ5NR (DDR5-6000 32GB×2 EXPO)",
      "・SSD 1: WD_Black SN8100 4TB (WDS400T1X0M)",
      "・SSD 2: Samsung 990 PRO 4TB (MZ-V9P4T0B-IT)",
      "・PSU: ASUS ROG-THOR-1200P3-GAMING (1200W)",
      "・CASE: ASUS ROG CRONOX GR801 CURVE TG SCREEN ARGB BLACK",
      "・FAN: ASUS ROG EURUX GR120 ARGB 3PK × 2パック",
      "",
      "【モニター・周辺機器】",
      "・Monitor: ASUS ROG Swift OLED PG32UCDM3 × 2台",
      "・Monitor Arm: ASUS ROG Ergo Monitor Arm AAS01 × 2台",
      "・Keyboard (※英語配列/US Layout): " + kbCode,
      "・Mouse: ASUS P718 ROG HARPE ACE EXTREME",
      "・Mousepad (Glass): ASUS NH04 ROG MOONSTONE ACE L/BLK",
      "・Mousepad (Desk XXL): ASUS ROG Hone Ace XXL (90MP0390-BPUA00)",
      "・Headset: ASUS ROGDELTA2",
      "・Mic: ASUS ROG CARNYX/BLK" + assemblyLine
    ].join("\n");
  }

  function matchesFilter(item) {
    if (state.storeFilter !== "all") {
      const tags = item.store_tags || [];
      const bs = (item.best_store || "").toLowerCase();
      if (!tags.includes(state.storeFilter) && !bs.includes(state.storeFilter)) {
        return false;
      }
    }
    if (state.searchQuery.trim() !== "") {
      const q = state.searchQuery.trim().toLowerCase();
      const hay = [
        item.category,
        item.name,
        item.kataban,
        item.kataban_alt,
        item.best_store
      ].join(" ").toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  }

  function renderStoreLinks(links) {
    if (!links) return "";
    const btns = [];
    if (links.kakaku) {
      btns.push(`<a href="${links.kakaku}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-kakaku" title="Buscar el precio más bajo en Kakaku.com">🔍 Kakaku</a>`);
    }
    if (links.tsukumo) {
      btns.push(`<a href="${links.tsukumo}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-tsukumo" title="Buscar en TSUKUMO Akihabara">🏬 TSUKUMO</a>`);
    }
    if (links.ark) {
      btns.push(`<a href="${links.ark}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-ark" title="Buscar en PC Shop ARK Akihabara">🛡️ ARK</a>`);
    }
    if (links.yodobashi) {
      btns.push(`<a href="${links.yodobashi}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-yodobashi" title="Buscar en Yodobashi Camera (10% Gold Points)">⚡ Yodobashi</a>`);
    }
    if (links.amazon) {
      btns.push(`<a href="${links.amazon}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-amazon" title="Buscar en Amazon.co.jp">📦 Amazon JP</a>`);
    }
    return `<div class="rog-store-links">${btns.join("")}</div>`;
  }

  function renderItemRow(item, opts = {}) {
    const isAltCpu = item.option_group === "cpu_choice" && item.option_key !== state.cpuChoice;
    let displayKataban = item.kataban;
    if (item.id === "kb_azoth_extreme_us") {
      displayKataban = state.kbSwitch === "NXSW"
        ? "M702 AZOTH EXTREME/NXSW/US/PBT"
        : "M702 AZOTH EXTREME/NXSM/US/PBT";
    }
    const isFreeMouse = item.id === "mouse_harpe_extreme" && state.yodobashiHack;
    const effectivePrice = isFreeMouse ? 0 : item.price_doc_jpy;

    return `
      <tr class="rog-item-row ${isAltCpu ? "rog-row-inactive-cpu" : ""}" data-item-id="${item.id}">
        <td>
          <div style="font-weight:700; color:#f8fafc;">${item.category}</div>
          ${item.option_group === "cpu_choice" ? `
            <span class="rog-cpu-badge ${isAltCpu ? "inactive" : "active"}">
              ${isAltCpu ? "Opción Alternativa (No sumada al subtotal activo)" : "✅ Seleccionado en tu Build"}
            </span>
          ` : ""}
        </td>
        <td>
          <div style="font-weight:700; color:#e2e8f0;">${item.name}</div>
          <div style="font-size:0.75rem; color:#94a3b8; margin-top:3px;">📊 ${item.price_live_note || ""}</div>
        </td>
        <td>
          <div class="rog-kataban-box">
            <code class="rog-kataban-code">${displayKataban}</code>
            <button type="button" class="rog-copy-btn" data-copy="${displayKataban}">📋 Copiar 型番</button>
          </div>
          ${item.kataban_alt ? `<div style="font-size:0.71rem; color:#64748b; margin-top:3px;">Cód. Alt: <code>${item.kataban_alt}</code></div>` : ""}
        </td>
        <td style="white-space:nowrap;">
          ${isFreeMouse ? `
            <div style="text-decoration:line-through; color:#64748b; font-size:0.8rem;">${fmtYen(item.price_doc_jpy)}</div>
            <div style="font-weight:900; color:#4ade80; font-size:1rem;">¥0 GRATIS 🎁</div>
            <div style="font-size:0.7rem; color:#4ade80;">Canjeado con Gold Points</div>
          ` : `
            <div style="font-weight:800; color:${isAltCpu ? "#94a3b8" : "#f59e0b"}; font-size:0.98rem;">${fmtYen(effectivePrice)}</div>
            <div style="font-size:0.73rem; color:#38bdf8;">${fmtUsd(effectivePrice)}</div>
          `}
        </td>
        <td>
          <div style="font-weight:600; color:#cbd5e1; font-size:0.8rem; margin-bottom:5px;">🏪 ${item.best_store}</div>
          ${renderStoreLinks(item.links)}
        </td>
      </tr>
    `;
  }

  function injectStyles() {
    if (document.getElementById("rog-sin-limites-styles")) return;
    const st = document.createElement("style");
    st.id = "rog-sin-limites-styles";
    st.textContent = `
      .rog-api-shell {
        background: linear-gradient(165deg, rgba(15, 19, 29, 0.98) 0%, rgba(10, 12, 18, 0.99) 100%);
        border: 1px solid rgba(239, 68, 68, 0.4);
        border-radius: 14px;
        padding: 18px;
        margin-top: 8px;
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.55);
      }
      .rog-kpi-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(205px, 1fr));
        gap: 10px;
        margin-bottom: 14px;
      }
      .rog-kpi-card {
        background: rgba(18, 24, 36, 0.92);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 10px;
        padding: 12px 14px;
      }
      .rog-kpi-card.highlight {
        border-color: rgba(239, 68, 68, 0.65);
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.14), rgba(212, 168, 83, 0.1));
      }
      .rog-kpi-lbl {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #94a3b8;
        font-weight: 700;
      }
      .rog-kpi-val {
        font-family: 'Orbitron', monospace;
        font-size: 1.22rem;
        font-weight: 900;
        color: #f8fafc;
        margin-top: 4px;
      }
      .rog-kpi-sub {
        font-size: 0.75rem;
        color: #38bdf8;
        margin-top: 3px;
      }
      .rog-controls-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        align-items: center;
        justify-content: space-between;
        background: rgba(12, 16, 24, 0.9);
        border: 1px solid rgba(212, 168, 83, 0.28);
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 14px;
      }
      .rog-btn-group {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        align-items: center;
      }
      .rog-toggle-btn {
        background: rgba(30, 41, 59, 0.75);
        color: #cbd5e1;
        border: 1px solid rgba(148, 163, 184, 0.28);
        border-radius: 8px;
        padding: 7px 11px;
        font-size: 0.76rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.18s ease;
      }
      .rog-toggle-btn:hover {
        border-color: #ef4444;
        color: #fff;
      }
      .rog-toggle-btn.active {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.28), rgba(212, 168, 83, 0.22));
        border-color: #ef4444;
        color: #fff;
        box-shadow: 0 0 12px rgba(239, 68, 68, 0.3);
      }
      .rog-toggle-btn.hack-active {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.26), rgba(16, 185, 129, 0.18));
        border-color: #22c55e;
        color: #4ade80;
      }
      .rog-search-input {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(148, 163, 184, 0.32);
        border-radius: 8px;
        color: #f8fafc;
        padding: 7px 11px;
        font-size: 0.78rem;
        min-width: 210px;
      }
      .rog-section-hdr {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
        margin: 16px 0 8px 0;
        padding: 8px 12px;
        background: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #ef4444;
        border-radius: 6px;
      }
      .rog-section-hdr h4 {
        margin: 0;
        font-size: 0.92rem;
        color: #f8fafc;
      }
      .rog-kataban-box {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-wrap: wrap;
      }
      .rog-kataban-code {
        background: rgba(239, 68, 68, 0.13);
        border: 1px solid rgba(239, 68, 68, 0.38);
        color: #fca5a5;
        padding: 3px 7px;
        border-radius: 5px;
        font-family: monospace;
        font-size: 0.78rem;
        font-weight: 700;
        user-select: all;
      }
      .rog-copy-btn {
        background: rgba(30, 41, 59, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.35);
        color: #e2e8f0;
        border-radius: 5px;
        padding: 3px 8px;
        font-size: 0.71rem;
        font-weight: 700;
        cursor: pointer;
      }
      .rog-copy-btn:hover {
        border-color: #d4a853;
        color: #fde047;
      }
      .rog-store-links {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
      }
      .rog-store-pill {
        display: inline-flex;
        align-items: center;
        padding: 3px 7px;
        border-radius: 5px;
        font-size: 0.7rem;
        font-weight: 700;
        text-decoration: none !important;
        border: 1px solid rgba(255,255,255,0.14);
        transition: transform 0.12s ease;
      }
      .rog-store-pill:hover {
        transform: translateY(-1px);
      }
      .rog-pill-kakaku { background: rgba(234, 179, 8, 0.16); color: #fde047 !important; border-color: rgba(234, 179, 8, 0.4); }
      .rog-pill-tsukumo { background: rgba(56, 189, 248, 0.16); color: #7dd3fc !important; border-color: rgba(56, 189, 248, 0.4); }
      .rog-pill-ark { background: rgba(239, 68, 68, 0.16); color: #fca5a5 !important; border-color: rgba(239, 68, 68, 0.4); }
      .rog-pill-yodobashi { background: rgba(34, 197, 94, 0.16); color: #86efac !important; border-color: rgba(34, 197, 94, 0.4); }
      .rog-pill-amazon { background: rgba(249, 115, 22, 0.16); color: #fdba74 !important; border-color: rgba(249, 115, 22, 0.4); }
      .rog-row-inactive-cpu {
        opacity: 0.52;
        background: rgba(15, 23, 42, 0.35);
      }
      .rog-cpu-badge {
        display: inline-block;
        margin-top: 4px;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.68rem;
        font-weight: 700;
      }
      .rog-cpu-badge.active {
        background: rgba(34, 197, 94, 0.18);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.4);
      }
      .rog-cpu-badge.inactive {
        background: rgba(148, 163, 184, 0.14);
        color: #94a3b8;
      }
      .rog-counter-card {
        margin-top: 16px;
        background: linear-gradient(145deg, rgba(20, 26, 38, 0.96), rgba(12, 16, 24, 0.98));
        border: 1px solid rgba(212, 168, 83, 0.45);
        border-radius: 12px;
        padding: 15px;
      }
      .rog-pre-list {
        background: #070a0f;
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 8px;
        padding: 12px;
        color: #e2e8f0;
        font-family: monospace;
        font-size: 0.78rem;
        line-height: 1.55;
        overflow-x: auto;
        white-space: pre;
        margin-top: 8px;
      }
    `;
    document.head.appendChild(st);
  }

  function renderApp() {
    const mount = document.getElementById("rog-sin-limites-api-mount");
    if (!mount) return;
    injectStyles();

    const totals = computeTotals();
    const headerSub = document.getElementById("rog-tech-room-subtotal");
    if (headerSub) {
      headerSub.textContent = fmtYen(totals.netTotal);
    }

    const d = state.data;
    const towerRows = d.tower_components.filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const displayRows = d.display_system.filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const periphRows = d.peripherals.filter(matchesFilter).map(it => renderItemRow(it)).join("");

    const fullJaScript = state.assemblyService
      ? `${d.counter_script.ja} ${d.counter_script.assembly_addon_ja}`
      : d.counter_script.ja;
    const fullRomajiScript = state.assemblyService
      ? `${d.counter_script.romaji} ${d.counter_script.assembly_addon_romaji}`
      : d.counter_script.romaji;
    const fullEsScript = state.assemblyService
      ? `${d.counter_script.es} ${d.counter_script.assembly_addon_es}`
      : d.counter_script.es;

    const katabanListText = buildKatabanCounterList();

    mount.innerHTML = `
      <div class="rog-api-shell">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
          <div>
            <span style="display:inline-block; background:rgba(239,68,68,0.2); border:1px solid #ef4444; color:#fca5a5; font-size:0.7rem; font-weight:800; padding:3px 9px; border-radius:999px; letter-spacing:0.06em;">
              🔴 API EN VIVO · AKIHABARA KATABAN (型番) PRICE TRACKER v3.0
            </span>
            <h3 style="margin:6px 0 2px 0; color:#f8fafc; font-size:1.1rem;">
              🔥 Configuración «Sin Límites» (Nivel 3: Extreme Tope Absoluto · Full ASUS ROG + RTX 5090 + Dual OLED 240Hz)
            </h3>
            <p style="margin:0; font-size:0.8rem; color:#94a3b8;">
              Códigos exactos del mercado japonés (<strong>型番 / Kataban</strong>) verificados en <strong>Kakaku.com</strong>, <strong>TSUKUMO eX.</strong>, <strong>PC Shop ARK</strong> y <strong>Yodobashi Camera Multimedia Akiba</strong> (a 4 min en tu Honda CB250R desde Asakusabashi).
            </p>
          </div>
          <div style="text-align:right; font-size:0.75rem; color:#94a3b8;">
            <div>Tipo de Cambio Activo: <strong style="color:#4ade80;">1 USD = ¥${state.jpyRate.toFixed(2)} JPY</strong></div>
            <div>19 Códigos Oficiales (型番) · Impuestos Incluidos (税込)</div>
          </div>
        </div>

        <!-- 4 KPI CARDS (RESUMEN DE PRESUPUESTO SIN LÍMITES) -->
        <div class="rog-kpi-grid">
          <div class="rog-kpi-card">
            <div class="rog-kpi-lbl">1. Subtotal Torre Completa</div>
            <div class="rog-kpi-val">${fmtYen(totals.towerSubtotal)}</div>
            <div class="rog-kpi-sub">${fmtUsd(totals.towerSubtotal)} · ${state.cpuChoice === "9950x3d" ? "Ryzen 9 9950X3D + RTX 5090 + 8TB" : "Ryzen 7 9850X3D + RTX 5090 + 8TB"}</div>
          </div>
          <div class="rog-kpi-card">
            <div class="rog-kpi-lbl">2. 2x OLED 4K 240Hz + 2x Brazos ROG</div>
            <div class="rog-kpi-val">${fmtYen(totals.displaySubtotal)}</div>
            <div class="rog-kpi-sub">${fmtUsd(totals.displaySubtotal)} · Genera <strong>+¥48,684 pts</strong> (10%) en Yodobashi</div>
          </div>
          <div class="rog-kpi-card">
            <div class="rog-kpi-lbl">3. Periféricos ROG Extreme (US Layout)</div>
            <div class="rog-kpi-val">${fmtYen(totals.periphSubtotal)}</div>
            <div class="rog-kpi-sub">${fmtUsd(totals.periphSubtotal)} · Azoth Extreme (${state.kbSwitch}) + Harpe Carbon</div>
          </div>
          <div class="rog-kpi-card highlight">
            <div class="rog-kpi-lbl">4. TOTAL GENERAL «SIN LÍMITES» (税込)</div>
            <div class="rog-kpi-val" style="color:#fde047;">${fmtYen(totals.netTotal)}</div>
            <div class="rog-kpi-sub" style="color:#4ade80; font-weight:700;">
              ${fmtUsd(totals.netTotal)} ${state.yodobashiHack ? `(Ahorro Hack: -${fmtYen(totals.totalHackSavings)})` : "(Todo incluido con impuestos)"}
            </div>
          </div>
        </div>

        <!-- BARRA INTERACTIVA DE CONFIGURACIÓN Y FILTROS -->
        <div class="rog-controls-bar">
          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#94a3b8; font-weight:700;">CPU:</span>
            <button type="button" class="rog-toggle-btn ${state.cpuChoice === "9950x3d" ? "active" : ""}" id="rog-btn-9950">
              🔥 Opción 1: Ryzen 9 9950X3D (16C · ¥109,980)
            </button>
            <button type="button" class="rog-toggle-btn ${state.cpuChoice === "9850x3d" ? "active" : ""}" id="rog-btn-9850">
              ⚡ Opción 2: Ryzen 7 9850X3D (8C · ¥69,940)
            </button>
          </div>

          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#94a3b8; font-weight:700;">Switch US:</span>
            <button type="button" class="rog-toggle-btn ${state.kbSwitch === "NXSW" ? "active" : ""}" id="rog-btn-nxsw">
              ❄️ NX Snow (/NXSW/US)
            </button>
            <button type="button" class="rog-toggle-btn ${state.kbSwitch === "NXSM" ? "active" : ""}" id="rog-btn-nxsm">
              🌩️ NX Storm (/NXSM/US)
            </button>
          </div>

          <div class="rog-btn-group">
            <button type="button" class="rog-toggle-btn ${state.yodobashiHack ? "hack-active" : ""}" id="rog-btn-hack">
              💡 ${state.yodobashiHack ? "Hack Yodobashi Activo (-¥62,300)" : "Aplicar Truco Yodobashi Gold Points (~¥65,000 Ahorro)"}
            </button>
            <button type="button" class="rog-toggle-btn ${state.assemblyService ? "active" : ""}" id="rog-btn-assembly">
              🛠️ ${state.assemblyService ? "Con 組立代行サービス (+¥22,000)" : "Armado en Casa (¥0) / Ver 組立代行"}
            </button>
          </div>
        </div>

        <!-- FILTRO POR TIENDA Y BUSCADOR DE KATABAN -->
        <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#94a3b8; font-weight:700;">Filtrar Tienda:</span>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "all" ? "active" : ""}" data-store-filter="all">Todas (19)</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "tsukumo" ? "active" : ""}" data-store-filter="tsukumo">🏬 TSUKUMO eX.</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "ark" ? "active" : ""}" data-store-filter="ark">🛡️ PC Shop ARK</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "yodobashi" ? "active" : ""}" data-store-filter="yodobashi">⚡ Yodobashi (10% Pts)</button>
          </div>
          <input type="search" class="rog-search-input" id="rog-kataban-search" placeholder="🔎 Filtrar por pieza o código 型番 (ej. 5090, WDS400)..." value="${state.searchQuery}">
        </div>

        <!-- TRUCO YODOBASHI GOLD POINTS BANNER -->
        <div style="background:rgba(34,197,94,0.09); border:1px solid rgba(34,197,94,0.38); border-radius:10px; padding:11px 14px; margin-bottom:14px; font-size:0.82rem; color:#e2e8f0;">
          <strong style="color:#4ade80;">💎 Truco para ahorrarte ~¥65,000 JPY el mismo día en Akihabara:</strong>
          Compra primero los dos monitores <code>PG32UCDM3</code> y los dos brazos <code>AAS01</code> en <strong>Yodobashi Camera (Multimedia Akiba)</strong> o <strong>Bic Camera</strong>. Como ambos dan el <strong>10% en puntos Gold Point</strong>, recibirás al instante <strong>~¥48,680 en puntos</strong>. Con esos puntos en la tarjeta, sube al piso de periféricos de la misma tienda y llévate el <strong>ROG Harpe Ace Extreme (<code>P718 ROG HARPE ACE EXTREME</code> · ¥45,800)</strong> <strong>completamente gratis (¥0)</strong>. Luego camina 5 minutos hasta <strong>TSUKUMO eX.</strong> o <strong>PC Shop ARK</strong> para comprar las piezas de la torre con el descuento de paquete CPU + Motherboard (<code>セット割引</code>).
        </div>

        <!-- TABLA 1: LA TORRE SIN LÍMITES -->
        <div class="rog-section-hdr">
          <h4>1. La Torre «Sin Límites» (Códigos Exactos en Japón / 型番)</h4>
          <span style="font-weight:800; color:#fde047;">Subtotal Torre: ${fmtYen(totals.towerSubtotal)} (${fmtUsd(totals.towerSubtotal)})</span>
        </div>
        <div class="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Componente</th>
                <th>Nombre Comercial &amp; Verificación en Tienda</th>
                <th>Código Exacto en Japón (型番) para Copiar/Pegar</th>
                <th>Precio Aprox. (税込)</th>
                <th>Mejor Tienda en Japón &amp; Links Reales</th>
              </tr>
            </thead>
            <tbody>
              ${towerRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
            </tbody>
          </table>
        </div>

        <!-- TABLA 2: SISTEMA DE DOBLE PANTALLA OLED 4K 240HZ -->
        <div class="rog-section-hdr">
          <h4>2. Sistema de Doble Pantalla OLED 4K 240Hz (Gen 3 Tandem OLED · DP 2.1a UHBR20 80Gbps + BlackShield)</h4>
          <span style="font-weight:800; color:#fde047;">Subtotal Pantallas + Brazos: ${fmtYen(totals.displaySubtotal)} (${fmtUsd(totals.displaySubtotal)})</span>
        </div>
        <div class="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Equipo</th>
                <th>Modelo Exacto &amp; Puntos Gold Point</th>
                <th>Código Exacto en Japón (型番)</th>
                <th>Precio por el Par (税込)</th>
                <th>Mejor Tienda &amp; Links Reales</th>
              </tr>
            </thead>
            <tbody>
              ${displayRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
            </tbody>
          </table>
        </div>

        <!-- TABLA 3: PERIFÉRICOS TOPE DE GAMA (US LAYOUT) -->
        <div class="rog-section-hdr">
          <h4>3. Periféricos Tope de Gama (con Teclado en Inglés / 英語配列 US Layout)</h4>
          <span style="font-weight:800; color:#fde047;">Subtotal Periféricos: ${fmtYen(totals.periphSubtotal)} (${fmtUsd(totals.periphSubtotal)})</span>
        </div>
        <div class="table-responsive">
          <table>
            <thead>
              <tr>
                <th>Periférico</th>
                <th>Modelo Insignia</th>
                <th>Código Exacto en Japón (型番)</th>
                <th>Precio Aprox. (税込)</th>
                <th>Mejor Tienda &amp; Links Reales</th>
              </tr>
            </thead>
            <tbody>
              ${periphRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
            </tbody>
          </table>
        </div>

        <!-- SECCIÓN 5: NOTA LISTA PARA MOSTRAR EN EL MOSTRADOR (TSUKUMO eX. / PC SHOP ARK) -->
        <div class="rog-counter-card">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
            <div>
              <h4 style="margin:0; color:#fde047; font-size:0.98rem;">
                🗣️ 5. Nota Lista para Mostrar en el Mostrador (TSUKUMO eX. Pisos 4F/5F/6F &amp; PC Shop ARK)
              </h4>
              <div style="font-size:0.76rem; color:#94a3b8;">
                Muestra esta tarjeta en tu celular en Akihabara para que el encargado reúna todas las cajas, aplique el descuento CPU+M/B y verifique el teclado en inglés (US Layout).
              </div>
            </div>
            <div style="display:flex; gap:6px; flex-wrap:wrap;">
              <button type="button" class="rog-toggle-btn active" id="rog-speak-ja-btn">🔊 Escuchar en Japonés</button>
              <button type="button" class="rog-toggle-btn" id="rog-copy-ja-btn">📋 Copiar Mensaje Japonés</button>
              <button type="button" class="rog-toggle-btn" id="rog-copy-list-btn">📋 Copiar Lista Completa de 型番</button>
            </div>
          </div>

          <div style="background:rgba(15,23,42,0.85); border-left:3px solid #d4a853; padding:10px 12px; border-radius:6px; margin-bottom:8px;">
            <div style="font-size:0.72rem; color:#d4a853; font-weight:700; margin-bottom:3px;">🇯🇵 TEXTO EN JAPONÉS (PARA MOSTRAR AL ENCARGADO):</div>
            <div style="font-size:0.95rem; font-weight:700; color:#fff; line-height:1.5;">${fullJaScript}</div>
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:8px; margin-bottom:10px;">
            <div style="background:rgba(15,23,42,0.6); padding:9px 11px; border-radius:6px; font-size:0.78rem; color:#cbd5e1;">
              <strong style="color:#38bdf8;">🔤 Pronunciación (Romaji):</strong><br>
              <em>${fullRomajiScript}</em>
            </div>
            <div style="background:rgba(15,23,42,0.6); padding:9px 11px; border-radius:6px; font-size:0.78rem; color:#cbd5e1;">
              <strong style="color:#4ade80;">🇪🇸 Traducción al Español:</strong><br>
              <em>${fullEsScript}</em>
            </div>
          </div>

          <div style="font-size:0.76rem; font-weight:700; color:#94a3b8; margin-top:6px;">
            📋 Lista limpia de códigos (型番) sincronizada con tu selección actual:
          </div>
          <pre class="rog-pre-list" id="rog-kataban-pre">${katabanListText}</pre>
        </div>
      </div>
    `;

    // Bind events
    const b9950 = document.getElementById("rog-btn-9950");
    if (b9950) b9950.addEventListener("click", () => { state.cpuChoice = "9950x3d"; renderApp(); });

    const b9850 = document.getElementById("rog-btn-9850");
    if (b9850) b9850.addEventListener("click", () => { state.cpuChoice = "9850x3d"; renderApp(); });

    const bNxsw = document.getElementById("rog-btn-nxsw");
    if (bNxsw) bNxsw.addEventListener("click", () => { state.kbSwitch = "NXSW"; renderApp(); });

    const bNxsm = document.getElementById("rog-btn-nxsm");
    if (bNxsm) bNxsm.addEventListener("click", () => { state.kbSwitch = "NXSM"; renderApp(); });

    const bHack = document.getElementById("rog-btn-hack");
    if (bHack) bHack.addEventListener("click", () => { state.yodobashiHack = !state.yodobashiHack; renderApp(); });

    const bAssembly = document.getElementById("rog-btn-assembly");
    if (bAssembly) bAssembly.addEventListener("click", () => { state.assemblyService = !state.assemblyService; renderApp(); });

    mount.querySelectorAll("[data-store-filter]").forEach(btn => {
      btn.addEventListener("click", () => {
        state.storeFilter = btn.getAttribute("data-store-filter") || "all";
        renderApp();
      });
    });

    const searchInput = document.getElementById("rog-kataban-search");
    if (searchInput) {
      searchInput.addEventListener("input", e => {
        state.searchQuery = e.target.value;
        const pos = e.target.selectionStart;
        renderApp();
        const reInput = document.getElementById("rog-kataban-search");
        if (reInput) {
          reInput.focus();
          try { reInput.setSelectionRange(pos, pos); } catch (err) {}
        }
      });
    }

    mount.querySelectorAll(".rog-copy-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        copyText(btn.getAttribute("data-copy") || "", btn);
      });
    });

    const speakBtn = document.getElementById("rog-speak-ja-btn");
    if (speakBtn) {
      speakBtn.addEventListener("click", () => speakJapanese(fullJaScript));
    }

    const copyJaBtn = document.getElementById("rog-copy-ja-btn");
    if (copyJaBtn) {
      copyJaBtn.addEventListener("click", () => copyText(fullJaScript, copyJaBtn));
    }

    const copyListBtn = document.getElementById("rog-copy-list-btn");
    if (copyListBtn) {
      copyListBtn.addEventListener("click", () => copyText(katabanListText, copyListBtn));
    }
  }

  function init() {
    detectLiveJpyRate();
    renderApp();
    fetch("assets/rog-sin-limites-feed.json?v=1")
      .then(r => r.ok ? r.json() : null)
      .then(json => {
        if (json && json.tower_components) {
          state.data = json;
          renderApp();
        }
      })
      .catch(() => {});
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
