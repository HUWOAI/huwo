# GOAI 评委速查（AI+眼镜 · 可参赛版）

> 赛题：**无界应用 Boundless Agents · AI+眼镜**  
> 线上产品：https://www.huwo.xyz/AIEAT/  
> 开源仓：https://github.com/HUWOAI/huwo  
> 测试号：`13800000001` / `Ok778899`（邀请码可选 `100001`）

## 一句话

找靠谱育婴师缺的是**可验证信任**。呼我用**量产 AI 眼镜第一视角** + **国标六维公平评测**，落地家政可信直聘 Agent：**测有国标 · 晒有实景 · 配有理由 · 看有证据 · 关有闭环**。

## 手册五性对照（设备原生）

| 要求 | 开源 Demo | 线上产品 |
|------|-----------|----------|
| 第一视角 | `post_on_duty_moment` 眼镜事件帧 | HUWO 眼镜拍照 → 在岗时间线 |
| 语音交互 | Web/脚本可演示工具轨迹 | 唤醒「Hey Luma」+ 全双工通话「呼我AI助手」 |
| 实时感知 | 事件制关键节点（非 24h） | 辅食/买菜/带娃人工触发 |
| 随身陪伴 | Skill 闭环可复现 | App + 眼镜同账号 |
| 轻量反馈 | 轨迹结果可播报示意 | TTS / 眼镜短提示 |

**边界：** 不做简单手机 App 复刻叙事；去掉眼镜则「看/关」故事不完整。

## 30 秒无 Key 复现

```bash
pip install -r requirements.txt
python scripts/run_demo.py housekeeping
python scripts/test_open_smoke.py
```

验证点：

1. `fair_interview_score` → **六维** dimensions  
2. `recommend_service_workers` → 每条 **≥3** `match_reasons`  
3. `end_care_shift` → `employer_feed_access=denied`  
4. 离岗后再 `list_on_duty_moments` → `acl_revoked` / 空列表  

## Agent 闭环（手册 8.2）

感知输入 → 意图（测/晒/配/看/关）→ 工具调用 → 可解释结果 → ACL/信用验证。  
评委模式（线上设置开）：首页可展开工具轨迹。

## 合规声明

- AI 测评 ≠ 人社官方职业鉴定  
- 事件制记录 ≠ 24 小时监控  
- 开源边界见 [OPEN_BOUNDARY.md](../OPEN_BOUNDARY.md)  
- 主体：衢州呼我网络科技有限公司；杭州研发中心：杭州汇融科技有限公司  

## 初赛材料建议链接

| 材料 | 位置 |
|------|------|
| 作品简介 ≤500 字 | [GOAI_SUBMIT_BLURB.md](./GOAI_SUBMIT_BLURB.md) |
| Demo 口播 | [DEMO_SCRIPT.md](./DEMO_SCRIPT.md) |
| 合规 | [COMPLIANCE.md](./COMPLIANCE.md) |
| 第三方 | [THIRD_PARTY.md](./THIRD_PARTY.md) |
