"""吃药提醒 Skill（Demo：进程内存储，非医疗/审方）。"""

from __future__ import annotations

import itertools
from typing import Any

DISCLAIMER = "日程提醒仅供参考，不构成医疗诊断；用药请遵医嘱，禁止 AI 审方。"

_id_seq = itertools.count(1)
_store: list[dict[str, Any]] = []


def _normalize_times(schedule_times: list[str] | str | None) -> list[str]:
    if schedule_times is None:
        return ["08:00"]
    if isinstance(schedule_times, str):
        parts = [x.strip() for x in schedule_times.replace("，", ",").split(",") if x.strip()]
        return parts or ["08:00"]
    cleaned: list[str] = []
    for t in schedule_times:
        s = str(t).strip()
        if s:
            cleaned.append(s[:5] if len(s) >= 5 and s[2] == ":" else s[:5])
    return cleaned or ["08:00"]


def create_med_reminder(
    *,
    medicine_name: str,
    member_name: str = "本人",
    dosage: str = "",
    schedule_times: list[str] | str | None = None,
    meal_relation: str = "遵医嘱",
    notes: str = "",
) -> dict[str, Any]:
    name = (medicine_name or "").strip()
    if not name:
        return {"error": "medicine_name required", "disclaimer": DISCLAIMER}
    cleaned = _normalize_times(schedule_times)
    row = {
        "id": next(_id_seq),
        "member_name": (member_name or "本人").strip() or "本人",
        "medicine_name": name,
        "dosage": dosage or "",
        "schedule_times": cleaned,
        "meal_relation": meal_relation or "遵医嘱",
        "notes": notes or "",
        "enabled": True,
        "disclaimer": DISCLAIMER,
    }
    _store.append(row)
    return row


def list_med_reminders() -> dict[str, Any]:
    return {"items": list(_store), "count": len(_store), "disclaimer": DISCLAIMER}


def reset_store() -> None:
    """测试用：清空内存提醒。"""
    _store.clear()
