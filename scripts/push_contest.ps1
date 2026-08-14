# 推送可参赛开源版到 GitHub（代理可用时执行）
# 用法（PowerShell）:
#   cd D:\AIEAT\open
#   .\scripts\push_contest.ps1
#
# 若本机 Clash/V2Ray 在 12334，会自动走代理；否则直连。

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

$proxy = "http://127.0.0.1:12334"
$proxyOk = $false
try {
  $tcp = Test-NetConnection 127.0.0.1 -Port 12334 -WarningAction SilentlyContinue
  $proxyOk = [bool]$tcp.TcpTestSucceeded
} catch { $proxyOk = $false }

if ($proxyOk) {
  $env:HTTP_PROXY = $proxy
  $env:HTTPS_PROXY = $proxy
  Write-Host "Using proxy $proxy"
  git push origin main
  git tag -f goai-contest-20260815
  git push origin goai-contest-20260815 --force
} else {
  Write-Host "Proxy $proxy not listening; trying direct (may fail in CN)..."
  git -c http.proxy= -c https.proxy= push origin main
  git tag -f goai-contest-20260815
  git -c http.proxy= -c https.proxy= push origin goai-contest-20260815 --force
}

git status -sb
git log -1 --oneline
Write-Host "Remote: https://github.com/HUWOAI/huwo"
Write-Host "Tag: goai-contest-20260815"
