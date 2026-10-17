#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the 3D Custom Renders for #7:🦖☢️ Godzilla 1954 (ShodaiGoji — Ginza Atomic Edition):
  1. assets/venum_custom_godzilla_1954.jpg
     - Main body: Volcanic Charcoal Grey & Obsidian Matte Black Venum Fangs
     - Thumb & Wrist Collar: Deep Metallic Slate / Dorsal Bone Silver-Grey
     - Velcro Strap, Thumb Logo & Stitching: Incandescent Cherenkov Atomic Blue (#00d4ff)
  2. assets/yokkao_shorts_godzilla_1954.jpg
     - Waistband & Center ★YOKKAO★ Patch: Cherenkov Atomic Ice Blue (#38bdf8) with Silver/Black border
     - Main Shorts Body: Volcanic Charcoal Slate Grey (#272b33) with Obsidian Black diagonal slashes
"""
from pathlib import Path
from PIL import Image
import colorsys

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"


def build_venum_godzilla_1954():
    raw_img = Image.open(ASSETS / "venum_custom_batman.jpg").convert("RGBA")
    r_px = raw_img.load()
    w, h = raw_img.size

    for y in range(h):
        for x in range(w):
            r, g, b, a = r_px[x, y]
            if a < 200:
                continue

            rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
            hue, sat, val = colorsys.rgb_to_hsv(rf, gf, bf)

            # 1. Yellow areas (Velcro strap + thumb VENUM text + stitching) -> Cherenkov Atomic Cyan/Blue!
            if sat > 0.35 and 0.07 <= hue <= 0.20:
                new_h = 0.545
                new_s = min(1.0, sat * 0.95)
                new_v = min(1.0, val * 1.02)
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                r_px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255), a)

            # 2. Royal Blue areas (Thumb + lower wrist collar) -> Volcanic Dorsal Charcoal / Bone Slate
            elif sat > 0.25 and 0.55 <= hue <= 0.72:
                new_h = 0.56
                new_s = sat * 0.22
                new_v = val * 0.68
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                r_px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255), a)

            # 3. Neutral grey/black main body -> deepen slightly into authentic 1954 ShodaiGoji charcoal
            elif sat <= 0.25 and val < 0.85:
                new_v = val * 0.90
                nr, ng, nb = colorsys.hsv_to_rgb(0.56, min(0.08, sat + 0.03), new_v)
                r_px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255), a)

    out_path = ASSETS / "venum_custom_godzilla_1954.jpg"
    raw_img.save(out_path, format="PNG")
    print(f"[OK] Saved {out_path.name}")


def build_yokkao_shorts_godzilla_1954():
    # Start from yokkao_shorts_blue_beetle.jpg which has:
    # - Sky Blue / Atomic Cyan waistband & center ★YOKKAO★ patch (hue ~0.52-0.57)
    # - Royal Blue main body (hue ~0.62-0.69)
    # - Matte Black diagonal slashes
    img = Image.open(ASSETS / "yokkao_shorts_blue_beetle.jpg").convert("RGB")
    px = img.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if r > 245 and g > 245 and b > 245:
                continue

            rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
            hue, sat, val = colorsys.rgb_to_hsv(rf, gf, bf)

            # 1. Royal Blue main body (hue 0.60 - 0.72) -> ShodaiGoji 1954 Volcanic Charcoal Grey!
            if sat > 0.35 and 0.60 <= hue <= 0.72:
                new_h = 0.58
                new_s = 0.14
                # Preserve satin folds and highlights while turning body into dark charcoal grey
                new_v = max(0.14, min(0.55, val * 0.48))
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255))

            # 2. Sky Blue / Cyan waistband & ★YOKKAO★ patch (hue 0.48 - 0.59) -> Keep incandescent Atomic Blue!
            elif sat > 0.25 and 0.48 <= hue < 0.60:
                new_h = 0.545
                new_s = min(1.0, sat * 1.05)
                new_v = min(1.0, val * 1.02)
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255))

            # 3. Yellow side text (hue 0.10 - 0.20) -> Bone Silver / Atomic White
            elif sat > 0.30 and 0.08 <= hue <= 0.22:
                new_h = 0.54
                new_s = 0.18
                new_v = min(1.0, val * 1.05)
                nr, ng, nb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
                px[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255))

    out_path = ASSETS / "yokkao_shorts_godzilla_1954.jpg"
    img.save(out_path, quality=95)
    print(f"[OK] Saved {out_path.name}")


if __name__ == "__main__":
    build_venum_godzilla_1954()
    build_yokkao_shorts_godzilla_1954()
