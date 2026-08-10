# 吃什么呼我 · HUWO AI — GOAI 开源 Demo

[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> **《吃什么，呼我》** 参赛项目内核开源模块（MIT）  
> 公开仓库：**https://github.com/HUWOAI/huwo**  
> 大赛官网：[GOAI 杭州人工智能创新大赛](https://goaihz.com/#intro)  
> 参赛团队：**衢州呼我网络科技有限公司**  
> 负责人：Richard.Mao · 官网：www.huwo.xyz · 小程序/抖音：**呼我**

本目录为 **HUWOAI/huwo** 开源首批代码，与闭源商业版 APP 后端（huwo.xyz）分离。

---

## 开源边界（一句话）

**开源：可复用的 AI 饮食 Agent Skill、Prompt、小虎机器人协议适配器、Demo 部署与模型调用示例。**  
**闭源：完整 APP 后端、账号/社交/碰一碰、用户数据、会员变现、私有知识库、量产固件。**

详细说明见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md)（可直接粘贴 GOAI 报名表）。

- [Gitee/GitHub 建仓指南](./docs/GITEE_SETUP.md)
- [GOAI 3 分钟答辩 Demo 脚本](./docs/GOAI_DEMO_SCRIPT.md)

---

## 30 秒跑通（无需大模型 Key）

```bash
cd open
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_demo.py meal-plan
python scripts/run_demo.py shopping
```

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
├── OPEN_BOUNDARY.md        GOAI 申报用开源边界说明
├── requirements.txt
├── .env.example
├── huwo_open/              核心开源 Python 包
│   ├── agent/
│   │   ├── prompts/        Prompt 工程（饮食顾问、识餐）
│   │   ├── skills/         三餐规划、POI、营养估算
│   │   ├── tools_schema.json
│   │   └── orchestrator.py 工具编排 + 可选 LLM 对话
│   ├── providers/          火山方舟 / MiniMax 调用封装
│   ├── robot/              小虎桌面机器人协议 + 适配器
│   ├── integrations/       第三方 Deeplink 示例
│   └── data/               示例菜品、POI、偏好 JSON
├── demo/app.py             FastAPI Demo 入口
├── scripts/                CLI、菜谱预处理
├── deploy/                 Docker 部署
├── docs/                   补充文档
└── ui-examples/            基础 UI 组件示例说明
```

---

## 技术亮点（评审关注）

1. **饮食 Agent Skill 编排**：工具定义 JSON + `execute_tool` 可扩展  
2. **Prompt 工程**：系统提示词、识餐 JSON 输出模板独立文件维护  
3. **小虎机器人适配器**：WebSocket 协议文档 + 内存模拟器（可接真机）  
4. **多模型 Provider**：火山方舟、MiniMax H3 OpenAI 兼容封装  
5. **可复现 Demo**：Docker / 本地脚本，示例数据集，无商业后端依赖  

---

## 第三方依赖

- 运行时：`fastapi`, `uvicorn`, `openai`, `python-dotenv`
- 商业 API（用户自备 Key）：[火山引擎方舟](https://www.volcengine.com/product/ark)、[MiniMax](https://www.minimaxi.com/)
- 闭源 APP 另接：MySQL、短信、RTC 等（不在本仓库）

---

## 与闭源商业版关系

| 模块 | 本开源仓库 | 商业版（huwo.xyz） |
|------|------------|-------------------|
| 饮食 Agent 框架 | ✓ Demo | ✓ 生产 + 私有 Prompt |
| 用户账号 / JWT | ✗ | ✓ |
| 碰一碰社交 | ✗ | ✓ |
| 会员 / 支付 | ✗ | ✓ |
| 完整 POI / 知识库 | 示例 JSON | ✓ 私有数据 |
| 小虎量产固件 | ✗ | ✓ |

---

## 许可证

MIT License — 见 [LICENSE](./LICENSE)。  
商标「呼我」「HUWO」「虎虎」「虎妹」归参赛团队所有，Fork 项目请勿冒用官方品牌。

---

## 联系

| 项目 | 信息 |
|------|------|
| 参赛团队 | 衢州呼我网络科技有限公司 |
| 负责人 | Richard.Mao |
| 官网 | https://www.huwo.xyz |
| 小程序 / 抖音 | 呼我 |
| 邮箱 | 36361139@qq.com |
| 电话 | 13858039966 |
| 开源仓库 | https://github.com/HUWOAI/huwo |
