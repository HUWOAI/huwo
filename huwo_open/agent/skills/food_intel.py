"""Food encyclopedia skills for open demo."""

from __future__ import annotations

from huwo_open.data.loader import foods


def _score(food: dict, kw: str) -> int:
    kw_l = kw.lower()
    name = food["name"].lower()
    if name == kw_l:
        return 100
    if kw_l in name:
        return 70
    for alias in food.get("aliases", []):
        if kw_l in alias.lower():
            return 65
    return 0


def lookup_food(keyword: str, limit: int = 5) -> dict:
    kw = keyword.strip()
    scored = [( _score(f, kw), f) for f in foods() if not kw or _score(f, kw) > 0]
    scored.sort(key=lambda x: (-x[0], x[1]["name"]))
    items = [
        {
            "id": f["id"],
            "name": f["name"],
            "aliases": f.get("aliases", []),
            "category_label": f.get("category_label"),
            "summary": f.get("summary"),
        }
        for _, f in scored[:limit]
    ]
    return {"items": items, "message": None if items else f"未找到与「{keyword}」相关的食物"}


def get_food_profile(food_id: str) -> dict:
    for food in foods():
        if food["id"] == food_id:
            return food
    return {"error": f"未找到食物 {food_id}"}


def match_foods_from_text(text: str, limit: int = 5) -> list[dict]:
    if not text.strip():
        return []
    found: dict[str, dict] = {}
    foods_sorted = sorted(foods(), key=lambda f: len(f["name"]), reverse=True)
    for food in foods_sorted:
        if food["name"] in text:
            found[food["id"]] = food
            continue
        for alias in food.get("aliases", []):
            if alias and alias in text:
                found[food["id"]] = food
                break
    return [
        {
            "id": f["id"],
            "name": f["name"],
            "summary": f.get("summary"),
            "category_label": f.get("category_label"),
        }
        for f in list(found.values())[:limit]
    ]


def check_food_suitability(food_id: str, population_tags: list[str] | None = None) -> dict:
    food = get_food_profile(food_id)
    if food.get("error"):
        return food
    tags = population_tags or ["general"]
    rules = {r["population_tag"]: r for r in food.get("suitability", [])}
    results = []
    overall = "suitable"
    priority = {"avoid": 3, "caution": 2, "suitable": 1, "unknown": 0}
    for tag in tags:
        rule = rules.get(tag) or rules.get("general")
        if rule:
            results.append(rule)
            if priority.get(rule["verdict"], 0) > priority.get(overall, 0):
                overall = rule["verdict"]
    return {
        "food_id": food["id"],
        "food_name": food["name"],
        "overall_verdict": overall,
        "population_results": results,
        "disclaimer": "以上内容仅供参考，不构成医疗建议。",
    }
