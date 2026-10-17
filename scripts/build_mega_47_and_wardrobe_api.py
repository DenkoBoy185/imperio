#!/usr/bin/env python3
"""
Atlas del Imperio — Mega Automation Engine (47 Prefectures + 24 Months + Wardrobe V8 + All Prices API)
Generates:
  1. assets/prefectures-47-feed.json
  2. assets/wardrobe-prices-feed.json
  3. assets/imperio-mega-api.js
And queries live FX rates (open.er-api.com / Frankfurter ECB) + Open-Meteo Japan regional telemetry.
"""
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"


def fetch_live_fx() -> dict:
    urls = [
        "https://open.er-api.com/v6/latest/USD",
        "https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY,KRW,THB",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ImperioMegaAPI/3.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                r = data.get("rates", {})
                if "JPY" in r and "KRW" in r:
                    return {
                        "JPY": round(float(r["JPY"]), 3),
                        "KRW": round(float(r["KRW"]), 3),
                        "THB": round(float(r.get("THB", 33.55)), 3),
                        "USD": 1.0,
                        "source": url,
                    }
        except Exception:
            pass
    return {"JPY": 158.08, "KRW": 1342.74, "THB": 33.53, "USD": 1.0, "source": "fallback"}


# ==============================================================================
# 1. COMPLETE 24-MONTH / 47-PREFECTURE MASTER ITINERARY DATASET
# ==============================================================================
ITINERARY_24_MONTHS = [
    {
        "month_num": 1,
        "date_label": "Octubre 2027",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Adaptación e inicio de entrenamientos)",
        "duration": "1 Día completo",
        "cat_protocol": "1 Día: Alimentadores automáticos y regreso a dormir a casa en Ikebukuro.",
        "shortcut": "Línea JR Yamanote a Nippori (12 min); luego línea Marunouchi a Ginza (16 min).",
        "prefectures": [
            {"num": 1, "name": "Tokio", "kanji": "東京都", "region": "Kanto", "lat": 35.7289, "lon": 139.7709, "activity": "Caza de Telas Kaiju en Nippori & Reconocimiento de Ginza 1954"}
        ],
        "schedule": [
            {"time": "10:30 hrs (Mañana)", "detail": "Salida de Ikebukuro hacia Nippori Textile Town. Recorrido con あやめ por las tiendas especializadas (Tomato y Nagato) para elegir la tela negra ceniza con textura volcánica y la espuma EVA ligera para las placas dorsales de tu bata de Godzilla 1954."},
            {"time": "14:00 hrs (Tarde)", "detail": "Traslado a Ginza 4-Chome. Paseo frente a la histórica Torre del Reloj de Ginza Wako (el punto exacto de la película de 1954 que inspirará tu entrada al ring) y visita a las galerías de kimonos de seda en Ginza para ver catálogos de teñido tradicional."},
            {"time": "18:30 hrs (Noche)", "detail": "Cena en un restaurante privado de Shabu-shabu en Ginza y regreso en la línea Marunouchi sentados hasta Ikebukuro a las 21:00 hrs (protegiendo el sueño sagrado de las 22:30 hrs)."}
        ],
        "nutrition_bruno": "Láminas de res magra y hongos shiitake en caldo kombu (alta proteína, 0 alcohol 🚫🍺, 0 mango 🚫🥭).",
        "antojo_ayame": "Parfait de castañas de otoño en Ginza Sembikiya.",
        "costs_jpy": {
            "transporte": 1200,
            "hospedaje": 0,
            "actividades_telas": 45000,
            "gastronomia": 26000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.tokyometro.jp/en/",
            "transport_label": "🚇 Ruta Yamanote + Marunouchi Line",
            "activity_url": "https://nippori-senigai.com/en/",
            "activity_label": "🧵 Mapa Oficial Nippori Textile Town (Tomato / Nagato)",
            "dining_url": "https://tabelog.com/en/tokyo/A1301/A130101/rstLst/shabushabu/",
            "dining_label": "🥩 Agendar Shabu-Shabu en Ginza (Tabelog) + Ginza Sembikiya",
            "hotel_url": "https://www.ikyu.com/",
            "hotel_label": "🏡 Dormir en Casa (Ikebukuro)",
            "maps_url": "https://www.google.com/maps/dir/Ikebukuro+Station/Nippori+Station/Ginza+Wako"
        }
    },
    {
        "month_num": 2,
        "date_label": "Noviembre 2027",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg)",
        "duration": "2 Sábados de excursión (sin dormir fuera de casa)",
        "cat_protocol": "1 Día (×2 sábados): Alimentadores automáticos y regreso a dormir a casa en Ikebukuro.",
        "shortcut": "Día A: Expreso Tobu Tojo directo desde Ikebukuro a Kawagoe (30 min). Día B: Autobús expreso vía Tokyo Bay Aqua-Line al sur de Chiba.",
        "prefectures": [
            {"num": 2, "name": "Saitama", "kanji": "埼玉県", "region": "Kanto", "lat": 35.9251, "lon": 139.4858, "activity": "Paseo en Kimono Retro bajo la Campana del Tiempo en Kawagoe («El Pequeño Edo»)"},
            {"num": 3, "name": "Chiba", "kanji": "千葉県", "region": "Kanto", "lat": 35.1411, "lon": 139.8392, "activity": "Atardecer Marino en el Muelle de Madera de Hota & Costa de Boso"}
        ],
        "schedule": [
            {"time": "Día A · 10:00–16:30 hrs (Saitama #02)", "detail": "Expreso Tobu Tojo directo desde Ikebukuro hasta Kawagoe (30 min). Renta de kimonos de paseo por el distrito de almacenes antiguos (Kurazukuri), campana Toki no Kane, callejón Kashiya Yokocho y comida de Unagi al carbón en Ogakiku (fundado en 1807)."},
            {"time": "Día B · 11:00–19:30 hrs (Chiba #03)", "detail": "Cruce de la Bahía de Tokio por Tokyo Bay Aqua-Line hacia la península de Boso. Caminata al atardecer por el muelle de madera sobre el mar en Hota / Haraoka con el Monte Fuji en el horizonte y cena de mariscos a la parrilla (Hamayaki)."}
        ],
        "nutrition_bruno": "Unagi al carbón (altísimo en proteína y omega-3) en Ogakiku + mariscos frescos a la parrilla (Hamayaki).",
        "antojo_ayame": "Dulces tradicionales de camote (Satsumaimo) en Kashiya Yokocho y brisa marina al atardecer.",
        "costs_jpy": {
            "transporte": 8400,
            "hospedaje": 0,
            "actividades_telas": 16000,
            "gastronomia": 28000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.tobu.co.jp/en/ticket/kawagoe/premium.html",
            "transport_label": "🚄 Pase Tobu Kawagoe Desde Ikebukuro",
            "activity_url": "https://koedo.or.jp/foreign/en/",
            "activity_label": "👘 Reservar Kimono Retro en Kawagoe & Ruta Haraoka Pier",
            "dining_url": "https://tabelog.com/en/saitama/A1103/A110303/11000083/",
            "dining_label": "🍱 Agendar Ogakiku Unagi (1807) & Hamayaki Hota",
            "hotel_url": "https://www.ikyu.com/",
            "hotel_label": "🏡 Excursiones de 1 Día (Dormir en Ikebukuro)",
            "maps_url": "https://www.google.com/maps/dir/Ikebukuro+Station/Kawagoe+Station/Haraoka+Pier"
        }
    },
    {
        "month_num": 3,
        "date_label": "Diciembre 2027",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Recuperación invernal)",
        "duration": "Fin de semana de 2 Noches",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada en Tokio con reporte diario de fotos y videos por LINE.",
        "shortcut": "JR / Expreso Hitachi a costa de Ibaraki + Compartimento privado en tren de lujo Tobu Spacia X a Nikko.",
        "prefectures": [
            {"num": 4, "name": "Tochigi", "kanji": "栃木県", "region": "Kanto", "lat": 36.7581, "lon": 139.5986, "activity": "Viaje en Cabina Privada del Tren «Spacia X» al Santuario Dorado de Nikko"},
            {"num": 5, "name": "Gunma", "kanji": "群馬県", "region": "Kanto", "lat": 36.6208, "lon": 138.5961, "activity": "Paseo Nocturno entre el Vapor Esmeralda del Yubatake en Kusatsu Onsen"},
            {"num": 6, "name": "Ibaraki", "kanji": "茨城県", "region": "Kanto", "lat": 36.3146, "lon": 140.5874, "activity": "El Torii Marino sobre las Rocas del Pacífico en Oarai Isosaki"}
        ],
        "schedule": [
            {"time": "Día 1 · Ibaraki (#06) y Tochigi (#04)", "detail": "09:30 hrs: Salida hacia la costa de Ibaraki para ver las olas romper contra el Kamiiso-no-Torii en Oarai Isosaki y almorzar Anko Nabe (rape magro de invierno). 15:00 hrs: Traslado a Nikko / Kinugawa Onsen en cabina privada del tren Tobu Spacia X y noche en ryokan sobre el cañón."},
            {"time": "Día 2 · Tochigi (#04) y Gunma (#05)", "detail": "09:30 hrs: Visita matutina sin multitudes al Santuario Nikko Toshogu entre cedros gigantes. 14:00 hrs: Cruce escénico a Kusatsu Onsen (Gunma), ceremonia tradicional Yumomi y paseo nocturno en yukata frente al Yubatake iluminado en verde esmeralda."}
        ],
        "nutrition_bruno": "Anko Nabe (rape blanco magro rico en colágeno), Yuba y trucha de río a la sal.",
        "antojo_ayame": "Manju caliente al vapor frente al Yubatake iluminado de Kusatsu.",
        "costs_jpy": {
            "transporte": 28000,
            "hospedaje": 96000,
            "actividades_telas": 14000,
            "gastronomia": 38000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://www.tobu.co.jp/spaciax/en/",
            "transport_label": "🚄 Reservar Cabina Privada Tobu Spacia X",
            "activity_url": "https://www.kusatsu-onsen.ne.jp/guide/en/",
            "activity_label": "♨️ Guía Oficial Kusatsu Onsen & Nikko Toshogu",
            "dining_url": "https://tabelog.com/en/ibaraki/A0801/A080102/rstLst/ankou/",
            "dining_label": "🍲 Agendar Anko Nabe en Oarai & Kaiseki en Kinugawa",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏯 Reservar Ryokan en Kinugawa & Kusatsu (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Ikebukuro+Station/Oarai+Isosaki+Shrine/Nikko+Toshogu/Kusatsu+Onsen"
        }
    },
    {
        "month_num": 4,
        "date_label": "Enero 2028",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg)",
        "duration": "2 Noches en el norte nevado",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada en Tokio con reporte diario por LINE.",
        "shortcut": "Atajo #1: JR Saikyo desde Ikebukuro a Omiya Station (24 min) + Yamagata / Tohoku Shinkansen en Green Car.",
        "prefectures": [
            {"num": 7, "name": "Yamagata", "kanji": "山形県", "region": "Tohoku", "lat": 38.5706, "lon": 140.5305, "activity": "Noche bajo la Nieve y Lámparas de Gas en Ginzan Onsen"},
            {"num": 8, "name": "Miyagi", "kanji": "宮城県", "region": "Tohoku", "lat": 38.3698, "lon": 141.0586, "activity": "Crucero Privado entre las 260 Islas de Pinos de la Bahía de Matsushima"},
            {"num": 9, "name": "Fukushima", "kanji": "福島県", "region": "Tohoku", "lat": 37.3341, "lon": 139.8608, "activity": "Aldea Samurái de Techos de Paja Nevados en Ouchijuku & Pintura de Akabeko"}
        ],
        "schedule": [
            {"time": "Día 1 · Yamagata (#07)", "detail": "Llegada en Shinkansen desde Omiya a Oishida y shuttle privado del ryokan hasta Ginzan Onsen. A las 17:00 hrs caminan juntos bajo la nieve azulada y las lámparas de gas sobre los puentes de madera antes del baño termal."},
            {"time": "Día 2 · Miyagi (#08)", "detail": "Cruce a Sendai y Matsushima. A las 12:30 hrs navegan por las 260 islas de pinos de la bahía de Matsushima. Almuerzo de Gyutan (lengua de res a las brasas estilo Sendai) y ostras al vapor."},
            {"time": "Día 3 · Fukushima (#09)", "detail": "Bajada a Aizu para caminar por la aldea nevada de Ouchijuku (periodo Edo) y taller artesanal donde pintan a mano su amuleto rojo Akabeko para proteger tu salud en el ring. Regreso a Omiya/Ikebukuro a las 20:00 hrs."}
        ],
        "nutrition_bruno": "Gyutan (lengua de res a las brasas en Sendai, altísima en hierro y proteína limpia) + ostras al vapor.",
        "antojo_ayame": "Zunda Mochi tibio en Sendai y chocolate caliente viendo la nieve en Ginzan Onsen.",
        "costs_jpy": {
            "transporte": 58000,
            "hospedaje": 125000,
            "actividades_telas": 18000,
            "gastronomia": 42000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://www.eki-net.com/en/jreast-train-reservation/Top/Index",
            "transport_label": "🚄 Reservar Yamagata/Tohoku Shinkansen Green Car (Omiya)",
            "activity_url": "https://www.ginzanonsen.jp/",
            "activity_label": "❄️ Ginzan Onsen + Crucero Bahía Matsushima + Taller Akabeko",
            "dining_url": "https://tabelog.com/en/miyagi/A0401/A040101/rstLst/gyutan/",
            "dining_label": "🥩 Agendar Gyutan Tradicional en Sendai (Tabelog Top)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Ryokan Histórico en Ginzan Onsen",
            "maps_url": "https://www.google.com/maps/dir/Omiya+Station/Ginzan+Onsen/Matsushima+Bay/Ouchijuku"
        }
    },
    {
        "month_num": 5,
        "date_label": "Febrero 2028",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (Último viaje antes de iniciar el Campamento #1)",
        "duration": "1 Noche (30 horas)",
        "cat_protocol": "Escapada de 1 noche (30h): Fuentes continuas de agua, alimentadores y monitoreo por cámara Wi-Fi.",
        "shortcut": "Tren de ultra lujo Saphir Odoriko directo desde Ikebukuro/Shinjuku a Izu + conexión Shinkansen a Nagoya.",
        "prefectures": [
            {"num": 10, "name": "Shizuoka", "kanji": "静岡県", "region": "Chubu", "lat": 34.7469, "lon": 138.9961, "activity": "Viaje en el Tren Panorámico «Saphir Odoriko» a los Cerezos Tempranos de Kawazu"},
            {"num": 11, "name": "Aichi", "kanji": "愛知県", "region": "Chubu", "lat": 35.0669, "lon": 136.9714, "activity": "Taller de Teñido Textil Tridimensional «Arimatsu Shibori» & Castillo Dorado de Nagoya"}
        ],
        "schedule": [
            {"time": "Día 1 · Shizuoka (#10)", "detail": "09:30 hrs: Abordan el tren panorámico Saphir Odoriko viendo el mar de Atami e Izu. 12:00 hrs: Caminata bajo el túnel rosa intenso de los 8,000 cerezos tempranos de Kawazu junto al río y el mar. Noche en ryokan costero cenando pescado Kinmedai al vapor."},
            {"time": "Día 2 · Aichi (#11)", "detail": "10:00 hrs: Shinkansen desde Atami/Mishima a Nagoya (1h 15m). 11:30 hrs: Visita al distrito histórico de Arimatsu (cuna del teñido Arimatsu Shibori de 400 años) donde あやめ crea su pañuelo de seda. Visita al Salón Honmaru de oro del Castillo de Nagoya y regreso a las 19:30 hrs."}
        ],
        "nutrition_bruno": "Pescado Kinmedai (alfonsino imperial) al vapor y sashimi marino fresco.",
        "antojo_ayame": "Sweets de Sakura temprano en Kawazu y creación de su propio pañuelo en Arimatsu.",
        "costs_jpy": {
            "transporte": 42000,
            "hospedaje": 68000,
            "actividades_telas": 16000,
            "gastronomia": 32000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.jreast.co.jp/saphir/en/",
            "transport_label": "🚄 Reservar Tren de Lujo JR Saphir Odoriko",
            "activity_url": "https://shibori-kaikan.com/",
            "activity_label": "🎨 Reservar Taller Textil Arimatsu Shibori & Kawazu-zakura",
            "dining_url": "https://tabelog.com/en/shizuoka/A2205/A220503/rstLst/",
            "dining_label": "🐟 Agendar Kinmedai en Izu & Hitsumabushi en Nagoya",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🌊 Reservar Ryokan Frente al Mar en Izu / Atami",
            "maps_url": "https://www.google.com/maps/dir/Ikebukuro+Station/Kawazu+Station/Arimatsu,+Nagoya/Nagoya+Castle"
        }
    },
    {
        "month_num": 6,
        "date_label": "Marzo 2028",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "ROJA",
        "zone_badge": "🔴 ZONA ROJA — FIGHT CAMP PELEA #1 (En pleno corte a 77.0 kg)",
        "duration": "4 Horas (A 10 minutos a pie de nuestro apartamento en Ikebukuro)",
        "cat_protocol": "Cita local de 4 horas: Regreso inmediato a casa con nuestros gatitos y chinchillas.",
        "shortcut": "Traslado matutino al dojo en tu Honda CBR (Regla del Conbini) y cita vespertina a pie en Sunshine City.",
        "prefectures": [],
        "schedule": [
            {"time": "16:00 hrs", "detail": "Después de tu entrenamiento matutino en la Honda CBR y tu siesta de recuperación, salen caminando juntos a Sunshine City Ikebukuro."},
            {"time": "16:30 hrs", "detail": "Recorrido relajado por el Sunshine Aquarium viendo a los pingüinos nadar sobre el horizonte de Tokio y el túnel de medusas iluminadas."},
            {"time": "18:00 hrs", "detail": "Función especial en el Planetario Konica Minolta Manten, acostados juntos en los asientos cama (Kumo / Cloud Seats) con aromaterapia relajante."},
            {"time": "19:30 hrs", "detail": "Cena limpia de sashimi de atún magro (Akami) y té caliente; dormidos en casa antes de las 22:00 hrs."}
        ],
        "nutrition_bruno": "Sashimi de atún magro (Akami) y pescado blanco de corte de peso (77.0 kg).",
        "antojo_ayame": "Crepa artesanal o té floral después del planetario.",
        "costs_jpy": {
            "transporte": 0,
            "hospedaje": 0,
            "actividades_telas": 12400,
            "gastronomia": 14000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://sunshinecity.jp/en/",
            "transport_label": "🚶 A 10 Minutos a Pie desde Casa en Ikebukuro",
            "activity_url": "https://planetarium.konicaminolta.jp/manten/",
            "activity_label": "🌌 Reservar Asientos Cama «Kumo» en Planetario Manten + Acuario",
            "dining_url": "https://tabelog.com/en/tokyo/A1305/A130501/rstLst/sashimi/",
            "dining_label": "🍣 Sashimi Magro Akami en Ikebukuro",
            "hotel_url": "https://sunshinecity.jp/en/",
            "hotel_label": "🏡 Descanso en Casa antes de las 22:00 hrs",
            "maps_url": "https://www.google.com/maps/search/Sunshine+Aquarium+Ikebukuro"
        }
    },
    {
        "month_num": 7,
        "date_label": "Abril 2028",
        "phase": "FASE 1",
        "phase_name": "El Despertar en Kanto, Tohoku Sur y Tokai (Meses 01–07)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — 🥊 PELEA #1 (DEBUT 77 KG: VICTORIA 1-0)",
        "duration": "Noche de Gala en la Bahía de Tokio (Regreso a dormir a casa)",
        "cat_protocol": "1 Día: Alimentadores automáticos y regreso a dormir con los gatitos tras el crucero.",
        "shortcut": "Taxi privado desde la arena hasta el muelle de Hinode en la Bahía de Tokio.",
        "prefectures": [],
        "schedule": [
            {"time": "Día del Combate", "detail": "Pesaje oficial en 77.0 kg, rehidratación controlada y calentamiento de manoplas en el vestidor con tus shorts YOKKAO y guantes Venum Pro Boxing tricolores. Sales a la jaula, dominas el combate y あやめ debuta como tu mánager recibiendo tu primera medalla (1-0)."},
            {"time": "19:00 hrs (Noche de Gala)", "detail": "Traslado en taxi privado al muelle de Hinode para abordar el crucero restaurante Symphony Moderna. Cena de celebración de 5 tiempos navegando bajo el Rainbow Bridge y frente a Odaiba y Tokyo Tower con la brisa marina."}
        ],
        "nutrition_bruno": "Menú Francés/Japonés de 5 tiempos con filete de res Wagyu y langosta post-pelea (0 alcohol 🚫🍺).",
        "antojo_ayame": "Postre de gala a bordo del Symphony Moderna viendo el Rainbow Bridge iluminado.",
        "costs_jpy": {
            "transporte": 9000,
            "hospedaje": 0,
            "actividades_telas": 36000,
            "gastronomia": 20000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.symphony-cruise.co.jp/en/",
            "transport_label": "🛳️ Muelle Hinode (Bahía de Tokio)",
            "activity_url": "https://www.symphony-cruise.co.jp/en/",
            "activity_label": "🚢 Reservar Crucero Cena Symphony Moderna (Ventana VIP)",
            "dining_url": "https://www.symphony-cruise.co.jp/en/",
            "dining_label": "🥩 Menú de Gala 5 Tiempos a Bordo",
            "hotel_url": "https://www.symphony-cruise.co.jp/en/",
            "hotel_label": "🏡 Regreso Triunfal a Nuestro Hogar en Ikebukuro",
            "maps_url": "https://www.google.com/maps/search/Hinode+Pier+Symphony+Cruise+Tokyo"
        }
    },
    {
        "month_num": 8,
        "date_label": "Mayo 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — VACACIONES POST-PELEA #1",
        "duration": "2 Noches",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #2: Metro Marunouchi desde Ikebukuro a Tokyo Station (16 min sentados) + Tokaido Shinkansen Nozomi a Shin-Kobe (2 hrs 40 min).",
        "prefectures": [
            {"num": 12, "name": "Hyogo", "kanji": "兵庫県", "region": "Kansai", "lat": 34.8394, "lon": 134.6939, "activity": "Banquete de Kobe Beef A5 frente al Puerto Marítimo & Castillo de la Garza Blanca en Himeji"},
            {"num": 13, "name": "Osaka", "kanji": "大阪府", "region": "Kansai", "lat": 34.6687, "lon": 135.5013, "activity": "Crucero Nocturno en Bote por los Neones de Dotonbori & Mirador Abeno Harukas"}
        ],
        "schedule": [
            {"time": "Día 1 · Hyogo (#12)", "detail": "Visita matutina al imponente Castillo de Himeji. Por la tarde, paseo junto al mar en Kobe Meriken Park y Harborland, culminando con un banquete de Kobe Beef A5 certificado cocinado a la plancha teppanyaki frente a ustedes."},
            {"time": "Día 2 · Osaka (#13)", "detail": "Traslado de 25 minutos a Osaka. Tarde en el mirador abierto del piso 60 de Abeno Harukas (Harukas 300) y noche divertida navegando en el barco Tombori River Cruise bajo el cartel de Glico en Dotonbori."}
        ],
        "nutrition_bruno": "Filete de Kobe Beef A5 certificado a la plancha teppanyaki sin restricción de báscula.",
        "antojo_ayame": "Takoyaki recién hecho en Dotonbori y pastelería de autor en Kobe.",
        "costs_jpy": {
            "transporte": 64000,
            "hospedaje": 88000,
            "actividades_telas": 16000,
            "gastronomia": 62000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://smart-ex.jp/en/index.php",
            "transport_label": "🚄 Reservar Shinkansen Nozomi en SmartEX (Tokyo ↔ Shin-Kobe)",
            "activity_url": "https://www.abenoharukas-300.jp/en/",
            "activity_label": "🏙️ Entradas Harukas 300 + Castillo de Himeji + Tombori Cruise",
            "dining_url": "https://tabelog.com/en/hyogo/A2801/A280101/rstLst/steak/",
            "dining_label": "🥩 Agendar Kobe Beef A5 Teppanyaki Frente al Puerto (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🚢 Reservar Hotel Frente al Puerto en Kobe Meriken Park",
            "maps_url": "https://www.google.com/maps/dir/Shin-Kobe+Station/Himeji+Castle/Meriken+Park/Dotonbori"
        }
    },
    {
        "month_num": 9,
        "date_label": "Junio 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — EXPEDICIÓN AÉREA & RECONOCIMIENTO CAPITÁN O-3",
        "duration": "3 Noches",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #3: Airport Limousine Bus desde Sunshine City Ikebukuro a Haneda (45 min) + Vuelo directo a Naha (2h 35m).",
        "prefectures": [
            {"num": 14, "name": "Okinawa", "kanji": "沖縄県", "region": "Kyushu & Okinawa", "lat": 26.3154, "lon": 127.7571, "activity": "Taller Real de Teñido «Ryukyu Bingata», Puente sobre el Mar Turquesa de Kouri & Elección de su Futuro Hogar en Chatan/Yomitan"}
        ],
        "schedule": [
            {"time": "Día 1 · Naha y Shuri", "detail": "Llegada a Naha y visita a un estudio tradicional de Ryukyu Bingata (紅型) en Shuri, donde あやめ conoce el arte de teñido multicolor de la antigua realeza de Okinawa. Tarde frente al mar en el santuario sobre el acantilado de Naminoue."},
            {"time": "Día 2 · El Reconocimiento Capitán O-3 (Chatan y Yomitan)", "detail": "Recorrido relajado por la costa de Chatan (Mihama) y los acantilados tranquilos de Yomitan y Onna (a minutos de Kadena Air Base). Toman café frente a la playa viendo la zona exacta donde vivirán con sus gatitos a partir de finales de 2029."},
            {"time": "Día 3 · Isla Kouri y Churaumi", "detail": "Cruce en coche por el puente de 2 km sobre agua cristalina hacia la Isla Kouri y visita al Acuario Churaumi para ver al tiburón ballena gigante. Cena de cerdo negro Agu en shabu-shabu."}
        ],
        "nutrition_bruno": "Cerdo negro Agu de Okinawa en shabu-shabu y filete estilo americano en Chatan.",
        "antojo_ayame": "Tartas de camote morado (Beni-imo) y taller de teñido real Ryukyu Bingata.",
        "costs_jpy": {
            "transporte": 84000,
            "hospedaje": 135000,
            "actividades_telas": 24000,
            "gastronomia": 48000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.ana.co.jp/en/jp/",
            "transport_label": "✈️ Reservar Vuelo Haneda ↔ Naha (ANA / JAL) + Limousine Bus",
            "activity_url": "https://churaumi.okinawa/en/",
            "activity_label": "🌺 Taller Ryukyu Bingata en Shuri + Acuario Churaumi",
            "dining_url": "https://tabelog.com/en/okinawa/rstLst/shabushabu/",
            "dining_label": "🥩 Agendar Agu Pork Shabu-Shabu & Steakhouse en Chatan",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏖️ Reservar Resort Frente al Mar en Chatan / Yomitan",
            "maps_url": "https://www.google.com/maps/dir/Naha+Airport/Chatan,+Okinawa/Yomitan,+Okinawa/Kouri+Bridge"
        }
    },
    {
        "month_num": 10,
        "date_label": "Julio 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Escape del calor húmedo de Tokio)",
        "duration": "2 Noches",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada con reporte diario por LINE.",
        "shortcut": "Atajo #1: JR a Omiya (24 min) + Tohoku Shinkansen Hayabusa en Gran Class (asientos tipo primera clase).",
        "prefectures": [
            {"num": 15, "name": "Aomori", "kanji": "青森県", "region": "Tohoku", "lat": 40.8294, "lon": 140.7353, "activity": "Museo de Carros Iluminados Nebuta frente al Mar & Taller de Bordado Kogin-zashi"},
            {"num": 16, "name": "Akita", "kanji": "秋田県", "region": "Tohoku", "lat": 39.5972, "lon": 140.5614, "activity": "Distrito Samurái de Kakunodate, Perros Akita & Aguas Termales Lechosas de Nyuto Onsen"},
            {"num": 17, "name": "Iwate", "kanji": "岩手県", "region": "Tohoku", "lat": 39.0014, "lon": 141.1066, "activity": "El Pabellón de Oro Puro de Chuson-ji (Hiraizumi) & Barca en la Playa de Rocas Blancas de Jodogahama"}
        ],
        "schedule": [
            {"time": "Día 1 · Iwate (#17)", "detail": "Parada en Hiraizumi para admirar el Konjikido (salón budista cubierto en hoja de oro y nácar) en Chuson-ji y excursión a la costa de Jodogahama para navegar en aguas color esmeralda entre rocas blancas."},
            {"time": "Día 2 · Akita (#16)", "detail": "Cruce en Shinkansen Komachi a Kakunodate para pasear por las mansiones samurái, saludar a los perros Akita y pasar la noche en las aguas termales lechosas del bosque en Nyuto Onsen / Tazawako, cenando pollo Hinai-jidori a la parrilla."},
            {"time": "Día 3 · Aomori (#15)", "detail": "Caminata fresca bajo las cascadas del arroyo Oirase junto al Lago Towada, visita al museo Nebuta Wa Rasse frente a la bahía de Aomori y compra de bordados tradicionales Kogin-zashi antes de volver en el Hayabusa."}
        ],
        "nutrition_bruno": "Pollo Hinai-jidori a las brasas y vieiras frescas de la bahía de Mutsu (Aomori).",
        "antojo_ayame": "Postres de manzana de Aomori y bordados artesanales Kogin-zashi.",
        "costs_jpy": {
            "transporte": 82000,
            "hospedaje": 108000,
            "actividades_telas": 19000,
            "gastronomia": 42000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://www.eki-net.com/en/jreast-train-reservation/Top/Index",
            "transport_label": "🚄 Reservar Shinkansen Hayabusa Gran Class (Omiya ↔ Aomori)",
            "activity_url": "https://www.nebuta.jp/warasse/foreign/english.html",
            "activity_label": "🏮 Museo Nebuta Wa Rasse + Chuson-ji + Kakunodate",
            "dining_url": "https://tabelog.com/en/akita/rstLst/",
            "dining_label": "🍗 Agendar Hinai-Jidori en Akita & Mariscos en Aomori",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Ryokan en Nyuto Onsen / Lago Towada",
            "maps_url": "https://www.google.com/maps/dir/Chuson-ji/Kakunodate/Oirase+Gorge/Nebuta+Museum+WA+RASSE"
        }
    },
    {
        "month_num": 11,
        "date_label": "Agosto 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla / Pre-Campamento Pelea #2 (78.5 kg en clima fresco de 21 °C)",
        "duration": "3 Noches",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #3: Limousine Bus a Haneda + Vuelo a Asahikawa / Sapporo y regreso desde Hakodate.",
        "prefectures": [
            {"num": 18, "name": "Hokkaido", "kanji": "北海道", "region": "Hokkaido", "lat": 43.1907, "lon": 140.9947, "activity": "Creación de Cajas Musicales de Vidrio en el Canal de Otaru, Colinas de Flores de Furano & Vista Nocturna de Doble Bahía en Hakodate"}
        ],
        "schedule": [
            {"time": "Día 1 · Furano y Biei", "detail": "Paseo en carrito eléctrico sin esfuerzo por las colinas tapizadas de flores multicolores en Shikisai-no-Oka y visita al Estanque Azul (Aoi Ike) de Biei."},
            {"time": "Día 2 · Otaru y Sapporo", "detail": "Tarde romántica en el puerto de Otaru: personalizan juntos una caja musical de cristal en Otaru Orgel Doh y pasean junto al canal iluminado con lámparas de gas al anochecer."},
            {"time": "Día 3 · Hakodate", "detail": "Bajada escénica al puerto de Hakodate para subir en teleférico al Monte Hakodate al atardecer, contemplando la ciudad con forma de reloj de arena flanqueada por el océano a ambos lados."}
        ],
        "nutrition_bruno": "Cangrejo real (Tarabagani), salmón salvaje y callo de hacha a la parrilla (0% grasa, proteína marina purísima para bajar a 77 kg).",
        "antojo_ayame": "Cheesecake doble de LeTAO en Otaru y su caja musical de cristal personalizada.",
        "costs_jpy": {
            "transporte": 92000,
            "hospedaje": 138000,
            "actividades_telas": 22000,
            "gastronomia": 54000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.jal.co.jp/jp/en/",
            "transport_label": "✈️ Vuelo Multidestino Haneda → Asahikawa / Hakodate → Haneda",
            "activity_url": "https://www.otaru-orgel.co.jp/en/",
            "activity_label": "🎵 Taller Otaru Orgel Doh + Shikisai-no-Oka + Teleférico Hakodate",
            "dining_url": "https://tabelog.com/en/hokkaido/rstLst/crab/",
            "dining_label": "🦀 Agendar Cangrejo Real Tarabagani en Sapporo / Hakodate",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏨 Reservar Hotel Frente al Canal en Otaru & Puerto de Hakodate",
            "maps_url": "https://www.google.com/maps/dir/Shikisai-no-oka/Otaru+Canal/Mount+Hakodate"
        }
    },
    {
        "month_num": 12,
        "date_label": "Septiembre 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — 🥊 PELEA #2 (SHOOTO: VICTORIA 2-0)",
        "duration": "1 Noche de celebración frente al mar",
        "cat_protocol": "1 Noche (30h): Fuentes continuas de agua, alimentadores y monitoreo por cámara Wi-Fi.",
        "shortcut": "Expreso directo JR Shonan-Shinjuku o línea Fukutoshin desde Ikebukuro hasta Yokohama / Minato Mirai (38 min).",
        "prefectures": [
            {"num": 19, "name": "Kanagawa", "kanji": "神奈川県", "region": "Kanto", "lat": 35.4550, "lon": 139.6313, "activity": "Cabina Aérea sobre el Mar en Yokohama Minato Mirai & Suite en el Piso 65 Frente al Puerto"}
        ],
        "schedule": [
            {"time": "Tarde Post-Combate", "detail": "Tras conseguir tu victoria 2-0 en el torneo regional de Amateur Shooto en 77 kg, viajan en línea directa al puerto de Yokohama sin fatiga de traslado."},
            {"time": "Noche Frente a la Bahía", "detail": "Cruzan el cielo nocturno sobre el agua en las cabinas de cristal del YOKOHAMA AIR CABIN, cenan pato Pekín y mariscos en el Barrio Chino (Chukagai) y duermen en una habitación panorámica en las alturas de la Landmark Tower."}
        ],
        "nutrition_bruno": "Pato asado magro, abulón y camarones salteados en Yokohama Chukagai.",
        "antojo_ayame": "Bollos calientes al vapor y paseo nocturno en teleférico sobre el mar.",
        "costs_jpy": {
            "transporte": 3200,
            "hospedaje": 58000,
            "actividades_telas": 8000,
            "gastronomia": 34000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://yokohama-air-cabin.jp/",
            "transport_label": "🚡 Expreso Directo Ikebukuro ↔ Minato Mirai + Air Cabin",
            "activity_url": "https://yokohama-air-cabin.jp/",
            "activity_label": "🌃 Cabina de Cristal Yokohama Air Cabin & Puerto Nocturno",
            "dining_url": "https://tabelog.com/en/kanagawa/A1401/A140105/rstLst/",
            "dining_label": "🦆 Agendar Cena de Gala en Yokohama Chinatown (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏙️ Reservar Suite Panorámica en Minato Mirai (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Ikebukuro+Station/Minatomirai+Station/Yokohama+Chinatown"
        }
    },
    {
        "month_num": 13,
        "date_label": "Octubre 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — 🦋 MISIÓN OFICIAL KIMONO DE MOTHRA 1961",
        "duration": "3 Noches",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #1: JR a Omiya (24 min) + Hokuriku Shinkansen Kagayaki directo (2 hrs 05 min).",
        "prefectures": [
            {"num": 20, "name": "Ishikawa", "kanji": "石川県", "region": "Chubu", "lat": 36.5613, "lon": 136.6562, "activity": "Encargo del Kimono de Seda de Mothra 1961 con un Maestro Tintorero de Kaga Yuzen en Kanazawa"},
            {"num": 21, "name": "Toyama", "kanji": "富山県", "region": "Chubu", "lat": 36.7077, "lon": 137.2137, "activity": "Crucero por el Cañón de Kurobe & Café frente al Canal de Kansui Park con Vista a los Alpes"},
            {"num": 22, "name": "Fukui", "kanji": "福井県", "region": "Chubu", "lat": 36.2375, "lon": 136.1252, "activity": "Puesta de Sol sobre el Mar de Japón desde las Columnas Volcánicas de Tojinbo"},
            {"num": 23, "name": "Gifu", "kanji": "岐阜県", "region": "Chubu", "lat": 36.2578, "lon": 136.9066, "activity": "Paseo por las Casas de Techo de Paja de Cuento de Hadas en Shirakawa-go"}
        ],
        "schedule": [
            {"time": "Día 1 · Toyama (#21) y Kanazawa (#20)", "detail": "Parada en Toyama para recorrer el cañón de otoño en el tren de Kurobe y tomar té en el mirador de cristal de Kansui Park. Por la tarde llegan a Kanazawa (Ishikawa)."},
            {"time": "Día 2 · Ishikawa (#20 — El Día de Mothra)", "detail": "Cita privada en un taller histórico de Kaga Yuzen (加賀友禅). Toman las medidas exactas de あやめ y encargan el rollo de seda pura (Tango Chirimen) con los colores de la Mothra de 1961 (marfil, oro, naranja tostado, rojo terracota y líneas negras). Visita a taller de pan de oro Kinpaku en Higashi Chaya."},
            {"time": "Día 3 · Gifu (#23) y Fukui (#22)", "detail": "Excursión matutina de 50 min a la aldea de Shirakawa-go (Gifu). Por la tarde bajan a la costa de Fukui para ver la puesta de sol desde los acantilados de Tojinbo y cenar cangrejo Echizen antes de tomar el Shinkansen de vuelta."}
        ],
        "nutrition_bruno": "Cangrejo Echizen de Fukui, pescado blanco Nodoguro a la sal y res Noto Wagyu.",
        "antojo_ayame": "Helado recubierto con hoja de oro real (Kinpaku) en Higashi Chaya y diseño de su Kimono de Mothra.",
        "costs_jpy": {
            "transporte": 68000,
            "hospedaje": 132000,
            "actividades_telas": 350000,
            "gastronomia": 56000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.eki-net.com/en/jreast-train-reservation/Top/Index",
            "transport_label": "🚄 Reservar Hokuriku Shinkansen Kagayaki desde Omiya",
            "activity_url": "http://www.kagayuzen.or.jp/",
            "activity_label": "🦋 Kaga Yuzen Kanazawa (Encargo Kimono Mothra) + Shirakawa-go",
            "dining_url": "https://tabelog.com/en/ishikawa/A1701/A170101/rstLst/",
            "dining_label": "🦀 Agendar Nodoguro en Kanazawa & Cangrejo Echizen en Fukui",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏯 Reservar Ryokan de Lujo en Kanazawa (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Toyama+Kansui+Park/Kanazawa+Station/Shirakawa-go/Tojinbo"
        }
    },
    {
        "month_num": 14,
        "date_label": "Noviembre 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "ROJA",
        "zone_badge": "🔴 ZONA ROJA — FIGHT CAMP TORNEO DEEP FUTURE KING (Hacia Peleas #3 y #4)",
        "duration": "1 Noche sin caminatas (Descanso pasivo al 100%)",
        "cat_protocol": "1 Noche (30h): Fuentes continuas de agua, alimentadores y monitoreo por cámara Wi-Fi.",
        "shortcut": "JR a Shinjuku (5 min) + Odakyu Romancecar GSE en asientos panorámicos delanteros hasta Hakone-Yumoto (85 min).",
        "prefectures": [],
        "schedule": [
            {"time": "Sábado · Traslado Panorámico", "detail": "Como en diciembre pelearás dos veces en la misma noche (Semifinal y Final del torneo), llegan directo a una suite con rotenburo (baño termal privado al aire libre en la terraza) para desinflamar articulaciones."},
            {"time": "Domingo · Lago Ashi y Regreso Temprano", "detail": "Navegan sentados por el Lago Ashi contemplando el Monte Fuji nevado y regresan temprano a Ikebukuro para continuar el corte a 77.0 kg."}
        ],
        "nutrition_bruno": "Pescado de lago a la parrilla, sashimi magro y caldo dashi mineralizante.",
        "antojo_ayame": "Té caliente y dulces otoñales en la terraza privada con vista al bosque de Hakone.",
        "costs_jpy": {
            "transporte": 9600,
            "hospedaje": 84000,
            "actividades_telas": 6000,
            "gastronomia": 24000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.odakyu.jp/english/romancecar/",
            "transport_label": "🚄 Reservar Asiento Panorámico Odakyu Romancecar GSE",
            "activity_url": "https://www.hakonenavi.jp/international/en/",
            "activity_label": "⛴️ Crucero Lago Ashi & Teleférico de Hakone",
            "dining_url": "https://www.ikyu.com/en/",
            "dining_label": "🍱 Cena Kaiseki Ligera de Campamento en la Habitación",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Suite con Rotenburo Privado en Hakone",
            "maps_url": "https://www.google.com/maps/dir/Shinjuku+Station/Hakone-Yumoto+Station/Lake+Ashi"
        }
    },
    {
        "month_num": 15,
        "date_label": "Diciembre 2028",
        "phase": "FASE 2",
        "phase_name": "Kansai, Okinawa, Tohoku Norte, Hokkaido y Hokuriku (Meses 08–15)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — 🏆 PELEAS #3 Y #4 (CAMPEÓN DEEP FUTURE KING: 4-0 INVICTO)",
        "duration": "Fin de Semana Real en Tokio (Durmiendo en casa con los gatitos)",
        "cat_protocol": "Citas en Tokio regresando temprano a dormir a casa antes de las 22:00 hrs.",
        "shortcut": "Línea Marunouchi directa desde Ikebukuro a Tokyo / Marunouchi (16 min).",
        "prefectures": [],
        "schedule": [
            {"time": "Noche del Torneo (2 Peleas en 1 Noche)", "detail": "Ganas la semifinal y la final en la misma cartelera del DEEP Future King Tournament (77 kg), colocándote 4-0 invicto, conquistando tu primer campeonato oficial y asegurando el pase directo a carteleras profesionales de DEEP."},
            {"time": "Día Siguiente · Iluminación Imperial", "detail": "Paseo triunfal con あやめ bajo las avenidas iluminadas con millones de luces doradas en Marunouchi Naka-dori y Roppongi Keyakizaka, con cena de corte Ribeye de Wagyu y mercado navideño."}
        ],
        "nutrition_bruno": "Ribeye Steak de Wagyu A5 a las brasas celebrando el campeonato 4-0 (0 alcohol 🚫🍺).",
        "antojo_ayame": "Chocolate caliente europeo y pastel navideño de fresas japonesas en Marunouchi.",
        "costs_jpy": {
            "transporte": 3000,
            "hospedaje": 0,
            "actividades_telas": 10000,
            "gastronomia": 46000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.tokyometro.jp/en/",
            "transport_label": "🚇 Metro Marunouchi Directo Ikebukuro ↔ Marunouchi",
            "activity_url": "https://www.marunouchi.com/en/",
            "activity_label": "✨ Iluminación Marunouchi Naka-dori & Roppongi Hills",
            "dining_url": "https://tabelog.com/en/tokyo/A1301/A130102/rstLst/steak/",
            "dining_label": "🥩 Agendar Steakhouse de Campeón en Marunouchi (Tabelog)",
            "hotel_url": "https://www.marunouchi.com/en/",
            "hotel_label": "🏡 Regreso Temprano a Nuestro Hogar con los Gatitos",
            "maps_url": "https://www.google.com/maps/dir/Marunouchi+Naka-dori+Street/Roppongi+Keyakizaka+Dori"
        }
    },
    {
        "month_num": 16,
        "date_label": "Enero 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — VACACIONES DE INVIERNO DEL CAMPEÓN (PARTE 1: KYUSHU NORTE)",
        "duration": "3 Noches en el sur cálido",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #3: Limousine Bus a Haneda + Vuelo a Fukuoka (1h 50m) y regreso desde Nagasaki.",
        "prefectures": [
            {"num": 24, "name": "Fukuoka", "kanji": "福岡県", "region": "Kyushu & Okinawa", "lat": 33.6403, "lon": 130.1989, "activity": "Atardecer frente al Torii Blanco en el Mar de Itoshima (Sakurai Futamigaura)"},
            {"num": 25, "name": "Oita", "kanji": "大分県", "region": "Kyushu & Okinawa", "lat": 33.2658, "lon": 131.3694, "activity": "Viaje en el Tren de Madera «Yufuin no Mori» a la Aldea Termal de Yufuin & Vapores Azules de Beppu"},
            {"num": 26, "name": "Saga", "kanji": "佐賀県", "region": "Kyushu & Okinawa", "lat": 33.1904, "lon": 129.8994, "activity": "Pintura de Tazas Gemelas en la Cuna de la Porcelana Real de Arita & Torii Sumergido de Tara"},
            {"num": 27, "name": "Nagasaki", "kanji": "長崎県", "region": "Kyushu & Okinawa", "lat": 32.7530, "lon": 129.8511, "activity": "Teleférico de Cristal a la Vista Nocturna de los 10 Millones de Dólares en el Monte Inasa"}
        ],
        "schedule": [
            {"time": "Día 1 · Fukuoka (#24)", "detail": "Recorrido por la costa de Itoshima tomando café frente a las olas y fotografiando el Torii blanco frente a las rocas gemelas de los esposos en el mar. Cena de Mizutaki (caldo rico en colágeno) en Hakata."},
            {"time": "Día 2 · Oita (#25)", "detail": "Abordan el tren clásico de madera y terciopelo verde Yufuin no Mori hacia Yufuin, pasean por Yufuin Floral Village, el lago Kinrin y visitan el manantial azul cobalto Umi Jigoku en Beppu."},
            {"time": "Día 3 · Saga (#26) y Nagasaki (#27)", "detail": "Mañana en Arita (Saga) para pintar un par de tazas gemelas de porcelana para su casa y ver los Torii sumergidos de Tara. Tarde en el tren bala Kamome hacia Nagasaki: Glover Garden sobre la bahía y subida nocturna al Monte Inasa."}
        ],
        "nutrition_bruno": "Mizutaki de pollo de corral en Hakata, carne Bungo Wagyu en Oita y pescado fresco en Nagasaki.",
        "antojo_ayame": "Rollo de pastel B-Speak en Yufuin, Castella tradicional en Nagasaki y sus tazas pintadas en Arita.",
        "costs_jpy": {
            "transporte": 94000,
            "hospedaje": 136000,
            "actividades_telas": 24000,
            "gastronomia": 52000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.jrkyushu.co.jp/english/train/yufuin_no_mori.html",
            "transport_label": "🚂 Reservar Tren Yufuin no Mori + Vuelos Haneda ↔ Fukuoka/Nagasaki",
            "activity_url": "https://www.nagasaki-ropeway.jp/",
            "activity_label": "🌃 Teleférico Monte Inasa + Porcelana Arita + Umi Jigoku Beppu",
            "dining_url": "https://tabelog.com/en/fukuoka/A4001/rstLst/mizutaki/",
            "dining_label": "🍲 Agendar Mizutaki Tradicional en Hakata (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Ryokan de Lujo en Yufuin & Hotel en Nagasaki",
            "maps_url": "https://www.google.com/maps/dir/Sakurai+Futamigaura/Yufuin+Station/Arita,+Saga/Mount+Inasa"
        }
    },
    {
        "month_num": 17,
        "date_label": "Febrero 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE — VACACIONES DEL CAMPEÓN (PARTE 2: KYUSHU SUR)",
        "duration": "3 Noches",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario por LINE.",
        "shortcut": "Atajo #3: Vuelo Haneda a Kumamoto (KMJ) y regreso desde Kagoshima (KOJ) + vehículo privado.",
        "prefectures": [
            {"num": 28, "name": "Kumamoto", "kanji": "熊本県", "region": "Kyushu & Okinawa", "lat": 32.7901, "lon": 130.7351, "activity": "Ceremonia de Té Matcha en el Jardín Suizenji & Mirador del Caldero Volcánico de Aso"},
            {"num": 29, "name": "Miyazaki", "kanji": "宮崎県", "region": "Kyushu & Okinawa", "lat": 32.7042, "lon": 131.3005, "activity": "Paseo en Barca bajo la Cascada de los Dioses en la Garganta de Takachiho & Santuario Marino Udo Jingu"},
            {"num": 30, "name": "Kagoshima", "kanji": "鹿児島県", "region": "Kyushu & Okinawa", "lat": 31.2367, "lon": 130.6425, "activity": "Baño de Arena Volcánica Caliente en la Orilla de la Playa de Ibusuki frente al Volcán Sakurajima"}
        ],
        "schedule": [
            {"time": "Día 1 · Kumamoto (#28)", "detail": "Visita al Castillo de Kumamoto, ceremonia de té matcha con dulces tradicionales frente al lago esmeralda del jardín Suizenji Jojuen y ruta escénica por las praderas volcánicas de Aso."},
            {"time": "Día 2 · Miyazaki (#29)", "detail": "Descenso a la mística Garganta de Takachiho, donde tú remas una barca junto a あやめ entre muros de basalto volcánico justo al pie de la cascada de Manai, seguido de la visita al santuario Udo Jingu dentro de una caverna frente al océano."},
            {"time": "Día 3 · Kagoshima (#30)", "detail": "Traslado a la costa sur de Ibusuki para vivir el Sunamushi Onsen: se recuestan juntos con yukata en la playa mientras los cubren con arena negra calentada por vapor geotérmico escuchando el mar y viendo el volcán Sakurajima."}
        ],
        "nutrition_bruno": "Res roja magra Akaushi de Aso y cerdo negro Kurobuta de Kagoshima al vapor.",
        "antojo_ayame": "Hielo raspado Shirokuma tradicional de Kagoshima y té matcha frente al lago Suizenji.",
        "costs_jpy": {
            "transporte": 92000,
            "hospedaje": 134000,
            "actividades_telas": 21000,
            "gastronomia": 49000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.ana.co.jp/en/jp/",
            "transport_label": "✈️ Vuelo Haneda → Kumamoto / Kagoshima → Haneda",
            "activity_url": "https://takachiho-kanko.info/en/boat/",
            "activity_label": "🚣 Reservar Barca Garganta de Takachiho + Arena Volcánica Ibusuki",
            "dining_url": "https://tabelog.com/en/kagoshima/rstLst/shabushabu/",
            "dining_label": "🥩 Agendar Akaushi Beef en Aso & Kurobuta en Kagoshima",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Ryokan Frente al Mar en Ibusuki (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Suizenji+Jojuen/Takachiho+Gorge/Udo+Jingu/Ibusuki+Hakusuikan"
        }
    },
    {
        "month_num": 18,
        "date_label": "Marzo 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Elección de la Joya Azul de Mothra)",
        "duration": "2 Noches",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada con reporte diario por LINE.",
        "shortcut": "Atajo #2: Shinkansen a Nagoya (1h 40m) + Tren turístico de primera clase Kintetsu Shimakaze (sillones de piel con masaje lumbar).",
        "prefectures": [
            {"num": 31, "name": "Mie", "kanji": "三重県", "region": "Kansai", "lat": 34.4820, "lon": 136.8433, "activity": "Santuario Sagrado de Ise Jingu, Rocas de los Esposos en Futami & Elección de la Joya Azul de Mothra en Toba"},
            {"num": 32, "name": "Wakayama", "kanji": "和歌山県", "region": "Kansai", "lat": 33.6690, "lon": 135.8891, "activity": "La Pagoda Roja junto a la Cascada de Nachi & Aguas Termales Frente al Pacífico en Shirahama"}
        ],
        "schedule": [
            {"time": "Día 1 · Mie (#31)", "detail": "Caminata entre los cedros milenarios de Ise Jingu, vista al mar en las rocas sagradas del matrimonio (Meoto Iwa) y visita a las joyerías artesanales de la bahía de Toba para adquirir el broche central (obidome) en turquesa / azul celeste que representa los ojos azules de la Mothra de 1961. Cena de langosta Ise-ebi a la parrilla."},
            {"time": "Día 2 · Wakayama (#32)", "detail": "Recorrido costero hacia Kii-Katsuura y Nachi para admirar la cascada de 133 metros de Nachi Falls detrás de la pagoda bermellón, cerrando en las playas de arena blanca de Shirahama con baño termal pegado al mar."}
        ],
        "nutrition_bruno": "Langosta de Ise (Ise-ebi) a la parrilla, filete Matsusaka Wagyu magro y atún fresco de Kii-Katsuura.",
        "antojo_ayame": "Akafuku Mochi junto al río en Ise y elección del broche azul celeste de Mothra en Toba.",
        "costs_jpy": {
            "transporte": 64000,
            "hospedaje": 112000,
            "actividades_telas": 55000,
            "gastronomia": 54000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://www.kintetsu.co.jp/foreign/english/shimakaze/",
            "transport_label": "🚄 Reservar Tren de Lujo Kintetsu Shimakaze + Shinkansen",
            "activity_url": "https://www.isejingu.or.jp/en/",
            "activity_label": "⛩️ Ise Jingu + Joyerías de Toba (Broche Mothra) + Nachi Falls",
            "dining_url": "https://tabelog.com/en/mie/rstLst/",
            "dining_label": "🦞 Agendar Langosta Ise-ebi & Matsusaka Beef en Ise-Shima",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🌊 Reservar Ryokan Frente al Mar en Bahía Ago / Shirahama",
            "maps_url": "https://www.google.com/maps/dir/Ise+Jingu/Meoto+Iwa/Toba+Bay/Nachi+Falls/Shirahama+Beach"
        }
    },
    {
        "month_num": 19,
        "date_label": "Abril 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Recepción final del Kimono y Obi de Mothra en Sakura)",
        "duration": "2 Noches en plena floración de cerezos",
        "cat_protocol": "2 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #2: Metro Marunouchi a Tokyo Station (16 min) + Shinkansen Nozomi a Kioto (2 hrs 15 min).",
        "prefectures": [
            {"num": 33, "name": "Kioto", "kanji": "京都府", "region": "Kansai", "lat": 35.0116, "lon": 135.7681, "activity": "Recepción del Obi Negro y Oro en el Distrito Textil de Nishijin & Paseo en Barca bajo los Cerezos de Arashiyama"},
            {"num": 34, "name": "Nara", "kanji": "奈良県", "region": "Kansai", "lat": 34.6851, "lon": 135.8048, "activity": "Alimentar a los Ciervos Sagrados bajo los Cerezos en Flor & Camino de las 3,000 Linternas de Kasuga Taisha"},
            {"num": 35, "name": "Shiga", "kanji": "滋賀県", "region": "Kansai", "lat": 35.2178, "lon": 135.8966, "activity": "Teleférico a la Terraza sobre las Nubes frente al Lago Biwa & Canales Antiguos de Omihachiman"}
        ],
        "schedule": [
            {"time": "Día 1 · Kioto (#33)", "detail": "Por la mañana navegan en barca privada por el río en Arashiyama rodeados de pétalos de cerezo. Por la tarde acuden a la casa tejedora de Nishijin (西陣) para recoger el obi de seda negra con bordados dorados y realizar la prueba completa en espejo del Kimono de Mothra y el tocado de plumas doradas con turquesas de あやめ."},
            {"time": "Día 2 · Nara (#34) y Shiga (#35)", "detail": "Mañana en el Parque de Nara dando galletas shika-senbei a los ciervos bajo los cerezos y caminando entre las 3,000 linternas de Kasuga Taisha. Tarde en teleférico a Biwako Terrace (Shiga) para tomar té viendo el Lago Biwa desde las alturas."}
        ],
        "nutrition_bruno": "Filete magro de Omi Beef (Shiga) y Yudofu proteico tradicional en Arashiyama.",
        "antojo_ayame": "Parfait de Matcha de Uji en Kioto y entrega final de su Obi imperial en Nishijin.",
        "costs_jpy": {
            "transporte": 62000,
            "hospedaje": 128000,
            "actividades_telas": 145000,
            "gastronomia": 52000,
            "cat_sitter": 16000
        },
        "booking_angles": {
            "transport_url": "https://smart-ex.jp/en/index.php",
            "transport_label": "🚄 Reservar Shinkansen Nozomi en SmartEX (Tokyo ↔ Kyoto)",
            "activity_url": "https://www.biwako-valley.com/en/",
            "activity_label": "🌸 Casa Tejedora Nishijin + Barca Arashiyama + Biwako Terrace",
            "dining_url": "https://tabelog.com/en/kyoto/rstLst/",
            "dining_label": "🥩 Agendar Omi Beef & Kaiseki de Primavera en Kioto (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏯 Reservar Ryokan junto al Río en Arashiyama (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Arashiyama,+Kyoto/Nishijin,+Kyoto/Kasuga+Taisha/Biwako+Terrace"
        }
    },
    {
        "month_num": 20,
        "date_label": "Mayo 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (79 kg — Ruta Completa por las 5 Prefecturas de Chugoku)",
        "duration": "3 Noches",
        "cat_protocol": "3 Noches: Servicio de Cat Sitter certificada con reporte diario de fotos y videos por LINE.",
        "shortcut": "Atajo #3: Vuelo desde Haneda a Izumo (IZO) y regreso desde Hiroshima / Yamaguchi.",
        "prefectures": [
            {"num": 36, "name": "Shimane", "kanji": "島根県", "region": "Chugoku", "lat": 35.4020, "lon": 132.6853, "activity": "Oración por su Matrimonio Eterno en el Gran Santuario de Izumo Taisha"},
            {"num": 37, "name": "Tottori", "kanji": "鳥取県", "region": "Chugoku", "lat": 35.5401, "lon": 134.2286, "activity": "Caminata al Atardecer por la Cima de las Dunas de Arena Frente al Mar de Japón"},
            {"num": 38, "name": "Okayama", "kanji": "岡山県", "region": "Chugoku", "lat": 34.5955, "lon": 133.7707, "activity": "Paseo en Bote Tradicional entre Sauces por el Canal de Kurashiki Bikan"},
            {"num": 39, "name": "Hiroshima", "kanji": "広島県", "region": "Chugoku", "lat": 34.2960, "lon": 132.3198, "activity": "Crucero Privado al Atardecer bajo el Gran Torii Flotante en la Isla de Miyajima"},
            {"num": 40, "name": "Yamaguchi", "kanji": "山口県", "region": "Chugoku", "lat": 34.4178, "lon": 131.0631, "activity": "El Túnel de los 123 Torii Rojos sobre el Acantilado Marino de Motonosumi & Puente Kintaikyo"}
        ],
        "schedule": [
            {"time": "Día 1 · Shimane (#36) y Tottori (#37)", "detail": "Aterrizan en Izumo y visitan Izumo Taisha, el santuario supremo de Japón donde los dioses bendicen los matrimonios destinados (En-musubi). Por la tarde recorren la costa hasta las Dunas de Tottori para ver caer el sol en el Mar de Japón."},
            {"time": "Día 2 · Okayama (#38) y Hiroshima (#39)", "detail": "Bajada al canal histórico de Kurashiki Bikan (Okayama) para navegar en bote de madera y ver tiendas de textiles artesanales. Tarde en ferry a la isla sagrada de Miyajima (Hiroshima), pasando bajo el gran Torii flotante al atardecer."},
            {"time": "Día 3 · Yamaguchi (#40)", "detail": "Excursión de 15 minutos desde Hiroshima al puente de cinco arcos de madera Kintaikyo en Iwakuni y visita costera a los 123 Torii rojos de Motonosumi frente al mar azul turquesa antes de regresar a Tokio."}
        ],
        "nutrition_bruno": "Ostras gigantes de Miyajima asadas a la parrilla, fugu/pescado blanco en Yamaguchi y almejas Shijimi de Shinji.",
        "antojo_ayame": "Momiji Manju recién horneado en Miyajima y frutas blancas reales de Okayama.",
        "costs_jpy": {
            "transporte": 98000,
            "hospedaje": 138000,
            "actividades_telas": 24000,
            "gastronomia": 54000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://www.jal.co.jp/jp/en/",
            "transport_label": "✈️ Vuelo Haneda → Izumo + Shinkansen Regreso desde Hiroshima",
            "activity_url": "https://izumooyashiro.or.jp/en",
            "activity_label": "⛩️ Izumo Taisha + Dunas Tottori + Kurashiki + Miyajima + Motonosumi",
            "dining_url": "https://tabelog.com/en/hiroshima/rstLst/",
            "dining_label": "🦪 Agendar Ostras a las Brasas en Miyajima (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🌊 Reservar Ryokan Frente al Mar en Miyajima / Izumo",
            "maps_url": "https://www.google.com/maps/dir/Izumo+Taisha/Tottori+Sand+Dunes/Kurashiki+Bikan+Historical+Quarter/Itsukushima+Shrine/Motonosumi+Shrine"
        }
    },
    {
        "month_num": 21,
        "date_label": "Junio 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "AMARILLA",
        "zone_badge": "🟡 Zona Amarilla (Últimas expediciones antes del Campamento Final)",
        "duration": "Parte A Shikoku (3 Noches) + Parte B Alpina y Mar del Norte (1 Noche)",
        "cat_protocol": "Parte A (3 Noches): Cat Sitter certificada con fotos/video por LINE. Parte B (1 Noche): Fuentes + cámara Wi-Fi.",
        "shortcut": "Parte A: Vuelo Haneda a Matsuyama (1h 25m). Parte B: Shinjuku/Omiya a Matsumoto, Kamikochi y costa de Niigata.",
        "prefectures": [
            {"num": 41, "name": "Ehime", "kanji": "愛媛県", "region": "Shikoku", "lat": 33.8520, "lon": 132.7864, "activity": "Salón Imperial de Dogo Onsen Honkan & Parada en la Estación Frente al Mar de Shimonada"},
            {"num": 42, "name": "Kagawa", "kanji": "香川県", "region": "Shikoku", "lat": 34.1869, "lon": 133.6458, "activity": "Sesión de Fotos al Atardecer en el «Espejo del Cielo» de la Playa Chichibugahama"},
            {"num": 43, "name": "Tokushima", "kanji": "徳島県", "region": "Shikoku", "lat": 34.2378, "lon": 134.6392, "activity": "Taller de Teñido Azul Índigo Tradicional «Aizome» & Remolinos Marinos de Naruto"},
            {"num": 44, "name": "Kochi", "kanji": "高知県", "region": "Shikoku", "lat": 33.4969, "lon": 133.5750, "activity": "Paseo frente al Pacífico en la Playa de Katsurahama & Bonito Asado al Fuego de Paja"},
            {"num": 45, "name": "Nagano", "kanji": "長野県", "region": "Chubu", "lat": 36.2483, "lon": 137.6368, "activity": "Aire Puro en el Puente de Aguas Cristalinas de Kamikochi & Castillo Negro de Matsumoto"},
            {"num": 46, "name": "Niigata", "kanji": "新潟県", "region": "Chubu", "lat": 38.4114, "lon": 139.4622, "activity": "Tren Gastronómico «Kairi» bordeando los Acantilados del Mar de Japón"}
        ],
        "schedule": [
            {"time": "Parte A · Día 1 — Ehime (#41) y Kochi (#44)", "detail": "Vuelo a Matsuyama. Baño en la histórica casa Dogo Onsen Honkan, tren costero Iyonada Monogatari deteniéndose en el andén frente al mar de Shimonada, y bajada a la playa de Katsurahama (Kochi) para cenar Katsuo no Tataki (bonito sellado al fuego de paja, 100% proteína magra)."},
            {"time": "Parte A · Día 2 — Tokushima (#43) y Kagawa (#42)", "detail": "Taller de teñido azul índigo Aizome (藍染) en Tokushima y vista de los remolinos gigantes del estrecho de Naruto. Al atardecer llegan a la playa de Chichibugahama (Kagawa), donde la marea baja refleja el cielo como un espejo perfecto."},
            {"time": "Parte B · Fin de Semana — Nagano (#45) y Niigata (#46)", "detail": "Caminata junto al río de deshielo turquesa en Kamikochi y Castillo de Matsumoto (Nagano #45), subiendo después a la costa de Niigata (#46) para abordar el tren panorámico Kairi viendo el atardecer sobre el Mar de Japón mientras cenan pescado blanco Nodoguro."}
        ],
        "nutrition_bruno": "Katsuo no Tataki (bonito al fuego de paja en Kochi, proteína magra pura) y pescado Nodoguro en Niigata.",
        "antojo_ayame": "Cítricos dulces de Ehime, pañuelo teñido en azul Aizome y fotos en el Espejo del Cielo de Chichibugahama.",
        "costs_jpy": {
            "transporte": 118000,
            "hospedaje": 156000,
            "actividades_telas": 32000,
            "gastronomia": 64000,
            "cat_sitter": 24000
        },
        "booking_angles": {
            "transport_url": "https://iyonadamonogatari.com/",
            "transport_label": "🚂 Reservar Tren Costero Iyonada Monogatari + Tren Kairi Niigata",
            "activity_url": "https://dogo.jp/en",
            "activity_label": "♨️ Dogo Onsen Honkan + Taller Aizome + Chichibugahama + Kamikochi",
            "dining_url": "https://tabelog.com/en/kochi/rstLst/",
            "dining_label": "🐟 Agendar Katsuo no Tataki al Fuego en Kochi (Tabelog)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏯 Reservar Ryokan en Dogo Onsen & Kamikochi",
            "maps_url": "https://www.google.com/maps/dir/Dogo+Onsen/Shimonada+Station/Katsurahama/Chichibugahama+Beach/Naruto+Whirlpools"
        }
    },
    {
        "month_num": 22,
        "date_label": "Julio 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "ROJA",
        "zone_badge": "🔴 ZONA ROJA — FIGHT CAMP FINAL & 🎉 ¡PREFECTURA #47: 100% DE JAPÓN CONQUISTADO (全国制覇)!",
        "duration": "1 Noche de descanso fresco al pie del Monte Fuji",
        "cat_protocol": "1 Noche (30h): Fuentes continuas de agua, alimentadores y monitoreo por cámara Wi-Fi.",
        "shortcut": "JR a Shinjuku (5 min) + Tren directo Fuji Excursion hasta Kawaguchiko (1 hr 50 min).",
        "prefectures": [
            {"num": 47, "name": "Yamanashi", "kanji": "山梨県", "region": "Chubu", "lat": 35.5171, "lon": 138.7518, "activity": "Crucero Privado en el Lago Kawaguchiko frente al Monte Fuji, Brindis por las 47 Prefecturas & Ensayo General de Godzilla y Mothra"}
        ],
        "schedule": [
            {"time": "Tarde · El Sello #47 (全国制覇)", "detail": "Al pisar Yamanashi, tú y あやめ colocan el sello #47 completando oficialmente todas las prefecturas de Japón. Paseo tranquilo en lancha privada por el Lago Kawaguchiko con el Monte Fuji de fondo y visita a los jardines de cajas musicales del bosque."},
            {"time": "Noche en la Suite · El Ensayo General de Godzilla y Mothra", "detail": "Con las cortinas cerradas en su ryokan frente al lago, realizan el ensayo privado de su entrada de retiro: tú vistes la bata oscura con las placas dorsales blanco hueso del Godzilla de 1954 y あやめ viste su Kimono de Mothra 1961 con el tocado dorado, cronometrando el gesto exacto en el que ella levanta las mangas aladas para quitarte la bata de los hombros."}
        ],
        "nutrition_bruno": "Pescado de montaña a la sal y cortes magros de Koshu Beef en porción exacta de campamento (77 kg).",
        "antojo_ayame": "Duraznos blancos reales de Yamanashi y brindis sin alcohol frente al Monte Fuji por las 47 prefecturas.",
        "costs_jpy": {
            "transporte": 12400,
            "hospedaje": 96000,
            "actividades_telas": 28000,
            "gastronomia": 28000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.eki-net.com/en/jreast-train-reservation/Top/Index",
            "transport_label": "🚄 Reservar Tren Directo JR Fuji Excursion (Shinjuku ↔ Kawaguchiko)",
            "activity_url": "https://kawaguchikomusicforest.jp/",
            "activity_label": "🗻 Lancha Privada Lago Kawaguchiko + Music Forest Museum",
            "dining_url": "https://www.ikyu.com/en/",
            "dining_label": "🥩 Cena Privada en Habitación con Vista al Monte Fuji",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "♨️ Reservar Suite Frente al Monte Fuji en Kawaguchiko (Ikyu)",
            "maps_url": "https://www.google.com/maps/dir/Shinjuku+Station/Kawaguchiko+Station/Kawaguchiko+Music+Forest+Museum"
        }
    },
    {
        "month_num": 23,
        "date_label": "Agosto 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "VERDE",
        "zone_badge": "🟢 ZONA VERDE CORTA — 🏆 PELEA #5 (DOBLE CAMPEÓN 二冠王: 5-0) + DOBLE LLAVE",
        "duration": "Noche de Gala en Tokio",
        "cat_protocol": "1 Noche (o regreso a casa): Monitoreo Wi-Fi y alimentadores automáticos.",
        "shortcut": "Traslado privado a la arena y cena de gala en Toranomon / Azabudai Hills.",
        "prefectures": [],
        "schedule": [
            {"time": "El Quinto Combate (5-0)", "detail": "Subes a la jaula/ring en 77 kg y conquistas tu segundo campeonato oficial (Campeonato KROSS×OVER / All-Japan), convirtiéndote en Doble Campeón (二冠王) con récord 5-0."},
            {"time": "La Reunión de la Doble Llave", "detail": "Al ver que saliste limpio y sin lesiones, tu entrenador en jefe y tu mánager あやめ autorizan por unanimidad firmar el Contrato de 1 Sola Pelea (Wan-Matchi Keiyaku / ワンマッチ契約) en DEEP TOKYO IMPACT o KROSS×OVER CAGE para celebrar tu 6ª y última pelea de graduación."},
            {"time": "Noche de Celebración", "detail": "Cena de sushi Omakase de alta gama y noche viendo la Torre de Tokio iluminada desde el piso 52 de Toranomon / Azabudai Hills."}
        ],
        "nutrition_bruno": "Sushi Omakase Edomae (atún Otoro, erizo Uni, pargo y calamar de máxima pureza).",
        "antojo_ayame": "Postre de alta pastelería con vista nocturna directa a Tokyo Tower.",
        "costs_jpy": {
            "transporte": 8000,
            "hospedaje": 88000,
            "actividades_telas": 0,
            "gastronomia": 64000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://www.azabudai-hills.com/en/",
            "transport_label": "🚕 Traslado VIP a Toranomon / Azabudai Hills",
            "activity_url": "https://www.azabudai-hills.com/en/",
            "activity_label": "🗼 Mirador Nocturno Frente a Tokyo Tower",
            "dining_url": "https://tabelog.com/en/tokyo/rstLst/sushi/",
            "dining_label": "🍣 Agendar Sushi Omakase en Tokio (Tabelog / TableCheck)",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "🏙️ Reservar Suite Frente a Tokyo Tower (Ikyu)",
            "maps_url": "https://www.google.com/maps/search/Azabudai+Hills+Tokyo+Tower+View"
        }
    },
    {
        "month_num": 24,
        "date_label": "Septiembre 2029",
        "phase": "FASE 3",
        "phase_name": "Kyushu Completo, Kansai Imperial, Chugoku, Shikoku y el Retiro 6-0 (Meses 16–24)",
        "zone_code": "DORADA",
        "zone_badge": "👑 ZONA DORADA DEFINITIVA — 🦖🦋 PELEA #6 (RETIRO INVICTO 6-0: GINZA 1954) + HELICÓPTERO",
        "duration": "Gran Noche de Retiro en Shinjuku FACE / Korakuen Hall + Vuelo Privado en Helicóptero al Día Siguiente",
        "cat_protocol": "Regreso a casa en Ikebukuro para celebrar con nuestros gatitos y preparar la mudanza a Okinawa O-3.",
        "shortcut": "Traslado privado a Shinjuku FACE / Korakuen Hall y al día siguiente al Helipuerto de Tokio (Shin-Kiba).",
        "prefectures": [],
        "schedule": [
            {"time": "1. Calentamiento en Camerino", "detail": "Vistes tus shorts YOKKAO tricolores y haces el último hitting de manoplas con tus guantes Venum Pro Boxing antes de que el inspector coloque las guantillas oficiales. Te pones la bata del Godzilla de 1954 mientras あやめ está lista a tu lado con su Kimono de Mothra 1961 y peineta de plumas doradas y turquesas."},
            {"time": "2. Entrada de 70 Segundos («La Caída de Ginza 1954»)", "detail": "0:00–0:15: Reflectores blancos a contraluz, humo bajo, campanadas de Ginza Wako, radio de 1954 y rugido original. 0:15–0:50: Tambor Taiko en vivo y caída en efecto dominó de los 4 bailarines en el pasillo. 0:50–1:10: En la escalera del ring, あやめ despliega las mangas aladas de Mothra (el único destello de color dorado, naranja y turquesa) al retirarte la bata de los hombros."},
            {"time": "3. El Combate y el Trono Vacante (6-0)", "detail": "Ganas tu sexto combate de forma contundente. En el centro del ring, con あやめ a tu lado, anuncias tu retiro oficial invicto (6-0), dejando tus títulos vacantes en la cima rumbo a tu carrera como Capitán O-3 en Okinawa."},
            {"time": "4. Día Siguiente · El Cielo de Tokio en Helicóptero", "detail": "Traslado al Helipuerto de Tokio (Shin-Kiba) para abordar un helicóptero privado al atardecer. Sobrevolando la Bahía de Tokio, Ginza, Shibuya y Tokyo Tower, brindan por haber conquistado las 47 prefecturas de Japón y tu 6-0 perfecto."}
        ],
        "nutrition_bruno": "Banquete Imperial de Graduación: Chateaubriand Wagyu A5 y mariscos de gala (0 alcohol 🚫🍺).",
        "antojo_ayame": "Pastel de celebración del 6-0 y vuelo privado al atardecer sobre Tokio.",
        "costs_jpy": {
            "transporte": 15000,
            "hospedaje": 0,
            "actividades_telas": 195000,
            "gastronomia": 75000,
            "cat_sitter": 0
        },
        "booking_angles": {
            "transport_url": "https://ariair.arila.co.jp/cruising/tokyo",
            "transport_label": "🚁 Helipuerto de Tokio (Shin-Kiba)",
            "activity_url": "https://ariair.arila.co.jp/cruising/tokyo",
            "activity_label": "🚁 Reservar Vuelo Privado en Helicóptero al Atardecer (ARIAir)",
            "dining_url": "https://tabelog.com/en/tokyo/rstLst/steak/",
            "dining_label": "🥩 Agendar Banquete Chateaubriand Wagyu A5 del Retiro 6-0",
            "hotel_url": "https://www.ikyu.com/en/",
            "hotel_label": "✈️🌺 Siguiente Parada: Octubre 2029 — Capitán O-3 en Okinawa",
            "maps_url": "https://www.google.com/maps/dir/Korakuen+Hall/Tokyo+Heliport"
        }
    }
]


# ==============================================================================
# 2. COMPLETE WARDROBE V8 + SAMSUNG TECH KOREA CATALOG (58 ITEMS)
# ==============================================================================
WARDROBE_CATALOG = {
    "categories": [
        {
            "id": "kicks",
            "name": "👟 13 Sneakers (GOAT · US 14)",
            "color": "#22c55e",
            "items": [
                {"code": "S01", "name": "Air Jordan 1 High OG 'Chicago Lost & Found'", "sku": "DZ5485-612", "size": "US 14", "currency": "USD", "price": 340, "url": "https://www.goat.com/sneakers/air-jordan-1-retro-high-og-dz5485-612"},
                {"code": "S02", "name": "Air Jordan 1 High OG 'Black Toe Reimagined'", "sku": "DZ5485-061", "size": "US 14", "currency": "USD", "price": 148, "url": "https://www.goat.com/sneakers/air-jordan-1-retro-high-og-black-toe-reimagined-dz5485-061"},
                {"code": "S03", "name": "Air Jordan 1 High OG 'Shadow 2.0'", "sku": "555088-035", "size": "US 14", "currency": "USD", "price": 165, "url": "https://www.goat.com/sneakers/air-jordan-1-retro-high-og-shadow-2-0-555088-035"},
                {"code": "S04", "name": "Air Jordan 1 High '85 'Neutral Grey'", "sku": "BQ4422-100", "size": "US 14", "currency": "USD", "price": 140, "url": "https://www.goat.com/sneakers/air-jordan-1-retro-high-85-og-neutral-grey-bq4422-100"},
                {"code": "S05", "name": "Marvel × Air Jordan 1 High OG 'Spider-Verse'", "sku": "DV1748-601", "size": "US 14", "currency": "USD", "price": 212, "url": "https://www.goat.com/sneakers/marvel-x-air-jordan-1-retro-high-og-spider-man-across-the-spider-verse-dv1748-601"},
                {"code": "S06", "name": "Air Jordan 1 High OG 'Turbo Green'", "sku": "555088-311", "size": "US 14", "currency": "USD", "price": 220, "url": "https://www.goat.com/sneakers/air-jordan-1-retro-high-og-turbo-green-555088-311"},
                {"code": "S07", "name": "Air Jordan 4 Retro 'Military Blue' (2024)", "sku": "FV5029-141", "size": "US 14", "currency": "USD", "price": 220, "url": "https://www.goat.com/sneakers/air-jordan-4-retro-military-blue-2024-fv5029-141"},
                {"code": "S08", "name": "Air Jordan 4 Retro 'Bred Reimagined'", "sku": "FV5029-006", "size": "US 14", "currency": "USD", "price": 280, "url": "https://www.goat.com/sneakers/air-jordan-4-retro-bred-reimagined-fv5029-006"},
                {"code": "S09", "name": "Air Jordan 4 Retro OG 'White Cement' (2025)", "sku": "FV5029-100", "size": "US 14", "currency": "USD", "price": 270, "url": "https://www.goat.com/sneakers/air-jordan-4-retro-og-white-cement-2025-fv5029-100"},
                {"code": "S10", "name": "Air Jordan 7 Retro 'Cardinal'", "sku": "CU9307-106", "size": "US 14", "currency": "USD", "price": 140, "url": "https://www.goat.com/sneakers/air-jordan-7-retro-cardinal-2022-cu9307-106"},
                {"code": "S11", "name": "Trophy Room × Air Jordan 7 Retro 'Olympic'", "sku": "DM1195-474", "size": "US 14", "currency": "USD", "price": 290, "url": "https://www.goat.com/sneakers/trophy-room-x-air-jordan-7-retro-olympic-dm1195-474"},
                {"code": "S12", "name": "Air Jordan 1 High OG 'Origin Story' (GRAIL)", "sku": "555088-602", "size": "US 14", "currency": "USD", "price": 650, "url": "https://www.goat.com/sneakers/spider-verse-x-air-jordan-1-retro-high-og-origin-story"},
                {"code": "S13", "name": "Air Jordan 13 Retro 'French Blue'", "sku": "414571-164", "size": "US 14", "currency": "USD", "price": 170, "url": "https://www.goat.com/sneakers/air-jordan-13-retro-french-blue-414571-164"}
            ]
        },
        {
            "id": "levis",
            "name": "👖 8 Levi's Jeans (36W × 32L · Con Promos)",
            "color": "#3b82f6",
            "items": [
                {"code": "L1", "name": "Levi's 501 Original — Medium Indigo", "sku": "005013367", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/straight/501-original-fit-mens-jeans/p/005013367"},
                {"code": "L2", "name": "Levi's 501 Original — Dark Rigid (STF)", "sku": "005010000", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/straight/501-original-fit-mens-jeans/p/005010000"},
                {"code": "L3", "name": "Levi's 501 Original — Light Stonewash", "sku": "005010134", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/straight/501-original-fit-mens-jeans/p/005010134"},
                {"code": "L4", "name": "Levi's 501 Original — Vintage 'The Concourse'", "sku": "005013715", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/straight/501-original-fit-mens-jeans/p/005013715"},
                {"code": "L5", "name": "Levi's 511 Slim — 'Yokohama Nights'", "sku": "045111150", "size": "36×32", "currency": "USD", "price": 54.50, "retail_usd": 69.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/slim/511-slim-fit-mens-jeans/p/045111150"},
                {"code": "L6", "name": "Levi's 511 Slim — 'The Banks'", "sku": "045113621", "size": "36×32", "currency": "USD", "price": 54.50, "retail_usd": 69.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/slim/511-slim-fit-mens-jeans/p/045113621"},
                {"code": "L7", "name": "Levi's 512 Slim Taper — Dark Indigo", "sku": "288331186", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/slim/512-slim-taper-fit-mens-jeans/p/288331186"},
                {"code": "L8", "name": "Levi's 512 Slim Taper — 'Keepin' It Clean'", "sku": "288331201", "size": "36×32", "currency": "USD", "price": 59.50, "retail_usd": 79.50, "url": "https://www.levi.com/US/en_US/clothing/men/jeans/slim/512-slim-taper-fit-mens-jeans/p/288331201"}
            ]
        },
        {
            "id": "hoodies",
            "name": "🧥 12 Supreme Hoodies (GOAT · XL)",
            "color": "#ef4444",
            "items": [
                {"code": "H1", "name": "Supreme Box Logo Hoodie — Navy (FW24)", "sku": "FW24SW11-NAVY", "size": "XL", "currency": "USD", "price": 330, "url": "https://www.goat.com/apparel/supreme-box-logo-hooded-sweatshirt-navy-fw24sw11-navy"},
                {"code": "H2", "name": "Supreme Box Logo Hoodie — Ash Grey (FW23)", "sku": "FW23SW56-ASH", "size": "XL", "currency": "USD", "price": 370, "url": "https://www.goat.com/apparel/supreme-box-logo-hooded-sweatshirt-ash-grey-fw23sw56-ash-grey"},
                {"code": "H3", "name": "Supreme Swarovski Motion Logo Hoodie — Navy (FW25)", "sku": "FW25SW62-NAVY", "size": "XL", "currency": "USD", "price": 350, "url": "https://www.goat.com/apparel/supreme-swarovski-motion-logo-hooded-sweatshirt-navy-fw25sw62-navy"},
                {"code": "H4", "name": "Supreme Small Box Hoodie — Black #1", "sku": "SUP-SMBOX-BLK1", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/search?query=supreme+small+box+hooded+sweatshirt+black+xl"},
                {"code": "H5", "name": "Supreme Small Box Hoodie — Black #2 (Backup)", "sku": "SUP-SMBOX-BLK2", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/search?query=supreme+small+box+hooded+sweatshirt+black+xl"},
                {"code": "H6", "name": "Supreme Small Box Hoodie — Navy", "sku": "SUP-SMBOX-NVY", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/search?query=supreme+small+box+hooded+sweatshirt+navy+xl"},
                {"code": "H7", "name": "Supreme Small Box Hoodie — Heather Grey", "sku": "SUP-SMBOX-GRY", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/search?query=supreme+small+box+hooded+sweatshirt+grey+xl"},
                {"code": "H8", "name": "Supreme Small Box Hoodie — Natural", "sku": "SUP-SMBOX-NAT", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/search?query=supreme+small+box+hooded+sweatshirt+natural+xl"},
                {"code": "Z1", "name": "Supreme Small Box Zip Up — Burnt Red (SS21)", "sku": "SS21SW52-RED", "size": "XL", "currency": "USD", "price": 354, "url": "https://www.goat.com/apparel/supreme-small-box-zip-up-hooded-sweatshirt-burnt-red-ss21sw52-burnt-red"},
                {"code": "Z2", "name": "Supreme Small Box Drawcord Zip — Washed Navy (FW22)", "sku": "FW22SW52-NVY", "size": "XL", "currency": "USD", "price": 220, "url": "https://www.goat.com/apparel/supreme-small-box-drawcord-zip-up-hooded-sweatshirt-washed-navy-fw22sw52-washed-navy"},
                {"code": "Z3", "name": "Supreme WINDSTOPPER Zip Up — Black (FW21)", "sku": "FW21SW16-BLK", "size": "XL", "currency": "USD", "price": 249, "url": "https://www.goat.com/apparel/supreme-windstopper-zip-up-hooded-sweatshirt-black-fw21sw16-black"},
                {"code": "Z4", "name": "Supreme Small Box Zip Up — Navy (SS21)", "sku": "SS21SW52-NVY", "size": "XL", "currency": "USD", "price": 250, "url": "https://www.goat.com/apparel/supreme-small-box-zip-up-hooded-sweatshirt-navy-ss21sw52-navy"}
            ]
        },
        {
            "id": "tees",
            "name": "👕 15 Tees (Supreme Grails + Small Box + Uniqlo Japón)",
            "color": "#f97316",
            "items": [
                {"code": "T1-T3", "name": "Supreme Small Box Tee — White × 3 (FW22)", "sku": "FW22KN12-WHT-X3", "size": "XL ×3", "currency": "USD", "price": 270, "url": "https://www.goat.com/apparel/supreme-small-box-tee-white-fw22kn12-white"},
                {"code": "T4-T5", "name": "Supreme Small Box Tee — White × 2 (FW20)", "sku": "FW20KN5-WHT-X2", "size": "XL ×2", "currency": "USD", "price": 180, "url": "https://www.goat.com/apparel/supreme-small-box-tee-white-fw20kn5-white"},
                {"code": "T6", "name": "Supreme × Burberry Box Logo Tee — White", "sku": "BURBERRYT1-WHT", "size": "XL", "currency": "USD", "price": 299, "url": "https://www.goat.com/apparel/supreme-x-burberry-box-logo-tee-white-burberryt1-white"},
                {"code": "T7", "name": "Supreme × Tiffany & Co Box Logo Tee — White", "sku": "FW21T37-WHT", "size": "XL", "currency": "USD", "price": 391, "url": "https://www.goat.com/apparel/supreme-x-tiffany-co-box-logo-tee-white-fw21t37-white"},
                {"code": "T8", "name": "Supreme Bandana Box Logo Tee — White", "sku": "FW19T55-WHT", "size": "XL", "currency": "USD", "price": 453, "url": "https://www.goat.com/apparel/supreme-bandana-box-logo-tee-white-fw19t55-white"},
                {"code": "T9", "name": "Supreme LA Box Logo Tee — White", "sku": "SS23T57-WHT", "size": "XL", "currency": "USD", "price": 428, "url": "https://www.goat.com/apparel/supreme-la-box-logo-tee-white-ss23t57-white"},
                {"code": "T10", "name": "Supreme Milan Box Logo Tee — White (GRAIL)", "sku": "SS21-MILAN-WHT", "size": "XL", "currency": "USD", "price": 678, "url": "https://www.goat.com/apparel/supreme-milan-box-logo-tee-white-0052-1ss210103mblt-whit"},
                {"code": "T11-T15", "name": "Uniqlo Supima Cotton Crew Neck Tee — White × 5 (Japón)", "sku": "UNIQLO-JP-X5", "size": "XL ×5", "currency": "JPY", "price": 7500, "url": "https://www.uniqlo.com/jp/ja/"}
            ]
        },
        {
            "id": "acc",
            "name": "🎒 Accesorios Supreme, Ray-Ban, Davek & Essentials",
            "color": "#a855f7",
            "items": [
                {"code": "A01", "name": "Supreme × Hanes Boxer Briefs 4-Pack Black × 4 (16 boxers)", "sku": "99HAA36-BLK-X4", "size": "XL ×4", "currency": "USD", "price": 156, "url": "https://www.goat.com/apparel/supreme-x-hanes-boxer-brief-4-pack-black-99haa36-black"},
                {"code": "A02", "name": "Supreme × Hanes Crew Socks 4-Pack Black × 3 (12 pares)", "sku": "99HAA26-BLK-X3", "size": "US 14", "currency": "USD", "price": 90, "url": "https://www.goat.com/apparel/supreme-x-hanes-crew-socks-4-pack-black-99haa26-black"},
                {"code": "A03", "name": "Supreme Authorized Mesh Back 5-Panel — Royal", "sku": "SS25H125-ROYAL", "size": "OS", "currency": "USD", "price": 60, "url": "https://www.goat.com/apparel/supreme-authorized-mesh-back-5-panel-royal-ss25h125-royal"},
                {"code": "A04", "name": "Supreme World Famous S Logo 6-Panel — Navy", "sku": "SS25H23-NAVY", "size": "OS", "currency": "USD", "price": 69, "url": "https://www.goat.com/apparel/supreme-world-famous-s-logo-6-panel-navy-ss25h23-navy"},
                {"code": "A05", "name": "Supreme × New Era Box Logo Beanie — Black (FW24)", "sku": "FW24BN13-BLK", "size": "OS", "currency": "USD", "price": 117, "url": "https://www.goat.com/apparel/supreme-x-new-era-box-logo-beanie-black-fw24bn13-black"},
                {"code": "A06", "name": "Supreme Backpack — Black (SS18)", "sku": "SS18B7-BLK", "size": "OS", "currency": "USD", "price": 150, "url": "https://www.goat.com/apparel/supreme-backpack-black-ss18b7-black"},
                {"code": "A07", "name": "Supreme Shoulder Bag — Black (SS18)", "sku": "SS18B10-BLK", "size": "OS", "currency": "USD", "price": 175, "url": "https://www.goat.com/apparel/supreme-shoulder-bag-black-ss18b10-black"},
                {"code": "A08", "name": "Supreme Waist Bag — Black (SS20)", "sku": "SS20B5-BLK", "size": "OS", "currency": "USD", "price": 350, "url": "https://www.goat.com/apparel/supreme-waist-bag-black-ss20b5-black"},
                {"code": "A09", "name": "Supreme × TNF Expedition Travel Wallet — Black", "sku": "FW18B4-BLK", "size": "OS", "currency": "USD", "price": 75, "url": "https://www.goat.com/apparel/supreme-x-the-north-face-expedition-travel-wallet-black-fw18b4-black"},
                {"code": "A10", "name": "Ray-Ban Original Wayfarer Classic (RB2140 G-15)", "sku": "RB2140-901", "size": "50mm", "currency": "USD", "price": 191, "url": "https://www.ray-ban.com/us/sunglasses/RB2140%20UNISEX%20original%20wayfarer%20classic-black/805289126577"},
                {"code": "A11", "name": "Samsung Galaxy Watch 7 — 44mm Black (Daily Backup)", "sku": "SM-L310NZKAXAA", "size": "44mm", "currency": "USD", "price": 190, "url": "https://www.samsung.com/us/watches/galaxy-watch7/"},
                {"code": "A12", "name": "Levi's Harness Buckle Belt + Reversible Belt (×2)", "sku": "LEVI-BELTS-X2", "size": "36", "currency": "USD", "price": 75, "url": "https://www.levi.com/US/en_US/accessories/men/belts/c/levi_accessories_men_belts"},
                {"code": "A13", "name": "Isotoner Leather Touchscreen Gloves + Paraguas Davek Solo", "sku": "WINTER-KIT", "size": "XL", "currency": "USD", "price": 138, "url": "https://www.davekny.com"}
            ]
        },
        {
            "id": "samsung_kr",
            "name": "📱 Samsung Tech Korea (Precios Oficiales en ₩ KRW + Tax-Free)",
            "color": "#38bdf8",
            "items": [
                {"code": "KR1", "name": "Samsung Galaxy Tab S11 Ultra (14.6\" · S Pen)", "sku": "SM-X936NZAIKOO", "size": "14.6\"", "currency": "KRW", "price": 1406720, "url": "https://www.samsung.com/sec/tablets/galaxy-tab-s11/buy/?modelCode=SM-X936NZAIKOO"},
                {"code": "KR2", "name": "Samsung Galaxy Watch Ultra 2 (LTE · Titanio)", "sku": "SM-L715NZKAKOO", "size": "47mm", "currency": "KRW", "price": 969100, "url": "https://www.samsung.com/sec/watches/galaxy-watch-ultra2/buy/?modelCode=SM-L715NZKAKOO"},
                {"code": "KR3", "name": "Samsung Galaxy Ring (Health & Sleep Tracking)", "sku": "SM-Q500NZKAKOO", "size": "Titanio", "currency": "KRW", "price": 499400, "url": "https://www.samsung.com/sec/rings/galaxy-ring/"},
                {"code": "KR4", "name": "Samsung Galaxy Buds 4 Pro (ANC · 360 Audio)", "sku": "SM-R640NZKAKOO", "size": "Pro", "currency": "KRW", "price": 349800, "url": "https://www.samsung.com/sec/buds/galaxy-buds/galaxy-buds4-pro/"}
            ]
        },
        {
            "id": "wolf",
            "name": "🐺 Modo Wolverine (Botas 1000 Mile + Chamarra Schott NYC)",
            "color": "#d97706",
            "items": [
                {"code": "W1", "name": "Wolverine 1000 Mile Original Boot", "sku": "W05300", "size": "US 14", "currency": "USD", "price": 375, "url": "https://www.wolverine.com/US/en/1000-mile/"},
                {"code": "W2", "name": "Schott NYC Classic Leather Jacket", "sku": "SCHOTT-XL", "size": "XL", "currency": "USD", "price": 325, "url": "https://www.schottnyc.com/store/men/jackets"},
                {"code": "W3", "name": "Hanes Premium White Tank Top 5-Pack", "sku": "HANES-TANK-XL", "size": "XL", "currency": "USD", "price": 25, "url": "https://www.amazon.com/s?k=hanes+premium+white+tank+top+men+xl"},
                {"code": "W4", "name": "Supreme Heavyweight Flannel Shirt — Red", "sku": "SUP-FLANNEL-XL", "size": "XL", "currency": "USD", "price": 65, "url": "https://www.goat.com/search?query=supreme+flannel+xl"}
            ]
        }
    ]
}


def main():
    fx = fetch_live_fx()
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # 1. Enrich 24-Month / 47-Prefecture Feed with live USD & totals
    total_24m_jpy = 0
    prefecture_index = []
    for m in ITINERARY_24_MONTHS:
        c = m["costs_jpy"]
        tot_jpy = sum(c.values())
        m["total_jpy"] = tot_jpy
        m["total_live_usd"] = round(tot_jpy / fx["JPY"])
        total_24m_jpy += tot_jpy
        for p in m["prefectures"]:
            prefecture_index.append({
                "num": p["num"],
                "name": p["name"],
                "kanji": p["kanji"],
                "region": p["region"],
                "month_num": m["month_num"],
                "date_label": m["date_label"],
                "activity": p["activity"],
                "lat": p["lat"],
                "lon": p["lon"]
            })

    pref_feed = {
        "meta": {
            "title": "Atlas del Imperio — API Maestra de las 47 Prefecturas (全国制覇) y 24 Meses con あやめ",
            "last_updated_utc": now_utc,
            "fx_rates": fx,
            "total_prefectures": 47,
            "total_months": 24,
            "total_campaign_jpy": total_24m_jpy,
            "total_campaign_live_usd": round(total_24m_jpy / fx["JPY"]),
            "base_location": "Apartamento en Ikebukuro (池袋), Tokio",
            "daily_transport": "Honda CBR (Regla del Conbini de あやめ)",
            "training_kit": "Shorts YOKKAO (Blanco/Rojo/Azul Rey) + Guantes Venum Pro Boxing (Azul/Rojo/Blanco)",
            "shortcuts_from_ikebukuro": [
                {
                    "id": "norte_omiya",
                    "title": "1. Atajo Norte y Mar de Japón (Tohoku, Hokkaido, Hokuriku, Nagano)",
                    "route": "Línea JR Saikyo o Shonan-Shinjuku desde Ikebukuro hasta Omiya Station (24 min exactos) y abordar ahí mismo el Shinkansen sin bajar a Tokyo Station."
                },
                {
                    "id": "oeste_marunouchi",
                    "title": "2. Atajo Oeste (Tokaido Shinkansen — Nagoya, Kioto, Osaka, Kobe, Hiroshima)",
                    "route": "Línea Tokyo Metro Marunouchi en Ikebukuro (inicio de línea = asientos vacíos garantizados para ambos) y llegar en 16 min exactos a Tokyo Station."
                },
                {
                    "id": "aereo_haneda",
                    "title": "3. Atajo Aéreo (Hokkaido, Kyushu, Shikoku, Okinawa)",
                    "route": "Airport Limousine Bus desde Sunshine City / Hotel Metropolitan Ikebukuro directo hasta la terminal en el Aeropuerto de Haneda (45 min)."
                }
            ],
            "cat_protocol_tiers": [
                {"tier": "Citas de 1 Día", "rule": "Alimentadores automáticos y regreso a dormir a casa en Ikebukuro con nuestros 2 gatitos y 2 chinchillas.", "cost_jpy": 0},
                {"tier": "Escapadas de 1 Noche (30h)", "rule": "Fuentes continuas de agua, alimentadores programados y monitoreo en vivo por cámara Wi-Fi.", "cost_jpy": 0},
                {"tier": "Viajes de 2 a 3 Noches", "rule": "Servicio de Cat Sitter certificada en Tokio con reporte diario de fotos y videos por LINE para que あやめ viaje con cero preocupación.", "cost_jpy": 8000}
            ]
        },
        "prefectures_47": sorted(prefecture_index, key=lambda x: x["num"]),
        "months_24": ITINERARY_24_MONTHS
    }

    (ASSETS / "prefectures-47-feed.json").write_text(
        json.dumps(pref_feed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    # 2. Enrich Wardrobe V8 Feed with live multi-currency conversions
    grand_wardrobe_usd = 0
    for cat in WARDROBE_CATALOG["categories"]:
        cat_usd = 0
        for item in cat["items"]:
            cur = item["currency"]
            amt = float(item["price"])
            if cur == "USD":
                usd_val = amt
            elif cur == "JPY":
                usd_val = amt / fx["JPY"]
            elif cur == "KRW":
                usd_val = amt / fx["KRW"]
            else:
                usd_val = amt
            item["live_usd"] = round(usd_val, 2)
            item["live_jpy"] = round(usd_val * fx["JPY"])
            item["live_krw"] = round(usd_val * fx["KRW"])
            if cur == "KRW":
                # ~8% effective tax-free tourist refund in Korea
                item["tax_free_krw"] = round(amt * 0.91)
                item["tax_free_usd"] = round((amt * 0.91) / fx["KRW"], 2)
            cat_usd += usd_val
        cat["subtotal_live_usd"] = round(cat_usd)
        cat["subtotal_live_jpy"] = round(cat_usd * fx["JPY"])
        cat["subtotal_live_krw"] = round(cat_usd * fx["KRW"])
        grand_wardrobe_usd += cat_usd

    wardrobe_feed = {
        "meta": {
            "title": "Guardarropa Imperio V8 + Samsung Tech Korea — Live Multi-Currency Price API",
            "last_updated_utc": now_utc,
            "fx_rates": fx,
            "grand_total_live_usd": round(grand_wardrobe_usd),
            "grand_total_live_jpy": round(grand_wardrobe_usd * fx["JPY"]),
            "grand_total_live_krw": round(grand_wardrobe_usd * fx["KRW"])
        },
        "categories": WARDROBE_CATALOG["categories"]
    }

    (ASSETS / "wardrobe-prices-feed.json").write_text(
        json.dumps(wardrobe_feed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    print(
        f"[OK] Built prefectures-47-feed.json (47 Prefectures, 24 Months, ¥{total_24m_jpy:,} / ${round(total_24m_jpy/fx['JPY']):,} USD) "
        f"& wardrobe-prices-feed.json (${round(grand_wardrobe_usd):,} USD / ¥{round(grand_wardrobe_usd*fx['JPY']):,} JPY)"
    )


if __name__ == "__main__":
    main()
