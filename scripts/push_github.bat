@echo off
REM 推送 open/ 开源首批代码到 GitHub HUWOAI/huwo
REM 使用前：在 GitHub → Settings → Developer settings → Personal access tokens
REM 创建 classic token，勾选 repo 权限

cd /d %~dp0..
echo Remote: 
git remote -v
echo.
echo 即将推送到 https://github.com/HUWOAI/huwo.git (branch: main)
echo.
if defined GITHUB_TOKEN (
  echo 使用环境变量 GITHUB_TOKEN 推送...
  git -c http.proxy=http://127.0.0.1:12334 -c https.proxy=http://127.0.0.1:12334 push https://x-access-token:%GITHUB_TOKEN%@github.com/HUWOAI/huwo.git main
) else (
  echo 若提示登录，用户名填 GitHub 用户名，密码处粘贴 Personal Access Token
  echo 或先设置: set GITHUB_TOKEN=ghp_xxxx  再运行本脚本
  echo.
  git -c http.proxy=http://127.0.0.1:12334 -c https.proxy=http://127.0.0.1:12334 push -u origin main
)
if %ERRORLEVEL% EQU 0 (
  echo.
  echo 成功! 仓库: https://github.com/HUWOAI/huwo
) else (
  echo.
  echo 推送失败。常见原因:
  echo  1. 网络无法访问 github.com — 请在本机 VPN/代理环境下重试
  echo  2. 未配置 Token — 使用 GitHub PAT 作为密码
  echo  3. 仓库已有内容 — 先 git pull origin main --rebase 再 push
  echo.
  echo 备用: 使用 git bundle 在有网络的机器导入:
  echo    git clone https://github.com/HUWOAI/huwo.git
  echo    cd huwo
  echo    git pull ..\huwo-open-v0.1.0.bundle main
  echo    git push origin main
)
pause
