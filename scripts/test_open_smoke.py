#!/usr/bin/env python3
"""开源 Demo 冒烟：golden / care / housekeeping 轨迹可跑通。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from scripts.run_demo import _care, _golden, _housekeeping  # noqa: E402


def test_med_reminder_string_schedule_times():
    from huwo_open.agent.skills.med_reminder import create_med_reminder, reset_store

    reset_store()
    row = create_med_reminder(medicine_name="维生素C", schedule_times="08:00,20:00")
    assert row["schedule_times"] == ["08:00", "20:00"]


def main() -> None:
    g = _golden()
    assert len(g["trajectory"]) >= 4, g
    names = [t["name"] for t in g["trajectory"]]
    assert "generate_meal_plan" in names and "open_grocery_checkout" in names

    c = _care()
    assert c["trajectory"][0]["result"].get("medicine_name")
    assert "disclaimer" in c["trajectory"][0]["result"]

    h = _housekeeping()
    score = h["trajectory"][0]["result"]
    assert score.get("score_overall") is not None
    dims = score.get("dimensions") or []
    assert len(dims) >= 6, dims
    assert {d.get("key") for d in dims} >= {"safety", "care", "feed", "symptom", "guide", "ethic"}
    recs = h["trajectory"][3]["result"].get("recommendations") or []
    assert recs
    assert len(recs[0].get("match_reasons") or []) >= 3
    ended = next(t["result"] for t in h["trajectory"] if t["name"] == "end_care_shift")
    assert ended.get("acl_revoked") is True
    assert ended.get("acl_receipt", {}).get("employer_feed_access") == "denied"
    closed = next(t["result"] for t in h["trajectory"] if t["name"] == "list_on_duty_moments")
    assert closed.get("items") == []
    assert closed.get("acl_active") is False

    schema = json.loads((ROOT / "huwo_open" / "agent" / "tools_schema.json").read_text(encoding="utf-8"))
    tool_names = {t["function"]["name"] for t in schema}
    for required in (
        "open_grocery_checkout",
        "create_med_reminder",
        "fair_interview_score",
        "publish_service_profile",
        "start_care_employment",
        "end_care_shift",
        "post_on_duty_moment",
    ):
        assert required in tool_names, required

    test_med_reminder_string_schedule_times()

    print("OPEN smoke PASSED")
    print(json.dumps({"golden_tools": names, "schema_count": len(tool_names)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
