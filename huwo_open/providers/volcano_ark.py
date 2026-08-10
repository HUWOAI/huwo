"""Volcano Ark (豆包) OpenAI-compatible client wrapper."""

from __future__ import annotations

import os

from openai import AsyncOpenAI


def create_volc_client() -> tuple[AsyncOpenAI, str]:
    api_key = os.getenv("VOLC_ARK_API_KEY", "")
    base_url = os.getenv("VOLC_ARK_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3")
    model = os.getenv("VOLC_ARK_MODEL", "")
    if not api_key or not model:
        raise RuntimeError("请配置 VOLC_ARK_API_KEY 与 VOLC_ARK_MODEL（见 .env.example）")
    return AsyncOpenAI(api_key=api_key, base_url=base_url, timeout=60.0), model
