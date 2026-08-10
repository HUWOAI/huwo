# 吃什么呼我 · HUWO AI — 开源 Demo

[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> **《吃什么，呼我》** 垂直饮食 Agent 内核开源模块（MIT）  
> 公开仓库：**https://github.com/HUWOAI/huwo**  
> 团队：**HUWO呼我 - 杭州汇融科技&衢州呼我网络**  
> 负责人：Richard.Mao · 官网：www.huwo.xyz · 小程序/抖音：**呼我**

本目录为 **HUWOAI/huwo** 开源首批代码，与闭源商业版 APP 后端（huwo.xyz）分离。

---

## 开源边界（一句话）

**开源：可复用的 AI 饮食 Agent Skill、Prompt、小虎机器人协议适配器、Demo 部署与模型调用示例。**  
**闭源：完整 APP 后端、账号/社交/碰一碰、用户数据、会员变现、私有知识库、量产固件。**

详细说明见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md)。

- [Gitee/GitHub 建仓指南](./docs/GITEE_SETUP.md)
- [3 分钟 Demo 脚本](./docs/DEMO_SCRIPT.md)

---

## 30 秒跑通（无需大模型 Key）

```bash
cd open
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_demo.py golden
python scripts/run_demo.py meal-plan
```

`golden` 会打印一条完整 Agent 轨迹（规划 → 清单 → 附近 → 小虎通知），对应「帮爸爸安排清淡晚餐」故事。

启动 Web Demo（无 Key 也能访问静态 Skill 接口）：

```bash
# Windows
scripts\run_demo.bat

# 或
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
```

浏览器打开：

- http://127.0.0.1:8765/docs — Swagger
- http://127.0.0.1:8765/demo/meal-plan — 三餐规划
- http://127.0.0.1:8765/demo/nearby?city=衢州 — 附近 POI
- http://127.0.0.1:8765/data/foods?q=小黄鱼 — **食物百科 Food Intel**（开源样本库）

---

## 配置大模型（可选，用于 `/demo/chat`）

```bash
cp .env.example .env
# 编辑 .env，填入火山方舟或 MiniMax Key
```

| 变量 | 说明 |
|------|------|
| `VOLC_ARK_API_KEY` | 火山方舟（豆包）API Key |
| `VOLC_ARK_MODEL` | 推理接入点 ID |
| `MINIMAX_API_KEY` | MiniMax H3 示例 |
| `LLM_PROVIDER` | `volc` 或 `minimax` |

---

## 目录结构

```
open/
├── LICENSE                 MIT
├── README.md
├── OPEN_BOUNDARY.md        开源边界说明
├── requirements.txt
├── .env.example
├── huwo_open/              核心开源 Python 包
│   ├── agent/
│   │   ├── prompts/        Prompt 工程（饮食顾问、识餐）
│   │   ├── skills/         三餐规划、POI、营养估算
│   │   ├── tools_schema.json
│   │   └── orchestrator.py 工具编排 + 可选 LLM 对话
│   ├── providers/          火山方舟 / MiniMax 调用封装
│   └── robot/              小虎机器人协议适配器
├── demo/                   FastAPI Demo 入口
├── docs/                   部署与 Demo 脚本
└── scripts/                本地运行脚本
```

---

## 与商业版关系

| 模块 | 开源 Demo | 商业版 huwo.xyz |
|------|-----------|-----------------|
| Agent Skill / Prompt | ✅ | ✅ |
| 食物百科样本库 | ✅ 500+ | ✅ + 条码/USDA |
| 账号 / 社交 / 群组 | ❌ | ✅ |
| 全双工语音 / RTC | ❌ | ✅ |
| 小虎硬件联动 | 协议示例 | ✅ 量产 |

---

## License

MIT — 详见 [LICENSE](./LICENSE)
