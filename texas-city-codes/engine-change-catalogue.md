# Engine change catalogue

All engine changes from the city files, grouped into rule types. Each rule type is one thing the Keystone engine must learn to do. For each: what it does, the survey input it needs, the cities that use it, and a sketch of the data. Counts are cities (tier 1 + tier 2, not the two fallback profiles) that have at least one change of that type.

Rule types are ranked by the number of cities that need them.

| Rule type | Cities | must | should | nice |
|---|---|---|---|---|
| [`code-edition-by-city`](#code-edition-by-city) | 42 | 20 | 24 | 0 |
| [`climate-zone-envelope`](#climate-zone-envelope) | 41 | 42 | 0 | 0 |
| [`setback-by-district`](#setback-by-district) | 36 | 24 | 12 | 0 |
| [`engineered-foundation-flag`](#engineered-foundation-flag) | 34 | 14 | 20 | 0 |
| [`impact-fee-estimate`](#impact-fee-estimate) | 33 | 13 | 21 | 0 |
| [`flood-elevation`](#flood-elevation) | 30 | 22 | 10 | 0 |
| [`permit-fee-formula`](#permit-fee-formula) | 27 | 3 | 23 | 1 |
| [`height-limit`](#height-limit) | 26 | 16 | 10 | 0 |
| [`survey-input-district`](#survey-input-district) | 25 | 21 | 6 | 0 |
| [`electrical-code-edition`](#electrical-code-edition) | 24 | 8 | 15 | 3 |
| [`lot-min-size`](#lot-min-size) | 22 | 0 | 22 | 1 |
| [`masonry-percentage`](#masonry-percentage) | 17 | 0 | 15 | 3 |
| [`building-line-plat`](#building-line-plat) | 13 | 9 | 5 | 0 |
| [`deed-restriction-check`](#deed-restriction-check) | 11 | 3 | 10 | 0 |
| [`lot-coverage`](#lot-coverage) | 10 | 6 | 3 | 1 |
| [`garage-placement`](#garage-placement) | 10 | 2 | 6 | 2 |
| [`windstorm-package`](#windstorm-package) | 9 | 11 | 3 | 2 |
| [`plumbing-code-variant`](#plumbing-code-variant) | 8 | 1 | 4 | 4 |
| [`wind-speed`](#wind-speed) | 7 | 3 | 4 | 0 |
| [`fire-sprinkler`](#fire-sprinkler) | 7 | 3 | 3 | 3 |
| [`impervious-cover`](#impervious-cover) | 7 | 1 | 5 | 1 |
| [`tree-preservation`](#tree-preservation) | 7 | 1 | 5 | 1 |
| [`egress-stairs-variant`](#egress-stairs-variant) | 6 | 2 | 2 | 2 |
| [`sealed-drawings-required`](#sealed-drawings-required) | 4 | 3 | 1 | 0 |
| [`expansive-soil-foundation`](#expansive-soil-foundation) | 4 | 3 | 2 | 1 |
| [`frost-depth`](#frost-depth) | 4 | 1 | 3 | 1 |
| [`tap-fee-estimate`](#tap-fee-estimate) | 4 | 0 | 1 | 3 |
| [`no-zoning`](#no-zoning) | 3 | 4 | 0 | 0 |
| [`min-dwelling-size`](#min-dwelling-size) | 3 | 3 | 0 | 0 |
| [`energy-compliance-doc`](#energy-compliance-doc) | 3 | 3 | 2 | 0 |
| [`snow-load`](#snow-load) | 3 | 0 | 2 | 1 |
| [`side-wall-articulation`](#side-wall-articulation) | 2 | 1 | 1 | 0 |
| [`seismic-category`](#seismic-category) | 2 | 1 | 0 | 2 |
| [`hail-roof`](#hail-roof) | 2 | 0 | 0 | 3 |
| [`adu-rules`](#adu-rules) | 2 | 0 | 1 | 1 |
| [`far-limit`](#far-limit) | 1 | 1 | 0 | 0 |
| [`setback-plane`](#setback-plane) | 1 | 1 | 0 | 0 |
| [`mechanical-cooling-required`](#mechanical-cooling-required) | 1 | 1 | 0 | 0 |
| [`occupancy-limit`](#occupancy-limit) | 1 | 0 | 1 | 0 |
| [`parking-min`](#parking-min) | 1 | 0 | 1 | 0 |
| [`termite-protection`](#termite-protection) | 1 | 0 | 1 | 0 |
| [`lot-drainage`](#lot-drainage) | 1 | 0 | 0 | 1 |

## code-edition-by-city

**Code edition by city.** Pick the IRC / IECC / IPC-UPC / NEC editions the city actually adopted (2015, 2021 or 2024 IRC) instead of the hard-wired 2021 IRC model. Drives stair, egress, energy and electrical checks.

- **Survey input:** City (from address).
- **Cities (42):** amarillo, arlington, austin, beaumont, cedar-park, celina, college-station, conroe, corpus-christi, cypress-unincorporated-harris, dallas, denton, el-paso, forney, fort-worth, frisco, garland, georgetown, houston, hutto, irving, katy, killeen, kyle, laredo, league-city, leander, little-elm, lubbock, mcallen, mckinney, midland, new-braunfels, pearland, pflugerville, plano, prosper, round-rock, san-antonio, sugar-land, texas-baseline, texas-unincorporated, tyler, waco
- **Priority mix:** 20 must, 24 should, 0 nice
- **Data sketch:**

```json
{"irc": "2024 IRC", "energy": "2021 IECC (amended)", "plumbing": "IPC 2024", "electrical": "NEC 2023", "effective": "2026-03-01", "ordinance": "..."}
```

Examples from the city files:

- `amarillo` (should, plan): Check plans against 2021 IRC (excluding Part VIII Electrical; Appendices A-J adopted) (city adoption) and energy code 2015 IECC last confirmed; 2021-cycle update not confirmed instead of the plain 2021 IRC model — source: [City of Amarillo - Residential Code Information (2021 IRC with City amendments F](https://www.amarillo.gov/building-safety/residential-permits/)
- `arlington` (should, plan): Check plans against 2021 IRC (Arlington local amendments, Construction Chapter Art. I Sec. 1.04) (city adoption) and energy code 2021 IECC (Arlington amended, adopted 11-1-2022) instead of the plain 2021 IRC model — source: [City of Arlington Ordinance 25-075 amending the Construction Chapter (recites 20](https://www.arlingtontx.gov/files/assets/city/v/1/city-secretary/documents/city-code-of-ordinances/adopted-ordinances-not-yet-codified/construction-chapter-ord.-25-075.pdf)
- `austin` (must, drawings): Use 2024 IRC (not 2021) as base residential code for Austin permits applied on/after 2025-07-10 — source: [Ordinance No. 20250410-040 (2024 IRC + local amendments, Ch. 25-12 Art. 11)](https://services.austintexas.gov/edims/document.cfm?id=450486)
- `beaumont` (should, plan): Check plans against 2021 IRC (city adoption) and energy code 2021 IECC instead of the plain 2021 IRC model — source: [City of Beaumont Commercial and Residential Accessory Building Permit Checklist ](https://www.beaumonttexas.gov/DocumentCenter/View/4134/Commercial-and-Residential-Accessory-Building-Permit-Checklist)
- `cedar-park` (should, plan): Check plans against 2021 IRC (city adoption) and energy code 2021 IECC instead of the plain 2021 IRC model — source: [City of Cedar Park Code of Ordinances - Chapter 3 Building Regulations (code ado](https://ecode360.com/38594319)
- `celina` (must, plan): Run plan checks against the 2024 IRC (not 2021) for permits after early 2026. — source: [Celina - Signed Building and Fire Code Ordinance 2024 I-Codes (Ord. 2026-003, am](https://www.celina-tx.gov/DocumentCenter/View/14757/Signed_Building-and-Fire-Code-Ordinance_2024-I-Codes)
- … and 38 more in the city files.

## climate-zone-envelope

**Climate-zone insulation table.** Choose wall/ceiling/floor R-values, window U-factor and SHGC from the IECC table for the county's climate zone (1A/2A/2B/3A/3B/4B), using the zone map of the energy-code edition in force (2015 vs 2021 maps differ: Dallas County 3A -> 2A).

- **Survey input:** County (from address); energy code edition comes from the city rule.
- **Cities (41):** amarillo, arlington, austin, beaumont, brownsville, cedar-park, celina, college-station, conroe, corpus-christi, cypress-unincorporated-harris, dallas, denton, el-paso, forney, fort-worth, frisco, garland, georgetown, houston, hutto, irving, killeen, kyle, laredo, league-city, leander, little-elm, lubbock, mcallen, mckinney, midland, new-braunfels, pearland, pflugerville, plano, prosper, round-rock, san-antonio, texas-baseline, tyler, waco
- **Priority mix:** 42 must, 0 should, 0 nice
- **Data sketch:**

```json
{"county": "Dallas", "zoneByEdition": {"2015": "3A", "2021": "2A"}, "table": "IECC R402.1.2 by edition"}
```

Examples from the city files:

- `amarillo` (must, envelope): Use climate zone 4B envelope tables (higher wall/ceiling R, lower fenestration U than CZ 3); energy edition unconfirmed (2015 IECC last confirmed) — source: Assumed: 2021 IECC Table R301.1 county climate zones (not fetched)
- `arlington` (must, envelope): Apply 2021 IECC Climate Zone 3A envelope tables. — source: Assumed - researcher judgement (not verified this session)
- `austin` (must, envelope): Use 2024 IECC CZ 2A envelope with Austin amendments (not state 2021 IECC) — source: [Council backup File ID 25-0605: 2024 IECC adoption (Ch. 25-12 Art. 12)](https://services.austintexas.gov/edims/document.cfm?id=448388)
- `beaumont` (must, envelope): Use climate zone 2A envelope tables; state floor is 2015 IRC Ch. 11 (ERI option under HSC 388.003) — source: [Texas Health & Safety Code Ch. 388 (Texas Building Energy Performance Standards)](https://statutes.capitol.texas.gov/Docs/HS/htm/HS.388.htm)
- `brownsville` (must, envelope): Envelope per IECC climate zone 2A — source: Assumed - agent judgement (no source found within wave-2 search budget)
- `cedar-park` (must, envelope): Use IECC Climate Zone 2A prescriptive envelope for the adopted IECC edition — source: Assumed
- … and 36 more in the city files.

## setback-by-district

**Setback by zoning district.** Replace the user's free-text setbacks with the district minimums (front, interior side, street side, rear), keeping the larger of district and plat building line.

- **Survey input:** Zoning district (or let the user pick from the city's list); corner lot yes/no; street type (local/arterial).
- **Cities (36):** arlington, austin, beaumont, brownsville, cedar-park, college-station, corpus-christi, dallas, el-paso, forney, fort-worth, frisco, garland, georgetown, houston, hutto, irving, katy, killeen, kyle, laredo, league-city, leander, little-elm, lubbock, mcallen, midland, new-braunfels, pearland, pflugerville, plano, round-rock, san-antonio, sugar-land, tyler, waco
- **Priority mix:** 24 must, 12 should, 0 nice
- **Data sketch:**

```json
{"district": "R-7.5(A)", "frontFt": 25, "sideFt": 5, "streetSideFt": 15, "rearFt": 5, "arterialFrontFt": 40, "frontPlusRearMinFt": null}
```

Examples from the city files:

- `arlington` (must, setbacks): RS-7.2: front 20 ft (40 ft on arterial/collector), street side 15 ft, interior side 5 ft (assumed), rear 20 ft; plat lines govern. — source: [City of Arlington Unified Development Code Chapter (code of ordinances PDF), Sec](https://www.arlingtontx.gov/files/assets/city/v/8/city-secretary/documents/city-code-of-ordinances/unified-development-code-chapter.pdf)
- `austin` (must, setbacks): SF-3/SF-2 setbacks: front 25, interior side 5, street side 15, rear 10 ft — source: [Neuhaus RE - Complete Guide to Zoning and Land Use in Austin (2026)](https://neuhausre.com/guides/zoning-land-use-guide-austin/)
- `beaumont` (should, setbacks): Default RS Residential Single-Family Dwelling (assumed): front 25, side 5, street side 10, rear 25 ft - ASSUMED, require user to confirm from plat/zoning letter — source: Assumed
- `brownsville` (must, setbacks): R-1: front 25 / corner street side 20 / side 5 / rear 5 ft (side/rear from third-party; verify) — source: [Brownsville TX code Chapter 3 (zoning districts) - Zoneomics mirror](https://www.zoneomics.com/code/brownsville-TX/chapter_3)
- `cedar-park` (must, setbacks): SU Semi-Urban Residential: front 25 / interior side 10 / street side 15 / rear 20 ft; lot 8,250 sf, 75 ft wide (90 corner); allow -5 ft front for porch or tree preservation — source: [Cedar Park TX UDC Chapter 11 - Table 11.03.061A Single-Family Residential Lot an](https://www.zoneomics.com/code/cedar-park-TX/chapter_3)
- `college-station` (must, setbacks): GS: front 25 / side 7.5 / street side 15 / rear 20 ft — source: [City of College Station - GS General Suburban zoning district fact sheet](https://www.cstx.gov/media/5sti0f32/gs.pdf)
- … and 30 more in the city files.

## engineered-foundation-flag

**Engineered foundation flag.** City requires a foundation designed and sealed by a Texas PE (usually post-tensioned slab per PTI on expansive clay). Add a 'needs engineer' flag, a soil-report line and a PT-slab line in the estimate; drawings show foundation as 'by engineer'.

- **Survey input:** None (city rule); optional soil report / PI value.
- **Cities (34):** arlington, beaumont, brownsville, cedar-park, celina, college-station, corpus-christi, dallas, denton, forney, fort-worth, frisco, garland, georgetown, houston, hutto, irving, katy, killeen, kyle, laredo, leander, little-elm, mcallen, mckinney, new-braunfels, pearland, pflugerville, plano, prosper, san-antonio, sugar-land, tyler, waco
- **Priority mix:** 14 must, 20 should, 0 nice
- **Data sketch:**

```json
{"required": true, "basis": "R401.2 amendment", "soilReport": "required|alternative", "estimate": ["geotech report", "PE foundation design", "PT slab premium"]}
```

Examples from the city files:

- `arlington` (should, foundation): Flag an engineered (PE-sealed) post-tensioned slab as the default for expansive DFW clay; confirm whether the city amendment mandates it. — source: Assumed - researcher judgement (not verified this session)
- `beaumont` (should, foundation): Flag engineer-designed slab for expansive clay — source: Assumed
- `brownsville` (should, foundation): Flag engineered slab (expansive Rio Grande delta clays) - assumed — source: Assumed - agent judgement (no source found within wave-2 search budget)
- `cedar-park` (should, foundation): Flag PE-sealed engineered slab (expansive clay east of I-35 / variable limestone and clay in the west) — source: Assumed
- `celina` (must, foundation): Flag PE-sealed engineered foundation (post-tensioned slab) for all new homes on Collin County expansive clay. — source: Assumed - agent judgement (no source could be read this session)
- `college-station` (should, foundation): Flag engineered slab (expansive clay); city requires foundation plans, seal rule not confirmed — source: [City of College Station - Single Family Dwelling/Duplex building permit page](https://www.cstx.gov/living-here/building-and-renovating/building-permits/single-family-dwellingduplex/)
- … and 28 more in the city files.

## impact-fee-estimate

**Impact fees per home.** Add water, wastewater and roadway impact (capital recovery) fees per single-family home to the estimate; amounts depend on service area and plat date.

- **Survey input:** Service area / plat date (or address); meter size (default 5/8 or 3/4 in).
- **Cities (33):** arlington, austin, brownsville, cedar-park, celina, college-station, conroe, dallas, denton, el-paso, forney, fort-worth, frisco, garland, georgetown, houston, hutto, irving, killeen, kyle, league-city, leander, little-elm, lubbock, mckinney, midland, new-braunfels, pearland, pflugerville, prosper, round-rock, san-antonio, waco
- **Priority mix:** 13 must, 21 should, 0 nice
- **Data sketch:**

```json
{"water": 4912, "wastewater": 2921, "roadway": 3209, "unit": "per LUE", "platAfter": "2024-01-01"}
```

Examples from the city files:

- `arlington` (must, estimate): Add water $828 + sewer $418 per 5/8 meter, plus roadway $253-312.50 per vehicle-mile by service area. — source: [City of Arlington impact fee - new fee schedules (Ord. 17-002, eff. 7-1-2017)](https://www.arlingtontx.gov/files/assets/city/v/3/planning-and-development-services/documents/long-range-planning/new-fee-schedules.pdf)
- `austin` (must, estimate): Add Austin Water impact fees $4,800 water + $2,900 wastewater per unit (lots platted after 2023-10-01) — source: [Austin Water - Rates and Fees (impact fee schedule)](https://www.austintexas.gov/water/rates-and-fees)
- `brownsville` (should, estimate): Add city capital recovery fee ~$850-$1,050 per home (2026) + BPUB impact fees (amount TBD) — source: [City of Brownsville news: commission action incl. capital recovery fee for new d](https://www.brownsvilletx.gov/CivicAlerts.asp?AID=1891)
- `cedar-park` (should, estimate): Add ~$6,350 water+wastewater impact fees per home (1 LUE; ~$3,170 ww + ~$3,180 water) — source: [Cedar Park Capital Improvement Advisory Committee approves water and wastewater ](https://cp.soar.com/articles/5602256/Cedar-Park/Williamson-County/Texas/Capital-Improvement-Advisory-Committee-approves-water-and-wastewater-impact-fee-study-report)
- `celina` (must, estimate): Add impact fees per SF home: water + wastewater + roadway, default ~$15,400 (DBA-reported adopted) with a high case ~$19,900 (2025 water/ww maximum $14,369 + roadway $5,500). Show as large line item. — source: [City of Celina updates impact fees](https://dallasbuilders.org/city-of-celina-updates-impact-fees/)
- `college-station` (must, estimate): Impact fees: water $2,325 + wastewater $3,300 + roadway ~$4,000 (to $6,000) — source: [City of College Station - Water and Wastewater Impact Fees table](https://www.cstx.gov/media/zw4iubt5/water-and-wastewater-impact-fees.pdf)
- … and 28 more in the city files.

## flood-elevation

**Flood elevation / freeboard.** If the lot is in or near a floodplain, raise the finished floor: e.g. BFE + 1 ft, BFE + 2 ft, 500-yr + 2 ft (Houston), fully-developed-watershed BFE + 18 in (Denton). Changes slab height, steps, foundation type (no fill / piers in V zones) and cost.

- **Survey input:** Address -> FEMA/city flood zone; BFE if known; distance to floodplain.
- **Cities (30):** arlington, austin, beaumont, brownsville, college-station, conroe, corpus-christi, cypress-unincorporated-harris, dallas, denton, garland, houston, irving, katy, kyle, laredo, league-city, lubbock, mcallen, mckinney, midland, new-braunfels, pearland, pflugerville, plano, round-rock, san-antonio, sugar-land, texas-baseline, texas-unincorporated, tyler, waco
- **Priority mix:** 22 must, 10 should, 0 nice
- **Data sketch:**

```json
{"zones": ["AE","X-shaded"], "datum": "500yr|BFE|fullyDevelopedBFE", "freeboardFt": 2, "noFill": true, "appliesWithinFtOfFloodplain": 200}
```

Examples from the city files:

- `arlington` (must, survey): In floodplain set lowest floor and finished garage 2 ft above fully urbanized BFE (not FEMA effective BFE). — source: [City of Arlington Flood Damage Prevention Chapter (code of ordinances PDF), Sec.](https://www.arlingtontx.gov/files/assets/city/v/3/city-secretary/documents/city-code-of-ordinances/flood-damage-prevention-chapter.pdf)
- `austin` (must, foundation): If in Austin regulatory floodplain (old FEMA 500-yr), lowest floor >= 100-yr WSE + 2 ft — source: [City of Austin Watershed - Atlas 14 Summary of Code Changes](https://www.austintexas.gov/sites/default/files/files/Watershed/flood/Atlas_14_Summary_of_Code_Changes.pdf)
- `beaumont` (must, foundation): Require FEMA flood zone/BFE input; if in SFHA set lowest floor >= BFE + 1 ft (assumed) and elevation certificate — source: Assumed
- `brownsville` (must, survey): If in SFHA: lowest floor >= BFE + 1 ft (assumed) — source: Assumed - agent judgement (no source found within wave-2 search budget)
- `college-station` (must, survey): If in SFHA, finished floor >= BFE + 1 ft; two elevation certificates — source: [City of College Station - Floodplains (Engineering)](https://cstx.gov/departments___city_hall/pds/engineering/floodplains)
- `conroe` (must, foundation): Finished floor >= BFE + 1.0 ft (surveyed) in SFHA. — source: [City of Conroe - Flood Safety Information (Engineering/Floodplain Management)](https://cms3.revize.com/revize/conroetx/Documents/Services/Engineering/Floodplain%20Management/Flood%20Safety/Flood%20Safety%20Information%20B.pdf)
- … and 26 more in the city files.

## permit-fee-formula

**Permit and plan-review fee.** Compute the building permit and plan-review fee from the city formula (per sq ft, flat, or tiered; Texas bars value-based residential fees, LGC 214.907).

- **Survey input:** Conditioned + garage + porch areas from the plan.
- **Cities (27):** amarillo, arlington, austin, beaumont, college-station, corpus-christi, dallas, denton, el-paso, garland, georgetown, houston, hutto, irving, kyle, laredo, league-city, little-elm, lubbock, mcallen, pearland, plano, prosper, round-rock, sugar-land, tyler, waco
- **Priority mix:** 3 must, 23 should, 1 nice
- **Data sketch:**

```json
{"type": "perSqFt", "rate": 0.41, "areaBasis": "under roof", "planReview": {"type": "pctOfPermit", "pct": 0.5}, "min": 50}
```

Examples from the city files:

- `amarillo` (should, estimate): Building permit $0.45/sf (2019 rate) — source: [NewsChannel 10: New state law requires change in Amarillo's building permit fee ](https://www.newschannel10.com/2019/06/04/new-state-law-requires-change-amarillos-building-permit-fee/)
- `arlington` (must, estimate): Permit by sq ft tiers (Table 2: $0.80 up to 1,200; $0.64 1,201-2,000) + 35% plan review. — source: [City of Arlington Planning and Development Services Fee Schedule (Exhibit A, 9-1](https://www.arlingtontx.gov/files/assets/city/v/1/planning-and-development-services/documents/permitting-amp-inspections/fee-schedule-9-1-25.pdf)
- `austin` (should, estimate): Plan review fee tier by sq ft ($1,141 for 2,001-3,000 sf) + 6% surcharge; other permit fees TBD — source: [City of Austin - Fees Residential (PDF)](https://austintexas.gov/sites/default/files/files/Development_Services/Fees_Residential.pdf)
- `beaumont` (should, estimate): Building permit = $0.50 x sq ft (min $55) + $150 plan review + $10 usage; MEP permits separate. — source: [COB Residential Building Permit Fee Schedule 2024](https://www.beaumonttexas.gov/DocumentCenter/View/2179/COB-Residential-Building-Permit-Fee-Schedule-2024)
- `college-station` (should, estimate): Building permit = $0.74 x sq ft (assume under roof) — source: [City of College Station - FY26 Planning & Development Services fee schedule](https://www.cstx.gov/media/vy2i0xpy/fy26-pds-fees.pdf)
- `corpus-christi` (should, estimate): Permit = sq ft x ($0.461 + $0.146) (FY2025), min $146.41 — source: [FY 2025 Development Fee Schedule](https://corpuschristitx.gov/media/wkljgujc/fy-2025-development-fee-schedule.pdf)
- … and 21 more in the city files.

## height-limit

**Height limit.** Maximum building height (ft and stories), measured per city definition; massing engine must check.

- **Survey input:** District.
- **Cities (26):** arlington, austin, brownsville, cedar-park, college-station, corpus-christi, dallas, el-paso, fort-worth, frisco, georgetown, hutto, katy, killeen, kyle, laredo, little-elm, lubbock, mcallen, new-braunfels, pflugerville, plano, prosper, san-antonio, sugar-land, tyler
- **Priority mix:** 16 must, 10 should, 0 nice
- **Data sketch:**

```json
{"maxFt": 35, "maxStories": 2.5, "measure": "mean roof height"}
```

Examples from the city files:

- `arlington` (must, massing): Cap height at 40 ft in RS-7.2. — source: [City of Arlington Unified Development Code Chapter (code of ordinances PDF), Sec](https://www.arlingtontx.gov/files/assets/city/v/8/city-secretary/documents/city-code-of-ordinances/unified-development-code-chapter.pdf)
- `austin` (must, massing): Max height 35 ft (32 ft inside Subchapter F boundary) — source: [Neuhaus RE - Complete Guide to Zoning and Land Use in Austin (2026)](https://neuhausre.com/guides/zoning-land-use-guide-austin/)
- `brownsville` (should, massing): Max height 35 ft — source: [Brownsville TX building setbacks (third-party summary)](https://cityrulelookup.com/cities/brownsville-tx/building-setbacks)
- `cedar-park` (must, massing): Max height 35 ft (SU) — source: [Cedar Park TX UDC Chapter 11 - Table 11.03.061A Single-Family Residential Lot an](https://www.zoneomics.com/code/cedar-park-TX/chapter_3)
- `college-station` (must, massing): GS max 2.5 stories / 35 ft — source: [College Station UDO Article 5 - District Purpose Statements and Supplemental Sta](https://library.municode.com/tx/college_station/codes/code_of_ordinances?nodeId=SPBLADEOR_APXAUNDEOR_ART5DIPUSTSUST)
- `corpus-christi` (should, massing): Max height 35 ft (average grade to highest roof point) — source: [Corpus Christi setbacks & height (beta third-party guide)](https://zoning.buildingclub.info/texas/corpus-christi/setbacks-height)
- … and 20 more in the city files.

## survey-input-district

**Ask for district / PD / plat.** Most new Texas homes sit in a Planned Development (PD/PUD) or a platted subdivision whose own standards override the base district. Ask the user for the district or PD name, or to upload the plat; otherwise use the base district with a warning.

- **Survey input:** District or PD name; plat (optional upload); HOA yes/no.
- **Cities (25):** amarillo, arlington, cedar-park, celina, college-station, conroe, dallas, denton, forney, frisco, garland, georgetown, hutto, irving, katy, kyle, leander, little-elm, mckinney, midland, new-braunfels, pflugerville, prosper, round-rock, sugar-land, texas-unincorporated
- **Priority mix:** 21 must, 6 should, 0 nice
- **Data sketch:**

```json
{"askDistrict": true, "basedistrictFallback": "SF-7", "pdCommon": true}
```

Examples from the city files:

- `amarillo` (must, survey): Ask user for district (R-1/R-2/R-3) and plat setbacks; provisional R-2: front 25, side 5, rear unknown, height 35 ft — source: [CityRuleLookup - Building setbacks rules in Amarillo TX (cites Ch. 4-10, Sec. 4-](https://cityrulelookup.com/blog/building-setbacks-rules-in-amarillo-tx)
- `arlington` (must, survey): Ask for the actual zoning district (default RS-7.2) and plat building lines; no setbacks verified yet, so do not auto-fill. — source: Assumed - researcher judgement (not verified this session)
- `cedar-park` (should, survey): Ask user for district (SU/SR/ES or PUD) and plat building lines; values from Zoneomics copy of UDC — source: [Cedar Park TX UDC Chapter 11 - Table 11.03.061A Single-Family Residential Lot an](https://www.zoneomics.com/code/cedar-park-TX/chapter_3)
- `celina` (must, survey): Ask for the lot's PD ordinance; most new Celina lots are PDs on an SF-R base. Use PD Area Regulations; if unknown use example-PD defaults front 20 / side 5 / corner side 15 / rear 20 ft and flag for confirmation. — source: [Celina - Sutton Fields Planned Development ordinance (DocumentCenter/View/2987)](https://www.celina-tx.gov/DocumentCenter/View/2987)
- `college-station` (must, survey): Ask district (GS/RS/E/R/MH/PDD) and overlay (NCO, ROO); NCO may override setbacks/height/coverage — source: [City of College Station - Single Family Overlay Districts](https://www.cstx.gov/departments___city_hall/pds/planning/single_family_overlay_districts)
- `conroe` (should, drawings): Default 2021 IRC/IECC CZ 2A, NEC 2023, flagged unverified. — source: [PermitMint - How to Get a Generator Permit in Conroe, TX (2026 Guide) (lists 202](https://permitmint.com/guides/generator/texas/conroe/)
- … and 21 more in the city files.

## electrical-code-edition

**Electrical code edition.** NEC edition for electrical checks (state default NEC 2026 from 2026-09-01; many cities still cite 2020 or 2023).

- **Survey input:** City.
- **Cities (24):** amarillo, beaumont, cedar-park, college-station, cypress-unincorporated-harris, dallas, forney, fort-worth, garland, georgetown, houston, hutto, irving, katy, kyle, laredo, leander, lubbock, midland, new-braunfels, pearland, plano, round-rock, san-antonio, texas-baseline, texas-unincorporated
- **Priority mix:** 8 must, 15 should, 3 nice
- **Data sketch:**

```json
{"nec": "2023", "stateDefault": "2026"}
```

Examples from the city files:

- `amarillo` (should, drawings): Electrical per NEC 2023 (IRC Part VIII excluded) — source: [City of Amarillo - Building Safety (adopted codes and local amendment ordinances](https://www.amarillo.gov/building-safety/)
- `beaumont` (should, drawings): Use 2021 IRC/IECC and NEC 2020 for Beaumont plan notes; include ICC 600 high-wind provisions where used. — source: [City of Beaumont Commercial and Residential Accessory Building Permit Checklist ](https://www.beaumonttexas.gov/DocumentCenter/View/4134/Commercial-and-Residential-Accessory-Building-Permit-Checklist)
- `cedar-park` (must, drawings): Use 2021 IRC (appendices AA,AB,AC,AE,AG,AH,AJ,AK,AN,AP), 2021 IECC, 2021 IPC, NEC 2020 — source: [City of Cedar Park Code of Ordinances - Chapter 3 Building Regulations (code ado](https://ecode360.com/38594319)
- `college-station` (should, plan): Electrical to NEC 2023 — source: [City of College Station - Building Codes (adopted codes, eff. 2026-01-01)](https://www.cstx.gov/living-here/building-and-renovating/building-codes/)
- `cypress-unincorporated-harris` (should, drawings): Electrical per NEC 2026 from 2026-09-01 — source: [TDLR - Commission adopts rules (16 TAC 73.100, 2026 NEC)](https://www.tdlr.texas.gov/news/rulemaking/2026/09/01/commission-adopts-rules-12/)
- `dallas` (should, drawings): Use NEC 2020 with Dallas amendments (not 2023) for electrical notes. — source: [City of Dallas Building Inspection - Current City Code (construction codes list)](https://dallascityhall.com/departments/sustainabledevelopment/buildinginspection/Pages/know_code.aspx)
- … and 20 more in the city files.

## lot-min-size

**Minimum lot size / width.** Check the lot against district minimum area, width and depth; warn if non-conforming.

- **Survey input:** Lot dimensions (already in survey) + district.
- **Cities (22):** arlington, austin, brownsville, college-station, corpus-christi, dallas, el-paso, fort-worth, frisco, houston, killeen, laredo, league-city, little-elm, lubbock, new-braunfels, pearland, pflugerville, plano, san-antonio, sugar-land, texas-baseline, tyler
- **Priority mix:** 0 must, 22 should, 1 nice
- **Data sketch:**

```json
{"minSqFt": 7000, "minWidthFt": 60, "minDepthFt": 100}
```

Examples from the city files:

- `arlington` (should, survey): RS-7.2 minimum lot 7,200 sf, 60 ft wide, 100 ft deep. — source: [City of Arlington Unified Development Code Chapter (code of ordinances PDF), Sec](https://www.arlingtontx.gov/files/assets/city/v/8/city-secretary/documents/city-code-of-ordinances/unified-development-code-chapter.pdf)
- `austin` (should, survey): Accept lots >= 1,800 sq ft and >= 15 ft wide for one small-lot SF home (HOME Phase 2) — source: [City of Austin - HOME Amendments page](https://www.austintexas.gov/development-services/home-amendments)
- `brownsville` (should, survey): R-1 min lot 5,000 sf, 50 ft wide, 70 ft deep — source: [Brownsville TX code Chapter 3 (zoning districts) - Zoneomics mirror](https://www.zoneomics.com/code/brownsville-TX/chapter_3)
- `college-station` (should, survey): GS min lot 5,000 sf, 50 ft wide, 100 ft deep — source: [City of College Station - GS General Suburban zoning district fact sheet](https://www.cstx.gov/media/5sti0f32/gs.pdf)
- `corpus-christi` (should, survey): RS-6 minimum lot 6,000 sq ft — source: [Printable step-by-step zoning guide (district names = min lot size)](https://corpuschristitx.gov/media/gsgg4nwx/printable-step-by-step.pdf)
- `dallas` (should, survey): Warn if the lot is smaller than 7,500 sq ft in R-7.5(A) (legal nonconforming lots may still build). — source: [City of Dallas Current Planning - R-7.5(A) Single Family District summary](https://dallascityhall.com/departments/sustainabledevelopment/planning/Pages/R75A.aspx)
- … and 17 more in the city files.

## masonry-percentage

**Masonry percentage.** City masonry % mandates are largely pre-empted (Gov't Code ch. 3000), so the engine applies none by default but asks about HOA / deed / PD masonry rules; if given, add brick/stone veneer to wall sections and estimate.

- **Survey input:** HOA/PD masonry % (user input).
- **Cities (17):** arlington, beaumont, celina, dallas, denton, forney, fort-worth, frisco, garland, irving, little-elm, mckinney, plano, prosper, sugar-land, texas-baseline, tyler, waco
- **Priority mix:** 0 must, 15 should, 3 nice
- **Data sketch:**

```json
{"cityRequirement": null, "preempted": true, "userHoaPct": 0.8, "appliesTo": "first floor|all"}
```

Examples from the city files:

- `arlington` (should, envelope): Do not apply a city masonry percentage (Gov't Code ch. 3000); prompt for HOA, deed or historic-district requirements. — source: [HB 2439 (2019) staff summary - Fort Worth Development Services (Gov't Code ch. 3](https://www.fortworthtexas.gov/files/assets/public/v/1/development-services/documents/housebill-2439.pdf)
- `beaumont` (should, envelope): Do not apply any city-mandated masonry %; only flag HOA/deed restriction check — source: [Texas Government Code Ch. 3000 (building products, materials, methods; HB 2439, ](https://statutes.capitol.texas.gov/Docs/GV/htm/GV.3000.htm)
- `celina` (should, envelope): Do not enforce city masonry %; prompt for PD/HOA masonry requirement. — source: [Texas Government Code Ch. 3000 (building products, materials, methods; HB 2439, ](https://statutes.capitol.texas.gov/Docs/GV/htm/GV.3000.htm)
- `dallas` (should, envelope): Do not apply any masonry percentage by default (Gov't Code ch. 3000). Show a prompt only if the lot is in a historic district or a PD or deed restriction requires masonry. — source: [HB 2439 (2019) staff summary - Fort Worth Development Services (Gov't Code ch. 3](https://www.fortworthtexas.gov/files/assets/public/v/1/development-services/documents/housebill-2439.pdf)
- `denton` (nice, envelope): No city masonry %; check HOA/deed restrictions. — source: Assumed (Texas HB 2439, 86th Leg. 2019, Gov't Code ch. 3000 - not fetched)
- `forney` (should, envelope): Do not apply any city-mandated masonry %; only flag HOA/deed restriction check — source: [Texas Government Code Ch. 3000 (building products, materials, methods; HB 2439, ](https://statutes.capitol.texas.gov/Docs/GV/htm/GV.3000.htm)
- … and 12 more in the city files.

## building-line-plat

**Plat building line.** Use plat building lines as setbacks where there is no zoning (Houston Ch. 42, Conroe, unincorporated) or where they exceed the district.

- **Survey input:** Plat building line values (user) or default.
- **Cities (13):** beaumont, cedar-park, conroe, forney, georgetown, houston, killeen, leander, mcallen, plano, round-rock, texas-unincorporated, tyler, waco
- **Priority mix:** 9 must, 5 should, 0 nice
- **Data sketch:**

```json
{"frontFt": 20, "garageFt": 19, "source": "plat"}
```

Examples from the city files:

- `beaumont` (must, survey): Read platted building lines from the recorded plat; they override district defaults when larger — source: Assumed
- `cedar-park` (should, survey): Most new homes are in PUDs/MUDs or HOA subdivisions - plat building lines, PUD standards and deed restrictions may override district setbacks and add masonry rules — source: Assumed
- `conroe` (must, survey): Read front/side building lines from recorded subdivision plat (Ch. 94). — source: [Building setbacks rules in Conroe TX (third-party summary: Ch. 94 subdivision, C](https://cityrulelookup.com/blog/building-setbacks-rules-in-conroe-tx)
- `forney` (must, survey): Read platted building lines from the recorded plat; they override district defaults when larger — source: Assumed
- `georgetown` (should, survey): Most new homes are in PUDs/MUDs or HOA subdivisions - plat building lines, PUD standards and deed restrictions may override district setbacks and add masonry rules — source: Assumed
- `houston` (must, setbacks): Front building line 20 ft on local street (default); 25 ft on major thoroughfare; allow optional 10 ft principal-structure line only if user confirms Sec. 42-157 performance standards / plat shows it — source: [Houston Code of Ordinances Ch. 42 Art. III Div. 3 Building Lines (Municode)](https://library.municode.com/tx/houston/codes/code_of_ordinances/312514?nodeId=COOR_CH42SUDEPL_ARTIIIPLST_DIV3BULI_SDAGEREBULI)
- … and 8 more in the city files.

## deed-restriction-check

**Deed restriction / HOA check.** Prompt for deed restrictions and HOA rules (often stricter than the city: masonry, roof, size, setbacks). Houston enforces deed restrictions as city law.

- **Survey input:** Yes/no + key values or upload.
- **Cities (11):** celina, cypress-unincorporated-harris, fort-worth, frisco, houston, katy, league-city, mckinney, pearland, prosper, sugar-land, texas-baseline, texas-unincorporated
- **Priority mix:** 3 must, 10 should, 0 nice
- **Data sketch:**

```json
{"ask": true, "fields": ["masonryPct","minSqFt","buildingLines","roof"]}
```

Examples from the city files:

- `celina` (should, survey): Check HOA/deed restrictions and platted building lines. — source: Assumed - agent judgement (no source could be read this session)
- `cypress-unincorporated-harris` (must, survey): Master-planned community ACC: masonry %, garage orientation, roof pitch, min house size — source: Assumed - prior knowledge, not verified at source this session
- `fort-worth` (should, survey): Ask for HOA/deed restrictions (often impose masonry %, minimum size, garage orientation in new Fort Worth subdivisions). — source: Assumed (no source reachable this session)
- `frisco` (should, survey): Check HOA/deed restrictions and platted building lines; typical Frisco HOAs control masonry, roof pitch, garage orientation and minimum size. — source: Assumed - agent judgement (no source could be read this session)
- `houston` (must, survey): Prompt user for recorded deed restrictions/HOA rules (setbacks, single-family use, masonry, height, fences); they override Chapter 42 when stricter and the City enforces them; flag affidavit at permit — source: [City of Houston Legal Department - Deed Restrictions](https://houstontx.gov/legal/deed.html)
- `katy` (should, survey): Prompt for HOA/deed restrictions (masonry %, setbacks, garage orientation) - common in master-planned subdivisions here — source: Assumed - regional practice
- … and 7 more in the city files.

## lot-coverage

**Lot (building) coverage.** Cap building footprint / lot area.

- **Survey input:** District.
- **Cities (10):** arlington, austin, brownsville, celina, college-station, dallas, el-paso, fort-worth, sugar-land, tyler
- **Priority mix:** 6 must, 3 should, 1 nice
- **Data sketch:**

```json
{"maxFraction": 0.45}
```

Examples from the city files:

- `arlington` (must, massing): Limit lot coverage to 50% in RS-7.2. — source: [City of Arlington Unified Development Code Chapter (code of ordinances PDF), Sec](https://www.arlingtontx.gov/files/assets/city/v/8/city-secretary/documents/city-code-of-ordinances/unified-development-code-chapter.pdf)
- `austin` (must, massing): Building coverage max 40% of lot — source: [City of Austin Board of Adjustment staff report citing 25-2-492 SF-3 limits](https://services.austintexas.gov/edims/document.cfm?id=440463)
- `brownsville` (must, massing): Max lot coverage 50% including accessory buildings — source: [Brownsville TX code Chapter 3 (zoning districts) - Zoneomics mirror](https://www.zoneomics.com/code/brownsville-TX/chapter_3)
- `celina` (nice, massing): Note 20% open space requirement applies at district/subdivision level (half usable); do not apply as a per-lot coverage cap unless PD says so. — source: [Celina TX Zoning Ordinance Art. 14.02 (Zoneomics mirror): SF-E, SF-R (Sec. 14.02](https://www.zoneomics.com/code/celina-TX/chapter_2)
- `college-station` (should, massing): If NCO overlay: load overlay limits (e.g. McCulloch NCO: 1 story, 41% coverage incl. parking) — source: [City of College Station - Single Family Overlay Districts](https://www.cstx.gov/departments___city_hall/pds/planning/single_family_overlay_districts)
- `dallas` (must, massing): Limit lot coverage to 45% for residential structures in R-7.5(A). — source: [City of Dallas Current Planning - R-7.5(A) Single Family District summary](https://dallascityhall.com/departments/sustainabledevelopment/planning/Pages/R75A.aspx)
- … and 4 more in the city files.

## garage-placement

**Garage placement and door width.** Garage must sit at a building line (e.g. Houston 19-20 ft; Lubbock 20 ft) or limit street-facing door width (Killeen 50% of facade, Arlington proposed 55%).

- **Survey input:** Lot orientation, street side; garage entry choice.
- **Cities (10):** arlington, fort-worth, frisco, georgetown, houston, hutto, killeen, leander, lubbock, san-antonio
- **Priority mix:** 2 must, 6 should, 2 nice
- **Data sketch:**

```json
{"minSetbackFt": 20, "maxDoorShareOfFacade": 0.5}
```

Examples from the city files:

- `arlington` (should, plan): Front-facing garage: apply UDC 4.1.6.G garage setback; keep garage openings <= 55% of house width (proposed 2025). — source: [City of Arlington Unified Development Code Annual Update 2025 (proposed amendmen](https://www.arlingtontx.gov/files/assets/city/v/2/planning-and-development-services/documents/zoning-unified-development-code/annual-udc-updates-2025.pdf)
- `fort-worth` (should, plan): Allow attached garage side setback 3 ft only if garage is >=18 ft behind front wall; detached garage behind rear wall may be 3 ft from lot line. — source: [Fort Worth Zoning Ordinance § 4.705 One-Family ("A-5") District](https://codelibrary.amlegal.com/codes/ftworth/latest/ftworth_tx/0-0-0-35059)
- `frisco` (should, plan): On front-entry (non-alley) lots apply Frisco Front Entry Lot Layout Guidelines - prefer J-swing/side-entry or recessed front garage; alley lots: rear garage 20 ft from alley (24 ft for swing-in). Treat as warning until PD/guideline values loaded. — source: [Single-Family Front Entry Lot Layout Guidelines (Feb 20, 2013)](https://friscotexas.gov/DocumentCenter/View/1002/Single-Family-Front-Entry-Lot-Layout-Guidelines-PDF?bidId=)
- `georgetown` (nice, plan): Provisional: set front-loaded garage door >= 25 ft from front property line / street ROW — source: Assumed
- `houston` (must, setbacks): When 10 ft principal line is used, street-facing garage/carport face must be >= 19 ft from property line (use 20 ft to be conservative); >=1/3 of street frontage of building must be habitable; single driveway approach <= 12 ft on narrow lots — source: [City of Houston Planning and Development Department plat notes (October 23, 2024](https://www.houstontx.gov/planning/DevelopRegs/docs_pdfs/ORD_NOTE.pdf)
- `hutto` (nice, plan): If new UDC N-1 applies: front-entry garage door >= 24 ft from front line — source: [Hutto Unified Development Code DRAFT 5/15/2025](https://www.huttotx.gov/DocumentCenter/View/5872/Hutto_UDC_DRAFT_05152025)
- … and 4 more in the city files.

## windstorm-package

**Windstorm package (TDI).** In TDI catalogue counties: design to the TDI-adopted code (2024 IRC from 2026-04-01) and the mapped wind speed, protect openings in the wind-borne debris region, specify roof deck nailing, uplift straps and continuous load path, engineer inspections and WPI-8 certificate. Adds estimate lines and drawing notes.

- **Survey input:** Address -> county/TDI area (Seaward/Inland I/Inland II).
- **Cities (9):** beaumont, brownsville, conroe, corpus-christi, houston, katy, league-city, pearland, sugar-land, texas-baseline
- **Priority mix:** 11 must, 3 should, 2 nice
- **Data sketch:**

```json
{"tdiArea": "Inland I", "designWindMph": 150, "debrisRegion": true, "openings": "impact-rated|shutters", "certificate": "WPI-8", "estimate": ["straps","impact windows","engineer inspections"]}
```

Examples from the city files:

- `beaumont` (must, structure): Apply TDI windstorm package for Inland II zone: design to 143 mph Vult (ASCE 7-10 equiv. of 110 mph) - re-check under 2024 IRC/ASCE 7-22 for certifications after 1 Apr 2026; ICC 600 high-wind prescriptive option; engineer windstorm certification and WPI-8; continuous load path. — source: [TDI Windstorm - Jefferson County wind zone page (Beaumont = Inland II, 110 mph 3](https://tdi.texas.gov/wind/maps/jefferso.html)
- `brownsville` (must, structure): TDI windstorm (TWIA) package: on/after Apr 1, 2026 design and build to the 2024 IRC as adopted by TDI (28 TAC 5.4013); a TDI-appointed qualified inspector or Texas PE must certify, TDI issues WPI-8 Certificate of Compliance needed for TWIA insurance. Brownsville = legacy Inland I (TDI note). — source: [TDI adopted rule: 28 TAC 5.4013 and amendments adopting 2024 IRC/IBC for TWIA-in](https://tdi.texas.gov/rules/2025/documents/20269774.pdf)
- `brownsville` (must, envelope): Wind-borne debris region: all exterior glazed openings (windows, glass doors, skylights) impact-rated or protected by tested shutters/approved panels; garage doors wind-rated. — source: [TDI Windstorm Inspection Program - general information](https://tdi.texas.gov/WIND/geninfo.html)
- `brownsville` (should, structure): 2024 IRC enhanced roof deck protection / sheathing attachment in wind-design-required areas (Vult >= 130 mph): spec sealed roof deck underlayment and high-wind sheathing nailing; engineer to confirm schedule. — source: [TDI Windstorm Transition to the 2024 IRC: What Texas Builders Need to Know](https://arcxis.com/technical-bulletin/tdi-windstorm-transition-to-the-2024-irc-what-texas-builders-need-to-know)
- `conroe` (must, structure): Do NOT add TDI windstorm package (Montgomery County not designated). — source: [TDI - TWIA insurability requirements (designated catastrophe areas)](https://tdi.texas.gov/WIND/documents/TWIAInsurabilityRequirementsFinal.pdf)
- `corpus-christi` (must, structure): TDI windstorm (TWIA) package: on/after Apr 1, 2026 design and build to the 2024 IRC as adopted by TDI (28 TAC 5.4013); a TDI-appointed qualified inspector or Texas PE must certify, TDI issues WPI-8 Certificate of Compliance needed for TWIA insurance. Mainland Corpus Christi = legacy Inland I; Padre/Mustang Island = Seaward (legacy zones, informational only). — source: [TDI adopted rule: 28 TAC 5.4013 and amendments adopting 2024 IRC/IBC for TWIA-in](https://tdi.texas.gov/rules/2025/documents/20269774.pdf)
- … and 10 more in the city files.

## plumbing-code-variant

**Plumbing code variant.** IPC vs UPC (Houston, Austin use UPC) changes fixture/vent rules and notes.

- **Survey input:** City.
- **Cities (8):** arlington, austin, dallas, fort-worth, frisco, houston, laredo, round-rock, texas-baseline
- **Priority mix:** 1 must, 4 should, 4 nice
- **Data sketch:**

```json
{"code": "UPC", "edition": 2021}
```

Examples from the city files:

- `arlington` (nice, drawings): Assume the NCTCOG regional amendments to the 2021 IRC and IECC (Chapter 11 deleted and replaced by the IECC; carport exception) until the city ordinance is confirmed. — source: [NCTCOG Recommended Amendments to the 2021 International Residential Code (Approv](https://nctcog.org/getmedia/feafbc55-3c35-4022-bcab-6b07c95c7f9e/2021-IRC-Amendments-Final.pdf)
- `austin` (should, drawings): Plumbing per UPC (IAPMO) not IPC — source: Assumed (agent judgement) - Austin historically adopts UPC; edition not verified
- `dallas` (should, plan): Use IPC 2021 (Dallas amendments) rules for fixtures and venting, not UPC. — source: [City of Dallas Building Inspection - Current City Code (construction codes list)](https://dallascityhall.com/departments/sustainabledevelopment/buildinginspection/Pages/know_code.aspx)
- `fort-worth` (nice, drawings): Plumbing per 2021 IPC/IFGC (not UPC). — source: [Building & Energy Codes (Development Services)](https://www.fortworthtexas.gov/departments/development-services/permits/building-energy-codes)
- `frisco` (nice, drawings): Plumbing per 2024 IPC (Frisco amended); electrical per 2023 NEC. — source: [City of Frisco Ordinance No. 2026-01-08 (2024 International Plumbing Code)](https://www.friscotexas.gov/DocumentCenter/View/39095/2024-International-Plumbing-Code-IPC-PDF)
- `houston` (must, drawings): Use UPC 2021 (and UMC 2021) instead of IRC plumbing/mechanical chapters for fixture/venting/DWV sizing — source: [Houston adopts 2021 UPC and UMC (IAPMO release 2023-10-26)](https://www.iapmo.org:443/media/31938/2023-10-26-houston-adopts-2021-upc-umc.pdf)
- … and 3 more in the city files.

## wind-speed

**Design wind speed.** Set ultimate design wind speed from the IRC map or city Table R301.2(1).

- **Survey input:** Address (county).
- **Cities (7):** brownsville, corpus-christi, cypress-unincorporated-harris, el-paso, houston, league-city, lubbock
- **Priority mix:** 3 must, 4 should, 0 nice
- **Data sketch:**

```json
{"vultMph": 115, "exposure": "B"}
```

Examples from the city files:

- `brownsville` (must, structure): Use basic (ultimate) design wind speed 150 mph for TDI windstorm areas under the 2024 IRC R301.2.1 (per City of Corpus Christi summary of TDI adoption); Risk Category II; exposure C, check D near open water/bays. — source: [City of Corpus Christi bulletin: TDI Windstorm update to 2024 ICC codes (effecti](https://www.corpuschristitx.gov/media/iiflluoc/tdi-windstorm-update-to-2024-icc-codes.pdf)
- `corpus-christi` (must, structure): Use basic (ultimate) design wind speed 150 mph for TDI windstorm areas under the 2024 IRC R301.2.1 (per City of Corpus Christi summary of TDI adoption); Risk Category II; exposure C, check D near open water/bays. — source: [City of Corpus Christi bulletin: TDI Windstorm update to 2024 ICC codes (effecti](https://www.corpuschristitx.gov/media/iiflluoc/tdi-windstorm-update-to-2024-icc-codes.pdf)
- `cypress-unincorporated-harris` (should, structure): Design wind ~130 mph (non-windstorm area) — source: Assumed - prior knowledge, not verified at source this session
- `el-paso` (should, structure): Design wind speed 115 mph (local table; 2015-era value, verify 2021 table) — source: [El Paso Code of Ordinances §18.10.050 Section R301.2 Climatic and geographic des](http://elpaso-tx.elaws.us/code/coor_title18_ch18.10_sec18.10.050)
- `houston` (should, structure): Get Vult by address lookup (Houston amendment); default 140 mph Risk II if lookup unavailable — source: [Houston Amendments to the 2021 International Residential Code for One- and Two-F](https://www.houstonpermittingcenter.org/media/9056/download)
- `league-city` (must, structure): Set design wind speed ~150-155 mph ultimate (verify by address). — source: [TDI Windstorm newsletter 2018 (ASCE 7-10 ultimate speed equivalents)](https://tdi.texas.gov/WIND/documents/newsletter22018 .pdf)
- … and 1 more in the city files.

## fire-sprinkler

**Fire sprinkler rule.** Texas bars city sprinkler mandates for 1-2 family homes (LGC 250.011) except pre-2009 rules (Frisco >= 6,000 sf; Plano R325). Add sprinkler cost when triggered.

- **Survey input:** Total floor area incl. garage.
- **Cities (7):** celina, cypress-unincorporated-harris, el-paso, frisco, mckinney, plano, prosper, texas-baseline, texas-unincorporated
- **Priority mix:** 3 must, 3 should, 3 nice
- **Data sketch:**

```json
{"required": false, "triggerSqFt": 6000, "grandfathered": true}
```

Examples from the city files:

- `celina` (nice, plan): Do not add a residential sprinkler mandate (state preemption) unless city shows a pre-2009 grandfathered rule. — source: [HB 738: Texas Adopts 2012 Versions of IRC and IBC; Addresses Residential Fire Sp](https://www.allensworthlaw.com/legal-updates/hb-738/)
- `cypress-unincorporated-harris` (should, plan): No sprinklers — source: [87(R) HB 738 Enrolled - Bill Text (IRC/IBC 2012 base dates; LGC 250.011 sprinkle](https://www.legis.state.tx.us/tlodocs/87R/billtext/html/HB00738F.HTM)
- `el-paso` (should, plan): Do not require residential fire sprinklers (R313 deleted locally) — source: [El Paso ordinance adopting International Residential Code with local amendments ](https://www2.elpasotexas.gov/municipal-clerk/agenda/07-20-10/07201011B-c.pdf)
- `frisco` (must, plan): If conditioned area + garage area >= 6,000 sq ft, require automatic fire sprinkler system (Frisco Fire Prevention approval) and add cost. — source: [Residential Submittal Guide, Frisco, Texas](https://www.friscotexas.gov/DocumentCenter/View/852/Residential-Submittal-Guideline-PDF)
- `mckinney` (nice, plan): Do not add a residential sprinkler mandate (state preemption) unless city shows a pre-2009 grandfathered rule. — source: [HB 738: Texas Adopts 2012 Versions of IRC and IBC; Addresses Residential Fire Sp](https://www.allensworthlaw.com/legal-updates/hb-738/)
- `plano` (must, plan): Plano retains local IRC Sec. R325 residential sprinkler rule (grandfathered pre-2009). Flag possible NFPA 13D system and ask user to confirm trigger with Plano Building Inspections; add sprinkler allowance to estimate when triggered. — source: [City of Plano ordinance adopting the 2024 International Residential Code with lo](https://content.civicplus.com/api/assets/tx-plano/6a2b7a22-3b2f-41c5-844b-6f5d6bb15067)
- … and 3 more in the city files.

## impervious-cover

**Impervious cover.** Cap all hard surfaces (roof + driveway + patios) / lot area; also Edwards Aquifer limits.

- **Survey input:** District; aquifer zone (address).
- **Cities (7):** austin, cedar-park, georgetown, kyle, leander, new-braunfels, san-antonio
- **Priority mix:** 1 must, 5 should, 1 nice
- **Data sketch:**

```json
{"maxFraction": 0.45, "includes": ["roof","driveway","patio"]}
```

Examples from the city files:

- `austin` (must, plan): Impervious cover max 45% (house+garage+driveway+patios); watershed rules may be lower — source: [City of Austin Board of Adjustment staff report citing 25-2-492 SF-3 limits](https://services.austintexas.gov/edims/document.cfm?id=440463)
- `cedar-park` (should, survey): Check TCEQ Edwards map: recharge/contributing zone homes fall under 30 TAC 213; confirm the subdivision has an approved WPAP/CZP, else individual plan needed — source: [TCEQ - Edwards Aquifer: Private Residences](https://www.tceq.texas.gov/permitting/eapp/edwards-aquifer-private-residences)
- `georgetown` (should, survey): Check TCEQ Edwards Aquifer map: lots on recharge zone fall under 30 TAC 213 (WPAP at subdivision level; single-family on lots > 5 ac one home exempt); city UDC Ch.13 impervious cover limits apply city+ETJ - read plat impervious cover allocation per lot — source: [Georgetown TX UDC - Environmental Protection (Zoneomics copy)](https://www.zoneomics.com/code/georgetown-TX/chapter_13)
- `kyle` (should, survey): West Kyle lots may be on Edwards recharge/contributing zone: check TCEQ map; 30 TAC 213 applies to private residences unless covered by subdivision-approved plan (or lot > 5 ac, 1 home) — source: [TCEQ - Edwards Aquifer: Private Residences](https://www.tceq.texas.gov/permitting/eapp/edwards-aquifer-private-residences)
- `leander` (should, survey): Much of west Leander is over the Edwards Aquifer recharge/contributing zone: subdivisions file TCEQ WPAPs under 30 TAC 213 (e.g. Edgewood Ph1). Check map; follow plat impervious-cover allocations and WPAP BMPs; lot-level single-family usually covered by the subdivision WPAP — source: [TCEQ Edwards Aquifer application - Edgewood Ph 1 Sec 1, Leander WPAP modificatio](https://www.tceq.texas.gov/downloads/permitting/edwards-aquifer/applications/austin/11003779.pdf)
- `new-braunfels` (should, survey): If lot is in Edwards Aquifer recharge/contributing zone (30 TAC 213), flag TCEQ WPAP/CZP and BMP constraints; ask user — source: [TCEQ Edwards Aquifer contributing-zone approval letter - Waggener Ranch Unit 2 (](https://www.cceo.org/environmental/documents/CZP/Waggener_Ranch_Unit_2.pdf)
- … and 1 more in the city files.

## tree-preservation

**Tree preservation.** Protected/heritage trees and their root zones are no-build areas; mitigation $/inch goes in the estimate.

- **Survey input:** Tree survey (user upload or yes/no for big trees).
- **Cities (7):** austin, cedar-park, conroe, dallas, georgetown, leander, san-antonio
- **Priority mix:** 1 must, 5 should, 1 nice
- **Data sketch:**

```json
{"protectedIn": 19, "heritageIn": 24, "rootZoneFtPerIn": 1, "mitigationPerIn": 450}
```

Examples from the city files:

- `austin` (must, survey): Require tree survey input: trees >=19 in DBH protected (permit), >=24 in listed species heritage (no removal w/o variance); keep footprint out of critical root zones — source: [City of Austin - City Arborist / Tree reviews and permitting](https://www.austintexas.gov/development-services/city-arborist)
- `cedar-park` (should, survey): Tree survey; heritage >= 26 in: avoid or budget $450/inch fee-in-lieu (3:1); $300/in 19-25.9 in, $150/in 8-18.9 in — source: [Community Impact - Cedar Park to preserve more trees with revised ordinance (201](https://communityimpact.com/leander-cedar-park/city-county/2019/03/15/cedar-park-to-preserve-more-trees-with-revised-ordinance)
- `conroe` (nice, survey): Flag Ch. 102 tree/canopy rules (30% canopy standard) - capture existing trees on survey. — source: [Building setbacks rules in Conroe TX (third-party summary: Ch. 94 subdivision, C](https://cityrulelookup.com/blog/building-setbacks-rules-in-conroe-tx)
- `dallas` (should, survey): Ask for a tree survey (trees 6 in caliper or more within 50 ft of work). Estimate inch-for-inch replacement for protected trees outside the unrestricted zone. Plant at least three 2-in trees, two in the front yard. — source: [Landscape Checklist - Ordinance 22053 (Article X)](https://dallascityhall.com/departments/sustainabledevelopment/buildinginspection/DCH%20documents/pdf/BI_Landscpchklst.pdf)
- `georgetown` (should, survey): Require tree survey; heritage >= 26 in DBH (listed species), protected 12-25 in; keep structure > 12 ft from heritage dripline (permit-form exemption), CRZ = 1 ft per in DBH; heritage removal mitigation 3:1 inches or $225/in x3 — source: [City of Georgetown AskGTX Knowledge Base - Heritage trees](https://georgetowntexas.qscend.com/askgtx/knowledgebase/article/588)
- `leander` (should, survey): Require tree survey; heritage tree removal mitigation 3:1 caliper inches (thresholds unverified) — source: [Leander P&Z Aug 2025 tree mitigation discussion (AI-generated meeting summary)](https://cp.soar.com/articles/5588078/Leander/Williamson-County/Texas/Williamson-County-Approves-Removal-of-Seven-Heritage-Trees-for-Wild-Spring-Phase-2-Development)
- … and 1 more in the city files.

## egress-stairs-variant

**Egress / stair amendments.** Local changes to stair or egress rules versus the model IRC.

- **Survey input:** None.
- **Cities (6):** austin, denton, houston, mckinney, pflugerville, plano
- **Priority mix:** 2 must, 2 should, 2 nice
- **Data sketch:**

```json
{"section": "R311.7", "change": "..."}
```

Examples from the city files:

- `austin` (should, plan): Visitability: provide accessible bathroom on entry level with 30x30 in clear floor space and accessible entry — source: [Affordability Impact Statement - 2024 IRC local amendments](https://services.austintexas.gov/edims/document.cfm?id=431901)
- `denton` (should, drawings): Base code 2021 IRC + 2021 IECC with Denton/NCTCOG amendments; electrical NEC 2020 (verify). — source: [Denton City Council 2022-04-05 item 22-667: ordinance repealing 2012 IRC and ado](https://denton-tx.granicusideas.com/meetings/3021-city-council-on-2022-04-05-2-00-pm/agenda_items/62476031f395e7d7be000c4e-y-id-22-667-consider-adoption-of-an-ordinance-of)
- `houston` (nice, plan): Check Houston-amended egress opening (R310) and exterior deck guard rules before finalising bedrooms/decks — source: [Houston Construction Code Modernization 2021 Building Code Adoption (TTI committ](https://311.houstontx.gov/council/committees/tti/20230824/Houston-Construction-Code-Modernization-2021-Building-Code-Adoption.pdf)
- `mckinney` (must, drawings): Use 2024 IRC / 2024 IECC / 2024 IPC-IMC-IFGC as base code for permits applied on or after 2025-10-01. — source: [City of McKinney Building Inspections page (2024 codes adopted, effective 2025-1](https://www.mckinneytexas.org/243/Building-Inspections)
- `pflugerville` (nice, plan): Use 2021 IRC; Appendix H patio-cover rules apply to covered patios — source: [City of Pflugerville Code of Ordinances - building/construction code chapter (eC](https://ecode360.com/39355343)
- `plano` (must, drawings): Use 2024 IRC (not 2021) as the base code for Plano permits; note code edition on drawings. — source: [City of Plano ordinance adopting the 2024 International Residential Code with lo](https://content.civicplus.com/api/assets/tx-plano/6a2b7a22-3b2f-41c5-844b-6f5d6bb15067)

## sealed-drawings-required

**Sealed drawings.** Which drawings need a Texas PE/RA seal (foundation, framing, windstorm).

- **Survey input:** None.
- **Cities (4):** beaumont, corpus-christi, houston, new-braunfels
- **Priority mix:** 3 must, 1 should, 0 nice
- **Data sketch:**

```json
{"foundation": true, "framing": false, "windstorm": true}
```

Examples from the city files:

- `beaumont` (must, drawings): Require Texas-registered engineer windstorm certification for the house (city rule: all buildings >= 120 sf). — source: [City of Beaumont Commercial and Residential Accessory Building Permit Checklist ](https://www.beaumonttexas.gov/DocumentCenter/View/4134/Commercial-and-Residential-Accessory-Building-Permit-Checklist)
- `corpus-christi` (must, drawings): Windstorm plans sealed by TDI-certified windstorm engineer in permit set — source: [Form DSD-1002 New Residential Application Package Checklist (rev. 04/2024)](https://dsforms.cctexas.com/files/1002%20p%20New%20Residential%20Application%20Package%20Checklist.pdf)
- `houston` (should, drawings): Require sealed truss/engineered-lumber drawings and construction-ready (non-preliminary) plan set — source: [Residential Master Plan (Houston Permitting Center)](https://www.houstonpermittingcenter.org/node/816)
- `new-braunfels` (must, drawings): Drawing set: sealed foundation + bracing sheets and engineer foundation letter — source: [City of New Braunfels - Engineered Foundation Letter (template)](https://www.newbraunfels.gov/DocumentCenter/View/1464/Engineered-Foundation-Letter-)

## expansive-soil-foundation

**Expansive-soil foundation design.** Where clay is expansive, size the slab (PT or stiffened) for the site PVR/PI; adds estimate cost and a drawing note.

- **Survey input:** Optional geotech PI/PVR; else regional default.
- **Cities (4):** cypress-unincorporated-harris, dallas, hutto, new-braunfels, texas-baseline, texas-unincorporated
- **Priority mix:** 3 must, 2 should, 1 nice
- **Data sketch:**

```json
{"pvrIn": 2.0, "slab": "PT|stiffened", "region": "Blackland Prairie"}
```

Examples from the city files:

- `cypress-unincorporated-harris` (must, foundation): PE-designed post-tensioned slab (Houston-area expansive clay) — source: Assumed - prior knowledge, not verified at source this session
- `dallas` (should, foundation): Default the foundation to a post-tensioned slab on grade designed for expansive clay (IRC R403.1.8 / IBC 1808.6). Add a geotech report line item. — source: [Dallas Residential Code 2021 - Chapter 4 Foundations (UpCodes republication)](https://up.codes/viewer/dallas/irc-2021/chapter/4/foundations)
- `hutto` (should, foundation): Assume high-PI expansive clay: PT slab with geotech report; large PVR — source: Assumed (Assumed - general Texas practice / researcher judgement)
- `new-braunfels` (nice, foundation): West-side lots: shallow limestone excavation adder; east-side: expansive clay — source: Assumed (researcher judgement)
- `texas-baseline` (must, foundation): Flag expansive clay risk; default foundation = post-tensioned slab or engineered slab designed and sealed by a Texas PE using a geotechnical report (PVR), per IRC R403.1.8 / PTI DC10.5 — source: Assumed - prior knowledge, not verified at source this session
- `texas-unincorporated` (must, foundation): Engineered (PE) slab on expansive clay — source: Assumed - prior knowledge, not verified at source this session

## frost-depth

**Frost depth / footing depth.** Minimum footing depth (Amarillo 24 in for > 600 sf) and pipe cover.

- **Survey input:** City / county.
- **Cities (4):** amarillo, el-paso, lubbock, midland
- **Priority mix:** 1 must, 3 should, 1 nice
- **Data sketch:**

```json
{"footingMinIn": 24, "waterServiceIn": 12}
```

Examples from the city files:

- `amarillo` (must, foundation): Footings min 24 in below grade for any structure > 600 sf (city IRC amendment R403.1.4) — source: [City of Amarillo - Residential Code Information (2021 IRC with City amendments F](https://www.amarillo.gov/building-safety/residential-permits/)
- `amarillo` (nice, drawings): Water service >= 12 in deep and 6 in below frost line; gas pipe >= 18 in cover — source: [City of Amarillo - Residential Code Information (2021 IRC with City amendments F](https://www.amarillo.gov/building-safety/residential-permits/)
- `el-paso` (should, foundation): Footing depth = max(12 in IRC R403.1.4, 6 in local frost line) = 12 in below undisturbed grade — source: [El Paso Code of Ordinances §18.10.050 Section R301.2 Climatic and geographic des](http://elpaso-tx.elaws.us/code/coor_title18_ch18.10_sec18.10.050)
- `lubbock` (should, foundation): Frost line 12 in below grade (city criteria) — source: [City of Lubbock - Climatic and Geographic Design Criteria sheet](https://www.mylubbock.us/DocumentCenter/View/325)
- `midland` (should, foundation): Footing depth >= 12 in (IRC minimum) until local frost line confirmed — source: Assumed: IRC R403.1.4 model minimum

## tap-fee-estimate

**Utility tap / meter fees.** Add water/sewer tap and meter fees (city or MUD) to the estimate.

- **Survey input:** Utility provider (city, MUD, WSC).
- **Cities (4):** cypress-unincorporated-harris, garland, hutto, sugar-land
- **Priority mix:** 0 must, 1 should, 3 nice
- **Data sketch:**

```json
{"waterTap": 915, "sewerTap": 200, "provider": "city"}
```

Examples from the city files:

- `cypress-unincorporated-harris` (should, estimate): Add MUD tap/capital fees placeholder; MUD tax affects owner cost — source: Assumed - prior knowledge, not verified at source this session
- `garland` (nice, estimate): Electric service is from Garland Power & Light (city utility), not Oncor. Use city utility connection fees once found. — source: Assumed - researcher judgement (not verified this session)
- `hutto` (nice, estimate): Ask which water provider serves the lot (city vs WSC) - tap/impact fees differ — source: Assumed (Assumed - general Texas practice / researcher judgement)
- `sugar-land` (nice, estimate): Add water connection $915 (5/8-in) + sewer tap $200. — source: [City of Sugar Land - Application for New Meter Utility Service](https://www.sugarlandtx.gov/DocumentCenter/View/25889)

## no-zoning

**No-zoning city.** City has no use zoning; only plat/development rules and deed restrictions limit the house.

- **Survey input:** None.
- **Cities (3):** conroe, cypress-unincorporated-harris, houston, texas-unincorporated
- **Priority mix:** 4 must, 0 should, 0 nice
- **Data sketch:**

```json
{"hasZoning": false}
```

Examples from the city files:

- `conroe` (must, setbacks): No city zoning: do not apply district setbacks/height/coverage; require user to enter plat building lines and deed-restriction setbacks. — source: [Crexi listing MLK & 1st Ave Conroe TX (states City of Conroe has no Zoning Ordin](https://www.crexi.com/properties/632769/texas-mlk-and-1st-ave---conroe-tx)
- `cypress-unincorporated-harris` (must, setbacks): No zoning - take setbacks from plat building lines and deed restrictions; ask for HOA design guidelines — source: Assumed - prior knowledge, not verified at source this session
- `houston` (must, setbacks): Disable district selection; use Chapter 42 building lines + plat + deed restrictions instead of zoning setbacks — source: [Proposed Amendments to Chapter 42 of the Code of Ordinances - FAQ](https://www.houstontx.gov/planning/DevelopRegs/docs_pdfs/chapter42-faq-v2.doc)
- `texas-unincorporated` (must, setbacks): Disable zoning setbacks/height/coverage; use plat building lines and deed restrictions as setbacks — source: Assumed - prior knowledge, not verified at source this session

## min-dwelling-size

**Minimum dwelling size.** Reject plans below the district minimum floor area.

- **Survey input:** District.
- **Cities (3):** cedar-park, garland, leander
- **Priority mix:** 3 must, 0 should, 0 nice
- **Data sketch:**

```json
{"minSqFt": 1500}
```

Examples from the city files:

- `cedar-park` (must, plan): Minimum living area 1,500 sf in SU — source: [Cedar Park TX UDC Chapter 11 - Table 11.03.061A Single-Family Residential Lot an](https://www.zoneomics.com/code/cedar-park-TX/chapter_3)
- `garland` (must, plan): For every two bedrooms provide one full bathroom and 120 sq ft of living area. — source: [City of Garland - New House (permit requirements and fees)](https://www.garlandtx.gov/3167/New-House)
- `leander` (must, plan): Minimum living area 1,200 sf in SFU, 1,500 sf in SFS — source: [City of Leander Composite Zoning Component Summary (PDF)](https://www.leandertx.gov/DocumentCenter/View/1186/Composite-Zoning-Component-Summary-PDF)

## energy-compliance-doc

**Energy compliance document.** Produce REScheck / ERI / HERS documentation the city requires at permit.

- **Survey input:** None.
- **Cities (3):** league-city, midland, sugar-land, texas-baseline, texas-unincorporated
- **Priority mix:** 3 must, 2 should, 0 nice
- **Data sketch:**

```json
{"method": "REScheck|ERI", "thirdPartyInspection": true}
```

Examples from the city files:

- `league-city` (should, drawings): City permit set to 2021 IRC/IECC (CZ 2A); separate TDI windstorm submittal to 2024 IRC. — source: [League City Council agenda/video - public hearing & action amending Ch. 22 Build](https://leaguecitytx.new.swagit.com/videos/246207)
- `midland` (must, drawings): Include ACCA Manual J (or RS summary) and energy compliance statement in permit set — source: [City of Midland - Residential Buildings & Additions Building Permit Submittal Re](https://www.midlandtexas.gov/DocumentCenter/View/9687/Residential-Building--Additions--Building-Permit-Submittal-Requirements---revised)
- `sugar-land` (must, drawings): Design to 2024 IRC + 2024 IECC (CZ 2A) + NEC 2023 with Ord. 2395 amendments for applications on/after Jan 21 2026 (not the 2021 IRC baseline). — source: [City of Sugar Land - Permits & Inspections (2024 ICC effective Jan 21 2026)](https://www.sugarlandtx.gov/2362/Permits-Inspections)
- `texas-baseline` (must, envelope): Energy compliance to 2015 IRC Chapter 11 statewide minimum unless the city adopted a newer IECC/IRC energy chapter; include REScheck/ERI documentation — source: [Texas Register, Oct 24 2025, In Addition: SECO notice on 2024 IRC energy chapter](https://www.sos.state.tx.us/texreg/archive/October242025/In%20Addition/In%20Addition.html)
- `texas-unincorporated` (should, envelope): Design to state energy code (2015 IRC ch. 11) by county climate zone even though not inspected — source: [Texas Register, Oct 24 2025, In Addition: SECO notice on 2024 IRC energy chapter](https://www.sos.state.tx.us/texreg/archive/October242025/In%20Addition/In%20Addition.html)

## snow-load

**Ground snow load.** Roof design snow load (Panhandle/West Texas).

- **Survey input:** City.
- **Cities (3):** amarillo, el-paso, lubbock
- **Priority mix:** 0 must, 2 should, 1 nice
- **Data sketch:**

```json
{"groundSnowPsf": 15}
```

Examples from the city files:

- `amarillo` (should, structure): Flag ground snow load input (Panhandle about 15-20 psf; not confirmed) — source: Assumed: Panhandle snow load
- `el-paso` (nice, structure): Ground snow load 5 psf (use IRC minimum roof live load 20 psf governs) — source: [El Paso Code of Ordinances §18.10.050 Section R301.2 Climatic and geographic des](http://elpaso-tx.elaws.us/code/coor_title18_ch18.10_sec18.10.050)
- `lubbock` (should, structure): Ground snow load 15 psf (city Table R301.2(1)) — source: [City of Lubbock - Climatic and Geographic Design Criteria sheet](https://www.mylubbock.us/DocumentCenter/View/325)

## side-wall-articulation

**Side-wall articulation.** Long side walls must step in (Austin Subchapter F).

- **Survey input:** District / overlay.
- **Cities (2):** austin, killeen
- **Priority mix:** 1 must, 1 should, 0 nice
- **Data sketch:**

```json
{"maxUnbrokenFt": 36, "offsetFt": 4}
```

Examples from the city files:

- `austin` (should, massing): Inside McMansion boundary: long side walls need an offset (articulation) - flag for review until trigger length verified — source: [City of Austin - Residential Design & Compatibility Standards (Subchapter F)](https://austintexas.gov/department/residential-design-compatibility-standards)
- `killeen` (must, massing): Include >= 5 listed architectural elements and >= 2 front-elevation features (corbels, quoins, louvered vents, keystones, etc.); use checklist — source: [City of Killeen Architectural Standards Verification Checklist - Single-Family/T](https://www.killeentexas.gov/DocumentCenter/View/9776/Single-Family-Two-Family-Residential-Checklist)

## seismic-category

**Seismic design category.** SDC (El Paso C; detached houses exempt per R301.2.2, townhouses not).

- **Survey input:** City; building type.
- **Cities (2):** el-paso, midland, texas-baseline
- **Priority mix:** 1 must, 0 should, 2 nice
- **Data sketch:**

```json
{"sdc": "C", "detachedExempt": true}
```

Examples from the city files:

- `el-paso` (must, structure): Set Seismic Design Category C; detached one-/two-family dwellings exempt from IRC R301.2.2 seismic provisions, but townhouse/attached products must apply SDC C seismic detailing — source: [El Paso Code of Ordinances §18.10.050 Section R301.2 Climatic and geographic des](http://elpaso-tx.elaws.us/code/coor_title18_ch18.10_sec18.10.050)
- `midland` (nice, structure): Keep SDC A per IRC, but show advisory about induced earthquakes (M5.2 Dec 2022) - suggest crack control joints/flexible connections — source: [Seismica article - seismicity of the greater Permian Basin (through Oct 2025)](https://seismica.library.mcgill.ca/article/download/1920/3918/37458)
- `texas-baseline` (nice, structure): SDC A statewide default; check El Paso area for higher SDC — source: Assumed - prior knowledge, not verified at source this session

## hail-roof

**Hail / roofing.** Roofing rules (re-roof tear-off; optional Class 4 shingles for insurance).

- **Survey input:** Roof choice.
- **Cities (2):** amarillo, lubbock, texas-baseline
- **Priority mix:** 0 must, 0 should, 3 nice
- **Data sketch:**

```json
{"class4Required": false}
```

Examples from the city files:

- `amarillo` (nice, envelope): Default roof to Class 4 impact-resistant (recommended, not code) — source: Assumed: hail exposure
- `lubbock` (nice, envelope): Default roof spec to Class 4 (UL 2218) impact-resistant shingles as recommended option (not code) — source: Assumed: High Plains hail exposure
- `texas-baseline` (nice, envelope): Offer Class 4 impact-resistant roofing option (DFW, Panhandle, Central TX) — source: Assumed - prior knowledge, not verified at source this session

## adu-rules

**ADU rules.** Whether a second unit / ADU is allowed and its size cap.

- **Survey input:** Wants ADU yes/no.
- **Cities (2):** austin, dallas
- **Priority mix:** 0 must, 1 should, 1 nice
- **Data sketch:**

```json
{"allowedByRight": false, "maxSqFt": 700}
```

Examples from the city files:

- `austin` (nice, plan): Allow up to 3 units on SF-1/2/3 lots; FAR 0.55/3,200 (2 units) or 0.65/4,350 (3 units) inside boundary, per-unit max 0.4/2,300 — source: [Ordinance 20250424-073 amending 25-2-773 FAR (council document)](https://services.austintexas.gov/edims/document.cfm?id=451575)
- `dallas` (should, plan): Block a by-right ADU in R-7.5(A). Offer it only with a Board of Adjustment special exception or an ADU overlay, at most the greater of 700 sq ft or 25% of the main house, one story, owner-occupancy deed restriction. — source: [Dallas ADU Rules 2026 (aduzoning.org summary citing 51A-4.209(b)(6))](https://www.aduzoning.org/adu-rules/dallas-tx/)

## far-limit

**FAR limit.** Cap gross floor area / lot area (Austin Subchapter F: larger of 0.4 FAR or 2,300 sf).

- **Survey input:** District; Subchapter F area yes/no.
- **Cities (1):** austin
- **Priority mix:** 1 must, 0 should, 0 nice
- **Data sketch:**

```json
{"far": 0.4, "orMinSqFt": 2300}
```

Examples from the city files:

- `austin` (must, massing): If inside McMansion boundary and single unit: gross floor area <= max(0.4 x lot area, 2,300 sq ft) — source: [Ordinance 20250424-073 amending 25-2-773 FAR (council document)](https://services.austintexas.gov/edims/document.cfm?id=451575)

## setback-plane

**Setback plane (tent).** 3D envelope check: plane rising from side lot lines (Austin: 15 ft up then 45 deg).

- **Survey input:** District / overlay.
- **Cities (1):** austin
- **Priority mix:** 1 must, 0 should, 0 nice
- **Data sketch:**

```json
{"startHeightFt": 15, "angleDeg": 45, "sides": ["side","rear"]}
```

Examples from the city files:

- `austin` (must, massing): Inside McMansion boundary: setback plane starting 15 ft above grade at side/rear lines, sloping inward 45 deg; check roof/dormers — source: [Austin Monitor (2006) - Council to hear McMansion proposal](https://www.austinmonitor.com/stories/2006/06/council-to-hear-mcmansion-proposal-today/)

## mechanical-cooling-required

**Required cooling.** Austin 2024 IRC amendment requires AC capable of 85 F indoors / 15 F below outdoor.

- **Survey input:** None.
- **Cities (1):** austin
- **Priority mix:** 1 must, 0 should, 0 nice
- **Data sketch:**

```json
{"maxIndoorF": 85}
```

Examples from the city files:

- `austin` (must, envelope): Mechanical design must include AC able to hold <=85 F and >=15 F below outdoor — source: [Community Impact - Housing in Austin will soon be required to have air condition](https://communityimpact.com/south-central-austin/government/housing-in-austin-will-soon-be-required-to-have-air-conditioning-for-residents/)

## occupancy-limit

**Occupancy limit.** Cap on unrelated occupants per dwelling (College Station: 4, or 2 in Restricted Occupancy Overlay). Warn when bedrooms exceed the cap for a rental-style plan.

- **Survey input:** Intended use (owner / rental); overlay (address).
- **Cities (1):** college-station
- **Priority mix:** 0 must, 1 should, 0 nice
- **Data sketch:**

```json
{"maxUnrelated": 4, "overlayMax": 2}
```

Examples from the city files:

- `college-station` (should, plan): Warn when plan has more than 4 bedrooms intended for unrelated occupants: max 4 unrelated per dwelling (2 in ROO). Do not market 5+ bed 'stealth dorm' layouts as rentals — source: [City of College Station - Occupancy Restrictions](https://www.cstx.gov/living-here/housing/occupancy-restrictions)

## parking-min

**Parking minimum.** Minimum off-street spaces (SB 15 caps at 1 on qualifying small lots).

- **Survey input:** Bedrooms.
- **Cities (1):** college-station
- **Priority mix:** 0 must, 1 should, 0 nice
- **Data sketch:**

```json
{"spaces": 2}
```

Examples from the city files:

- `college-station` (should, plan): Parking may scale with bedrooms (assumed; College Station ties single-family parking to bedroom count) - check before adding bedrooms — source: Assumed (Assumed - general Texas practice / researcher judgement)

## termite-protection

**Termite protection.** Termite protection (R318) note where the city table says moderate-heavy.

- **Survey input:** None.
- **Cities (1):** el-paso
- **Priority mix:** 0 must, 1 should, 0 nice
- **Data sketch:**

```json
{"probability": "moderate to heavy"}
```

Examples from the city files:

- `el-paso` (should, structure): Termite: moderate to heavy - include termite protection (R318) on drawings — source: [El Paso Code of Ordinances §18.10.050 Section R301.2 Climatic and geographic des](http://elpaso-tx.elaws.us/code/coor_title18_ch18.10_sec18.10.050)

## lot-drainage

**Lot drainage.** Show lot drainage to street/storm conveyance on the site plan.

- **Survey input:** None.
- **Cities (1):** fort-worth
- **Priority mix:** 0 must, 0 should, 1 nice
- **Data sketch:**

```json
{"toStorm": true}
```

Examples from the city files:

- `fort-worth` (nice, survey): Site plan must show lot surface drainage diverted to storm sewer conveyance (amended R401.3). — source: [Ordinance No. 25383-03-2022 - Fort Worth Residential Code (2021 IRC with local a](https://www.fortworthtexas.gov/files/assets/public/development-services/documents/building-code-local-amendments/2021-approved-local-amendments/irc-amendments-2021-ordinance-25383-03-2022.pdf)

