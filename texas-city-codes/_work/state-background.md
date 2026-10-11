# Texas state background for single-family design (group "state")

Read date: 2026-10-11.

**How this was checked.** The egress policy blocked statutes.capitol.texas.gov, capitol.texas.gov, comptroller.texas.gov, tdi.texas.gov, energycodes.gov, justia, FindLaw and public.law, for both WebFetch and curl. The shared web-search budget ran out partway through. Each item below is marked as one of:
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
**Unverified.** This uses the 2009-2018 IECC county list, which is the map the 2015 IRC uses.

| Zone | Counties |
|---|---|
| 2A | Harris, Fort Bend, Montgomery, Brazoria, Galveston, Waller, Jefferson, Brazos, Bexar, Comal, Travis, Williamson, Hays, Bell, McLennan, Nueces, Cameron, Hidalgo |
| 2B | Webb |
| 3A | Dallas, Tarrant, Collin, Denton, Kaufman, Smith |
| 3B | El Paso, Lubbock, Midland |
| 4B | Potter, Randall (Panhandle) |

**2021 IECC map:** about 400 US counties moved, mostly one zone warmer. A secondary source lists Cameron County as 1A under the 2021 IECC (https://harth.build/resources/climate-data/ashrae-climate-zones-explained/). The same source cites Dallas County going from 3A to 2A, but I could not confirm that and it is uncertain. Cities that adopt the 2021 IECC should be checked against the 2021 Table R301.1 directly.

## 3. Counties and unincorporated land
- **No building code or permit for houses.** Counties have no general building-code or zoning power [Unverified].
- **LGC 233.151-.157 (subchapter F)** [Unverified]:
  - New single-family and duplex construction in unincorporated areas must follow the IRC as it existed May 1, 2008, or the IRC edition used in the county seat.
  - Three inspections are required: foundation, framing/MEP rough-in, and final. They may be done by a licensed engineer, a registered architect, a TREC professional inspector, an ICC-certified inspector, or a county inspector.
  - The county may require notice.
- **Floodplain** [Unverified]: Water Code ch. 16, subchapter I lets counties adopt NFIP floodplain rules and require development permits.
- **Septic (OSSF)** [Unverified]: HSC ch. 366 and 30 TAC ch. 285 require permits from the TCEQ authorized agent. In new subdivisions, lots need about 0.5 acre with public water or 1 acre with a private well (30 TAC 285.4).
- **Platting** [Unverified]: LGC ch. 232 requires a commissioners-court plat.
- **County fire code** [Unverified]: LGC 233, subchapter C (233.061 and following) applies to counties of about 250k+ population or adjacent counties. It does not apply to one- and two-family dwellings.
- **Sprinklers:** LGC 250.011 [Secondary] bars counties from requiring them.
- **ETJ** [Unverified]: SB 2038 (2023, LGC ch. 42 subchapter D, effective Sept 1, 2023) lets landowners petition or vote to leave a city's ETJ. Released land then falls under county rules only.

## 4. Windstorm (TDI, Insurance Code ch. 2210) [Unverified]
- **Where it applies:** the 14 first-tier coastal counties (Aransas, Brazoria, Calhoun, Cameron, Chambers, Galveston, Jefferson, Kenedy, Kleberg, Matagorda, Nueces, Refugio, San Patricio, Willacy), plus Harris County east of SH 146 (La Porte, Morgan's Point, Pasadena, Seabrook and Shoreacres areas).
- **Requirement:** a windstorm certificate (WPI-8) is needed for TWIA coverage. Construction must meet the TDI-adopted IRC/IBC with windstorm amendments.
- **Project cities inside the area:** Corpus Christi (Nueces), Brownsville (Cameron), League City and Galveston (Galveston), Pearland (Brazoria), and Beaumont (Jefferson).
- **Project cities outside it:** Houston proper (except areas east of SH 146), Cypress, Katy/Sugar Land (Fort Bend), and The Woodlands (Montgomery).
- **HB 1900 (2023):** its details were **not verified**. Treat any claim about it as open.

## 5. Fire sprinklers [Secondary]
- **LGC 250.011**, added by HB 738 (2021): a municipality, county or ESD "may not enact an ordinance, bylaw, order, building code, or rule requiring the installation of a multipurpose residential fire protection sprinkler system or any other fire protection sprinkler system in a new or existing one- or two-family dwelling."
- **Exceptions:** cities that had a requirement before Jan 1, 2009, and certain ESDs.
- **Practical effect:** IRC R313 is deleted or made optional.
- **Sources:** HB 738 enrolled (link above) and Allensworth https://www.allensworthlaw.com/legal-updates/hb-738/

## 6. Plumbing and electrical [Unverified]
- **Plumbing:** Occupations Code 1301.255 lets a city adopt either the IPC or the UPC. Houston uses the UPC; most DFW cities use the IPC.
- **Electrical:** Occupations Code ch. 1305 has TDLR adopt the NEC. NEC 2023 has been the statewide default since about Sept 1, 2023. A TDLR move to NEC 2026 has not been confirmed.

## 7. Permit timing and third-party inspection [Unverified]
- **LGC 214.904 (2019):** a city must grant or deny a building permit within 45 days.
- **HB 14 (2023), LGC ch. 247:** if a regulatory authority misses its review or inspection deadlines, the applicant may use a qualified third-party reviewer or inspector.
- **Unincorporated areas:** inspections come from LGC 233.154 (section 3).

## 8. Product and material preemption: HB 2439 (2019, Gov't Code ch. 3000) [Unverified]
- **The rule:** a governmental entity may not prohibit or limit a building product, material or method that a national model code published in the last three code cycles approves. This is why city masonry-percentage ordinances generally cannot be enforced against new homes after Sept 1, 2019.
- **Exceptions:**
  - historic districts and landmarks
  - certain Main Street or downtown areas
  - windstorm and fire rules
  - the energy code (SB 783 added the exception for SECO-adopted codes)
- **What still requires masonry:**
  - private deed restrictions and HOA covenants, which the statute does not reach
  - historic districts
  - some PDs or development agreements, where builders accept masonry voluntarily. This is legally contested.
- **Later changes:** no repeal or narrowing was found, apart from the SB 783 energy-code exception. DFW profiles should treat masonry % as "HOA/PD only - confirm".

## 9. 2025 housing bills [Unverified, from prior knowledge]
- **SB 15 (2025), small lots:**
  - Applies to new subdivisions of 5+ acres in cities over about 150k population in counties over about 300k.
  - The city may not require lots larger than 3,000 sq ft, width over about 30 ft, depth over about 75 ft, or setbacks above about 15 ft front, 5 ft side, 10 ft rear.
  - The city may not cap lot coverage below about 75%, and parking is limited to about 1 space.
  - Effect: narrow-lot plans become possible.
- **SB 840 (2025):** allows residential/multifamily and mixed use by right on commercial, office and retail land in large cities. It does not change detached-house design.
- **HB 24 (2025):** raises the share of owners needed for a zoning protest petition (20% to about 60% for some changes) and lowers the supermajority needed to override one. It affects rezonings, not house design.
- **HB 3699 (2023):** plat and subdivision process changes. Not verified.
- **Numbers to confirm:** all of the figures above should be checked against the enrolled text.

## 10. Expansive clay [Unverified]
- **Where:** large parts of DFW, Austin, San Antonio, Waco and Houston sit on high-plasticity clays (Blackland Prairie, Beaumont Formation).
- **How it is measured:** TxDOT Tex-124-E gives potential vertical rise (PVR). PVR above about 1 in is commonly treated as expansive. NRCS Web Soil Survey lists shrink-swell class and linear extensibility.
- **Code:** IRC R403.1.8 requires foundations on expansive soil to be designed for it.
- **Texas practice:**
  - a geotechnical report
  - a post-tensioned slab designed and sealed by a Texas PE to PTI DC10.5 (or the WRI/BRAB methods)
  - many cities require a PE-sealed foundation by local amendment
- **Engine flag:** set the expansive-soil and engineered-foundation flag to "must" statewide unless a site report shows low PVR.
