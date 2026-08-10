# 部署说明

## 本地 Python

```bash
cd open
python -m venv .venv && source .venv/bin/activate  # Windows 用 Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # 可选：配置大模型
python -m uvicorn demo.app:app --reload --port 8765
```

## Docker

```bash
cd open
cp .env.example .env
docker compose -f deploy/docker-compose.yml up --build
```

## 验证清单（GOAI 评审）

- [ ] `GET /health` 返回 ok
- [ ] `GET /demo/meal-plan` 返回三餐 JSON
- [ ] `GET /demo/nearby?city=衢州` 返回 POI 列表
- [ ] `POST /demo/tool` body `{"name":"robot_notify","arguments":{"expression":"happy","tts_text":"你好"}}`
- [ ] 配置 Key 后 `POST /demo/chat` body `{"message":"帮我安排晚餐"}`

## 与闭源生产环境

生产环境 `https://www.huwo.xyz` 使用完整 FastAPI 后端（MySQL、账号、社交等），**不在本仓库**。  
本 Demo 仅验证开源模块可独立运行。
