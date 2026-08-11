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


def links_for_shopping_list(items: list[str] | None = None, keyword: str = "") -> dict:
    """买菜履约入口（开源示意：优先京东秒送叙事；真实开放平台密钥仅在商业版）。"""
    names = [x for x in (items or []) if str(x).strip()]
    kw = keyword.strip() or (" ".join(names[:3]) if names else "生鲜蔬菜")
    enc = urllib.parse.quote(kw)
    return {
        "grocery_provider": "jd_daojia",
        "grocery_provider_label": "京东秒送",
        "keyword": kw,
        "items": names,
        "primary": {
            "label": "去京东秒送买菜（示意链）",
            "url": f"https://daojia.jd.com/html/index.html#search?key={enc}",
        },
        "alternates": [
            {"label": "去盒马", "url": f"https://www.freshhema.com/search?keyword={enc}"},
            {"label": "去美团买菜", "url": f"https://waimai.meituan.com/search?keyword={enc}"},
        ],
        "note": "开源 Demo 仅返回公开检索深链；京东秒送开放平台下单需商业版密钥。",
    }
