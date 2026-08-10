# Gitee / GitHub 公开仓库建仓指南

> 仅上传 **`open/`** 目录内容，勿包含上级 `backend/`、`AGENTS.md`、`deploy_config.json`。

---

## 一、Gitee 建仓（推荐国内访问）

1. 登录 [Gitee](https://gitee.com/) → **右上角 +** → **新建仓库**
2. 填写：
   - **仓库名称**：`huwo-ai-open` 或 `huwo-diet-agent-demo`
   - **路径**：与名称一致
   - **开源**：公开
   - **许可证**：MIT（与 `LICENSE` 一致）
   - **初始化**：**不要**勾选「使用 Readme 文件初始化」（本地已有）
3. 创建后复制 HTTPS 地址，例如：  
   `https://gitee.com/your-org/huwo-ai-open.git`

### 本地推送（在 `D:\AIEAT\open` 目录）

```powershell
cd D:\AIEAT\open
git init
git add .
git status
git commit -m "feat: HUWO AI 开源 Demo v0.1.0 — 饮食 Agent + 小虎机器人适配器"
git branch -M main
git remote add origin https://gitee.com/your-org/huwo-ai-open.git
git push -u origin main
```

首次推送若提示登录，使用 Gitee 账号 + **私人令牌**（设置 → 私人令牌 → 勾选 projects）。

---

## 二、GitHub 镜像（可选，面向国际开发者）

1. [GitHub New repository](https://github.com/new) → 名称 `huwo-ai-open` → Public → 不初始化 README
2. 同一本地仓库可添加第二个 remote：

```powershell
git remote add github https://github.com/your-org/huwo-ai-open.git
git push -u github main
```

仓库 README 中填 **主仓库 URL**（Gitee 或 GitHub 二选一，建议 Gitee 国内访问快）。

---

## 三、仓库设置建议

| 项 | 建议 |
|----|------|
| 仓库描述 | 吃什么呼我 · 饮食 AI Agent 开源 Demo · MIT |
| Topics / 标签 | `ai-agent`, `diet`, `fastapi`, `huwo`, `volcengine` |
| 默认分支 | `main` |
| README | 使用本仓根目录 `README.md`（已含快速开始） |
| 安全 | 确认 `.env` 未提交；Gitee → 仓库 → 扫描密钥 |

---

## 四、仓库信息填写参考

| 字段 | 填写示例 |
|------|----------|
| 开源仓库地址 | `https://gitee.com/your-org/huwo-ai-open` |
| 开源协议 | MIT |
| 开源说明 | 附链接：`.../blob/main/OPEN_BOUNDARY.md` |
| 可复现说明 | 见 `README.md`：`pip install` + `uvicorn demo.app:app` |
| Demo 在线（若有） | 可选部署 Demo 到云服务器 `http://ip:8765/docs` |

---

## 五、常见问题

**Q：能否把整个 AIEAT 仓库公开？**  
A：不要。仅 `open/` 子目录作为公开仓，商业后端与密钥留在私有仓。

**Q：push 被拒绝 large files？**  
A：本仓不含视频/APK。若误加文件，检查 `.gitignore` 是否包含 `.venv/`。

**Q：国内访问 GitHub 较慢？**  
A：同步镜像到 Gitee，README 同时放两个链接；或提供录屏 + 本地 `run_demo.bat` 步骤。

---

## 六、推送后自检

```powershell
# 克隆到新目录验证
cd %TEMP%
git clone https://gitee.com/your-org/huwo-ai-open.git huwo-test
cd huwo-test
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python scripts\run_demo.py meal-plan
```

应输出三餐 JSON。
