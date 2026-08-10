"""Nearby POI search skill (sample data)."""

from __future__ import annotations

from huwo_open.data.loader import default_preferences, pois
from huwo_open.integrations.deeplink import links_for_poi


def search_nearby(
    *,
    poi_type: str = "restaurant",
    keyword: str | None = None,
    city: str | None = None,
    limit: int = 8,
) -> dict:
    city = city or default_preferences().get("city", "衢州")
    results = [p for p in pois() if p.get("city") == city and p.get("poi_type") == poi_type]
    if keyword:
        kw = keyword.lower()
        results = [
            p
            for p in results
            if kw in p["name"].lower() or kw in p.get("tags", "").lower()
        ]
    if not results:
        results = [p for p in pois() if p.get("poi_type") == poi_type][:limit]
    out = []
    for p in results[:limit]:
        item = dict(p)
        item["external_links"] = links_for_poi(item)
        out.append(item)
    return {"city": city, "results": out}
