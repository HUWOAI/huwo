"""MiniMax H3 — OpenAI-compatible API example (configure per official docs)."""

from __future__ import annotations

import os

from openai import AsyncOpenAI


def create_minimax_client() -> tuple[AsyncOpenAI, str]:
    api_key = os.getenv("MINIMAX_API_KEY", "")
    base_url = os.getenv("MINIMAX_BASE_URL", "https://api.minimax.chat/v1")
    model = os.getenv("MINIMAX_MODEL", "MiniMax-Text-01")
    if not api_key:
        raise RuntimeError("请配置 MINIMAX_API_KEY（见 .env.example）")
    return AsyncOpenAI(api_key=api_key, base_url=base_url, timeout=60.0), model
