# HUWO — Open Source Demo (MIT)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-HUWOAI%2Fhuwo-181717?logo=github)](https://github.com/HUWOAI/huwo)
[![中文](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87-red)](./README.md)

> **HUWO AI · Family Super-Agent** — open-source Agent kernel  
> Tagline: **You call — we answer** (您有所呼，我有所应)  
> Team: **Quzhou HUWO Network Technology Co., Ltd.**（衢州呼我网络科技有限公司）  
> Hangzhou R&D center: **Hangzhou Huirong Technology Co., Ltd.**（杭州汇融科技有限公司）  
> Live product: https://www.huwo.xyz/AIEAT/  
> Contest track: GOAI Boundless Agents · **AI + Smart Glasses** · Trusted home-care hiring Agent

**中文文档:** [README.md](./README.md)

This repository is a **runnable, demoable, reproducible** golden-path demo covering meal planning, light care reminders, and the home-care hiring loop:

**Assess → Publish → Match → See (glasses POV) → Close (ACL revoke)**

including **≥3 match reasons**, on-duty event frames, and **off-duty employer feed denial**.

---

## Why this repo?

Judges and developers can verify **without an LLM API key**:

1. Agent **tool-call trajectories** (not chat-wrapper theater)  
2. Housekeeping path with **explainable match schema** and **ACL revoke after shift end**  
3. Commercial APIs are swappable; production secrets and full question banks stay private  

Full App / accounts / glasses firmware live on the production site. Boundary: [OPEN_BOUNDARY.en.md](./OPEN_BOUNDARY.en.md).

---

## 30-second quickstart (no LLM key)

```bash
git clone https://github.com/HUWOAI/huwo.git
cd huwo
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_demo.py golden
python scripts/run_demo.py care
python scripts/run_demo.py housekeeping
python scripts/test_open_smoke.py
```

| Command | Closed loop |
|---------|-------------|
| `golden` | Mild dinner constraints → shopping list → grocery deeplink sketch → nearby → Xiaohu `robot_notify` |
| `care` | Med reminder create/list (task assistant; **not** prescribing) |
| `housekeeping` | **Assess** fair interview → **Publish** listing → **Match** ≥3 reasons → **See** glasses event frames → **Close** ACL (`employer_feed_access=denied`) |

Web demo:

```bash
python -m uvicorn demo.app:app --host 127.0.0.1 --port 8765
```

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8765/docs | Swagger |
| http://127.0.0.1:8765/demo/golden-path | Meal golden path |
| http://127.0.0.1:8765/demo/care-path | Care path |
| http://127.0.0.1:8765/demo/housekeeping-path | Hiring + ACL path |
| http://127.0.0.1:8765/meta/tools | Tool schema |
| http://127.0.0.1:8765/demo/metrics | Self-check summary |

---

## Live product (full stack)

| Item | Detail |
|------|--------|
| H5 | https://www.huwo.xyz/AIEAT/ |
| Website | https://www.huwo.xyz/ |
| Login | **SMS code** or **phone + password**; **invite code optional** on signup |
| Test account | `13800000001` / password `Ok778899` (optional invite `100001`) |
| Voice call persona | **HUWO AI Assistant** (assess / hire / tasks) |
| Glasses | Shortcuts: weaning check / grocery note / care moment → on-duty timeline; **End shift** → ACL receipt |
| Judge mode | Settings → Judge mode ON → always-expanded Agent traces on home |

Narrative: national-standard assessment → media résumé → explainable match → glasses first-person events → **revoke employer media access on off-duty**.

---

## Open vs closed (one line)

| Open (MIT) | Closed |
|------------|--------|
| Agent skills, tool schema, prompts | Production `.env`, payment certs |
| Match-reason fields, on/off-duty ACL sketch | Private user data, full scoring keys |
| Xiaohu robot adapter, no-key demos | Mass-production firmware, full commercial backend |

See [OPEN_BOUNDARY.en.md](./OPEN_BOUNDARY.en.md).

---

## Docs

| English | Chinese | Topic |
|---------|---------|-------|
| [docs/DEMO_SCRIPT.en.md](./docs/DEMO_SCRIPT.en.md) | [docs/DEMO_SCRIPT.md](./docs/DEMO_SCRIPT.md) | 3-min demo script |
| [docs/COMPLIANCE.en.md](./docs/COMPLIANCE.en.md) | [docs/COMPLIANCE.md](./docs/COMPLIANCE.md) | Compliance notes |
| [docs/DEPLOY.en.md](./docs/DEPLOY.en.md) | [docs/DEPLOY.md](./docs/DEPLOY.md) | Deploy |
| — | [docs/METRICS.md](./docs/METRICS.md) | Metrics |
| — | [docs/THIRD_PARTY.md](./docs/THIRD_PARTY.md) | Third-party APIs |

---

## Optional LLM (`/demo/chat`)

```bash
cp .env.example .env
```

| Variable | Meaning |
|----------|---------|
| `VOLC_ARK_API_KEY` | Volcano Ark API key |
| `VOLC_ARK_MODEL` | Endpoint / model id |
| `MINIMAX_API_KEY` | MiniMax example |
| `LLM_PROVIDER` | `volc` or `minimax` |

**No key required** for `golden` / `care` / `housekeeping`. Without a key, `/demo/chat` falls back to a rule-based router.

---

## Layout

```
├── LICENSE
├── README.md / README.en.md
├── OPEN_BOUNDARY.md / OPEN_BOUNDARY.en.md
├── huwo_open/agent|providers|integrations|robot
├── demo/
├── docs/
└── scripts/run_demo.py · test_open_smoke.py
```

---

## Trademark & contact

“呼我” / “HUWO” trademarks are **not** licensed under MIT.  
Website: https://www.huwo.xyz · Collaboration: [Issues](https://github.com/HUWOAI/huwo/issues).
