# 3-Minute Demo Script (Open Kernel)

> Team: **Callme Group LLC / HUWO**  
> Product: HUWO AI · Family Super-Agent  
> Track: GOAI **AI + Smart Glasses** · trusted home-care hiring Agent  
> 中文: [DEMO_SCRIPT.md](./DEMO_SCRIPT.md)

---

## 0:00–0:20 Opening

“We are HUWO. Tagline: you call — we answer. This open repo shows verifiable Agent loops—meals, light care, and home-care **Assess → Publish → Match → See → Close**—not chat wrappers.”

---

## 0:20–0:55 Meal golden path

```bash
python scripts/run_demo.py golden
```

Or: `http://127.0.0.1:8765/demo/golden-path`

Say: “Trajectory includes meal plan → shopping list → grocery deeplink sketch → nearby → Xiaohu `robot_notify`. Works without an LLM key.”

---

## 0:55–1:50 Housekeeping Assess→…→Close (main story)

```bash
python scripts/run_demo.py housekeeping
```

Or: `http://127.0.0.1:8765/demo/housekeeping-path`

Talking points:

1. **Assess**: `fair_interview_score` — transparent rules  
2. **Publish**: `publish_service_profile`  
3. **Match**: `recommend_service_workers` with **≥3** `match_reasons`  
4. **See**: `post_on_duty_moment` — weaning / grocery / care frames  
5. **Close**: `end_care_shift` → `acl_receipt.employer_feed_access = denied`; `list_on_duty_moments` returns empty  

Optional: `python scripts/run_demo.py care` (med reminder; assistant boundary only).

---

## 1:50–2:30 Live product (online)

Open https://www.huwo.xyz/AIEAT/

- Voice call persona: **HUWO AI Assistant**  
- Market card with 3 match reasons  
- Glasses shortcuts or “judge inject one frame”  
- Moments → **End shift** → hold ACL receipt 2 seconds  
- Settings → **Judge mode** → expanded tool traces  

---

## 2:30–2:50 Boundary + compliance

“MIT covers skills / schema / prompts / ACL sketch. Accounts, social, production secrets, firmware stay closed. Nutrition/meds are not medical advice; we do not claim 24/7 monitoring.”

---

## 2:50–3:00 Close

“You call — we answer. Repo https://github.com/HUWOAI/huwo — live and demoable.”
