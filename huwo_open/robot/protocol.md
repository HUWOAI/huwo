# 小虎桌面机器人 ↔ 饮食助手 通信协议（Demo / SDK 参考）

## 1. 设计目标

- 手机 APP / Demo 与 **呼我小虎 3 代** 桌面机器人双向通信
- 开源部分仅包含 **协议定义 + Python 参考适配器**（无量产固件、无私有 PCB）
- 商业版闭源：账号绑定、OTA、表情资源包、产测

## 2. 传输层（推荐）

| 场景 | 协议 | 说明 |
|------|------|------|
| 局域网开发 | WebSocket `ws://{robot_ip}:8766/huwo/v1` | Demo 默认 |
| 云端（商业版） | WSS + JWT | 闭源 APP 使用 |
| 备选 | MQTT `huwo/robot/{device_id}/cmd` | 物联网集成 |

## 3. 消息信封

```json
{
  "type": "command | event | ack",
  "msg_id": "uuid",
  "device_id": "robot-demo-001",
  "payload": { }
}
```

## 4. 下行指令（APP → 机器人）

### `show_expression`

```json
{
  "type": "command",
  "payload": {
    "action": "show_expression",
    "expression": "happy | think | sad | surprise | neutral",
    "screen_title": "HUWO",
    "screen_subtitle": "今日午餐推荐"
  }
}
```

### `speak`

```json
{
  "type": "command",
  "payload": {
    "action": "speak",
    "text": "已为你安排清蒸鲈鱼配时蔬",
    "lang": "zh-CN"
  }
}
```

### `show_meal_card`

```json
{
  "type": "command",
  "payload": {
    "action": "show_meal_card",
    "meal_type": "午餐",
    "name": "清蒸鲈鱼+清炒时蔬",
    "calories": 240,
    "reason": "高蛋白低脂"
  }
}
```

## 5. 上行事件（机器人 → APP）

### `wake_word`

用户说「呼我」或按键唤醒。

### `meal_log_request`

```json
{
  "type": "event",
  "payload": {
    "action": "meal_log_request",
    "transcript": "我刚吃了一份沙拉"
  }
}
```

## 6. Demo 适配器

见 `huwo_open/robot/adapter.py`：`RobotAdapter` 在内存中模拟设备，可替换为真实 WebSocket 客户端。

## 7. 与闭源 APP 的边界

| 开源 | 闭源 |
|------|------|
| 协议 JSON Schema | 设备配对、用户绑定 |
| 参考 Python 适配器 | Android/iOS 原生 SDK |
| 模拟器 | 量产固件、表情 IP 资源 |
