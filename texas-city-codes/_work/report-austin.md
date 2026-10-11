# Report - group "austin" (austin, round-rock)

## Research conditions (important)
- Direct page fetching was blocked for the whole session: WebFetch got DNS failures and curl got proxy CONNECT 403 for every host tried (austintexas.gov, services.austintexas.gov, library.municode.com, publicinput.com, roundrocktexas.gov, amlegal, ecode360, census.gov, iccsafe.org).
- So every Austin value comes from WebSearch result summaries of the cited pages. Those are marked **Secondary**, never Sourced, because the primary text was not read directly.
- The shared web-search budget (200 per turn, across all agents) ran out partway through Austin. Round Rock got **no** searches, so its file is entirely **Assumed**: placeholders flagged as unverified, with null where I had no confident value.

## austin - mostly complete (Secondary)
Found:
- IRC: 2024 IRC by Ord. 20250410-040, effective 2025-07-10. The 2021 IRC was in force before that.
- IECC: 2024 IECC with Austin amendments, council File 25-0605, effective 2025-07-10. Ordinance number not found.
- SF-3 limits (25-2-492): 5,750 sf lot, 50 ft width, setbacks 25 front / 5 side / 15 street side / 10 rear, 35 ft height, 40% building coverage, 45% impervious cover.
- Subchapter F: floor area max is the larger of 0.4 FAR or 2,300 sf. The tent starts 15 ft up and slopes in at 45 degrees (from 2006 text). Height 32 ft.
- HOME Phase 1: Ord. 20231207-001, effective 2024-02-05, allows up to 3 units.
- HOME Phase 2: adopted 2024-05-16, effective 2024-08-16; 1,800 sf small lot, 15 ft width.
- Ord. 20250424-073 set the 25-2-773 FAR gradient: 0.55 / 3,200 sf and 0.65 / 4,350 sf.
- Mandatory air conditioning amendment (85 F max, 15 F below outdoor).
- Visitability: 30x30 in bathroom clear floor space.
- Trees: protected at 19 in, heritage at 24 in (25-8-621 / 641).
- Atlas 14: the regulatory 100-yr floodplain is the old FEMA 500-yr floodplain; freeboard is 2 ft.
- Impact fees: $4,800 water + $2,900 wastewater = $7,700 (lots platted after 2023-10-01).
- Plan review tier fee: $1,141 for 2,001-3,000 sf, plus a 6% surcharge.

Not found / Assumed:
- HOME Phase 2 ordinance number: 20240516-006 is not confirmed.
- Plumbing, electrical and mechanical editions. UPC is assumed.
- Full DSD per-sq-ft fees and the building permit fee, so the worked example is null.
- Tap and Austin Energy fees, frost depth, market $/sf.
- Whether foundation engineering is mandatory.
- The side-wall articulation trigger length.
- Current Subchapter F text, including garage exemptions.
- Status of new Atlas 14 maps.
- Population (shown as about 994k from memory, Assumed).
- Parking minimums (eliminated in 2023, from memory, Assumed).

## round-rock - INCOMPLETE (all Assumed)
- The file is valid but holds only placeholders: SF-2, 6,500 sf lot, 25/5/15/20 setbacks, 2021 IRC and IPC are from memory and unverified.
- Fees, impact fees, tree, flood and masonry values are null or general.
- The engine changes include a "must verify district/plat" flag.
- Round Rock needs a full re-run once fetching or search is available.

## Second-check notes (values re-checked against a second source)
- Austin IRC edition (2024, effective 2025-07-10): the city technical-codes table and the Ord. 20250410-040 text agree (two search results). The 2021 dates come from the historic adoption table.
- Austin SF-3 coverage and impervious cover (40% / 45%) and front setback (25 ft): BOA variance staff reports and the Neuhaus 2026 guide agree.
- Interior side setback: 5 ft per the guide. One BOA case showed 10 ft, probably a different district. Street side 15 ft per the BOA reports and the guide.
- 0.4 / 2,300 sf: the 2006 Austin Monitor article and the 2025 council ordinance (as a per-unit cap) agree.
- Freeboard 2 ft: the 2019 draft commentary, the Summary of Code Changes and a secondary article agree.
- None of the above was read from Municode directly.
