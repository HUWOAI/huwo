"""Agent tool dispatch + optional LLM chat loop (Demo)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from huwo_open.agent.skills.meal_plan import build_meal_plan, build_shopping_list
from huwo_open.agent.skills.nearby import search_nearby
from huwo_open.agent.skills.nutrition import estimate_meal_from_text, search_dish
from huwo_open.data.loader import default_preferences
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
    return json.dumps({"error": f"unknown tool {name}"}, ensure_ascii=False)


def get_robot_adapter() -> RobotAdapter:
    return _robot


async def chat_once(user_message: str, history: list[dict] | None = None) -> str:
    """Single-turn chat with tool calling (requires LLM API key)."""
    from huwo_open.providers import create_llm_client

    client, model = create_llm_client()
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
    if msg.tool_calls:
        parts = [msg.content or ""]
        for tc in msg.tool_calls:
            fn = tc.function
            args = json.loads(fn.arguments or "{}")
            result = execute_tool(fn.name, args)
            parts.append(f"\n[工具 {fn.name}] {result}")
        return "".join(parts).strip()
    return (msg.content or "").strip()
