#!/usr/bin/env python3
"""CLI Demo：无需启动 Web 服务，直接调用 Agent Skill。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from huwo_open.agent.orchestrator import execute_tool  # noqa: E402
from huwo_open.agent.skills.meal_plan import build_meal_plan, build_shopping_list  # noqa: E402


def _golden() -> dict:
    meal = build_meal_plan(goal="清淡")
    shop = build_shopping_list()
    nearby = execute_tool("search_nearby", {"poi_type": "restaurant", "city": "衢州"})
    grocery = execute_tool("open_grocery_checkout", {"keyword": "清淡生鲜"})
    robot = execute_tool(
        "robot_notify",
        {"expression": "happy", "tts_text": "今晚清蒸鲈鱼，少油少盐", "screen_title": "爸爸晚餐"},
    )
    return {
        "story": "帮爸爸安排今晚清淡晚餐（花生过敏）",
        "trajectory": [
            {"name": "generate_meal_plan", "result": meal},
            {"name": "get_shopping_list", "result": shop},
            {"name": "open_grocery_checkout", "result": json.loads(grocery)},
            {"name": "search_nearby", "result": json.loads(nearby)},
            {"name": "robot_notify", "result": json.loads(robot)},
        ],
    }


def _care() -> dict:
    create = execute_tool(
        "create_med_reminder",
        {
            "member_name": "爸爸",
            "medicine_name": "阿司匹林肠溶片",
            "dosage": "每次1片",
            "schedule_times": ["08:00", "20:00"],
            "meal_relation": "饭后",
        },
    )
    listed = execute_tool("list_med_reminders", {})
    robot = execute_tool(
        "robot_notify",
        {"expression": "think", "tts_text": "爸爸，该吃药了", "screen_title": "吃药提醒"},
    )
    return {
        "story": "健康关怀：设置并播报吃药提醒（非诊疗）",
        "trajectory": [
            {"name": "create_med_reminder", "result": json.loads(create)},
            {"name": "list_med_reminders", "result": json.loads(listed)},
            {"name": "robot_notify", "result": json.loads(robot)},
        ],
    }


def _housekeeping() -> dict:
    score = execute_tool(
        "fair_interview_score",
        {"roles": "育婴嫂", "years_exp": 5, "certificates": "育婴员,健康证", "answer_quality": 8.5},
    )
    profile = execute_tool(
        "publish_service_profile",
        {
            "display_name": "小周",
            "roles": "育婴嫂",
            "years_exp": 5,
            "city": "杭州",
            "certificates": "育婴员,健康证",
            "resume_text": "五年育婴经验，持证上岗，擅长辅食与作息管理。",
            "score_overall": json.loads(score)["score_overall"],
        },
    )
    demand = execute_tool(
        "publish_service_demand",
        {
            "title": "住家育婴一周体验",
            "service_types": "育婴嫂",
            "city": "杭州",
            "schedule_text": "下周一起",
            "budget_text": "面议",
        },
    )
    demand_id = json.loads(demand)["id"]
    rec = execute_tool("recommend_service_workers", {"demand_id": demand_id, "limit": 3})
    pack = execute_tool("get_cert_study_pack", {"role": "育婴"})
    profile_id = json.loads(profile)["id"]
    emp = execute_tool(
        "start_care_employment",
        {"profile_id": profile_id, "caregiver_name": "小周", "note": "Demo 上岗"},
    )
    emp_id = json.loads(emp)["id"]
    weaning = execute_tool(
        "post_on_duty_moment",
        {"employment_id": emp_id, "kind": "weaning", "content": "看辅食 · 眼镜第一视角"},
    )
    grocery = execute_tool(
        "post_on_duty_moment",
        {"employment_id": emp_id, "kind": "grocery", "content": "记买菜 · 配料表"},
    )
    care = execute_tool(
        "post_on_duty_moment",
        {"employment_id": emp_id, "kind": "care", "content": "记带娃瞬间"},
    )
    ended = execute_tool("end_care_shift", {"employment_id": emp_id})
    closed = execute_tool("list_on_duty_moments", {"employment_id": emp_id})
    return {
        "story": "测→晒→配→看→关：公平面试 · 挂牌 · ≥3条匹配解释 · 眼镜三捷径 · 离岗 ACL",
        "trajectory": [
            {"name": "fair_interview_score", "result": json.loads(score)},
            {"name": "publish_service_profile", "result": json.loads(profile)},
            {"name": "publish_service_demand", "result": json.loads(demand)},
            {"name": "recommend_service_workers", "result": json.loads(rec)},
            {"name": "get_cert_study_pack", "result": json.loads(pack)},
            {"name": "start_care_employment", "result": json.loads(emp)},
            {"name": "post_on_duty_moment", "result": json.loads(weaning)},
            {"name": "post_on_duty_moment", "result": json.loads(grocery)},
            {"name": "post_on_duty_moment", "result": json.loads(care)},
            {"name": "end_care_shift", "result": json.loads(ended)},
            {"name": "list_on_duty_moments", "result": json.loads(closed)},
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="HUWO AI Open Demo CLI")
    parser.add_argument(
        "action",
        choices=["meal-plan", "shopping", "nearby", "tool", "chat", "golden", "care", "housekeeping"],
        help="要运行的 Demo 动作",
    )
    parser.add_argument("--message", "-m", default="帮我安排三餐", help="chat 模式用户消息")
    parser.add_argument("--tool", default="generate_meal_plan", help="tool 模式工具名")
    parser.add_argument("--args", default="{}", help="tool 模式 JSON 参数")
    args = parser.parse_args()

    if args.action == "meal-plan":
        print(json.dumps(build_meal_plan(), ensure_ascii=False, indent=2))
    elif args.action == "shopping":
        print(json.dumps(build_shopping_list(), ensure_ascii=False, indent=2))
    elif args.action == "nearby":
        print(execute_tool("search_nearby", {"poi_type": "restaurant", "city": "衢州"}))
    elif args.action == "tool":
        print(execute_tool(args.tool, json.loads(args.args)))
    elif args.action == "golden":
        print(json.dumps(_golden(), ensure_ascii=False, indent=2))
    elif args.action == "care":
        print(json.dumps(_care(), ensure_ascii=False, indent=2))
    elif args.action == "housekeeping":
        print(json.dumps(_housekeeping(), ensure_ascii=False, indent=2))
    elif args.action == "chat":
        import asyncio

        from huwo_open.agent.orchestrator import chat_once

        out = asyncio.run(chat_once(args.message))
        print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
