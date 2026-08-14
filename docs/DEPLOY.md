# Deploy Guide

English: [DEPLOY.en.md](./DEPLOY.en.md)

## Local Python

```bash
git clone https://github.com/HUWOAI/huwo.git
cd huwo
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # 可选：配置大模型
python -m uvicorn demo.app:app --reload --port 8765
```

## Docker

```bash
cd huwo
cp .env.example .env
docker compose -f deploy/docker-compose.yml up --build
```

## 验证清单

- [ ] `GET /health` 返回 ok
- [ ] `GET /demo/golden-path` 完整 trajectory（**推荐，无需 Key**）
- [ ] `GET /demo/housekeeping-path` 含 `match_reasons` 与离岗 ACL
- [ ] `python scripts/run_demo.py golden`
- [ ] `python scripts/run_demo.py housekeeping`
- [ ] `python scripts/test_open_smoke.py`
- [ ] `GET /demo/meal-plan` 返回三餐 JSON
- [ ] `POST /demo/tool` body `{"name":"robot_notify","arguments":{"expression":"happy","tts_text":"你好"}}`
- [ ] 配置 Key 后 `POST /demo/chat` → `reply` + `trajectory`；无 Key 时规则降级

## 与闭源生产环境

生产环境 `https://www.huwo.xyz` 使用完整 FastAPI 后端（MySQL、账号、服务市场、眼镜 ACL 等），**不在本仓库**。  
本 Demo 仅验证开源模块可独立运行。
