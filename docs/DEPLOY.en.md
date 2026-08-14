# Deploy Guide (English)

中文: [DEPLOY.md](./DEPLOY.md)

## Local Python

```bash
git clone https://github.com/HUWOAI/huwo.git
cd huwo
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env   # optional LLM keys
python -m uvicorn demo.app:app --reload --port 8765
```

## Docker

```bash
cd huwo
cp .env.example .env
docker compose -f deploy/docker-compose.yml up --build
```

## Checklist

- [ ] `GET /health` → ok
- [ ] `GET /demo/golden-path` full trajectory (**preferred, no key**)
- [ ] `GET /demo/housekeeping-path` includes `match_reasons` and off-duty ACL
- [ ] `python scripts/run_demo.py golden`
- [ ] `python scripts/run_demo.py housekeeping`
- [ ] `python scripts/test_open_smoke.py`
- [ ] `GET /demo/meal-plan` returns meal JSON
- [ ] `POST /demo/tool` with `robot_notify`
- [ ] With keys: `POST /demo/chat` → `reply` + `trajectory`; without keys: rule fallback

## vs production

Production at `https://www.huwo.xyz` runs the full FastAPI stack (MySQL, accounts, marketplace, glasses ACL, etc.) — **not** in this repo. This demo only proves the open modules run standalone.
