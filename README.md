# 呼我 HUWO — 开源 Demo（MIT）

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)
[![English](https://img.shields.io/badge/README-English-blue)](./README.en.md)

> **呼我人工智能 · 家庭超级智能体** — Agent 内核开源模块  
> 口号：**您有所呼，我有所应**  
> 团队：**衢州呼我网络科技有限公司**（EN: Quzhou HUWO Network Technology Co., Ltd.）  
> 呼我杭州研发中心：**杭州汇融科技有限公司**  
> 线上产品：https://www.huwo.xyz/AIEAT/  
> 赛题对齐：GOAI 无界应用 · **AI+眼镜** · 家政可信直聘 Agent

**English:** [README.en.md](./README.en.md)

本仓库提供**可运行、可演示、可复制**的黄金路径 Demo：饮食决策、健康关怀、以及 **测 → 晒 → 配 → 看 → 关** 家政直聘闭环（含 ≥3 条匹配解释、眼镜在岗事件帧、离岗 ACL）。

---

## 为什么开源这个仓库？

评委与开发者**无需大模型 Key**，即可验证：

1. Agent **工具调用轨迹**可复现（非纯聊天套壳）  
2. 家政路径含 **匹配解释 schema** 与 **离岗关闭雇主影像访问（ACL）**  
3. 商业 API 可替换；题库密钥与生产数据不在本仓  

完整 App / 账号 / 眼镜固件见线上产品；开源边界见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md)。

---

## 30 秒跑通（无需大模型 Key）

```bash
git clone https://github.com/HUWOAI/huwo.git
cd huwo
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_demo.py golden
python scripts/run_demo.py care
python scripts/run_demo.py housekeeping
python scripts/test_open_smoke.py
```

| 命令 | 闭环 |
|------|------|
| `golden` | 清淡晚餐约束 → 清单 → 买菜深链示意 → 附近 → 小虎 `robot_notify` |
| `care` | 吃药提醒创建/列表（任务助手边界，非审方） |
| `housekeeping` | **测**公平面试 → **晒**挂牌 → **配**≥3 条解释 → **看**眼镜三捷径事件 → **关**离岗 ACL（`employer_feed_access=denied`） |

启动 Web Demo：

```bash
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
```

| URL | 说明 |
|-----|------|
| http://127.0.0.1:8765/docs | Swagger |
| http://127.0.0.1:8765/demo/golden-path | 饮食黄金路径 |
| http://127.0.0.1:8765/demo/care-path | 健康关怀 |
| http://127.0.0.1:8765/demo/housekeeping-path | 家政测晒配看关 + ACL |
| http://127.0.0.1:8765/meta/tools | Tool Schema |
| http://127.0.0.1:8765/demo/metrics | 评测自检摘要 |

---

## 线上产品（完整能力）

| 项 | 链接 / 说明 |
|----|-------------|
| H5 Demo | https://www.huwo.xyz/AIEAT/ |
| 官网 | https://www.huwo.xyz/ |
| 登录 | **验证码登录** 或 **手机号+密码登录**；开通时可填 **邀请码（可选）** |
| 测试账号 | `13800000001` / 密码 `Ok778899`（邀请码可选 `100001`） |
| 通话默认情景 | **呼我AI助手**（测评 / 找人 / 办事） |
| 眼镜 | Tab「看辅食 / 记买菜 / 记带娃瞬间」→ 在岗时间线；结束工作 → ACL 回执 |
| 评委模式 | 设置 → 评委模式开 → 首页 Agent 轨迹展开 |

叙事主线：**国标测评 → 影像简历 → 匹配解释 → 眼镜第一视角 → 离岗关权限**。

---

## 开源边界（一句话）

| 开放（MIT） | 不开放 |
|-------------|--------|
| Agent Skill / Tool Schema / Prompt | 生产 `.env`、支付证书 |
| 匹配解释字段、在岗/离岗 ACL 示意 | 用户隐私数据、完整题库密钥 |
| 小虎协议适配器、无 Key Demo | 量产固件、完整商业后端 |

详见 [OPEN_BOUNDARY.md](./OPEN_BOUNDARY.md) · [English boundary](./OPEN_BOUNDARY.en.md)。

---

## 文档

| 中文 | English | 说明 |
|------|---------|------|
| [docs/DEMO_SCRIPT.md](./docs/DEMO_SCRIPT.md) | [docs/DEMO_SCRIPT.en.md](./docs/DEMO_SCRIPT.en.md) | 3 分钟演示脚本 |
| [docs/COMPLIANCE.md](./docs/COMPLIANCE.md) | [docs/COMPLIANCE.en.md](./docs/COMPLIANCE.en.md) | 合规摘要 |
| [docs/METRICS.md](./docs/METRICS.md) | — | 评测指标与复现 |
| [docs/THIRD_PARTY.md](./docs/THIRD_PARTY.md) | — | 商业 API / 依赖披露 |
| [docs/DEPLOY.md](./docs/DEPLOY.md) | [docs/DEPLOY.en.md](./docs/DEPLOY.en.md) | 部署说明 |
| [docs/GITEE_SETUP.md](./docs/GITEE_SETUP.md) | — | 镜像说明 |

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

**无 Key 不影响** `golden` / `care` / `housekeeping` 规则路径。未配置 Key 时，`/demo/chat` 自动降级为规则引擎。

---

## 目录结构

```
├── LICENSE                 MIT
├── README.md               中文介绍
├── README.en.md            English overview
├── OPEN_BOUNDARY.md        开源边界
├── OPEN_BOUNDARY.en.md
├── requirements.txt
├── .env.example
├── huwo_open/
│   ├── agent/              prompts · skills · tools_schema · orchestrator
│   ├── providers/          火山方舟 / MiniMax 示例
│   ├── integrations/       买菜深链示意
│   └── robot/              小虎协议适配器
├── demo/                   FastAPI Demo
├── docs/
└── scripts/
    ├── run_demo.py
    └── test_open_smoke.py
```

---

## 商标与联系

「呼我」「HUWO」商标不属于 MIT 授权范围。  
官网：https://www.huwo.xyz · 开源协作见 [Issues](https://github.com/HUWOAI/huwo/issues)。
