/**
 * AKIHABARA ROG «SIN LÍMITES» + ASUS #DREAMPCLIST (UPGRADE WHAT MATTERS 2026)
 * HARDWARE & KATABAN LIVE PRICE TRACKER API v4.0
 *
 * Includes 3 Complete Workstations:
 * 1. Configuración «Sin Límites» (Nivel 3: Extreme Tope Absoluto · ¥2,809,059 JPY) -> Bed Room 2 (デンコボーイ司令室 4.0帖)
 * 2. AI Starter (Versión AMD · #dreampclist · ¥334,400 JPY / ~$1,920–$2,230 USD) -> Sala (LDK 12.7帖)
 * 3. Content Creator Extreme (ProArt + ROG RTX 5090 / 5080 · #dreampclist · ¥1,952,960 JPY + Monitores ProArt PA32UCDM / PA32KCX 8K) -> Sala / Estudio (LDK 12.7帖)
 */
(function () {
  "use strict";

  const FALLBACK_DATA = {
    meta: {
      api_name: "Akihabara ROG «Sin Límites» + ASUS #dreampclist (Upgrade What Matters 2026) Price Tracker API",
      version: "4.0.0-dreampclist",
      tier: "Nivel 3 ROG «Sin Límites» (Cuarto Bruno) + #dreampclist AI Starter AMD & Content Creator Extreme (Sala LDK 12.7帖)",
      updated_at: "2026-10-18T07:05:00Z",
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
    ai_starter_amd: [
      {
        id: "ai_cpu_9700x",
        slot: "cpu",
        category: "Procesador (CPU)",
        name: "AMD Ryzen 7 9700X (o Ryzen 5 9600X · Zen 5 AVX-512 512-bit · 65W)",
        kataban: "100-100001404WOF",
        kataban_alt: "Ryzen 7 9700X BOX / Ryzen 5 9600X BOX",
        why_included: "Arquitectura Zen 5 con soporte nativo de instrucciones AVX-512 de 512 bits para acelerar inferencia en CPU y bajo consumo energético (65W)",
        usd_range: "$319 USD",
        jpy_range: "¥53,800",
        price_doc_jpy: 53800,
        price_live_note: "$319 USD / ¥53,800 en TSUKUMO / PC Shop ARK (Opción Ryzen 5 9600X: ¥39,800)",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/100-100001404WOF/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=Ryzen+7+9700X",
          ark: "https://www.ark-pc.co.jp/search/?key=100-100001404WOF",
          amazon: "https://www.amazon.co.jp/s?k=Ryzen+7+9700X+BOX"
        }
      },
      {
        id: "ai_mb_prime_b850",
        slot: "mb",
        category: "Tarjeta Madre",
        name: "ASUS Prime B850-PLUS WIFI (o TUF Gaming B850-PLUS WIFI)",
        kataban: "PRIME B850-PLUS WIFI",
        kataban_alt: "TUF GAMING B850-PLUS WIFI",
        why_included: "Socket AM5, ranura PCIe 5.0 x16 para la GPU, 3 puertos M.2, Wi-Fi 6E/7, ASUS AI Advisor y AI Networking II",
        usd_range: "$189 – $219 USD",
        jpy_range: "¥34,800 – ¥39,800",
        price_doc_jpy: 37800,
        price_live_note: "$189–$219 USD / ¥34,800 (Prime B850) a ¥39,800 (TUF B850) en TSUKUMO / ARK",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PRIME%20B850-PLUS%20WIFI/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=B850-PLUS+WIFI",
          ark: "https://www.ark-pc.co.jp/search/?key=B850-PLUS+WIFI",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+PRIME+B850-PLUS+WIFI"
        }
      },
      {
        id: "ai_gpu_5060ti_16gb",
        slot: "gpu",
        category: "Tarjeta Gráfica (GPU)",
        name: "ASUS Prime / TUF Gaming GeForce RTX 5060 Ti 16GB GDDR7 (o Prime RTX 5070 12GB)",
        kataban: "PRIME-RTX5060TI-O16G",
        kataban_alt: "TUF-RTX5060TI-O16G-GAMING / PRIME-RTX5070-O12G",
        why_included: "Los 16 GB de VRAM GDDR7 y los núcleos Tensor de 5.ª generación (arquitectura Blackwell con soporte FP4) permiten cargar modelos de IA medianos (Llama / DeepSeek en Ollama/LM Studio) completos en memoria de video",
        usd_range: "$479 – $599 USD",
        jpy_range: "¥84,800 – ¥108,000",
        price_doc_jpy: 96800,
        price_live_note: "$479–$599 USD / ¥84,800 – ¥108,000 en TSUKUMO eX. / PC Shop ARK",
        best_store: "TSUKUMO eX. / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ASUS%20RTX%205060%20Ti%2016GB/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=RTX+5060+Ti+16GB",
          ark: "https://www.ark-pc.co.jp/search/?key=RTX5060TI+16G",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+Prime+RTX+5060+Ti+16GB"
        }
      },
      {
        id: "ai_ram_32gb",
        slot: "ram",
        category: "Memoria RAM",
        name: "32 GB (2 x 16 GB) DDR5-6000 CL30 (Corsair Vengeance / TeamGroup T-Force EXPO)",
        kataban: "CMK32GX5M2B6000Z30",
        kataban_alt: "FF3D532G6000HC30DC01 (T-Force Delta)",
        why_included: "Capacidad base indispensable para manejar contenedores de IA, compilación de código y multitarea con perfiles AMD EXPO",
        usd_range: "$480 – $520 USD",
        jpy_range: "¥62,000",
        price_doc_jpy: 62000,
        price_live_note: "$480–$520 USD / ¥62,000 en PC Shop ARK / TSUKUMO",
        best_store: "PC Shop ARK / TSUKUMO",
        store_tags: ["ark", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/CMK32GX5M2B6000Z30/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=DDR5-6000+16GBx2+CL30",
          ark: "https://www.ark-pc.co.jp/search/?key=CMK32GX5M2B6000Z30",
          amazon: "https://www.amazon.co.jp/s?k=CMK32GX5M2B6000Z30"
        }
      },
      {
        id: "ai_aio_prime_lc360",
        slot: "aio",
        category: "Enfriamiento Líquido (AIO)",
        name: "ASUS Prime LC 360 ARGB (Espejo infinito intercambiable)",
        kataban: "PRIME LC 360 ARGB",
        kataban_alt: "90RC0100-M0UAY0",
        why_included: "Enfriamiento de 360 mm silencioso con lentes de espejo infinito intercambiables en el bloque de la CPU",
        usd_range: "$129 USD",
        jpy_range: "¥19,800",
        price_doc_jpy: 19800,
        price_live_note: "$129 USD / ¥19,800 en TSUKUMO / Amazon.co.jp",
        best_store: "TSUKUMO / Amazon.co.jp",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PRIME%20LC%20360%20ARGB/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PRIME+LC+360+ARGB",
          ark: "https://www.ark-pc.co.jp/search/?key=PRIME+LC+360+ARGB",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+Prime+LC+360+ARGB"
        }
      },
      {
        id: "ai_ssd_gen4_2tb",
        slot: "ssd",
        category: "Almacenamiento",
        name: "SSD NVMe PCIe 4.0 de 1 TB / 2 TB (WD_Black SN850X / Lexar NM790 ~7,000 MB/s)",
        kataban: "WDS200T2X0E",
        kataban_alt: "WDS100T2X0E (1TB: ¥18,500 / 2TB: ¥32,000)",
        why_included: "Velocidad de lectura de ~7,000 MB/s para cargar checkpoints de Stable Diffusion y datasets de varios gigabytes en segundos",
        usd_range: "$115 – $195 USD",
        jpy_range: "¥18,500 – ¥32,000",
        price_doc_jpy: 25800,
        price_live_note: "$115–$195 USD / ¥18,500 (1TB) a ¥32,000 (2TB) en PC Shop ARK / TSUKUMO",
        best_store: "PC Shop ARK / TSUKUMO",
        store_tags: ["ark", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/WDS200T2X0E/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=WDS200T2X0E",
          ark: "https://www.ark-pc.co.jp/search/?key=WDS200T2X0E",
          amazon: "https://www.amazon.co.jp/s?k=WDS200T2X0E"
        }
      },
      {
        id: "ai_psu_prime_750g",
        slot: "psu",
        category: "Fuente de Poder (PSU)",
        name: "ASUS Prime 750W Gold (Prime 750G) o Prime 850G (ATX 3.1 · PCIe 5.1 12V-2x6)",
        kataban: "AP-750G",
        kataban_alt: "AP-850G (Prime 850W Gold)",
        why_included: "Certificación 80 Plus Gold, estándar ATX 3.1 y cable nativo PCIe 5.1 (12V-2x6) listo para tarjetas serie RTX 50",
        usd_range: "$109 – $129 USD",
        jpy_range: "¥18,900 – ¥21,800",
        price_doc_jpy: 19800,
        price_live_note: "$109–$129 USD / ¥18,900 (750G) a ¥21,800 (850G) en TSUKUMO / Kakaku",
        best_store: "TSUKUMO / Amazon.co.jp",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ASUS%20AP-750G/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ASUS+Prime+750W",
          ark: "https://www.ark-pc.co.jp/search/?key=AP-750G",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+Prime+750W+Gold"
        }
      },
      {
        id: "ai_case_ap202",
        slot: "case",
        category: "Gabinete (Chassis)",
        name: "ASUS Prime AP202 TG ARGB (o ASUS ProArt PA401)",
        kataban: "PRIME AP202 TG ARGB",
        kataban_alt: "PROART PA401 WOOD EDITION TG",
        why_included: "Chasis de flujo de aire optimizado con panel de cristal templado y diseño limpio que ocupa poco espacio en el escritorio de la Sala (LDK 12.7帖)",
        usd_range: "$99 – $129 USD",
        jpy_range: "¥15,800 – ¥21,000",
        price_doc_jpy: 18600,
        price_live_note: "$99–$129 USD / ¥15,800 (Prime AP202) a ¥21,000 (ProArt PA401) en TSUKUMO",
        best_store: "TSUKUMO / Yodobashi",
        store_tags: ["tsukumo", "yodobashi", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20PA401/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+PA401",
          ark: "https://www.ark-pc.co.jp/search/?key=PA401",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+PA401"
        }
      }
    ],
    content_creator_extreme: [
      {
        id: "cc_cpu_9950x3d",
        slot: "cpu",
        option_group: "cc_platform",
        option_key: "amd",
        is_default: true,
        category: "Procesador (Opción AMD)",
        name: "AMD Ryzen 9 9950X3D (o Ryzen 9 9950X · 16 Núcleos / 32 Hilos)",
        kataban: "Ryzen 9 9950X3D BOX",
        kataban_alt: "100-100000719WOF / Ryzen 9 9950X BOX",
        why_included: "16 núcleos y 32 hilos para tiempos de renderizado mínimos en Blender, Cinema 4D, Unreal Engine 5 y compilación pesada",
        usd_range: "$699 USD",
        jpy_range: "¥109,980",
        price_doc_jpy: 109980,
        price_live_note: "$699 USD / ¥109,980 en TSUKUMO / PC Shop ARK",
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
        id: "cc_cpu_285k",
        slot: "cpu",
        option_group: "cc_platform",
        option_key: "intel",
        is_default: false,
        category: "Procesador (Opción Intel)",
        name: "Intel Core Ultra 9 285K (24 Núcleos: 8P + 16E · Intel Quick Sync 8K)",
        kataban: "BX80768285K",
        kataban_alt: "Core Ultra 9 285K BOX",
        why_included: "24 núcleos (8P + 16E) con codificador Intel Quick Sync para aceleración por hardware de líneas de tiempo 8K en Premiere Pro y DaVinci Resolve",
        usd_range: "$515 USD",
        jpy_range: "¥92,800",
        price_doc_jpy: 92800,
        price_live_note: "$515 USD / ¥92,800 en TSUKUMO / PC Shop ARK",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/BX80768285K/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=Core+Ultra+9+285K",
          ark: "https://www.ark-pc.co.jp/search/?key=BX80768285K",
          amazon: "https://www.amazon.co.jp/s?k=BX80768285K"
        }
      },
      {
        id: "cc_mb_x870e_proart",
        slot: "mb",
        option_group: "cc_platform",
        option_key: "amd",
        is_default: true,
        category: "Tarjeta Madre (Opción AMD)",
        name: "ASUS ProArt X870E-CREATOR WIFI (10GbE + 2.5GbE · Dual USB4 40Gbps · PCIe 5.0 x8/x8)",
        kataban: "PROART X870E-CREATOR WIFI",
        kataban_alt: "90MB1J40-M0EAY0",
        why_included: "Doble ranura PCIe 5.0 (x8/x8 para 2 GPUs), 10Gb + 2.5Gb Ethernet para NAS, Dual USB4 (40 Gbps), Wi-Fi 7 y 4 ranuras M.2",
        usd_range: "$499 USD",
        jpy_range: "¥89,800",
        price_doc_jpy: 89800,
        price_live_note: "$499 USD / ¥89,800 en TSUKUMO / PC Shop ARK",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20X870E-CREATOR%20WIFI/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+X870E-CREATOR+WIFI",
          ark: "https://www.ark-pc.co.jp/search/?key=PROART+X870E-CREATOR+WIFI",
          amazon: "https://www.amazon.co.jp/s?k=PROART+X870E-CREATOR+WIFI"
        }
      },
      {
        id: "cc_mb_z890_proart",
        slot: "mb",
        option_group: "cc_platform",
        option_key: "intel",
        is_default: false,
        category: "Tarjeta Madre (Opción Intel)",
        name: "ASUS ProArt Z890-CREATOR WIFI (Thunderbolt 5 80/120Gbps · 10GbE + 2.5GbE · 5x M.2)",
        kataban: "PROART Z890-CREATOR WIFI",
        kataban_alt: "90MB1J10-M0EAY0",
        why_included: "Equipada con puertos Thunderbolt 5 (hasta 80/120 Gbps), 10Gb + 2.5Gb Ethernet, Wi-Fi 7 y 5 ranuras M.2",
        usd_range: "$529 USD",
        jpy_range: "¥94,800",
        price_doc_jpy: 94800,
        price_live_note: "$529 USD / ¥94,800 en TSUKUMO / PC Shop ARK",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20Z890-CREATOR%20WIFI/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+Z890-CREATOR+WIFI",
          ark: "https://www.ark-pc.co.jp/search/?key=PROART+Z890-CREATOR+WIFI",
          amazon: "https://www.amazon.co.jp/s?k=PROART+Z890-CREATOR+WIFI"
        }
      },
      {
        id: "cc_gpu_5090",
        slot: "gpu",
        option_group: "cc_gpu",
        option_key: "rtx5090",
        is_default: true,
        category: "Tarjeta Gráfica (GPU — Opción Tope RTX 5090)",
        name: "ASUS ROG Astral GeForce RTX 5090 32GB GDDR7 OC (NVENC 9.ª Gen 4:2:2 10-bit)",
        kataban: "ROG-ASTRAL-RTX5090-O32G-GAMING",
        kataban_alt: "TUF-RTX5090-O32G-GAMING",
        why_included: "32 GB de VRAM y codificadores NVENC de 9.ª generación con soporte nativo para video 4:2:2 de 10 bits y modelos de IA generativa pesados",
        usd_range: "$4,829+ USD",
        jpy_range: "¥1,199,800",
        price_doc_jpy: 1199800,
        price_live_note: "$4,829+ USD / ¥1,199,800 en TSUKUMO eX. / PC Shop ARK",
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
        id: "cc_gpu_proart_5080",
        slot: "gpu",
        option_group: "cc_gpu",
        option_key: "rtx5080",
        is_default: false,
        category: "Tarjeta Gráfica (GPU — Opción ProArt RTX 5080)",
        name: "ASUS ProArt GeForce RTX 5080 16GB GDDR7 OC (2.5-Slot Slim para Dual-GPU x8/x8)",
        kataban: "PROART-RTX5080-O16G",
        kataban_alt: "PROART-RTX5080-O16G (1x o 2x unidades)",
        why_included: "Diseño compacto 2.5-slot sin RGB pensado para estaciones ProArt de estudio y configuraciones de simple o doble GPU",
        usd_range: "$2,800 USD",
        jpy_range: "¥480,000",
        price_doc_jpy: 480000,
        price_live_note: "$2,800 USD / ¥480,000 en TSUKUMO eX. / PC Shop ARK",
        best_store: "TSUKUMO eX. / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20RTX%205080/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+RTX+5080",
          ark: "https://www.ark-pc.co.jp/search/?key=PROART+RTX5080",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+RTX+5080"
        }
      },
      {
        id: "cc_ram_128gb",
        slot: "ram",
        category: "Memoria RAM",
        name: "64 GB (2x32GB) o 128 GB / 192 GB (4x48GB) DDR5 (G.Skill / Corsair Workstation Kit)",
        kataban: "F5-6000J3040G32GX2-TZ5NR",
        kataban_alt: "CMK96GX5M2B6000C30 ×2 (192GB Kit: ¥240,000)",
        why_included: "Para simulaciones de fluidos, caching de After Effects en tiempo real y escenas 3D con millones de polígonos",
        usd_range: "$1,030 – $1,850 USD",
        jpy_range: "¥123,800 – ¥240,000",
        price_doc_jpy: 123800,
        price_live_note: "$1,030–$1,850 USD / ¥123,800 (64GB) a ¥240,000 (192GB 4x48GB) en PC Shop ARK",
        best_store: "PC Shop ARK",
        store_tags: ["ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/F5-6000J3040G32GX2-TZ5NR/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=DDR5+48GBx2",
          ark: "https://www.ark-pc.co.jp/search/?key=F5-6000J3040G32GX2-TZ5NR",
          amazon: "https://www.amazon.co.jp/s?k=F5-6000J3040G32GX2-TZ5NR"
        }
      },
      {
        id: "cc_aio_proart_lc420",
        slot: "aio",
        category: "Enfriamiento Líquido (AIO)",
        name: "ASUS ProArt LC 420 (o ProArt LC 360 · Ventiladores Noctua NF-A14 industrialPPC-2000 PWM)",
        kataban: "PROART LC 420",
        kataban_alt: "90RC00N0-M0UAY0 / PROART LC 360",
        why_included: "Radiador de 420 mm con ventiladores Noctua NF-A14 industrialPPC-2000 PWM e indicador luminoso minimalista de carga en la bomba",
        usd_range: "$289 USD",
        jpy_range: "¥46,800",
        price_doc_jpy: 46800,
        price_live_note: "$289 USD / ¥46,800 en TSUKUMO / PC Shop ARK / Amazon.co.jp",
        best_store: "TSUKUMO / PC Shop ARK",
        store_tags: ["tsukumo", "ark", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20LC%20420/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+LC+420",
          ark: "https://www.ark-pc.co.jp/search/?key=PROART+LC+420",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+LC+420"
        }
      },
      {
        id: "cc_ssd_8tb_dual",
        slot: "ssd",
        category: "Almacenamiento (8TB Total)",
        name: "4 TB PCIe 5.0 NVMe (WD_Black SN8100 / Crucial T705) + 4 TB PCIe 4.0 (Samsung 990 PRO)",
        kataban: "WDS400T1X0M + MZ-V9P4T0B-IT",
        kataban_alt: "CT4000T705SSD3 + MZ-V9P4T0B-IT",
        why_included: "Unidad principal Gen 5 (~14,500–14,900 MB/s) para scratch disk de video 8K RAW y secundaria de 4 TB para librería de proyectos",
        usd_range: "$610 USD (8TB total)",
        jpy_range: "¥267,980",
        price_doc_jpy: 267980,
        price_live_note: "¥139,980 (SN8100 4TB Gen5) + ¥128,000 (990 PRO 4TB Gen4) = ¥267,980 en ARK / TSUKUMO",
        best_store: "PC Shop ARK / TSUKUMO",
        store_tags: ["ark", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/WDS400T1X0M/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=MZ-V9P4T0B-IT",
          ark: "https://www.ark-pc.co.jp/search/?key=WDS400T1X0M",
          amazon: "https://www.amazon.co.jp/s?k=WDS400T1X0M"
        }
      },
      {
        id: "cc_psu_proart_1200w",
        slot: "psu",
        category: "Fuente de Poder (PSU)",
        name: "ASUS ProArt 1200W Platinum (o ROG Thor 1200W Platinum III)",
        kataban: "PROART-1200P",
        kataban_alt: "ROG-THOR-1200P3-GAMING",
        why_included: "Potencia estable de 1200W para soportar picos de renderizado con CPU y GPU al 100% durante horas",
        usd_range: "$399 – $499 USD",
        jpy_range: "¥68,000 – ¥80,524",
        price_doc_jpy: 72000,
        price_live_note: "$399–$499 USD / ¥68,000 (ProArt 1200W) a ¥80,524 (ROG Thor III 1200W) en TSUKUMO",
        best_store: "TSUKUMO / Amazon.co.jp",
        store_tags: ["tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/ROG-THOR-1200P3-GAMING/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=ASUS+1200W+Platinum",
          ark: "https://www.ark-pc.co.jp/search/?key=ROG-THOR-1200P3-GAMING",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ROG+Thor+1200W+Platinum+III"
        }
      },
      {
        id: "cc_case_pa602",
        slot: "case",
        category: "Gabinete (Chassis)",
        name: "ASUS ProArt PA602 (Normal o Wood Edition con madera de fresno certificada FSC)",
        kataban: "PROART PA602 WOOD EDITION TG",
        kataban_alt: "PROART PA602 / 90DC00J0-B09000",
        why_included: "Ventiladores frontales de 200 mm x 38 mm preinstalados, detector infrarrojo de polvo en el filtro frontal y ruedas integradas para mover la estación en la Sala (LDK 12.7帖)",
        usd_range: "$229 – $269 USD",
        jpy_range: "¥39,800 – ¥46,800",
        price_doc_jpy: 42800,
        price_live_note: "$229–$269 USD / ¥39,800 (PA602) a ¥46,800 (PA602 Wood Edition) en TSUKUMO / Yodobashi",
        best_store: "TSUKUMO / Yodobashi",
        store_tags: ["tsukumo", "yodobashi", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PROART%20PA602/",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PROART+PA602",
          ark: "https://www.ark-pc.co.jp/search/?key=PROART+PA602",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+PA602"
        }
      }
    ],
    proart_monitors: [
      {
        id: "mon_pa32ucdm",
        slot: "monitor_proart",
        option_group: "proart_mon_choice",
        option_key: "pa32ucdm",
        is_default: true,
        category: "Monitor ProArt Opción 1 (31.5\" 4K QD-OLED 240Hz)",
        name: "ASUS ProArt Display OLED PA32UCDM (31.5\" 4K QD-OLED a 240Hz, ΔE < 1, Thunderbolt 4 96W)",
        kataban: "PA32UCDM",
        kataban_alt: "ProArt Display OLED PA32UCDM",
        why_included: "Precisión de color de estudio (ΔE < 1, 99% DCI-P3) combinada con 240Hz QD-OLED y puerto Thunderbolt 4 en cadena",
        usd_range: "~$1,499 USD",
        jpy_range: "¥238,000",
        price_doc_jpy: 238000,
        price_live_note: "~$1,499 USD / ¥238,000 en Yodobashi Camera (+10% Gold Points) / TSUKUMO",
        best_store: "Yodobashi / TSUKUMO",
        store_tags: ["yodobashi", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PA32UCDM/",
          yodobashi: "https://www.yodobashi.com/?word=PA32UCDM",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PA32UCDM",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+PA32UCDM"
        }
      },
      {
        id: "mon_pa32kcx",
        slot: "monitor_proart",
        option_group: "proart_mon_choice",
        option_key: "pa32kcx",
        is_default: false,
        category: "Monitor ProArt Opción 2 (32\" 8K Mini-LED Colorímetro Motorizado)",
        name: "ASUS ProArt Display 8K PA32KCX (32\" 8K 7680×4320 Mini-LED, 4,096 zonas, 1,200 nits, Dual TB4)",
        kataban: "PA32KCX",
        kataban_alt: "ProArt Display 8K PA32KCX",
        why_included: "Primer monitor profesional 8K Mini-LED de 4,096 zonas del mundo con colorímetro motorizado integrado y 1,200 nits para masterización HDR",
        usd_range: "~$3,999+ USD",
        jpy_range: "~¥650,000",
        price_doc_jpy: 650000,
        price_live_note: "~$3,999+ USD / ~¥650,000 en Yodobashi Camera (+10% Gold Points) / TSUKUMO",
        best_store: "Yodobashi / TSUKUMO",
        store_tags: ["yodobashi", "tsukumo", "kakaku"],
        links: {
          kakaku: "https://kakaku.com/search_results/PA32KCX/",
          yodobashi: "https://www.yodobashi.com/?word=PA32KCX",
          tsukumo: "https://shop.tsukumo.co.jp/search/?keyword=PA32KCX",
          amazon: "https://www.amazon.co.jp/s?k=ASUS+ProArt+PA32KCX"
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
    activeBuildTab: "all",       // "all" | "sin_limites" | "creator_extreme" | "ai_starter"
    cpuChoice: "9950x3d",        // "9950x3d" | "9850x3d" (Sin Límites)
    kbSwitch: "NXSW",            // "NXSW" (Snow) | "NXSM" (Storm)
    yodobashiHack: false,
    assemblyService: false,
    ccPlatform: "amd",           // "amd" (9950X3D + X870E ProArt) | "intel" (Ultra 9 285K + Z890 ProArt)
    ccGpu: "rtx5090",            // "rtx5090" (¥1,199,800) | "rtx5080" (¥480,000)
    ccMonitor: "pa32ucdm",       // "pa32ucdm" (¥238,000) | "pa32kcx" (¥650,000) | "none" (¥0)
    salaStationMode: "ai_starter", // "ai_starter" (¥334,400) | "creator_extreme" | "both"
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
    // 1. Sin Límites (Bed Room 2: DenkoBoy Command Center)
    const towerItems = (d.tower_components || []).filter(it => {
      if (it.option_group === "cpu_choice") {
        return it.option_key === state.cpuChoice;
      }
      return true;
    });

    const towerSubtotal = towerItems.reduce((acc, it) => acc + it.price_doc_jpy, 0);
    const displaySubtotal = (d.display_system || []).reduce((acc, it) => acc + it.price_doc_jpy, 0);
    const periphSubtotal = (d.peripherals || []).reduce((acc, it) => acc + it.price_doc_jpy, 0);

    const grossTotal = towerSubtotal + displaySubtotal + periphSubtotal;
    const assemblyCost = state.assemblyService ? 22000 : 0;
    const hackMouseSavings = state.yodobashiHack ? 45800 : 0;
    const hackSetSavings = state.yodobashiHack ? 16500 : 0;
    const totalHackSavings = hackMouseSavings + hackSetSavings;
    const netTotal = grossTotal + assemblyCost - totalHackSavings;

    // 2. AI Starter (AMD) — Sala LDK
    const aiStarterSubtotal = (d.ai_starter_amd || []).reduce((acc, it) => acc + it.price_doc_jpy, 0);

    // 3. Content Creator Extreme — Sala / Estudio LDK
    const ccItems = (d.content_creator_extreme || []).filter(it => {
      if (it.option_group === "cc_platform") return it.option_key === state.ccPlatform;
      if (it.option_group === "cc_gpu") return it.option_key === state.ccGpu;
      return true;
    });
    const ccTowerSubtotal = ccItems.reduce((acc, it) => acc + it.price_doc_jpy, 0);
    const ccMonObj = (d.proart_monitors || []).find(m => m.option_key === state.ccMonitor);
    const ccMonitorSubtotal = ccMonObj ? ccMonObj.price_doc_jpy : 0;
    const ccTotal = ccTowerSubtotal + ccMonitorSubtotal;

    // Active Living Room (Sala LDK 12.7帖) PC Budget
    let salaActiveTotal = aiStarterSubtotal;
    let salaActiveLabel = "AI Starter (Versión AMD · #dreampclist)";
    if (state.salaStationMode === "creator_extreme") {
      salaActiveTotal = ccTotal;
      salaActiveLabel = `Content Creator Extreme (${state.ccPlatform.toUpperCase()} + ${state.ccGpu === "rtx5090" ? "RTX 5090" : "ProArt RTX 5080"})`;
    } else if (state.salaStationMode === "both") {
      salaActiveTotal = aiStarterSubtotal + ccTotal;
      salaActiveLabel = "Dual Sala: AI Starter (AMD) + Content Creator Extreme";
    }

    return {
      towerSubtotal,
      displaySubtotal,
      periphSubtotal,
      grossTotal,
      assemblyCost,
      totalHackSavings,
      netTotal,
      aiStarterSubtotal,
      ccTowerSubtotal,
      ccMonitorSubtotal,
      ccTotal,
      salaActiveTotal,
      salaActiveLabel,
      combinedEcosystemTotal: netTotal + salaActiveTotal
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

    const salaSection = state.salaStationMode === "ai_starter"
      ? [
          "",
          "【LDK（リビング 12.7帖）用サブ機：ASUS #dreampclist AI Starter (AMD)】",
          "・CPU: AMD Ryzen 7 9700X BOX (100-100001404WOF)",
          "・M/B: ASUS PRIME B850-PLUS WIFI (または TUF GAMING B850-PLUS WIFI)",
          "・GPU: ASUS PRIME-RTX5060TI-O16G (16GB GDDR7)",
          "・RAM: DDR5-6000 CL30 32GB (16GB×2 EXPO / CMK32GX5M2B6000Z30)",
          "・AIO: ASUS PRIME LC 360 ARGB",
          "・SSD: WD_Black SN850X 2TB (WDS200T2X0E)",
          "・PSU: ASUS Prime 750W Gold (AP-750G)",
          "・CASE: ASUS PRIME AP202 TG ARGB (または ProArt PA401)"
        ].join("\n")
      : [
          "",
          "【LDK（リビング 12.7帖）用スタジオ機：ASUS #dreampclist Content Creator Extreme】",
          state.ccPlatform === "amd"
            ? "・CPU: AMD Ryzen 9 9950X3D BOX (100-100000719WOF)\n・M/B: ASUS PROART X870E-CREATOR WIFI (10GbE + Dual USB4)"
            : "・CPU: Intel Core Ultra 9 285K (BX80768285K)\n・M/B: ASUS PROART Z890-CREATOR WIFI (Thunderbolt 5 + 10GbE)",
          state.ccGpu === "rtx5090"
            ? "・GPU: ASUS ROG-ASTRAL-RTX5090-O32G-GAMING"
            : "・GPU: ASUS PROART-RTX5080-O16G",
          "・RAM: G.Skill F5-6000J3040G32GX2-TZ5NR (64GB / または 128GB-192GB DDR5)",
          "・AIO: ASUS PROART LC 420 (Noctua NF-A14 industrialPPC-2000 PWM)",
          "・SSD: WD_Black SN8100 4TB (WDS400T1X0M) + Samsung 990 PRO 4TB (MZ-V9P4T0B-IT)",
          "・PSU: ASUS PROART-1200P (1200W Platinum)",
          "・CASE: ASUS PROART PA602 WOOD EDITION TG",
          state.ccMonitor === "pa32kcx"
            ? "・Monitor ProArt: ASUS ProArt Display 8K PA32KCX (32\" 8K Mini-LED)"
            : (state.ccMonitor === "pa32ucdm" ? "・Monitor ProArt: ASUS ProArt Display OLED PA32UCDM (31.5\" 4K 240Hz)" : "")
        ].filter(Boolean).join("\n");

    return [
      "【メイン機（Bed Room 2 司令室）：ROG「Sin Límites」Extreme 構成】",
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
      "・Mic: ASUS ROG CARNYX/BLK" + salaSection + assemblyLine
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
        item.why_included || "",
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
      btns.push(`<a href="${links.kakaku}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-kakaku" title="Buscar el precio más bajo en Kakaku.com">🔍 Kakaku 購入 🔗</a>`);
    }
    if (links.tsukumo) {
      btns.push(`<a href="${links.tsukumo}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-tsukumo" title="Buscar en TSUKUMO Akihabara">🏬 TSUKUMO 購入 🔗</a>`);
    }
    if (links.ark) {
      btns.push(`<a href="${links.ark}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-ark" title="Buscar en PC Shop ARK Akihabara">🛡️ ARK 購入 🔗</a>`);
    }
    if (links.yodobashi) {
      btns.push(`<a href="${links.yodobashi}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-yodobashi" title="Buscar en Yodobashi Camera (10% Gold Points)">⚡ Yodobashi 購入 🔗</a>`);
    }
    if (links.amazon) {
      btns.push(`<a href="${links.amazon}" target="_blank" rel="noopener" class="rog-store-pill rog-pill-amazon" title="Buscar en Amazon.co.jp">📦 Amazon 購入 🔗</a>`);
    }
    return `<div class="rog-store-links">${btns.join("")}</div>`;
  }

  function renderItemRow(item, opts = {}) {
    let isInactiveOption = false;
    if (item.option_group === "cpu_choice") {
      isInactiveOption = item.option_key !== state.cpuChoice;
    } else if (item.option_group === "cc_platform") {
      isInactiveOption = item.option_key !== state.ccPlatform;
    } else if (item.option_group === "cc_gpu") {
      isInactiveOption = item.option_key !== state.ccGpu;
    } else if (item.option_group === "proart_mon_choice") {
      isInactiveOption = item.option_key !== state.ccMonitor;
    }

    let displayKataban = item.kataban;
    if (item.id === "kb_azoth_extreme_us") {
      displayKataban = state.kbSwitch === "NXSW"
        ? "M702 AZOTH EXTREME/NXSW/US/PBT"
        : "M702 AZOTH EXTREME/NXSM/US/PBT";
    }
    const isFreeMouse = item.id === "mouse_harpe_extreme" && state.yodobashiHack;
    const effectivePrice = isFreeMouse ? 0 : item.price_doc_jpy;
    const usdShort = "$" + Math.round(effectivePrice / (state.jpyRate || 147)).toLocaleString("en-US");

    return `
      <tr class="rog-item-row ${isInactiveOption ? "rog-row-inactive-cpu" : ""}" data-item-id="${item.id}">
        <td>
          <div style="font-weight:700; color:#f8fafc;">${item.category}</div>
          ${item.option_group ? `
            <span class="rog-cpu-badge ${isInactiveOption ? "inactive" : "active"}">
              ${isInactiveOption ? "Opción Alternativa (No sumada al subtotal activo)" : "✅ Seleccionado en tu Build"}
            </span>
          ` : ""}
        </td>
        <td>
          <div style="font-weight:700; color:#e2e8f0;">${item.name}</div>
          ${item.why_included ? `<div style="font-size:0.76rem; color:#cbd5e1; margin-top:4px; line-height:1.4;">🎯 <strong>Por qué se incluye:</strong> ${item.why_included}</div>` : ""}
          <div style="font-size:0.73rem; color:#94a3b8; margin-top:3px;">📊 ${item.price_live_note || ""}</div>
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
            <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
              <span style="font-weight:800; color:${isInactiveOption ? "#94a3b8" : "#f8fafc"}; font-size:0.95rem;">${fmtYen(effectivePrice)}</span>
              <span class="imperio-inline-usd">${usdShort}</span>
            </div>
            ${item.usd_range ? `<div style="font-size:0.7rem; color:#38bdf8; margin-top:2px;">Ref. #dreampclist: ${item.usd_range} / ${item.jpy_range}</div>` : ""}
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
      .rog-build-tabs {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 8px;
        margin-bottom: 14px;
      }
      .rog-build-tab {
        background: rgba(18, 24, 38, 0.9);
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 10px;
        padding: 10px 12px;
        text-align: left;
        cursor: pointer;
        color: #e2e8f0;
        transition: all 0.18s ease;
      }
      .rog-build-tab:hover {
        border-color: rgba(212, 168, 83, 0.65);
        transform: translateY(-1px);
      }
      .rog-build-tab.active {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.22), rgba(212, 168, 83, 0.16));
        border-color: #ef4444;
        box-shadow: 0 0 16px rgba(239, 68, 68, 0.25);
      }
      .rog-build-tab .tab-eyebrow {
        font-size: 0.66rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #f59e0b;
        font-weight: 800;
      }
      .rog-build-tab .tab-title {
        font-size: 0.86rem;
        font-weight: 800;
        color: #ffffff;
        margin: 2px 0;
      }
      .rog-build-tab .tab-price {
        font-family: 'Orbitron', monospace;
        font-size: 0.82rem;
        color: #4ade80;
        font-weight: 700;
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
      .rog-kpi-card.sala-highlight {
        border-color: rgba(56, 189, 248, 0.65);
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.14), rgba(168, 85, 247, 0.1));
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
        font-size: 1.18rem;
        font-weight: 900;
        color: #f8fafc;
        margin-top: 4px;
      }
      .rog-kpi-sub {
        font-size: 0.74rem;
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
        font-size: 0.75rem;
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
      .rog-toggle-btn.proart-active {
        background: linear-gradient(135deg, rgba(212, 168, 83, 0.28), rgba(56, 189, 248, 0.22));
        border-color: #d4a853;
        color: #fde047;
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
      .rog-section-hdr.proart {
        background: rgba(212, 168, 83, 0.12);
        border-left-color: #d4a853;
      }
      .rog-section-hdr.aistarter {
        background: rgba(56, 189, 248, 0.12);
        border-left-color: #38bdf8;
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

  function notifyFloorplanSync(totals) {
    window.__IMPERIO_ASUS_STATE__ = {
      salaStationMode: state.salaStationMode,
      ccPlatform: state.ccPlatform,
      ccGpu: state.ccGpu,
      ccMonitor: state.ccMonitor,
      cpuChoice: state.cpuChoice,
      totals: totals
    };
    window.dispatchEvent(new CustomEvent("imperio:asus-station-updated", {
      detail: window.__IMPERIO_ASUS_STATE__
    }));
  }

  function renderApp() {
    const mount = document.getElementById("rog-sin-limites-api-mount");
    if (!mount) return;
    injectStyles();

    const totals = computeTotals();
    notifyFloorplanSync(totals);

    const headerSub = document.getElementById("rog-tech-room-subtotal");
    if (headerSub) {
      headerSub.innerHTML = `${fmtYen(totals.netTotal)} <span class="imperio-inline-usd">⚡ ${fmtUsd(totals.netTotal)}</span>`;
    }
    const salaSubEl = document.getElementById("sala-pc-room-subtotal");
    if (salaSubEl) {
      salaSubEl.innerHTML = `${fmtYen(totals.salaActiveTotal)} <span class="imperio-inline-usd">⚡ ${fmtUsd(totals.salaActiveTotal)}</span>`;
    }

    const d = state.data;
    const towerRows = (d.tower_components || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const displayRows = (d.display_system || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const periphRows = (d.peripherals || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const aiStarterRows = (d.ai_starter_amd || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const ccExtremeRows = (d.content_creator_extreme || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");
    const proartMonRows = (d.proart_monitors || []).filter(matchesFilter).map(it => renderItemRow(it)).join("");

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

    const showSinLimites = state.activeBuildTab === "all" || state.activeBuildTab === "sin_limites";
    const showAiStarter = state.activeBuildTab === "all" || state.activeBuildTab === "ai_starter";
    const showCreatorExtreme = state.activeBuildTab === "all" || state.activeBuildTab === "creator_extreme";

    mount.innerHTML = `
      <div class="rog-api-shell">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
          <div>
            <span style="display:inline-block; background:rgba(239,68,68,0.2); border:1px solid #ef4444; color:#fca5a5; font-size:0.7rem; font-weight:800; padding:3px 9px; border-radius:999px; letter-spacing:0.06em;">
              🔴 API EN VIVO v4.0 · ROG «SIN LÍMITES» + CAMPAÑA ASUS #DREAMPCLIST (UPGRADE WHAT MATTERS 2026)
            </span>
            <h3 style="margin:6px 0 2px 0; color:#f8fafc; font-size:1.08rem;">
              🔥 Ecosistema Completo ASUS Japón: 1) «Sin Límites» ROG Extreme (Cuarto Bruno 4.0帖) + 2) AI Starter AMD &amp; 3) Content Creator Extreme ProArt (Sala LDK 12.7帖)
            </h3>
            <p style="margin:0; font-size:0.8rem; color:#94a3b8;">
              Todos los códigos oficiales <strong>型番 (Kataban)</strong> verificados en <strong>Kakaku.com</strong>, <strong>TSUKUMO eX.</strong>, <strong>PC Shop ARK</strong> y <strong>Yodobashi Camera Multimedia Akiba</strong>, sincronizados en tiempo real con el <strong>Mapa CAD de la Sala (LDK 12.7帖)</strong>.
            </p>
          </div>
          <div style="text-align:right; font-size:0.75rem; color:#94a3b8;">
            <div>Tipo de Cambio Activo: <strong style="color:#4ade80;">1 USD = ¥${state.jpyRate.toFixed(2)} JPY</strong></div>
            <div>3 Estaciones ASUS · Impuestos Incluidos (税込)</div>
          </div>
        </div>

        <!-- PESTAÑAS DE LAS 3 CONFIGURACIONES ASUS -->
        <div class="rog-build-tabs">
          <button type="button" class="rog-build-tab ${state.activeBuildTab === "all" ? "active" : ""}" data-build-tab="all">
            <div class="tab-eyebrow">🌐 VISTA COMPLETA (3 ESTACIONES)</div>
            <div class="tab-title">Ver Todas las Configuraciones ASUS</div>
            <div class="tab-price">Cuarto Bruno (4.0帖) + Sala (LDK 12.7帖)</div>
          </button>
          <button type="button" class="rog-build-tab ${state.activeBuildTab === "sin_limites" ? "active" : ""}" data-build-tab="sin_limites">
            <div class="tab-eyebrow">💻 BED ROOM 2 (デンコボーイ司令室 4.0帖)</div>
            <div class="tab-title">1. «Sin Límites» (ROG Nivel 3 Extreme)</div>
            <div class="tab-price">${fmtYen(totals.netTotal)} (${fmtUsd(totals.netTotal)})</div>
          </button>
          <button type="button" class="rog-build-tab ${state.activeBuildTab === "ai_starter" ? "active" : ""}" data-build-tab="ai_starter">
            <div class="tab-eyebrow">🛋️ SALA LDK (12.7帖) · #DREAMPCLIST</div>
            <div class="tab-title">2. AI Starter (Versión AMD · IA Local)</div>
            <div class="tab-price">${fmtYen(totals.aiStarterSubtotal)} (~$1,920–$2,230 USD)</div>
          </button>
          <button type="button" class="rog-build-tab ${state.activeBuildTab === "creator_extreme" ? "active" : ""}" data-build-tab="creator_extreme">
            <div class="tab-eyebrow">🎬 SALA / ESTUDIO LDK (12.7帖) · #DREAMPCLIST</div>
            <div class="tab-title">3. Content Creator Extreme (ProArt 8K)</div>
            <div class="tab-price">${fmtYen(totals.ccTowerSubtotal)} (+ Monitor ProArt)</div>
          </button>
        </div>

        <!-- 4 KPI CARDS (RESUMEN DE PRESUPUESTO MULTIZONA) -->
        <div class="rog-kpi-grid">
          <div class="rog-kpi-card highlight">
            <div class="rog-kpi-lbl">💻 Cuarto Bruno (4.0帖): «Sin Límites» ROG</div>
            <div class="rog-kpi-val" style="color:#fde047;">${fmtYen(totals.netTotal)}</div>
            <div class="rog-kpi-sub">${fmtUsd(totals.netTotal)} · Torre ¥2.10M + 2x OLED ¥486.8K + Perif. ¥215.5K</div>
          </div>
          <div class="rog-kpi-card">
            <div class="rog-kpi-lbl">🤖 #dreampclist 1: AI Starter (AMD)</div>
            <div class="rog-kpi-val">${fmtYen(totals.aiStarterSubtotal)}</div>
            <div class="rog-kpi-sub">~$1,920–$2,230 USD (~¥308K–¥358K) · Ryzen 7 9700X + RTX 5060 Ti 16GB</div>
          </div>
          <div class="rog-kpi-card">
            <div class="rog-kpi-lbl">🎬 #dreampclist 2: Content Creator Extreme</div>
            <div class="rog-kpi-val">${fmtYen(totals.ccTowerSubtotal)}</div>
            <div class="rog-kpi-sub">${fmtUsd(totals.ccTowerSubtotal)} (Torre ProArt) · + Monitor ProArt: ${fmtYen(totals.ccTotal)}</div>
          </div>
          <div class="rog-kpi-card sala-highlight">
            <div class="rog-kpi-lbl">🛋️ Estación Activa en Mapeo de Sala (LDK 12.7帖)</div>
            <div class="rog-kpi-val" style="color:#38bdf8;">${fmtYen(totals.salaActiveTotal)}</div>
            <div class="rog-kpi-sub" style="color:#e2e8f0;">${totals.salaActiveLabel} · <a href="#floor-plan" style="color:#4ade80; text-decoration:underline;">Ver en Mapa CAD LDK ↗</a></div>
          </div>
        </div>

        <!-- BARRA INTERACTIVA DE CONFIGURACIÓN Y SINCRONIZACIÓN CON LA SALA (LDK 12.7帖) -->
        <div class="rog-controls-bar">
          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#38bdf8; font-weight:800;">🛋️ PC asignada a la Sala (LDK 12.7帖):</span>
            <button type="button" class="rog-toggle-btn ${state.salaStationMode === "ai_starter" ? "proart-active" : ""}" id="rog-sala-ai">
              🤖 AI Starter AMD (${fmtYen(totals.aiStarterSubtotal)})
            </button>
            <button type="button" class="rog-toggle-btn ${state.salaStationMode === "creator_extreme" ? "proart-active" : ""}" id="rog-sala-cc">
              🎬 Content Creator Extreme (${fmtYen(totals.ccTotal)})
            </button>
            <button type="button" class="rog-toggle-btn ${state.salaStationMode === "both" ? "proart-active" : ""}" id="rog-sala-both">
              ⚡ Ambas en Sala (${fmtYen(totals.aiStarterSubtotal + totals.ccTotal)})
            </button>
          </div>

          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#d4a853; font-weight:800;">Opciones Content Creator:</span>
            <button type="button" class="rog-toggle-btn ${state.ccPlatform === "amd" ? "active" : ""}" id="rog-cc-amd">
              AMD 9950X3D + X870E ProArt
            </button>
            <button type="button" class="rog-toggle-btn ${state.ccPlatform === "intel" ? "active" : ""}" id="rog-cc-intel">
              Intel Ultra 9 285K + Z890 TB5
            </button>
            <button type="button" class="rog-toggle-btn ${state.ccGpu === "rtx5090" ? "active" : ""}" id="rog-cc-5090">
              GPU: RTX 5090 32GB (¥1.19M)
            </button>
            <button type="button" class="rog-toggle-btn ${state.ccGpu === "rtx5080" ? "active" : ""}" id="rog-cc-5080">
              GPU: ProArt RTX 5080 (¥480K)
            </button>
            <button type="button" class="rog-toggle-btn ${state.ccMonitor === "pa32ucdm" ? "proart-active" : ""}" id="rog-cc-mon4k">
              🖥️ +PA32UCDM 4K OLED (¥238K)
            </button>
            <button type="button" class="rog-toggle-btn ${state.ccMonitor === "pa32kcx" ? "proart-active" : ""}" id="rog-cc-mon8k">
              🖥️ +PA32KCX 8K Mini-LED (¥650K)
            </button>
          </div>
        </div>

        <!-- CONTROLES DE LA TORRE PRINCIPAL SIN LÍMITES Y FILTRO DE TIENDAS -->
        <div class="rog-controls-bar" style="border-color:rgba(239,68,68,0.28);">
          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#94a3b8; font-weight:700;">CPU «Sin Límites»:</span>
            <button type="button" class="rog-toggle-btn ${state.cpuChoice === "9950x3d" ? "active" : ""}" id="rog-btn-9950">
              🔥 Ryzen 9 9950X3D (¥109,980)
            </button>
            <button type="button" class="rog-toggle-btn ${state.cpuChoice === "9850x3d" ? "active" : ""}" id="rog-btn-9850">
              ⚡ Ryzen 7 9850X3D (¥69,940)
            </button>
            <button type="button" class="rog-toggle-btn ${state.kbSwitch === "NXSW" ? "active" : ""}" id="rog-btn-nxsw">
              ❄️ Switch NX Snow (/US)
            </button>
            <button type="button" class="rog-toggle-btn ${state.kbSwitch === "NXSM" ? "active" : ""}" id="rog-btn-nxsm">
              🌩️ Switch NX Storm (/US)
            </button>
          </div>

          <div class="rog-btn-group">
            <button type="button" class="rog-toggle-btn ${state.yodobashiHack ? "hack-active" : ""}" id="rog-btn-hack">
              💡 ${state.yodobashiHack ? "Hack Yodobashi Activo (-¥62,300)" : "Aplicar Truco Yodobashi Gold Points (~¥65,000 Ahorro)"}
            </button>
            <button type="button" class="rog-toggle-btn ${state.assemblyService ? "active" : ""}" id="rog-btn-assembly">
              🛠️ ${state.assemblyService ? "Con 組立代行サービス (+¥22,000)" : "Armado DIY (¥0)"}
            </button>
          </div>
        </div>

        <!-- FILTRO POR TIENDA Y BUSCADOR DE KATABAN -->
        <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:space-between; margin-bottom:12px;">
          <div class="rog-btn-group">
            <span style="font-size:0.74rem; color:#94a3b8; font-weight:700;">Filtrar Tienda:</span>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "all" ? "active" : ""}" data-store-filter="all">Todas (39 códigos)</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "tsukumo" ? "active" : ""}" data-store-filter="tsukumo">🏬 TSUKUMO eX.</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "ark" ? "active" : ""}" data-store-filter="ark">🛡️ PC Shop ARK</button>
            <button type="button" class="rog-toggle-btn ${state.storeFilter === "yodobashi" ? "active" : ""}" data-store-filter="yodobashi">⚡ Yodobashi (10% Pts)</button>
          </div>
          <input type="search" class="rog-search-input" id="rog-kataban-search" placeholder="🔎 Filtrar pieza o 型番 (ej. ProArt, B850, 5090, PA32KCX)..." value="${state.searchQuery}">
        </div>

        ${showAiStarter ? `
          <!-- ===================================================================
               SECCIÓN A: AI STARTER (VERSIÓN AMD) — #DREAMPCLIST (SALA LDK 12.7帖)
               =================================================================== -->
          <div class="rog-section-hdr aistarter">
            <div>
              <h4>🤖 Estación de Sala Opción A: AI Starter (Versión AMD · #dreampclist Upgrade What Matters 2026) — IA Local, LLMs (Llama/DeepSeek en Ollama/LM Studio), Stable Diffusion &amp; Productividad</h4>
              <div style="font-size:0.75rem; color:#bae6fd; margin-top:2px;">
                📍 Ubicación en el Mapa CAD: <strong>Living Dining Kitchen (LDK 12.7帖 · Esquina Noreste junto a toma 10GbE LAN)</strong> · Prioriza <strong>16 GB de VRAM GDDR7 (FP4 Blackwell)</strong> + <strong>32 GB DDR5-6000 CL30</strong> + <strong>Zen 5 AVX-512 (65W)</strong>.
              </div>
            </div>
            <span style="font-weight:800; color:#38bdf8; white-space:nowrap;">
              Total AI Starter: ${fmtYen(totals.aiStarterSubtotal)} (~$1,920 – $2,230 USD / ~¥308K – ¥358K)
            </span>
          </div>
          <div class="table-responsive">
            <table>
              <thead>
                <tr>
                  <th>Categoría</th>
                  <th>Componente de la Muestra (AMD) &amp; Por qué se incluye en este nivel</th>
                  <th>Código Exacto en Japón (型番)</th>
                  <th>Precio Aprox. (USD / JPY)</th>
                  <th>Mejor Tienda &amp; Links</th>
                </tr>
              </thead>
              <tbody>
                ${aiStarterRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
              </tbody>
            </table>
          </div>
        ` : ""}

        ${showCreatorExtreme ? `
          <!-- ===================================================================
               SECCIÓN B: CONTENT CREATOR EXTREME — #DREAMPCLIST (SALA / ESTUDIO LDK 12.7帖)
               =================================================================== -->
          <div class="rog-section-hdr proart">
            <div>
              <h4>🎬 Estación de Sala Opción B: Content Creator Extreme (#dreampclist ASUS ProArt + ROG) — Estación de Trabajo 8K, 3D, VFX e IA Avanzada</h4>
              <div style="font-size:0.75rem; color:#fde68a; margin-top:2px;">
                📍 Ubicación en el Mapa CAD: <strong>Living Dining Kitchen (LDK 12.7帖 · Estudio Creativo Compartido Bruno &amp; あやめ)</strong> · Conectividad <strong>10GbE + Dual USB4 (40Gbps) / Thunderbolt 5 (80/120Gbps)</strong>, NVENC 9.ª Gen 4:2:2 10-bit y chasis <strong>ProArt PA602 con ruedas integradas</strong>.
              </div>
            </div>
            <span style="font-weight:800; color:#fde047; white-space:nowrap;">
              Torre: ${fmtYen(totals.ccTowerSubtotal)} · Con Monitor ProArt: ${fmtYen(totals.ccTotal)} (${fmtUsd(totals.ccTotal)})
            </span>
          </div>
          <div class="table-responsive">
            <table>
              <thead>
                <tr>
                  <th>Categoría</th>
                  <th>Componente de la Muestra (Extreme) &amp; Por qué es el estándar para creación pesada</th>
                  <th>Código Exacto en Japón (型番)</th>
                  <th>Precio Aprox. (USD / JPY)</th>
                  <th>Mejor Tienda &amp; Links</th>
                </tr>
              </thead>
              <tbody>
                ${ccExtremeRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
              </tbody>
            </table>
          </div>

          <!-- MONITORES PROART RECOMENDADOS -->
          <div class="rog-section-hdr proart" style="margin-top:10px;">
            <h4>🖥️ Monitores ASUS ProArt que acompañan al Content Creator Extreme en la Sala (Calibración ΔE &lt; 1)</h4>
            <span style="font-weight:800; color:#fde047;">Activo: ${state.ccMonitor === "pa32kcx" ? "PA32KCX 8K Mini-LED (¥650,000)" : "PA32UCDM 4K QD-OLED 240Hz (¥238,000)"}</span>
          </div>
          <div class="table-responsive">
            <table>
              <thead>
                <tr>
                  <th>Monitor ProArt</th>
                  <th>Especificaciones de Estudio &amp; Colorimetría</th>
                  <th>Código Exacto en Japón (型番)</th>
                  <th>Precio Aprox. (USD / JPY)</th>
                  <th>Mejor Tienda &amp; Links</th>
                </tr>
              </thead>
              <tbody>
                ${proartMonRows || `<tr><td colspan="5" style="text-align:center; color:#94a3b8;">Sin coincidencias para el filtro actual.</td></tr>`}
              </tbody>
            </table>
          </div>
        ` : ""}

        ${showSinLimites ? `
          <!-- ===================================================================
               SECCIÓN C: CONFIGURACIÓN «SIN LÍMITES» (NIVEL 3: EXTREME TOPE ABSOLUTO · CUARTO BRUNO 4.0帖)
               =================================================================== -->
          <div style="background:rgba(34,197,94,0.09); border:1px solid rgba(34,197,94,0.38); border-radius:10px; padding:11px 14px; margin:16px 0 12px 0; font-size:0.82rem; color:#e2e8f0;">
            <strong style="color:#4ade80;">💎 Truco para ahorrarte ~¥65,000 JPY el mismo día en Akihabara (Torre «Sin Límites»):</strong>
            Compra primero los dos monitores <code>PG32UCDM3</code> y los dos brazos <code>AAS01</code> en <strong>Yodobashi Camera (Multimedia Akiba)</strong> o <strong>Bic Camera</strong>. Como ambos dan el <strong>10% en puntos Gold Point</strong>, recibirás al instante <strong>~¥48,680 en puntos</strong>. Con esos puntos en la tarjeta, sube al piso de periféricos de la misma tienda y llévate el <strong>ROG Harpe Ace Extreme (<code>P718 ROG HARPE ACE EXTREME</code> · ¥45,800)</strong> <strong>completamente gratis (¥0)</strong>. Luego camina 5 minutos hasta <strong>TSUKUMO eX.</strong> o <strong>PC Shop ARK</strong> para comprar las piezas de la torre con el descuento de paquete CPU + Motherboard (<code>セット割引</code>).
          </div>

          <div class="rog-section-hdr">
            <h4>1. La Torre Principal «Sin Límites» en Bed Room 2 (デンコボーイ司令室 4.0帖 · Códigos Exactos 型番)</h4>
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
        ` : ""}

        <!-- SECCIÓN 5: NOTA LISTA PARA MOSTRAR EN EL MOSTRADOR (TSUKUMO eX. / PC SHOP ARK) -->
        <div class="rog-counter-card">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
            <div>
              <h4 style="margin:0; color:#fde047; font-size:0.98rem;">
                🗣️ Nota Lista para Mostrar en el Mostrador (TSUKUMO eX. Pisos 4F/5F/6F &amp; PC Shop ARK) — Incluye Torre Principal + PC de Sala
              </h4>
              <div style="font-size:0.76rem; color:#94a3b8;">
                Muestra esta tarjeta en tu celular en Akihabara para que el encargado reúna todas las cajas (Cuarto Bruno + Estación de Sala), aplique el descuento CPU+M/B y verifique el teclado US Layout.
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
            📋 Lista limpia de códigos (型番) sincronizada con tu selección actual (Bed Room 2 + Sala LDK):
          </div>
          <pre class="rog-pre-list" id="rog-kataban-pre">${katabanListText}</pre>
        </div>
      </div>
    `;

    // Bind Build Tabs
    mount.querySelectorAll("[data-build-tab]").forEach(btn => {
      btn.addEventListener("click", () => {
        state.activeBuildTab = btn.getAttribute("data-build-tab") || "all";
        renderApp();
      });
    });

    // Bind Sala Mode buttons
    const bSalaAi = document.getElementById("rog-sala-ai");
    if (bSalaAi) bSalaAi.addEventListener("click", () => { state.salaStationMode = "ai_starter"; renderApp(); });

    const bSalaCc = document.getElementById("rog-sala-cc");
    if (bSalaCc) bSalaCc.addEventListener("click", () => { state.salaStationMode = "creator_extreme"; renderApp(); });

    const bSalaBoth = document.getElementById("rog-sala-both");
    if (bSalaBoth) bSalaBoth.addEventListener("click", () => { state.salaStationMode = "both"; renderApp(); });

    // Bind Content Creator toggles
    const bCcAmd = document.getElementById("rog-cc-amd");
    if (bCcAmd) bCcAmd.addEventListener("click", () => { state.ccPlatform = "amd"; renderApp(); });

    const bCcIntel = document.getElementById("rog-cc-intel");
    if (bCcIntel) bCcIntel.addEventListener("click", () => { state.ccPlatform = "intel"; renderApp(); });

    const bCc5090 = document.getElementById("rog-cc-5090");
    if (bCc5090) bCc5090.addEventListener("click", () => { state.ccGpu = "rtx5090"; renderApp(); });

    const bCc5080 = document.getElementById("rog-cc-5080");
    if (bCc5080) bCc5080.addEventListener("click", () => { state.ccGpu = "rtx5080"; renderApp(); });

    const bCcMon4k = document.getElementById("rog-cc-mon4k");
    if (bCcMon4k) bCcMon4k.addEventListener("click", () => { state.ccMonitor = "pa32ucdm"; renderApp(); });

    const bCcMon8k = document.getElementById("rog-cc-mon8k");
    if (bCcMon8k) bCcMon8k.addEventListener("click", () => { state.ccMonitor = "pa32kcx"; renderApp(); });

    // Bind Sin Límites buttons
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

  // Expose helper so the Floor Plan CAD API can switch the Living Room station directly
  window.setImperioSalaStationMode = function (mode) {
    if (["ai_starter", "creator_extreme", "both"].includes(mode)) {
      state.salaStationMode = mode;
      renderApp();
    }
  };

  function init() {
    detectLiveJpyRate();
    renderApp();
    fetch("assets/rog-sin-limites-feed.json?v=4")
      .then(r => r.ok ? r.json() : null)
      .then(json => {
        if (json && json.tower_components) {
          state.data = Object.assign({}, FALLBACK_DATA, json);
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
