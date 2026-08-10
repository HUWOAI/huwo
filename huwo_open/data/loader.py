"""Load bundled JSON datasets (no database required)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent


@lru_cache(maxsize=8)
def load_json(name: str) -> list | dict:
    path = DATA_DIR / name
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def dishes() -> list[dict]:
    return load_json("sample_dishes.json")  # type: ignore[return-value]


def pois() -> list[dict]:
    return load_json("sample_poi.json")  # type: ignore[return-value]


def default_preferences() -> dict:
    return load_json("sample_preferences.json")  # type: ignore[return-value]


def foods() -> list[dict]:
    return load_json("sample_foods.json")  # type: ignore[return-value]
