"""FastAPI Demo — GOAI 可复现入口。"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# 加载 open/.env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from huwo_open.agent.orchestrator import (  # noqa: E402
    chat_once,
    execute_tool,
    get_robot_adapter,
    load_system_prompt,
    load_tools_schema,
)
from huwo_open.agent.skills.meal_plan import build_meal_plan, build_shopping_list  # noqa: E402
from huwo_open.agent.skills.nearby import search_nearby  # noqa: E402
from huwo_open.data.loader import default_preferences, dishes, pois  # noqa: E402

app = FastAPI(
    title="吃什么呼我 — GOAI 开源 Demo",
    description="内核开源模块：饮食 Agent Skill + 小虎机器人适配器 + 第三方模型调用示例",
    version="0.1.0-open",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatIn(BaseModel):
    message: str = Field(..., min_length=1, examples=["帮我安排今天晚餐"])


class ToolIn(BaseModel):
    name: str
    arguments: dict = Field(default_factory=dict)


@app.get("/health")
def health():
    return {"status": "ok", "service": "huwo-open-demo", "license": "MIT"}


@app.get("/")
def root():
    return {
        "project": "吃什么呼我 · HUWO AI Open Demo",
        "docs": "/docs",
        "note": "商业版 APP 后端、社交、账号体系不在本仓库",
    }


@app.get("/meta/tools")
def meta_tools():
    return {"tools": load_tools_schema()}


@app.get("/meta/prompt")
def meta_prompt():
    return {"system_prompt_preview": load_system_prompt()[:500] + "..."}


@app.get("/data/dishes")
def data_dishes():
    return dishes()


@app.get("/data/poi")
def data_poi(city: str = "衢州"):
    return [p for p in pois() if p.get("city") == city]


@app.get("/demo/meal-plan")
def demo_meal_plan():
    return build_meal_plan()


@app.get("/demo/shopping-list")
def demo_shopping_list():
    return build_shopping_list()


@app.get("/demo/nearby")
def demo_nearby(city: str = "衢州", poi_type: str = "restaurant"):
    return search_nearby(city=city, poi_type=poi_type)


@app.post("/demo/tool")
def demo_tool(body: ToolIn):
    return {"result": execute_tool(body.name, body.arguments)}


@app.post("/demo/chat")
async def demo_chat(body: ChatIn):
    try:
        reply = await chat_once(body.message)
        return {"reply": reply, "preferences": default_preferences()}
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e)) from e


@app.get("/demo/robot/events")
def robot_events():
    return {"events": get_robot_adapter().drain_events()}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("DEMO_HOST", "0.0.0.0")
    port = int(os.getenv("DEMO_PORT", "8765"))
    uvicorn.run("demo.app:app", host=host, port=port, reload=False)
