"""Dish search + simple nutrition heuristics."""

from __future__ import annotations

from huwo_open.data.loader import dishes


def search_dish(keyword: str, limit: int = 5) -> dict:
    kw = keyword.strip().lower()
    items = [
        d
        for d in dishes()
        if kw in d["name"].lower() or kw in d.get("tags", "").lower()
    ][:limit]
    return {"items": items, "message": None if items else f"未找到与「{keyword}」相关的菜品"}


def estimate_meal_from_text(meal_type: str, content: str) -> dict:
    """Rule-based fallback when no vision API — Demo only."""
    base = 350
    protein = 15
    if any(k in content for k in ("沙拉", "轻食", "蔬菜")):
        base, protein = 280, 12
    elif any(k in content for k in ("火锅", "烧烤", "炸鸡")):
        base, protein = 650, 25
    return {
        "meal_type": meal_type,
        "content": content,
        "calories": base,
        "protein_g": protein,
        "carbs_g": 40,
        "fat_g": 12,
        "gi_hint": "中",
        "advice": "已记录，建议搭配蔬菜与适量蛋白。",
    }
