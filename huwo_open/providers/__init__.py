"""Unified LLM client factory for Demo."""

from __future__ import annotations

import os

from openai import AsyncOpenAI

from huwo_open.providers.minimax_h3 import create_minimax_client
from huwo_open.providers.volcano_ark import create_volc_client


def create_llm_client() -> tuple[AsyncOpenAI, str]:
    provider = os.getenv("LLM_PROVIDER", "volc").lower()
    if provider == "minimax":
        return create_minimax_client()
    return create_volc_client()
