# Report - group "fortworth" (fort-worth, denton, plano) - 2026-10-11

## Session constraints (read first)
- WebFetch and curl could not reach any target site this session: every host (fortworthtexas.gov, codelibrary.amlegal.com, nctcog.org, plano.gov, cityofdenton.com, municode, census.gov, iccsafe.org, capitol.texas.gov) returned ENOTFOUND or a proxy 403 (organization egress policy).
- The only working research channel was WebSearch, and the shared per-turn search budget (200 calls) ran out after 11 Fort Worth searches. Denton and Plano got **no** searches.
- Fort Worth values seen only in search extracts of the primary ordinance/city pages are marked **Secondary**, with the note "Read via web-search extract". No value is marked Sourced.
- Denton and Plano values are **Assumed**, with url "", and come from agent knowledge flagged "unverified". Both files are valid placeholders. They should be re-researched in a session with web access and a search budget.
- NCTCOG regional amendments could not be read or cited (nctcog.org blocked, no search budget left).

## fort-worth - mostly complete (Secondary)
- IRC: 2021 IRC by Ord. 25383-03-2022 (City Code §§ 7-61 to 7-64), effective 2022-04-01. Energy is still the **2015 IECC**: the city kept it when it adopted the 2021 codes. Plumbing: 2021 IPC/IFGC. Electrical: the city page says 2026 NEC effective 2026-09-01 (2023 NEC by Ord. 26721-02-2024 before that). Re-verify the 2026 NEC.
- Foundation: amended R401.2 requires every new foundation to be sealed by a Texas PE (UpCodes compilation). The Administrative Code (Ord. 25387) requires engineered plans or a geotech report showing non-expansive soil.
- A-5 (§ 4.705): 5,000 sq ft lot, 50 ft width, front 20 ft (15 ft on a limited local street), side 5, side street 10 (extract was garbled), rear 5, height 35 ft, coverage 50%. Attached garage side yard 3 ft if at least 18 ft behind the front wall. Detached rear garage 3 ft.
- Impact fees: water+wastewater $5,828 for a 5/8 in meter (permits from 2026-10-01; Ord. 27745-06-2025). Transportation = vehicle-miles x Schedule 1 rate (A $1,642 / B $3,308 / C $1,781 per vehicle-mile) x 65% collection (from 2026-06-01). The per-house dollar amount was not computed because vehicle-miles per single-family unit was not retrieved.
- Not found: permit/plan-review fee formula (so the worked example is null), tap fees, lot depth, flood freeboard, frost depth, parking count, ADU rules, Urban Forestry applicability, market $/sq ft.
- 2nd check: IRC edition was confirmed by three separate search extracts (ordinance PDF, § 7-61 amlegal, city codes page), and no 2024 IRC adoption was found. The A-5 front/side/rear setbacks were confirmed by two separate searches of § 4.705 and match the A-7.5 table and BOA dockets. PropertyZoned's 25/6/5 figures were rejected. Water/wastewater fee amounts were seen once (city page extract plus utilitycostguide agreement).

## denton - placeholder (Assumed only)
- Not found: everything Denton-specific (IRC edition, DDC district table, fees, trees, flood). The engine is set to ask for the zoning district, climate zone 3A, a provisional engineered-foundation flag, and no city masonry rule (HB 2439).
- 2nd check: none possible.

## plano - placeholder (Assumed only)
- SF-7 was chosen per SPEC. 7,000 sq ft lot / 60 ft width / 100 ft depth / front 25 / side 5 come from agent memory, are marked unverified, and the engine change is marked "should/provisional". Rear, height and coverage are null.
- Masonry: Plano historically had high masonry requirements. HB 2439 (2019, Gov't Code ch. 3000) blocks city material mandates outside exemptions. HOAs commonly still require masonry, so the engine prompts for deed restrictions.
- 2nd check: none possible.

## Cross-city notes
- HB 2439 effect is recorded as Assumed (statute not fetched).
- SB 15 (2025) allows 3,000 sq ft lots in new subdivisions in large cities (Fort Worth Report). This was recorded for Fort Worth and also likely applies to Plano.
- New ruleType added: `other-drainage-to-storm` (Fort Worth amended R401.3).
