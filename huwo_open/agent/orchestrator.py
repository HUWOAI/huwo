"""Agent tool dispatch + optional LLM chat loop (Demo)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from huwo_open.agent.skills.food_intel import check_food_suitability, get_food_profile, lookup_food
from huwo_open.agent.skills.housekeeping import (
    end_care_shift,
    fair_interview_score,
    get_cert_study_pack,
    list_on_duty_moments,
    post_on_duty_moment,
    publish_service_demand,
    publish_service_profile,
    recommend_service_workers,
    start_care_employment,
)
from huwo_open.agent.skills.meal_plan import build_meal_plan, build_shopping_list
from huwo_open.agent.skills.med_reminder import create_med_reminder, list_med_reminders
from huwo_open.agent.skills.nearby import search_nearby
from huwo_open.agent.skills.nutrition import estimate_meal_from_text, search_dish
from huwo_open.data.loader import default_preferences
from huwo_open.integrations.deeplink import links_for_shopping_list
from huwo_open.robot.adapter import RobotAdapter

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
_robot = RobotAdapter()


def load_system_prompt() -> str:
    return (PROMPTS_DIR / "diet_advisor_system.txt").read_text(encoding="utf-8")


def load_tools_schema() -> list[dict]:
    return json.loads((Path(__file__).parent / "tools_schema.json").read_text(encoding="utf-8"))


def execute_tool(name: str, args: dict[str, Any]) -> str:
    pref = default_preferences()
    if name == "search_dish":
        return json.dumps(search_dish(args.get("keyword", ""), int(args.get("limit", 5))), ensure_ascii=False)
    if name == "generate_meal_plan":
        plan = build_meal_plan(goal=args.get("goal") or pref.get("diet_goal"))
        compact = {
            "date": args.get("date_label", "今天"),
            "goal": plan["goal"],
            "breakfast": next((m["name"] for m in plan["meals"] if m["type"] == "早餐"), ""),
            "lunch": next((m["name"] for m in plan["meals"] if m["type"] == "午餐"), ""),
            "dinner": next((m["name"] for m in plan["meals"] if m["type"] == "晚餐"), ""),
            "meals": plan["meals"],
        }
        return json.dumps(compact, ensure_ascii=False)
    if name == "search_nearby":
        return json.dumps(
            search_nearby(
                poi_type=args.get("poi_type", "restaurant"),
                keyword=args.get("keyword"),
                city=args.get("city") or pref.get("city"),
            ),
            ensure_ascii=False,
        )
    if name == "get_shopping_list":
        return json.dumps(build_shopping_list(), ensure_ascii=False)
    if name == "analyze_meal_text":
        data = estimate_meal_from_text(args.get("meal_type", "午餐"), args.get("content", ""))
        return json.dumps(data, ensure_ascii=False)
    if name == "robot_notify":
        result = _robot.notify(
            expression=args.get("expression", "happy"),
            tts_text=args.get("tts_text", ""),
            screen_title=args.get("screen_title", "HUWO"),
        )
        return json.dumps(result, ensure_ascii=False)
    if name == "lookup_food":
        return json.dumps(lookup_food(args.get("keyword", ""), int(args.get("limit", 5))), ensure_ascii=False)
    if name == "get_food_profile":
        return json.dumps(get_food_profile(args.get("food_id", "")), ensure_ascii=False)
    if name == "check_food_suitability":
        return json.dumps(
            check_food_suitability(args.get("food_id", ""), args.get("population_tags")),
            ensure_ascii=False,
        )
    if name == "open_grocery_checkout":
        shop = build_shopping_list()
        names = []
        if isinstance(shop, dict):
            for it in shop.get("items") or shop.get("list") or []:
                if isinstance(it, dict):
                    names.append(str(it.get("name") or it.get("item") or ""))
                else:
                    names.append(str(it))
        return json.dumps(
            links_for_shopping_list(names, keyword=str(args.get("keyword") or "")),
            ensure_ascii=False,
        )
    if name == "create_med_reminder":
        return json.dumps(
            create_med_reminder(
                medicine_name=str(args.get("medicine_name") or ""),
                member_name=str(args.get("member_name") or "本人"),
                dosage=str(args.get("dosage") or ""),
                schedule_times=args.get("schedule_times"),
                meal_relation=str(args.get("meal_relation") or "遵医嘱"),
                notes=str(args.get("notes") or ""),
            ),
            ensure_ascii=False,
        )
    if name == "list_med_reminders":
        return json.dumps(list_med_reminders(), ensure_ascii=False)
    if name == "fair_interview_score":
        return json.dumps(
            fair_interview_score(
                roles=str(args.get("roles") or "保姆"),
                years_exp=float(args.get("years_exp") or 0),
                certificates=str(args.get("certificates") or ""),
                answer_quality=float(args.get("answer_quality") or 7),
            ),
            ensure_ascii=False,
        )
    if name == "publish_service_profile":
        return json.dumps(
            publish_service_profile(
                roles=str(args.get("roles") or ""),
                resume_text=str(args.get("resume_text") or ""),
                display_name=str(args.get("display_name") or "求职者"),
                years_exp=float(args.get("years_exp") or 0),
                city=str(args.get("city") or pref.get("city") or "杭州"),
                certificates=str(args.get("certificates") or ""),
                score_overall=args.get("score_overall"),
            ),
            ensure_ascii=False,
        )
    if name == "publish_service_demand":
        return json.dumps(
            publish_service_demand(
                title=str(args.get("title") or ""),
                service_types=str(args.get("service_types") or ""),
                city=str(args.get("city") or pref.get("city") or "杭州"),
                schedule_text=str(args.get("schedule_text") or ""),
                budget_text=str(args.get("budget_text") or ""),
            ),
            ensure_ascii=False,
        )
    if name == "recommend_service_workers":
        return json.dumps(
            recommend_service_workers(
                demand_id=args.get("demand_id"),
                limit=int(args.get("limit") or 3),
            ),
            ensure_ascii=False,
        )
    if name == "get_cert_study_pack":
        return json.dumps(get_cert_study_pack(str(args.get("role") or "")), ensure_ascii=False)
    if name == "start_care_employment":
        return json.dumps(
            start_care_employment(
                profile_id=args.get("profile_id"),
                caregiver_name=str(args.get("caregiver_name") or ""),
                note=str(args.get("note") or ""),
            ),
            ensure_ascii=False,
        )
    if name == "post_on_duty_moment":
        return json.dumps(
            post_on_duty_moment(
                employment_id=args.get("employment_id"),
                content=str(args.get("content") or ""),
                kind=str(args.get("kind") or "care"),
                media_url=str(args.get("media_url") or ""),
            ),
            ensure_ascii=False,
        )
    if name == "end_care_shift":
        return json.dumps(end_care_shift(args.get("employment_id")), ensure_ascii=False)
    if name == "list_on_duty_moments":
        return json.dumps(list_on_duty_moments(args.get("employment_id")), ensure_ascii=False)
    return json.dumps({"error": f"unknown tool {name}"}, ensure_ascii=False)


def get_robot_adapter() -> RobotAdapter:
    return _robot


def _rule_based_reply(user_message: str) -> dict[str, Any]:
    """无 LLM Key 时的规则降级：按关键词直接路由到工具，保证 Demo 可演示。"""
    text = user_message or ""
    trajectory: list[dict[str, Any]] = []
    parts: list[str] = ["（未配置 LLM Key，走规则引擎演示）"]

    def _run(name: str, args: dict[str, Any]) -> Any:
        result = execute_tool(name, args)
        try:
            obj: Any = json.loads(result)
        except Exception:
            obj = result
        trajectory.append({"name": name, "arguments": args, "result": obj})
        return obj

    if any(k in text for k in ("晚餐", "三餐", "吃什么", "饭", "meal")):
        goal = "清淡" if "清淡" in text else None
        plan = _run("generate_meal_plan", {"goal": goal} if goal else {})
        dinner = plan.get("dinner") or ""
        parts.append(f"今晚推荐：{dinner}。" if dinner else "已生成三餐方案。")
        shop = _run("get_shopping_list", {})
        items = shop.get("items") or []
        if items:
            parts.append("采购清单：" + "、".join(str(i.get("name")) for i in items[:6]) + "。")
    elif any(k in text for k in ("吃药", "药", "提醒", "medication")):
        _run("list_med_reminders", {})
        parts.append("已查询吃药提醒（任务助手，不构成医疗建议）。")
    elif any(k in text for k in ("离岗", "结束工作", "ACL")):
        _run("end_care_shift", {})
        parts.append("已离岗并关闭雇主影像权限。")
    elif any(k in text for k in ("家政", "保姆", "育婴", "月嫂", "护工")):
        _run("recommend_service_workers", {"limit": 3})
        parts.append("已为您匹配家政候选人（AI 公平初筛，复核权在人）。")
    elif any(k in text for k in ("附近", "餐厅", "超市", "nearby")):
        _run("search_nearby", {"poi_type": "restaurant"})
        parts.append("已查询附近推荐。")
    else:
        _run("generate_meal_plan", {})
        parts.append("已生成今日三餐参考方案；配置 LLM Key 后可自由对话。")
    return {"reply": "".join(parts), "trajectory": trajectory}


async def chat_once(user_message: str, history: list[dict] | None = None) -> dict[str, Any]:
    """Single-turn chat with tool calling.

    Returns ``{"reply": str, "trajectory": [{"name","arguments","result"}, ...]}``.
    未配置 LLM Key 时自动降级为规则路径（演示可用，评测文档承诺的无 Key 路径）。
    """
    try:
        from huwo_open.providers import create_llm_client

        client, model = create_llm_client()
    except (RuntimeError, ImportError):
        return _rule_based_reply(user_message)
    pref = default_preferences()
    system = load_system_prompt() + f"\n用户上下文：{json.dumps(pref, ensure_ascii=False)}"
    messages: list[dict] = [{"role": "system", "content": system}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": user_message})

    tools = load_tools_schema()
    resp = await client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=1024,
    )
    msg = resp.choices[0].message
    trajectory: list[dict[str, Any]] = []
    if msg.tool_calls:
        parts = [msg.content or ""]
        for tc in msg.tool_calls:
            fn = tc.function
            args = json.loads(fn.arguments or "{}")
            result = execute_tool(fn.name, args)
            try:
                result_obj: Any = json.loads(result)
            except Exception:
                result_obj = result
            trajectory.append({"name": fn.name, "arguments": args, "result": result_obj})
            parts.append(f"\n[工具 {fn.name}] {result}")
        return {"reply": "".join(parts).strip(), "trajectory": trajectory}
    return {"reply": (msg.content or "").strip(), "trajectory": trajectory}
