# Texas state background for single-family design (group "state")

Read date: 2026-10-11.

**How this was checked.** The egress policy blocked statutes.capitol.texas.gov, capitol.texas.gov, comptroller.texas.gov, tdi.texas.gov, energycodes.gov, justia, FindLaw and public.law, for both WebFetch and curl. Wave 3 (same date) re-checked sections 2-9 through search excerpts (statutes host still unreachable: DNS failure). Each item below is marked as one of:
- **[Secondary]**: read from search-result excerpts of the cited page. The page itself could not be opened.
- **[Unverified]**: comes from prior knowledge of Texas law and was not re-checked this session. A follow-up session with access to statutes.capitol.texas.gov should confirm every [Unverified] item.

## 1. Building codes for houses: LGC 214.212 (IRC) and 214.216 (IBC)
- **214.212(a)** [Secondary]: the state adopts the IRC "as it existed on May 1, 2012" as the municipal residential code. HB 738 (87R, 2021) changed the date from May 1, 2001, effective Jan 1, 2022. Sources: HB 738 enrolled https://www.legis.state.tx.us/tlodocs/87R/billtext/html/HB00738F.HTM, FindLaw 214.212 https://codes.findlaw.com/tx/local-government-code/loc-gov-t-sect-214-212.html, and https://texas.public.law/statutes/tex._local_gov't_code_section_214.212
- **214.212(c)-(e)** [Secondary]: a city may set procedures for local amendments and may adopt later ICC editions. It may adopt a local amendment only after a public hearing, and only by ordinance.
- **214.216** [Secondary, partial]: the House version of HB 738 moved the IBC date from 2003 to May 1, 2012. I did not see the enrolled wording. This section covers commercial buildings only.
- **Conclusion:** 2012 IRC is the legal minimum. Cities may adopt newer editions such as the 2021 IRC, and most large cities have. An unlisted city should be designed to the 2021 IRC with a warning to confirm the city's adoption.
- **Newer legislation:** no 2023 or 2025 change to 214.212 was found. Search coverage was limited.

## 2. Statewide residential energy code: HSC ch. 388
- **388.003(a)** [Secondary]: the energy chapter of the IRC "as it existed on May 1, 2015" has been the state single-family energy code since Sept 1, 2016. Source: FindLaw https://codes.findlaw.com/tx/health-and-safety-code/health-safety-sect-388-003/
- **388.003(b)** [Secondary]: on or after Sept 1, 2021, SECO may adopt the latest IRC energy chapter. Conditions (TML summary https://www.tml.org/DocumentCenter/View/2817/Building-Codes---2021-07-PDF):
  - SECO needs written stringency findings from the TAMU Energy Systems Laboratory.
  - It may adopt no more often than once every 6 years.
  - The effective date must be at least 9 months after adoption.
- **2021 IECC / 2021 IRC chapter 11 was never adopted statewide** [Secondary]. SECO began rulemaking, but a legal reading of a 2019 bill (HB 2439) stopped it. SB 2453 (2023) would have fixed this and was vetoed. Source: SB 783 analysis https://capitol.texas.gov/tlodocs/89R/analysis/html/SB00783F.htm
- **SB 783 (89R, 2025)** [Secondary]: passed and took effect Sept 1, 2025 (LegiScan https://legiscan.com/TX/text/SB783/id/3057306). It exempts SECO-adopted energy codes from the product-preemption law and requires an economic impact analysis.
- **Texas Register, Oct 24, 2025** [Secondary]: SECO asked for comments on the 2024 IRC energy chapter (single-family) and the 2024 IECC. The notice confirms the 2015 code is still in force. Source: https://www.sos.state.tx.us/texreg/archive/October242025/In%20Addition/In%20Addition.html
- **No final SECO adoption was found as of 2026-10-11.** Even if SECO adopted the 2024 code in 2026, it could not take effect until at least 9 months later.
- **Conclusion:** the state minimum in 2025-2026 is the 2015 IRC chapter 11. The 2024 edition is under review.
- **Local stricter codes** [Secondary]: 388.003(d)-(e) let cities adopt local amendments that are not less stringent. The older text limits this to nonattainment and affected counties. AG Opinion JC-0457 quotes it: https://www.oag.state.tx.us/sites/default/files/opinion-files/opinion/2002/jc0457.pdf. I did not see the current text of (e). In practice, cities such as Austin (2024 IECC) and the DFW cities (2021 IECC) adopt newer editions.

### County to IECC climate zone
Two maps are needed. The state code (2015 IRC ch. 11) uses the 2009-2018 county list. Cities that adopted the 2021 IECC or newer use the 2021 map.

| Zone | 2009-2018 list [Unverified, prior knowledge] | 2021 IECC changes |
|---|---|---|
| 2A | Harris, Fort Bend, Montgomery, Brazoria, Galveston, Waller, Jefferson, Brazos, Bexar, Comal, Travis, Williamson, Hays, Bell, McLennan, Nueces, Cameron, Hidalgo | adds **Dallas** [Secondary] and **Tarrant** [Secondary, weak] |
| 2B | Webb | none seen |
| 3A | Dallas, Tarrant, Collin, Denton, Rockwall, Kaufman, Ellis, Johnson, Smith | **Collin, Denton, Rockwall stay 3A** [Secondary] |
| 3B | El Paso, Lubbock, Midland | not checked |
| 4B | Potter, Randall | not checked |

- **Dallas 2A / Collin, Denton, Rockwall 3A:** City of Dallas public comment on its 2021 IECC adoption https://dallascityhall.com/departments/sustainabledevelopment/buildinginspection/DCH%20documents/pdf/code_amendments/Public%20Comment%202021%20IECC%20CofD.pdf
- **DFW CZ3 to CZ2:** JM blog https://jm.com/en/blog/2021/march/understanding-the-iecc-s-new-climate-zone-map. It names the metro, not Tarrant's county row.
- **Split cities:** NCTCOG's 2024 IECC amendments say a city spanning 2A and 3A should amend Table R301.1 to one zone. Source: https://nctcog.org/getmedia/def8c875-d973-46d0-bb17-d26c0ec780ac/2024-IECC-Amendments-Final_Approved.pdf
- **Cameron 1A: conflicting.** harth.build says 1A, OpenEI says 2A. It stays 2A in the engine, flagged.
- **Still to check:** Ellis, Johnson, Kaufman, Parker, Hidalgo, Willacy, Potter and Randall under 2021. Use the PNNL 2022 county guide https://www.pnnl.gov/publications/guide-determining-climate-zone-county-building-america-and-iecc-2021-updates

## 3. Counties and unincorporated land
- **No general county building code, zoning or building permit for houses** [Unverified, prior knowledge].
- **LGC 233.151-.157 (subch. F, HB 2833, 81R, 2009)** [Secondary]:
  - **233.152:** applies only in a county whose commissioners court adopted an order or resolution. Galveston and Collin adopted one in 2009. Harris was not found. SB 170 (83R) proposed agricultural-land exemptions; passage not confirmed.
  - **233.153(a):** new single-family or duplex construction begun after Sept 1, 2009 must conform to the IRC "published as of May 1, 2008" or the version used in the county seat. The county may not charge a fee to enforce it. It does not apply where a city's ETJ building code applies. Sources: https://texas.public.law/statutes/tex._local_gov't_code_section_233.153 and https://eagenda.collincountytx.gov/docs/2009/CC/20090713_951/30376%5FExhibit%20A%2Epdf
  - **233.154(a):** at least 3 inspections on a vacant lot. They are the foundation (before concrete), framing and mechanical (before drywall), and completion. The builder chooses an engineer, architect, TREC inspector, ICC-certified inspector or county inspector. Notice is set by 233.154(b)-(c). **233.155** lets the county refer the inspector for discipline or seek an injunction. Source: https://texas.public.law/statutes/tex._local_gov't_code_section_233.154
- **County fire code (233.062(a))** [Secondary]: covers only commercial establishments, public buildings and multifamily of 4+ units. **One- and two-family homes are not covered.** The base is the 2005 IFC/UFC, and later editions are allowed. The 233.061 population wording is unconfirmed (HB 1034, 87R, proposed striking it). Source: https://texas.public.law/statutes/tex._local_gov't_code_section_233.062
- **Floodplain, OSSF, plat** [Unverified]: Water Code ch. 16 subch. I; HSC ch. 366 and 30 TAC 285; LGC ch. 232.
- **ETJ release, SB 2038 (88R, 2023, LGC ch. 42 subch. D)** [Secondary]:
  - A city must release land on a valid petition. Source: https://capitol.texas.gov/tlodocs/88R/analysis/html/SB02038F.htm
  - City of Grand Prairie v. State was still pending. In a related case the Texas Supreme Court said city consent is "not required" (https://news.trellis.law/texas-supreme-court-revives-case-over-extraterritorial-jurisdiction/).
- **Harris County (unincorporated)** [Secondary]:
  - **Permit:** Engineering Dept (OCE) residential development permit (https://eng.hctx.net/permits/Residential-A).
  - **Floodplain:** Floodplain Management Regulations, effective 2019-07-09 (https://www.eng.hctx.net/portals/23/fpmregs-effect190709.pdf). In the 1% or 0.2% floodplain, the lowest floor must be at least 24 in above the 0.2% WSE or 12 in above the street crown, whichever is higher. A floodway is reported at 36 in. No fill is allowed for elevation in the 100-yr floodplain. Permits are Class I outside the floodplain and Class II inside. The figures come from KPRC and Houston quotes; the PDF table was not read.
  - **Not found:** the permit fee and MUD tap fees, which are set in each district's rate order.

## 4. Windstorm (Insurance Code ch. 2210) [Secondary]
- **Where it applies:** the 14 first-tier counties (Aransas, Brazoria, Calhoun, Cameron, Chambers, Galveston, Jefferson, Kenedy, Kleberg, Matagorda, Nueces, Refugio, San Patricio, Willacy). In Harris County it applies only **inside the city limits of La Porte, Morgan's Point, Pasadena, Seabrook and Shoreacres AND east of SH 146**. Source: TWIA https://www.twia.org/?p=40566. Unincorporated Harris County, including Cypress, is outside.
- **TDI windstorm code:**
  - 2018 IRC/IBC for 2020-04-01 to 2026-03-31.
  - **2024 IRC/IBC from 2026-04-01.** The new rule is 28 TAC 5.4013 plus amendments to 5.4011, 5.4012 and others. The proposal said March 1; the adopted rule moved it to April 1, 2026. **Confirmed.**
  - Sources: https://agate.tdi.texas.gov/wind/geninfo.html and Texas Register Feb 13 2026 https://www.sos.texas.gov/texreg/archive/February132026/Adopted%20Rules/28.INSURANCE.html
- **Correction: HB 1900 is 86R (2019), not 2023.** With SB 615 it moved completed-construction certificates of compliance back to TDI from 2020-06-01, and it changed TWIA funding. Sources: TDI overview https://tdi.texas.gov:443/pubs/pc/twia-overview.pdf and LegiScan https://www.legiscan.com/TX/text/HB1900/2019. 88R changes are summarized in TWIA's 2024 biennial report (not read).
- **Building code and inspection eligibility:** Insurance Code 2210.251-.252 and 2210.258-.259.

## 5. Fire sprinklers [Secondary]
- **LGC 250.011**, added by HB 738 (2021), bars cities, counties and ESDs from requiring sprinklers in one- or two-family dwellings.
- **Exception:** cities that had a requirement before Jan 1, 2009.
- **Sources:** HB 738 enrolled and Allensworth (see section 1).

## 6. Plumbing and electrical [Secondary]
- **Plumbing, Occupations Code 1301.255:**
  - The plumbing board adopts both the UPC and the IPC "as those codes existed on May 31, 2001", and may adopt later editions by rule.
  - Cities may amend for local conditions as long as the change does not substantially depart from board rules.
  - Bills in 87R, 88R and 89R (e.g. HB 747, 89R) proposed an IPC-only code; none was confirmed passed.
  - Source: Justia 2025 https://law.justia.com/codes/texas/occupations-code/title-8/chapter-1301/subchapter-e/section-1301-255/
- **Electrical: NEC 2026 statewide from 2026-09-01. Confirmed.**
  - The TDLR Commission voted on 2026-07-28 to amend 16 TAC 73.100 (51 TexReg 5776, Aug 28 2026).
  - Texas amendment: NEC 210.8(F) GFCI is not required for outdoor dwelling HVAC outlets.
  - Cities may amend if the change is at least as stringent.
  - Sources: https://www.tdlr.texas.gov/news/rulemaking/2026/09/01/commission-adopts-rules-12/ and https://www.houstonpermittingcenter.org/news-events/2026-national-electrical-code-effective-september-1-2026

## 7. Permit timing and third-party inspection [Unverified]
- **LGC 214.904:** a city must grant or deny a building permit within 45 days.
- **HB 14 (2023), LGC ch. 247:** third-party review or inspection is allowed if the city misses its deadlines.

## 8. Product and material preemption: Gov't Code ch. 3000 (HB 2439, 86R, eff. 2019-09-01) [Secondary]
- **3000.002(a):** a governmental entity may not adopt or enforce a rule, charter provision, ordinance, order, building code or other regulation that prohibits or limits a building product, material or method approved by a national model code published within the last three code cycles, or that sets a standard stricter than that code.
- **(b):** local amendments to the building code are allowed if they do not conflict with (a).
- **Exceptions** (Fort Worth summary https://www.fortworthtexas.gov/files/assets/public/development-services/documents/housebill-2439.pdf and Dallas ZOAC reports):
  - areas of historical, cultural or architectural significance, where the city is a Certified Local Government or has a THC-compliant landmark ordinance
  - designations made by April 1, 2019, and National Register districts
  - state-agency programs that require particular standards, incentives or financing
- **Exceptions not verified:** windstorm, fire or other code exceptions. The full (c)-(d) list was not seen.
- **SB 783 (89R, 2025):** amended ch. 3000 to exempt SECO-adopted energy codes.
- **Sources:** https://texas.public.law/statutes/tex._gov't_code_section_3000.002 and https://capitol.texas.gov/tlodocs/86R/billtext/html/HB02439F.HTM
- **Engine rule:** no city masonry %. Apply one only for an HOA or deed restriction, or a qualifying historic district.

## 9. Housing bills [Secondary]
- **SB 15 (89R, 2025), small lots.** Signed June 20, 2025. It adds LGC ch. 211 subch. D and applies to applications on or after 2025-09-01.
  - **Who it covers:** a city of more than 150,000 people wholly or partly in a county of more than 300,000, on an unplatted tract of 5+ acres zoned single-family. "Small lot" means 4,000 sf or less.
  - **What the city may not require:**
    - a lot larger than 3,000 sf, wider than 30 ft or deeper than 75 ft
    - setbacks over 15 ft front, 10 ft rear or 5 ft side
    - covered parking, or more than 1 space
    - more than 30% permeable surface
    - maximum bulk, wall articulation, or certain ceiling-height rules
  - **Not affected:** HOA and deed restrictions, historic preservation, water and sewer, building codes and flood rules.
  - **Excluded areas:** land within 3,000 ft of an airport or military base, and within 1 mile of a law-enforcement training campus in a county of 2.6M or more.
  - The committee draft's 1,400 sf / 20 ft / 60 ft figures were superseded.
  - Sources: https://capitol.texas.gov/tlodocs/89R/analysis/html/SB00015F.htm, https://gov.texas.gov/news/post/governor-abbott-signs-laws-to-combat-statewide-housing-crisis-in-austin and https://www.elpasotexas.gov/assets/Documents/CoEP/Planning-and-Inspections/misc/SB-15-Information-Sheet.pdf
- **SB 840 (89R, 2025, eff. 2025-09-01):** multifamily and mixed-use residential by right on office, commercial, retail and warehouse land in large cities. The population cutoff is not confirmed. No effect on detached-house design. Source: https://www.gptx.org/Newsroom/Notice-Effective-September-1st-Senate-Bill-840
- **HB 24 (89R, 2025):** the zoning protest threshold rises from 20% to 60%. Rezonings only. Source: https://open.pluralpolicy.com/tx/bills/89R/HB24
- **SB 1787:** the 88R (2023) bill set a 1,400 sf lot cap in counties of 300k+. No evidence it passed, and no 2025 SB 1787 on lot setbacks was found. SB 15 is the enacted law.
- **SB 2038 (2023):** see section 3.

## 10. Expansive clay [Unverified]
- **Where:** large parts of DFW, Austin, San Antonio, Waco and Houston sit on high-plasticity clays.
- **Measures:** TxDOT Tex-124-E gives PVR, with about 1 in or more treated as expansive. NRCS Web Soil Survey gives shrink-swell class.
- **Code:** IRC R403.1.8.
- **Texas practice:** a geotech report and a PE-sealed PT slab (PTI DC10.5).
- **Engine flag:** "must" statewide unless a site report shows low PVR.
