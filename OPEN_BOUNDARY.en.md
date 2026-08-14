# Open-Source Boundary (English)

This project uses a **kernel-open** model: reproducible Agent skills and demos are MIT-licensed; the full commercial product evolves separately. Aligned with GOAI “Open. Share. Build.”

## 1. What is open (MIT)

- Family / home-care Agent skills (meal planning, food intel sketches, med-reminder assistant boundary, **fair interview + supply/demand match**)
- **Match-reason schema** (≥3 explainable reasons) and **on-duty / off-duty ACL sketch** (`employer_feed_access=denied` after shift end)
- Recipe/nutrition sample scripts, grocery deeplink sketches
- Xiaohu desktop-robot adapter & protocol notes
- Demo deploy scripts, Volcano / MiniMax call examples, sample config & docs

Public repo: **https://github.com/HUWOAI/huwo**

## 2. What stays closed

Mobile app full business backend, account system, social features, private user data, membership/commerce, private knowledge bases, production open-platform secrets (e.g. JD delivery), **mass-production firmware / PCB** — commercial assets, **not** open-sourced here.

## 3. Third-party dependencies

Volcano Engine (Ark LLM, speech/RTC, etc.), MiniMax, and Python packages listed in `requirements.txt` under their own licenses. API keys are configured by deployers; the repo only ships placeholders (`.env.example`).

## 4. Roadmap

We keep iterating skills, smoke tests, and docs in this single MIT repo. We do not invent fake multi-repo splits. Firmware and commercial backends remain closed.

**IP** belongs to **Quzhou HUWO Network Technology Co., Ltd.**（衢州呼我网络科技有限公司）.  
Hangzhou R&D center: **Hangzhou Huirong Technology Co., Ltd.**（杭州汇融科技有限公司）.  
Site: www.huwo.xyz · Open-source contact via GitHub Issues.

---

## FAQ

**Why not open everything?**  
Differentiation sits in family memory, compliant operations, and multi-device coordination. The open slice focuses on reproducible skills/demos for “fork and verify.”

**How does the commercial product map to this demo?**  
Demo exposes equivalent tool schemas and trajectories. Production at huwo.xyz adds accounts, groups, RTC, persistent marketplace, and hardware linkage.

**Can I fork for commercial use?**  
MIT allows fork and modification. Trademarks “呼我” / “HUWO” and closed services are out of scope.
