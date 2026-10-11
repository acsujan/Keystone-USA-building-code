# Report: group "collin" (frisco, mckinney, celina, prosper), 2026-10-11

## Environment limits (affects every city)
- **All direct page fetches were blocked.** WebFetch and curl both failed for friscotexas.gov, mckinneytexas.org, celina-tx.gov, prospertx.gov, ecode360.com, library.municode.com, nctcog.org and capitol.texas.gov. The proxy refused the connections (organization policy) or DNS failed.
- **The shared web-search budget ran out** (200 searches per turn, used by all agents) after about 12 searches of mine, all spent on Frisco.
- **No value is marked "Sourced".** Everything from a city document is "Secondary": it came from web-search summaries of that document, and each note says so. Everything else is "Assumed", with the reason given.
- In the sources CSV, `date_read` means the date the search result was used. It does not mean the full document was read.

## frisco: mostly complete; key items Secondary
- **IRC edition is 2024, not 2021.** It took effect 2026-03-01 under Ord. 2026-01-10, which replaced Ord. 2022-11-58 (2021 IRC).
  - **2nd check:** confirmed in three city sources: the Adopted Codes page, the Most Requested Ordinances page and the Residential Submittal Guide.
- **Other codes:**
  - Energy: 2024 IECC under Ord. 2026-01-05. The effective date conflicts on the city's own site: 03-01-2026 in one version, 06-02-2026 / 2026-06-42 in another.
  - Plumbing: 2024 IPC (Ord. 2026-01-08).
  - Electrical: 2023 NEC (Ord. 2024-01-02, effective 2024-02-16).
  - Fire: 2024 IFC.
- **Sprinklers:** required when air-conditioned area plus garage area reaches 6,000 sq ft (Residential Submittal Guide; seen in 2 searches).
  - Texas law bars cities from requiring sprinklers in one- and two-family homes unless the rule was in force on or before 2009-01-01 (Allensworth summary of HB 738, Secondary).
  - Frisco's rule is presumably legal under that grandfather clause. I did not verify that from the ordinance.
- **Foundation:** a foundation plan sealed by a Texas PE, plus PTI design data and an engineer letter, is required for all new homes (submittal guide).
- **Zoning (SF-7 base):**
  - Min lot 7,000 sf (2nd check: purpose text and area table agree). Width 60 ft, height 40 ft / 2.5 stories, front yard 25 ft: all Secondary from snippets that did not label columns clearly.
  - Side 5, street side 15, rear 20 and coverage 45% are **Assumed**.
  - **2nd check on setbacks: not achieved.** Snippets were ambiguous across districts.
- **Garages:** the 2013 "Single-Family Front Entry Lot Layout Guidelines" exist (title only). Smaller-lot districts show a 20 ft rear yard for alley-facing garages and 24 ft for swing-in garages. I could not read the J-swing details.
- **Not found:** impact fee amounts (the city's 2025 audit confirms roadway, water and wastewater fees exist), permit and plan-review fees, tap fees, flood freeboard, minimum dwelling size, review times.

## mckinney: skeleton only (mostly Assumed)
- No McKinney search was possible after the budget ran out.
- One McKinney impact-fee comparison PDF (DocumentCenter/View/25377) appeared in a Frisco search, but its numbers could not be mapped to cities.
- IRC 2021 + NCTCOG is assumed. McKinney may have moved to the 2024 codes the way Frisco did. The district name under the UDC is not verified.
- **2nd check: none.**

## celina: skeleton only (Assumed)
- PD/MUD dominance and the impact-fee and MUD/PID cost flags are noted.
- **2nd check: none.**

## prosper: skeleton only (Assumed)
- SF-10 is used as the base district. The garage and masonry history comes from my background knowledge.
- **2nd check: none.**

## Masonry / HB 2439
- All four files treat a city masonry percentage as not enforceable by the city (Tex. Gov't Code ch. 3000, from HB 2439 in 2019). PD and HOA covenants are flagged instead.
- This is from my background knowledge. I could not read the statute this session (Assumed).

## Next pass needed
Re-run McKinney, Celina and Prosper, and finish Frisco's fees and setbacks, from a session with fetch access or remaining search budget. Priority targets:
- the impact-fee ordinances for all four cities
- Frisco ZO 2.06.04 table
- McKinney UDC residential table
- Prosper ZO Ch. 3
- Celina adopted-codes page

## Wave 3 (34 searches; Secondary) - celina, prosper (+ forney, beaumont in report-east.md)
- celina: 2024 IRC + amendments (Ord. 2026-003; eff. Jan/Feb 2026, pages differ); before: 2021 IRC + NCTCOG from Nov 2022. NEC 2023 (Ord. 2023-111; 2026-002 allows copper-clad Al). PD on SF-R base (14.02.203); defaults 20/5/15/20 from Sutton Fields PD (confirm). Impact ~ $15,400 (water $4,400 + ww $5,500 + road $5,500; DBA, year unknown); 2025 study max W+WW $14,369 -> high case ~ $19,900. Pop 51,661 (V2024).
- prosper: 2021 I-codes (permits from 2023-05-01), NEC 2023 (2023-11-01). SF-10 base 10,000 sf; mostly PDs. W+WW impact $14,390 (from $6,643 in 2025); roadway $940-1,397/veh-mile. Permit $1.00/sf incl. garage/porches (FY 2025-10-01) -> $2,940.
- Second check: Celina IRC (ordinance title + 2 pages).
