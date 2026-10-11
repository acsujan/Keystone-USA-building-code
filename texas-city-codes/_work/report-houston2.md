# Report: group houston2 (pearland, league-city, conroe)

Read date 2026-10-11. **Environment limits:** every direct fetch failed. WebFetch returned DNS errors (ENOTFOUND) and curl got proxy 403 for TDI, the city sites, Municode, ecode360, the Census site and others. After about 20 searches in this group, the shared web-search budget (200 per turn, across all agents) ran out. So every value comes from search-engine extracts of the cited pages. For that reason nothing is marked "Sourced": primary-document text seen only in an extract is marked **Secondary**, with a note saying so. All three files pass validate.py.

## pearland: about 55% complete
- Found:
  - Adopted codes from the city's adopted-codes page: 2021 IRC, IECC, IPC, IMC, IFGC and IFC, plus NEC 2023.
  - Flood rule (Municode Ch. 10 1/2): finished floor at least 1 ft above BFE, or at/above the 500-yr elevation, whichever is higher. The attached-garage slab follows the same rule.
  - Permit fee of $0.41/sf. Worked example: 2,840 sf x $0.41 = $1,164.40.
  - Impact fee of about $9,625 water+sewer (2023 report). Another report says $9,265, and the city has since moved to a meter-based fee.
  - District minimum lot sizes: R-1 8,800 sf, R-2 7,000 sf, R-3 6,000 sf.
  - Census V2023 population: 127,736.
- Windstorm:
  - All of Brazoria County is a TDI catalogue area, and the TDI Brazoria page lists Pearland as Inland II.
  - The Harris County designation covers only Morgan's Point, La Porte, Shoreacres, Seabrook and Pasadena east of SH 146. Fort Bend is not designated.
  - Result: WPI-8 is needed only for parcels on the Brazoria side.
- Not found:
  - Primary UDC setbacks, height and coverage. The setbacks 25/5/15/20 come from a third-party guide, and the rear value is Assumed.
  - Text of the residential amendments.
  - Masonry rule, tap fees, plan-review fee, market $/sf.
- 2nd check:
  - IRC edition: confirmed in two separate searches of the city adopted-codes page. The Municode Ch. 7 extract showed only IBC 2021 (Sec. 7-13), so the ordinance itself was not seen.
  - Setbacks: two searches gave consistent third-party values, but the UDC extract was garbled (conflicting R-2 text), so they are not verified.

## league-city: about 15% complete (windstorm only)
- Found:
  - Galveston County is a whole-county catalogue area, and League City is listed as Inland I.
  - The Inland I/II line in Galveston County follows the Brazoria/Galveston county line to Friendswood's southern limits, then Friendswood's eastern limits. It is not tied to I-45, so there is no inland I-45 split: the whole Galveston part of the city is Inland I.
  - Legacy Inland I wind speed: 120 mph (ASCE 7-05), which TDI equates to 155 mph ultimate (2018 TDI newsletter).
  - A source says the TDI zones were replaced by Risk Category based ASCE 7 speeds after the 2018-code adoption.
- Not found: everything city-specific (code editions, UDC, flood freeboard, fees, masonry, MUD fees). Code editions are entered as Assumed placeholders (2021 IRC/IECC).
- 2nd check: TDI status appeared in two separate searches (the Galveston map page and the TWIA designated-areas document).

## conroe: about 5% complete
- windstormCounty = false: Montgomery County is not on the TDI designated list.
- All other values are Assumed or null with notFound. Zoning status is deliberately left null (unverified).
- 2nd check: none.

## Cross-city windstorm findings
- TDI adopted the 2018 IRC/IBC for windstorm certification effective Sept 1, 2020.
- A Texas Register rule (adopted Feb 13, 2026) makes the 2024 IRC/IBC apply to windstorm certification on and after April 1, 2026.
- So League City homes, and Brazoria-side Pearland homes, are checked by TDI against the 2024 IRC, while the city permit likely uses the 2021 IRC. These are separate submittals.
- The process: WPI-1 before construction starts, then plan review and inspections by a TDI-appointed PE, then a WPI-8 certificate. The certificate is needed for TWIA wind/hail coverage.

## Needs a follow-up run (with search/fetch access)
- League City and Conroe: the full city data set.
- Pearland: UDC table values, residential amendments, and the current meter-based impact fee.

## Wave 3 (39 searches; Secondary)
- league-city: 2021 IRC/IECC/IPC/IMC/IFGC + local amendments in Ch. 22 (agenda; ord. no. not seen); NEC not found. RSF-7 7,000 sf; front 25 (UDC Table 3.3.2, 2025 variance agenda); side 5/rear 20/street 15/35 ft placeholders. Flood (2018): 24 in above BFE or 3 in above 500-yr; infill variance (2022). Permit $0.40/sf -> $1,136. Impact $11,860-14,825 water+ww (+93%, Dec 2023). Pop 118,456 (V2024).
- conroe: no zoning (2 sources); plat building lines (Ch. 94) + deed restrictions. Flood: FF >= BFE + 12 in (city handout). No impact fees (study, adoption ~Q4 2027). 2021 IRC + NEC 2023 third-party only (official record: 2009 IRC eff. 2013).
- katy: 2021 I-codes + NEC 2023 (Ch. 3 Art. 3.02, ~Jan 2024; agenda). R-1 (third party): front 25 (35 major), corner 25, rear 15, 32 ft. Floodplain at/above 500-yr (unconfirmed for city).
- sugar-land: 2024 I-codes + NEC 2023 (Ord. 2395, applications from 2026-01-21; 2 city pages). R-1: 6,600 sf, 60x110, front 25, sides 5 (total >= 10% width), rear 15 (25 arterial), 35 ft/2.5 st, 40% coverage (rear/coverage from garbled table). FY25 Ord. 2355 tiered fee + 50% plan check -> ~$2,730 Assumed. Tap water $915 + sewer $200.
