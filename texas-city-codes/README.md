# Texas city building codes, zoning and cost: data package for Keystone AI

Research for Keystone AI's Texas US-parity work (plan `2026-10-11-us-parity-advanced-features-plan.md`, part B). When a user picks a Texas city, the engine should apply that city's adopted code, zoning limits and cost level. This folder holds what each city adopts, what it means for a house design, and what the engine must change.

**Research date:** all sources read 2026-10-11, in one session.
**Coverage:** all 20 tier-1 cities and all 23 tier-2 places, including Cypress (unincorporated Harris County). Also two fallback profiles: "Texas city, not listed" and "Unincorporated Texas county". That makes 45 JSON files.

> **Read this first: how reliable the data is.**
> The research environment could not open web pages directly; every page fetch failed (DNS errors or proxy 403s, including on Municode, American Legal, eCode360, city sites, capitol.texas.gov, TDI and BLS). The only working channel was web search, which returns extracts of pages. So:
> - Almost nothing is marked **Sourced** (2 values, both Census populations). A value read from a search extract of a primary document (city code, ordinance, fee schedule, statute) is marked **Secondary**, and its `note` says so. Everything else is **Assumed**, with the reason in `note`.
> - About 40-60% of each tier-1 file is researched (Sourced or Secondary). Tier-2 files are 27-58% researched, and Cypress is 13%. The table [Completeness by city](#completeness-by-city) has the figure for each city.
> - Nothing was invented. Unknown values are `null` with a "Not found" note. Where sources conflict, the note says which one was chosen and why.
> - **Before the engine relies on a value, it should check `status`.** Treat `Assumed` values as defaults the user must confirm. The engine changes already carry this (for example `survey-input-district` and "confirm with city" warnings).
> - A follow-up session with page access (Municode or AmLegal tables and fee-schedule PDFs) can turn most Secondary values into Sourced ones without changing the structure.

## Contents

| File | What it is |
|---|---|
| `cities/<city-id>.json` | One file per city or profile, in the shape from the brief. Each leaf is `{value, unit?, status, source:{id,title,section?,url,read}, note?}`. Extra keys: `tier`, `comparison` (one-line values for the table below), `notFound`, and `params` on each engine change (machine-readable values). |
| `cities/texas-baseline.json` | Fallback for a Texas city that is not listed: state floor plus the most common amendments. |
| `cities/texas-unincorporated.json` | Fallback for land outside city limits. |
| `texas-state-background.md` | The section 3 Texas background items, each checked and marked [Secondary] or [Unverified]. |
| `engine-change-catalogue.md` | All engine changes, de-duplicated into 42 rule types. For each: the survey input it needs, the cities that use it, and a data sketch. |
| `sources.csv` | Every source used: id, title, url, publisher, date_read, city_ids. |
| `_work/` | Working files: the research spec, the validator (`validate.py`), the build scripts, per-group research reports (`report-*.md`, including what was checked twice) and the cost-factor data (`cost-factors.json`). |

## Method

1. **Primary sources first.** Agents searched each city's code of ordinances (Municode, AmLegal, eCode360), its building-code adoption page or ordinance, its zoning or unified development code, and its fee schedule. When none appeared, they used city summary pages, permit guides, council agendas, Board of Adjustment dockets and trade sources (marked Secondary). Third-party zoning aggregators (PropertyZoned, Zoneomics, Building Club) were used only when nothing better turned up; the note says so, and those values are flagged as low confidence.
2. **Copyright.** ICC text is recorded only as section numbers and short values. No RSMeans or other paid cost data was used.
3. **Typical district.** The most common single-family district for new detached homes was chosen (for example Dallas R-7.5(A), Austin SF-3, Fort Worth A-5, San Antonio R-6). In fast-growing suburbs most new homes are in Planned Developments (PDs/PUDs) with their own standards. There the base district is given and the engine is told to ask the user (`survey-input-district`).
4. **Worked fee example.** The house is 2,400 sq ft conditioned, two storeys, with an assumed 440 sq ft attached garage (2,840 sq ft under roof). Texas bars residential permit fees based on the home's value (Local Government Code §214.907, from HB 852 of 2019; Secondary), so most cities charge per square foot. Each file's `note` shows the arithmetic.
5. **Checks.** Every file passes `_work/validate.py` (required fields, leaf shape, status values, URL present on non-Assumed values). Each research group re-checked the IRC edition and typical-district setbacks against a second source where it could (listed in `_work/report-*.md`). The coordinator spot-checked 5 tier-1 cities again (below).
6. **Rounds.** The research was done in 4 rounds because the shared web-search budget ran out in round 1. Rounds 2-4 replaced round-1 placeholders city by city, tier 1 first.

### Cost factor method

- **Baseline:** US national = 1.00. Keystone's current single Texas multiplier is 0.95.
- **Labour index L:** the weighted mean of (metro annual median wage ÷ US annual median wage), using BLS OEWS May 2024 data read from O*NET OnLine's Texas local-wages pages (Secondary). Weights:
  - carpenters 47-2031: 0.30
  - electricians 47-2111: 0.20
  - plumbers 47-2152: 0.20
  - construction laborers 47-2061: 0.20
  - HVAC mechanics 49-9021: 0.10

  Where a trade is missing (HVAC in Killeen-Temple, Waco, Tyler and College Station-Bryan), the remaining weights are renormalised.
- **Factor:** 0.40 × L + 0.60 × M, where 0.40 is the labour share. The materials index M = 1.00 for every Texas metro, because no public, citable metro materials index was found. The materials notes (brick from Texas plants; freight to the Panhandle, the Valley and West Texas; coastal hardware) are qualitative and marked Assumed.
- US medians used: carpenters $59,310; electricians $62,350; plumbers $62,970; laborers $46,730; HVAC $59,810.

| Metro (BLS code) | Trades found | Labour index L | Cost factor |
|---|---|---|---|
| Beaumont-Port Arthur, TX (13140) | 5/5 | 0.915 | 0.97 |
| Houston-Pasadena-The Woodlands, TX (26420) | 5/5 | 0.89 | 0.96 |
| Austin-Round Rock-San Marcos, TX (12420) | 5/5 | 0.905 | 0.96 |
| Dallas-Fort Worth-Arlington, TX (19100) | 5/5 | 0.885 | 0.95 |
| Midland, TX (33260) | 5/5 | 0.881 | 0.95 |
| San Antonio-New Braunfels, TX (41700) | 5/5 | 0.847 | 0.94 |
| Corpus Christi, TX (18580) | 5/5 | 0.849 | 0.94 |
| Amarillo, TX (11100) | 5/5 | 0.79 | 0.92 |
| Killeen-Temple, TX (28660) | 4/5 | 0.798 | 0.92 |
| Waco, TX (47380) | 4/5 | 0.805 | 0.92 |
| Tyler, TX (46340) | 4/5 | 0.789 | 0.92 |
| College Station-Bryan, TX (17780) | 4/5 | 0.789 | 0.92 |
| Lubbock, TX (31180) | 5/5 | 0.746 | 0.9 |
| El Paso, TX (21340) | 5/5 | 0.731 | 0.89 |
| Laredo, TX (29700) | 5/5 | 0.736 | 0.89 |
| Brownsville-Harlingen, TX (15180) | 5/5 | 0.69 | 0.88 |
| McAllen-Edinburg-Mission, TX (32580) | 5/5 | 0.704 | 0.88 |
| Dallas-Plano-Irving, TX Metropolitan Division (19124) | 0/5 | – | use 19100 (0.95) |
| Fort Worth-Arlington-Grapevine, TX Metropolitan Division (23104) | 0/5 | – | use 19100 (0.95) |
| **Texas statewide** | 5/5 | 0.866 | **0.95** |

Market cost figures (market figures, not quotes):
- NAHB *Cost of Constructing a Home 2024*: about $162/sq ft national construction cost (64.4% of sales price, 2,647 sq ft average).
- Census, South region: $146.64/sq ft median sales price (2023 sales).
- NAHB, West South Central: $138/sq ft for custom homes started in 2024, excluding land.

No public Texas metro cost per square foot was found. All three figures are Secondary.

## Texas background (summary of `texas-state-background.md`)

- **IRC floor.** Local Government Code §214.212 makes the IRC "as it existed on May 1, 2012" the state minimum for city residential codes (HB 738, effective 2022-01-01). Cities may adopt newer editions and amend them, after a public hearing and by ordinance. In practice:
  - **2024 IRC:** Austin, San Antonio, Frisco, Plano, McKinney, Irving, Killeen, Round Rock, Sugar Land, Hutto, Celina, Little Elm, Waco and College Station.
  - **2021 IRC:** most other cities.
  - **2015 IRC:** Garland.
  - **2018 IRC:** Midland and McAllen (McAllen inferred).
- **Energy.** The statewide code is still the 2015 IRC chapter 11 (Health & Safety Code §388.003). SECO never adopted the 2021 edition. SB 783 (2025) cleared the way, and SECO took comments on the 2024 IRC/IECC in October 2025. No final adoption was found, and any new edition takes effect at least 9 months after adoption. Cities adopt newer editions themselves: Fort Worth kept the 2015 IECC, Waco uses 2018, and Austin uses 2024.
- **Climate zones.** Under the 2015 map, the Houston, Austin and San Antonio areas, Central Texas, the coast and the Valley are 2A; Laredo is 2B; DFW and Tyler are 3A; El Paso, Lubbock and Midland are 3B; and Amarillo is 4B. The **2021 map moves Dallas County (and probably Tarrant) to 2A**, while Collin, Denton and Rockwall stay 3A. The envelope table therefore depends on both the county and the energy-code edition in force. Cameron and Hidalgo moving to 1A is unconfirmed (sources conflict).
- **Unincorporated land.** Counties have no zoning and no building permit for houses. In counties that opted in (Galveston and Collin did in 2009), LGC §233.153 requires the IRC as of 2008 or the county seat's edition, with 3 inspections by a builder-chosen inspector. The county fire code (§233.062) does not cover one- and two-family homes. What still applies: floodplain permits (Harris County: higher of 24 in above the 500-year flood level or 12 in above the street crown), septic/OSSF rules, plat building lines, MUD fees and deed restrictions.
- **Windstorm.** TDI certification (WPI-8) is required in the 14 first-tier coastal counties: Aransas, Brazoria, Calhoun, Cameron, Chambers, Galveston, Jefferson, Kenedy, Kleberg, Matagorda, Nueces, Refugio, San Patricio and Willacy. In Harris County it covers only La Porte, Morgan's Point, Pasadena, Seabrook, Shoreacres and the area east of SH 146. **TDI uses the 2024 IRC/IBC for windstorm from 2026-04-01** (28 TAC §5.4013). Project cities in the windstorm area:
  - Corpus Christi
  - Brownsville
  - League City (Galveston County part)
  - Pearland (Brazoria County part only)
  - Beaumont
- **Sprinklers.** LGC §250.011 bars cities from requiring sprinklers in one- and two-family homes. Rules adopted before 2009 are exempt, which is why Frisco (6,000 sq ft and up) and Plano (R325) still have them.
- **Masonry.** Gov't Code ch. 3000 (HB 2439, 2019) bars cities from prohibiting or limiting building products approved by a national model code. So a city "80% masonry" rule is generally unenforceable outside historic districts. Brick requirements now come from HOAs, deed restrictions and some PDs. The engine should ask the user, not apply a city percentage.
- **Plumbing and electrical.** Texas allows the IPC or the UPC (Occupations Code §1301.255). Houston and Austin use the UPC; most others use the IPC. **The statewide electrical code is NEC 2026 from 2026-09-01** (16 TAC §73.100), so city NEC 2020 and 2023 adoptions are being superseded.
- **Small lots, SB 15 (2025).** In cities over 150,000 people in counties over 300,000, on new subdivisions of 5 or more acres, the city may not require more than a 3,000 sq ft lot, 30 ft width, 75 ft depth, or setbacks over 15 ft front, 5 ft side and 10 ft rear. It also may not require covered parking or more than one space. This applies to applications from 2025-09-01.
- **Expansive clay.** Most of Texas east of the Balcones and DFW sits on expansive clay. Many cities require a Texas PE to design and seal the foundation (usually a post-tensioned slab), for example Dallas, Fort Worth, Frisco, San Antonio, Houston, Corpus Christi, New Braunfels, Forney and McKinney.

## Comparison table (all cities against the IRC-2021 model)

The "IRC-2021 model" row is what Keystone does today. Values are short forms; the JSON has sources and statuses. "?" or "assumed" in a cell means the value was not confirmed.

| City | Tier | IRC edition | Energy code | Plumbing | Typical district | Front/side/rear (ft) | Max height | Coverage / FAR | Masonry rule | Engineer-sealed foundation | Windstorm | Flood note | Permit fee, 2,400 sf example | Impact fees | Cost factor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **IRC-2021 model (Keystone today)** | – | 2021 IRC | 2021 IRC ch. 11 (IECC) | IPC | – | user value | 3 storeys (IRC scope) | – | none | no | no | none | – | none | 0.95 (single TX) |
| [Texas city, not listed](cities/texas-baseline.json) | fallback | 2021 IRC typical (state floor 2012) | 2015 IRC ch.11 (state) | IPC (or UPC) | n/a | user input | 35 ft placeholder | n/a | not enforceable by city (Gov't Code 3000.002) - HOA/historic only | yes - recommended statewide | 14 coastal counties + E. Harris (TDI 2024 IRC from 2026-04-01) | BFE + 1 ft default | n/a | city-specific | 0.95 |
| [Unincorporated Texas county](cities/texas-unincorporated.json) | fallback | none (LGC 233.153: 2008 IRC or county-seat IRC where county opted in) | 2015 IRC ch.11 (uninspected) | licensed plumber, no county code | none | plat/deed | none | none | deed restrictions only | recommended | by county | county permit, BFE+1-2 ft | no building permit | none (MUD fees) | 0.95 |
| [City of Amarillo](cities/amarillo.json) | 1 | 2021 IRC (amended) | 2015 IECC? (unconfirmed) | 2021 (IPC assumed) | R-2 (assumed) | 25/5/? (secondary) | 35 ft | not found | none | not found; 24 in footings | no | not found | $1,278 (2019 $0.45/sf) | none found | 0.92 |
| [City of Arlington](cities/arlington.json) | 1 | 2021 IRC (Arlington amended) | 2021 IECC (amended) | IPC 2021 | RS-7.2 | 20/5/20 (40 ft arterial front; 15 street side) | 40 ft | 50% / no FAR | none (Gov't Code 3000) | likely (regional practice) | no | 2 ft above fully urbanized BFE | ~$2,074 (assumed tier) | $1,246 water+sewer + roadway | 0.95 |
| [City of Austin](cities/austin.json) | 1 | 2024 IRC (amended) | 2024 IECC (Austin amended) | UPC (edition unverified) | SF-3 | 25/5/10 (15 street side) | 35 ft (32 ft in McMansion area) | 40% bldg / 45% IC / FAR 0.4 or 2,300 sf (McMansion area) | none | unverified | no | 2 ft above Atlas-14 100-yr (old 500-yr) | incomplete (plan review ~$1,209+) | $7,700 water+ww | 0.96 |
| [City of Brownsville](cities/brownsville.json) | 1 | not found (TDI: 2024 IRC for windstorm) | not verified | not verified | R-1 | 25/5/5 (20 corner) | 35 ft | 50% / none | none (ch. 3000) | likely (assumed) | yes - TDI Inland I legacy, 150 mph 2024 IRC | +1 ft assumed | ~$2,800 (rough) | CRF ~$850-1,050 + BPUB | 0.88 |
| [City of Corpus Christi](cities/corpus-christi.json) | 1 | 2021 IRC (amended) | 2021 IECC? (pages conflict w/ 2015) | IPC 2021 | RS-6 | 25/5/20 (3rd-party) | 35 ft | not found | none (ch. 3000) | yes - PE-sealed, all new homes | yes - TDI, 2024 IRC 150 mph, WPI-8 | AE BFE+1 ft; VE LHSM BFE+1 ft | $1,724 | not found | 0.94 |
| [City of Dallas](cities/dallas.json) | 1 | 2021 IRC (Dallas Ch. 57, amended 2025) | 2021 IECC (Dallas Ch. 59) | IPC 2021 | R-7.5(A) | 25/5/5 | 30 ft | 45% / no FAR | none (Gov't Code 3000) | yes - PE-sealed, all new homes | no | 3 ft above design flood | ~$985 | $0 | 0.95 |
| [City of Denton](cities/denton.json) | 1 | 2021 IRC (Secondary) | 2021 IECC (Secondary) | IPC 2021 (assumed) | R4 (provisional; enter district) | not found (R1 front 20) | not found (R1 40 ft) | not found | none by city; HOA | likely (unverified) | no | 18 in above fully-developed 100-yr WSEL (2.5 ft above FIS) | $2,669 (0.89/sf x 2,840 + $141) | water+ww by meter (amount not found) | 0.95 |
| [City of El Paso](cities/el-paso.json) | 1 | 2021 IRC (secondary) | 2021 IRC Ch.11 (assumed) | not found | R-3 | 20/5/20 (front+rear>=50) | 35 ft | 50% / no FAR | none | no local mandate found | no | not found | ~$2,258 (assumed tier) | $1,880-2,070 w+ww (growth areas) | 0.89 |
| [City of Fort Worth](cities/fort-worth.json) | 1 | 2021 IRC (amended) | 2015 IECC (amended) | IPC 2021 | A-5 | 20/5/5 (street side 10) | 35 ft | 50% / no FAR | none (HB 2439) | yes - all new homes (PE sealed) | no | unverified (>=1 ft assumed) | not found | $5,828 water+ww + transportation (by area) | 0.95 |
| [City of Frisco](cities/frisco.json) | 1 | 2024 IRC (amended, eff. 2026-03-01) | 2024 IECC (amended) | IPC 2024 | SF-7 (most new = PD) | 25/5/20 (side/rear assumed) | 40 ft/2.5 st | 45% assumed / no FAR | not city-enforceable (HB 2439); PD/HOA usually 80-100% | yes - PE sealed, all new homes | no | not verified | not found | roadway+water+ww (amount not found) | 0.95 |
| [City of Garland](cities/garland.json) | 1 | 2015 IRC (Garland amended) | 2015 IECC | IPC 2015 | SF-7 | 25/5/? (provisional; corner 15) | 35 ft (assumed) | unconfirmed / no FAR | none (Gov't Code 3000) | likely; PT slab engineer letter | no | 2 ft above BFE | ~$1,560 | $593 water + $3,034 roadway (post-2017 plats) | 0.95 |
| [City of Houston](cities/houston.json) | 1 | 2021 IRC + Houston amendments | 2021 IECC (amended; solar-ready mandatory) | UPC 2021 | none (Ch. 42) | 20 front (10 + 19-20 garage optional)/0/0 | none (IRC 3 st) | none | none (deed restr. may) | yes - PE seal | no | 500-yr + 2 ft | not computed (tiers unread) | $4,383/SU water+ww + drainage $25.56/1000sf | 0.96 |
| [City of Irving](cities/irving.json) | 1 | 2024 IRC (Irving amended, eff. 5-1-2026) | 2024 IECC (amended) | IPC 2024 | R-7.5 | 25/5/20 (provisional) | unconfirmed (25-30 ft) | unconfirmed / no FAR | none (Gov't Code 3000) | likely (not confirmed) | no | 2 ft (provisional) | ~$1,477 | $2,693 water+ww (+ roadway) | 0.95 |
| [City of Killeen](cities/killeen.json) | 1 | 2024 IRC (eff. 2026-01-01) | 2024 IECC (amended) | IPC 2024 | R-1 | 25/5/25 (street side 15) | 35 ft/2.5 st | not found / none | none; 5 architectural elements | likely (expansive clay) - assumed | no | not verified | not computed | $1,579 water+ww | 0.92 |
| [City of Laredo](cities/laredo.json) | 1 | 2021 IRC | 2021 IECC | IPC 2021 | R-1 | 25/5/20 (3rd-party) | 35 ft | not found | none (ch. 3000) | likely (assumed) | no | +1 ft assumed | $1,951 | lot charge (2008: $1,600 for 6-8k sf) | 0.89 |
| [City of Lubbock](cities/lubbock.json) | 1 | 2021 IRC (amended) | 2021 IECC (amended) | IPC 2021 | SF-2 | 20/5/15 | 35 ft | not found | none | not found | no | BFE+1 ft; playa+2 ft | $312 (FY23-24 $0.11/sf) | roadway up to ~$3,150 (by area) | 0.9 |
| [City of McKinney](cities/mckinney.json) | 1 | 2024 IRC (Secondary, eff. 2025-10-01) | 2024 IECC (Secondary) | IPC 2024 | PD (fallback SF-5 base) | 20/7/15 (low-confidence fallback) | 35 ft / 2.5 st | 50% (SF-5, low confidence) | not city-enforceable; PD/HOA | yes - engineer letter in submittal | no | 2 ft above BFE (Secondary) | not found | water $1,754 + ww $2,899 (2019) + roadway by area | 0.95 |
| [City of Plano](cities/plano.json) | 1 | 2024 IRC (Secondary) | not verified | IPC (edition unverified) | SF-7 | 25/5/15 (Secondary) | 35 ft | not found | none by city (ch. 3000); HOA often | likely (unverified) | no | not verified (default 2 ft) | $1,443 (0.48/sf x 2,840 + $80) | not found | 0.95 |
| [City of Round Rock](cities/round-rock.json) | 1 | 2024 IRC | 2024 IECC | IPC 2024 | SF-2 (PUDs common) | 25/5/20 (unverified) | unverified | unknown / none | historic requirement, limited by state law | likely | no | 2 ft above ultimate 100-yr | $485 flat | ~$11,042 (W $4,912 + WW $2,921 + road $3,209) | 0.96 |
| [City of San Antonio](cities/san-antonio.json) | 1 | 2024 IRC (amended) | 2021 IECC (amended) | IPC 2024 | R-6 | 10*/5/20 (*verify; plat often 20) | 35 ft/2.5 st | not found / none | none | yes - PE/RA/geotech; PT = PE | no | ultimate-dev 100-yr; +1 ft assumed | not computed | $7.3k-$11.5k SAWS w+ww | 0.94 |
| [City of Beaumont](cities/beaumont.json) | 2 | 2021 IRC | 2021 IECC | IPC 2021 (assumed) | R-S | 25/5/25 (assumed) | 35 ft (assumed) | unknown | none (state preemption) | assumed yes | yes - TDI Inland II, 110 mph (143 Vult); engineer cert | Art. 24.05; freeboard not found (assume BFE+1) | $1,580 | none found | 0.97 |
| [City of Cedar Park](cities/cedar-park.json) | 2 | 2021 IRC (amended) | 2021 IECC | IPC 2021 | SU Semi-Urban Residential | 25/10/20 (15 street side) | 35 ft | unknown / none | no city mandate (HB 2439); HOA/PUD may | likely - assumed | no | unverified | not computed (BVD valuation; rate not found) | ~$6,350 water+ww per LUE | 0.96 |
| [City of Celina](cities/celina.json) | 2 | 2024 IRC (Ord. 2026-003, eff. early 2026) | 2024 IECC | IPC 2024 | PD on SF-R base | 20/5/20 (example PD) | not found | not found (20% open space district-level) | not city-enforceable; PD/HOA | yes (assumed) | no | not found | not found | ~$15,400-19,900 water+ww+roadway | 0.95 |
| [City of College Station](cities/college-station.json) | 2 | 2024 IRC (2026) | 2024 IECC (amended) | IPC 2024 | GS | 25/7.5/20 | 35 ft/2.5 st | not found / none | none (state preemption) | plans req.; seal not confirmed | no | 1 ft freeboard | $2,102 | ~$9,625 w+ww+roadway | 0.92 |
| [City of Conroe](cities/conroe.json) | 2 | 2021 IRC (third-party; unverified) | unverified | unverified | none - no zoning | plat/deed only | building code only | none (plat) | not found | likely (unverified) | no | BFE+12 in | not found | $0 (study pending, ~2027) | 0.96 |
| [City of Forney](cities/forney.json) | 2 | 2021 IRC + NCTCOG (eff. 1/1/2023) | 2021 IECC | IPC 2021 | PD (preferred); legacy SF-6 | 25/5/20 (assumed) | 35 ft (assumed) | unknown | not city-enforceable; PD/HOA | yes - engineer stamped + foundation letter | no | not found | not found | not found | 0.95 |
| [City of Georgetown](cities/georgetown.json) | 2 | 2021 IRC (amended) | 2021 IECC (amended) | IPC 2021 (assumed) | RS (5,500 sf min lot) | 20/6/10 (unverified) | 35 ft | unknown / none | no city mandate (HB 2439); HOA/PUD may | likely - assumed | no | unverified | $1,570 | water+ww max ~$18.3k/LUE + transportation (2025 increases) | 0.96 |
| [City of Hutto](cities/hutto.json) | 2 | 2024 IRC (Ord. 2025-008) | 2024 IECC (likely) | IPC 2024 | SF-2 / PUD (new UDC pending) | 25/5/20 (assumed) | 35 ft (assumed) | not found / none | none (state preemption) | yes (assumed) | no | 1 ft freeboard (assumed) | $1,600 flat (2022) | ~$11,620 water+ww (2021-era) | 0.96 |
| [City of Katy](cities/katy.json) | 2 | 2021 IRC | 2021 IECC (likely) | IPC 2021 (likely) | R-1 | 25(35 major)/5*/15 | 32 ft | unverified | preempted by state law (HOA may require) | likely | no | 500-yr (reported) | not found | not found (facility fees exist) | 0.96 |
| [City of Kyle](cities/kyle.json) | 2 | 2021 IRC | 2021 IECC | IPC 2021 | R-1-2 (or PUD) | 25/5/20 (assumed) | 35 ft (assumed) | not found / none | none (state preemption) | yes (assumed) | no | 1 ft freeboard (assumed) | $1,285 | $12,514 water+ww per LUE | 0.96 |
| [City of League City](cities/league-city.json) | 2 | 2021 IRC | 2021 IECC | IPC 2021 | RSF-7 | 25/5*/20* (*placeholder) | 35 ft (placeholder) | not found | not found | likely (unverified) | yes - Inland I, WPI-8 (whole city) | BFE+24 in or 500-yr+3 in | $1,136 | $11,860-$14,825 water+ww | 0.96 |
| [City of Leander](cities/leander.json) | 2 | 2021 IRC (Ord. 25-034-00) | 2021 IECC | IPC 2021 (assumed) | SFU (7,200 sf, 1,200 sf min home) | 20/5/10 (unverified) | 35 ft (unverified) | unknown / none | no city mandate (HB 2439); HOA/PUD may | likely - assumed | no | unverified | not found | water $8,762 + ww $2,301 (+ roadway) | 0.96 |
| [City of McAllen](cities/mcallen.json) | 2 | 2018 IRC (inferred) | unknown (state floor) | IPC 2018 | R-1 (UDC 2026) | 25/6/10 (rear Secondary; front/side assumed) | 35 ft (assumed) | not found | none known | likely (assumed) | no | +1 ft assumed | $454 | not found (MPU) | 0.88 |
| [City of Midland](cities/midland.json) | 2 | 2018 IRC | 2015 IECC | IPC 2018 | SF-2 (assumed) | 25/5/10 (assumed) | 35 ft (assumed) | not found | none (assumed) | not required (not found) | no | 1 ft freeboard | not found | w+ww+roadway (amounts not found) | 0.95 |
| [City of New Braunfels](cities/new-braunfels.json) | 2 | 2021 IRC (2023) | 2021 IECC | IPC 2021 | R-1A-6.6 | 25/5/20 (assumed) | 35 ft (assumed) | not found / none | none (state preemption) | yes - PE seal >500 sf | no | 2 ft freeboard | not found | $23,224 NBU w+ww + roadway | 0.94 |
| [City of Pearland](cities/pearland.json) | 2 | 2021 IRC (amended) | 2021 IECC | IPC 2021 | R-2 | 25/5/20 (unverified) | not found | not found | not found (PD/HOA likely) | likely (unverified) | yes - Brazoria-county parcels only (Inland II, WPI-8) | 1 ft above BFE or 500-yr, whichever higher | $1,164 | ~$9,625 water+ww (2023) | 0.96 |
| [City of Pflugerville](cities/pflugerville.json) | 2 | 2021 IRC (+App. H, J) | 2021 IECC (assumed) | IPC 2021 (assumed) | SF-S | 25/7.5/20(assumed) | 35 ft | not found / none | none (state preemption) | yes - expansive clay (assumed) | no | 1 ft freeboard (assumed) | not found | up to ~$14.7k water + $1.3k-$15.1k ww per SU (max allowable) | 0.96 |
| [City of Sugar Land](cities/sugar-land.json) | 2 | 2024 IRC (eff. 2026-01-21) | 2024 IECC | IPC 2024 | R-1 | 25/5/15 | 35 ft/2.5 st | 40% (verify) | preempted by state law (HOA may require) | likely | no | Ch. 8 min FFE (value not found) | ~$2,730 (est.) | none found; tap $1,115 | 0.96 |
| [City of Tyler](cities/tyler.json) | 2 | 2021 IRC (Sec. 6-151 amend.) | 2021 IECC | IPC 2021 | R-1A | 25/7.5/25 (street side 12) | 42 ft | 50% / no FAR | none (state preemption) | practice (assumed) | no | 1 ft freeboard | $1,193 | none found | 0.92 |
| [City of Waco](cities/waco.json) | 2 | 2024 IRC | 2018 IECC | IPC 2024 | R-1B | 25/5/25 (assumed) | 35 ft (assumed) | unknown | none (state preemption) | practice (assumed) | no | floodplain permit; freeboard unconfirmed | $775 | water+ww+roadway (amounts TBD) | 0.92 |
| [Cypress (unincorporated Harris County)](cities/cypress-unincorporated-harris.json) | 2 | none (LGC 233; 2021 IRC typical) | 2015 IRC ch.11 (uninspected) | MUD rules | none - deed restrictions | 20/5/10 placeholder (plat) | none | none | HOA | yes | no (not TWIA area) | 0.2% WSE + 24 in or street crown + 12 in (higher) | not found | none (MUD) | 0.96 |
| [Town of Little Elm](cities/little-elm.json) | 2 | 2024 IRC | 2024 IECC? (unconfirmed; state floor 2015 IRC Ch.11) | IPC (2024 likely) | SF-4 | 25/6/20 (street side ~15 assumed) | 35 ft/3 st | none found / none | none (state preemption); check HOA/PD | assumed yes | no | NFIP; freeboard not found | $2,414 (+$295 review) | ~$7,947 SA1 (water+ww+road) | 0.95 |
| [Town of Prosper](cities/prosper.json) | 2 | 2021 IRC (eff. 5/1/2023) | 2021 IECC | IPC 2021 | SF-10 base (most new = PD) | not found (SF-12.5: 30/8/25) | 40 ft / 2.5 st | not found | not city-enforceable; PD/HOA | yes (assumed) | no | not found | $2,940 | $14,390 water+ww + roadway | 0.95 |

## Top 10 engine changes (ranked by how many cities need them)

| # | Rule type | Cities needing it (of 43) | must / should / nice | What the engine does |
|---|---|---|---|---|
| 1 | `code-edition-by-city` | 42 | 20 / 24 / 0 | Pick the IRC / IECC / IPC-UPC / NEC editions the city actually adopted (2015, 2021 or 2024 IRC) instead of the hard-wired 2021 IRC model. Drives stair, egress, energy and electrical checks. |
| 2 | `climate-zone-envelope` | 41 | 42 / 0 / 0 | Choose wall/ceiling/floor R-values, window U-factor and SHGC from the IECC table for the county's climate zone (1A/2A/2B/3A/3B/4B), using the zone map of the energy-code edition in force (2015 vs 2021 maps differ: Dallas |
| 3 | `setback-by-district` | 36 | 24 / 12 / 0 | Replace the user's free-text setbacks with the district minimums (front, interior side, street side, rear), keeping the larger of district and plat building line. |
| 4 | `engineered-foundation-flag` | 34 | 14 / 20 / 0 | City requires a foundation designed and sealed by a Texas PE (usually post-tensioned slab per PTI on expansive clay). Add a 'needs engineer' flag, a soil-report line and a PT-slab line in the estimate; drawings show foun |
| 5 | `impact-fee-estimate` | 33 | 13 / 21 / 0 | Add water, wastewater and roadway impact (capital recovery) fees per single-family home to the estimate; amounts depend on service area and plat date. |
| 6 | `flood-elevation` | 30 | 22 / 10 / 0 | If the lot is in or near a floodplain, raise the finished floor: e.g. BFE + 1 ft, BFE + 2 ft, 500-yr + 2 ft (Houston), fully-developed-watershed BFE + 18 in (Denton). Changes slab height, steps, foundation type (no fill  |
| 7 | `permit-fee-formula` | 27 | 3 / 23 / 1 | Compute the building permit and plan-review fee from the city formula (per sq ft, flat, or tiered; Texas bars value-based residential fees, LGC 214.907). |
| 8 | `height-limit` | 26 | 16 / 10 / 0 | Maximum building height (ft and stories), measured per city definition; massing engine must check. |
| 9 | `survey-input-district` | 25 | 21 / 6 / 0 | Most new Texas homes sit in a Planned Development (PD/PUD) or a platted subdivision whose own standards override the base district. Ask the user for the district or PD name, or to upload the plat; otherwise use the base  |
| 10 | `electrical-code-edition` | 24 | 8 / 15 / 3 | NEC edition for electrical checks (state default NEC 2026 from 2026-09-01; many cities still cite 2020 or 2023). |

The full list of 42 rule types, with the survey inputs and data sketches, is in [`engine-change-catalogue.md`](engine-change-catalogue.md).

## Completeness by city

"Researched" counts leaf values marked Sourced or Secondary. "Assumed" counts values that are placeholders, judgement or not found.

| City | Tier | Researched values (Sourced+Secondary) | Assumed | Share researched | Engine changes |
|---|---|---|---|---|---|
| City of Amarillo | 1 | 20 | 34 | 37% | 9 |
| City of Arlington | 1 | 32 | 23 | 58% | 14 |
| City of Austin | 1 | 32 | 31 | 51% | 18 |
| City of Brownsville | 1 | 20 | 32 | 38% | 12 |
| City of Corpus Christi | 1 | 36 | 20 | 64% | 13 |
| City of Dallas | 1 | 31 | 30 | 51% | 17 |
| City of Denton | 1 | 18 | 36 | 33% | 9 |
| City of El Paso | 1 | 28 | 24 | 54% | 14 |
| City of Fort Worth | 1 | 34 | 28 | 55% | 15 |
| City of Frisco | 1 | 26 | 35 | 43% | 13 |
| City of Garland | 1 | 28 | 26 | 52% | 12 |
| City of Houston | 1 | 44 | 26 | 63% | 18 |
| City of Irving | 1 | 30 | 24 | 56% | 10 |
| City of Killeen | 1 | 28 | 29 | 49% | 10 |
| City of Laredo | 1 | 26 | 24 | 52% | 10 |
| City of Lubbock | 1 | 33 | 24 | 58% | 14 |
| City of McKinney | 1 | 29 | 30 | 49% | 10 |
| City of Plano | 1 | 21 | 33 | 39% | 13 |
| City of Round Rock | 1 | 19 | 34 | 36% | 10 |
| City of San Antonio | 1 | 39 | 26 | 60% | 12 |
| City of Beaumont | 2 | 18 | 37 | 33% | 11 |
| City of Cedar Park | 2 | 24 | 30 | 44% | 12 |
| City of Celina | 2 | 29 | 31 | 48% | 9 |
| City of College Station | 2 | 37 | 30 | 55% | 14 |
| City of Conroe | 2 | 13 | 37 | 26% | 9 |
| City of Forney | 2 | 19 | 36 | 35% | 9 |
| City of Georgetown | 2 | 18 | 35 | 34% | 13 |
| City of Hutto | 2 | 16 | 43 | 27% | 12 |
| City of Katy | 2 | 18 | 32 | 36% | 9 |
| City of Kyle | 2 | 19 | 40 | 32% | 11 |
| City of League City | 2 | 25 | 28 | 47% | 12 |
| City of Leander | 2 | 17 | 39 | 30% | 12 |
| City of McAllen | 2 | 16 | 34 | 32% | 8 |
| City of Midland | 2 | 23 | 33 | 41% | 10 |
| City of New Braunfels | 2 | 28 | 38 | 42% | 13 |
| City of Pearland | 2 | 27 | 30 | 47% | 12 |
| City of Pflugerville | 2 | 17 | 47 | 27% | 10 |
| City of Sugar Land | 2 | 29 | 21 | 58% | 14 |
| City of Tyler | 2 | 28 | 28 | 50% | 11 |
| City of Waco | 2 | 16 | 37 | 30% | 9 |
| Cypress (unincorporated Harris County) | 2 | 8 | 52 | 13% | 10 |
| Town of Little Elm | 2 | 27 | 30 | 47% | 10 |
| Town of Prosper | 2 | 24 | 33 | 42% | 10 |
| Texas city, not listed | fallback | 19 | 43 | 31% | 14 |
| Unincorporated Texas county | fallback | 8 | 54 | 13% | 11 |

## What could not be found, by city

Each city's JSON has a full `notFound` list. The first items for each:

- **City of Amarillo:** Zoning lot size/rear yard/coverage from ordinance.; Floodplain freeboard.; Snow load and wind design values.; Water/sewer tap fees.; Mechanical/fuel gas editions.
- **City of Arlington:** Arlington Sec. 1.04 single-family amendment text; Fee tier above 2,000 sq ft; Post-2017 impact-fee updates; Tap fees; Market cost per sq ft
- **City of Austin:** Primary LDC text (Municode blocked); DSD per-sq-ft fees; tap fees; frost depth; market $/sqft; population vintage verification
- **City of Brownsville:** IRC edition adopted by city; Fee schedule; BPUB fee amounts; Flood freeboard; Foundation seal rule
- **City of Corpus Christi:** Impact fees per home; Water/wastewater tap fees; Lot coverage/open space for RS-6; Fire sprinkler local rule; Minimum lot width (assumed 50 ft)
- **City of Dallas:** R-7.5(A) min lot width and depth, corner side yard, story limit; Single-family parking count (51A-4.209); Tap and meter fees; Local Table R301.2(1) wind, frost and termite values; Residential review times; Market cost per sq ft
- **City of Denton:** R4/R6/R7 dimensional standards; impact fee $ amounts; tap fees; roadway impact fee; garage/ADU/tree rules; review days; market $/sf
- **City of El Paso:** 2021 IRC adoption ordinance number/date; FY2026 permit fee tier rate; Floodplain freeboard; Plumbing, electrical, mechanical, fuel gas editions; Tap fees; Market cost per sq ft; Review times
- **City of Fort Worth:** permit fee formula; plan review fee; tap fees; minimum lot depth; flood freeboard; frost depth; parking count; ADU rules; market $/sqft
- **City of Frisco:** Permit and plan review fees; Impact fee rates; Tap fees; Flood freeboard value; Lot coverage; Min dwelling size; Review days
- **City of Garland:** SF-7 setbacks/height/coverage table; Garland 2015 IRC amendment text; Wastewater impact and sewer tap fee amounts; Market cost per sq ft
- **City of Houston:** Permit fee tier amounts (PDF not fetchable); Tap/meter fees; Market cost per sq ft; Frost depth; Corner-lot side building line; Chapter 26 parking text
- **City of Irving:** R-7.5 setbacks, height and coverage (jumbled extracts); Text of Irving 2024 IRC amendments; Tap fees; Residential A/AE freeboard; Market cost per sq ft
- **City of Killeen:** R-1 lot coverage; parking minimum; ADU rules; tree rules; permit fee formula; tap fees; review days; flood freeboard; local Table R301.2(1) climatic values
- **City of Laredo:** Flood freeboard; Current utility impact/lot charges; Lot coverage; Street side setback; Foundation seal rule
- **City of Lubbock:** Street-side setback, lot depth, lot coverage, ADU and parking rules in SF-2.; IRC local amendment text.; Water/sewer tap fees and water/wastewater impact fee amounts.; ZIP list / review days.
- **City of McKinney:** permit fee schedule; current impact fee amounts / roadway; official UDC setbacks; NEC edition; tap fees; review days; market $/sf
- **City of Plano:** R325 sprinkler trigger; SF-7 lot width/depth/coverage/street side; impact fee amounts; tap fees; flood freeboard; energy edition; review days; market $/sf
- **City of Round Rock:** SF-2 setbacks/height/coverage from current code.; Adoption ordinance number.; Market cost per sq ft (not researched; search budget).; Tree ordinance details.
- **City of San Antonio:** FY2026 fee table; R-6 coverage limit; Freeboard; Frost depth local table; Review days; Market $/sf
- **City of Beaumont:** R-S dimensions; Flood freeboard; Tap fees; Adoption ordinance number; Plumbing/mechanical code names; Market $/sf
- **City of Cedar Park:** Permit fee rate table; Floodplain freeboard; City impervious cover limits
- **City of Celina:** SF-R base dimensions; Permit fee rate; Flood freeboard; Garage orientation rule; Tap fees; Market $/sf
- **City of College Station:** Ordinance number for 2024 code adoption; GS lot coverage; Roadway fee table amount; Residential foundation seal rule
- **City of Conroe:** adoption ordinance for current codes; permit fee formula/example; tap fees; market $/sf; review days
- **City of Forney:** Setbacks/height/coverage; Permit fee rate; Impact fees; Flood freeboard; Ordinance number; Market $/sf
- **City of Georgetown:** RS setbacks (table not in search extracts); Floodplain freeboard; Impact fee collection rates after Aug 2025; Plumbing code name (assumed IPC); Population vintage estimate (not searched)
- **City of Hutto:** SF-2 setbacks; Current impact fees; Tree rules; Floodplain freeboard
- **City of Katy:** impact/facility fees; permit fee formula/example; R-1 min lot size/width, interior side yard, coverage; plan review fee; review days
- **City of Kyle:** R-1-2 setbacks/height/coverage; Roadway impact fee; Floodplain freeboard; Adopting ordinance number for 2021 codes
- **City of League City:** UDC dimensional table (side/rear/height/coverage); NEC edition; adoption ordinance number; plan review fee; city tap fees; market $/sf; review days
- **City of Leander:** SFU/SFS setbacks; Building permit fee schedule; Roadway impact fee amount; Floodplain freeboard; Tree DBH thresholds
- **City of McAllen:** IRC adoption ordinance/edition explicitly; UDC R-1 dimensional table; MPU tap/impact fees; Floodplain freeboard (1 search); Climate zone under 2021 IECC (2 searches)
- **City of Midland:** Zoning setbacks/lot/height for SF districts; Permit fee values; Impact fee amounts; Ordinance numbers for 2018 code adoption; Frost depth
- **City of New Braunfels:** Permit fee schedule; R-1A-6.6 dimensional table; Roadway impact fee amounts; Ordinance number for 2021 code adoption; Tap/meter fees
- **City of Pearland:** UDC setbacks/height/coverage (primary); IRC adoption ordinance number; residential amendments text; masonry rule; tap fees; plan review fee; market $/sf; review days
- **City of Pflugerville:** Building permit fee schedule (city page 'not found'); Lot coverage / impervious cover; Tree ordinance details; Flood freeboard; Plan review days
- **City of Sugar Land:** flood freeboard value; impact fee schedule; R-1 FAR; full permit fee tiers; review days
- **City of Tyler:** Sec. 6-151 amendment text; Water/sewer tap and impact fees; UDC lot width/depth rows; Local Table R301.2(1) design criteria (wind, frost)
- **City of Waco:** R-1B dimensional standards (Ch. 28 not reachable); Impact fee dollar amounts; 2024 IRC local amendments; Floodplain freeboard; Tap fees
- **Cypress (unincorporated Harris County):** Harris County permit fee schedule; Harris County plat building-line standard; MUD tap fees
- **Town of Little Elm:** Census Vintage 2024 population; SF-4 lot width/depth, corner setback, min dwelling size; freeboard; tap fees; review days; tree rules
- **Town of Prosper:** SF-10 setbacks/coverage; Flood freeboard; Roadway impact fee per home; Tap fees; Adoption ordinance number; Market $/sf
- **Texas city, not listed:** Direct reads of statutes.capitol.texas.gov (DNS/egress blocked); all statute values are from search excerpts (Secondary); 2021 IECC Table R301.1 Texas rows (only Dallas, Collin, Denton, Rockwall seen)
- **Unincorporated Texas county:** Direct reads of statutes.capitol.texas.gov (DNS/egress blocked) - statute values are Secondary from search excerpts; OSSF lot-size figures (30 TAC 285.4) not re-verified

## Coordinator spot-checks (second reads of tier-1 values)

| City | Value checked | Result |
|---|---|---|
| Dallas | R-7.5(A) front 25 / side 5 / rear 5 / height 30 ft | Confirmed on the city's R-7.5(A) planning page. Coverage 45% not visible in the extract (truncated); 45% seen on R-5(A) page only. |
| Austin | SF-3 front 25 / street side 15 / side 5 / rear 10 / 35 ft / 40% building / 45% impervious | Confirmed by two independent summaries; § 25-2-773 overrides for 2-3 units (HOME). |
| Fort Worth | A-5 front 20 / side 5 / rear 5 | Not fully confirmed: a city BOA docket shows a 25 ft "projected front yard" on an A-5 lot (block-face rule). Kept 20 ft base, engine asks. |
| San Antonio | R-6 front yard | Still conflicting (10 ft PropertyZoned / 20 ft old IB 565 / 25 ft Building Club). Engine uses max(district, plat line) and asks. |
| Plano | SF-7 7,000 sf, 25/5/15, 35 ft | Same figures again, but only from a beta third-party site; not primary. |

## The biggest differences between Texas cities that change a house design

1. **Which code edition applies.** Texas cities span four IRC editions: 2015 (Garland), 2018 (Midland, McAllen), 2021 (most) and 2024 (Austin, San Antonio, Frisco, Plano, McKinney, Irving, Round Rock, Sugar Land, Killeen, Waco, College Station and others). Energy editions are mixed too: 2015 in Fort Worth, 2018 in Waco, 2024 in Austin. Austin's 2024 amendments also require air conditioning in every home.
2. **Setbacks and massing.** Base fronts are mostly 20-25 ft, but:
   - Houston has no zoning, only Chapter 42 building lines (20 ft front, a 10 ft house line with a 19-20 ft garage line, no side or rear setbacks).
   - El Paso requires front plus rear of at least 50 ft.
   - Arlington requires 40 ft on arterials.
   - Austin adds an FAR cap (larger of 0.4 or 2,300 sq ft), a 45° tent plane starting 15 ft up, 40% building coverage and 45% impervious cover.
   - Most suburban homes are in PDs, so the plat governs.
3. **Flood elevation.** Rules range from BFE + 1 ft to 2 ft above the 500-year flood level (Houston), 3 ft above the design flood (Dallas), 2 ft above "ultimate" or fully urbanized floodplains (Round Rock, Arlington) and 18 in above the fully developed floodplain, including lots within 200 ft of it (Denton). Lubbock adds playa-lake overflow, and coastal V zones need piles or piers with no fill.
4. **Coastal windstorm.** In Corpus Christi, Brownsville, League City, Beaumont and part of Pearland, the house must be designed and certified for about 140-150 mph under TDI's 2024 IRC. That means opening protection in the debris region, roof deck nailing, uplift connectors and engineer inspections.
5. **Garage and facade rules.** Examples:
   - Houston and Lubbock garage building lines (19-20 ft).
   - Killeen caps garage doors at 50% of the facade and requires 5 architectural elements.
   - Leander needs a lot at least 60 ft wide for a 3-bay front garage.
   - Austin and Cedar Park protect heritage trees from 24-26 in, which can move the footprint.
   - Masonry is now mostly an HOA question, not a city rule.

## The biggest cost drivers

1. **Impact fees.** These range from $0 (Dallas, Conroe) and about $1,600 (Killeen) to $11,000-15,000 (Round Rock, Kyle, League City, Prosper, Celina) and about $23,000 (New Braunfels NBU water and wastewater, plus a roadway fee). This is often 5-20 times the building permit fee.
2. **Engineered foundations on expansive clay.** These cities require a Texas PE-sealed foundation (usually post-tensioned) and often a geotechnical report. The cost includes the engineering fee, the soil report and the slab premium.
3. **Windstorm package** on the coast: impact-rated windows or shutters, straps and hardware, sealed roof deck, engineer inspections and WPI-8.
4. **Flood elevation.** Raising the slab 1-3 ft (fill where allowed, otherwise a stem wall or piers) in Houston, Dallas, Austin, Denton and coastal cities.
5. **Labour level and local rules.** Metro factors run from 0.88 (Brownsville, McAllen) to 0.97 (Beaumont). Add HOA masonry (brick veneer), tree mitigation ($225-450 per inch of trunk in Georgetown and Cedar Park), the 2024 IECC envelope where adopted, and sprinklers in grandfathered Frisco and Plano.

## Open questions for a Texas architect or engineer

1. **PD and plat setbacks.** For most new subdivisions (Frisco, McKinney, Celina, Prosper, Round Rock, Leander, Forney), is it right to treat the recorded plat and PD ordinance as governing, and to warn when base-district values are used?
2. **Engineered foundations.** In which cities does a PE seal apply to every new house (Dallas R401.2, Fort Worth, Frisco, San Antonio for PT slabs, New Braunfels over 500 sq ft)? Elsewhere, is it only standard practice? What is the typical fee range for a PE design plus geotech report for a 2,400 sq ft house on high-PI clay?
3. **Climate zones.** Under the 2021 IECC map, confirm the zones for Tarrant, Ellis, Johnson, Kaufman, Parker, Cameron and Hidalgo. For cities that span 2A and 3A, confirm which zone the city's amendment uses.
4. **Windstorm.** For a house permitted in 2026-2027 in Corpus Christi or League City, confirm the design wind speed and opening-protection requirements under TDI's 2024 IRC, while the city itself enforces the 2021 IRC.
5. **Masonry.** Confirm how Gov't Code ch. 3000 applies to masonry rules in PDs and zoning adopted before 2019 (Plano, Frisco, McKinney, Sugar Land).
6. **Sprinklers.** What exactly triggers Plano's R325 sprinkler rule, and does Frisco's 6,000 sq ft rule (conditioned plus garage) still apply under the 2024 IRC?
7. **Energy code.** Fort Worth (2015 IECC) and Waco (2018 IECC) are below the 2021 model. Should the engine design to the city's minimum or to the 2021 IECC as a better default?
8. **Electrical.** NEC 2026 has been the state code since 2026-09-01. Do the city NEC 2020 and 2023 adoptions matter at all for plan review now?
9. **SB 15.** Does it apply to any Keystone lot at all? It covers only new 5+ acre subdivisions in large cities, so probably not for single custom homes.
10. **Unincorporated Harris County.** Confirm whether Harris County opted into LGC subchapter F (the 233.153 standard), and the Engineering Department permit fee.
