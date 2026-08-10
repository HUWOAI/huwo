"""FastAPI Demo — 可复现开源入口。"""

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
from huwo_open.data.loader import default_preferences, dishes, foods, pois  # noqa: E402

app = FastAPI(
    title="吃什么呼我 — 开源 Demo",
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


@app.get("/data/foods/stats")
def data_foods_stats():
    from huwo_open.data.loader import foods

    cats: dict[str, int] = {}
    for f in foods():
        c = f.get("category", "other")
        cats[c] = cats.get(c, 0) + 1
    return {"total": len(foods()), "categories": cats, "version": "v2"}


@app.get("/data/foods")
def data_foods(q: str = ""):
    from huwo_open.agent.skills.food_intel import lookup_food

    if q:
        return lookup_food(q, limit=20)
    return {"items": [{"id": f["id"], "name": f["name"], "summary": f.get("summary")} for f in foods()]}


@app.get("/data/foods/barcode/{barcode}")
async def data_food_barcode(barcode: str):
    """Demo stub — 生产环境走 /api/v1/food/barcode/{barcode}。"""
    try:
        import httpx

        code = "".join(c for c in barcode if c.isdigit())
        async with httpx.AsyncClient(timeout=12.0) as client:
            resp = await client.get(
                f"https://world.openfoodfacts.org/api/v2/product/{code}.json",
                headers={"User-Agent": "HuwoAI-OpenDemo/1.0"},
            )
            if resp.status_code != 200 or resp.json().get("status") != 1:
                raise HTTPException(status_code=404, detail="条码未找到")
            product = resp.json().get("product") or {}
            return {
                "found": True,
                "name": product.get("product_name") or code,
                "barcode": code,
                "source": "openfoodfacts",
            }
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/data/foods/usda/search")
def data_food_usda_search(q: str = ""):
    return {
        "configured": False,
        "message": "USDA 需配置 API Key；请使用商业版 /api/v1/food/usda/search",
        "items": [],
        "query": q,
    }


@app.get("/data/foods/{food_id}")
def data_food_detail(food_id: str):
    from huwo_open.agent.skills.food_intel import get_food_profile

    data = get_food_profile(food_id)
    if data.get("error"):
        raise HTTPException(status_code=404, detail=data["error"])
    return data


@app.post("/demo/food/batch-lookup")
def demo_food_batch_lookup(body: dict):
    from huwo_open.agent.skills.food_intel import lookup_food

    keywords = body.get("keywords") or []
    results = []
    for kw in keywords:
        if not kw:
            continue
        items = lookup_food(kw, limit=3).get("items", [])
        results.append({"keyword": kw, "items": items, "total": len(items)})
    return {"results": results}


@app.get("/demo/nearby")
def demo_nearby(city: str = "衢州", poi_type: str = "restaurant"):
    return search_nearby(city=city, poi_type=poi_type)


@app.post("/demo/tool")
def demo_tool(body: ToolIn):
    return {"result": execute_tool(body.name, body.arguments)}


@app.post("/demo/chat")
async def demo_chat(body: ChatIn):
    try:
        out = await chat_once(body.message)
        return {
            "reply": out["reply"],
            "trajectory": out.get("trajectory") or [],
            "preferences": default_preferences(),
        }
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e)) from e


@app.get("/demo/golden-path")
def demo_golden_path():
    """评审可一键验证的黄金闭环（无需大模型 Key）。"""
    pref = default_preferences()
    meal = build_meal_plan(goal="清淡")
    shop = build_shopping_list()
    nearby = search_nearby(city=pref.get("city") or "衢州", poi_type="restaurant")
    robot = get_robot_adapter().notify(
        expression="happy",
        tts_text="今晚清蒸鲈鱼，少油少盐",
        screen_title="爸爸晚餐",
    )
    trajectory = [
        {"name": "generate_meal_plan", "arguments": {"goal": "清淡"}, "result": meal},
        {"name": "get_shopping_list", "arguments": {}, "result": shop},
        {"name": "search_nearby", "arguments": {"poi_type": "restaurant"}, "result": nearby},
        {"name": "robot_notify", "arguments": {"tts_text": "今晚清蒸鲈鱼"}, "result": robot},
    ]
    return {
        "story": "异地子女一句话：帮爸爸安排今晚清淡晚餐（花生过敏）",
        "closed_loop": [
            "任务理解：清淡 + 花生过敏 + 晚餐",
            "计划生成：三餐/晚餐推荐",
            "工具调用：购物清单 + 附近餐厅",
            "结果交付：小虎机器人屏显 + TTS",
            "可验证：本接口返回完整 trajectory",
        ],
        "trajectory": trajectory,
        "preferences": pref,
    }


@app.get("/demo/robot/events")
def robot_events():
    return {"events": get_robot_adapter().drain_events()}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("DEMO_HOST", "0.0.0.0")
    port = int(os.getenv("DEMO_PORT", "8765"))
    uvicorn.run("demo.app:app", host=host, port=port, reload=False)
