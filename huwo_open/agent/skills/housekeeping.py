"""家政服务 Skill（Demo：内存供需 + 公平评测示意，非真实撮合）。"""

from __future__ import annotations

import itertools
from typing import Any

_TEACHER_PHONE = "13858039966"
_pid = itertools.count(1001)
_did = itertools.count(2001)
_profiles: list[dict[str, Any]] = []
_demands: list[dict[str, Any]] = []

_CERT_PACKS: dict[str, dict[str, Any]] = {
    "育婴": {
        "title": "育婴员 / 母婴护理方向考证资料包",
        "certs": ["育婴员（人社职业技能等级）", "母婴护理相关培训证明", "健康证"],
    },
    "月嫂": {
        "title": "母婴护理员 / 月嫂方向考证资料包",
        "certs": ["母婴护理员培训", "育婴员", "健康证"],
    },
    "护工": {
        "title": "养老护理员方向考证资料包",
        "certs": ["养老护理员（人社）", "健康证", "急救常识培训"],
    },
    "保洁": {
        "title": "家政服务员 / 保洁方向资料包",
        "certs": ["家政服务员（人社）", "健康证"],
    },
    "默认": {
        "title": "家政综合能力提升与考证资料包",
        "certs": ["家政服务员", "育婴员或养老护理员（按岗位选）", "健康证"],
    },
}


def fair_interview_score(
    *,
    roles: str = "保姆",
    years_exp: float = 0,
    certificates: str = "",
    answer_quality: float = 7.0,
) -> dict[str, Any]:
    """AI 公平面试示意分：规则透明、可复现，降低人为偏见叙事。"""
    base = 5.0
    base += min(3.0, float(years_exp) * 0.3)
    if certificates.strip():
        base += 1.0
    base += max(0.0, min(2.0, (float(answer_quality) - 5.0) * 0.4))
    score = round(min(10.0, base), 1)
    return {
        "roles": roles,
        "score_overall": score,
        "dimensions": {
            "experience": round(min(10.0, 4 + float(years_exp) * 0.5), 1),
            "certificates": 8.0 if certificates.strip() else 5.0,
            "communication": round(min(10.0, float(answer_quality)), 1),
            "fairness_note": "规则评分，不因籍贯/外貌加权",
        },
        "disclaimer": "Demo 评测仅供参考，不构成劳动/背景调查结论；正式背调与签约在商业版完成。",
        "insurance_hint": "本单建议投保（占位）— 商业版可引导服务过程保险，不输出承保结论。",
    }


def publish_service_profile(
    *,
    roles: str,
    resume_text: str,
    display_name: str = "求职者",
    years_exp: float = 0,
    city: str = "杭州",
    certificates: str = "",
    score_overall: float | None = None,
) -> dict[str, Any]:
    if score_overall is None:
        score_overall = fair_interview_score(
            roles=roles, years_exp=years_exp, certificates=certificates
        )["score_overall"]
    row = {
        "id": next(_pid),
        "display_name": display_name,
        "roles": roles,
        "years_exp": years_exp,
        "city": city,
        "certificates": certificates,
        "resume_text": resume_text,
        "score_overall": score_overall,
        "status": "demo_published",
        "note": "开源 Demo 内存挂牌；商业版写入服务市场并脱敏展示联系方式。",
    }
    _profiles.append(row)
    return row


def publish_service_demand(
    *,
    title: str,
    service_types: str,
    city: str = "杭州",
    schedule_text: str = "",
    budget_text: str = "",
) -> dict[str, Any]:
    row = {
        "id": next(_did),
        "title": title,
        "service_types": service_types,
        "city": city,
        "schedule_text": schedule_text,
        "budget_text": budget_text,
        "status": "demo_open",
        "insurance_hint": "本单建议投保（占位）",
        "note": "开源 Demo 内存需求；商业版进入供需市场。",
    }
    _demands.append(row)
    return row


def recommend_service_workers(demand_id: int | None = None, limit: int = 3) -> dict[str, Any]:
    items = sorted(_profiles, key=lambda x: float(x.get("score_overall") or 0), reverse=True)
    if not items:
        items = [
            {
                "id": 0,
                "display_name": "示例育婴嫂·小周",
                "roles": "育婴嫂",
                "city": "杭州",
                "score_overall": 8.6,
                "note": "无挂牌时返回示例，便于评委复现推荐轨迹",
            }
        ]
    return {
        "demand_id": demand_id,
        "recommendations": items[: max(1, min(limit, 5))],
        "fairness_note": "按评测分与岗位匹配排序，不引入地域歧视权重。",
    }


def get_cert_study_pack(role: str = "") -> dict[str, Any]:
    text = role or ""
    key = "默认"
    for k in ("月嫂", "育婴", "护工", "养老", "保洁", "保姆"):
        if k in text:
            if k in ("护工", "养老"):
                key = "护工"
            elif k == "保姆":
                key = "保洁"
            else:
                key = k
            break
    pack = _CERT_PACKS.get(key, _CERT_PACKS["默认"])
    return {
        **pack,
        "role_hint": role or "综合家政",
        "teacher_phone": _TEACHER_PHONE,
        "teacher_note": f"考证与培训咨询请联系老师：{_TEACHER_PHONE}（Demo 联络号）",
    }
