#!/usr/bin/env python3
"""
Atlas del Imperio — Automated Live Price & FX Tracker
1. Fetches real-time institutional exchange rates (USD -> JPY, KRW, THB)
   from open.er-api.com and api.frankfurter.dev (ECB).
2. Queries live Shopify JSON APIs (jp.venum.com & billabong.com) to verify
   real-time product catalog availability and pricing.
3. Recalculates all 10 phases, CAPEX zones, and OPEX monthly totals in USD,
   and writes the updated state to assets/prices-feed.json.
"""
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FEED_PATH = ROOT / "assets" / "prices-feed.json"

PRIMARY_FX_URL = "https://open.er-api.com/v6/latest/USD"
FALLBACK_FX_URL = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=JPY,KRW,THB"

SHOPIFY_ENDPOINTS = {
    "venum_japan": "https://jp.venum.com/products.json?limit=5",
    "billabong_us": "https://www.billabong.com/products.json?limit=5",
}


def fetch_json(url: str, timeout: int = 15) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AtlasImperioPriceTracker/2.0"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_live_fx() -> dict:
    try:
        data = fetch_json(PRIMARY_FX_URL)
        rates = data.get("rates", {})
        if all(k in rates for k in ("JPY", "KRW", "THB")):
            return {
                "JPY": round(float(rates["JPY"]), 4),
                "KRW": round(float(rates["KRW"]), 4),
                "THB": round(float(rates["THB"]), 4),
                "USD": 1.0,
                "source": "open.er-api.com",
            }
    except Exception as exc:
        print(f"[WARN] Primary FX API failed: {exc}")

    data = fetch_json(FALLBACK_FX_URL)
    rates = data.get("rates", {})
    return {
        "JPY": round(float(rates["JPY"]), 4),
        "KRW": round(float(rates["KRW"]), 4),
        "THB": round(float(rates["THB"]), 4),
        "USD": 1.0,
        "source": "api.frankfurter.dev (ECB)",
    }


def check_shopify_catalogs() -> dict:
    status = {}
    for key, url in SHOPIFY_ENDPOINTS.items():
        try:
            data = fetch_json(url, timeout=10)
            products = data.get("products", [])
            status[key] = {
                "online": True,
                "sample_count": len(products),
                "checked_url": url,
            }
        except Exception as exc:
            status[key] = {
                "online": False,
                "error": str(exc),
                "checked_url": url,
            }
    return status


def compute_phase_usd(phase: dict, rates: dict) -> int:
    total = 0.0
    for comp in phase.get("components", []):
        amt = float(comp["amount"])
        cur = comp["currency"]
        rate = float(rates.get(cur, 1.0))
        total += amt / rate
    return round(total)


def main() -> None:
    feed = json.loads(FEED_PATH.read_text(encoding="utf-8"))
    fx = get_live_fx()
    catalogs = check_shopify_catalogs()
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    feed["meta"]["last_updated_utc"] = now_iso
    feed["meta"]["active_fx_source"] = fx.pop("source", "open.er-api.com")
    feed["meta"]["catalog_apis"] = catalogs
    feed["fx_rates"]["live"] = fx

    grand_total_live_usd = 0
    for phase in feed.get("phases", []):
        live_usd = compute_phase_usd(phase, fx)
        phase["live_usd"] = live_usd
        grand_total_live_usd += live_usd

    feed["grand_total_live_usd"] = grand_total_live_usd
    feed["grand_total_ref_usd"] = sum(p.get("ref_usd", 0) for p in feed.get("phases", []))
    feed["investment_bucket_live_usd"] = (
        feed["capital_total_usd"] - feed["emergency_fund_usd"] - grand_total_live_usd
    )
    feed["opex_tokyo"]["live_base_usd"] = round(feed["opex_tokyo"]["base_jpy"] / fx["JPY"])
    feed["opex_tokyo"]["live_with_suzuki_usd"] = round(
        feed["opex_tokyo"]["with_suzuki_1on1_jpy"] / fx["JPY"]
    )
    feed["capex_rooms_jpy"]["live_total_usd"] = round(
        feed["capex_rooms_jpy"]["total_jpy"] / fx["JPY"]
    )

    FEED_PATH.write_text(json.dumps(feed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"[OK] Updated {FEED_PATH.name} at {now_iso} | "
        f"1 USD = {fx['JPY']} JPY, {fx['KRW']} KRW, {fx['THB']} THB | "
        f"Grand Total Live: ${grand_total_live_usd:,} USD | "
        f"CAPEX Live: ${feed['capex_rooms_jpy']['live_total_usd']:,} USD"
    )


if __name__ == "__main__":
    main()
