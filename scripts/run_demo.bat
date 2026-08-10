@echo off
cd /d %~dp0..
python -m venv .venv 2>nul
call .venv\Scripts\activate
pip install -r requirements.txt -q
if not exist .env copy .env.example .env
echo.
echo === 无 API Key 时可访问 http://127.0.0.1:8765/demo/meal-plan ===
echo === 配置 .env 后可用 /demo/chat 调用大模型 ===
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
