# Cost agent report: Texas metro construction cost factors

Read date: 2026-10-11. Status: **PROVISIONAL, incomplete.** Every factor is marked `Assumed` with `provisional: true`.

## Method (as specified)
- Factor = 0.40 x L + 0.60 x M, rounded to 2 decimals. Baseline: US national = 1.00.
- L = weighted mean of (metro annual median / US annual median) for these trades:
  - 47-2031 Carpenters: 0.30
  - 47-2111 Electricians: 0.20
  - 47-2152 Plumbers: 0.20
  - 47-2061 Construction Laborers: 0.20
  - 49-9021 HVAC: 0.10
- If a trade is missing for a metro, its weight is dropped and the other weights are rescaled to sum to 1.
- M = 1.00 for all metros. The per-metro notes on materials are qualitative and unsourced (Assumed).

## What was actually possible
- **No page could be fetched directly.**
  - WebFetch failed with a DNS error (ENOTFOUND) on every host, including wikipedia.org.
  - curl got proxy 403 from bls.gov, data.bls.gov, api.bls.gov, download.bls.gov, texaswages.com, lmi.twc.texas.gov, onetonline.org, careeronestop.org, census.gov and nahb.org.
- **All values come from web-search extracts** of the pages, so they are marked Secondary.
- **The search budget ran out.** It is 200 searches per turn, shared by all agents. It ran out after the carpenter table was complete. Electrician, plumber, laborer and HVAC values for each metro were **not retrieved**.
- **So L uses carpenters only** (weight rescaled to 1.00). This uses the method's rescaling rule, but because the data could not be reached. The occupations were not suppressed.
- **Release used: OEWS May 2024**, through the O*NET OnLine Texas local-wages page. That page carries BLS 2024 data, with US $59,310 and Texas $48,150 on the same page.
  - The May 2025 OEWS was published 2026-05-15 (USDL-26-0725), but its metro tables could not be reached.
  - May 2025 national medians are recorded only for reference:
    - Carpenters: $60,580, from the BLS Occupational Outlook Handbook.
    - Electricians: $63,190, from WageDex.
    - Plumbers: $63,800, from WageDex.
    - Laborers: $47,120, from WageDex.
    - HVAC: $61,010, from O*NET and WageDex.

## Results (provisional, carpenter-only)
| MSA | Code | Carpenter median 2024 | L | Factor |
|---|---|---|---|---|
| Beaumont-Port Arthur | 13140 | 50,230 | 0.847 | 0.94 |
| Austin-Round Rock-San Marcos | 12420 | 49,650 | 0.837 | 0.93 |
| Houston-Pasadena-The Woodlands | 26420 | 48,910 | 0.825 | 0.93 |
| Dallas-Fort Worth-Arlington | 19100 | 48,420 | 0.816 | 0.93 |
| Midland | 33260 | 48,210 | 0.813 | 0.93 |
| Corpus Christi | 18580 | 47,850 | 0.807 | 0.92 |
| San Antonio-New Braunfels | 41700 | 47,670 | 0.804 | 0.92 |
| Tyler | 46340 | 46,460 | 0.783 | 0.91 |
| College Station-Bryan | 17780 | 46,090 | 0.777 | 0.91 |
| Amarillo | 11100 | 46,030 | 0.776 | 0.91 |
| Laredo | 29700 | 45,930 | 0.774 | 0.91 |
| Waco | 47380 | 44,800 | 0.755 | 0.90 |
| Killeen-Temple | 28660 | 44,350 | 0.748 | 0.90 |
| McAllen-Edinburg-Mission | 32580 | 40,470 | 0.682 | 0.87 |
| Lubbock | 31180 | 39,930 | 0.673 | 0.87 |
| El Paso | 21340 | 39,790 | 0.671 | 0.87 |
| Brownsville-Harlingen | 15180 | 36,760 | 0.620 | 0.85 |
| **Texas statewide** | - | 48,150 | 0.812 | 0.92 |

- The denominator is the US median of $59,310 from May 2024.
- The DFW metro divisions are not published on the O*NET page. They are left null, so use 19100 for them. Their codes (19124 Dallas-Plano-Irving, 23104 Fort Worth-Arlington-Grapevine) are **unverified**.

## Caveats and second checks
- **The factors are probably biased low.** Texas carpenters are paid relatively less than Texas electricians, plumbers and HVAC workers compared with the national level.
  - Houston's May 2025 mean wages for electricians (~$61,470) and plumbers (~$63,860) are close to the national figures, but carpenters (~$53,000) are well below.
  - The full five-trade L is therefore likely higher than the carpenter-only L.
  - Do not replace Keystone's 0.95 Texas multiplier with these numbers until the full five-trade basket has been run.
- **Second check on the US carpenter median.** $59,310 for May 2024 matches on O*NET, the O*NET 47-2031 summary and Salary Atlas.
- **Second check on Houston carpenters.**
  - TWC's Workforce Report PDF lists $48,524 (2024 OEWS). O*NET lists $48,910.
  - The gap is 0.8%, which changes the factor by less than 0.005.
  - The TWC figure's statistic type was not confirmed.
- **Lubbock ($39,930) and El Paso ($39,790)** came from search extracts and should be re-read on the live page.

## Market cost per sq ft
- **NAHB $162/sq ft and 64% construction share.** These came from the coordinator brief. NAHB was not read in this run, so they are marked Assumed.
- **Census Survey of Construction (South region):** not retrieved.
- **Texas metro figures:** not retrieved.
- All three are market figures, not quotes.

## To finish (next run, fresh search budget)
1. Fetch O*NET `localwages/<SOC>.00?st=TX` for 47-2111, 47-2152, 47-2061 and 49-9021. Get the US, Texas and all MSA rows from the same release.
2. Better: get the BLS `oes/2025/may/oes_<code>.htm` pages for May 2025 data, and switch everything to May 2025.
3. Look up the Census SOC South-region price and floor area, and the NAHB 2024 public summary.
4. Re-run `build_cost.py`. It is kept in the agent's scratchpad, and its logic is simple to rewrite.
