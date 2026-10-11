# Report - group "east" (little-elm, forney, waco, tyler, beaumont)

Read date: 2026-10-11. All 5 files validate (`_work/validate.py` OK).

## Tooling problems this run (read first)
- WebFetch failed on every host (DNS `getaddrinfo ENOTFOUND`, including census.gov, municode, amlegal, littleelm.gov). Bash curl is blocked by the egress proxy.
- The shared WebSearch budget (200 per turn, across all agents) ran out after 13 searches in this group, partway through Little Elm.
- So no primary page was opened directly. Values taken from search-engine excerpts of primary pages are marked **Secondary**, with the note "Read via search-engine excerpt". Nothing is marked Sourced. Values with no search evidence are **Assumed**, with url "" and a reason.
- New ruleType added: `irc-edition`, used where the base IRC edition differs from or confirms the 2021 model.

## little-elm - mostly complete (Secondary)
- IRC: **2024 IRC**, from Municode Ch. 22 Sec. 22-19 (2026 supplement, AWC span amendments, some appendices excluded). 2nd check: the Town's 2020 residential packet lists the 2018 IRC, so it is older, and the Town Fire Code web page still says 2018 IFC. The two excerpts that mentioned Municode both said 2024, so I used 2024. The adopting ordinance number was not found.
- District: SF-4 (lots of at least 6,000 sq ft). Setbacks 25 front / 6 side / 20 rear, height 35 ft / 3 stories. These come from a PropZone (Gridics) parcel table, not the ordinance. The street-side setback of 15 ft is Assumed. 2nd check: I found no second source for the setbacks; only the 6,000 sq ft purpose statement appeared in two excerpts. Most new subdivisions are PDs, so the engine asks about a PD.
- Fees: $0.85 per gross sq ft (includes MEP) plus $295 plan review, from the 2019 fee chart, the latest one found. Worked example: 2,840 sq ft x $0.85 = $2,414 (+$295). Impact fees under Ord. 1431 (Dec 2017), from zonefee.com: water $1,519, wastewater $2,930, roadway $3,498 (SA1) or $1,684 (SA2).
- Not found: Census V2024 population, lot width/depth, minimum dwelling size, freeboard, tap fees, review days, tree rules, energy edition (2024 IECC likely).

## forney / waco / beaumont - skeleton only (Assumed)
- No search budget was left. The IRC edition is null. Setbacks, district, lot size and height are typical regional defaults, flagged `assumed` and `requireUserConfirm` in engineChanges. Fees are not found.
- State-level items are cited (Secondary, from search excerpts): the energy floor of 2015 IRC Ch. 11 (HSC 388.003, SECO), and the Gov't Code 3000.002 masonry preemption.
- Beaumont: the TDI windstorm package, flood elevation and sealed wind design are must/should engine changes, but the wind zone and speed (130-150 mph range) and the freeboard (1 ft) are Assumed.

## tyler - partial
- IRC: **2021 IRC as amended in Sec. 6-151**, from an American Legal code excerpt (Secondary). The content of the amendments was not read. Everything else is Assumed, as for the other three.

## 2nd-check summary
- Re-checked: Little Elm IRC edition (Municode excerpt vs. the 2020 packet and Fire Code page; conflict resolved toward the newer Municode text), Little Elm fee rate (fee chart excerpt plus zonefee.com agree on $0.85 per sq ft), Little Elm SF-4 minimum lot (2 excerpts).
- Not re-checked: all setbacks, and every value for Forney, Waco, Tyler (except the IRC edition) and Beaumont.

## Recommended follow-up
Re-run this group once fetch and search work again. Priorities: the Forney, Waco and Beaumont IRC adoption and zoning tables; the Beaumont TDI zone and freeboard; the Tyler Sec. 6-151 content; current fee schedules; Census Vintage 2024 populations.

## Wave 3 (Secondary) - forney, beaumont
- forney: 2021 IRC + local/NCTCOG amendments, 2021 IECC/IPC, NEC 2020, eff. 2023-01-01. Engineer-stamped structural plans + foundation letter for every new home (FAQ). PD preferred; SF-6 7,700 sf (weak). Pop 35,470 (V2023).
- beaumont: TDI Inland II, 110 mph (old basis) ~ 143 mph ultimate; city requires TX-registered engineer windstorm certification for buildings >= 120 sf. 2021 IRC/IECC/IFC, NEC 2020, ICC 600-2020. Permit $0.50/sf + $150 + $10 -> $1,580 (garage incl.). No impact fees found. Floodplain Art. 24.05 (freeboard not found). R-S (28.03.002). Pop 112,193 (V2023).
- LGC 214.907 (HB 852, 2019) bars residential permit fees based on home value.
