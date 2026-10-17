#!/usr/bin/env python3
"""
Generates the Ultimate 2-Year Master Calendar of 384 Unique Dates for Bruno & Ayame
(24 Active Months in Japan = 96 Weeks = 384 Unique Dates + 90-Day Thailand Protocol).
Includes:
  - Real itemized JPY budgets per date (Home, Geek, Tokyo Outing, 1-to-3 Day Prefecture Getaway)
  - Live API Real-Time USD conversion (connected to open.er-api.com & api.frankfurter.dev)
  - 2-to-3 Day Ryokan / Private Onsen / Shinkansen / Regional Wagyu logistics & Pet-Sitter protocol
  - Direct reservation links (Rakuten Travel, Jalan, TableCheck, JR East, Official Venues)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_JS = ROOT / "assets" / "citas-ayame.js"

# Wait: let's import the existing 24 months from our script or define them with enhanced 2-3 day prefecture trips and exact real JPY prices!
from datetime import datetime, timezone

MONTHS_DATA = [
    # ==================== PRIMAVERA 2027 ====================
    {
        "id": "2027-04",
        "title": "Abril 2027 — 🌸 Primavera 1: Cerezos en Flor y Estreno del Nido en Asakusabashi",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Recién instalados en Urbanex Asakusabashi Front · Rehabilitación suave post-VBT en St. Luke's",
        "weeks": [
            {
                "w": 1,
                "home": "Cena inaugural en casa: Filete Tenderloin de Niku no Hanamasa sellado en sartén Lodge + fresas japonesas Tochiotome y armado juntos de su rincón de costura JUKI",
                "home_jpy": 4800,
                "out": "Paseo de Hanami (cerezos en flor) al atardecer por el Parque Sumida (Asakusa) tomando té verde caliente viendo el Skytree iluminado",
                "out_jpy": 3500,
                "geek": "Noche inaugural de Kingdom Hearts HD 1.5+2.5 ReMIX en la PS5 Pro desde Traverse Town con los gatitos encima y bromas de Denji y Reze",
                "geek_jpy": 2500,
                "pref": "🌊 [2 Días / 1 Noche · Prefectura de Kanagawa · Kamakura & Enoshima] Tren JR Green Car + Noche en Kamakura Prince Hotel / Ryokan frente al mar + Gran Buda Kotoku-in + Cena de carne Hayama Wagyu (Pet-sitter 24h en Asakusabashi incluido)",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 2,
                "home": "Taller en casa: elegir patrones del kimono inspirado en Wakamo (Blue Archive) mientras le cocinas Ribeye 300g con mantequilla de ajo y arroz de Zojirushi",
                "home_jpy": 4500,
                "out": "Crucero al atardecer en el Tokyo Cruise (Suijo Bus) por el río Sumida saliendo desde Asakusa hasta Hamarikyu Gardens (boletos + té matcha)",
                "out_jpy": 4600,
                "geek": "Visita juntos a Eorzea Cafe (Final Fantasy XIV) en Pasela Akihabara (a 2 min de casa) pidiendo mocktails sin alcohol de Poción y Éter + filete temático",
                "geek_jpy": 9800,
                "pref": "🏮 [Día Completo · Prefectura de Saitama · Koedo Kawagoe] Expreso Red Arrow + alquiler de kimono de paseo para あやめ + Callejón de los Dulces + Almuerzo de Unagi y carne 武蔵野 Wagyu",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            },
            {
                "w": 3,
                "home": "Spa de Hinoki en casa: baño aromático con sales de ciprés japonés, mascarillas faciales coreanas y cena de Striploin con piña fresca",
                "home_jpy": 5200,
                "out": "Recorrido por Nippori Fabric Town (日暮里繊維街, a 10 min en JR): visitar Tomato Fabrics para comprar sedas carmesí y brocados dorados para あやめ",
                "out_jpy": 14500,
                "geek": "Tarde en Akihabara Radio Kaikan y AmiAmi buscando figuras oficiales de Blue Archive (Yuuka, Ako y Wakamo) para decorar ambos escritorios",
                "geek_jpy": 18000,
                "pref": "⛩️ [2 Días / 1 Noche · Prefectura de Chiba · Naritasan & Sawara] Hotel tradicional en Sawara (el Pequeño Edo de canales) + paseo en barca + Templo Naritasan Shinshoji + Cena Kazusa Wagyu",
                "pref_jpy": 54000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 4,
                "home": "Noche de cine Ghibli en el sofá N-Shield de Nitori: ver 'El Viaje de Chihiro' con hamburguesas caseras 100% Wagyu hechas por ti y té de cebada",
                "home_jpy": 4200,
                "out": "Festival de las Glicinas (Fuji Matsuri) en el Santuario Kameido Tenjin (a 2 estaciones en JR Sobu) bajo túneles morados de flores + cena Yakiniku",
                "out_jpy": 11500,
                "geek": "Sesión cooperativa en Nintendo Switch 2 (Mario Kart / It Takes Two) en el televisor 55\" 4K con apuesta de masajes de hombros",
                "geek_jpy": 3000,
                "pref": "🎡 [2 Días / 1 Noche · Prefectura de Kanagawa · Yokohama Minato Mirai] Estancia en Yokohama Royal Park / InterContinental con vista a la bahía + Jardín Sankeien + Teleférico Air Cabin + Steakhouse en Motomachi",
                "pref_jpy": 64000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2027-05",
        "title": "Mayo 2027 — 🌸 Primavera 2: Brisa de Mayo, Rosas y Artesanía de Edo",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mes 3–4 post-cirugía · Paseos al aire libre y escapadas de 2–3 días en tren expreso",
        "weeks": [
            {
                "w": 5,
                "home": "Noche de Teppanyaki casero: cubos de filete estilo Saikoro Steak con brotes de soya en sartén de hierro y prueba de telas en el maniquí 9号 de あやめ",
                "home_jpy": 4900,
                "out": "Jardín de Rosas de Primavera en los Jardines Kyu-Furukawa (Kita-ku): villa occidental histórica rodeada de 100 variedades de rosas + salón de té",
                "out_jpy": 5800,
                "geek": "Visita a Square Enix Garden / ARTNIA en Shinjuku para ver los cristales de Final Fantasy, comprar peluches de Moogle/Chocobo y parfaits",
                "geek_jpy": 11200,
                "pref": "🌸 [2 Días / 1 Noche · Prefectura de Tochigi · Ashikaga Flower Park & Sano] Expreso Ryomo + entrada nocturna VIP a la Gran Glicina iluminada + Ryokan en Tochigi con cena Shimotsuke Wagyu",
                "pref_jpy": 59000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 6,
                "home": "Taller de accesorios en casa: armar horquillas de flores (Kanzashi) con cuentas compradas en Asakusabashi mientras cenas Roast Beef casero",
                "home_jpy": 6200,
                "out": "Taller de vidrio tallado tradicional Edo Kiriko en Sumida/Asakusa: grabar juntos un par de vasos de cristal con motivos de flores de cerezo",
                "out_jpy": 13600,
                "geek": "Maratón de Chainsaw Man (Arco de Reze) en casa con bocadillos premium y recreación de las poses surrealistas (シュール) de Denji y Reze",
                "geek_jpy": 3200,
                "pref": "🏝️ [Día Completo · Prefectura de Kanagawa · Isla de Enoshima] Romancecar a Katase-Enoshima + Santuario Benzaiten + Cuevas marinas Iwaya + Faro Sea Candle + Cena de mar y tierra",
                "pref_jpy": 26500,
                "days": "1 Día Completo"
            },
            {
                "w": 7,
                "home": "Cena temática de Ryokan en casa: Sukiyaki hiper-proteico con doble porción de res magra de Hanamasa, tofu y huevo pasteurizado en cazuela",
                "home_jpy": 5500,
                "out": "Planetario Konica Minolta Planetaria TOKYO (Yurakucho) acostados en el asiento doble 'Galaxy Seat' viendo las constelaciones con aromaterapia",
                "out_jpy": 8400,
                "geek": "Tarde de Arcade en GiGO Akihabara y Taito Station: ganar peluches en UFO Catcher para la cama de あやめ y jugar Taiko no Tatsujin juntos",
                "geek_jpy": 7500,
                "pref": "💠 [2 Días / 1 Noche · Prefectura de Ibaraki · Hitachi Seaside Park & Oarai] Expreso Hitachi desde Ueno + colinas azules de nemophilas frente al Pacífico + Ryokan frente al mar en Oarai con carne Hitachi Wagyu",
                "pref_jpy": 62000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 8,
                "home": "Noche de repostería sin azúcar refinada ni mango: preparar juntos Cheesecake japonés esponjoso con fresas después de cenar filete Sirloin",
                "home_jpy": 4800,
                "out": "Paseo en bote de remos por el foso de Chidorigafuchi y los Jardines del Este del Palacio Imperial + cena de filetes en Marunouchi",
                "out_jpy": 12800,
                "geek": "Empezar Final Fantasy VII Rebirth en la PS5 Pro: tú pasas los jefes difíciles y あやめ explora el mundo y elige los atuendos en Costa del Sol",
                "geek_jpy": 9800,
                "pref": "🗻 [3 Días / 2 Noches · Prefectura de Yamanashi · Lago Kawaguchiko & Monte Fuji] Expreso Fuji Excursion + 2 noches en Ryokan con Rotenburo privado frente al Monte Fuji + Parque Oishi + Cena Koshu Wagyu A5 + Pet-sitter 48h",
                "pref_jpy": 98000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    # ==================== VERANO 2027 ====================
    {
        "id": "2027-06",
        "title": "Junio 2027 — 🎆 Verano 1: Hortensias (Ajisai), Acuarios y Días de Lluvia Cálida",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Mes 5 post-cirugía · Escapadas a onsens de montaña con hortensias y actividades techadas en Tokio",
        "weeks": [
            {
                "w": 9,
                "home": "Campamento de lluvia en la sala: armar un fuerte de mantas en el sofá Nitori con luces cálidas, cenar filetes con papas al romero y escuchar la lluvia con los gatos",
                "home_jpy": 4400,
                "out": "Ruta de las Hortensias (Bunkyo Ajisai Matsuri) en el Santuario Hakusan: caminar bajo paraguas transparentes entre 3,000 hortensias azules",
                "out_jpy": 5200,
                "geek": "Visita al Museo Ghibli en Mitaka (boletos + café Straw Hat) y paseo por el parque Inokashira",
                "geek_jpy": 7800,
                "pref": "♨️ [2 Días / 1 Noche · Prefectura de Kanagawa · Hakone & Tren de las Hortensias] Romancecar GSE en asientos panorámicos + Ryokan en Gora con onsen privado + Museo al Aire Libre + Crucero Lago Ashi",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 10,
                "home": "Noche de pintura en acuarela: pintar retratos divertidos de sus 2 gatitos y las 2 chinchillas después de cenar Hamburg Steak casero",
                "home_jpy": 5600,
                "out": "Acuario Sumida (en Tokyo Skytree Town, a 6 min de casa): ver la zona de medusas iluminadas y los pingüinos + cena en Solamachi",
                "out_jpy": 13500,
                "geek": "Tarde en Ikebukuro Sunshine City: Pokémon Center Mega Tokyo, tienda Bandai Namco y mercancía de Blue Archive",
                "geek_jpy": 12000,
                "pref": "🐬 [2 Días / 1 Noche · Prefectura de Chiba · Kamogawa Sea World & Costa Boso] Hotel frente al mar con aguas termales + espectáculo de orcas y belugas + cena de filetes y langosta de Boso",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 11,
                "home": "Sesión de costura creativa: terminar el Obi (cinturón) del kimono de Wakamo de あやめ mientras le preparas brochetas de res Kushiyaki en casa",
                "home_jpy": 5100,
                "out": "teamLab Planets TOKYO en Toyosu: caminar descalzos por el agua iluminada con carpas koi digitales y el jardín flotante de orquídeas reales",
                "out_jpy": 11600,
                "geek": "Noche de Kingdom Hearts III en la PS5 Pro: explorar los mundos de Toy Box y Tangled juntos tomando batidos caseros de sandía y fresa",
                "geek_jpy": 2800,
                "pref": "🌊 [3 Días / 2 Noches · Prefectura de Shizuoka · Atami & Península de Izu] Shinkansen Kodama Green Car + 2 noches en Ryokan frente al océano con Rotenburo privado + Jardín ACAO Forest + Wagyu de Shizuoka",
                "pref_jpy": 94000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 12,
                "home": "Cena de degustación de cortes: comparar 150g de Tenderloin vs 150g de Ribeye vs 150g de Striploin hechos a término medio con sal de Okinawa",
                "home_jpy": 6500,
                "out": "Taller de cerámica tradicional en Yanaka (barrio antiguo de gatos en Taito-ku): moldear juntos en torno dos tazas de té para el departamento",
                "out_jpy": 11000,
                "geek": "Ir a Akihabara Mandarake Complex (8 pisos de tesoros retro) a buscar artbooks originales de Kingdom Hearts y Final Fantasy de Tetsuya Nomura",
                "geek_jpy": 14000,
                "pref": "🛶 [Día Completo · Prefectura de Saitama · Chichibu & Nagatoro] Tren panorámico Laview + descenso tranquilo en barca tradicional de madera por las rocas del río Arakawa + carne a la parrilla",
                "pref_jpy": 25000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2027-07",
        "title": "Julio 2027 — 🎆 Verano 2: Tanabata, Fuegos Artificiales del Sumida y Fase 0A en Fighter's Flow",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Arranca tu Fase 0A en Fighter's Flow (15 de julio) con autorización médica · Escapadas a montañas frescas",
        "weeks": [
            {
                "w": 13,
                "home": "Noche de Tanabata (7 de julio) en casa: escribir deseos en tiras de papel (Tanzaku) para colgar en bambú en el balcón + cena de filete Tataki con ponzu",
                "home_jpy": 4900,
                "out": "Tanabata Matsuri en Shitamachi (calle Kappabashi entre Asakusa y Ueno, cerca de casa): pasear bajo las decoraciones gigantes de papel",
                "out_jpy": 5500,
                "geek": "Sesión de fotos profesional en casa: あやめ estrenando su kimono/yukata estilo Wakamo que cosió en su taller y tú con tu outfit de gala",
                "geek_jpy": 4500,
                "pref": "🌅 [Día Completo · Prefectura de Kanagawa · Península de Miura e Isla Jogashima] Caminata por los acantilados volcánicos frente al mar con brisa fresca y almuerzo frente al puerto",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 14,
                "home": "Noche de Kakigori casero saludable: después de cenar filetes de res, preparar hielo raspado estilo japonés con jarabe natural de fresa",
                "home_jpy": 4600,
                "out": "Mercado de las Flores de Farolillo (Hozuki-ichi) en el Templo Senso-ji de Asakusa: comprar una planta de hozuki roja para el balcón",
                "out_jpy": 6800,
                "geek": "Visita a Kirby Cafe en Tokyo Solamachi (Skytree) o pop-up café de Blue Archive en Akihabara (reserva en línea)",
                "geek_jpy": 11500,
                "pref": "🌲 [3 Días / 2 Noches · Prefectura de Tochigi · Nikko & Lago Chuzenji (1,200m de altitud)] Expreso Spacia X en asientos Cockpit Lounge + 2 noches en Ryokan junto al lago con clima fresco de 20°C + Santuario Toshogu + Cascada Kegon",
                "pref_jpy": 96000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 15,
                "home": "Cena post-entreno con tu Mánager: te hace masaje con pistola de percusión en los trapecios tras tu sesión con Hayato Suzuki y cenan Wagyu Burgers caseras",
                "home_jpy": 4800,
                "out": "Art Aquarium Museum GINZA (en Mitsukoshi): exposición de peces dorados (Kingyo) nadando en peceras de cristal iluminadas como linternas",
                "out_jpy": 9200,
                "geek": "Jugar Blue Archive y comparar sus personajes favoritos en la ROG Zephyrus G16 White mientras escuchan el OST de Mitsukiyo",
                "geek_jpy": 3500,
                "pref": "🍃 [2 Días / 1 Noche · Prefectura de Nagano · Karuizawa] Shinkansen Asama (1h 10m) al pueblo alpino fresco de Karuizawa + Hotel en el bosque + Cascada Shiraito + Cena Shinshu Premium Beef",
                "pref_jpy": 72000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 16,
                "home": "Velada de Fuegos Artificiales del Río Sumida (Sumidagawa Hanabi Taikai): ver los 20,000 fuegos artificiales desde Yanagibashi a pasos de tu puerta y cenar filetes en casa sin multitudes",
                "home_jpy": 7500,
                "out": "Maxell Aqua Park Shinagawa: espectáculo nocturno de delfines con proyecciones digitales de fuegos artificiales bajo techo climatizado",
                "out_jpy": 9800,
                "geek": "Visitar exhibición especial de anime de verano en Tokyo Dome City Gallery AaMo y tiendas de coleccionables",
                "geek_jpy": 8500,
                "pref": "🦙 [Día Completo · Prefectura de Chiba · Mother Farm (Madre Bokujo)] Colinas frescas de Chiba: dar de comer a alpacas y comer carne a la parrilla Jingisukan",
                "pref_jpy": 23000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2027-08",
        "title": "Agosto 2027 — 🎆 Verano 3: Farolillos de Verano y Gran Viaje Romántico antes de Phuket",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Último mes en Tokio antes de volar a Tailandia el 1 de septiembre · Mes de consentir al máximo a あやめ",
        "weeks": [
            {
                "w": 17,
                "home": "Noche de Yakiniku sin humo en la mesa: asar láminas de lengua de res (Gyutan) y Harami de Hanamasa con salsa de limón y sésamo",
                "home_jpy": 5800,
                "out": "Festival de Linternas Flotantes (Toro Nagashi) en el río Sumida (Asakusa): lanzar juntos una linterna de papel iluminada sobre el agua al anochecer",
                "out_jpy": 6500,
                "geek": "Ir a Nakano Broadway (el templo del coleccionismo retro y celdas de animación originales) y cenar filete en Nakano",
                "geek_jpy": 14500,
                "pref": "⛰️ [2 Días / 1 Noche · Prefectura de Yamanashi · Altiplano de Kiyosato (1,400m)] Expreso Azusa + Kiyosato Terrace en telesilla con aire fresco + Hotel de montaña con cena de carne Koshu",
                "pref_jpy": 61000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 18,
                "home": "Taller de álbum físico: imprimir las mejores fotos de abril a agosto y armar juntos un álbum scrapbooking con cintas Washi de Asakusabashi",
                "home_jpy": 5200,
                "out": "Jardines Hamarikyu al atardecer: tomar té matcha con wagashi tradicional en la casa de té flotante Nakajima-no-Ochaya sobre el estanque",
                "out_jpy": 5400,
                "geek": "Noche de concierto sinfónico de videojuegos en Tokio (Distant Worlds Final Fantasy / Kingdom Hearts Orchestra o recital de piano de anime)",
                "geek_jpy": 19600,
                "pref": "♨️ [2 Días / 1 Noche · Prefectura de Gunma · Ikaho Onsen] Pueblo de las 365 escaleras de piedra + Ryokan con baño privado (Kashikiri Onsen) de aguas doradas + Carne Joshu Wagyu",
                "pref_jpy": 64000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 19,
                "home": "Preparar 'Cápsulas de Amor' para los 90 días: esconderle 12 cartas escritas a mano por ti (1 para abrir cada domingo que estés en Tailandia) + cena de Tenderloin",
                "home_jpy": 6000,
                "out": "Crucero nocturno en barco tradicional Yakatabune por la bahía de Tokio saliendo de Yanagibashi (¡frente a tu edificio en el río Kanda/Sumida!)",
                "out_jpy": 22000,
                "geek": "Terminar juntos la historia de Kingdom Hearts II Final Mix en la PS5 Pro y dejar configurado Discord + PS Remote Play para jugar juntos desde Phuket",
                "geek_jpy": 3000,
                "pref": "⛩️ [2 Días / 1 Noche · Prefectura de Kanagawa · Hakone Sengokuhara] Ryokan de montaña en Sengokuhara + Santuario Hakone con el Torii rojo en el agua + Carne Ashigara Wagyu",
                "pref_jpy": 69000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 20,
                "home": "Cena especial de despedida pre-campamento en casa: el corte más fino de Wagyu Sirloin A5 + fresas y dejarle toda la despensa, arena de gatos y heno de chinchillas listos para 3 meses",
                "home_jpy": 9500,
                "out": "Mirador Shibuya Sky / Tokyo City View al atardecer viendo todo Tokio iluminarse mientras le prometes volver hecho una máquina para tus 5 peleas",
                "out_jpy": 9000,
                "geek": "Comprar dos amuletos iguales en el Santuario Kanda Myojin (Akihabara): uno para tu maleta de Bangtao y otro para la bolsa de あやめ",
                "geek_jpy": 4000,
                "pref": "🌊 [3 Días / 2 Noches · Prefectura de Shizuoka · Izu Kogen & Monte Omuro] Despedida de 3 días antes de Tailandia: tren Saphir Odoriko + Ryokan con onsen privado mirando al mar + Costa de Jogasaki + Pet-sitter 48h",
                "pref_jpy": 105000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    # ==================== PAUSA 3 MESES EN TAILANDIA (SEPT - NOV 2027) ====================
    {
        "id": "2027-09-11",
        "title": "Septiembre – Noviembre 2027 — 🥊 PAUSA PRESENCIAL: Campamento de 90 Días en Bangtao (Tailandia)",
        "season": "campamento",
        "season_label": "🥊 Campamento Tailandia (90 Días)",
        "phase_note": "Del 1 de septiembre al 11 de diciembre de 2027 estás en Phuket entrenando 2 veces al día y comiendo filetotes en Mamma Mia. No hay citas presenciales en Tokio, pero mantienen este protocolo semanal a distancia (20:00 hrs Tailandia = 22:00 hrs Japón):",
        "weeks": [
            {
                "w": "Tailandia (Sem 1–13)",
                "home": "💌 Domingo de Carta Escondida: Cada domingo en Tokio, あやめ abre una de las 12 cartas físicas que le dejaste escondidas en casa + pedido UberEats sorpresa de filete/postre que le mandas a la puerta",
                "home_jpy": 4500,
                "out": "📸 Reporte de tu Mánager: Le mandas videos cortos de tus sparrings en Bangtao y fotos de tus filetotes en Mamma Mia para que ella elija la música y estética de tus redes",
                "out_jpy": 0,
                "geek": "🎮 Viernes de Co-Op Online (19:30 TH / 21:30 JP): 45 minutos jugando juntos Final Fantasy XIV / Switch 2 online antes de su baño nocturno",
                "geek_jpy": 0,
                "pref": "🌙 Ritual Sagrado de las 22:00 JP (20:00 TH): Videollamada suave de 20 minutos mientras ella está en cama con los gatitos hasta que a las 22:30 JP se duerme tranquila",
                "pref_jpy": 0,
                "days": "Conexión Diaria Online"
            }
        ]
    },
    # ==================== INVIERNO 2027-2028 ====================
    {
        "id": "2027-12",
        "title": "Diciembre 2027 — ❄️ Invierno 1: Regreso Triunfal de Tailandia, Iluminaciones y Navidad Juntos",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Regresas el 11–12 de diciembre hecho una roca de 78.5 kg · Reencuentro con あやめ, Navidad y Año Nuevo en Japón",
        "weeks": [
            {
                "w": 21,
                "home": "Noche de Reencuentro tras 90 días: entregarle sus regalos de Tailandia (sedas tailandesas para su taller de costura) y cenar Filete Tenderloin caliente en casa abrazados con los gatos",
                "home_jpy": 6800,
                "out": "Paseo por las Iluminaciones de Invierno de Marunouchi (calle Naka-dori vestida con 1.2 millones de luces color champán) tomando té caliente",
                "out_jpy": 5500,
                "geek": "Estrenar juntos tu equipamiento Venum x Mike Tyson Black/Gold en casa: sesión de fotos donde tu Mánager あやめ dirige tus poses oficiales de peleador",
                "geek_jpy": 3000,
                "pref": "✨ [Día Completo · Prefectura de Kanagawa · Sagamiko Illumillion] El festival de iluminación más grande de Kanto en el bosque del lago Sagami con telesilla iluminado sobre un mar de luces",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            },
            {
                "w": 22,
                "home": "Noche de Shabu-Shabu invernal en casa: caldo dashi hirviendo con láminas finas de res magra de Hanamasa, hongos shiitake y salsa de ajonjolí",
                "home_jpy": 5400,
                "out": "Mercado Navideño Europeo en Azabudai Hills / Roppongi Hills y caminata viendo la Torre de Tokio iluminada con colores de invierno",
                "out_jpy": 8500,
                "geek": "Visita a Akihabara Kotobukiya y Volks Hobby Paradise para comprar materiales de modelismo y ver las vitrinas navideñas de anime",
                "geek_jpy": 12000,
                "pref": "🌲 [Día Completo · Prefectura de Saitama · Parque Moominvalley (Hanno)] Pueblo nórdico junto al lago Miyazawa en Saitama: cabañas escandinavas y bosque iluminado de invierno",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 23,
                "home": "Cena de Nochebuena (24 de diciembre) en casa: Roast Beef navideño horneado por ti + pastel de Navidad japonés de fresas con crema (Christmas Shortcake)",
                "home_jpy": 8900,
                "out": "Patinaje suave tomados de la mano o paseo por la pista iluminada de Tokyo Midtown (Roppongi) + cena navideña de filetes Wagyu",
                "out_jpy": 18500,
                "geek": "Maratón navideño de Kingdom Hearts (visitar Christmas Town en Halloween Town de KH2) con gorros navideños para los gatitos",
                "geek_jpy": 3500,
                "pref": "🎄 [2 Días / 1 Noche · Prefectura de Chiba · Tokyo German Village & Kisarazu] Hotel frente a la bahía de Tokio + iluminación invernal de 3 millones de LEDs + cena de Navidad",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 24,
                "home": "Nochevieja Japonesa (Omisoka · 31 de diciembre): cenar Toshikoshi Soba con láminas de Roast Beef en casa a las 20:00 y escuchar las campanas de los templos abrazados",
                "home_jpy": 6500,
                "out": "Feria de Año Nuevo (Hagoita-Ichi) en el Templo Senso-ji de Asakusa: ver las paletas decorativas tradicionales de madera pintada",
                "out_jpy": 6000,
                "geek": "Armar juntos su lista de videojuegos y animes más esperados de 2028 mientras abren sobres coleccionables de cartas de Blue Archive / Final Fantasy",
                "geek_jpy": 7500,
                "pref": "♨️ [2 Días / 1 Noche · Prefectura de Kanagawa · Odawara & Yugawara Onsen] Castillo de Odawara + noche de fin de año en Ryokan de Yugawara Onsen con baño termal privado",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2028-01",
        "title": "Enero 2028 — ❄️ Invierno 2: Hatsumode, Nieve Termal y Recta Final al Debut en Tokio",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Enero 2028 · Entrenando en Fighter's Flow con Hayato Suzuki rumbo a tu Pelea #1 en febrero",
        "weeks": [
            {
                "w": 25,
                "home": "Cena de Año Nuevo (Oshogatsu) hiper-carnívora: filetes de Ribeye + Ozoni casero y escribir juntos su caligrafía de Año Nuevo (Kakizome)",
                "home_jpy": 5800,
                "out": "Hatsumode (primera visita al santuario del año) en el Santuario Kanda Myojin: pedir por tu victoria 5–0 en el octágono y por la paz de あやめ y 千秋-san",
                "out_jpy": 5000,
                "geek": "Caza de Fukubukuro (bolsas de la suerte de Año Nuevo) en Akihabara y Animate para あやめ",
                "geek_jpy": 15000,
                "pref": "❄️ [3 Días / 2 Noches · Prefectura de Gunma · Kusatsu Onsen en la Nieve] Expreso Kusatsu-Shima + 2 noches en Ryokan tradicional viendo el Yubatake humeante rodeado de nieve blanca + Carne Joshu Wagyu",
                "pref_jpy": 98000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 26,
                "home": "Taller de vestuario de pelea: あやめ da las últimas puntadas a tu bata/kimono de entrada al octágono mientras tú le cocinas Tenderloin con espárragos",
                "home_jpy": 5200,
                "out": "Exhibición de Bonsáis centenarios en el Jardín Rikugien en calma invernal con casa de té junto al agua",
                "out_jpy": 4800,
                "geek": "Tarde de juegos de mesa japoneses para dos (Shogi / Hanafuda / Machi Koro) y videojuegos indie en la Switch 2",
                "geek_jpy": 4500,
                "pref": "🏔️ [2 Días / 1 Noche · Prefectura de Niigata · Gala Yuzawa & Echigo-Yuzawa Onsen] Shinkansen directo desde Ueno (75 min) hasta la nieve pura de Niigata: subir en góndola a ver los Alpes nevados y dormir en Ryokan termal",
                "pref_jpy": 74000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 27,
                "home": "Noche de Sukiyaki estilo Kansai (dorando primero la carne en hierro fundido) + masaje de pies para あやめ",
                "home_jpy": 5500,
                "out": "Paseo por el Jardín de Ciruelos Tempranos (Ume) en el Santuario Yushima Tenjin (en Bunkyo-ku, a 5 min de casa)",
                "out_jpy": 4200,
                "geek": "Visitar Tamashii Nations Store Tokyo en Akihabara para ver las armaduras a escala real",
                "geek_jpy": 6500,
                "pref": "♨️ [2 Días / 1 Noche · Prefectura de Tochigi · Kinugawa Onsen] Aguas termales junto al cañón nevado del río Kinugawa y visita a Tobu World Square iluminado",
                "pref_jpy": 62000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 28,
                "home": "Ensayo general de pesaje y esquina en casa: practicar con あやめ tu lista de canciones de salida y el protocolo de OS-1 + cena limpia de filete magro",
                "home_jpy": 4800,
                "out": "Crucero de invierno con calefacción y techo de cristal (Himiko / Hotaluna diseñado por Leiji Matsumoto) desde Asakusa hasta Odaiba",
                "out_jpy": 7600,
                "geek": "En Odaiba: ver el Unicorn Gundam tamaño real transformarse con luces nocturnas y entrar a The Gundam Base Tokyo",
                "geek_jpy": 8500,
                "pref": "🦢 [Día Completo · Prefectura de Yamanashi · Lago Yamanaka] Ver los cisnes blancos nadando con el Monte Fuji cubierto de nieve de fondo y almorzar carne Koshu",
                "pref_jpy": 26000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2028-02",
        "title": "Febrero 2028 — ❄️ Invierno 3: ¡MES DE TU DEBUT OFICIAL (Pelea #1) y San Valentín en Tokio!",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Febrero 2028 · ¡Tu Pelea #1 (1–0) en KROSS×OVER / JMMAF con あやめ como tu Mánager oficial!",
        "weeks": [
            {
                "w": 29,
                "home": "Noche de Setsubun (3 de febrero): lanzar frijoles de la suerte ('Oni wa soto! Fuku wa uchi!') con máscaras divertidas y comer rollos Ehomaki rellenos de Roast Beef",
                "home_jpy": 5200,
                "out": "Festival del Ciruelo (Bunkyo Ume Matsuri) en Yushima Tenjin y paseo tranquilo por los jardines de Koishikawa Korakuen",
                "out_jpy": 4800,
                "geek": "Jugar juntos Final Fantasy XVI / VII en modo historia mientras descansas las piernas en la semana previa al corte de agua",
                "geek_jpy": 3000,
                "pref": "🌸 [2 Días / 1 Noche · Prefectura de Shizuoka · Cerezos Tempranos de Kawazu (Kawazu-zakura)] Tren expreso Odoriko a Kawazu para ver los primeros cerezos rosas en pleno febrero + Ryokan termal frente al mar",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 30,
                "home": "Cena de San Valentín (14 de febrero): ella te regala chocolates artesanales japoneses y tú le cocinas Chateaubriand con fresas blancas Awayuki",
                "home_jpy": 8500,
                "out": "Salón del Chocolate (Salon du Chocolat) en Isetan Shinjuku / Nihombashi Mitsukoshi para elegir bombones juntos",
                "out_jpy": 9500,
                "geek": "Cita de fotos Purikura en Akihabara vestida de estilo invernal y tú con tu hoodie Supreme Box Logo",
                "geek_jpy": 4200,
                "pref": "🌺 [Día Completo · Prefectura de Ibaraki · Mito Kairakuen] Uno de los 3 Grandes Jardines de Japón durante el Festival del Ciruelo de Mito (3,000 ciruelos en flor) + Hitachi Beef",
                "pref_jpy": 27000,
                "days": "1 Día Completo"
            },
            {
                "w": 31,
                "home": "🏆 ¡CENA DE VICTORIA DE TU PELEA #1 (1–0)! Banquete en casa con tu medalla/trofeo: Doble Wagyu Burger + Tenderloin 300g y あやめ celebrando como Mánager invicta",
                "home_jpy": 7800,
                "out": "Paseo de celebración por Ginza Chuo-dori comprándole un detalle hermoso en Ginza Itoya (12 pisos de papelería fina para su taller)",
                "out_jpy": 14000,
                "geek": "Comprar una vitrina acrílica con luz LED en Akihabara para exhibir tu primer trofeo/guantes de victoria junto a sus figuras de Blue Archive",
                "geek_jpy": 12500,
                "pref": "♨️ [3 Días / 2 Noches · Prefectura de Kanagawa · Retiro de Victoria en Hakone Gora] 2 noches en Ryokan de lujo en Gora con Rotenburo privado de aguas termales para regenerar tus músculos post-pelea + Pet-sitter 48h",
                "pref_jpy": 108000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 32,
                "home": "Noche de cine y masaje de recuperación: ver juntos los videos de tu sumisión de la Pelea #1 y editar el reel triunfal para redes",
                "home_jpy": 4500,
                "out": "Visita al Museo Edo-Tokyo renovado en Ryogoku (a 1 estación de Asakusabashi) cruzando el río Sumida a pie",
                "out_jpy": 5200,
                "geek": "Tarde en el Café Capcom (Ikebukuro) o Monster Hunter Bar en Shinjuku probando platillos temáticos de cazador",
                "geek_jpy": 9800,
                "pref": "🌼 [Día Completo · Prefectura de Chiba · Península de Boso (Tateyama)] Campos de flores amarillas Nanohana frente al mar en Tateyama con clima templado",
                "pref_jpy": 23500,
                "days": "1 Día Completo"
            }
        ]
    },
    # ==================== PRIMAVERA 2028 ====================
    {
        "id": "2028-03",
        "title": "Marzo 2028 — 🌸 Primavera 3: White Day, Campeonato DEEP Future King (4–0) y Viaje a Kioto",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Marzo 2028 · White Day (14 mar) + Torneo DEEP Future King (Peleas #2, #3 y #4 → ¡Campeón 4–0!)",
        "weeks": [
            {
                "w": 33,
                "home": "Noche de Hinamatsuri (3 de marzo): decorar el departamento con flores de durazno (Momo) y preparar Chirashizushi con láminas de Roast Beef y salmón",
                "home_jpy": 5600,
                "out": "Exposición de las Mil Muñecas Hina en las escaleras históricas Hyakudan Kaidan (Hotel Gajoen Tokyo en Meguro)",
                "out_jpy": 6800,
                "geek": "Noche de estudio de brackets del torneo DEEP Future King con tu Mánager あやめ usando pizarrón estilo anime táctico",
                "geek_jpy": 3000,
                "pref": "🌿 [Día Completo · Prefectura de Saitama · Valle de Hanno & Kinchakuda] Caminata ligera por los ríos cristalinos antes del torneo",
                "pref_jpy": 19500,
                "days": "1 Día Completo"
            },
            {
                "w": 34,
                "home": "Cena de White Day (14 de marzo): regalarle un collar/accesorio delicado + cena de filete Wagyu A5 hecha por ti",
                "home_jpy": 18000,
                "out": "Paseo por el barrio histórico de Kagurazaka (las callejuelas empedradas de Tokio) y postre en una casa de té tradicional",
                "out_jpy": 7500,
                "geek": "Visitar exposición de arte de Final Fantasy (Yoshitaka Amano / Square Enix Pop-up) y comprar pósters enmarcados",
                "geek_jpy": 11000,
                "pref": "🏯 [Día Completo · Prefectura de Kanagawa · Castillo de Odawara en floración temprana] Pasear por los fosos del castillo y comer carne junto al mar",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 35,
                "home": "🏆👑 ¡BANQUETE DE CAMPEÓN DE DEEP FUTURE KING (4–0)! Celebrar en casa con el trofeo/cinturón tras ganar tus 3 peleas en una tarde en New Pier Hall",
                "home_jpy": 9500,
                "out": "Paseo triunfal de Hanami temprano por el río Meguro viendo los farolillos rosas reflejados en el canal con los primeros cerezos",
                "out_jpy": 8000,
                "geek": "Sesión de fotos épica en casa: あやめ posando con tu trofeo de Campeón de DEEP vestida de Wakamo / Ako y tú con tus guantes oficiales",
                "geek_jpy": 3500,
                "pref": "⛩️ [3 Días / 2 Noches · Prefectura de Kioto · Viaje de Campeón en Shinkansen Nozomi a KIOTO] 2 noches en Ryokan tradicional en Higashiyama/Arashiyama + Santuario Fushimi Inari (donde Wakamo se siente en casa) + Kiyomizu-dera + Cena de filete Omi/Kyoto Wagyu + Pet-sitter 48h",
                "pref_jpy": 135000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 36,
                "home": "Noche de picnic Hanami en la sala: preparar juntos cajas Bento de dos pisos con filete Teriyaki casero, tamagoyaki y fresas",
                "home_jpy": 5200,
                "out": "Hanami en el Jardín Nacional Shinjuku Gyoen (1,000 cerezos de 65 variedades): acostarse sobre una manta bajo los pétalos que caen",
                "out_jpy": 4500,
                "geek": "Tarde de compras en Shibuya Parco (6º piso Cyberspace): Nintendo Tokyo, Pokémon Center, Jump Shop y Capcom Store",
                "geek_jpy": 14000,
                "pref": "🚂 [Día Completo · Prefectura de Tochigi · Moka Railway] Ver el tren de vapor real SL Moka cruzando un túnel de cerezos en flor y campos amarillos de colza",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2028-04",
        "title": "Abril 2028 — 🌸 Primavera 4: Viaje Corto a Corea (Estética Fina) y Aniversario de Cerezos",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Abril 2028 · Viaje corto a Seúl (Cantoplastia + 5 Carillas, cero lipo) y regreso a la primavera de Tokio",
        "weeks": [
            {
                "w": 37,
                "home": "Noche de estreno de sonrisa y mirada nueva: cena suave de filete Tenderloin cortado en bocados tiernos y sopa cremosa en casa",
                "home_jpy": 5400,
                "out": "Paseo por el Túnel de Cerezos Tardíos (Yaezakura) y Azaleas del Santuario Nezu (en Bunkyo-ku)",
                "out_jpy": 4500,
                "geek": "Noche de Kingdom Hearts: Birth by Sleep / Dream Drop Distance con gafas de descanso mientras cicatrizan los ojos",
                "geek_jpy": 3000,
                "pref": "🚃 [Día Completo · Prefectura de Chiba · Ferrocarril Kominato] Viaje en el tren retro amarillo cruzando campos de flores primaverales en el corazón rural de Chiba",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 38,
                "home": "Taller de diseño de modas: comprar telas de lino y algodón fresco de primavera para hacer ropa de verano para ambos en la máquina JUKI",
                "home_jpy": 6800,
                "out": "Paseo por el Parque Inokashira en Kichijoji: pedalear en un bote de cisne por el lago y comer pasteles Totoro en Shirohige's Cream Puff Factory",
                "out_jpy": 6500,
                "geek": "Visitar Kichijoji Petit Mura (el pueblo temático de cuento de hadas de gatos en Kichijoji)",
                "geek_jpy": 5800,
                "pref": "🌸 [Día Completo · Prefectura de Saitama · Parque Hitsujiyama (Chichibu)] Ver la alfombra gigante rosa y blanca de Shibazakura (musgo rosa en flor) frente al monte Buko",
                "pref_jpy": 23000,
                "days": "1 Día Completo"
            },
            {
                "w": 39,
                "home": "Noche de Fondue de Queso y Filete: cubos calientes de Striploin a la parrilla sumergidos en queso fundido en la mesa del comedor",
                "home_jpy": 5900,
                "out": "Visita al Jardín Botánico de Koishikawa (el más antiguo de Japón, perteneciente a la Universidad de Tokio) en una tarde soleada",
                "out_jpy": 4200,
                "geek": "Tarde de juegos de ritmo y baile en casa (Just Dance / Taiko / Project Diva) para reírse y mover el cuerpo juntos",
                "geek_jpy": 3500,
                "pref": "🏡 [2 Días / 1 Noche · Prefectura de Kanagawa · Ruta Futura Casa 二世帯住宅 en Shonan/Kamakura] Hotel frente al mar en Kamakura/Tsujido + explorar barrios residenciales tranquilos para el futuro hogar con 千秋-san",
                "pref_jpy": 56000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 40,
                "home": "Noche de Spa capilar y facial en casa: cepillado relajante, mascarillas y cena de salmón salvaje + filete magro",
                "home_jpy": 5200,
                "out": "Festival de las Peonías (Botan Matsuri) en el Templo Ueno Toshogu (a 5 min de Asakusabashi en el Parque Ueno)",
                "out_jpy": 4800,
                "geek": "Ir a Akihabara Super Potato (el museo viviente de consolas retro de los 90s y 2000s) y jugar clásicos en el último piso",
                "geek_jpy": 6500,
                "pref": "⛰️ [2 Días / 1 Noche · Prefectura de Gunma · Parque Floral de Gunma & Monte Akagi] Ryokan de montaña + invernaderos de flores + carne Joshu Wagyu",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2028-05",
        "title": "Mayo 2028 — 🌸 Primavera 5: Boda Civil (Kon'in Todoke), 5ª Pelea (5–0) y Luna de Miel Corta",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mayo 2028 · ¡Boda oficial con あやめ y cierre invicto 5–0 de tu campaña de MMA!",
        "weeks": [
            {
                "w": 41,
                "home": "💍 ¡Noche de Boda Oficial (Kon'in Todoke)! Cena íntima a la luz de las velas LED en casa: Chateaubriand Wagyu A5, fresas reales y brindis con Perrier y jugo de uva blanca (0 alcohol)",
                "home_jpy": 12000,
                "out": "Entregar juntos su registro de matrimonio (婚姻届) en la alcaldía y sesión de fotos vestidos de gala frente a los puentes de piedra de Marunouchi",
                "out_jpy": 25000,
                "geek": "Enmarcar juntos su certificado de matrimonio conmemorativo con diseño especial de anime/flores en su pared del salón",
                "geek_jpy": 5500,
                "pref": "🌸 [Día Especial · Prefectura de Kanagawa · Banquete Familiar de Boda con 千秋-san en Yokohama] Invitar a la mamá de あやめ a un restaurante tradicional con jardín privado en Yokohama para celebrar su matrimonio y mostrarle el respaldo total que tendrá",
                "pref_jpy": 45000,
                "days": "1 Día Familiar"
            },
            {
                "w": 42,
                "home": "Noche de lectura de manga juntos en el sofá: cada uno lee su tomo favorito con los pies entrelazados y los gatitos ronroneando en medio",
                "home_jpy": 4200,
                "out": "Festival Kanda Matsuri / Sanja Matsuri en Asakusa: ver los santuarios portátiles (Mikoshi) dorados desfilando cerca de nuestro barrio",
                "out_jpy": 6500,
                "geek": "Visitar el Museo de Arte de Mori (Roppongi) o exhibición inmersiva de videojuegos/manga en Tokio",
                "geek_jpy": 7800,
                "pref": "🌹 [Día Completo · Prefectura de Chiba · Jardín de Rosas de Keisei (Yachiyo)] Caminar bajo pérgolas de 1,600 variedades de rosas perfumadas en su punto máximo de mayo",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 43,
                "home": "🏆👑 ¡CENA DE LA 5ª PELEA INVICTA (5–0)! Celebrar el retiro invicto de tu campaña amateur con los 2 campeonatos en la vitrina de casa",
                "home_jpy": 9800,
                "out": "Crucero panorámico por los canales de Nihombashi saliendo del puente histórico de Nihombashi bajo el cielo azul de mayo",
                "out_jpy": 8500,
                "geek": "Grabar y editar juntos el documental casero 'De 0–0 a 5–0 en Japón: El Peleador y su Mánager あやめ' para guardarlo toda la vida",
                "geek_jpy": 3000,
                "pref": "🎍 [3 Días / 2 Noches · Prefectura de Shizuoka · Mini Luna de Miel en Shuzenji Onsen (Península de Izu)] 2 noches en Ryokan histórico con Rotenburo privado junto al Bosque de Bambú de Shuzenji y los puentes rojos sobre el río Katsura + Pet-sitter 48h",
                "pref_jpy": 115000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 44,
                "home": "Cena de brochetas de filete y piña asada a la plancha + noche de masajes de espalda completa",
                "home_jpy": 4800,
                "out": "Paseo por el Jardín de Iris (Horikiri Shobuen en Katsushika-ku) viendo miles de flores de iris blancas y moradas junto al agua",
                "out_jpy": 4500,
                "geek": "Tarde de diseño 3D / ilustración en tu PC RTX 5090 ayudando a あやめ a digitalizar sus patrones de costura",
                "geek_jpy": 2500,
                "pref": "🏔️ [3 Días / 2 Noches · Prefectura de Nagano · Kamikochi & Castillo de Matsumoto] Expreso Azusa + 2 noches en los Alpes Japoneses: aguas turquesa del río Azusa en el valle alpino de Kamikochi + Castillo Negro de Matsumoto + Carne Shinshu Wagyu",
                "pref_jpy": 112000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    # ==================== VERANO 2028 ====================
    {
        "id": "2028-06",
        "title": "Junio 2028 — 🎆 Verano 4: Luciérnagas, Santuarios de Musgo y Paz de Recién Casados",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Junio 2028 · Ya con tus 5 peleas ganadas (5–0), entrenas por puro placer y salud sin riesgo de lesiones",
        "weeks": [
            {
                "w": 45,
                "home": "Noche de cine en casa con proyector de estrellas en el techo: ver 'Your Name (Kimi no Na wa)' después de cenar filete Ribeye con espárragos",
                "home_jpy": 4800,
                "out": "Noche de las Luciérnagas (Hotaru no Yube) en los jardines del Hotel Chinzanso Tokyo: caminar de la mano viendo cientos de luciérnagas reales brillar entre la niebla",
                "out_jpy": 12000,
                "geek": "Recorrer las calles de Akihabara y Kanda buscando las locaciones reales de animes famosos y tomar fotos recreando cada plano",
                "geek_jpy": 4500,
                "pref": "💠 [Día Completo · Prefectura de Kanagawa · Kita-Kamakura (Templo Meigetsuin)] Ver la famosa ventana circular (Satori no Mado) rodeada de miles de hortensias azules",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 46,
                "home": "Taller de perfumería casera japonesa: crear bolsitas aromáticas (Nioibukuro) con sándalo y clavo para los closets de su ropa y tus hoodies",
                "home_jpy": 5400,
                "out": "Taller de Kintsugi (reparación de cerámica con polvo dorado) en Tokio: unir una pieza de cerámica juntos como símbolo de sanación y belleza",
                "out_jpy": 13500,
                "geek": "Empezar una partida nueva de Final Fantasy X HD Remaster en la PS5 Pro reviviendo la escena del lago Macalania",
                "geek_jpy": 3000,
                "pref": "🏕️ [2 Días / 1 Noche · Prefectura de Yamanashi · Lago Motosu & Glamping de Lujo frente al Fuji] Ver el lago del billete de ¥1,000 (locación de Yuru Camp) + Glamping con baño privado y BBQ de filetes Koshu Wagyu",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 47,
                "home": "Cena de Roast Beef en costra de hierbas horneado en casa + cata de sandía japonesa dulce de verano",
                "home_jpy": 5200,
                "out": "Visita al Museo Nezu en Minami-Aoyama y caminata por su jardín secreto de bambú y linternas de piedra",
                "out_jpy": 6500,
                "geek": "Ir a una cafetería temática tranquila de gatos/nutrias o pop-up de anime en Harajuku/Ikebukuro que a あやめ le haga ilusión",
                "geek_jpy": 7800,
                "pref": "🛶 [Día Completo · Prefectura de Chiba · Canales de Sawara en temporada de Iris] Paseo en barca bajo sauces llorones y jardín de 400 variedades de iris",
                "pref_jpy": 23000,
                "days": "1 Día Completo"
            },
            {
                "w": 48,
                "home": "Noche de juegos de feria japonesa (Ennichi) en casa: preparar yakisoba con tiras gruesas de filete y jugar pesca de globos de agua en el baño",
                "home_jpy": 4600,
                "out": "Ceremonia de purificación de mitad de año (Nagoshi no Harae) cruzando juntos el gran anillo de junco (Chinowa Kuguri) en el Santuario Kanda",
                "out_jpy": 4500,
                "geek": "Noche de trivia y dibujo de personajes de Blue Archive y Kingdom Hearts de memoria sin ver referencias",
                "geek_jpy": 2500,
                "pref": "🌿 [2 Días / 1 Noche · Prefectura de Tochigi · Nasu Highlands] Shinkansen a Nasu-Shiobara + Ryokan en el bosque fresco + granja South Hills + Tochigi Wagyu",
                "pref_jpy": 64000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2028-07",
        "title": "Julio 2028 — 🎆 Verano 5: Campanas de Viento (Furin), Hokkaido en Verano y Brisa Marina",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Julio 2028 · Incluye escapada de 3 días a los campos de lavanda de Hokkaido (22°C en pleno julio)",
        "weeks": [
            {
                "w": 49,
                "home": "Decorar el balcón de Asakusabashi con una campana de cristal Edo Furin pintada a mano + cena de filete Sirloin con ensalada de pepino japonés",
                "home_jpy": 5200,
                "out": "Mercado de las Campanillas (Asagao Matsuri) en Iriya (Taito-ku, a 6 min de casa)",
                "out_jpy": 5800,
                "geek": "Visitar el Museo Fujiko F. Fujio (Doraemon) o exposición de verano de Weekly Shonen Jump",
                "geek_jpy": 6500,
                "pref": "🎐 [Día Completo · Prefectura de Saitama · Santuario Kawagoe Hikawa (Enmusubi Furin)] Caminar bajo el túnel de 2,000 campanas de viento de cristal que suenan con la brisa para los matrimonios felices",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 50,
                "home": "Noche de helados artesanales en casa: hacer paletas heladas de fresa, arándanos y yogur griego después de cenar filetes a la plancha",
                "home_jpy": 4500,
                "out": "Acuario Sunshine (Ikebukuro) al atardecer viendo los 'pingüinos voladores' nadar sobre el horizonte de Tokio",
                "out_jpy": 8800,
                "geek": "Tarde en Akihabara probando teclados mecánicos custom y keycaps de resina artesanales para el setup de あやめ",
                "geek_jpy": 12000,
                "pref": "🌴 [Día Completo · Prefectura de Kanagawa · Hayama & Zushi Marina] Paseo estilo Riviera japonesa entre palmeras frente al mar en Zushi y carne de res Hayama Gyu",
                "pref_jpy": 25000,
                "days": "1 Día Completo"
            },
            {
                "w": 51,
                "home": "Taller de teñido japonés Shibori (añil Índigo) en casa: teñir dos pañuelos Tenugui con patrones geométricos únicos",
                "home_jpy": 5800,
                "out": "Caminata por el Valle de Todoroki (el único cañón boscoso natural dentro de Tokio con río y puente rojo, 5°C más fresco)",
                "out_jpy": 5200,
                "geek": "Noche de película de Makoto Shinkai ('El Jardín de las Palabras' y 'Weathering With You') abrazados con aire acondicionado fresco",
                "geek_jpy": 3000,
                "pref": "🌉 [2 Días / 1 Noche · Prefectura de Shizuoka · Mishima Skywalk & Izu Nagaoka Onsen] El puente colgante más largo de Japón con vista al Fuji + manantiales cristalinos de Kakita River + Ryokan termal",
                "pref_jpy": 59000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 52,
                "home": "🎉 ¡Semana 52 (1 Año Activo de Citas)! Cena de aniversario del calendario: Filete Tenderloin + pastel de crepas (Mille Crepe) de frutas sin mango",
                "home_jpy": 7800,
                "out": "Festival de Fuegos Artificiales de Adachi o Katsushika sentados cómodos en asientos reservados pagados viendo el cielo iluminarse",
                "out_jpy": 16000,
                "geek": "Crear juntos en PC un fotolibro impreso de tapa dura con las mejores fotos de las primeras 52 semanas de aventuras",
                "geek_jpy": 6500,
                "pref": "💜 [3 Días / 2 Noches · Prefectura de Hokkaido · Sapporo, Otaru y Campos de Lavanda de Furano (Farm Tomita)] Vuelo corto desde Haneda (1h 30m) al verano fresco de 22°C de Hokkaido: colinas infinitas de lavanda morada, canal de Otaru, carne Furano Wagyu y melón Yubari + Pet-sitter 48h",
                "pref_jpy": 148000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    {
        "id": "2028-08",
        "title": "Agosto 2028 — 🎆 Verano 6: Campos de Girasoles, Festivales Obon y Montañas Frescas",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Agosto 2028 · Escapadas a tierras altas frescas y noches mágicas en Tokio",
        "weeks": [
            {
                "w": 53,
                "home": "Cena de Hamburguesas Smash dobles con queso cheddar en pan brioche tostado hechas por ti + batido frío de plátano y fresa",
                "home_jpy": 4800,
                "out": "Iluminación de linternas de verano en el Santuario Tokyo Daijingu / Meiji Jingu",
                "out_jpy": 5500,
                "geek": "Visitar el evento de verano de Akihabara Electric Town Festival y buscar tapices de edición limitada de Wakamo y Yuuka",
                "geek_jpy": 11000,
                "pref": "🌻 [Día Completo · Prefectura de Yamanashi · Campos de Girasoles de Hokuto (Akeno)] Caminar entre 600,000 girasoles amarillos gigantes frente a los Alpes del Sur",
                "pref_jpy": 23000,
                "days": "1 Día Completo"
            },
            {
                "w": 54,
                "home": "Noche de Somen helado en cuenco de hielo con tiras de filete de res a la parrilla y jengibre rallado",
                "home_jpy": 4400,
                "out": "teamLab Borderless en Azabudai Hills: perderse juntos en la sala de lámparas de cristal infinitas (Crystal World)",
                "out_jpy": 11600,
                "geek": "Jugar juntos Kingdom Hearts: Melody of Memory (el juego musical de toda la saga) cantando 'Simple and Clean' y 'Sanctuary'",
                "geek_jpy": 4800,
                "pref": "🚠 [2 Días / 1 Noche · Prefectura de Gunma · Minakami Onsen & Tanigawadake Ropeway] Teleférico a 1,500m de altitud con brisa fresca de 20°C + Ryokan junto al río Tone con Rotenburo",
                "pref_jpy": 64000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 55,
                "home": "Sesión de costura de otoño: diseñar juntos una capa/haori ligera para あやめ que combine con tus outfits",
                "home_jpy": 6200,
                "out": "Jardín Happo-en en Shirokanedai: ver la colección de bonsáis de 500 años y los estanques de carpas koi en silencio absoluto",
                "out_jpy": 5800,
                "geek": "Tarde en un Café de Juegos de Mesa (JELLY JELLY CAFE en Akihabara) en mesa privada para dos",
                "geek_jpy": 5200,
                "pref": "🏞️ [3 Días / 2 Noches · Prefectura de Miyagi · Sendai & Bahía de Matsushima (Una de las 3 Grandes Vistas de Japón)] Shinkansen Hayabusa (90 min desde Ueno) + crucero entre las 260 islas de pinos de Matsushima + Ryokan frente al mar + cena de Sendai Gyutan y Sendai Wagyu A5",
                "pref_jpy": 112000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 56,
                "home": "Noche de cine clásico y filetes al ajo: preparar Garlic Rice en la plancha de hierro igual que en los restaurantes Teppanyaki de Ginza",
                "home_jpy": 5100,
                "out": "Paseo nocturno frente al mar en el Parque Marino de Odaiba viendo el Rainbow Bridge iluminado",
                "out_jpy": 6200,
                "geek": "Visitar Animate Ikebukuro (el edificio de anime más grande del mundo renovado) y su terraza café",
                "geek_jpy": 9500,
                "pref": "🗼 [Día Completo · Prefectura de Chiba · Cabo Inubosaki (Choshi)] Viaje en el pintoresco tren Choshi Electric Railway hasta el faro blanco en el punto más oriental de Kanto",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            }
        ]
    },
    # ==================== OTOÑO 2028 ====================
    {
        "id": "2028-09",
        "title": "Septiembre 2028 — 🍁 Otoño 1: Luna de Cosecha (Tsukimi), Lirios Rojos y Primer Otoño Juntos en Tokio",
        "season": "otono",
        "season_label": "🍁 Otoño (秋)",
        "phase_note": "Septiembre 2028 · ¡Su primer otoño completo juntos en Japón!",
        "weeks": [
            {
                "w": 57,
                "home": "Noche de Tsukimi (Contemplación de la Luna Llena de Otoño): hacer Tsukimi Dango con forma de conejitos + Hamburg Steak con huevo ('luna llena')",
                "home_jpy": 4900,
                "out": "Festival de la Luna (Tsukimi) en los Jardines Mukojima-Hyakkaen (en Sumida-ku, cerca de casa): escuchar los grillos de otoño entre linternas de papel",
                "out_jpy": 5200,
                "geek": "Ir a Tokyo Game Show (TGS 2028 VIP/Public Day en Makuhari Messe) para probar los nuevos juegos de Square Enix y Bandai Namco",
                "geek_jpy": 12000,
                "pref": "🌺 [Día Completo · Prefectura de Saitama · Kinchakuda (Hidaka)] Caminar entre 5 millones de Lirios Araña Rojos (Higanbana) que cubren el bosque como una alfombra carmesí",
                "pref_jpy": 19500,
                "days": "1 Día Completo"
            },
            {
                "w": 58,
                "home": "Cena de otoño con filete Tenderloin y hongos Matsutake/Eringi salteados en mantequilla y salsa de soya",
                "home_jpy": 6800,
                "out": "Paseo por las galerías de arte y cafés tranquilos de Kiyosumi-Shirakawa + Jardín Kiyosumi (cruzando las piedras 'Iso-watari' sobre el agua)",
                "out_jpy": 5800,
                "geek": "Maratón de anime de otoño: elegir 3 estrenos de la temporada y ver los primeros episodios acurrucados con los gatos",
                "geek_jpy": 3000,
                "pref": "⛩️ [Día Completo · Prefectura de Kanagawa · Kamakura Hasedera y Engakuji] Pasear por los templos zen de Kamakura con la brisa fresca de septiembre",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 59,
                "home": "Taller de encuadernación japonesa (Watoji) en casa: coser juntos a mano dos cuadernos con cubiertas de tela de kimono de Nippori",
                "home_jpy": 5400,
                "out": "Recorrido en bicicleta eléctrica por las calles arboladas de Marunouchi, Hibiya Park y el Palacio Imperial",
                "out_jpy": 5000,
                "geek": "Visitar el Museo de la Ciencia y la Innovación (Miraikan en Odaiba) y ver las exhibiciones de robótica e IA",
                "geek_jpy": 6200,
                "pref": "❤️ [2 Días / 1 Noche · Prefectura de Ibaraki · Kochia Roja en Hitachi Seaside Park] Ver las 32,000 plantas de Kochia teñidas de rojo carmesí frente al océano + Ryokan costero con cena Hitachi Wagyu",
                "pref_jpy": 62000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 60,
                "home": "Noche de cata de castañas japonesas (Kuri) y camote asado (Yaki-imo) como postre después de un filete Striploin de 350g",
                "home_jpy": 5200,
                "out": "Asistir a una función vespertina corta (1 acto con audioguía) en el Teatro Kabukiza de Ginza para admirar el vestuario tradicional japonés",
                "out_jpy": 9500,
                "geek": "Tarde de compras en Ikebukuro Otome Road / K-Books para que あやめ compre todo el merch de sus personajes favoritos",
                "geek_jpy": 11000,
                "pref": "🍇 [2 Días / 1 Noche · Prefectura de Yamanashi · Katsunuma & Kofu Onsen] Recolectar uvas gigantes Shine Muscat directamente del viñedo + Ryokan con vista al Fuji y filete Koshu",
                "pref_jpy": 59000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2028-10",
        "title": "Octubre 2028 — 🍁 Otoño 2: Cosmos en Flor, Halloween Cosplay y Colores de Montaña",
        "season": "otono",
        "season_label": "🍁 Otoño (秋)",
        "phase_note": "Octubre 2028 · El mejor clima del año en Japón (18–20°C y cielos despejados)",
        "weeks": [
            {
                "w": 61,
                "home": "Cena de filete Ribeye con puré de calabaza japonesa (Kabocha) y canela + decorar la sala con pequeñas calabazas reales de otoño",
                "home_jpy": 4800,
                "out": "Festival de las Flores Cosmos en el Parque Showa Kinen (Tachikawa): caminar entre millones de flores cosmos rosas y blancas",
                "out_jpy": 5500,
                "geek": "Preparar juntos su Cosplay de pareja para fin de mes: Denji y Reze (Chainsaw Man) o Sensei y Wakamo (Blue Archive) en el taller de あやめ",
                "geek_jpy": 14000,
                "pref": "🍁 [2 Días / 1 Noche · Prefectura de Tochigi · Oku-Nikko (Ryuzu Falls y Chuzenji)] Primeras hojas rojas de otoño (Koyo) en las cascadas altas de Nikko + noche en Ryokan junto al lago",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 62,
                "home": "Noche de hornear galletas con formas de sus 2 gatitos y las 2 chinchillas después de cenar Roast Beef",
                "home_jpy": 4500,
                "out": "Feria del Libro Antiguo de Kanda Jimbocho (a 6 min de casa): buscar grabados Ukiyo-e y libros de arte textil para あやめ",
                "out_jpy": 8500,
                "geek": "Jugar Luigi's Mansion o juegos de misterio/aventura ligeros en la Switch 2",
                "geek_jpy": 5800,
                "pref": "🍂 [2 Días / 1 Noche · Prefectura de Nagano · Estanque Kumoba (Karuizawa)] Ver los arces rojos reflejados como un espejo en el 'Lago de los Cisnes' de Karuizawa + Hotel en el bosque",
                "pref_jpy": 69000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 63,
                "home": "Cena de Gyukatsu casero (filete de res empanizado en panko ultra crujiente por fuera y término medio rojo por dentro, terminado en piedra caliente)",
                "home_jpy": 5600,
                "out": "Festival de los Crisantemos (Kiku Matsuri) en el Santuario Yushima Tenjin y Templo Senso-ji",
                "out_jpy": 4800,
                "geek": "Visitar el evento de Halloween de Ikebukuro (Ikebukuro Halloween Cosplay Fest, seguro, ordenado y artístico) de día",
                "geek_jpy": 7500,
                "pref": "🏯 [3 Días / 2 Noches · Prefectura de Ishikawa · Kanazawa en Shinkansen Kagayaki (2h 30m directo desde Ueno)] Jardín Kenrokuen en otoño, barrio de geishas Higashi Chaya, helado con hoja de oro real y cena de carne Noto Wagyu A5 + Pet-sitter 48h",
                "pref_jpy": 128000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 64,
                "home": "🎃 Noche de Halloween en Casa (31 de octubre): ponerse sus trajes de Denji & Reze / Wakamo en casa, sesión de fotos divertida con los gatos y cena de filetes",
                "home_jpy": 5800,
                "out": "Tokyo DisneySea en otoño (regresando a las 20:30 en tren directo para respetar su descanso): pasear por Fantasy Springs y Mediterranean Harbor",
                "out_jpy": 28000,
                "geek": "En DisneySea / casa: celebrar el vínculo con Kingdom Hearts buscando los emblemas ocultos y jugando el mundo de Hércules/Arendelle",
                "geek_jpy": 6500,
                "pref": "🌊 [Día Completo · Prefectura de Ibaraki · Puente Colgante de Ryujin y Cascadas Fukuroda] Una de las 3 grandes cascadas de Japón rodeada de arces otoñales",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2028-11",
        "title": "Noviembre 2028 — 🍁 Otoño 3: Ginkgos Dorados, Momiji Nocturno y Tori-no-Ichi",
        "season": "otono",
        "season_label": "🍁 Otoño (秋)",
        "phase_note": "Noviembre 2028 · Tokio y el Monte Fuji se pintan de oro y rojo carmesí (Momijigari)",
        "weeks": [
            {
                "w": 65,
                "home": "Cena de olla caliente Sukiyaki de otoño con hongos Maitake y doble filete de res + té Hojicha tostado",
                "home_jpy": 5600,
                "out": "Avenida de los Ginkgos de Meiji Jingu Gaien (Icho Namiki): caminar sobre la alfombra dorada de hojas amarillas de ginkgo tomando cacao caliente",
                "out_jpy": 5200,
                "geek": "Visitar el Museo de la Animación de Toei o exposición de arte original de Square Enix / Type-Moon",
                "geek_jpy": 7500,
                "pref": "🍁 [2 Días / 1 Noche · Prefectura de Yamanashi · Corredor de Arces de Kawaguchiko (Momiji Kairou)] Túnel de arces rojos iluminados de noche con el Monte Fuji nevado atrás + Ryokan con onsen privado",
                "pref_jpy": 72000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 66,
                "home": "Taller de bordado japonés Sashiko en casa: bordar motivos tradicionales en tela índigo mientras escuchan jazz japonés de fondo",
                "home_jpy": 4900,
                "out": "Iluminación Nocturna de Otoño en el Jardín Rikugien: ver los arces rojos reflejados en el gran estanque central al anochecer",
                "out_jpy": 5800,
                "geek": "Tarde en Akihabara buscando bandas sonoras en vinilo/CD de Final Fantasy y Kingdom Hearts en Tower Records",
                "geek_jpy": 8800,
                "pref": "🍂 [Día Completo · Prefectura de Saitama · Nagatoro Momiji Light-up] Paseo bajo arces rojos iluminados junto al río en Nagatoro",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            },
            {
                "w": 67,
                "home": "Cena del 'Día de la Buena Pareja' en Japón (11月22日 — いい夫婦の日 / Ii Fufu no Hi): regalarle un ramo de rosas + filete Tenderloin 300g hecho por ti",
                "home_jpy": 9500,
                "out": "Feria Tori-no-Ichi en el Santuario Otori de Asakusa (Taito-ku): comprar juntos un rastrillo de bambú de la fortuna (Kumade) para atraer prosperidad al hogar",
                "out_jpy": 8500,
                "geek": "Noche de maratón de su saga favorita de videojuegos: rejugar las mejores escenas de Kingdom Hearts I, II y III",
                "geek_jpy": 2500,
                "pref": "⛰️ [Día Completo · Prefectura de Kanagawa · Montaña Oyama (Isehara)] Subir en funicular al Santuario Oyama Afuri para ver las hojas rojas de otoño y toda la costa de Shonan",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 68,
                "home": "Noche de estofado de res japonés (Beef Stew estilo Yoshoku cocinado a fuego lento por 3 horas con trozos gigantes de carne tierna)",
                "home_jpy": 5400,
                "out": "Paseo por el campus histórico de la Universidad de Tokio (Hongo, en Bunkyo-ku) bajo el gran Ginkgo centenario y el estanque Sanshiro",
                "out_jpy": 4500,
                "geek": "Crear juntos en PC stickers personalizados de LINE con dibujos de sus 2 gatitos, las 2 chinchillas y ustedes dos para su chat diario",
                "geek_jpy": 3000,
                "pref": "🦌 [3 Días / 2 Noches · Prefectura de Nara & Osaka en Shinkansen] Dar de comer galletas senbei a los ciervos sagrados del Parque de Nara bajo los arces rojos + Templo Todai-ji + noche en Osaka/Nara probando carne Kobe/Matsusaka + Pet-sitter 48h",
                "pref_jpy": 132000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    # ==================== INVIERNO 2028-2029 ====================
    {
        "id": "2028-12",
        "title": "Diciembre 2028 — ❄️ Invierno 4: Segunda Navidad Juntos, Onsen y Luces de Tokio",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Diciembre 2028 · Su primera Navidad ya casados oficialmente",
        "weeks": [
            {
                "w": 69,
                "home": "Noche de Yuzu-yu (baño caliente con cítricos Yuzu reales flotando en la tina para el solsticio de invierno Toji) + cena de filete Ribeye",
                "home_jpy": 5200,
                "out": "Iluminación de invierno de Omotesando bajo los árboles zelkova y paseo por Aoyama",
                "out_jpy": 6500,
                "geek": "Visitar la exposición de invierno de Akihabara UDX y comprar figuras navideñas para su estantería",
                "geek_jpy": 9500,
                "pref": "✨ [2 Días / 1 Noche · Prefectura de Shizuoka · Gotemba Tokinosumika & Vista al Fuji] Túnel de luces de invierno gigantes + hotel con aguas termales mirando al Monte Fuji",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 70,
                "home": "Taller de coronas navideñas estilo japonés (Shimenawa moderno con flores secas y listones de Asakusabashi) + cena de carne asada",
                "home_jpy": 5800,
                "out": "Mercado de Navidad de Tokyo Skytree Town viendo la iluminación navideña desde abajo",
                "out_jpy": 7200,
                "geek": "Noche de juego cooperativo de invierno (Overcooked! All You Can Eat / Pikmin 4) en la Switch 2 riéndose sin parar",
                "geek_jpy": 3500,
                "pref": "🏛️ [Día Completo · Prefectura de Tochigi · Ashikaga Flower Park 'Flower Fantasy' Navideño] Galardonada como la iluminación #1 de Japón",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            },
            {
                "w": 71,
                "home": "🎄 Cena de Segunda Navidad en Casa: Filete Wellington / Roast Beef de Tenderloin hecho por ti + pastel de fresas Amaou de Fukuoka",
                "home_jpy": 9800,
                "out": "Concierto de cuerdas a la luz de las velas (Candlelight Concert de música de Joe Hisaishi / Studio Ghibli) en Tokio",
                "out_jpy": 15000,
                "geek": "Intercambio de regalos frikis de Navidad: edición coleccionista de su juego/artbook más deseado envuelto con tela Furoshiki hecha por ella",
                "geek_jpy": 16000,
                "pref": "💎 [2 Días / 1 Noche · Prefectura de Kanagawa · Hakone Venetian Glass Museum & Ashinoko] Árboles de cristal de Murano brillando al sol de invierno + Ryokan navideño en Hakone",
                "pref_jpy": 72000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 72,
                "home": "Nochevieja 2028 en casa: cena de filetes de Wagyu + Toshikoshi Soba y agradecer juntos por el año de su boda y tu 5–0",
                "home_jpy": 7500,
                "out": "Visita tranquila de fin de año al Santuario Meiji y paseo por Harajuku",
                "out_jpy": 5500,
                "geek": "Ver el resumen anual de sus horas jugadas en PlayStation Wrap-Up y Nintendo Switch Year in Review abrazados con los gatos",
                "geek_jpy": 2500,
                "pref": "🏮 [3 Días / 2 Noches · Prefectura de Gunma · Shima Onsen (Sekizenkan)] El pueblo termal histórico que inspiró 'El Viaje de Chihiro' con su puente rojo bajo la nieve + baño privado y carne Joshu Wagyu",
                "pref_jpy": 96000,
                "days": "3 Días / 2 Noches"
            }
        ]
    },
    {
        "id": "2029-01",
        "title": "Enero 2029 — ❄️ Invierno 5: Paisajes Nevados, Siete Dioses de la Fortuna y Calor de Hogar",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Enero 2029 · Invierno acogedor y planeación del patrimonio familiar en Kanagawa",
        "weeks": [
            {
                "w": 73,
                "home": "Cena de Año Nuevo 2029: filetes de Ribeye a la plancha + pastelillos de arroz Mochi rellenos de fresa (Ichigo Daifuku) hechos en casa",
                "home_jpy": 5800,
                "out": "Ruta de los Siete Dioses de la Fortuna de Yanaka o Nihombashi (Shichifukujin Meguri): paseo suave coleccionando los sellos Goshuin en el libro de あやめ",
                "out_jpy": 5200,
                "geek": "Tarde en Akihabara estrenando su presupuesto de Año Nuevo en materiales de costura pro y periféricos blancos para su setup",
                "geek_jpy": 14000,
                "pref": "🕯️ [2 Días / 1 Noche · Prefectura de Tochigi · Yunishigawa Onsen (Kamakura Snow Festival)] Ver cientos de pequeños iglús de nieve iluminados con velas por la noche junto al río nevado + noche en Ryokan",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 74,
                "home": "Noche de Chanko Nabe hiper-proteico (la olla de los luchadores de sumo de nuestro barrio vecino Ryogoku, hecha con carne de res, pollo y verduras)",
                "home_jpy": 5400,
                "out": "Asistir una tarde al Torneo de Sumo de Enero (Hatsu Basho) en el Ryogoku Kokugikan (a 1 estación de Asakusabashi) desde asientos cómodos",
                "out_jpy": 19000,
                "geek": "Jugar Street Fighter 6 / Tekken 8 en modo divertido (con controles modernos para que あやめ te gane y celebre)",
                "geek_jpy": 3000,
                "pref": "🗻 [Día Completo · Prefectura de Yamanashi · Lago Saiko Iyashi no Sato Nenba] Aldea tradicional de techos de paja frente al Monte Fuji nevado donde se visten de samurái y kimono",
                "pref_jpy": 26000,
                "days": "1 Día Completo"
            },
            {
                "w": 75,
                "home": "Taller de velas aromáticas de cera de soya en casa: hacer velas con aroma a lavanda y vainilla para el ritual de las 22:00 hrs",
                "home_jpy": 4900,
                "out": "Jardín de Peonías de Invierno (Fuyu Botan) cubiertas con sombreritos de paja para la nieve en el Santuario Ueno Toshogu",
                "out_jpy": 4800,
                "geek": "Visitar el Café Pokémon (Nihombashi Takashimaya, a 5 min en tren por la línea Asakusa desde casa)",
                "geek_jpy": 9500,
                "pref": "🐒 [3 Días / 2 Noches · Prefectura de Nagano · Parque de los Monos de Nieve de Jigokudani & Shibu Onsen] Shinkansen a Nagano + 2 noches en el pueblo empedrado de Shibu Onsen (los 9 baños de la suerte) + ver a los macacos bañándose en aguas termales en la nieve",
                "pref_jpy": 104000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 76,
                "home": "Noche de filetes al estilo Steak Au Poivre y papas gratinadas hechas al horno",
                "home_jpy": 5200,
                "out": "Museo de Artesanía Tradicional de Edo Taito (en Asakusa) y merienda de Taiyaki recién horneado",
                "out_jpy": 4800,
                "geek": "Noche de diseño del cuarto de costura y gaming que tendrá あやめ en la futura casa 二世帯住宅 de Kanagawa usando software 3D",
                "geek_jpy": 2500,
                "pref": "🍓 [Día Completo · Prefectura de Chiba · Recolección de Fresas (Ichigo-gari) en Boso] Invernaderos tibios en Chiba para comer fresas recién cortadas ilimitadas en enero",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2029-02",
        "title": "Febrero 2029 — ❄️ Invierno 6: Ciruelos en Flor, Kobe/Arima Onsen y 1 Año de tu Debut",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Febrero 2029 · Primer aniversario de tu Debut en MMA en Japón",
        "weeks": [
            {
                "w": 77,
                "home": "Cena de aniversario de tu Debut en MMA: recrear tu banquete post-pelea (Filete Tenderloin 300g + Wagyu Burger) viendo las fotos de aquel día",
                "home_jpy": 6800,
                "out": "Festival del Ciruelo de Hanegi Park (Setagaya): caminar entre 650 ciruelos rojos y blancos en flor con aroma dulce de invierno",
                "out_jpy": 4800,
                "geek": "Tarde en Ikebukuro visitando el Planetario 'Manten' en Sunshine City acostados en los asientos 'Nube (Kumo Seat)' blancos y esponjosos",
                "geek_jpy": 8400,
                "pref": "🌸 [2 Días / 1 Noche · Prefectura de Shizuoka · Atami Baien (Jardín de Ciruelos de Atami)] El jardín de ciruelos más temprano de Japón junto con aguas termales frente al mar",
                "pref_jpy": 58000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 78,
                "home": "Cena de San Valentín 2029 en casa: Fondue de chocolate oscuro con fresas, plátano y malvaviscos después de cenar filete Sirloin",
                "home_jpy": 7200,
                "out": "Paseo romántico por Yebisu Garden Place iluminado y mirador con vista a la Torre de Tokio",
                "out_jpy": 6500,
                "geek": "Jugar juntos el nuevo lanzamiento de Square Enix / Kingdom Hearts / Final Fantasy en la PS5 Pro",
                "geek_jpy": 9800,
                "pref": "🥩 [3 Días / 2 Noches · Prefectura de Hyogo · Kobe & Arima Onsen (El Onsen Imperial más antiguo de Japón)] Shinkansen a Shin-Kobe + 2 noches en Arima Onsen (aguas Kinsen doradas y Ginsen plateadas) + Cena oficial de Filete KOBE BEEF A5 certificado frente al puerto de Kobe",
                "pref_jpy": 138000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 79,
                "home": "Taller de marroquinería básica en casa: hacer dos porta-tarjetas Suica de cuero genuino comprado en las tiendas de piel de Asakusabashi",
                "home_jpy": 6500,
                "out": "Visita al Parque Kasai Rinkai (con la segunda rueda de la fortuna más grande de Japón frente a la bahía de Tokio)",
                "out_jpy": 5200,
                "geek": "Ir a Akihabara Gachapon Hall (500 máquinas de cápsulas) con ¥5,000 en monedas de ¥100 para sacar miniaturas para su escritorio",
                "geek_jpy": 6000,
                "pref": "⛩️ [Día Completo · Prefectura de Saitama · Santuario Mitsumine (Chichibu)] Santuario místico en la cima de la montaña entre cedros gigantes centenarios",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 80,
                "home": "Noche de Teppanyaki de mar y tierra (Surf & Turf): Filete Tenderloin 250g + vieiras gigantes de Hokkaido (Hotate) a la mantequilla",
                "home_jpy": 6800,
                "out": "Paseo por el barrio retro de Shibamata (Katsushika-ku): calle tradicional Taishakuten Sando y cruzar el río Edo en la barca tradicional Yagiri-no-Watashi",
                "out_jpy": 5500,
                "geek": "Noche de karaoke privado para dos (Pasela en Akihabara) cantando openings de anime, Utada Hikaru (Kingdom Hearts) y canciones de Blue Archive",
                "geek_jpy": 7800,
                "pref": "⛰️ [Día Completo · Prefectura de Ibaraki · Monte Tsukuba en Teleférico] Subir al pico doble del Monte Tsukuba viendo toda la llanura de Kanto",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            }
        ]
    },
    # ==================== PRIMAVERA 2029 ====================
    {
        "id": "2029-03",
        "title": "Marzo 2029 — 🌸 Primavera 6: Tercer Año de Cerezos, Takayama y Arquitectos en Kanagawa",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Marzo 2029 · Primavera radiante y avances concretos para la casa 二世帯住宅",
        "weeks": [
            {
                "w": 81,
                "home": "Cena de Hinamatsuri 2029: filete de res cortado en dados sobre arroz de sushi decorado con huevo en tiras",
                "home_jpy": 5400,
                "out": "Paseo de cerezos tempranos (Kanzakura) en el Parque Ueno y visita al Museo Nacional de Tokio",
                "out_jpy": 5200,
                "geek": "Tarde de pintura de miniaturas / figuras en el taller de casa con pinceles finos",
                "geek_jpy": 5800,
                "pref": "🏡 [Día Completo · Prefectura de Kanagawa · Showrooms de Casas 二世帯住宅 (TVK Housing Plaza Yokohama)] Ver casas modelo reales de dos generaciones para el retiro de 千秋-san + cena en Yokohama",
                "pref_jpy": 25000,
                "days": "1 Día Completo"
            },
            {
                "w": 82,
                "home": "Cena de White Day 2029: regalarle un conjunto de sedas de Kioto para su colección + filete Chateaubriand hecho en casa",
                "home_jpy": 16500,
                "out": "Caminata bajo los cerezos llorones (Shidarezakura) iluminados del Jardín Rikugien",
                "out_jpy": 4800,
                "geek": "Ir a AnimeJapan 2029 en Tokyo Big Sight para ver los stands oficiales de Blue Archive, Fate y Chainsaw Man",
                "geek_jpy": 9500,
                "pref": "🏯 [3 Días / 2 Noches · Prefectura de Gifu · Takayama & Aldea Histórica de Shirakawa-go] Shinkansen + Expreso Hida: calles Edo de Sanmachi Suji, casas de techo de paja Gassho-zukuri y cena de Filete HIDA WAGYU A5 a la parrilla",
                "pref_jpy": 124000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 83,
                "home": "Noche de picnic interior con vista al balcón: brochetas de filete, fresas y té de flor de cerezo (Sakura-cha)",
                "home_jpy": 4800,
                "out": "Recorrido en barco abierto por el río Kanda y el río Nihombashi pasando bajo los puentes históricos cubiertos de cerezos",
                "out_jpy": 7800,
                "geek": "Maratón de películas de anime de primavera ('La Chica que Saltaba a Través del Tiempo')",
                "geek_jpy": 3000,
                "pref": "🌸 [Día Completo · Prefectura de Saitama · Gongendo Tsutsumi (Satte)] El dique de 1 km con 1,000 cerezos rosas arriba y una alfombra amarilla infinita de flores de colza abajo",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 84,
                "home": "Cena de filete Ribeye con mantequilla compuesta de hierbas hecha en casa + sesión de cepillado y mimos a los gatos y chinchillas",
                "home_jpy": 4900,
                "out": "Paseo de Hanami por Yanaka y las cafeterías en casas antiguas de madera de Ueno Sakuragi Atari",
                "out_jpy": 5500,
                "geek": "Sesión cooperativa de construir su isla/casa perfecta en Animal Crossing / Dragon Quest Builders en Switch 2",
                "geek_jpy": 3000,
                "pref": "🏯 [2 Días / 1 Noche · Prefectura de Yamanashi · Castillo de Kofu & Isawa Onsen] Cerezos rodeando las murallas del castillo con los Alpes del Sur nevados al fondo + noche en Ryokan termal",
                "pref_jpy": 59000,
                "days": "2 Días / 1 Noche"
            }
        ]
    },
    {
        "id": "2029-04",
        "title": "Abril 2029 — 🌸 Primavera 7: Pétalos sobre el Agua, Tulipanes y Brisa de Abril",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Abril 2029 · Mes 22 activo de citas únicas",
        "weeks": [
            {
                "w": 85,
                "home": "Noche de Tataki de filete de res con ajo crujiente hecho en casa + postre de gelatina de cristal japonesa (Mizu Shingen Mochi)",
                "home_jpy": 5200,
                "out": "Ver el fenómeno 'Hanaikada' (balsas de pétalos rosas cubriendo el agua por completo) en el foso de Chidorigafuchi",
                "out_jpy": 4800,
                "geek": "Visitar tiendas de papelería de personajes y estudios de animación en Mitaka-Kichijoji",
                "geek_jpy": 6500,
                "pref": "🌷 [Día Completo · Prefectura de Chiba · Sakura Furusato Square] Ver el molino de viento holandés real rodeado de 700,000 tulipanes de todos los colores en Sakura, Chiba",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            },
            {
                "w": 86,
                "home": "Taller de confección de cojines y camitas nuevas para los 2 gatitos usando telas acolchadas en la máquina JUKI de あやめ",
                "home_jpy": 5800,
                "out": "Festival de las Azaleas (Tsutsuji Matsuri) en el Santuario Nezu y almuerzo de carne en Yanesen",
                "out_jpy": 5500,
                "geek": "Tarde de realidad virtual / arcade inmersivo en RED° TOKYO TOWER (dentro de la Torre de Tokio)",
                "geek_jpy": 9600,
                "pref": "🎎 [Día Completo · Prefectura de Gunma · Templo Daruma de Shorinzan (Takasaki)] Pintar juntos los ojos de un Daruma tradicional pidiendo un deseo familiar",
                "pref_jpy": 23000,
                "days": "1 Día Completo"
            },
            {
                "w": 87,
                "home": "Cena de filetes Striploin al estilo chimichurri fresco hecho en casa + noche de masajes con aceite tibio",
                "home_jpy": 5100,
                "out": "Paseo por los Jardines Hama-rikyu viendo los campos de flores de primavera frente a los rascacielos",
                "out_jpy": 4800,
                "geek": "Competencia amistosa de Mario Party / Overcooked con premios de vales hechos a mano ('Vale por 1 tarde entera en Nippori')",
                "geek_jpy": 3000,
                "pref": "🏺 [2 Días / 1 Noche · Prefectura de Tochigi · Feria de Cerámica de Mashiko & Utsunomiya] Recorrer las galerías de alfarería tradicional de Mashiko para elegir platos artesanales para sus filetes + hotel boutique",
                "pref_jpy": 56000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 88,
                "home": "Noche de degustación de tés japoneses sin teína (Mugicha, Sobacha, Kuromamecha) + cena de Roast Beef",
                "home_jpy": 4800,
                "out": "Visitar el Jardín de Glicinas de Kameido Tenjin al atardecer viendo el Tokyo Skytree enmarcado entre las flores moradas",
                "out_jpy": 5200,
                "geek": "Actualización estética de ambos setups (fondos de pantalla animados en Wallpaper Engine de Blue Archive y Kingdom Hearts)",
                "geek_jpy": 3500,
                "pref": "🌺 [Día Completo · Prefectura de Kanagawa · Kurihama Hana no Kuni (Yokosuka)] Caminar entre un millón de amapolas y flores de primavera frente al mar en Yokosuka",
                "pref_jpy": 21000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2029-05",
        "title": "Mayo 2029 — 🌸 Primavera 8: Primer Aniversario de Bodas y Escapada a Okinawa",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mayo 2029 · ¡1er Aniversario de Bodas (Bodas de Papel) con escapada de 3 días!",
        "weeks": [
            {
                "w": 89,
                "home": "💍 ¡Cena de 1er Aniversario de Bodas (Bodas de Papel)! Entregarle una carta de amor escrita en papel japonés Washi artesanal + Chateaubriand Wagyu en casa",
                "home_jpy": 12500,
                "out": "Paseo de aniversario por los Jardines del Hotel New Otani Tokyo (jardín japonés de 400 años con cascada y puente rojo) y cena de cortes premium sin alcohol",
                "out_jpy": 24000,
                "geek": "Sesión de fotos conmemorativa del 1er aniversario recreando la primera foto que se tomaron juntos en Asakusabashi",
                "geek_jpy": 4500,
                "pref": "🏝️ [3 Días / 2 Noches · Prefectura de Okinawa · Viaje de 1er Aniversario de Bodas a Okinawa (Ishigaki / Onna-son)] Resort frente al mar color turquesa + Acuario Churaumi (tiburón ballena) + Cena de filete Ishigaki Beef / Motobu Wagyu (sin mango 🚫🥭) + Pet-sitter 48h",
                "pref_jpy": 145000,
                "days": "3 Días / 2 Noches"
            },
            {
                "w": 90,
                "home": "Taller de prensado de flores naturales (Oshibana): prensar las flores de su ramo de aniversario para enmarcarlas en cristal",
                "home_jpy": 5200,
                "out": "Festival de las Rosas en el Jardín Botánico Jindai (Chofu) y paseo por las calles antiguas del Templo Jindaiji",
                "out_jpy": 5800,
                "geek": "Visitar las tiendas de figuras y coleccionables de Akihabara para elegir la figura de aniversario del año",
                "geek_jpy": 15000,
                "pref": "🗻 [Día Completo · Prefectura de Yamanashi · Fuji Shibazakura Festival (Lago Motosu)] Ver los 500,000 musgos rosas en flor a los pies del Monte Fuji",
                "pref_jpy": 24000,
                "days": "1 Día Completo"
            },
            {
                "w": 91,
                "home": "Cena de Hamburguesas Wagyu rellenas de queso gouda hechas por ti + tarde de sol en el balcón con los gatitos",
                "home_jpy": 4800,
                "out": "Paseo en kayak doble tranquilo por los canales de Tokio pasando bajo el Tokyo Skytree al atardecer",
                "out_jpy": 11000,
                "geek": "Noche de música y nostalgia: escuchar todos los temas de Dearly Beloved (Kingdom Hearts) desde KH1 hasta KH3 mientras platican de sus sueños",
                "geek_jpy": 2500,
                "pref": "🌹 [Día Completo · Prefectura de Saitama · Jardín de Rosas de Ina y Pueblo Bonsai de Omiya] Caminar entre arcos de rosas de mayo",
                "pref_jpy": 20000,
                "days": "1 Día Completo"
            },
            {
                "w": 92,
                "home": "Noche de brochetas de filete Tenderloin y pimientos asados + sesión de spa de manos para あやめ (después de sus tardes de costura)",
                "home_jpy": 5100,
                "out": "Visita al Museo de Arte Teien de Tokio (antigua residencia Art Déco en Meguro) y sus jardines verdes",
                "out_jpy": 5500,
                "geek": "Tarde de armado de un diorama japonés en miniatura (Book Nook de callejón de Tokio con luz LED) para poner entre sus mangas",
                "geek_jpy": 6800,
                "pref": "🏰 [Día Completo · Prefectura de Kanagawa · Isla de Sarushima (Yokosuka)] Barco de 10 minutos a la isla deshabitada cubierta de bosque y ladrillos cubiertos de musgo estilo Laputa (El Castillo en el Cielo)",
                "pref_jpy": 22000,
                "days": "1 Día Completo"
            }
        ]
    },
    {
        "id": "2029-06",
        "title": "Junio 2029 — 🎆 Verano 7: Cierre de los 2 Años Completos (Semana 96 · 384 Citas Únicas)",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Junio 2029 · Completan 24 meses activos en Japón (96 semanas = 384 citas únicas sin repetir jamás)",
        "weeks": [
            {
                "w": 93,
                "home": "Cena de filetes Ribeye con mantequilla de trufa y sal marina + noche de lluvia acogedora viendo anime desde la cama",
                "home_jpy": 5600,
                "out": "Camino de las Hortensias de Asukayama Park (subiendo en el pequeño monorriel gratuito Asukayama Park Monorail en Kita-ku)",
                "out_jpy": 4500,
                "geek": "Tarde en Nakano / Akihabara buscando ediciones retro de Kingdom Hearts para Game Boy Advance / PSP para su colección histórica",
                "geek_jpy": 12000,
                "pref": "⛩️ [Día Completo · Prefectura de Chiba · Templo Hondoji (Matsudo)] El 'Templo de las Hortensias' de Chiba con su pagoda de 5 pisos entre 50,000 hortensias",
                "pref_jpy": 19500,
                "days": "1 Día Completo"
            },
            {
                "w": 94,
                "home": "Taller de creación de sellos japoneses (Hanko / Gomu-in) grabados en goma con las caritas de sus gatitos y chinchillas",
                "home_jpy": 4800,
                "out": "Visita al Museo de la Espada Japonesa (en Ryogoku, a 1 estación de casa) y los jardines Kyu-Yasuda",
                "out_jpy": 5200,
                "geek": "Noche de torneo cooperativo en PS5 Pro y Switch 2 celebrando todos los juegos completados juntos en estos 2 años",
                "geek_jpy": 3000,
                "pref": "🛶 [2 Días / 1 Noche · Prefectura de Tochigi · Ohirasan Shrine & Kura no Machi] Subir el sendero de las 4,000 hortensias + paseo en barca por el río Uzuma + Ryokan tradicional",
                "pref_jpy": 54000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 95,
                "home": "Cena de filete Sirloin en costra de ajo tostado + preparar juntos parfaits caseros de arándanos, fresas y crema batida",
                "home_jpy": 5200,
                "out": "Crucero nocturno por la bahía de Tokio viendo el Rainbow Bridge iluminado y la brisa cálida de junio",
                "out_jpy": 9500,
                "geek": "Exposición de vestuario y diseño textil del Japón moderno / anime en Tokio para inspirar los nuevos diseños de あやめ",
                "geek_jpy": 6800,
                "pref": "💎 [2 Días / 1 Noche · Prefectura de Kanagawa · Hakone Glass Forest & Lago Ashi] Ryokan con Rotenburo privado en Hakone + paseo bajo los árboles de cristal",
                "pref_jpy": 68000,
                "days": "2 Días / 1 Noche"
            },
            {
                "w": 96,
                "home": "👑 ¡CITA #384 (FINAL DEL CALENDARIO DE 2 AÑOS)! Banquete Real en casa: Chateaubriand 350g, brindis sin alcohol y abrir el álbum con los recuerdos de las 96 semanas",
                "home_jpy": 12000,
                "out": "Paseo al atardecer desde nuestra puerta en Yanagibashi por toda la ribera del río Sumida hasta Asakusa recordando cómo empezó el Imperio",
                "out_jpy": 6500,
                "geek": "Ceremonia de graduación gamer/otaku en casa: encender las luces de la vitrina con tus trofeos 5–0 de MMA y los kimonos diseñados por あやめ",
                "geek_jpy": 4500,
                "pref": "🏡 [3 Días / 2 Noches · Prefectura de Kanagawa · Celebración Familiar en Kamakura/Enoshima con 千秋-san] Celebrar los 2 años de felicidad y revisar el proyecto del futuro hogar 二世帯住宅 para las dos generaciones",
                "pref_jpy": 95000,
                "days": "3 Días / 2 Noches"
            }
        ]
    }
]


def main():
    active_weeks = [w for m in MONTHS_DATA if m["season"] != "campamento" for w in m["weeks"]]
    assert len(active_weeks) == 96, f"Expected 96 active weeks, got {len(active_weeks)}"

    total_2yr_jpy = 0
    multi_day_count = 0
    for m in MONTHS_DATA:
        m_total = 0
        for w in m["weeks"]:
            w["total_jpy"] = w["home_jpy"] + w["out_jpy"] + w["geek_jpy"] + w["pref_jpy"]
            m_total += w["total_jpy"]
            if "Días" in w.get("days", ""):
                multi_day_count += 1
        m["month_total_jpy"] = m_total
        if m["season"] != "campamento":
            total_2yr_jpy += m_total

    js_content = f"""/**
 * Atlas del Imperio — Calendario Maestro de 2 Años de Citas Únicas para あやめ (v2.0 Live API)
 * 24 Meses Activos en Japón (96 Semanas = 384 Citas 100% Únicas) + Pausa de 3 Meses en Tailandia.
 * Conectado en tiempo real a https://open.er-api.com/v6/latest/USD y api.frankfurter.dev (ECB)
 * para rastrear y actualizar en vivo cada costo en JPY y USD.
 */
(function () {{
  const MONTHS_DATA = {json.dumps(MONTHS_DATA, ensure_ascii=False, indent=2)};
  const TOTAL_2YR_JPY = {total_2yr_jpy};
  const MULTI_DAY_TRIPS = {multi_day_count};

  let liveJpyRate = 158.09;
  let apiSource = "ExchangeRate-API (En Vivo)";
  let apiUpdated = new Date().toISOString();

  async function fetchLiveJpyRate() {{
    try {{
      const r = await fetch("https://open.er-api.com/v6/latest/USD", {{ cache: "no-store" }});
      if (r.ok) {{
        const d = await r.json();
        if (d && d.rates && d.rates.JPY) {{
          liveJpyRate = Number(d.rates.JPY);
          apiSource = "open.er-api.com (En Vivo)";
          apiUpdated = d.time_last_update_utc || new Date().toUTCString();
          return;
        }}
      }}
    }} catch (_) {{}}
    try {{
      const r2 = await fetch("https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY", {{ cache: "no-store" }});
      if (r2.ok) {{
        const d2 = await r2.json();
        if (d2 && d2.rates && d2.rates.JPY) {{
          liveJpyRate = Number(d2.rates.JPY);
          apiSource = "Frankfurter ECB (En Vivo)";
          apiUpdated = d2.date || new Date().toISOString().slice(0, 10);
        }}
      }}
    }} catch (_) {{}}
  }}

  function fmtJpy(n) {{
    return "¥" + Math.round(n).toLocaleString("en-US");
  }}

  function fmtUsdFromJpy(jpy) {{
    return "$" + Math.round(jpy / liveJpyRate).toLocaleString("en-US");
  }}

  async function renderAyameCalendar() {{
    const container = document.getElementById("ayame-dates-container");
    if (!container) return;

    await fetchLiveJpyRate();

    const savedChecks = JSON.parse(localStorage.getItem("imperio_ayame_dates_v1") || "{{}}");

    let activeSeason = "all";
    let onlyMultiDay = false;
    let searchQuery = "";

    function updateSummaryBanner() {{
      const summaryEl = document.getElementById("ayame-live-api-summary");
      if (!summaryEl) return;
      const avgMonthJpy = Math.round(TOTAL_2YR_JPY / 24);
      const completedCount = Object.keys(savedChecks).length;
      summaryEl.innerHTML = `
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:10px; margin-bottom:14px;">
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(74,222,128,0.4); border-radius:10px; padding:10px 12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">🛰️ Tasa API En Vivo Hoy</div>
            <div style="font-size:1.05rem; font-weight:800; color:#4ade80;">$1 USD = ¥${{liveJpyRate.toFixed(2)}} JPY</div>
            <div style="font-size:0.7rem; color:#d1d5db;">${{apiSource}}</div>
          </div>
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(244,114,182,0.4); border-radius:10px; padding:10px 12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">💕 Inversión Promedio Mensual (4 Semanas)</div>
            <div style="font-size:1.05rem; font-weight:800; color:#f9a8d4;">${{fmtJpy(avgMonthJpy)}} / mes <span style="color:#4ade80;">(⚡ ${{fmtUsdFromJpy(avgMonthJpy)}} USD)</span></div>
            <div style="font-size:0.7rem; color:#d1d5db;">Cubierto dentro de tu partida OPEX 'Diamante あやめ' (¥200,000/mes)</div>
          </div>
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(251,146,60,0.4); border-radius:10px; padding:10px 12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">🚅 Escapadas de 2–3 Días (Ryokan + Onsen)</div>
            <div style="font-size:1.05rem; font-weight:800; color:#fdba74;">${{MULTI_DAY_TRIPS}} Viajes de 2–3 Días + ${{96 - MULTI_DAY_TRIPS}} Full-Day</div>
            <div style="font-size:0.7rem; color:#d1d5db;">Incluye Kioto, Hokkaido, Okinawa, Kanazawa, Kobe, Takayama, Hakone y Kusatsu</div>
          </div>
          <div style="background:rgba(0,0,0,0.4); border:1px solid rgba(167,139,250,0.4); border-radius:10px; padding:10px 12px;">
            <div style="font-size:0.7rem; color:#9ca3af; text-transform:uppercase;">✅ Progreso de Citas & Total 2 Años</div>
            <div style="font-size:1.05rem; font-weight:800; color:#c4b5fd;">${{completedCount}} / 96 Semanas (${{completedCount * 4}} / 384 Citas)</div>
            <div style="font-size:0.7rem; color:#4ade80;">Total 24 Meses: ${{fmtJpy(TOTAL_2YR_JPY)}} (⚡ ${{fmtUsdFromJpy(TOTAL_2YR_JPY)}} USD hoy)</div>
          </div>
        </div>
      `;
    }}

    function updateView() {{
      updateSummaryBanner();
      const listEl = document.getElementById("ayame-months-list");
      if (!listEl) return;

      const q = searchQuery.trim().toLowerCase();
      let html = "";

      for (const m of MONTHS_DATA) {{
        if (activeSeason !== "all" && m.season !== activeSeason) continue;

        const filteredWeeks = m.weeks.filter((w) => {{
          if (onlyMultiDay && !w.days.includes("Noche")) return false;
          if (!q) return true;
          return (
            m.title.toLowerCase().includes(q) ||
            w.home.toLowerCase().includes(q) ||
            w.out.toLowerCase().includes(q) ||
            w.geek.toLowerCase().includes(q) ||
            w.pref.toLowerCase().includes(q) ||
            w.days.toLowerCase().includes(q)
          );
        }});

        if (filteredWeeks.length === 0) continue;

        const borderColor =
          m.season === "primavera"
            ? "#f472b6"
            : m.season === "verano"
            ? "#38bdf8"
            : m.season === "otono"
            ? "#fb923c"
            : m.season === "invierno"
            ? "#a78bfa"
            : "#ef4444";

        html += `
          <div class="room-card" style="margin-bottom:1.1rem; border-left:4px solid ${{borderColor}};">
            <div class="room-header" onclick="this.nextElementSibling.classList.toggle('open'); this.nextElementSibling.style.maxHeight = this.nextElementSibling.classList.contains('open') ? '4000px' : null;" style="cursor:pointer;">
              <div class="room-title" style="font-size:1rem;">${{m.title}}</div>
              <div class="room-subtotal" style="font-size:0.82rem; color:${{borderColor}};">
                ${{m.season_label}} · ${{fmtJpy(m.month_total_jpy)}} <span style="background:rgba(34,197,94,0.18); color:#4ade80; border:1px solid rgba(74,222,128,0.4); padding:2px 7px; border-radius:5px; margin-left:5px;">⚡ ${{fmtUsdFromJpy(m.month_total_jpy)}} USD</span>
              </div>
            </div>
            <div class="room-content open" style="max-height:4000px; padding:0.9rem 1.1rem;">
              <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:0.8rem;">📌 <strong>Contexto de Fase:</strong> ${{m.phase_note}}</p>
              <div style="overflow-x:auto;">
                <table style="width:100%; border-collapse:collapse; font-size:0.81rem;">
                  <thead>
                    <tr style="background:rgba(255,255,255,0.04);">
                      <th style="width:85px;">Semana &amp; Costo API</th>
                      <th style="width:22%;">🏠 1. Cita en Nuestra Casa<br><small style="color:#9ca3af;">(Mié 19:00–21:15 · Juntos en el 2LDK)</small></th>
                      <th style="width:22%;">🎮 2. Cita Friki Juntos<br><small style="color:#9ca3af;">(Jue 19:00–21:15 · Ikebukuro/Akiba/Casa)</small></th>
                      <th style="width:22%;">🌿 3. Actividad Afuera Tokio<br><small style="color:#9ca3af;">(Vie 17:45–21:00 · Regreso Juntos)</small></th>
                      <th style="width:34%;">🚅 4. Escapada Prefectura (1 a 3 Días)<br><small style="color:#9ca3af;">(Ryokan / Onsen / Wagyu / Pet-Sitter)</small></th>
                    </tr>
                  </thead>
                  <tbody>
        `;

        for (const w of filteredWeeks) {{
          const key = m.id + "-w" + w.w;
          const checked = savedChecks[key] ? "checked" : "";
          const isMulti = w.days.includes("Noche");
          const badgeStyle = isMulti
            ? "background:rgba(251,146,60,0.22); color:#fdba74; border:1px solid #fb923c;"
            : "background:rgba(56,189,248,0.15); color:#7dd3fc; border:1px solid rgba(56,189,248,0.35);";

          html += `
            <tr>
              <td style="font-weight:bold; text-align:center;">
                <label style="cursor:pointer; display:flex; flex-direction:column; align-items:center; gap:4px;">
                  <span>Sem ${{w.w}}</span>
                  <input type="checkbox" data-date-key="${{key}}" ${{checked}} style="accent-color:#f472b6; width:16px; height:16px; cursor:pointer;" title="Marcar semana completada">
                  <span style="font-size:0.72rem; color:#e5e7eb;">${{fmtJpy(w.total_jpy)}}</span>
                  <span style="font-size:0.7rem; color:#4ade80; background:rgba(34,197,94,0.14); padding:1px 5px; border-radius:4px;">⚡ ${{fmtUsdFromJpy(w.total_jpy)}}</span>
                </label>
              </td>
              <td>
                ${{w.home}}
                <div style="margin-top:4px; font-size:0.72rem; color:#9ca3af;">🥩 Costo: <strong>${{fmtJpy(w.home_jpy)}}</strong> (<span style="color:#4ade80;">${{fmtUsdFromJpy(w.home_jpy)}}</span>)</div>
              </td>
              <td>
                ${{w.geek}}
                <div style="margin-top:4px; font-size:0.72rem; color:#9ca3af;">🎮 Costo: <strong>${{fmtJpy(w.geek_jpy)}}</strong> (<span style="color:#4ade80;">${{fmtUsdFromJpy(w.geek_jpy)}}</span>)</div>
              </td>
              <td>
                ${{w.out}}
                <div style="margin-top:4px; font-size:0.72rem; color:#9ca3af;">🌿 Costo: <strong>${{fmtJpy(w.out_jpy)}}</strong> (<span style="color:#4ade80;">${{fmtUsdFromJpy(w.out_jpy)}}</span>)</div>
              </td>
              <td>
                <div style="margin-bottom:4px;">
                  <span style="display:inline-block; font-size:0.68rem; font-weight:700; padding:1px 7px; border-radius:999px; ${{badgeStyle}}">🗓️ ${{w.days}}</span>
                </div>
                <span style="color:#fcd34d;">${{w.pref}}</span>
                <div style="margin-top:4px; font-size:0.72rem; color:#9ca3af;">🚅 Costo: <strong>${{fmtJpy(w.pref_jpy)}}</strong> (<span style="color:#4ade80;">⚡ ${{fmtUsdFromJpy(w.pref_jpy)}} USD</span>)</div>
              </td>
            </tr>
          `;
        }}

        html += `
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        `;
      }}

      listEl.innerHTML = html || `<p style="padding:1rem; color:var(--text-muted);">No se encontraron citas con ese filtro.</p>`;

      listEl.querySelectorAll("input[data-date-key]").forEach((cb) => {{
        cb.addEventListener("change", (e) => {{
          const k = e.target.getAttribute("data-date-key");
          if (e.target.checked) savedChecks[k] = true;
          else delete savedChecks[k];
          localStorage.setItem("imperio_ayame_dates_v1", JSON.stringify(savedChecks));
          updateSummaryBanner();
        }});
      }});
    }}

    container.innerHTML = `
      <div id="ayame-live-api-summary"></div>

      <div class="item-card" style="margin-bottom:1.1rem; border-color:#38bdf8; background:rgba(56,189,248,0.05);">
        <h4 style="color:#7dd3fc; margin-bottom:0.4rem;">🏡 Protocolo de Hogar Compartido con あやめ &amp; Logística de Escapadas de 2–3 Días</h4>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:10px; font-size:0.8rem; color:var(--text-main);">
          <div>
            <strong>🏠🐱🐹 1. Hogar Compartido (Regresar a Casa = Regresar Juntos):</strong><br>
            あやめ vive contigo en su departamento 2LDK en <strong>Urbanex Asakusabashi Front</strong> junto a nuestros <strong>2 gatitos y 2 chinchillas</strong>. En las citas locales regresan juntos a casa antes de las 21:00 hrs; y en los viajes de 2 o 3 días queda programado el comedero <strong>PETLIBRO</strong>, fuente inox, deshumidificador Sharp + <strong>SwitchBot</strong> y visita diaria de <strong>Pet-Sitter certificada en Taito-ku (Japan Pet Sitter Service / Sewakl, ¥3,500/visita — ya incluido)</strong> con video por LINE.
          </div>
          <div>
            <strong>♨️ 2. Reserva de Ryokan con Rotenburo Privado:</strong><br>
            Todos los viajes de 2–3 días incluyen habitación con <strong>baño termal privado al aire libre (客室露天風呂 / Kashikiri Onsen)</strong> reservado vía <a href="https://travel.rakuten.co.jp/" target="_blank" style="color:#f472b6;">Rakuten Travel</a> / <a href="https://www.jalan.net/" target="_blank" style="color:#f472b6;">Jalan</a>, cena Kaiseki/Teppanyaki con <strong>Wagyu regional (Kobe, Hida, Omi, Koshu, Sendai, Hitachi, Kagoshima — 0 alcohol 🚫🍺 y 0 mango 🚫🥭)</strong> servida a las 18:30 para que a las <strong>22:30 hrs</strong> esté durmiendo abrazada a ti.
          </div>
          <div>
            <strong>🚅 3. Transporte VIP Sin Multitudes (Estándar あやめ):</strong><br>
            Asientos reservados en <strong>Shinkansen Green Car</strong> (<a href="https://www.eki-net.com/" target="_blank" style="color:#38bdf8;">JR East Ekinet</a> / SmartEX), <strong>Odakyu Romancecar GSE</strong>, <strong>Saphir Odoriko</strong> o <strong>Tobu Spacia X Cockpit Suite</strong>, llevando solo una mochila ligera (enviando equipaje por <em>Yamato Takkyubin</em> si es de 3 días).
          </div>
        </div>
      </div>

      <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:space-between; margin-bottom:1.2rem; background:rgba(244,114,182,0.07); border:1px solid rgba(244,114,182,0.3); padding:12px 16px; border-radius:10px;">
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <button class="plan-tab ayame-filter-btn active" data-season="all">🌸🎆🍁❄️ Todas (96 Sem · 384 Citas)</button>
          <button class="plan-tab ayame-filter-btn" data-season="primavera">🌸 Primavera (春)</button>
          <button class="plan-tab ayame-filter-btn" data-season="verano">🎆 Verano (夏)</button>
          <button class="plan-tab ayame-filter-btn" data-season="otono">🍁 Otoño (秋)</button>
          <button class="plan-tab ayame-filter-btn" data-season="invierno">❄️ Invierno (冬)</button>
          <button class="plan-tab ayame-filter-btn" data-season="campamento">🥊 Pausa Tailandia (90d)</button>
          <button class="plan-tab" id="btn-only-multiday" style="border-color:#fb923c; color:#fdba74;">🏨 Ver Solo Viajes de 2–3 Días (${{MULTI_DAY_TRIPS}})</button>
        </div>
        <input id="ayame-date-search" type="search" placeholder="🔍 Buscar prefectura, onsen, juego (ej. Kioto, Hokkaido, Okinawa, Kingdom Hearts)..." style="background:rgba(0,0,0,0.45); border:1px solid rgba(255,255,255,0.2); color:#fff; padding:6px 12px; border-radius:6px; min-width:300px; font-size:0.82rem;">
      </div>
      <div id="ayame-months-list"></div>
    `;

    container.querySelectorAll(".ayame-filter-btn").forEach((btn) => {{
      btn.addEventListener("click", () => {{
        container.querySelectorAll(".ayame-filter-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeSeason = btn.getAttribute("data-season");
        updateView();
      }});
    }});

    const multiBtn = document.getElementById("btn-only-multiday");
    if (multiBtn) {{
      multiBtn.addEventListener("click", () => {{
        onlyMultiDay = !onlyMultiDay;
        multiBtn.classList.toggle("active", onlyMultiDay);
        updateView();
      }});
    }}

    const searchInput = document.getElementById("ayame-date-search");
    if (searchInput) {{
      searchInput.addEventListener("input", (e) => {{
        searchQuery = e.target.value || "";
        updateView();
      }});
    }}

    updateView();
  }}

  if (document.readyState === "loading") {{
    document.addEventListener("DOMContentLoaded", renderAyameCalendar);
  }} else {{
    renderAyameCalendar();
  }}
}})();
"""
    OUT_JS.write_text(js_content, encoding="utf-8")
    print(
        f"[OK] Generated {OUT_JS.name} | 96 weeks (384 unique dates) | "
        f"{multi_day_count} multi-day 2-3d Ryokan/Resort getaways | "
        f"Total 2yr JPY: {total_2yr_jpy:,} JPY (avg {round(total_2yr_jpy/24):,} JPY/month)"
    )


if __name__ == "__main__":
    main()
