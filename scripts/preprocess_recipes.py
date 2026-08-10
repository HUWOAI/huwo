"""Normalize raw recipe CSV/JSON lines into sample_dishes.json format."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="输入 JSON 数组文件")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "huwo_open" / "data" / "sample_dishes.json",
    )
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8"))
    out = []
    for r in rows:
        out.append(
            {
                "name": r["name"],
                "category": r.get("category", "主食"),
                "calories": int(r.get("calories", 200)),
                "protein": int(r.get("protein", 5)),
                "tags": r.get("tags", ""),
            }
        )
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(out)} dishes -> {args.output}")


if __name__ == "__main__":
    main()
