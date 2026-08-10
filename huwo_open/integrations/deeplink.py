"""Third-party deeplink helpers (no secrets)."""

from __future__ import annotations

import urllib.parse


def build_deeplinks(keyword: str, city: str = "") -> dict[str, dict]:
    kw = urllib.parse.quote(keyword or "美食")
    city_q = urllib.parse.quote(city or "")
    return {
        "meituan": {
            "label": "去美团外卖",
            "url": f"https://waimai.meituan.com/search?keyword={kw}",
        },
        "eleme": {
            "label": "去饿了么",
            "url": f"https://h5.ele.me/search?keyword={kw}",
        },
        "taobao": {
            "label": "去淘宝",
            "url": f"https://s.taobao.com/search?q={kw}",
        },
        "jd": {
            "label": "去京东",
            "url": f"https://search.jd.com/Search?keyword={kw}",
        },
        "hema": {
            "label": "去盒马",
            "url": f"https://www.freshhema.com/search?keyword={kw}",
        },
    }


def links_for_poi(poi: dict) -> list[dict]:
    name = poi.get("name") or "餐厅"
    ptype = poi.get("poi_type") or "restaurant"
    city = poi.get("city") or ""
    links = build_deeplinks(name, city)
    if ptype == "restaurant":
        order = ["meituan", "eleme"]
    elif ptype == "market":
        order = ["hema", "meituan"]
    else:
        order = ["meituan", "eleme"]
    return [links[k] for k in order if k in links]
