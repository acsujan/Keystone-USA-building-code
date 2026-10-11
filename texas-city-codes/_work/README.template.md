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
| `engine-change-catalogue.md` | All engine changes, de-duplicated into NRULES rule types. For each: the survey input it needs, the cities that use it, and a data sketch. |
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

COSTTABLE

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

COMPARISON

## Top 10 engine changes (ranked by how many cities need them)

TOP

The full list of NRULES rule types, with the survey inputs and data sketches, is in [`engine-change-catalogue.md`](engine-change-catalogue.md).

## Completeness by city

"Researched" counts leaf values marked Sourced or Secondary. "Assumed" counts values that are placeholders, judgement or not found.

COMPLETENESS

## What could not be found, by city

Each city's JSON has a full `notFound` list. The first items for each:

NOTFOUND

## Coordinator spot-checks (second reads of tier-1 values)

SPOT

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
