# 评测指标与复现（开源仓）

对齐「可运行 Demo + 运行证据」。完整参赛评测表见商业仓材料包；本文件保证 **fork 本仓库即可自检**。

## 快速自检

```bash
pip install -r requirements.txt
python scripts/test_open_smoke.py
python scripts/run_demo.py golden
python scripts/run_demo.py housekeeping
python -m uvicorn demo.app:app --port 8765
# 打开 /demo/metrics 、 /demo/golden-path 、 /demo/housekeeping-path
```

## 指标

| 指标 | 期望 |
|------|------|
| `test_open_smoke.py` | 打印 `OPEN smoke PASSED` |
| golden 退出码 | 0；trajectory 含规划/清单/深链或附近/`robot_notify` |
| housekeeping | 推荐项 `match_reasons` **≥3**；`end_care_shift.acl_revoked`；离岗后 moments 为空 |
| 无 Key | 规则路径可跑；`/demo/chat` 可降级 |

## 失败分支（演示建议）

- 缺忌口信息 → 追问后再规划（商业对话情景）  
- 无模型 Key → 使用本仓库规则路径，勿伪装在线 LLM  
- 健康追问 → 免责，不审方  
- 离岗后访问 → 应体现 ACL deny，而非继续吐出在岗影像  

## 基线

本地曾于 2026-08-14 验证 `housekeeping` + smoke（含 ACL）exit 0。请在你的环境复测后更新日期。
