# Compliance Notes (Open Repo)

中文: [COMPLIANCE.md](./COMPLIANCE.md)

## Product boundaries

| Capability | Allowed | Forbidden |
|------------|---------|-----------|
| Meal advice | Menus / food intel under preference & allergy constraints | Medical diagnosis or prescriptions |
| Med reminders | Schedule reminders (task assistant) | AI prescribing / changing meds / clinical conclusions |
| Home-care assess / match | Transparent rule scores, ≥3 match reasons, listing sketches | Fake background checks, discriminatory ranking, guaranteeing jobs |
| Glasses / on-duty media | Authorized **event-based** logs; ACL revoke after off-duty | Unauthorized recording; claiming 24/7 monitoring |
| Insurance | “Consider insurance” placeholder (commercial) | Guaranteed underwriting / payout claims |

## Data

- Open demo uses sample JSON only — no real user PII.  
- API keys are not committed; `.env.example` placeholders only.

## Third parties

See [THIRD_PARTY.md](./THIRD_PARTY.md).
