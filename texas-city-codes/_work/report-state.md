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
