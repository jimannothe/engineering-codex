# Job Score Comparison

Comparison of the current scorer against the previous committed scorer for all top-level job HTML files in `projects/jobs`.

| Job | Old | New | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| (1) Empleos de solicitud sencilla de LinkedIn _ LinkedIn.html | 56 | 56 | +0 | Unknown (1) Empleos de solicitud sencilla de LinkedIn; missing: JavaScript, Java, SQL, APIs |
| BackendEngineerWallets_Tether.io_LinkedIn.html | 53 | 53 | +0 | Tether.io Backend Engineer - Wallets; missing: JavaScript, Java, SQL, Agile |
| Integration_Engineer_Access_Information_Management_LinkedIn.html | 92 | 60 | -32 | Access Integration Engineer; missing: JavaScript, SQL, APIs, Security / auth |
| OffensiveSecurityPenetrationTester_KornFerry_LinkedIn.html | 69 | 61 | -8 | Korn Ferry Offensive Security Penetration Tester; missing: JavaScript, Java, SQL, APIs |
| ProductQualityEngineer_TalentScout_LinkedIn.html | 79 | 79 | +0 | Talent Scout Product Quality Engineer; missing: APIs, SaaS, Manual testing, Security / auth |
| Python_Software_Engineer_3Pilla _LinkedIn.html | 69 | 61 | -8 | 3Pillar Python Software Engineer; missing: JavaScript, SQL, APIs, Agile |
| Software_ElectronicsEngineer_Teradyne_LinkedIn.html | 69 | 69 | +0 | Teradyne Software/Electronics Engineer; missing: C++ |
| Technical_Support_Engineer_Armis_LinkedIn.html | 66 | 54 | -12 | Armis Technical Support Engineer; missing: SQL, APIs, Networking, Troubleshooting |
| VerificaValidationEngineer_MatthewsMarkingSystems_LinkedIn.html | 92 | 92 | +0 | Matthews Marking Systems Verification &amp; Validation Engineer; missing: APIs, Manual testing, Project management |

## What Changed

- The new scorer is stricter about named tools and platforms.
- Generic matches like `integration`, `validation`, and `automation` no longer inflate scores as much.
- Roles with real stack overlap still score high, but the model now penalizes missing platform-specific evidence.

## Observations

- The biggest drop was the Access Integration Engineer role because it depends on Boomi, NetSuite, Salesforce, and ADP rather than broad integration keywords.
- Armis also dropped because the older model rewarded generic support overlap more heavily than the new one.
- Matthews stayed high because the validation and system-level overlap is genuine and the named-stack gap is smaller.
- The QA and software roles remain in the middle because they have partial overlap but still need more direct tooling evidence.
