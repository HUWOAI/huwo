# UI 组件示例

商业版 H5 使用 **uni-app (Vue3)**。开源仓提供设计参考，完整页面在闭源 `frontend/`。

## 三餐卡片布局要点

- 餐次标签（早/午/晚）+ 菜名 + kcal / 蛋白质
- AI 推荐理由一行
- 操作：「换一换」「已吃」「一键下单（商业版跳转第三方）」

## 对接开源 Demo API

```javascript
// H5 fetch 示例
const plan = await fetch('http://127.0.0.1:8765/demo/meal-plan').then(r => r.json())
const meals = plan.meals
```

## 小虎机器人联动

调用 `POST /demo/tool`：

```json
{
  "name": "robot_notify",
  "arguments": {
    "expression": "happy",
    "tts_text": "午餐推荐清蒸鲈鱼",
    "screen_title": "HUWO"
  }
}
```

然后 `GET /demo/robot/events` 查看模拟下发指令。

完整协议见 `huwo_open/robot/protocol.md`。
