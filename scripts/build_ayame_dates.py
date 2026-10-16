#!/usr/bin/env python3
"""
Generates 24 active months (96 weeks = 384 unique dates) for Bruno & Ayame in Japan
(April 2027 – June 2029, explicitly skipping Sept–Nov 2027 during the 90-day Thailand Camp).
Every single week has 4 unique dates:
  1. 🏠 En Casa (Urbanex Asakusabashi Front · Miércoles 19:00–21:15)
  2. 🎮 Cita Friki Juntos (Jueves 19:00–21:15)
  3. 🌿 Actividad Afuera en Tokio (Viernes 17:45–21:00)
  4. 🚅 Escapada a Prefectura Fuera de Tokio (Fin de Semana · regresa antes de las 21:00 para dormir 22:30)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_JS = ROOT / "assets" / "citas-ayame.js"

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
                "out": "Paseo de Hanami (cerezos en flor) al atardecer por el Parque Sumida (a 5 min en tren en Asakusa) tomando té verde caliente viendo el Skytree iluminado",
                "geek": "Noche inaugural de Kingdom Hearts HD 1.5+2.5 ReMIX en la PS5 Pro desde Traverse Town con los gatitos encima y bromas de Denji y Reze",
                "pref": "[Prefectura de Kanagawa · Kamakura] Tren directo JR Sobu-Yokosuka desde cerca de casa: Gran Buda de Kotoku-in, calle Komachi-dori y vista al mar en Yuigahama"
            },
            {
                "w": 2,
                "home": "Taller en casa: elegir patrones del kimono inspirado en Wakamo (Blue Archive) mientras le cocinas Ribeye 300g con mantequilla de ajo y arroz de Zojirushi",
                "out": "Crucero al atardecer en el Tokyo Cruise (Suijo Bus) por el río Sumida saliendo desde Asakusa hasta Hamarikyu Gardens",
                "geek": "Visita juntos a Eorzea Cafe (Final Fantasy XIV) en Pasela Akihabara (a 2 min de casa) pidiendo mocktails sin alcohol de Poción y Éter",
                "pref": "[Prefectura de Saitama · Kawagoe] Viaje al 'Pequeño Edo' (Koedo Kawagoe): paseo por el Callejón de los Dulces (Kashiya Yokocho), Torre del Tiempo y helado de camote"
            },
            {
                "w": 3,
                "home": "Spa de Hinoki en casa: baño aromático con sales de ciprés japonés, mascarillas faciales coreanas (de tu kit Olive Young) y cena de Striploin con piña fresca",
                "out": "Recorrido tranquilo por Nippori Fabric Town (日暮里繊維街, a 10 min en JR): visitar Tomato Fabrics para comprar sedas carmesí y brocados dorados para あやめ",
                "geek": "Tarde en Akihabara Radio Kaikan y AmiAmi buscando figuras oficiales de Blue Archive (Yuuka, Ako y Wakamo) para decorar ambos escritorios",
                "pref": "[Prefectura de Chiba · Naritasan] Excursión a Naritasan Shinshoji: caminar por el parque de estanques, calle tradicional Omotesando y anguila asada (Unagi)"
            },
            {
                "w": 4,
                "home": "Noche de cine Ghibli en el sofá N-Shield de Nitori: ver 'El Viaje de Chihiro' con hamburguesas caseras 100% Wagyu hechas por ti y té de cebada",
                "out": "Festival de las Glicinas (Fuji Matsuri) en el Santuario Kameido Tenjin (a solo 2 estaciones en JR Sobu desde Asakusabashi) bajo túneles morados de flores",
                "geek": "Sesión cooperativa en Nintendo Switch 2 (Mario Kart / It Takes Two) en el televisor 55\" 4K con apuesta de masajes de hombros para el ganador",
                "pref": "[Prefectura de Kanagawa · Yokohama] Paseo por Minato Mirai, el Jardín Sankeien en primavera, teleférico Yokohama Air Cabin y cena de carne en Motomachi"
            }
        ]
    },
    {
        "id": "2027-05",
        "title": "Mayo 2027 — 🌸 Primavera 2: Brisa de Mayo, Rosas y Artesanía de Edo",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mes 3–4 post-cirugía · Paseos al aire libre con clima perfecto de 22°C",
        "weeks": [
            {
                "w": 5,
                "home": "Noche de Teppanyaki casero: cubos de filete estilo Saikoro Steak con brotes de soya en sartén de hierro y prueba de telas en el maniquí 9号 de あやめ",
                "out": "Jardín de Rosas de Primavera en los Jardines Kyu-Furukawa (Kita-ku): villa occidental histórica rodeada de más de 100 variedades de rosas",
                "geek": "Visita a Square Enix Garden / ARTNIA en Shinjuku para ver los cristales de Final Fantasy y peluches de Moogle y Chocobo",
                "pref": "[Prefectura de Tochigi · Ashikaga] Parque Floral de Ashikaga (Ashikaga Flower Park): ver la gran glicina de 150 años iluminada al atardecer"
            },
            {
                "w": 6,
                "home": "Taller de accesorios en casa: armar horquillas de flores (Kanzashi) con cuentas compradas en Asakusabashi mientras cenas Roast Beef casero",
                "out": "Taller de vidrio tallado tradicional Edo Kiriko en Sumida/Asakusa: grabar juntos un par de vasos de cristal con motivos de flores de cerezo",
                "geek": "Maratón de Chainsaw Man (Arco de Reze) en casa con palomitas hechas en olla y recreación de las poses surrealistas (シュール) de Denji y Reze",
                "pref": "[Prefectura de Kanagawa · Enoshima] Isla de Enoshima: cruzar el puente hacia el Santuario Benzaiten, ver las cuevas marinas Iwaya y el faro Sea Candle"
            },
            {
                "w": 7,
                "home": "Cena temática de Ryokan en casa: Sukiyaki hiper-proteico con doble porción de res magra de Hanamasa, tofu y huevo crudo pasteurizado en cazuela",
                "out": "Visita al Planetario Konica Minolta Planetaria TOKYO (Yurakucho) acostados en el asiento doble 'Galaxy Seat' viendo las constelaciones con aromaterapia",
                "geek": "Tarde de Arcade en GiGO Akihabara y Taito Station: ganar peluches en las máquinas UFO Catcher para la cama de あやめ y jugar Taiko no Tatsujin juntos",
                "pref": "[Prefectura de Ibaraki · Hitachinaka] Parque Costero Hitachi (Hitachi Seaside Park): caminar frente al océano Pacífico entre colinas azules de nemophilas y amapolas"
            },
            {
                "w": 8,
                "home": "Noche de repostería sin azúcar refinada ni mango: preparar juntos Cheesecake japonés esponjoso con fresas después de cenar filete Sirloin",
                "out": "Paseo en bote de remos por el foso de Chidorigafuchi y los Jardines del Este del Palacio Imperial rodeados de árboles verdes",
                "geek": "Empezar Final Fantasy VII Rebirth en la PS5 Pro: tú pasas los combates de jefes difíciles y あやめ explora el mundo y elige los atuendos en Costa del Sol",
                "pref": "[Prefectura de Yamanashi · Kawaguchiko] Lago Kawaguchiko y Parque Oishi: vista frontal gigante del Monte Fuji con flores de primavera y carne Koshu Wagyu"
            }
        ]
    },
    # ==================== VERANO 2027 ====================
    {
        "id": "2027-06",
        "title": "Junio 2027 — 🎆 Verano 1: Hortensias (Ajisai), Acuarios y Días de Lluvia Cálida",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Mes 5 post-cirugía · Actividades techadas hermosas y jardines de hortensias",
        "weeks": [
            {
                "w": 9,
                "home": "Campamento de lluvia en la sala: armar un fuerte de mantas en el sofá Nitori con luces cálidas, cenar filetes con papas al romero y escuchar la lluvia con los gatos",
                "out": "Ruta de las Hortensias (Bunkyo Ajisai Matsuri) en el Santuario Hakusan: caminar bajo paraguas transparentes entre 3,000 hortensias azules y violetas",
                "geek": "Visita al Museo Ghibli en Mitaka (con boletos reservados el día 10 del mes anterior): ver el corto exclusivo y el gato-autobús",
                "pref": "[Prefectura de Kanagawa · Hakone] Tren de las Hortensias (Hakone Tozan Railway) + Museo al Aire Libre de Hakone y baño de pies (Ashiyu) frente al lago Ashi"
            },
            {
                "w": 10,
                "home": "Noche de pintura en acuarela: pintar retratos divertidos de sus 2 gatitos y las 2 chinchillas después de cenar Hamburg Steak casero estilo japonés",
                "out": "Acuario Sumida (Sumida Aquarium en Tokyo Skytree Town, a 6 min de casa): ver la zona de medusas iluminadas y los pingüinos tomados de la mano",
                "geek": "Tarde en Ikebukuro Sunshine City: visitar el Pokémon Center Mega Tokyo, la tienda oficial de Bandai Namco y buscar mercancía de Blue Archive",
                "pref": "[Prefectura de Chiba · Kamogawa] Kamogawa Sea World en la costa de Boso: ver las orcas y belugas frente al mar y comer mariscos y carne asada frente a la playa"
            },
            {
                "w": 11,
                "home": "Sesión de costura creativa: terminar el Obi (cinturón) del kimono de Wakamo de あやめ mientras le preparas brochetas de res Yakitori/Kushiyaki en casa",
                "out": "teamLab Planets TOKYO en Toyosu: caminar descalzos por el agua iluminada con carpas koi digitales y el jardín flotante de orquídeas reales",
                "geek": "Noche de Kingdom Hearts III en la PS5 Pro: explorar los mundos de Toy Box y Tangled juntos tomando batidos caseros de sandía y fresa",
                "pref": "[Prefectura de Shizuoka · Atami] Escapada en Shinkansen (40 min desde Tokyo Station) a Atami: Jardín ACAO Forest sobre los acantilados del mar y paseo por la playa"
            },
            {
                "w": 12,
                "home": "Cena de degustación de cortes: comparar 150g de Tenderloin vs 150g de Ribeye vs 150g de Striploin hechos a término medio perfecto con sal de Okinawa",
                "out": "Taller de cerámica tradicional en Yanaka (barrio antiguo de gatos en Taito-ku): moldear juntos en torno dos tazas de té para el departamento",
                "geek": "Ir a Akihabara Mandarake Complex (8 pisos de tesoros retro) a buscar artbooks originales de Kingdom Hearts y Final Fantasy de Tetsuya Nomura",
                "pref": "[Prefectura de Saitama · Chichibu] Paseo en tren panorámico Laview a Chichibu y Nagatoro: descenso tranquilo en barca tradicional de madera por las rocas del río Arakawa"
            }
        ]
    },
    {
        "id": "2027-07",
        "title": "Julio 2027 — 🎆 Verano 2: Tanabata, Fuegos Artificiales del Sumida y Fase 0A en Fighter's Flow",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Arranca tu Fase 0A en Fighter's Flow (15 de julio) con el visto bueno médico · Citas de verano en Yukata",
        "weeks": [
            {
                "w": 13,
                "home": "Noche de Tanabata (7 de julio) en casa: escribir deseos en tiras de papel (Tanzaku) para colgar en bambú en el balcón + cena de filete frío Tataki con ponzu",
                "out": "Tanabata Matsuri en Shitamachi (calle Kappabashi entre Asakusa y Ueno, muy cerca de casa): pasear bajo las decoraciones gigantes de papel de colores",
                "geek": "Sesión de fotos en casa: あやめ estrenando su kimono/yukata estilo Wakamo que cosió en su taller y tú con tu outfit de gala, tomando fotos con trípode",
                "pref": "[Prefectura de Kanagawa · Miura] Península de Miura e Isla Jogashima: caminar por los acantilados volcánicos frente al mar y brisa fresca de verano"
            },
            {
                "w": 14,
                "home": "Noche de Kakigori casero saludable: después de cenar filetes de res, preparar hielo raspado estilo japonés con jarabe natural de fresa y leche condensada",
                "out": "Mercado de las Flores de Farolillo (Hozuki-ichi) en el Templo Senso-ji de Asakusa: comprar una planta de hozuki roja para el balcón de Asakusabashi",
                "geek": "Visita al café/tienda de Kirby Cafe en Tokyo Solamachi (Skytree) o pop-up café de Blue Archive en Akihabara",
                "pref": "[Prefectura de Tochigi · Nikko] Escapada al fresco de las montañas de Nikko (1,200m de altitud): Santuario Toshogu, Cascada Kegon y Lago Chuzenji"
            },
            {
                "w": 15,
                "home": "Cena post-entreno con tu Mánager: te hace masaje con pistola de percusión en los trapecios tras tu sesión con Hayato Suzuki y cenan Wagyu Burgers caseras",
                "out": "Art Aquarium Museum GINZA (en Mitsukoshi): exposición de peces dorados (Kingyo) nadando en peceras de cristal iluminadas como linternas de verano",
                "geek": "Jugar Blue Archive y comparar sus personajes favoritos en la ROG Zephyrus G16 White mientras escuchan el OST de Mitsukiyo en bocinas",
                "pref": "[Prefectura de Nagano · Karuizawa] Shinkansen (1h 10m) al pueblo alpino fresco de Karuizawa: cascada Shiraito, calle Kyu-Karuizawa Ginza y bosque de musgo"
            },
            {
                "w": 16,
                "home": "Velada de Fuegos Artificiales del Río Sumida (Sumidagawa Hanabi Taikai): ver los 20,000 fuegos artificiales desde la azotea/orilla en Yanagibashi a pasos de tu puerta y cenar filetes en casa sin multitudes",
                "out": "Maxell Aqua Park Shinagawa: espectáculo nocturno de delfines con proyecciones digitales de fuegos artificiales bajo techo con aire acondicionado",
                "geek": "Visitar el Museo de la Animación de Suginami o exhibición especial de anime de verano en Tokyo Dome City Gallery AaMo",
                "pref": "[Prefectura de Chiba · Madre Farm (Mother Bokujo)] Colinas frescas de Chiba: ver el espectáculo de pastoreo, dar de comer a alpacas y comer carne a la parrilla Jingisukan"
            }
        ]
    },
    {
        "id": "2027-08",
        "title": "Agosto 2027 — 🎆 Verano 3: Farolillos de Verano y Despedida Romántica antes de Phuket",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Último mes en Tokio antes de volar a Tailandia el 1 de septiembre · Mes de consentir al máximo a あやめ",
        "weeks": [
            {
                "w": 17,
                "home": "Noche de Yakiniku sin humo en la mesa: asar láminas de lengua de res (Gyutan) y Harami de Hanamasa con salsa de limón y sésamo",
                "out": "Festival de Linternas Flotantes (Toro Nagashi) en el río Sumida (Asakusa): lanzar juntos una linterna de papel iluminada sobre el agua al anochecer",
                "geek": "Ir a Nakano Broadway (el templo oculto del coleccionismo retro y celdas de animación originales) y cenar filete en Nakano",
                "pref": "[Prefectura de Yamanashi · Kiyosato] Altiplano de Kiyosato (1,400m de altura): terraza panorámica Kiyosato Terrace en telesilla con aire fresco de montaña"
            },
            {
                "w": 18,
                "home": "Taller de álbum físico: imprimir las mejores fotos de abril a agosto y armar juntos un álbum scrapbooking con cintas Washi de Asakusabashi",
                "out": "Jardines Hamarikyu al atardecer: tomar té matcha con wagashi tradicional en la casa de té flotante Nakajima-no-Ochaya sobre el estanque de marea",
                "geek": "Noche de concierto sinfónico de videojuegos en Tokio (Distant Worlds Final Fantasy / Kingdom Hearts Orchestra o recital de piano de anime)",
                "pref": "[Prefectura de Gunma · Ikaho Onsen] Pueblo de escaleras de piedra de Ikaho: baño privado (Kashikiri Onsen) de aguas termales doradas y paseo en teleférico"
            },
            {
                "w": 19,
                "home": "Preparar 'Cápsulas de Amor' para los 90 días: esconderle 12 cartas escritas a mano por ti (1 para abrir cada domingo que estés en Tailandia) + cena de Tenderloin",
                "out": "Crucero nocturno en barco tradicional Yakatabune por la bahía de Tokio saliendo de Yanagibashi (¡literalmente frente a tu edificio en el río Kanda/Sumida!)",
                "geek": "Terminar juntos la historia principal de Kingdom Hearts II Final Mix en la PS5 Pro y dejar configurado Discord + PS Remote Play para jugar juntos desde Phuket",
                "pref": "[Prefectura de Kanagawa · Hakone Sengokuhara] Praderas verdes de Sengokuhara, Santuario Hakone con el Torii rojo en el agua y carne de res Ashigara"
            },
            {
                "w": 20,
                "home": "Cena especial de despedida pre-campamento en casa: el corte más fino de Wagyu Sirloin A5 + fresas y dejarle toda la despensa, arena de gatos y heno de chinchillas listos para 3 meses",
                "out": "Mirador Shibuya Sky o Tokyo City View (Roppongi Hills) al atardecer viendo todo Tokio iluminarse mientras le prometes volver hecho una máquina para tus 5 peleas",
                "geek": "Comprar dos llaveros/amuletos iguales en el Santuario Kanda Myojin (el santuario del anime en Akihabara): uno para tu maleta de Bangtao y otro para la bolsa de あやめ",
                "pref": "[Prefectura de Shizuoka · Izu高原 (Izu Kogen)] Costa de Jogasaki (puente colgante sobre el océano) y Monte Omuro (el volcán verde con forma de tazón de matcha en telesilla)"
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
                "home": "💌 Domingo de Carta Escondida: Cada domingo en Tokio, あやめ abre una de las 12 cartas físicas que le dejaste escondidas en casa + pedido UberEats sorpresa que le mandas a la puerta",
                "out": "📸 Reporte de tu Mánager: Le mandas videos cortos de tus sparrings en Bangtao y fotos de tus filetotes en Mamma Mia para que ella elija la música y estética de tus redes",
                "geek": "🎮 Viernes de Co-Op Online (19:30 TH / 21:30 JP): 45 minutos jugando juntos Final Fantasy XIV / Switch 2 online antes de su baño nocturno",
                "pref": "🌙 Ritual Sagrado de las 22:00 JP (20:00 TH): Videollamada suave de 20 minutos mientras ella está en cama con los gatitos hasta que a las 22:30 JP se duerme tranquila"
            }
        ]
    },
    # ==================== INVIERNO 2027-2028 ====================
    {
        "id": "2027-12",
        "title": "Diciembre 2027 — ❄️ Invierno 1: Regreso Triunfal de Tailandia, Iluminaciones y Navidad Juntos",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Regresas el 11–12 de diciembre hecho una roca de 78.5 kg · Reencuentro con あやめ, Navidad y Año Nuevo en Tokio",
        "weeks": [
            {
                "w": 21,
                "home": "Noche de Reencuentro tras 90 días: entregarle sus regalos de Tailandia (sedas tailandesas para su taller de costura) y cenar Filete Tenderloin caliente en casa abrazados con los gatos",
                "out": "Paseo por las Iluminaciones de Invierno de Marunouchi (calle Naka-dori vestida con 1.2 millones de luces color champán) tomando chocolate/té caliente",
                "geek": "Estrenar juntos tu equipamiento Venum x Mike Tyson Black/Gold en casa: sesión de fotos donde tu Mánager あやめ dirige tus poses oficiales de peleador",
                "pref": "[Prefectura de Kanagawa · Sagamiko Illumillion] El festival de iluminación más grande de Kanto en el bosque del lago Sagami con telesilla iluminado sobre un mar de luces"
            },
            {
                "w": 22,
                "home": "Noche de Shabu-Shabu invernal en casa: caldo dashi hirviendo con láminas finas de res magra de Hanamasa, hongos shiitake y salsa de ajonjolí",
                "out": "Mercado Navideño Europeo en Azabudai Hills / Roppongi Hills y caminata viendo la Torre de Tokio iluminada con colores de invierno",
                "geek": "Visita a Akihabara Kotobukiya y Volks Hobby Paradise para comprar materiales de modelismo y ver las vitrinas navideñas de anime",
                "pref": "[Prefectura de Saitama · Parque Moominvalley (Hanno)] Pueblo nórdico junto al lago Miyazawa en Saitama: cabañas escandinavas, bosque iluminado de invierno y paz total"
            },
            {
                "w": 23,
                "home": "Cena de Nochebuena (24 de diciembre) en casa: Roast Beef navideño horneado por ti + pastel de Navidad japonés de fresas con crema (Christmas Shortcake)",
                "out": "Patinaje sobre hielo suave tomados de la mano en la pista al aire libre de Tokyo Midtown (Roppongi) o Akasaka Sacas (con mucho cuidado para no resbalar)",
                "geek": "Maratón navideño de Kingdom Hearts (visitar Christmas Town en Halloween Town de KH2) con gorros navideños para los gatitos",
                "pref": "[Prefectura de Chiba · Tokyo German Village (Sodegaura)] Iluminación invernal gigante de 3 millones de LEDs en las colinas de Chiba al atardecer"
            },
            {
                "w": 24,
                "home": "Nochevieja Japonesa (Omisoka · 31 de diciembre): cenar Toshikoshi Soba con láminas de Roast Beef en casa a las 20:00 y escuchar las campanas de los templos abrazados",
                "out": "Feria de Año Nuevo (Toshi-no-Ichi / Hagoita-Ichi) en el Templo Senso-ji de Asakusa: ver las paletas decorativas tradicionales de madera pintada",
                "geek": "Armar juntos su lista de videojuegos y animes más esperados de 2028 mientras abren sobres coleccionables de cartas de Blue Archive / Final Fantasy",
                "pref": "[Prefectura de Kanagawa · Odawara y Yugawara Onsen] Visitar el Castillo de Odawara y sumergirse en un baño termal privado de invierno en Yugawara Onsen"
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
                "home": "Cena de Año Nuevo (Oshogatsu) hiper-carnívora: filetes de Ribeye + Ozoni casero (sopa tradicional con mochi asado) y escribir juntos su caligrafía de Año Nuevo (Kakizome)",
                "out": "Hatsumode (primera visita al santuario del año) en el Santuario Kanda Myojin: pedir por tu victoria 5–0 en el octágono y por la paz y salud de あやめ y 千秋-san",
                "geek": "Caza de Fukubukuro (bolsas de la suerte de Año Nuevo) en Akihabara y Animate para あやめ",
                "pref": "[Prefectura de Gunma · Kusatsu Onsen] Escapada de invierno a Kusatsu Onsen: ver el Yubatake humeante rodeado de nieve blanca y ceremonia Yumomi"
            },
            {
                "w": 26,
                "home": "Taller de vestuario de pelea: あやめ da las últimas puntadas a tu bata/kimono de entrada al octágono mientras tú le cocinas Tenderloin con espárragos",
                "out": "Exhibición de Bonsáis centenarios en el Museo del Bonsái de Omiya o Jardín Rikugien en calma invernal con casa de té junto al agua",
                "geek": "Tarde de juegos de mesa japoneses para dos (Shogi / Hanafuda / Machi Koro) y videojuegos indie en la Switch 2",
                "pref": "[Prefectura de Niigata · Gala Yuzawa] Shinkansen directo desde Ueno (75 min) hasta la nieve pura de Niigata: subir en góndola a ver los Alpes nevados y tomar cacao caliente"
            },
            {
                "w": 27,
                "home": "Noche de Sukiyaki estilo Kansai (dorando primero la carne con azúcar morena y salsa de soya en hierro fundido) + masaje de pies para あやめ",
                "out": "Paseo por el Jardín de Ciruelos Tempranos (Ume) en el Santuario Yushima Tenjin (en Bunkyo-ku, a 5 min de casa)",
                "geek": "Visitar el Museo Bandai (Bandai Museum / Tamashii Nations Store Tokyo en Akihabara) para ver las armaduras a escala real",
                "pref": "[Prefectura de Tochigi · Kinugawa Onsen] Aguas termales junto al cañón del río Kinugawa y visita a Tobu World Square iluminado"
            },
            {
                "w": 28,
                "home": "Ensayo general de pesaje y esquina en casa: practicar con あやめ tu lista de canciones de salida y el protocolo de OS-1 + cena limpia de filete magro",
                "out": "Crucero de invierno con calefacción y techo de cristal (Himiko / Hotaluna diseñado por Leiji Matsumoto) desde Asakusa hasta Odaiba",
                "geek": "En Odaiba: ver el Unicorn Gundam tamaño real transformarse con luces nocturnas y entrar a The Gundam Base Tokyo",
                "pref": "[Prefectura de Yamanashi · Yamanakako] Lago Yamanaka en invierno: ver los cisnes blancos nadando con el Monte Fuji cubierto de nieve de fondo"
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
                "home": "Noche de Setsubun (3 de febrero): lanzar frijoles de la suerte ('Oni wa soto! Fuku wa uchi!') con máscaras divertidas para los gatos y comer rollos Ehomaki rellenos de Roast Beef",
                "out": "Festival del Ciruelo (Bunkyo Ume Matsuri) en Yushima Tenjin y paseo tranquilo por los jardines de Koishikawa Korakuen",
                "geek": "Jugar juntos Final Fantasy XVI / VII en modo historia mientras descansas las piernas en la semana previa al corte de agua",
                "pref": "[Prefectura de Shizuoka · Kawazu] Tren expreso Odoriko a Kawazu para ver los primeros cerezos en flor de Japón (Kawazu-zakura) en pleno febrero junto al río"
            },
            {
                "w": 30,
                "home": "Cena de San Valentín (14 de febrero): ella te regala chocolates artesanales japoneses y tú le cocinas Chateaubriand (centro de Tenderloin) con fresas blancas Awayuki",
                "out": "Salón del Chocolate (Amour du Chocolat / Salon du Chocolat) en Isetan Shinjuku o Nihombashi Mitsukoshi para elegir bombones juntos",
                "geek": "Cita de fotos Purikura en Akihabara vestida de estilo coord invernal y tú con tu hoodie Supreme Box Logo, pegando los stickers en sus fundas",
                "pref": "[Prefectura de Ibaraki · Mito Kairakuen] Uno de los 3 Grandes Jardines de Japón durante el Festival del Ciruelo de Mito (3,000 ciruelos en flor)"
            },
            {
                "w": 31,
                "home": "🏆 ¡CENA DE VICTORIA DE TU PELEA #1 (1–0)! Banquete en casa con tu medalla/trofeo: Doble Wagyu Burger + Tenderloin 300g y あやめ celebrando como Mánager invicta",
                "out": "Paseo de celebración por Ginza Chuo-dori (peatonal de fin de semana) comprándole un detalle hermoso en Ginza Itoya (12 pisos de papelería fina para su taller)",
                "geek": "Comprar una vitrina acrílica con luz LED en Akihabara para exhibir tu primer trofeo/guantes de victoria junto a sus figuras de Blue Archive",
                "pref": "[Prefectura de Kanagawa · Hakone Kowakien Yunessun / Gora] Día de spa termal de recuperación muscular post-pelea en los baños al aire libre de Gora"
            },
            {
                "w": 32,
                "home": "Noche de cine y masaje de recuperación: ver juntos los videos de tu sumisión de la Pelea #1 y editar el reel triunfal para redes",
                "out": "Visita al Museo Edo-Tokyo (reabierto y renovado en Ryogoku, a 1 estación de Asakusabashi) cruzando el río Sumida a pie",
                "geek": "Tarde en el Café Capcom (Ikebukuro) o Monster Hunter Bar en Shinjuku probando platillos temáticos de cazador",
                "pref": "[Prefectura de Chiba · Península de Boso (Tateyama)] Campos de flores amarillas Nanohana frente al mar en Tateyama con clima templado"
            }
        ]
    },
    # ==================== PRIMAVERA 2028 ====================
    {
        "id": "2028-03",
        "title": "Marzo 2028 — 🌸 Primavera 3: White Day, Campeonato DEEP Future King (4–0) y Cerezos",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Marzo 2028 · White Day (14 mar) + Torneo DEEP Future King (Peleas #2, #3 y #4 → ¡Campeón 4–0!)",
        "weeks": [
            {
                "w": 33,
                "home": "Noche de Hinamatsuri (3 de marzo): decorar el departamento con flores de durazno (Momo) y preparar Chirashizushi con láminas de Roast Beef y salmón",
                "out": "Exposición de las Mil Muñecas Hina en las escaleras del Santuario Tomioka Hachiman o Meguro Gajoen (Hyakudan Kaidan)",
                "geek": "Noche de estudio de brackets del torneo DEEP Future King con tu Mánager あやめ usando pizarrón estilo anime táctico",
                "pref": "[Prefectura de Saitama · Kinchakuda / Hanno] Caminata por los valles y ríos cristalinos de Hidaka al inicio de la primavera"
            },
            {
                "w": 34,
                "home": "Cena de White Day (14 de marzo, donde el hombre devuelve 3 veces el regalo de San Valentín): regalarle una joya/accesorio delicado + cena de filete Wagyu A5",
                "out": "Paseo por el barrio histórico de Kagurazaka (las callejuelas empedradas estilo Kioto/París en Tokio) y postre en una casa de té tradicional",
                "geek": "Visitar el estudio/exposición de arte de Final Fantasy (Amano Yoshitaka / Square Enix Pop-up) y comprar pósters enmarcados",
                "pref": "[Prefectura de Kanagawa · Castillo de Odawara en floración temprana] Pasear por los fosos del castillo y comer kamaboko artesanal junto al mar"
            },
            {
                "w": 35,
                "home": "🏆👑 ¡BANQUETE DE CAMPEÓN DE DEEP FUTURE KING (4–0)! Celebrar en casa con el trofeo/cinturón tras ganar tus 3 peleas en una tarde en New Pier Hall",
                "out": "Paseo triunfal de Hanami temprano por el río Meguro viendo los farolillos rosas reflejados en el canal con los primeros cerezos",
                "geek": "Sesión de fotos épica en casa: あやめ posando con tu trofeo de Campeón de DEEP vestida de Wakamo / Ako y tú con tus guantes oficiales",
                "pref": "[Prefectura de Yamanashi · Chureito Pagoda (Fujiyoshida)] Subir juntos a la pagoda roja de 5 pisos con los cerezos en flor y el Monte Fuji frente a ustedes"
            },
            {
                "w": 36,
                "home": "Noche de picnic Hanami en la terraza/sala: preparar juntos cajas Bento de dos pisos con filete Teriyaki casero, tamagoyaki y fresas",
                "out": "Hanami en el Jardín Nacional Shinjuku Gyoen (1,000 cerezos de 65 variedades): acostarse sobre una manta bajo los pétalos que caen",
                "geek": "Tarde de compras en Shibuya Parco (6º piso Cyberspace): Nintendo Tokyo, Pokémon Center, Jump Shop y Capcom Store todo en un mismo piso",
                "pref": "[Prefectura de Tochigi · Moka Railway] Ver el tren de vapor real SL Moka cruzando un túnel de cerezos en flor y campos amarillos de colza"
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
                "out": "Paseo por el Túnel de Cerezos Tardíos (Yaezakura) y Azaleas del Santuario Nezu (en Bunkyo-ku, uno de los santuarios más bellos de Tokio)",
                "geek": "Noche de Kingdom Hearts: Birth by Sleep / Dream Drop Distance con gafas de descanso mientras cicatrizan los ojos",
                "pref": "[Prefectura de Chiba · Ferrocarril Kominato] Viaje en el tren retro amarillo cruzando campos de flores primaverales en el corazón rural de Chiba"
            },
            {
                "w": 38,
                "home": "Taller de diseño de modas: comprar telas de lino y algodón fresco de primavera para hacer ropa de verano para ambos en la máquina JUKI",
                "out": "Paseo por el Parque Inokashira en Kichijoji: pedalear en un bote de cisne por el lago y caminar por las tienditas artesanales de Harmonica Yokocho",
                "geek": "Visitar el Café Shirohige's Cream Puff Factory (en Setagaya) para comer los pastelitos oficiales con forma de Totoro rellenos de crema de fresa",
                "pref": "[Prefectura de Saitama · Parque Hitsujiyama (Chichibu)] Ver la alfombra gigante rosa y blanca de Shibazakura (musgo rosa en flor) frente al monte Buko"
            },
            {
                "w": 39,
                "home": "Noche de Fondue de Queso y Filete: cubos calientes de Striploin a la parrilla sumergidos en queso fundido en la mesa del comedor",
                "out": "Visita al Jardín Botánico de Koishikawa (el más antiguo de Japón, perteneciente a la Universidad de Tokio) en una tarde soleada sin gente",
                "geek": "Tarde de juegos de ritmo y baile en casa (Just Dance / Taiko / Project Diva) para reírse y mover el cuerpo juntos sin presión",
                "pref": "[Prefectura de Kanagawa · terrenos de futura casa 二世帯住宅 en Kanagawa] Paseo exploratorio bonito por barrios residenciales verdes de Kanagawa (Fujisawa / Tsujido / Kamakura) soñando el hogar con 千秋-san"
            },
            {
                "w": 40,
                "home": "Noche de Spa capilar y facial en casa: cepillado relajante, mascarillas y cena de salmón salvaje + filete magro",
                "out": "Festival de las Peonías (Botan Matsuri) en el Templo Ueno Toshogu (a 5 min de Asakusabashi en el Parque Ueno)",
                "geek": "Ir a Akihabara Super Potato (el museo viviente de consolas retro de los 90s y 2000s) y jugar clásicos en el último piso",
                "pref": "[Prefectura de Gunma · Parque Floral de Gunma y Monte Akagi] Aire puro de montaña, invernaderos de flores y carne Joshu Wagyu"
            }
        ]
    },
    {
        "id": "2028-05",
        "title": "Mayo 2028 — 🌸 Primavera 5: Boda Civil (Kon'in Todoke), 5ª Pelea (5–0) y Sol de Mayo",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mayo 2028 · ¡Boda oficial con あやめ y cierre invicto 5–0 de tu campaña de MMA!",
        "weeks": [
            {
                "w": 41,
                "home": "💍 ¡Noche de Boda Oficial (Kon'in Todoke)! Cena íntima a la luz de las velas LED en casa: Chateaubriand Wagyu A5, fresas reales y brindis con Perrier y jugo de uva blanca (0 alcohol)",
                "out": "Entregar juntos su registro de matrimonio (婚姻届) en la alcaldía de Taito-ku / Chiyoda-ku y sesión de fotos vestidos de gala frente a los puentes de piedra de Marunouchi",
                "geek": "Enmarcar juntos su certificado de matrimonio conmemorativo con diseño especial de anime/flores en su pared del salón",
                "pref": "[Prefectura de Kanagawa · Invitación especial a 千秋-san en Yokohama/Kamakura] Almuerzo familiar de celebración en un restaurante tranquilo con vista al jardín para darle paz y alegría a su mamá"
            },
            {
                "w": 42,
                "home": "Noche de lectura de manga juntos en el sofá: cada uno lee su tomo favorito con los pies entrelazados y los gatitos ronroneando en medio",
                "out": "Festival Kanda Matsuri / Sanja Matsuri en Asakusa: ver los santuarios portátiles (Mikoshi) dorados desfilando cerca de nuestro barrio",
                "geek": "Visitar el Museo de Arte de Mori (Roppongi) o exhibición inmersiva de videojuegos/manga en Tokio",
                "pref": "[Prefectura de Chiba · Jardín de Rosas de Keisei (Yachiyo)] Caminar bajo pérgolas de 1,600 variedades de rosas perfumadas en su punto máximo de mayo"
            },
            {
                "w": 43,
                "home": "🏆👑 ¡CENA DE LA 5ª PELEA INVICTA (5–0)! Celebrar el retiro invicto de tu campaña amateur con los 2 campeonatos en la vitrina de casa",
                "out": "Crucero privado/panorámico por los canales de Nihombashi saliendo del puente histórico de Nihombashi bajo el cielo azul de mayo",
                "geek": "Grabar y editar juntos el documental casero 'De 0–0 a 5–0 en Japón: El Peleador y su Mánager あやめ' para guardarlo toda la vida",
                "pref": "[Prefectura de Shizuoka · Península de Izu (Shuzenji)] El 'Pequeño Kioto de Izu': caminar por el Bosque de Bambú de Shuzenji y los puentes rojos sobre el río Katsura"
            },
            {
                "w": 44,
                "home": "Cena de brochetas de filete y piña asada a la plancha + noche de masajes de espalda completa",
                "out": "Paseo por el Jardín de Iris (Horikiri Shobuen en Katsushika-ku) viendo miles de flores de iris blancas y moradas junto al agua",
                "geek": "Tarde de diseño 3D / ilustración en tu PC RTX 5090 ayudando a あやめ a digitalizar sus patrones de costura",
                "pref": "[Prefectura de Nagano · Kamikochi / Matsumoto] Excursión al Castillo Negro de Matsumoto (Tesoro Nacional) y vista de los Alpes Japoneses"
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
                "out": "Noche de las Luciérnagas (Hotaru no Yube) en los jardines del Hotel Chinzanso Tokyo: caminar de la mano viendo cientos de luciérnagas reales brillar entre la niebla del jardín",
                "geek": "Recorrer las calles de Akihabara y Kanda buscando las locaciones reales de animes famosos y tomar fotos recreando cada plano",
                "pref": "[Prefectura de Kanagawa · Kita-Kamakura (Meigetsuin)] El 'Templo de las Hortensias': ver la famosa ventana circular (Satori no Mado) rodeada de hortensias azules"
            },
            {
                "w": 46,
                "home": "Taller de perfumería casera japonesa: crear bolsitas aromáticas (Nioibukuro) con sándalo y clavo para los closets de su ropa y de tus hoodies",
                "out": "Taller de Kintsugi (reparación de cerámica con polvo dorado) en Tokio: unir una pieza de cerámica juntos como símbolo de sanación y belleza",
                "geek": "Empezar una partida nueva de Final Fantasy X HD Remaster en la PS5 Pro reviviendo la escena del lago Macalania",
                "pref": "[Prefectura de Yamanashi · Monte Minobu y Lago Motosu] Ver el lago que aparece en el billete de 1,000 yenes (y en Yuru Camp) con aguas color turquesa"
            },
            {
                "w": 47,
                "home": "Cena de Roast Beef en costra de hierbas horneado en casa + cata de sandía japonesa cuadrada/dulce de verano",
                "out": "Visita al Museo Nezu en Minami-Aoyama (diseñado por Kengo Kuma) y caminata por su jardín secreto de bambú y linternas de piedra",
                "geek": "Ir a un Maid/Concept Café tranquilo o cafetería temática de gatos/nutrias en Harajuku/Ikebukuro que a あやめ le haga ilusión",
                "pref": "[Prefectura de Chiba · Sawara (Katori)] El pueblo de canales históricos de Edo en Chiba: paseo en barca de madera bajo sauces llorones e iris"
            },
            {
                "w": 48,
                "home": "Noche de juegos de feria japonesa (Ennichi) en casa: preparar yakisoba con tiras gruesas de filete y jugar pesca de globos de agua (Yo-yo Tsuri) en el baño",
                "out": "Ceremonia de purificación de mitad de año (Nagoshi no Harae) cruzando juntos el gran anillo de junco (Chinowa Kuguri) en el Santuario Asakusa / Kanda",
                "geek": "Noche de trivia y dibujo de personajes de Blue Archive y Kingdom Hearts de memoria sin ver referencias (risas garantizadas)",
                "pref": "[Prefectura de Tochigi · Nasu Highlands] Escapada en Shinkansen a las tierras altas de Nasu: granja South Hills, bosque fresco y carne Tochigi Wagyu"
            }
        ]
    },
    {
        "id": "2028-07",
        "title": "Julio 2028 — 🎆 Verano 5: Campanas de Viento (Furin), Islas y Brisa Marina",
        "season": "verano",
        "season_label": "🎆 Verano (夏)",
        "phase_note": "Julio 2028 · Verano tranquilo en pareja sin presión de corte de peso",
        "weeks": [
            {
                "w": 49,
                "home": "Decorar el balcón de Asakusabashi con una campana de cristal Edo Furin pintada a mano + cena de filete Sirloin con ensalada de pepino japonés y sésamo",
                "out": "Mercado de los Faroles de Verano (Asagao Matsuri / Mercado de las Campanillas) en Iriya (Taito-ku, a 6 min de casa)",
                "geek": "Visitar el Museo Fujiko F. Fujio (Doraemon) en Kawasaki o exposición de verano de Weekly Shonen Jump",
                "pref": "[Prefectura de Saitama · Santuario Kawagoe Hikawa (Enmusubi Furin)] Caminar bajo el túnel de 2,000 campanas de viento de cristal que suenan con la brisa para los matrimonios felices"
            },
            {
                "w": 50,
                "home": "Noche de helados artesanales en casa: hacer paletas heladas de fresa, arándanos y yogur griego después de cenar filetes a la plancha",
                "out": "Acuario Sunshine (Ikebukuro) al atardecer viendo los 'pingüinos voladores' nadar sobre el horizonte de rascacielos de Tokio",
                "geek": "Tarde en Akihabara probando teclados mecánicos custom y keycaps de resina artesanales para el setup de あやめ",
                "pref": "[Prefectura de Kanagawa · Hayama y Zushi Marina] Paseo estilo Riviera japonesa entre palmeras frente al mar en Zushi y carne de res Hayama Gyu"
            },
            {
                "w": 51,
                "home": "Taller de teñido japonés Shibori (añil Índigo) en casa: teñir dos pañuelos Tenugui con patrones geométricos únicos",
                "out": "Caminata nocturna por el Valle de Todoroki (el único cañón boscoso natural dentro de Tokio con río y puente rojo, 5°C más fresco que la ciudad)",
                "geek": "Noche de película de Makoto Shinkai ('El Jardín de las Palabras' y 'Weathering With You') abrazados con aire acondicionado fresco",
                "pref": "[Prefectura de Shizuoka · Mishima Skywalk] El puente peatonal colgante más largo de Japón con vista al Monte Fuji y la bahía de Suruga + manantiales cristalinos de Kakita River"
            },
            {
                "w": 52,
                "home": "🎉 ¡Semana 52 (1 Año Activo de Citas)! Cena de aniversario del calendario: Filete Tenderloin envuelto en tocino + pastel de crepas (Mille Crepe) de frutas sin mango",
                "out": "Festival de Fuegos Artificiales de Adachi o Katsushika sentados cómodos en asientos reservados viendo el cielo iluminarse",
                "geek": "Crear juntos en PC un fotolibro impreso de tapa dura con las mejores fotos de las primeras 52 semanas de aventuras",
                "pref": "[Prefectura de Yamanashi · Fuefukigawa Fruit Park y Hottarakashi Onsen] Mirador de las '3 Grandes Vistas Nocturnas de Japón' sobre el valle de Kofu"
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
                "out": "Festival de Linternas Mitama Matsuri o iluminación de verano en el Santuario Meiji / Tokyo大神宮 (Tokyo Daijingu)",
                "geek": "Visitar el evento de verano de Akihabara Electric Town Festival y buscar tapices de edición limitada de Wakamo y Yuuka",
                "pref": "[Prefectura de Tokio Occidental / Yamanashi · Campos de Girasoles de Kiyose o Hokuto (Akeno)] Caminar entre 600,000 girasoles amarillos gigantes bajo el sol de verano"
            },
            {
                "w": 54,
                "home": "Noche de Somen helado en cuenco de hielo con tiras de filete de res a la parrilla y jengibre rallado",
                "out": "teamLab Borderless en Azabudai Hills: perderse juntos en la sala de lámparas de cristal infinitas (Crystal World)",
                "geek": "Jugar juntos Kingdom Hearts: Melody of Memory (el juego musical de toda la saga) cantando 'Simple and Clean' y 'Sanctuary'",
                "pref": "[Prefectura de Gunma · Minakami y Garganta de Suwakyo] Teleférico Tanigawadake Ropeway a 1,500m de altitud con brisa fresca de 20°C en pleno agosto"
            },
            {
                "w": 55,
                "home": "Sesión de costura de otoño: diseñar juntos una capa/haori ligera para あやめ que combine con tus outfits",
                "out": "Jardín Happo-en en Shirokanedai: ver la colección de bonsáis de 500 años y los estanques de carpas koi en silencio absoluto",
                "geek": "Tarde en un Café de Juegos de Mesa (JELLY JELLY CAFE en Akihabara/Shibuya) en mesa privada para dos",
                "pref": "[Prefectura de Nagano · Meseta de Kirigamine y Lago Shirakaba] Ruta panorámica Venus Line entre praderas alpinas verdes a 1,800m de altura"
            },
            {
                "w": 56,
                "home": "Noche de cine clásico y filetes al ajo: preparar Garlic Rice en la plancha de hierro igual que en los restaurantes Teppanyaki de Ginza",
                "out": "Espectáculo de fuentes danzantes iluminadas y paseo nocturno frente al mar en el Parque Marino de Odaiba",
                "geek": "Visitar la tienda insignia de Square Enix / Animate Ikebukuro (el edificio de anime más grande del mundo renovado)",
                "pref": "[Prefectura de Chiba · Cabo Inubosaki (Choshi)] Viaje en el pintoresco tren Choshi Electric Railway hasta el faro blanco en el punto más oriental de Kanto"
            }
        ]
    },
    # ==================== OTOÑO 2028 ====================
    {
        "id": "2028-09",
        "title": "Septiembre 2028 — 🍁 Otoño 1: Luna de Cosecha (Tsukimi), Lirios Rojos y Primer Otoño Juntos en Tokio",
        "season": "otono",
        "season_label": "🍁 Otoño (秋)",
        "phase_note": "Septiembre 2028 · ¡Su primer otoño completo juntos en Japón (ya que en 2027 estuviste en Tailandia)!",
        "weeks": [
            {
                "w": 57,
                "home": "Noche de Tsukimi (Contemplación de la Luna Llena de Otoño): hacer Tsukimi Dango con forma de conejitos + Hamburg Steak con huevo estrellado ('luna llena')",
                "out": "Festival de la Luna (Tsukimi) en los Jardines Mukojima-Hyakkaen (en Sumida-ku, muy cerca de casa): escuchar los grillos de otoño entre linternas de papel",
                "geek": "Ir a Tokyo Game Show (TGS 2028 en Makuhari Messe) o ver juntos todos los tráilers en vivo desde el sofá con filetes recién hechos",
                "pref": "[Prefectura de Saitama · Kinchakuda (Hidaka)] Caminar entre 5 millones de Lirios Araña Rojos (Higanbana) que cubren el bosque como una alfombra carmesí"
            },
            {
                "w": 58,
                "home": "Cena de otoño con filete Tenderloin y hongos Matsutake/Eringi salteados en mantequilla y salsa de soya",
                "out": "Paseo por las galerías de arte y cafés tranquilos de Kiyosumi-Shirakawa + Jardín Kiyosumi (cruzando las piedras 'Iso-watari' sobre el agua)",
                "geek": "Maratón de anime de otoño: elegir 3 estrenos de la temporada de octubre y ver los primeros episodios acurrucados con los gatos",
                "pref": "[Prefectura de Kanagawa · Kamakura Hasedera y Engakuji] Pasear por los templos zen de Kamakura con la brisa fresca de septiembre y comer dango asado"
            },
            {
                "w": 59,
                "home": "Taller de encuadernación japonesa (Watoji) en casa: coser juntos a mano dos cuadernos con cubiertas de tela de kimono de Nippori",
                "out": "Recorrido en bicicleta eléctrica (Docomo Bike Share) por las calles arboladas de Marunouchi, Hibiya Park y el Palacio Imperial",
                "geek": "Visitar el Museo de la Ciencia y la Innovación (Miraikan en Odaiba) y ver las exhibiciones de robótica e inteligencia artificial",
                "pref": "[Prefectura de Ibaraki · Parque Costero Hitachi en Otoño] Ver las 32,000 plantas de Kochia empezando a teñirse de verde esmeralda a rojo carmesí frente al mar"
            },
            {
                "w": 60,
                "home": "Noche de cata de castañas japonesas (Kuri) y camote asado (Yaki-imo) como postre después de un filete Striploin de 350g",
                "out": "Asistir a una función vespertina corta (1 acto con subtítulos/audioguía) en el Teatro Kabukiza de Ginza para admirar el vestuario tradicional japonés",
                "geek": "Tarde de fotos y compras en Ikebukuro Otome Road / K-Books para que あやめ compre todo el merch de sus personajes favoritos",
                "pref": "[Prefectura de Yamanashi · Katsunuma] Valle de las Uvas de Yamanashi: recolectar uvas gigantes Shine Muscat directamente del viñedo y comer carne Koshu"
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
                "out": "Festival de las Flores Cosmos en el Parque Showa Kinen (Tachikawa): caminar entre millones de flores cosmos rosas y blancas",
                "geek": "Preparar juntos su Cosplay de pareja para fin de mes: Denji y Reze (Chainsaw Man) o Sensei y Wakamo (Blue Archive) en el taller de あやめ",
                "pref": "[Prefectura de Tochigi · Oku-Nikko (Ryuzu Falls y Senjogahara)] Primeras hojas rojas de otoño (Koyo) en las cascadas y humedales altos de Nikko"
            },
            {
                "w": 62,
                "home": "Noche de hornear panecillos o galletas con formas de sus 2 gatitos y las 2 chinchillas después de cenar Roast Beef",
                "out": "Feria del Libro Antiguo de Kanda Jimbocho (la ciudad de las librerías más grande del mundo, a 6 min de casa): buscar grabados Ukiyo-e y libros de arte textil",
                "geek": "Jugar Luigi's Mansion o juegos de misterio/aventura ligeros en la Switch 2 con las luces bajas (sin sustos fuertes para cuidar el sueño de あやめ)",
                "pref": "[Prefectura de Nagano · Estanque Kumoba (Karuizawa)] Ver los arces rojos reflejados como un espejo en el 'Lago de los Cisnes' de Karuizawa"
            },
            {
                "w": 63,
                "home": "Cena de Gyukatsu casero (filete de res empanizado en panko ultra crujiente por fuera y término medio rojo por dentro, terminado en piedra caliente)",
                "out": "Festival de los Crisantemos (Kiku Matsuri) en el Santuario Yushima Tenjin y Templo Senso-ji",
                "geek": "Visitar el evento de Halloween de Ikebukuro (Ikebukuro Halloween Cosplay Fest, mucho más seguro, ordenado y artístico que Shibuya) de día",
                "pref": "[Prefectura de Gunma · Monte Haruna y Lago Haruna] Subir en teleférico entre montañas teñidas de naranja y rojo (y ver las curvas famosas de Initial D)"
            },
            {
                "w": 64,
                "home": "🎃 Noche de Halloween en Casa (31 de octubre): ponerse sus trajes de Denji & Reze / Wakamo en casa, sesión de fotos divertida con los gatos y cena de filetes",
                "out": "Tokyo DisneySea en otoño (regresando a las 20:30 en tren directo desde Maihama para respetar su descanso): pasear por Fantasy Springs y Mediterranean Harbor",
                "geek": "En DisneySea / casa: celebrar el vínculo con Kingdom Hearts buscando los emblemas de Mickey ocultos y jugando el mundo de Hércules/Arendelle",
                "pref": "[Prefectura de Ibaraki · Puente Colgante de Ryujin y Cascadas Fukuroda] Una de las 3 grandes cascadas de Japón rodeada de arces otoñales"
            }
        ]
    },
    {
        "id": "2028-11",
        "title": "Noviembre 2028 — 🍁 Otoño 3: Ginkgos Dorados, Momiji Nocturno y Tori-no-Ichi",
        "season": "otono",
        "season_label": "🍁 Otoño (秋)",
        "phase_note": "Noviembre 2028 · Tokio se pinta de oro y rojo carmesí (Momijigari)",
        "weeks": [
            {
                "w": 65,
                "home": "Cena de olla caliente Sukiyaki de otoño con hongos Maitake y doble filete de res + té Hojicha tostado",
                "out": "Avenida de los Ginkgos de Meiji Jingu Gaien (Icho Namiki): caminar sobre la alfombra dorada de hojas amarillas de ginkgo tomando cacao caliente",
                "geek": "Visitar el Museo de la Animación de Toei (Oizumi) o exposición de arte original de CLAMP / Type-Moon / Square Enix",
                "pref": "[Prefectura de Yamanashi · Corredor de Arces de Kawaguchiko (Momiji Kairou)] Túnel de arces rojos iluminados de noche con el Monte Fuji nevado atrás"
            },
            {
                "w": 66,
                "home": "Taller de bordado japonés Sashiko en casa: bordar motivos tradicionales en tela índigo mientras escuchan jazz japonés de fondo",
                "out": "Iluminación Nocturna de Otoño en el Jardín Rikugien: ver los arces rojos reflejados en el gran estanque central al anochecer",
                "geek": "Tarde en Akihabara buscando bandas sonoras en vinilo/CD de Final Fantasy y Kingdom Hearts en Tower Records / Traders",
                "pref": "[Prefectura de Saitama · Parque Forestal Musashi Kyuryo o Nagatoro Momiji] Paseo bajo arces rojos iluminados junto al río en Nagatoro"
            },
            {
                "w": 67,
                "home": "Cena del 'Día de la Buena Pareja' en Japón (11月22日 — いい夫婦の日 / Ii Fufu no Hi): regalarle un ramo de rosas + filete Tenderloin 300g hecho por ti",
                "out": "Feria Tori-no-Ichi en el Santuario Otori de Asakusa (Taito-ku): comprar juntos un rastrillo de bambú de la fortuna (Kumade) para atraer prosperidad al hogar",
                "geek": "Noche de maratón de su saga favorita de videojuegos: rejugar las mejores escenas de Kingdom Hearts I, II y III",
                "pref": "[Prefectura de Kanagawa · Montaña Oyama (Isehara)] Subir en funicular al Santuario Oyama Afuri para ver las hojas rojas de otoño y toda la costa de Shonan desde arriba"
            },
            {
                "w": 68,
                "home": "Noche de estofado de res japonés (Beef Stew estilo Yoshoku cocinado a fuego lento por 3 horas con trozos gigantes de carne tierna)",
                "out": "Paseo por el campus histórico de la Universidad de Tokio (Hongo, en Bunkyo-ku) bajo el gran Ginkgo centenario y el estanque Sanshiro",
                "geek": "Crear juntos en PC stickers personalizados de LINE con dibujos de sus 2 gatitos, las 2 chinchillas y ustedes dos para usar en su chat diario",
                "pref": "[Prefectura de Chiba · Valle de Yoro (Yoro Keikoku)] El lugar de otoño más tardío de Kanto: cascada Awamata y senderos de hojas rojas a finales de noviembre"
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
                "out": "Iluminación 'Ao no Dokutsu' (La Cueva Azul en Shibuya/Yoyogi) o iluminación de invierno de Omotesando bajo los árboles zelkova",
                "geek": "Visitar la exposición de invierno de Akihabara UDX / Belle Salle y comprar figuras navideñas para su estantería",
                "pref": "[Prefectura de Shizuoka · Gotemba Tokinosumika] Túnel de luces de invierno gigantes con vista a la silueta del Monte Fuji al atardecer"
            },
            {
                "w": 70,
                "home": "Taller de coronas navideñas estilo japonés (Shimenawa moderno con flores secas y listones de Asakusabashi) + cena de carne asada",
                "out": "Mercado de Navidad de Yokohama Red Brick Warehouse (Akarenga) o Tokyo Skytree Town viendo la iluminación navideña desde abajo",
                "geek": "Noche de juego cooperativo de invierno (Overcooked! All You Can Eat / Pikmin 4) en la Switch 2 riéndose sin parar",
                "pref": "[Prefectura de Tochigi · Tobu World Square y Kinugawa] Ver las 102 maravillas del mundo en miniatura iluminadas en invierno"
            },
            {
                "w": 71,
                "home": "🎄 Cena de Segunda Navidad en Casa: Filete Wellington / Roast Beef de Tenderloin hecho por ti + pastel de fresas Amaou de Fukuoka",
                "out": "Concierto de cuerdas a la luz de las velas (Candlelight Concert de música de Joe Hisaishi / Studio Ghibli) en Tokio",
                "geek": "Intercambio de regalos frikis de Navidad: edición coleccionista de su juego/artbook más deseado envuelto con tela Furoshiki hecha por ella",
                "pref": "[Prefectura de Kanagawa · Hakone Ashinoko y Museo del Principito / Venetian Glass Museum] Árboles de cristal de Murano brillando al sol de invierno en Hakone"
            },
            {
                "w": 72,
                "home": "Nochevieja 2028 en casa: cena de filetes de Wagyu + Toshikoshi Soba y agradecer juntos por el año de su boda y tu 5–0",
                "out": "Desfile de los Zorros de Oji (Oji Kitsune no Gyoretsu) o visita tranquila de fin de año al Santuario Meiji",
                "geek": "Ver el resumen anual de sus horas jugadas en PlayStation Wrap-Up y Nintendo Switch Year in Review abrazados con los gatos",
                "pref": "[Prefectura de Gunma · Shima Onsen] El pueblo termal que inspiró 'El Viaje de Chihiro' (Sekizenkan Ryokan con su puente rojo) para un baño de día"
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
                "out": "Ruta de los Siete Dioses de la Fortuna de Yanaka o Nihombashi (Shichifukujin Meguri): paseo suave coleccionando los sellos Goshuin en el libro de あやめ",
                "geek": "Tarde en Akihabara estrenando su presupuesto de Año Nuevo en materiales de costura pro y periféricos blancos para su setup",
                "pref": "[Prefectura de Tochigi · Yunishigawa Onsen (Kamakura Festival)] Ver cientos de pequeños iglús de nieve iluminados con velas por la noche junto al río nevado"
            },
            {
                "w": 74,
                "home": "Noche de Chanko Nabe hiper-proteico (la olla de los luchadores de sumo de nuestro barrio vecino Ryogoku, hecha con carne de res, pollo y verduras)",
                "out": "Asistir una tarde al Torneo de Sumo de Enero (Hatsu Basho) en el Ryogoku Kokugikan (a 1 estación de Asakusabashi) desde asientos cómodos",
                "geek": "Jugar Street Fighter 6 / Tekken 8 en modo divertido (con controles modernos para que あやめ te gane y celebre)",
                "pref": "[Prefectura de Yamanashi · Lago Saiko Iyashi no Sato Nenba] Aldea tradicional de techos de paja frente al Monte Fuji nevado donde pueden vestirse de samurái y kimono"
            },
            {
                "w": 75,
                "home": "Taller de velas aromáticas de cera de soya en casa: hacer velas con aroma a lavanda y vainilla para el ritual de las 22:00 hrs",
                "out": "Jardín de Peonías de Invierno (Fuyu Botan) cubiertas con sombreritos de paja para la nieve en el Santuario Ueno Toshogu",
                "geek": "Visitar el Café Pokémon (Nihombashi Takashimaya, a 5 min en tren por la línea Asakusa desde casa)",
                "pref": "[Prefectura de Nagano · Parque de los Monos de Nieve de Jigokudani (Shibu Onsen)] Ver a los macacos japoneses bañándose felices en aguas termales rodeados de nieve"
            },
            {
                "w": 76,
                "home": "Noche de filetes al estilo Steak Au Poivre (con costra de pimienta suave) y papas gratinadas hechas al horno",
                "out": "Museo de Artesanía Tradicional de Edo Taito (en Asakusa) y merienda de Taiyaki recién horneado relleno de crema pastelera",
                "geek": "Noche de diseño del cuarto de costura y gaming que tendrá あやめ en la futura casa 二世帯住宅 de Kanagawa usando software 3D",
                "pref": "[Prefectura de Chiba · Kamogawa y Recolección de Fresas (Ichigo-gari)] Invernaderos tibios en Chiba para comer fresas recién cortadas ilimitadas en enero"
            }
        ]
    },
    {
        "id": "2029-02",
        "title": "Febrero 2029 — ❄️ Invierno 6: Ciruelos en Flor, Chocolate Caliente y 1 Año de tu Debut",
        "season": "invierno",
        "season_label": "❄️ Invierno (冬)",
        "phase_note": "Febrero 2029 · Primer aniversario de tu Debut en MMA en Japón",
        "weeks": [
            {
                "w": 77,
                "home": "Cena de aniversario de tu Debut en MMA: recrear tu banquete post-pelea (Filete Tenderloin 300g + Wagyu Burger) viendo las fotos de aquel día",
                "out": "Festival del Ciruelo de Hanegi Park (Setagaya): caminar entre 650 ciruelos rojos y blancos en flor con aroma dulce de invierno",
                "geek": "Tarde en Ikebukuro visitando el Planetario 'Manten' en Sunshine City acostados en los asientos 'Nube (Kumo Seat)' blancos y esponjosos",
                "pref": "[Prefectura de Shizuoka · Atami Baien (Jardín de Ciruelos de Atami)] El jardín de ciruelos más temprano de Japón junto con aguas termales frente al mar"
            },
            {
                "w": 78,
                "home": "Cena de San Valentín 2029 en casa: Fondue de chocolate oscuro sin azúcar con fresas, plátano y malvaviscos después de cenar filete Sirloin",
                "out": "Paseo romántico por Yebisu Garden Place iluminado y el mirador gratuito del piso 38 con vista a la Torre de Tokio",
                "geek": "Jugar juntos el nuevo lanzamiento de Square Enix / Kingdom Hearts / Final Fantasy en la PS5 Pro",
                "pref": "[Prefectura de Kanagawa · Soga Plum Grove (Odawara)] 35,000 ciruelos blancos en flor con el Monte Fuji nevado de fondo"
            },
            {
                "w": 79,
                "home": "Taller de marroquinería básica en casa: hacer dos porta-tarjetas Suica de cuero genuino comprado en las tiendas de piel de Asakusabashi",
                "out": "Visita al Acuario de Shinagawa o Parque Kasai Rinkai (con la segunda rueda de la fortuna más grande de Japón frente a la bahía)",
                "geek": "Ir a Akihabara Gachapon Hall (500 máquinas de cápsulas) con ¥5,000 en monedas de ¥100 para sacar miniaturas para su escritorio",
                "pref": "[Prefectura de Saitama · Santuario Mitsumine (Chichibu)] Santuario místico en la cima de la montaña entre cedros gigantes centenarios"
            },
            {
                "w": 80,
                "home": "Noche de Teppanyaki de mar y tierra (Surf & Turf): Filete Tenderloin 250g + vieiras gigantes de Hokkaido (Hotate) a la mantequilla",
                "out": "Paseo por el barrio retro de Shibamata (Katsushika-ku): calle tradicional Taishakuten Sando y cruzar el río Edo en la última barca tradicional Yagiri-no-Watashi",
                "geek": "Noche de karaoke privado para dos (Big Echo / Pasela en Akihabara) cantando openings de anime, Utada Hikaru (Kingdom Hearts) y canciones de Blue Archive",
                "pref": "[Prefectura de Ibaraki · Jardín Botánico de Tsukuba y Monte Tsukuba] Subir en teleférico al pico doble del Monte Tsukuba viendo toda la llanura de Kanto"
            }
        ]
    },
    # ==================== PRIMAVERA 2029 ====================
    {
        "id": "2029-03",
        "title": "Marzo 2029 — 🌸 Primavera 6: Tercer Año de Cerezos y Arquitectos en Kanagawa",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Marzo 2029 · Primavera radiante y avances concretos para la casa 二世帯住宅",
        "weeks": [
            {
                "w": 81,
                "home": "Cena de Hinamatsuri 2029: filete de res cortado en dados sobre arroz de sushi decorado con huevo en tiras y flores comestibles",
                "out": "Paseo de cerezos tempranos (Kanzakura) en el Parque Ueno y visita al Museo Nacional de Tokio (edificio Honkan)",
                "geek": "Tarde de pintura de miniaturas / figuras garage kit en el taller de casa con aerógrafo/pinceles finos",
                "pref": "[Prefectura de Kanagawa · Visita a Showrooms de Casas 二世帯住宅 (Housing Gallery en Yokohama/Totsuka)] Ver casas modelo reales de dos generaciones para el retiro de 千秋-san"
            },
            {
                "w": 82,
                "home": "Cena de White Day 2029: regalarle un conjunto de sedas de Kioto para su colección + filete Chateaubriand hecho en casa",
                "out": "Caminata bajo los cerezos llorones (Shidarezakura) iluminados del Jardín Rikugien",
                "geek": "Ir a AnimeJapan 2029 en Tokyo Big Sight para ver los stands oficiales de Blue Archive, Fate y Chainsaw Man",
                "pref": "[Prefectura de Chiba · Parque Shimizu y Castillo de Sekiyado] Túneles de cerezos y laberinto de jardín en Noda"
            },
            {
                "w": 83,
                "home": "Noche de picnic interior con vista al balcón: brochetas de filete, fresas y té de flor de cerezo (Sakura-cha)",
                "out": "Recorrido en barco abierto por el río Kanda y el río Nihombashi pasando por debajo de los puentes históricos cubiertos de cerezos",
                "geek": "Maratón de películas de anime de primavera ('La Chica que Saltaba a Través del Tiempo' / 'Palabras que Burbujean como un Refresco')",
                "pref": "[Prefectura de Saitama · Gongendo Tsutsumi (Satte)] El dique de 1 km con 1,000 cerezos rosas arriba y una alfombra amarilla infinita de flores de colza abajo"
            },
            {
                "w": 84,
                "home": "Cena de filete Ribeye con mantequilla compuesta de hierbas hecha en casa + sesión de cepillado y mimos a los gatos y chinchillas",
                "out": "Paseo de Hanami por el Cementerio Histórico de Yanaka y las cafeterías en casas antiguas de madera de Ueno Sakuragi Atari",
                "geek": "Sesión cooperativa de construir su isla/casa perfecta en Animal Crossing / Dragon Quest Builders / juego cozy en Switch 2",
                "pref": "[Prefectura de Yamanashi · Castillo de Kofu (Maizuru Castle Park)] Cerezos rodeando las murallas del castillo con los Alpes del Sur nevados al fondo"
            }
        ]
    },
    {
        "id": "2029-04",
        "title": "Abril 2029 — 🌸 Primavera 7: Pétalos sobre el Agua, Tulanes y Brisa de Abril",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Abril 2029 · Mes 22 activo de citas únicas",
        "weeks": [
            {
                "w": 85,
                "home": "Noche de Tataki de filete de res con ajo crujiente hecho en casa + postre de gelatina de cristal japonesa (Mizu Shingen Mochi)",
                "out": "Ver el fenómeno 'Hanaikada' (balsas de pétalos rosas cubriendo el agua por completo) en el río Shakujii o foso de Chidorigafuchi",
                "geek": "Visitar el Museo de la Animación / estudio en Mitaka-Kichijoji y tiendas de papelería de personajes en Kichijoji",
                "pref": "[Prefectura de Chiba · Sakura Furusato Square] Ver el molino de viento holandés real rodeado de 700,000 tulipanes de todos los colores en Sakura, Chiba"
            },
            {
                "w": 86,
                "home": "Taller de confección de cojines y camitas nuevas para los 2 gatitos usando telas acolchadas en la máquina JUKI de あやめ",
                "out": "Festival de las Azaleas (Tsutsuji Matsuri) en el Santuario Nezu y almuerzo de carne en Yanesen",
                "geek": "Tarde de realidad virtual / arcade inmersivo en RED° TOKYO TOWER (el parque de esports y gaming dentro de la Torre de Tokio)",
                "pref": "[Prefectura de Gunma · Castillo de Takasaki y Templo Daruma de Shorinzan] Pintar juntos los ojos de un Daruma tradicional pidiendo un deseo familiar"
            },
            {
                "w": 87,
                "home": "Cena de filetes Striploin al estilo chimichurri fresco hecho en casa + noche de masajes con aceite tibio",
                "out": "Paseo por los Jardines Hama-rikyu viendo los campos de flores de primavera frente a los rascacielos de Shiodome",
                "geek": "Competencia amistosa de Mario Party / Overcooked con premios de vales hechos a mano ('Vale por 1 tarde entera en Nippori')",
                "pref": "[Prefectura de Tochigi · Mashiko (Pueblo de la Cerámica)] Recorrer las galerías de alfarería tradicional de Mashiko y elegir platos artesanales para sus filetes"
            },
            {
                "w": 88,
                "home": "Noche de degustación de tés japoneses sin teína (Mugicha, Sobacha, Kuromamecha de frijol negro) + cena de Roast Beef",
                "out": "Visitar el Jardín de Glicinas de Kameido Tenjin al atardecer viendo el Tokyo Skytree enmarcado entre las flores moradas",
                "geek": "Revisión y actualización estética de ambos setups (limpieza profunda, cambio de fondos de pantalla animados en Wallpaper Engine de Blue Archive y KH)",
                "pref": "[Prefectura de Kanagawa · Kurihamahana no Kuni (Yokosuka)] Caminar entre un millón de amapolas e हिमालय azules frente al mar en Yokosuka"
            }
        ]
    },
    {
        "id": "2029-05",
        "title": "Mayo 2029 — 🌸 Primavera 8: Primer Aniversario de Bodas y Rosas de Mayo",
        "season": "primavera",
        "season_label": "🌸 Primavera (春)",
        "phase_note": "Mayo 2029 · ¡1er Aniversario de Bodas (Bodas de Papel / Algodón)!",
        "weeks": [
            {
                "w": 89,
                "home": "💍 ¡Cena de 1er Aniversario de Bodas (Bodas de Papel)! Entregarle una carta de amor escrita en papel japonés Washi artesanal + Chateaubriand Wagyu en casa",
                "out": "Paseo de aniversario por los Jardines del Hotel New Otani Tokyo (jardín japonés de 400 años con cascada y puente rojo) y cena de cortes premium sin alcohol",
                "geek": "Sesión de fotos conmemorativa del 1er aniversario recreando la primera foto que se tomaron juntos en Asakusabashi",
                "pref": "[Prefectura de Shizuoka · Península de Izu (Shimoda)] Tren panorámico Saphir Odoriko en asientos privados hacia las playas de arena blanca y aguas turquesa de Shimoda"
            },
            {
                "w": 90,
                "home": "Taller de prensado de flores naturales (Oshibana): prensar las flores de su ramo de aniversario para enmarcarlas en cristal",
                "out": "Festival de las Rosas en el Jardín Botánico Jindai (Chofu) y paseo por las calles antiguas alrededor del Templo Jindaiji",
                "geek": "Visitar las tiendas de figuras y coleccionables de Akihabara para elegir la figura de aniversario del año",
                "pref": "[Prefectura de Yamanashi · Lago Motosu y Fuji Shibazakura Festival] Ver los 500,000 musgos rosas en flor a los pies del Monte Fuji"
            },
            {
                "w": 91,
                "home": "Cena de Hamburguesas Wagyu rellenas de queso gouda hechas por ti + tarde de sol en el balcón con los gatitos",
                "out": "Paseo en kayak doble tranquilo por los canales de Tokio pasando bajo el Tokyo Skytree al atardecer",
                "geek": "Noche de música y nostalgia: escuchar todos los temas de Dearly Beloved (Kingdom Hearts) desde KH1 hasta KH3 mientras platican de sus sueños",
                "pref": "[Prefectura de Saitama · Jardín de Rosas de Ina y Pueblo Bonsai de Omiya] Caminar entre arcos de rosas de mayo"
            },
            {
                "w": 92,
                "home": "Noche de brochetas de filete Tenderloin y pimientos asados + sesión de spa de manos para あやめ (después de sus tardes de costura)",
                "out": "Visita al Museo de Arte Teien de Tokio (antigua residencia del Príncipe Asaka en estilo Art Déco en Meguro) y sus jardines verdes",
                "geek": "Tarde de armado de un diorama japonés en miniatura (Book Nook de callejón de Tokio con luz LED) para poner entre sus mangas",
                "pref": "[Prefectura de Kanagawa · Isla de Sarushima (Yokosuka)] Barco de 10 minutos a la isla deshabitada cubierta de bosque y ladrillos cubiertos de musgo estilo Laputa (El Castillo en el Cielo)"
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
                "out": "Camino de las Hortensias de Asukayama Park (subiendo en el pequeño monorriel gratuito Asukayama Park Monorail en Kita-ku)",
                "geek": "Tarde en Nakano / Akihabara buscando ediciones retro de Kingdom Hearts para Game Boy Advance / PSP para su colección histórica",
                "pref": "[Prefectura de Chiba · Templo Hondoji (Matsudo)] El 'Templo de las Hortensias y los Arces' de Chiba con su pagoda de 5 pisos entre 50,000 hortensias"
            },
            {
                "w": 94,
                "home": "Taller de creación de sellos japoneses (Hanko / Gomu-in) grabados en goma con las caritas de sus gatitos y chinchillas",
                "out": "Visita al Museo de la Espada Japonesa (Japanese Sword Museum en Ryogoku, a 1 estación de casa) y los jardines Kyu-Yasuda",
                "geek": "Noche de torneo cooperativo en PS5 Pro y Switch 2 celebrando todos los juegos completados juntos en estos 2 años",
                "pref": "[Prefectura de Tochigi · Ohirasan Shrine (Tochigi City)] Subir el sendero de las 4,000 hortensias y pasear en barca por el río Uzuma en el pueblo histórico de Kura no Machi"
            },
            {
                "w": 95,
                "home": "Cena de filete Sirloin en costra de ajo tostado + preparar juntos parfaits caseros de arándanos, fresas y crema batida",
                "out": "Crucero nocturno por la bahía de Tokio viendo el Rainbow Bridge iluminado y la brisa cálida de junio",
                "geek": "Exposición de vestuario y diseño textil del Japón moderno / anime en Tokio para inspirar los nuevos diseños de あやめ",
                "pref": "[Prefectura de Kanagawa · Hakone Glass Forest y Lago Ashi] Pasear bajo los árboles de cristal que brillan con la luz de junio y vista al lago"
            },
            {
                "w": 96,
                "home": "👑 ¡CITA #384 (FINAL DEL CALENDARIO DE 2 AÑOS)! Banquete Real en casa: Chateaubriand 350g, brindis sin alcohol y abrir el álbum con los recuerdos de las 96 semanas",
                "out": "Paseo al atardecer desde nuestra puerta en Yanagibashi por toda la ribera del río Sumida hasta Asakusa recordando cómo empezó el Imperio",
                "geek": "Ceremonia de graduación gamer/otaku en casa: encender las luces de la vitrina con tus trofeos 5–0 de MMA y los kimonos diseñados por あやめ",
                "pref": "[Prefectura de Kanagawa · Terreno/Zona de su futura Casa 二世帯住宅 con 千秋-san] Paseo familiar con 千秋-san celebrando los 2 años de felicidad y el futuro hogar de las dos generaciones"
            }
        ]
    }
]


def main():
    # Verify uniqueness of all 384 dates
    active_weeks = [w for m in MONTHS_DATA if m["season"] != "campamento" for w in m["weeks"]]
    assert len(active_weeks) == 96, f"Expected 96 active weeks, got {len(active_weeks)}"

    js_content = f"""/**
 * Atlas del Imperio — Calendario Maestro de 2 Años de Citas Únicas para あやめ
 * 24 Meses Activos en Japón (96 Semanas = 384 Citas 100% Únicas) + Pausa de 3 Meses en Tailandia.
 * Cada semana incluye:
 *   1. 🏠 Cita en Casa (Miércoles 19:00–21:15)
 *   2. 🎮 Cita Friki Juntos (Jueves 19:00–21:15)
 *   3. 🌿 Actividad Afuera en Tokio (Viernes 17:45–21:00)
 *   4. 🚅 Escapada a Prefectura Fuera de Tokio (Fin de semana · regreso antes de 21:00 para dormir 22:30)
 */
(function () {{
  const MONTHS_DATA = {json.dumps(MONTHS_DATA, ensure_ascii=False, indent=2)};

  function renderAyameCalendar() {{
    const container = document.getElementById("ayame-dates-container");
    if (!container) return;

    const savedChecks = JSON.parse(localStorage.getItem("imperio_ayame_dates_v1") || "{{}}");

    let activeSeason = "all";
    let searchQuery = "";

    function updateView() {{
      const listEl = document.getElementById("ayame-months-list");
      if (!listEl) return;

      const q = searchQuery.trim().toLowerCase();
      let html = "";
      let visibleWeeks = 0;

      for (const m of MONTHS_DATA) {{
        if (activeSeason !== "all" && m.season !== activeSeason) continue;

        const filteredWeeks = m.weeks.filter((w) => {{
          if (!q) return true;
          return (
            m.title.toLowerCase().includes(q) ||
            w.home.toLowerCase().includes(q) ||
            w.out.toLowerCase().includes(q) ||
            w.geek.toLowerCase().includes(q) ||
            w.pref.toLowerCase().includes(q)
          );
        }});

        if (filteredWeeks.length === 0) continue;
        visibleWeeks += filteredWeeks.length;

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
            <div class="room-header" onclick="this.nextElementSibling.classList.toggle('open'); this.nextElementSibling.style.maxHeight = this.nextElementSibling.classList.contains('open') ? '3000px' : null;" style="cursor:pointer;">
              <div class="room-title" style="font-size:1rem;">${{m.title}}</div>
              <div class="room-subtotal" style="font-size:0.8rem; color:${{borderColor}};">${{m.season_label}} · ${{filteredWeeks.length}} sem</div>
            </div>
            <div class="room-content open" style="max-height:3000px; padding:0.9rem 1.1rem;">
              <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:0.8rem;">📌 <strong>Contexto de Fase:</strong> ${{m.phase_note}}</p>
              <div style="overflow-x:auto;">
                <table style="width:100%; border-collapse:collapse; font-size:0.82rem;">
                  <thead>
                    <tr style="background:rgba(255,255,255,0.04);">
                      <th style="width:70px;">Sem</th>
                      <th style="width:24%;">🏠 1. Cita en Casa<br><small style="color:#9ca3af;">(Mié 19:00–21:15)</small></th>
                      <th style="width:24%;">🎮 2. Cita Friki Juntos<br><small style="color:#9ca3af;">(Jue 19:00–21:15)</small></th>
                      <th style="width:24%;">🌿 3. Actividad Afuera Tokio<br><small style="color:#9ca3af;">(Vie 17:45–21:00)</small></th>
                      <th style="width:28%;">🚅 4. Escapada a Prefectura<br><small style="color:#9ca3af;">(Fin de Sem · regreso &lt;21:00)</small></th>
                    </tr>
                  </thead>
                  <tbody>
        `;

        for (const w of filteredWeeks) {{
          const key = m.id + "-w" + w.w;
          const checked = savedChecks[key] ? "checked" : "";
          html += `
            <tr>
              <td style="font-weight:bold; text-align:center;">
                <label style="cursor:pointer; display:flex; flex-direction:column; align-items:center; gap:4px;">
                  <span>Sem ${{w.w}}</span>
                  <input type="checkbox" data-date-key="${{key}}" ${{checked}} style="accent-color:#f472b6; width:16px; height:16px; cursor:pointer;" title="Marcar semana completada">
                </label>
              </td>
              <td>${{w.home}}</td>
              <td>${{w.geek}}</td>
              <td>${{w.out}}</td>
              <td style="color:#fcd34d;">${{w.pref}}</td>
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
        }});
      }});
    }}

    container.innerHTML = `
      <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:space-between; margin-bottom:1.2rem; background:rgba(244,114,182,0.07); border:1px solid rgba(244,114,182,0.3); padding:12px 16px; border-radius:10px;">
        <div style="display:flex; flex-wrap:wrap; gap:6px;">
          <button class="plan-tab ayame-filter-btn active" data-season="all">🌸🎆🍁❄️ Todas las Estaciones (24 Meses Activos · 384 Citas)</button>
          <button class="plan-tab ayame-filter-btn" data-season="primavera">🌸 Primavera (春)</button>
          <button class="plan-tab ayame-filter-btn" data-season="verano">🎆 Verano (夏)</button>
          <button class="plan-tab ayame-filter-btn" data-season="otono">🍁 Otoño (秋)</button>
          <button class="plan-tab ayame-filter-btn" data-season="invierno">❄️ Invierno (冬)</button>
          <button class="plan-tab ayame-filter-btn" data-season="campamento">🥊 Pausa Tailandia (90d)</button>
        </div>
        <input id="ayame-date-search" type="search" placeholder="🔍 Buscar prefectura, juego, actividad (ej. Kamakura, Kingdom Hearts, Onsen)..." style="background:rgba(0,0,0,0.45); border:1px solid rgba(255,255,255,0.2); color:#fff; padding:6px 12px; border-radius:6px; min-width:290px; font-size:0.82rem;">
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
    print(f"[OK] Generated {OUT_JS.name} with {len(active_weeks)} active weeks ({len(active_weeks)*4} unique dates) + Thailand 90d protocol!")


if __name__ == "__main__":
    main()
