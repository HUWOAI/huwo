# 3 分钟 Demo 脚本（开源内核 · 黄金闭环）

> 团队：**衢州呼我网络科技有限公司**  
> 呼我杭州研发中心：**杭州汇融科技有限公司**  
> 登录：验证码 / 手机号+密码；邀请码可选  
> 产品：呼我人工智能 · 家庭超级智能体  
> 赛题对齐：GOAI **AI+眼镜** · 家政可信直聘 Agent  
> English: [DEMO_SCRIPT.en.md](./DEMO_SCRIPT.en.md)

---

## 0:00–0:20 开场

「我们是衢州呼我网络科技有限公司。口号：您有所呼，我有所应。开源仓演示可验证的 Agent 闭环——饮食、关怀、以及家政 **测晒配看关**——不是陪聊。」

---

## 0:20–0:55 饮食黄金闭环

```bash
python scripts/run_demo.py golden
```

或：`http://127.0.0.1:8765/demo/golden-path`

口述：「轨迹含三餐规划 → 采购清单 → 买菜深链示意 → 附近 → 小虎 robot_notify。无大模型 Key 可验证。」

---

## 0:55–1:50 家政测→晒→配→看→关（主叙事）

```bash
python scripts/run_demo.py housekeeping
```

或：`http://127.0.0.1:8765/demo/housekeeping-path`

口述要点：

1. **测**：`fair_interview_score` 规则透明评分  
2. **晒**：`publish_service_profile` 挂牌  
3. **配**：`recommend_service_workers` 每条 **≥3 条** `match_reasons`  
4. **看**：`post_on_duty_moment` 看辅食 / 记买菜 / 带娃瞬间  
5. **关**：`end_care_shift` → `acl_receipt.employer_feed_access = denied`；再 `list_on_duty_moments` 为空  

可选加一句：`python scripts/run_demo.py care`（吃药提醒，任务助手边界）。

---

## 1:50–2:30 线上产品（有网）

打开 https://www.huwo.xyz/AIEAT/  

- 打电话情景：**呼我AI助手**  
- 市场卡片看 3 条匹配解释  
- 眼镜三捷径或「评委演示注入一帧」  
- 家庭相册 **结束工作** → ACL 回执停 2 秒  
- 设置 → **评委模式** → 工具轨迹展开  

---

## 2:30–2:50 开源边界 + 合规

「MIT 开源 Skill / Schema / Prompt / ACL 示意；账号、社交、生产密钥、固件闭源。营养/用药不替代医疗；不做 24h 监控承诺。」

---

## 2:50–3:00 收束

「您有所呼，我有所应。仓库 https://github.com/HUWOAI/huwo ，已上线可演示。」
