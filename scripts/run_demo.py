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


def main() -> None:
    parser = argparse.ArgumentParser(description="HUWO AI Open Demo CLI")
    parser.add_argument(
        "action",
        choices=["meal-plan", "shopping", "nearby", "tool", "chat"],
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
    elif args.action == "chat":
        import asyncio

        from huwo_open.agent.orchestrator import chat_once

        print(asyncio.run(chat_once(args.message)))


if __name__ == "__main__":
    main()
