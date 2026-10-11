# Research spec shared by all research agents (read fully before starting)

Date today: 2026-10-11. Write every "read" date as the date you actually fetched the page (use 2026-10-11 unless told otherwise).
Repo folder: /home/user/Keystone-USA-building-code/texas-city-codes/

## Ground rules
1. Cite everything. Every leaf value is an object:
   {"value": <number|string|bool|null>, "unit": "<optional>", "status": "Sourced|Secondary|Assumed", "source": {"id": "<source id>", "title": "...", "section": "<clause, optional>", "url": "...", "read": "2026-10-11"}, "note": "<optional short plain note>"}
   - Sourced = you read it in the primary document (city code of ordinances on Municode/AmLegal/eCode360/Franklin, adoption ordinance, state statute, official fee schedule PDF).
   - Secondary = city summary page, permit guide/FAQ, handout, trade source quoting it.
   - Assumed = your judgement, nothing found; source.title must say "Assumed" and `note` must give the reason. url may be "".
   - If a value is unknown, use {"value": null, "status": "Assumed", "source": {...}, "note": "Not found: <what you tried>"}. NEVER invent a clause number, ordinance number or URL. Only cite URLs you actually fetched or that appeared in search results you used.
   - If a page is behind login/paywall/JS and you could not read it, say so in note; do not guess its content.
2. Primary sources first (city code of ordinances, building code adoption ordinance & local amendments page, zoning/UDC, fee schedule).
3. Copyright: ICC code text (IRC/IECC): record section numbers and short values only. No RSMeans. Public cost data only.
4. Record the IRC edition ACTUALLY adopted + local amendments affecting house design.
5. No accounts, purchases, form submissions, contacting anyone.
6. Plain language for homeowners in "plainLanguage".
7. Municode pages are JS-rendered; if WebFetch returns nothing, try: library.municode.com search results in WebSearch snippets, the city's own website building/permits page, amlegal (codelibrary.amlegal.com), ecode360, the city's PDF of the adoption ordinance or "local amendments" PDF, the city's UDC PDF, the NCTCOG regional amendments (DFW cities often adopt NCTCOG recommended amendments - cite nctcog.org), and the "International Code Adoptions" ICC map (iccsafe.org/adoptions). Mark Secondary when it's not the ordinance itself.
8. Be efficient: aim for breadth with honest statuses. Finish every city you are assigned with a valid file before deepening any one city.

## Typical-district choice
Pick the most common single-family district for NEW detached homes (e.g. Dallas R-7.5(A), Austin SF-3, Fort Worth A-5, San Antonio R-6, Plano SF-7, Frisco SF-7 or SF-8.5 etc.). If several common, pick one and list others in zoning.other.

## Worked fee example
2,400 sq ft conditioned, two-storey detached house, plus assume a 440 sq ft attached garage (state your assumption). If fee is by valuation, compute valuation using the city's own valuation table if published, else the ICC Building Valuation Data (BVD) table, latest public edition, group R-3 type VB (cite it; value ~ $170-190/sq ft range for R-3 VB in 2025-2026 BVD; garage U at the BVD U rate). Show the arithmetic in `note`.

## Cost factor (DO NOT compute; a separate cost agent does it)
Set cost.factor to {"value": null, "status": "Assumed", "source": {"id":"cost-method","title":"See README cost method (filled by cost agent)","url":"","read":"2026-10-11"}, "note": "PENDING_COST_AGENT"} and cost.method to "PENDING_COST_AGENT". DO fill cost.perSqFtMarket (public market figure, source, year, flagged market figure not a quote) and cost.drivers.

## JSON shape (cities/<id>.json, ids lowercase-hyphen, e.g. "fort-worth", "college-station", "cypress-unincorporated-harris")
{
  "id": "austin", "name": "City of Austin", "state": "TX", "tier": 1,
  "counties": ["Travis","Williamson","Hays"],
  "msa": {"name": "Austin-Round Rock-San Marcos, TX", "blsCode": "12420"},
  "population": <leaf, value=latest Census Vintage estimate (say which vintage in note)>,
  "zipCodesOrBoundary": <leaf: list of ZIPs as string or a link to official city-limits map>,
  "climateZone": <leaf e.g. "2A" / "3A" / "3B" / "4B", source IECC Table/2021 IECC Fig R301.1 county list or DOE map; Secondary ok>,
  "windstormCounty": <leaf bool; TDI windstorm designated catalogue area>,
  "codes": {
    "irc": {"edition": <leaf e.g. "2021 IRC">, "ordinance": <leaf>, "amendments": [{"topic": "foundation|garage separation|fire sprinklers|room size|egress|stairs|smoke/CO alarms|masonry|other", "summary": "...", "section": "...", "status": "...", "source": {...}}]},
    "energy": {"edition": <leaf>, "stretchCode": <leaf>, "ordinance": <leaf optional>},
    "plumbing": <leaf "IPC 2021"/"UPC 2021">,
    "electrical": <leaf "NEC 2023">,
    "mechanical": <leaf>, "fuelGas": <leaf>,
    "fire": <leaf incl. any one/two-family sprinkler rule>,
    "wind": <leaf: ultimate design wind speed mph (ASCE 7-16/IRC 2021 Fig R301.2(2)) + any local value; Secondary/Assumed from map OK with note>,
    "hailRoofing": <leaf>,
    "seismic": <leaf SDC, usually A in TX; El Paso area check>,
    "frostDepth": <leaf inches, from local IRC Table R301.2(1) values if published>
  },
  "zoning": {"hasZoning": <leaf bool>, "typicalDistrict": <leaf>, "minLotSqFt": <leaf>, "minLotWidthFt": <leaf>, "minLotDepthFt": <leaf>,
    "setbacksFt": {"front": <leaf>, "side": <leaf>, "streetSide": <leaf>, "rear": <leaf>},
    "maxHeightFt": <leaf>, "maxStories": <leaf>, "maxLotCoverage": <leaf, value as fraction 0.45 with unit "fraction">, "imperviousCover": <leaf>, "far": <leaf>,
    "parking": <leaf>, "garageRules": <leaf>, "adu": <leaf>, "masonry": <leaf>, "trees": <leaf>, "minDwellingSizeSqFt": <leaf optional>,
    "other": [<leaf>...]},
  "process": {"steps": [<leaf>...], "sealsRequired": [<leaf>...], "inspections": [<leaf>...], "reviewDays": <leaf>},
  "fees": {"permitFormula": <leaf>, "workedExample2400sqft": <leaf value number USD, note shows arithmetic>, "planReview": <leaf>, "impactFees": [<leaf>...], "tapFees": [<leaf>...]},
  "cost": {"factor": <leaf PENDING>, "method": "PENDING_COST_AGENT", "perSqFtMarket": <leaf>, "drivers": [<leaf>...]},
  "flood": <leaf: floodplain ordinance + freeboard rule e.g. "lowest floor 1 ft above BFE" or Houston 500-yr+2ft>,
  "engineChanges": [{"id": "<city>-<short>", "ruleType": "<one of RULE TYPES below>", "area": "setbacks|massing|plan|structure|envelope|foundation|estimate|drawings|survey", "change": "specific, e.g. Front setback 25 ft when district is SF-3", "priority": "must|should|nice", "params": {<machine-readable key values, e.g. "frontFt": 25>}, "source": {...}}],
  "plainLanguage": "5-10 short sentences for a homeowner",
  "openQuestions": ["..."],
  "notFound": ["what you could not find"],
  "comparison": {"irc": "2021 IRC", "energy": "2021 IECC (amended)", "plumbing": "UPC 2021", "district": "SF-3", "setbacks": "25/5/10", "maxHeight": "32 ft/2 st", "coverageFar": "40% / FAR 0.4", "masonry": "none", "engFoundation": "yes - all new homes", "windstorm": "no", "flood": "1 ft freeboard", "permitFeeExample": "$X", "impactFees": "$Y water+ww", "costFactor": "PENDING"}
}

## RULE TYPES (use these ruleType ids; add a new one only if none fits, name it kebab-case)
setback-by-district, lot-min-size, height-limit, lot-coverage, impervious-cover, far-limit, setback-plane, side-wall-articulation, garage-placement, parking-min, adu-rules, masonry-percentage, tree-preservation, min-dwelling-size, engineered-foundation-flag, expansive-soil-foundation, windstorm-package, climate-zone-envelope, energy-stretch-code, flood-elevation, plumbing-code-variant, electrical-code-edition, fire-sprinkler, garage-separation, egress-stairs-variant, frost-depth, seismic-category, wind-speed, hail-roof, impact-fee-estimate, permit-fee-formula, tap-fee-estimate, cost-factor, deed-restriction-check, building-line-plat, survey-input-district, no-zoning, sealed-drawings-required, energy-compliance-doc

## Also write (per agent group G, e.g. "dfw-core")
1. _work/sources-<G>.csv  header: id,title,url,publisher,date_read,city_ids  (city_ids separated by ';'). Source ids: short kebab, unique, prefixed with city id (e.g. "austin-ldc-25-2-492").
2. _work/report-<G>.md  : per city: complete? what not found; a 2nd-check note for spot-checked values (IRC edition and setbacks re-verified via a second source or second read).
3. Validate each file: run `python3 /home/user/Keystone-USA-building-code/texas-city-codes/_work/validate.py cities/<id>.json` from the texas-city-codes folder and fix errors.
Do NOT git commit or push; the coordinator does that. Do not edit other groups' files.
