# 呼我 HUWO — 开源 Demo

[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

> **呼我人工智能 · 家庭健康服务平台** — Agent 内核开源模块（MIT）  
> 口号：**您有所呼，我有所应**  
> 公开仓库：**https://github.com/HUWOAI/huwo**  
> 团队：**呼我网络科技** · EN：**Callme Group LLC**  
> 负责人：毛新明 Richard · 官网：https://www.huwo.xyz · 线上 Demo：https://www.huwo.xyz/AIEAT/

本目录为 **HUWOAI/huwo** 开源代码，与闭源商业版 APP 后端分离。对齐 GOAI 赛道二「无界应用｜Boundless Agents」：**可运行、可演示、可复制**，强调工具调用与任务闭环。

---

## 开源边界（一句话）

**开源：可复用的家庭健康 Agent Skill / Tool Schema、Prompt、小虎协议适配器、Demo 与模型调用示例。**  
**闭源：完整 APP 后端、账号/社交、用户家庭数据、会员变现、私有知识库、量产固件、开放平台生产密钥。**

详细说明见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md)。

- [Gitee/GitHub 建仓指南](./docs/GITEE_SETUP.md)
- [3 分钟 Demo 脚本](./docs/DEMO_SCRIPT.md)
- [合规要点摘要](./docs/COMPLIANCE.md)

---

## 30 秒跑通（无需大模型 Key）

```bash
cd open
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_demo.py golden
python scripts/run_demo.py care
python scripts/run_demo.py housekeeping
```

| 命令 | 闭环 |
|------|------|
| `golden` | 清淡晚餐 → 清单 → 京东秒送示意 → 附近 → 小虎通知 |
| `care` | 吃药提醒创建/列表 → 小虎播报 |
| `housekeeping` | 公平面试 → 挂牌 → 需求 → 推荐 → 考证包 |

启动 Web Demo：

```bash
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
```

- http://127.0.0.1:8765/docs — Swagger  
- http://127.0.0.1:8765/demo/golden-path  
- http://127.0.0.1:8765/demo/care-path  
- http://127.0.0.1:8765/demo/housekeeping-path  
- http://127.0.0.1:8765/meta/tools — 完整 Tool Schema  

---

## 配置大模型（可选，用于 `/demo/chat`）

```bash
cp .env.example .env
```

| 变量 | 说明 |
|------|------|
| `VOLC_ARK_API_KEY` | 火山方舟 API Key |
| `VOLC_ARK_MODEL` | 推理接入点 ID |
| `MINIMAX_API_KEY` | MiniMax 示例 |
| `LLM_PROVIDER` | `volc` 或 `minimax` |

---

## 目录结构

```
open/
├── LICENSE                 MIT
├── README.md
├── OPEN_BOUNDARY.md
├── requirements.txt
├── .env.example
├── huwo_open/
│   ├── agent/
│   │   ├── prompts/
│   │   ├── skills/         饮食 / 百科 / 吃药 / 家政
│   │   ├── tools_schema.json
│   │   └── orchestrator.py
│   ├── providers/          火山方舟 / MiniMax
│   ├── integrations/       买菜深链示意
│   └── robot/              小虎协议适配器
├── demo/                   FastAPI Demo
├── docs/
└── scripts/
```

---

## 与商业版关系

| 模块 | 开源 Demo | 商业版 huwo.xyz |
|------|-----------|-----------------|
| Agent Skill / Schema | ✅ | ✅ |
| 食物百科样本库 | ✅ 500+ | ✅ + 条码/USDA |
| 吃药提醒 | ✅ 内存 Demo | ✅ MySQL 持久化 |
| 家政公平评测/供需 | ✅ 内存 Demo | ✅ 服务市场 |
| 京东秒送 | ✅ 深链示意 | ✅ 开放平台对接 |
| 账号 / 社交 / 群组 | ❌ | ✅ |
| 全双工语音 / RTC | ❌ | ✅ |

---

## License

MIT — 详见 [LICENSE](./LICENSE)。商标「呼我」「HUWO」及闭源服务不在许可范围内。
