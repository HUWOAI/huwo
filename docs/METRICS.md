# 评测指标与复现（开源仓）

对齐「可运行 Demo + 运行证据」。完整参赛评测表见商业仓材料包；本文件保证 **fork 本仓库即可自检**。

## 快速自检

```bash
pip install -r requirements.txt
python scripts/run_demo.py golden
python -m uvicorn demo.app:app --port 8765
# 浏览器打开 /demo/metrics 与 /demo/golden-path
```

## 指标

| 指标 | 期望 |
|------|------|
| golden 退出码 | 0 |
| trajectory | 含规划/清单/附近或深链/robot_notify 等步骤 |
| 无 Key | 规则路径可跑 |
| care / housekeeping | 退出码 0 |

## 失败分支（演示建议）

- 缺忌口信息 → 追问后再规划（商业对话情景）  
- 无模型 Key → 使用本仓库规则路径，勿伪装在线 LLM  
- 健康追问 → 免责，不审方  

## 基线

本地曾于 2026-08-12 验证 `golden` exit 0（Windows）。请在你的环境复测后更新日期。
