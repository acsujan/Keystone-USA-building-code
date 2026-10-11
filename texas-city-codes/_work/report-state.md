# Report, group "state" (2026-10-11)

**Limits this session.**
- WebFetch and curl to every statute host were blocked by egress policy (403 CONNECT: statutes.capitol.texas.gov, capitol.texas.gov, comptroller.texas.gov, tdi.texas.gov, energycodes.gov, justia, FindLaw, public.law).
- The shared web-search budget ran out after 8 searches.
- So nothing has status Sourced. Values come from search-result excerpts (Secondary) or prior knowledge (Assumed, labelled "not verified at source").

| File | Complete? | Notes |
|---|---|---|
| cities/texas-baseline.json | Valid; structure complete | 14 engineChanges. IRC floor, sprinkler ban and energy-code status are Secondary; the rest are Assumed. |
| cities/texas-unincorporated.json | Valid | LGC 233, OSSF, floodplain, plat and county fire code rules are all Assumed (statute text not readable). |
| cities/cypress-unincorporated-harris.json | Valid, thin | Harris County Engineering permit, fee and floodplain freeboard were not read. Setbacks are placeholders from typical plats. |
| _work/state-background.md | Written | Every item is tagged Secondary or Unverified. |

**Second check.**
- LGC 214.212 2012 date: two independent excerpts agreed (HB 738 enrolled text, and the FindLaw/public.law codified text).
- HSC 388.003 2015 base: two excerpts agreed (FindLaw text, and the Oct 2025 Texas Register notice).
- LGC 250.011: the enrolled-text excerpt and the Allensworth summary agreed.

**Not verified (follow-up needed):**
- Gov't Code ch. 3000
- LGC 233.151-.157 and 233.061 and following
- Insurance Code 2210 and HB 1900
- Occupations Code 1301.255 and 1305
- SB 15, SB 840, HB 24 (2025) and SB 2038
- the 2021 IECC Texas county list (only Cameron = 1A was seen, from a secondary source)
- Harris County floodplain and permit pages

## Wave 3 (33 searches; Secondary)
- Gov't Code 3000.002 confirmed (products approved by national model code in last 3 cycles); historic/CLG exceptions; SB 783 (2025) exempts SECO energy codes. Full (c)-(d) exceptions not seen.
- LGC 233.152 opt-in (Galveston, Collin 2009; Harris not found); 233.153 IRC as of 2008-05-01 or county-seat edition; 233.154 three inspections; 233.062 fire code not for 1-2 family.
- Windstorm: 14 counties + Harris (La Porte, Morgan's Point, Pasadena, Seabrook, Shoreacres east of SH 146). TDI 2024 IRC/IBC eff. 2026-04-01 (28 TAC 5.4013). HB 1900 is 2019 (86R), not 2023.
- Plumbing: IPC or UPC (Occ. Code 1301.255). NEC 2026 statewide eff. 2026-09-01 (16 TAC 73.100).
- SB 15 (2025) passed: cities >150k in counties >300k, unplatted 5+ ac tracts; small lots <=3,000 sf / 30 ft / 75 ft; setbacks max 15/5/10; no covered parking, max 1 space, <=30% permeable, no bulk/articulation; from 2025-09-01. SB 840, HB 24 passed (no detached-house design change). SB 2038 in force.
- Climate zones under 2021 IECC: Dallas 2A; Collin/Denton/Rockwall 3A; Tarrant 2A weak; Cameron 1A conflicting (kept 2A).
- Harris County floodplain regs (2019-07-09): max(0.2% + 24 in, street crown + 12 in); floodway 36 in; no fill.
- Second checks: TDI date, NEC 2026, SB 15, Dallas 2A (2 sources each).
