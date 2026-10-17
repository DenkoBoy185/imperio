# -*- coding: utf-8 -*-
"""
Generador Oficial del Dossier y API de Ruteo en Tiempo Real para la Honda CB250R (8BK-MC52)
Fuente Oficial Honda Japón:
- https://www.honda.co.jp/CB250R/type/
- https://www.honda.co.jp/CB250R/spec/
- https://www.honda.co.jp/CB250R/powerunit/
- https://www.honda.co.jp/CB250R/chassis/
- https://www.honda.co.jp/CB250R/equipment/

Genera:
1. assets/cb250r-routes-feed.json (Especificaciones oficiales Honda Japón, colores, CAPEX/OPEX legal 250cc Keijirin 0-Shaken y 28 destinos de la Matriz 168H).
2. assets/cb250r-telemetry-api.js (Mapa interactivo Leaflet + OSRM Street Routing API en vivo + Open-Meteo Tokyo Riding Weather API + Calculadora de Rutina Semanal y Reproductor de Audio Oficial del Escape MC52E).
"""

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

BASES = {
    "asakusabashi": {
        "id": "asakusabashi",
        "name": "Base Principal · Urbanex Asakusabashi Front (台東区柳橋1-13-6)",
        "short_name": "Asakusabashi Front (台東区柳橋)",
        "lat": 35.6975,
        "lon": 139.7863,
        "ward": "Taito-ku / Chuo-riverfront",
        "parking_note": "Estacionamiento de motos residencial / mensual Yanagibashi (¥8,000–¥12,000/mes) a 30m del lobby."
    },
    "ikebukuro": {
        "id": "ikebukuro",
        "name": "Hub Secundario · Ikebukuro Base (豊島区池袋)",
        "short_name": "Ikebukuro Hub (豊島区池袋)",
        "lat": 35.7295,
        "lon": 139.7109,
        "ward": "Toshima-ku",
        "parking_note": "Estacionamiento mensual Ikebukuro Higashi/Nishi (¥9,500/mes) + Sunshine City 24h Bike Parking."
    }
}

CB250R_OFFICIAL_SPECS = {
    "model_name": "Honda CB250R (Neo Sports Café)",
    "tagline_jp": "日常にあたらしい風を吹き込むネイキッドロードスポーツ",
    "tagline_es": "Naked Road Sports que sopla un nuevo viento en tu rutina diaria de Tokio",
    "official_urls": {
        "type_price": "https://www.honda.co.jp/CB250R/type/",
        "spec": "https://www.honda.co.jp/CB250R/spec/",
        "design": "https://www.honda.co.jp/CB250R/design/",
        "powerunit": "https://www.honda.co.jp/CB250R/powerunit/",
        "chassis": "https://www.honda.co.jp/CB250R/chassis/",
        "equipment": "https://www.honda.co.jp/CB250R/equipment/",
        "exhaust_audio_mp3": "https://www.honda.co.jp/CB250R/assets/files/CB250R_sound.mp3"
    },
    "model_code": "ホンダ・8BK-MC52 (Normativa Emisiones Reiwa 2 / Heisei 32)",
    "engine_code": "MC52E",
    "engine_type_jp": "水冷4ストロークDOHC4バルブ単気筒",
    "engine_type_es": "Monocilíndrico 4 tiempos DOHC 4 válvulas refrigerado por líquido",
    "displacement_cc": 249,
    "bore_stroke_mm": "76.0 × 55.0 mm",
    "compression_ratio": 10.7,
    "max_power": "20 kW [27 PS] / 9,500 rpm",
    "max_torque": "23 N·m [2.3 kgf·m] / 7,750 rpm",
    "fuel_system": "PGM-FI (Inyección Electrónica Programada Honda)",
    "fuel_type": "無鉛レギュラーガソリン (Gasolina Regular Sin Plomo · ~¥175/L)",
    "tank_capacity_l": 10.0,
    "fuel_consumption": {
        "wmtc_km_l": 33.7,
        "wmtc_note": "33.7 km/L (Clase 3-1 · 1 pasajero) → 337 km de autonomía real por tanque",
        "constant_60kmh_km_l": 45.0,
        "constant_note": "45.0 km/L (a 60 km/h constantes · 2 pasajeros) → hasta 450 km de autonomía"
    },
    "transmission": "6 velocidades de retorno (常時噛合式6段リターン) + Assist & Slipper® Clutch (アシスト＆スリッパー®クラッチ)",
    "dimensions": {
        "length_mm": 2020,
        "width_mm": 805,
        "height_mm": 1045,
        "wheelbase_mm": 1355,
        "ground_clearance_mm": 153,
        "seat_height_mm": 795,
        "curb_weight_kg": 144,
        "min_turning_radius_m": 2.3,
        "seating_capacity": 2
    },
    "chassis_and_brakes": {
        "frame": "Chasis tipo Diamante en acero de alta tensión (高張力鋼ダイヤモンドフレーム) con placas de pivote independientes",
        "front_suspension": "Horquilla invertida Showa (Hitachi Astemo) SFF-BP (Separate Function Front Fork - Big Piston) φ41 mm",
        "rear_suspension": "Basculante de acero de alta tensión con eje hueco φ20 mm + Monoshock de cámara separada con 7 niveles de precarga",
        "front_brake": "Disco flotante lobulado sin buje φ296 mm + Pinza radial de 4 pistones opuestos",
        "rear_brake": "Disco hidráulico lobulado φ220 mm",
        "abs_system": "IMU-linked 2-Channel ABS (車体姿勢推定システム付ABS · Supresión de levantamiento trasero en frenada de emergencia)",
        "tires_front": "110/70R17M/C 54H (Radial)",
        "tires_rear": "150/60R17M/C 66H (Radial)",
        "handlebar": "Manillar cónico de aluminio (テーパーハンドル φ28.6 mm en torretas → φ22.2 mm en puños)",
        "instrument_panel": "Pantalla LCD Digital Multifunción con Indicador de Marcha (1–6), Shift-Up Indicator programable y Peak Hold de RPM"
    },
    "pricing_japan": {
        "msrp_tax_included_jpy": 564300,
        "msrp_pre_tax_jpy": 513000,
        "estimated_on_road_jpy": 625000,
        "jibaiseki_3yr_jpy": 12220,
        "weight_tax_one_time_jpy": 4900,
        "annual_road_tax_jpy": 3600,
        "shaken_inspection_jpy": 0,
        "shaken_note": "Categoría 軽二輪 (249cc <= 250cc): 100% EXENTA DE SHAKEN (車検不要) de por vida y 100% legal en autopistas (首都高 / 高速道路)."
    },
    "official_colors": [
        {
            "id": "black",
            "name_jp": "マットガンパウダーブラックメタリック",
            "name_en": "Matte Gunpowder Black Metallic",
            "badge": "Edición Sigilo · Godzilla 1954 Spec (Recomendada)",
            "hex": "#2a2d34",
            "accent_hex": "#9ca3af",
            "image_url": "https://www.honda.co.jp/CB250R/assets/images/type/black.png",
            "swatch_url": "https://www.honda.co.jp/CB250R/assets/images/type/color-01.png",
            "notes": "Acabado negro mate íntegro con barras de horquilla Showa SFF-BP oscurecidas; combina con tu estética ShodaiGoji 1954."
        },
        {
            "id": "blue",
            "name_jp": "マットパールアジャイルブルー",
            "name_en": "Matte Pearl Agile Blue",
            "badge": "Azul Rey Mate · Horquilla Dorada Showa",
            "hex": "#1d4ed8",
            "accent_hex": "#f59e0b",
            "image_url": "https://www.honda.co.jp/CB250R/assets/images/type/blue.png",
            "swatch_url": "https://www.honda.co.jp/CB250R/assets/images/type/color-08.png",
            "notes": "Azul rey mate perlado que hace juego exacto con tus guantes Venum Pro Boxing y shorts YOKKAO azul/rojo/blanco."
        },
        {
            "id": "red",
            "name_jp": "キャンディークロモスフィアレッド",
            "name_en": "Candy Chromosphere Red",
            "badge": "Rojo Caramelo · Horquilla Dorada Showa",
            "hex": "#dc2626",
            "accent_hex": "#f59e0b",
            "image_url": "https://www.honda.co.jp/CB250R/assets/images/type/red.png",
            "swatch_url": "https://www.honda.co.jp/CB250R/assets/images/type/color-02.png",
            "notes": "Rojo metálico profundo de alta visibilidad nocturna en Tokio con botellas Showa SFF-BP doradas."
        }
    ]
}

DESTINATIONS = [
    # 1. MMA & ENTRENAMIENTO
    {
        "id": "fighters_flow",
        "category": "mma",
        "category_label": "🥊 MMA & Entrenamiento (6-0)",
        "name": "FIGHTER'S FLOW (Takadanobaba · 高田馬場)",
        "subtitle": "Sede Central MMA & 1-a-1 con Hayato Suzuki + Regla del Conbini de あやめ",
        "lat": 35.7126,
        "lon": 139.7038,
        "address": "Shinjuku-ku, Takadanobaba 1-chome",
        "schedule_slot": "Lun–Vie 11:00–13:30 JST (Campamento) + Sáb 11:00–12:30 JST (1-a-1 Hayato Suzuki)",
        "trips_per_week": 6,
        "asakusabashi": {"km": 9.4, "cb250r_min": 18, "train_min": 31, "highway": False},
        "ikebukuro": {"km": 2.8, "cb250r_min": 8, "train_min": 14, "highway": False},
        "parking_spot": "Takadanobaba Station Municipal Bike Parking (高田馬場駅駐輪場 · ¥100/día, primeros 120 min gratis)",
        "tactical_note": "Terminas de entrenar a las 13:30, guardas tus guantes Venum en la maleta/mochila rígida y en 18 min estás duchándote en casa sin oler a sudor en el tren."
    },
    {
        "id": "kodokan_judo",
        "category": "mma",
        "category_label": "🥊 MMA & Entrenamiento (6-0)",
        "name": "Kodokan Judo Institute (講道館 · Kasuga/Korakuen)",
        "subtitle": "Meca Mundial del Judo — Derribos, Ashi-Waza y Control de Clinch",
        "lat": 35.7077,
        "lon": 139.7533,
        "address": "1-16-30 Kasuga, Bunkyo-ku, Tokyo",
        "schedule_slot": "Sesiones técnicas complementarias de derribo (Randori vespertino)",
        "trips_per_week": 2,
        "asakusabashi": {"km": 3.8, "cb250r_min": 9, "train_min": 21, "highway": False},
        "ikebukuro": {"km": 4.9, "cb250r_min": 12, "train_min": 18, "highway": False},
        "parking_spot": "Tokyo Dome City / Kasuga Bike Lot (春日駐輪場 · a 80m del Kodokan)",
        "tactical_note": "Ruta directa por Kuramae-hashi Dori / Kasuga Dori sin transbordos."
    },
    {
        "id": "triforce_bjj",
        "category": "mma",
        "category_label": "🥊 MMA & Entrenamiento (6-0)",
        "name": "Tri-Force BJJ Asakusabashi (トライフォース浅草橋)",
        "subtitle": "Jiu-Jitsu Brasileño y Defensa de Sumisiones a 350m de tu Edificio",
        "lat": 35.6980,
        "lon": 139.7845,
        "address": "Asakusabashi 1-chome, Taito-ku, Tokyo",
        "schedule_slot": "Drills técnicos de suelo / No-Gi grappling",
        "trips_per_week": 2,
        "asakusabashi": {"km": 0.4, "cb250r_min": 2, "train_min": 5, "highway": False},
        "ikebukuro": {"km": 9.8, "cb250r_min": 20, "train_min": 28, "highway": False},
        "parking_spot": "En tu propio edificio Urbanex Asakusabashi Front (a 3 min caminando)",
        "tactical_note": "Desde Asakusabashi puedes ir caminando en 3 min; desde Ikebukuro llegas en 20 min en la CB250R."
    },
    {
        "id": "golds_gym_conditioning",
        "category": "mma",
        "category_label": "🥊 MMA & Entrenamiento (6-0)",
        "name": "Gold's Gym North Tokyo / Anytime Fitness (Pesas & Corte a 77 kg)",
        "subtitle": "Fuerza Explosiva, Sauna de Control Hídrico y Báscula Digital",
        "lat": 35.7312,
        "lon": 139.7145,
        "address": "Higashi-Ikebukuro 1-chome, Toshima-ku, Tokyo",
        "schedule_slot": "Mar / Jue / Dom — Acondicionamiento físico y chequeo de 79 kg → 77 kg",
        "trips_per_week": 3,
        "asakusabashi": {"km": 9.6, "cb250r_min": 19, "train_min": 29, "highway": False},
        "ikebukuro": {"km": 0.7, "cb250r_min": 3, "train_min": 8, "highway": False},
        "parking_spot": "Higashi-Ikebukuro Underground Bike Parking (東池袋地下駐輪場)",
        "tactical_note": "Ideal para combinar con salida o compras en Ikebukuro junto a あやめ."
    },

    # 2. ABASTO HIPER-CARNÍVORO & NUTRICIÓN 168H
    {
        "id": "hanamasa_asakusabashi",
        "category": "nutrition",
        "category_label": "🥩 Abasto Hiper-Carnívoro & Comidas",
        "name": "Niku no Hanamasa Asakusabashi (肉のハナマサ 浅草橋店 · 24H)",
        "subtitle": "Central Mayorista de Carne 24 Horas — Ribeye, Lomo, Pollo y Huevos por Caja",
        "lat": 35.6974,
        "lon": 139.7858,
        "address": "Asakusabashi 1-chome, Taito-ku, Tokyo",
        "schedule_slot": "Abasto cada 48h (14:00 JST post-entreno o 20:00 JST)",
        "trips_per_week": 4,
        "asakusabashi": {"km": 0.3, "cb250r_min": 1, "train_min": 3, "highway": False},
        "ikebukuro": {"km": 10.1, "cb250r_min": 21, "train_min": 29, "highway": False},
        "parking_spot": "Frente a tienda / Yanagibashi Home Parking (carga rápida en mochila térmica)",
        "tactical_note": "0 Alcohol 🚫🍺 y 0 Mango 🚫🥭. Aquí compras tus bloques de 2 kg de carne de res y pechuga para mantener 210g+ de proteína diaria."
    },
    {
        "id": "hanamasa_ikebukuro",
        "category": "nutrition",
        "category_label": "🥩 Abasto Hiper-Carnívoro & Comidas",
        "name": "Niku no Hanamasa Ikebukuro (肉のハナマサ 池袋店 · 24H)",
        "subtitle": "Sucursal Mayorista Norte cuando regresas de FIGHTER'S FLOW",
        "lat": 35.7332,
        "lon": 139.7075,
        "address": "Ikebukuro 2-chome, Toshima-ku, Tokyo",
        "schedule_slot": "Escala rápida de 5 min al salir de Takadanobaba",
        "trips_per_week": 2,
        "asakusabashi": {"km": 10.5, "cb250r_min": 21, "train_min": 33, "highway": False},
        "ikebukuro": {"km": 0.8, "cb250r_min": 3, "train_min": 9, "highway": False},
        "parking_spot": "Bahía lateral de carga rápida Niku no Hanamasa Ikebukuro",
        "tactical_note": "Aplicas literal la 'Regla del Conbini de あやめ': paras con la CB250R, compras en 4 minutos y sigues directo a casa."
    },
    {
        "id": "steakhouse_ryuho",
        "category": "nutrition",
        "category_label": "🥩 Abasto Hiper-Carnívoro & Comidas",
        "name": "Steakhouse Ryuho & Little Butcher (浅草橋 ステーキ柳鳳)",
        "subtitle": "Teppanyaki Wagyu Magro & Cortes Carnívoros de Premio Post-Sparring",
        "lat": 35.6979,
        "lon": 139.7860,
        "address": "Yanagibashi 1-chome, Taito-ku, Tokyo",
        "schedule_slot": "Almuerzos de carga limpia (14:00 JST) o cena con あやめ",
        "trips_per_week": 2,
        "asakusabashi": {"km": 0.2, "cb250r_min": 1, "train_min": 2, "highway": False},
        "ikebukuro": {"km": 10.2, "cb250r_min": 21, "train_min": 30, "highway": False},
        "parking_spot": "En casa (a 120 metros a pie de Urbanex Asakusabashi Front)",
        "tactical_note": "Proteína pura recién salida de la plancha sin salsas azucaradas."
    },
    {
        "id": "ootoya_uogashi_akiba",
        "category": "nutrition",
        "category_label": "🥩 Abasto Hiper-Carnívoro & Comidas",
        "name": "Ootoya & Uogashi Nihon-Ichi Akihabara (大戸屋・魚がし日本一 秋葉原)",
        "subtitle": "Pescado a la Parrilla, Sashimi de Atún/Salmón y Huevos en Semana de Corte",
        "lat": 35.6988,
        "lon": 139.7742,
        "address": "Kanda Sakumacho, Chiyoda-ku, Tokyo",
        "schedule_slot": "Almuerzo/Cena rápida entre bloques de Stream y Citas",
        "trips_per_week": 3,
        "asakusabashi": {"km": 1.3, "cb250r_min": 4, "train_min": 10, "highway": False},
        "ikebukuro": {"km": 8.9, "cb250r_min": 18, "train_min": 24, "highway": False},
        "parking_spot": "UDX Akihabara Motorcycle Parking (秋葉原UDXバイク駐車場 · 24h cubierto)",
        "tactical_note": "En 4 minutos en la CB250R estás estacionado bajo techo en Akihabara UDX."
    },
    {
        "id": "costco_makuhari",
        "category": "nutrition",
        "category_label": "🥩 Abasto Hiper-Carnívoro & Comidas",
        "name": "Costco Wholesale Makuhari (コストコ幕張 · Vía Shuto Expressway)",
        "subtitle": "Abasto Mensual Masivo: Sakura Chicken Breast, Salmón Noruego y Whey Isolate",
        "lat": 35.6562,
        "lon": 140.0294,
        "address": "1-4 Toyosuna, Mihama-ku, Chiba",
        "schedule_slot": "1 Sábado al mes (13:00 JST) por autopista costera",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 27.5, "cb250r_min": 26, "train_min": 58, "highway": True},
        "ikebukuro": {"km": 36.4, "cb250r_min": 35, "train_min": 72, "highway": True},
        "parking_spot": "Costco Makuhari Dedicated Free Motorcycle Zone (Gratis)",
        "tactical_note": "Aquí brilla el motor de 249cc (27 PS): subes legalmente a la Shuto Expressway Route 7 / Higashi-Kanto y llegas en menos de la mitad del tiempo que en tren."
    },

    # 3. SALUD, BIENESTAR & TELAS DE あやめ
    {
        "id": "ai_clinic_kanda",
        "category": "ayame_care",
        "category_label": "🌸 Salud, Bienestar & Telas de あやめ",
        "name": "Ai Clinic Kanda (アイクリニック神田 · Dra. Nishimatsu)",
        "subtitle": "Control Ginecológico Especializado y Tratamiento PMDD de あやめ",
        "lat": 35.6918,
        "lon": 139.7709,
        "address": "Kanda Kajicho, Chiyoda-ku, Tokyo",
        "schedule_slot": "1 visita mensual programada con acompañamiento de Bruno",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 1.8, "cb250r_min": 5, "train_min": 14, "highway": False},
        "ikebukuro": {"km": 8.8, "cb250r_min": 18, "train_min": 25, "highway": False},
        "parking_spot": "Kanda Station East Bike Meter Parking (神田駅東口パーキングメーター)",
        "tactical_note": "Cero estrés ni empujones de vagón para あやめ en sus días sensibles."
    },
    {
        "id": "counseling_haco",
        "category": "ayame_care",
        "category_label": "🌸 Salud, Bienestar & Telas de あやめ",
        "name": "Counseling Room haco / Terapia Clínica (神田・秋葉原)",
        "subtitle": "Sesiones Individuales y de Pareja (Blindaje Emocional y Paz en Casa)",
        "lat": 35.6935,
        "lon": 139.7720,
        "address": "Kanda Sudacho, Chiyoda-ku, Tokyo",
        "schedule_slot": "Martes / Jueves 17:30–18:30 JST (Justo al terminar tu Stream de Kick)",
        "trips_per_week": 2,
        "asakusabashi": {"km": 1.6, "cb250r_min": 5, "train_min": 13, "highway": False},
        "ikebukuro": {"km": 8.6, "cb250r_min": 17, "train_min": 24, "highway": False},
        "parking_spot": "Kanda Sudacho Bike Parking (神田須田町駐輪場)",
        "tactical_note": "Cierras directo en Kick a las 17:00, tomas la CB250R y en 5 minutos exactos estás en consulta."
    },
    {
        "id": "nippori_textile_town",
        "category": "ayame_care",
        "category_label": "🌸 Salud, Bienestar & Telas de あやめ",
        "name": "Nippori Textile Town · Tomato & Nagato (日暮里繊維街)",
        "subtitle": "Seda Habutai 100%, Hilos Dorados y Terciopelo para Kimono Mothra 1961 & Bata Godzilla 1954",
        "lat": 35.7278,
        "lon": 139.7725,
        "address": "Higashi-Nippori 5-chome, Arakawa-ku, Tokyo",
        "schedule_slot": "Miércoles o Sábado por la tarde con あやめ (Compras de confección)",
        "trips_per_week": 1,
        "asakusabashi": {"km": 4.1, "cb250r_min": 9, "train_min": 19, "highway": False},
        "ikebukuro": {"km": 6.4, "cb250r_min": 14, "train_min": 16, "highway": False},
        "parking_spot": "Nippori Station Port Tower Bike Parking (日暮里駅駐輪場 · primeros 120 min gratis)",
        "tactical_note": "Llevas los rollos de seda japonesa sin que se arruguen en el metro."
    },
    {
        "id": "coto_academy_iidabashi",
        "category": "ayame_care",
        "category_label": "🌸 Salud, Bienestar & Telas de あやめ",
        "name": "Coto Japanese Academy Iidabashi (飯田橋 · Clases JLPT N2)",
        "subtitle": "Dominio del Japonés para Negocios, Entrevistas Post-Pelea y Familia de あやめ",
        "lat": 35.7018,
        "lon": 139.7445,
        "address": "Iidabashi 4-chome, Chiyoda-ku, Tokyo",
        "schedule_slot": "3 sesiones por semana (Presencial / Híbrido)",
        "trips_per_week": 2,
        "asakusabashi": {"km": 4.4, "cb250r_min": 10, "train_min": 16, "highway": False},
        "ikebukuro": {"km": 5.3, "cb250r_min": 12, "train_min": 15, "highway": False},
        "parking_spot": "Iidabashi Ramla Bike Parking (飯田橋ラムラ駐輪場)",
        "tactical_note": "Al terminar clase estás a 2 minutos de Kagurazaka para cenar con あやめ."
    },
    {
        "id": "exotic_vet_bunkyo",
        "category": "ayame_care",
        "category_label": "🌸 Salud, Bienestar & Telas de あやめ",
        "name": "Clínica Veterinaria Felina & Exóticos (文京・台東 動物病院)",
        "subtitle": "Cuidado Preventivo para los 2 Gatitos y las 2 Chinchillas de あやめ",
        "lat": 35.7042,
        "lon": 139.7615,
        "address": "Hongo / Yushima, Bunkyo-ku, Tokyo",
        "schedule_slot": "Revisión preventiva mensual y resguardo veterinario",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 2.9, "cb250r_min": 7, "train_min": 18, "highway": False},
        "ikebukuro": {"km": 6.2, "cb250r_min": 14, "train_min": 21, "highway": False},
        "parking_spot": "Estacionamiento propio de la clínica veterinaria",
        "tactical_note": "Para ir por medicamentos, alimento premium o timothy hay para las chinchillas en minutos."
    },

    # 4. LAS 4 CITAS SEMANALES CON あやめ & SPOTS IRL (YOUTUBE / KICK +$15K/MES)
    {
        "id": "sunshine_city_ikebukuro",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Sunshine City Ikebukuro (サンシャイン水族館 & プラネタリウム満天)",
        "subtitle": "Cita Semanal #1: Acuario Nocturno de Medusas, Planetario Manten en Camas Nube y Pokémon Center",
        "lat": 35.7289,
        "lon": 139.7196,
        "address": "3-1 Higashi-Ikebukuro, Toshima-ku, Tokyo",
        "schedule_slot": "Miércoles 18:00–21:00 JST (Cita Corta #1 + B-Roll Cinematográfico 4K)",
        "trips_per_week": 1,
        "asakusabashi": {"km": 9.1, "cb250r_min": 18, "train_min": 29, "highway": False},
        "ikebukuro": {"km": 0.9, "cb250r_min": 3, "train_min": 10, "highway": False},
        "parking_spot": "Sunshine City B1 Motorcycle Parking (サンシャインシティバイク駐車場 · 30 min ¥100)",
        "tactical_note": "Regreso garantizado a casa a las 21:20 JST para cumplir la regla sagrada de dormir a las 22:30 JST."
    },
    {
        "id": "akihabara_kanda_myojin",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Akihabara Radio Kaikan, Eorzea Cafe & Kanda Myojin (秋葉原・神田明神)",
        "subtitle": "Cita Semanal #2: Figuras Retro, Santuario de la Prosperidad IT/Empresarial y Stream IRL",
        "lat": 35.6984,
        "lon": 139.7731,
        "address": "1-15-16 Sotokanda / 2-16-2 Sotokanda, Chiyoda-ku, Tokyo",
        "schedule_slot": "Jueves 18:00–21:00 JST (Cita Geek con あやめ + Stream IRL en Kick)",
        "trips_per_week": 1,
        "asakusabashi": {"km": 1.4, "cb250r_min": 4, "train_min": 11, "highway": False},
        "ikebukuro": {"km": 8.7, "cb250r_min": 17, "train_min": 23, "highway": False},
        "parking_spot": "Akihabara UDX Motorcycle Parking (秋葉原UDX · ¥600 máx 24h)",
        "tactical_note": "Uno de los mejores escenarios nocturnos de neón en todo Japón para grabar con tu Sony ZV-E1 / DJI Osmo Pocket 3."
    },
    {
        "id": "ginza_wako_motoji",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Ginza 4-Chome: Torre del Reloj Wako & Ginza Motoji (銀座四丁目・和光・もとじ)",
        "subtitle": "Cita de Viernes #3: El Cruce Exacto de Godzilla 1954 + Alta Sastrería de Kimonos para あやめ",
        "lat": 35.6712,
        "lon": 139.7650,
        "address": "Ginza 4-chome, Chuo-ku, Tokyo",
        "schedule_slot": "Viernes 18:30–21:30 JST (Cena Wagyu A5 en Ginza y Paseo Nocturno)",
        "trips_per_week": 1,
        "asakusabashi": {"km": 4.2, "cb250r_min": 11, "train_min": 20, "highway": False},
        "ikebukuro": {"km": 10.4, "cb250r_min": 21, "train_min": 26, "highway": False},
        "parking_spot": "Ginza Six Motorcycle Parking / Higashi-Ginza Underground Bike Lot (東銀座地下駐車場)",
        "tactical_note": "Aquí grabas el documental pre-pelea de tu entrada escénica 'Ginza 1954: Godzilla & Mothra'."
    },
    {
        "id": "kagurazaka_hanamachi",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Kagurazaka Hanamachi (神楽坂 花街 · Callejones de Geishas Hyogo-Yokocho)",
        "subtitle": "Cita Tradicional: Empedrado Histórico de Geishas, Ryotei Privado y Faroles de Papel",
        "lat": 35.7022,
        "lon": 139.7392,
        "address": "Kagurazaka 3-chome, Shinjuku-ku, Tokyo",
        "schedule_slot": "Sábado 17:30–21:00 JST (Cita de Fin de Semana en Tokio)",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 4.8, "cb250r_min": 11, "train_min": 22, "highway": False},
        "ikebukuro": {"km": 4.6, "cb250r_min": 11, "train_min": 18, "highway": False},
        "parking_spot": "Kagurazaka Station Bike Parking (神楽坂駅駐輪場)",
        "tactical_note": "Con un radio de giro de solo 2.3m, la CB250R entra y estaciona sin esfuerzo junto a las cuestas históricas de Kagurazaka."
    },
    {
        "id": "asakusa_kannonura",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Asakusa Kannon-ura Hanamachi & Sumida River Walk (浅草観音裏・隅田川)",
        "subtitle": "Distrito de Geishas de Asakusa (Kenban), Senso-ji Iluminado de Noche sin Turistas y Río Sumida",
        "lat": 35.7168,
        "lon": 139.7966,
        "address": "Asakusa 3-chome, Taito-ku, Tokyo",
        "schedule_slot": "Paseo nocturno 19:30–21:15 JST",
        "trips_per_week": 1,
        "asakusabashi": {"km": 2.6, "cb250r_min": 7, "train_min": 15, "highway": False},
        "ikebukuro": {"km": 9.9, "cb250r_min": 20, "train_min": 31, "highway": False},
        "parking_spot": "Kaminarimon Underground Motorcycle Parking (雷門地下駐輪場)",
        "tactical_note": "A las 20:00 hrs Senso-ji está vacío e iluminado: tomas épicas de tu Honda CB250R junto a Tokyo Skytree."
    },
    {
        "id": "hinode_symphony_cruise",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Hinode Pier · Crucero Nocturno Symphony Tokyo Bay (日の出ふ頭)",
        "subtitle": "Embarque para Cena Francesa Navegando Bajo el Rainbow Bridge con あやめ",
        "lat": 35.6525,
        "lon": 139.7615,
        "address": "2-7-104 Kaigan, Minato-ku, Tokyo",
        "schedule_slot": "Sábado de Gala 18:30–21:30 JST (0 Alcohol: Mocktails de Autor)",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 6.4, "cb250r_min": 15, "train_min": 29, "highway": False},
        "ikebukuro": {"km": 12.8, "cb250r_min": 25, "train_min": 39, "highway": True},
        "parking_spot": "Hinode Pier Terminal Motorcycle Space (日の出客船ターミナル駐輪スペース)",
        "tactical_note": "Ahorras 14 minutos por trayecto y evitas la caminata desde Hamamatsucho Station en noches de viento."
    },
    {
        "id": "toyosu_senkyakubanrai",
        "category": "dates_irl",
        "category_label": "💑 Citas con あやめ & Grabación YouTube/Kick",
        "name": "Toyosu Senkyakubanrai & teamLab Planets (豊洲 千客万来・チームラボ)",
        "subtitle": "Onsen Privado con Vista a la Bahía de Tokio (Manyo Club) y Arte Digital Inmersivo",
        "lat": 35.6492,
        "lon": 139.7898,
        "address": "6-5-1 Toyosu, Koto-ku, Tokyo",
        "schedule_slot": "Domingo de Recuperación Muscular y Cita con あやめ (15:00–20:00 JST)",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 6.8, "cb250r_min": 16, "train_min": 34, "highway": False},
        "ikebukuro": {"km": 14.5, "cb250r_min": 27, "train_min": 42, "highway": True},
        "parking_spot": "Toyosu Senkyakubanrai Dedicated Bike Parking (千客万来駐輪場 · primeras 2h gratis)",
        "tactical_note": "En tren requiere 2 transbordos (Yurikamome); en tu CB250R cruzas los puentes de la bahía en 16 minutos."
    },

    # 5. ARENAS MMA (6-0) & HUBS DE SALIDA NACIONAL (47 PREFECTURAS)
    {
        "id": "korakuen_hall",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Korakuen Hall / Tokyo Dome City (後楽園ホール · Arena Sagrada)",
        "subtitle": "Sede Histórica de Shooto, DEEP y Carteleras Estelares en Tokio",
        "lat": 35.7056,
        "lon": 139.7519,
        "address": "1-3-61 Koraku, Bunkyo-ku, Tokyo",
        "schedule_slot": "Pesajes Oficiales (77.0 kg), Estudio de Rivales y Noches de Pelea",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 3.6, "cb250r_min": 8, "train_min": 16, "highway": False},
        "ikebukuro": {"km": 5.1, "cb250r_min": 12, "train_min": 17, "highway": False},
        "parking_spot": "Tokyo Dome LaQua Motorcycle Parking (ラクーアバイク駐車場)",
        "tactical_note": "A solo 8 minutos de casa para llegar fresco al pesaje oficial en 77.0 kg."
    },
    {
        "id": "shinjuku_face",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Shinjuku FACE (新宿FACE · Sede KROSS×OVER & DEEP Future King)",
        "subtitle": "Escenario de tu Debut 77 kg (Abril 2028) y Torneo DEEP Future King (Diciembre 2028)",
        "lat": 35.6955,
        "lon": 139.7031,
        "address": "1-20-1 Kabukicho, Shinjuku-ku, Tokyo (Humax Pavilion 7F)",
        "schedule_slot": "Reconocimiento de Arena, Pesajes y Peleas #1, #3 y #4",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 9.2, "cb250r_min": 19, "train_min": 27, "highway": False},
        "ikebukuro": {"km": 4.5, "cb250r_min": 11, "train_min": 15, "highway": False},
        "parking_spot": "Shinjuku Subnade / Kabukicho Public Bike Parking (西武新宿駅前駐輪場)",
        "tactical_note": "Donde estrenas la producción de 70 segundos 'Ginza 1954: Godzilla & Mothra' junto a あやめ."
    },
    {
        "id": "tokyo_station_shinkansen",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Tokyo Station (東京駅 · Hub Tokaido Shinkansen hacia el Oeste)",
        "subtitle": "Salida hacia Kioto, Osaka, Kobe, Nagoya, Shizuoka, Hiroshima y Okayama",
        "lat": 35.6812,
        "lon": 139.7671,
        "address": "1-9 Marunouchi, Chiyoda-ku, Tokyo",
        "schedule_slot": "Sábados 07:30 JST en fines de semana de Expedición Nacional",
        "trips_per_week": 0.5,
        "asakusabashi": {"km": 3.1, "cb250r_min": 8, "train_min": 14, "highway": False},
        "ikebukuro": {"km": 8.9, "cb250r_min": 19, "train_min": 16, "highway": False},
        "parking_spot": "Yaesu Underground Motorcycle Parking (八重洲地下街バイク駐車場 · techado y vigilado)",
        "tactical_note": "Conecta directo con el Atajo #2 (Marunouchi Line 16 min desde Ikebukuro o 8 min desde Asakusabashi)."
    },
    {
        "id": "omiya_shinkansen_hub",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Omiya Station Hub (大宮駅 · Atajo Shinkansen Norte & Mar de Japón)",
        "subtitle": "Puerta Norte hacia Tohoku (Sendai/Aomori), Hokkaido (Hakodate), Kanazawa y Nagano",
        "lat": 35.9063,
        "lon": 139.6240,
        "address": "錦町 630, Omiya-ku, Saitama",
        "schedule_slot": "Atajo Estratégico #1 para Expediciones del Norte",
        "trips_per_week": 0.25,
        "asakusabashi": {"km": 29.8, "cb250r_min": 31, "train_min": 42, "highway": True},
        "ikebukuro": {"km": 22.4, "cb250r_min": 24, "train_min": 24, "highway": True},
        "parking_spot": "Omiya Station West Exit Municipal Bike Parking (大宮駅西口駐輪場)",
        "tactical_note": "Por la Shuto Expressway Route S5 Saitama Omiya llegas volando con la CB250R."
    },
    {
        "id": "haneda_airport",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Aeropuerto Internacional de Haneda (羽田空港 · Terminales 1, 2 y 3)",
        "subtitle": "Vuelos Nacionales JAL/ANA hacia Kyushu, Shikoku, San'in, Hokkaido y Okinawa (Kadena O-3)",
        "lat": 35.5494,
        "lon": 139.7798,
        "address": "Hanedakuko, Ota-ku, Tokyo",
        "schedule_slot": "Expediciones Aéreas de las 47 Prefecturas (Viernes tarde / Sábado 07:00 JST)",
        "trips_per_week": 0.25,
        "asakusabashi": {"km": 21.4, "cb250r_min": 24, "train_min": 41, "highway": True},
        "ikebukuro": {"km": 28.9, "cb250r_min": 33, "train_min": 52, "highway": True},
        "parking_spot": "Haneda Airport P1–P4 Dedicated Motorcycle Zone (羽田空港バイク駐車場 · ¥500/día máx)",
        "tactical_note": "Por la Shuto Expressway B (Bayshore Route) llegas en 24 min desde Asakusabashi directo a la terminal."
    },
    {
        "id": "shinkiba_tokyo_heliport",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Helipuerto de Tokio Shin-Kiba (東京ヘリポート 新木場 · Gala 6-0)",
        "subtitle": "Vuelo Nocturno Privado en Helicóptero sobre Tokyo Tower y Rainbow Bridge (Retiro Invicto Sep 2029)",
        "lat": 35.6358,
        "lon": 139.8390,
        "address": "4-7-25 Shinkiba, Koto-ku, Tokyo",
        "schedule_slot": "Expedición #24 (Septiembre 2029) — Cierre del 6-0 antes de Okinawa O-3",
        "trips_per_week": 0.1,
        "asakusabashi": {"km": 11.8, "cb250r_min": 18, "train_min": 38, "highway": True},
        "ikebukuro": {"km": 19.6, "cb250r_min": 28, "train_min": 49, "highway": True},
        "parking_spot": "Tokyo Heliport Visitor Parking (東京ヘリポート駐車場 · Gratis)",
        "tactical_note": "En transporte público hay que tomar tren + autobús en Shin-Kiba; en moto o taxi llegas directo al hangar en 18 min."
    },
    {
        "id": "hakone_odawara_touring",
        "category": "arenas_hubs",
        "category_label": "🏟️ Arenas MMA & Hubs Shinkansen/Vuelos",
        "name": "Ruta Touring: Hakone Ashinoko & Monte Fuji (箱根・芦ノ湖スカイライン)",
        "subtitle": "Escapada en la CB250R por la Tomei Expressway hacia Ryokan con Onsen Privado",
        "lat": 35.2041,
        "lon": 139.0256,
        "address": "Moto-Hakone, Ashigarashimo-gun, Kanagawa",
        "schedule_slot": "Fines de semana de aire limpio de montaña pre-campamento",
        "trips_per_week": 0.25,
        "asakusabashi": {"km": 92.0, "cb250r_min": 78, "train_min": 108, "highway": True},
        "ikebukuro": {"km": 89.5, "cb250r_min": 75, "train_min": 102, "highway": True},
        "parking_spot": "Hakone Sightseeing Boat Moto-Hakone Free Bike Parking",
        "tactical_note": "Con un solo tanque de 10L (337–450 km de autonomía) vas desde Tokio hasta el Lago Ashi, recorres el Hakone Skyline y regresas a Tokio sin repostar."
    }
]

GAS_PRICE_JPY_PER_L = 175.0
FX_DEFAULT = 158.2
WMTC_KM_PER_L = CB250R_OFFICIAL_SPECS["fuel_consumption"]["wmtc_km_l"]
CRUISE_KM_PER_L = CB250R_OFFICIAL_SPECS["fuel_consumption"]["constant_60kmh_km_l"]

for d in DESTINATIONS:
    for base_key in ("asakusabashi", "ikebukuro"):
        b = d[base_key]
        km = b["km"]
        # One-way fuel in liters & mL (WMTC 33.7 km/L)
        liters_one_way = round(km / WMTC_KM_PER_L, 3)
        ml_one_way = int(round(liters_one_way * 1000))
        cost_jpy_one_way = int(round(liters_one_way * GAS_PRICE_JPY_PER_L))
        time_saved_one_way = max(0, b["train_min"] - b["cb250r_min"])
        b["fuel_liters_one_way"] = liters_one_way
        b["fuel_ml_one_way"] = ml_one_way
        b["fuel_cost_jpy_one_way"] = cost_jpy_one_way
        b["fuel_cost_jpy_roundtrip"] = cost_jpy_one_way * 2
        b["time_saved_one_way_min"] = time_saved_one_way
        b["time_saved_roundtrip_min"] = time_saved_one_way * 2

# Compute Weekly Summary for both bases (Round-trip = 2x per trip)
WEEKLY_SUMMARY = {}
for base_key in ("asakusabashi", "ikebukuro"):
    total_km_week = 0.0
    total_cb_min_week = 0.0
    total_train_min_week = 0.0
    for d in DESTINATIONS:
        trips = d["trips_per_week"]
        b = d[base_key]
        total_km_week += b["km"] * 2 * trips
        total_cb_min_week += b["cb250r_min"] * 2 * trips
        total_train_min_week += b["train_min"] * 2 * trips
    liters_week = round(total_km_week / WMTC_KM_PER_L, 2)
    cost_jpy_week = int(round(liters_week * GAS_PRICE_JPY_PER_L))
    saved_min_week = int(round(total_train_min_week - total_cb_min_week))
    WEEKLY_SUMMARY[base_key] = {
        "total_roundtrips_per_week": round(sum(d["trips_per_week"] for d in DESTINATIONS), 1),
        "total_km_week": round(total_km_week, 1),
        "total_km_month": round(total_km_week * 4.33, 1),
        "cb250r_hours_week": round(total_cb_min_week / 60.0, 2),
        "train_hours_week": round(total_train_min_week / 60.0, 2),
        "saved_minutes_week": saved_min_week,
        "saved_hours_week": round(saved_min_week / 60.0, 2),
        "saved_hours_year": round((saved_min_week * 52) / 60.0, 1),
        "fuel_liters_week": liters_week,
        "fuel_tanks_per_month": round((liters_week * 4.33) / 10.0, 2),
        "fuel_cost_jpy_week": cost_jpy_week,
        "fuel_cost_jpy_month": int(round(cost_jpy_week * 4.33))
    }

FEED_PAYLOAD = {
    "api_version": "1.0.0",
    "generated_at": "2026-10-17T23:15:00Z",
    "source": "Honda Motor Co., Ltd. Official Japan Specs (https://www.honda.co.jp/CB250R/type/ & /spec/) + OSRM Tokyo Street Routing Engine",
    "default_fx_jpy_per_usd": FX_DEFAULT,
    "tokyo_regular_gas_jpy_per_l": GAS_PRICE_JPY_PER_L,
    "bases": BASES,
    "cb250r_specs": CB250R_OFFICIAL_SPECS,
    "weekly_summary": WEEKLY_SUMMARY,
    "destinations": DESTINATIONS
}

feed_path = ASSETS / "cb250r-routes-feed.json"
feed_path.write_text(json.dumps(FEED_PAYLOAD, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"[OK] Generated {feed_path} ({feed_path.stat().st_size:,} bytes)")
