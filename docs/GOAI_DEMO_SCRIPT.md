# GOAI 答辩 · 3 分钟 Demo 脚本

> 《吃什么，呼我》— 内核开源 Demo 现场演示  
> 建议：屏幕分屏（左：Swagger / 终端，右：PPT 或产品截图）

---

## 0:00–0:30 开场（问题 + 方案）

**口述：**

「各位评委好，我们是杭州汇融、衢州呼我网络，产品叫 **《吃什么，呼我》**。

痛点是：年轻人和家庭每天纠结吃什么、怎么吃才健康，异地子女也很难关心父母饮食。

我们的方案是 **AI 垂直饮食智能** —— 手机 APP + **小虎桌面机器人**，语音一句话完成三餐规划、记饮食、附近餐厅推荐；硬件我们在桐乡、深圳有近十万方产线。

今天演示的是 **GOAI 开源模块**：饮食 Agent 核心能力，MIT 协议，评审可 clone 后本地复现。」

**屏幕：** 打开 `https://gitee.com/.../huwo-ai-open` 或本地 `http://127.0.0.1:8765/docs`

---

## 0:30–1:15 开源边界（15 秒）+ 无 Key 跑 Skill

**口述：**

「我们采用 **内核开源**：Agent Skill、Prompt、小虎机器人协议适配器开源；完整 APP 账号、碰一碰社交、会员和数据闭源，保护商业壁垒。协议 MIT，不传染闭源后端。」

**操作 1 — 终端（无需大模型 Key）：**

```powershell
cd open
python scripts\run_demo.py meal-plan
```

**口述：** 「这是三餐规划 Skill，从示例菜品库按用户偏好（均衡、清淡、花生过敏）生成早中晚推荐。」

**操作 2 — 浏览器：**

打开 `GET /demo/nearby?city=衢州`

**口述：** 「附近餐厅 POI 搜索，并生成美团、饿了么 Deeplink，商业版一键跳转下单。」

---

## 1:15–2:15 Agent 工具编排 + 大模型（可选）

**口述：**

「核心是可扩展的 **工具编排**：`tools_schema.json` 定义 search_dish、generate_meal_plan、search_nearby、get_shopping_list、robot_notify 等；`orchestrator.py` 统一 dispatch，对接火山方舟或 MiniMax。」

**操作 3 — Swagger：**

`POST /demo/tool`

```json
{
  "name": "robot_notify",
  "arguments": {
    "expression": "happy",
    "tts_text": "午餐推荐清蒸鲈鱼配时蔬",
    "screen_title": "HUWO"
  }
}
```

然后 `GET /demo/robot/events`

**口述：** 「这是 **小虎 3 代桌面机器人** 开源适配器：下发表情、TTS、餐食卡片。协议文档在 `robot/protocol.md`，量产固件闭源。」

**（若已配置 .env API Key）操作 4：**

`POST /demo/chat`

```json
{ "message": "我在衢州，帮我安排今天晚餐，要清淡一点" }
```

**口述：** 「大模型自动选择工具，返回可执行的三餐/推荐结果。」

---

## 2:15–2:45 竞品吸收 + 差异化

**口述（可配合一页 PPT）：**

| 能力 | 对标 | 我们 |
|------|------|------|
| 拍照记餐 | Cal AI | 视觉识餐 API（商业版） |
| 膳食+买菜清单 | Fay | Skill 已开源 Demo |
| 本地 POI | 美团 | 30 城 + Deeplink |
| 实时语音 | 豆包 | 火山 RTC（商业版） |
| 硬件 | — | 虎虎/虎妹桌面机器人 + 自有产线 |

「差异化：**家庭饮食记忆 + 语音优先 + 软硬一体**，不是纯 Chatbot。」

---

## 2:45–3:00 收尾

**口述：**

「开源仓库 `open/` 已含 LICENSE、README、部署脚本与 Docker；评审 clone 后 30 分钟内可跑通 Demo。

完整产品已上线 huwo.xyz，3 代小虎机器人正与 APP 打通。

谢谢各位评委，欢迎提问。」

---

## 备用：无网络 / 无 Key 最小路径

仅执行以下三条，保证 90 秒内完成：

1. `python scripts\run_demo.py meal-plan`
2. `python scripts\run_demo.py shopping`
3. 浏览器打开 `/docs` → 展示 `tools_schema` 与 `OPEN_BOUNDARY.md`

---

## 评委可能提问 · 参考答法

**Q：为什么不开源全部 APP？**  
A：创业团队需保留社交、用户数据与商业化；GOAI 允许内核开源，我们 Agent 层已完整可复现。

**Q：和豆包/美团有什么区别？**  
A：垂直饮食 + 家庭协同 + 机器人屏显；不做通用对话，做「吃什么到下单」闭环。

**Q：开源如何持续？**  
A：复赛迭代 huwo-ai-skills 插件仓、城市 POI 贡献模板、机器人 SDK 示例。

**Q：硬件能否自己造？**  
A：协议与适配器开源；PCB/固件认证后采购官方主控板，桐乡深圳产线代工。
