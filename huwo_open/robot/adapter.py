"""小虎机器人交互适配器 — Demo 内存模拟 + 可扩展 WebSocket。"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Any


@dataclass
class RobotAdapter:
    device_id: str = "robot-demo-001"
    _events: list[dict[str, Any]] = field(default_factory=list)

    def notify(
        self,
        *,
        expression: str = "happy",
        tts_text: str = "",
        screen_title: str = "HUWO",
        screen_subtitle: str = "",
        meal_card: dict | None = None,
    ) -> dict[str, Any]:
        msg_id = str(uuid.uuid4())
        commands: list[dict] = [
            {
                "type": "command",
                "msg_id": msg_id,
                "device_id": self.device_id,
                "payload": {
                    "action": "show_expression",
                    "expression": expression,
                    "screen_title": screen_title,
                    "screen_subtitle": screen_subtitle,
                },
            },
        ]
        if tts_text:
            commands.append(
                {
                    "type": "command",
                    "msg_id": msg_id,
                    "device_id": self.device_id,
                    "payload": {"action": "speak", "text": tts_text, "lang": "zh-CN"},
                }
            )
        if meal_card:
            commands.append(
                {
                    "type": "command",
                    "msg_id": msg_id,
                    "device_id": self.device_id,
                    "payload": {"action": "show_meal_card", **meal_card},
                }
            )
        self._events.extend(commands)
        return {"ok": True, "sent": len(commands), "msg_id": msg_id, "commands": commands}

    def drain_events(self) -> list[dict]:
        out = list(self._events)
        self._events.clear()
        return out
