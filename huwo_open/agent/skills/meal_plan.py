"""Standalone meal planning skill — no ORM, uses sample_dishes.json."""

from __future__ import annotations

import random
import re
from datetime import date

from huwo_open.data.loader import dishes, default_preferences

MEAL_CATEGORIES = {
    "早餐": ["饮品", "蛋类", "主食", "小吃"],
    "午餐": ["荤菜", "蔬菜", "主食"],
    "晚餐": ["荤菜", "蔬菜", "卤味"],
}

STAPLE_EXTRAS = ("鸡蛋", "西兰花", "番茄", "豆腐", "牛奶", "糙米")


def _pick(categories: list[str], exclude: set[str]) -> dict | None:
    pool = [d for d in dishes() if d["category"] in categories and d["name"] not in exclude]
    if not pool:
        pool = [d for d in dishes() if d["name"] not in exclude]
    return random.choice(pool) if pool else None


def build_meal_plan(
    *,
    goal: str | None = None,
    taste: str | None = None,
    plan_date: str | None = None,
) -> dict:
    pref = default_preferences()
    goal = goal or pref.get("diet_goal", "均衡")
    taste = taste or pref.get("taste", "清淡")
    used: set[str] = set()
    meals: list[dict] = []
    actions = {"早餐": "一键下单", "午餐": "换一换", "晚餐": "一键下单"}

    for meal_type, cats in MEAL_CATEGORIES.items():
        dish = _pick(cats, used)
        if not dish:
            continue
        used.add(dish["name"])
        name = dish["name"]
        cal = dish["calories"]
        protein = dish["protein"]
        if meal_type == "早餐":
            d2 = _pick(["蛋类", "饮品"], used)
            if d2:
                used.add(d2["name"])
                name = f"{d2['name']}+{dish['name']}"
                cal += d2["calories"]
                protein += d2["protein"]
        reason = f"符合{goal}目标，{taste}口味"
        if "减脂" in goal or "低卡" in dish.get("tags", ""):
            reason = "高蛋白低脂，减脂优选"
        meals.append(
            {
                "type": meal_type,
                "name": name,
                "calories": cal,
                "protein": protein,
                "reason": reason,
                "action": actions[meal_type],
            }
        )

    return {"date": plan_date or date.today().isoformat(), "goal": goal, "meals": meals}


def build_shopping_list(plan: dict | None = None) -> dict:
    plan = plan or build_meal_plan()
    seen: set[str] = set()
    items: list[dict] = []
    for meal in plan["meals"]:
        for part in re.split(r"[+＋、,，]", meal["name"]):
            n = part.strip()
            if n and n not in seen:
                seen.add(n)
                items.append({"name": n, "category": "食材", "from_meal": meal["type"]})
    for staple in STAPLE_EXTRAS:
        if len(items) >= 12:
            break
        if staple not in seen:
            seen.add(staple)
            items.append({"name": staple, "category": "常备", "from_meal": ""})
    keyword = " ".join(i["name"] for i in items[:5])
    return {
        "date": plan["date"],
        "goal": plan["goal"],
        "items": items,
        "tip": "Demo 清单；商业版可跳转淘宝/盒马等。",
        "deeplink_hint": {
            "taobao": f"https://s.taobao.com/search?q={keyword}",
            "jd": f"https://search.jd.com/Search?keyword={keyword}",
        },
    }
