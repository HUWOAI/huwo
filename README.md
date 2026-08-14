# 呼我 HUWO — 开源 Demo（MIT）

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)

> **呼我人工智能 · 家庭健康服务平台** — Agent 内核开源模块  
> 口号：**您有所呼，我有所应**  
> 团队：**呼我网络科技**（EN: Callme Group LLC）  
> 线上产品：https://www.huwo.xyz/AIEAT/  
> 本仓库：**可运行、可演示、可复制**的饮食 / 关怀 / 家政 Agent 闭环 Demo

对齐赛道关键词：行业 Agent、任务闭环、工具调用、多模态入口（语音/多端）、数据合规。

---

## 30 秒跑通（无需大模型 Key）

```bash
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
| `golden` | 清淡晚餐约束 → 清单 → 买菜深链示意 → 附近 → 小虎 `robot_notify` |
| `care` | 吃药提醒创建/列表示意（任务助手边界，非审方） |
| `housekeeping` | 公平面试 → 挂牌 → ≥3 条匹配解释 → 眼镜三捷径 → 离岗 ACL |

启动 Web Demo：

```bash
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
```

- http://127.0.0.1:8765/docs — Swagger  
- http://127.0.0.1:8765/demo/golden-path  
- http://127.0.0.1:8765/demo/care-path  
- http://127.0.0.1:8765/demo/housekeeping-path  
- http://127.0.0.1:8765/meta/tools — Tool Schema  
- http://127.0.0.1:8765/demo/metrics — 评测自检摘要  

---

## 开源边界（一句话）

**开源**：可复用的家庭健康 Agent Skill / Tool Schema、Prompt、小虎协议适配器、Demo、模型调用示例。  
**闭源**：完整 APP 后端、账号/社交、用户家庭数据、会员变现、生产密钥、量产固件。

详见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md)。

---

## 文档

| 文档 | 说明 |
|------|------|
| [docs/DEMO_SCRIPT.md](./docs/DEMO_SCRIPT.md) | 3 分钟演示脚本 |
| [docs/COMPLIANCE.md](./docs/COMPLIANCE.md) | 合规摘要 |
| [docs/METRICS.md](./docs/METRICS.md) | 评测指标与复现 |
| [docs/THIRD_PARTY.md](./docs/THIRD_PARTY.md) | 商业 API / 依赖披露 |
| [docs/DEPLOY.md](./docs/DEPLOY.md) | 部署说明 |
| [docs/GITEE_SETUP.md](./docs/GITEE_SETUP.md) | 镜像说明 |

---

## 可选：配置大模型（`/demo/chat`）

```bash
cp .env.example .env
```

| 变量 | 说明 |
|------|------|
| `VOLC_ARK_API_KEY` | 火山方舟 API Key |
| `VOLC_ARK_MODEL` | 推理接入点 ID |
| `MINIMAX_API_KEY` | MiniMax 示例 |
| `LLM_PROVIDER` | `volc` 或 `minimax` |

**无 Key 不影响** `golden` / `care` / `housekeeping` 规则路径复现。

---

## 目录结构

```
├── LICENSE                 MIT
├── README.md
├── OPEN_BOUNDARY.md
├── requirements.txt
├── .env.example
├── huwo_open/
│   ├── agent/              prompts · skills · tools_schema · orchestrator
│   ├── providers/          火山方舟 / MiniMax 示例
│   ├── integrations/       买菜深链示意
│   └── robot/              小虎协议适配器
├── demo/                   FastAPI Demo
├── docs/
└── scripts/run_demo.py
```

---

## 商标与联系

「呼我」「HUWO」商标不属于 MIT 授权范围。  
官网：https://www.huwo.xyz · 开源协作见仓库 Issues。
