# Reference documents for the US structural check and Texas city rules

The documents Sujan asked for on 2026-10-11 (sections A–F), with where each one can be had and whether it is free.

**Why the files are not here.** The cloud session that made this kit could not download anything (every page fetch was blocked), and it cannot write to your `E:\` drive. Most of these documents are also copyrighted and are not posted for free download. So this folder gives you:

| File | What it does |
|---|---|
| `download-free-docs.ps1` | Run it on your PC. It downloads the free documents (manufacturer guides, Texas windstorm rule, statutes, free previews and errata) into `E:\Github\keystone\US homes types\`, sorted into subfolders, with a log. |
| `hazard-lookups.csv` | The 43 Texas places with the address to type into the free ASCE Hazard Tool, the ASCE 7 edition to pick, and the file name to save each report under (item 8). |
| `city-zoning-documents.csv` | The 34 cities whose setbacks are disputed or assumed in the research. Each row has the best official link found and a search string for the zoning table (item F). |

How to run the script: open PowerShell in this folder and run `powershell -ExecutionPolicy Bypass -File .\download-free-docs.ps1`. Add `-Target "<folder>"` to save somewhere else. Links found by web search on 2026-10-12; if one has moved, the log shows FAIL and the table below names the publisher page.

## Status of every requested document

Legend: **Free download** = the script gets it. **Free view only** = you can read it online, but download and print are blocked. **Paid** = buy, or borrow through a library. Prices are given only where a store listing showed them.

### A. 2021 and 2024 IRC (chapters 3, 4, 5, 6 and 8)

| # | Document | Status | Where |
|---|---|---|---|
| 1 | 2021 IRC | Free view only, through ICC Digital Codes "Basic" access (guests can read; no copy, paste or print). Paid PDF or Premium subscription for download. | Read: codes.iccsafe.org, search "2021 IRC". Buy: shop.iccsafe.org. |
| 2 | 2024 IRC | Same as 2021. | Read: codes.iccsafe.org, search "2024 IRC". Buy: [ICC shop, 2024 IRC](https://shop.iccsafe.org/2024-international-residential-coder.html) (soft cover, loose leaf, PDF, eBook). |

The ICC Basic view does not let you print chapters to PDF, and its terms do not allow copying the text. So the legitimate ways to get the chapter 3–8 tables (section D) as files are:
1. Buy the 2021 and 2024 IRC PDFs (or Digital Codes Premium for those titles).
2. Use a library: university libraries such as Texas State and Rice often subscribe to ICC Digital Codes Premium. Check the library catalogue for "ICC Digital Codes".
3. Ask the city building department; some keep public reference copies.

For the engine itself, recording section numbers and the numeric values of tables (spans, nailing schedules) for internal use is the same approach the research package used. Copying the printed pages is the part the free view does not allow.

### B. Engineered path (beams, wide headers, shear walls)

| # | Document | Status | Where |
|---|---|---|---|
| 3 | AWC NDS 2024 + NDS Supplement (design values) | Free view only on awc.org. Search, print and zoom are only in the purchased PDF. | [2024 NDS](https://awc.org/resources/2024-nds/), [2024 NDS Supplement](https://awc.org/resources/2024-nds-supplement/). The 2018 NDS has a free view-only page too: [2018 NDS](https://awc.org/publications/2018-nds). Do not mix design values from different NDS editions. |
| 4 | AWC SDPWS 2021 | Free view only. Paid PDF: $65 from AWC, $60 with commentary from ICC. | [2021 SDPWS](https://awc.org/resources/2021-sdpws/), [ICC listing](https://shop.iccsafe.org/2021-sdpws-standard-w-commentary.html) |
| 5 | AWC WFCM 2018 / 2024 | 2024: paid ($90 with commentary from ICC). 2018: the **WFCM Workbook is a free download** from the AWC 2018 WFCM page; the full manual is paid. | [2024 WFCM](https://awc.org/resources/2024-wfcm/), [2018 WFCM](https://awc.org/resources/2018-wfcm/), [ICC 2024 WFCM](https://shop.iccsafe.org/2024-wood-frame-construction-manual-wfcm-for-one-and-two-family-dwellings-with-commentary.html) |
| 6 | AWC Span Tables for Joists and Rafters + Design Values for Joists and Rafters | 2024 and 2021 editions are on awc.org (view-only or download terms not confirmed). The 2005 edition is a free PDF. The free AWC Span Calculator uses the 2018 NDS values. | [2024 Span Tables](https://awc.org/publications/2024-span-tables), [2024 Design Values](https://awc.org/publications/2024-design-values-for-joists-and-rafters), [2021 Span Tables](https://awc.org/publications/2021-span-tables) |
| 7 | ASCE/SEI 7-22 (or 7-16), ch. 2, 4, 7, 26–30 | Paid. Only the foreword and index are free previews. ASCE's 2021 free trial (7-16/7-10) has ended. | ASCE Library / asce.org. Check a university library's ASCE Library access. Note: the 2021 IRC references ASCE 7-16; the 2024 IRC references ASCE 7-22. |
| 8 | Hazard lookups | **Free tool, no login: ASCE Hazard Tool** (wind, snow, seismic, flood, ice and others, for ASCE 7-10/16/22). **ATC Hazards by Location shut down on 2024-12-31**, and ATC points users to the ASCE tool. | [ascehazardtool.org](https://ascehazardtool.org). Use `hazard-lookups.csv`: one report per city at Risk Category II. Pick ASCE 7-16 for 2021-IRC cities and ASCE 7-22 for 2024-IRC cities. For the windstorm cities (Corpus Christi, Brownsville, League City, Pearland, Beaumont), also run ASCE 7-22, because TDI uses the 2024 IRC. |
| 9 | LVL and I-joist design guides | **Free download** (script). Boise Cascade MTP-E7000 (US East, rev. 04/26) and MTP-W7000 (West, rev. 11/25) cover BCI joists and VERSA-LAM LVL. For Weyerhaeuser, the script gets the Southwest and East quick-link/reference guides. TJ-9000 (beams, headers, columns) and TJ-4000 (TJI joists) are listed on Weyerhaeuser's specification-center pages, but no current direct PDF link was found; download them there. | [Weyerhaeuser spec center (Mid-Atlantic page lists TJ-9000/TJ-4000)](https://www.weyerhaeuser.com/woodproducts/engineered-lumber/resources/specification-center/mid-atlantic-specification-center/), [Microllam LVL beams](https://www.weyerhaeuser.com/woodproducts/engineered-lumber/microllam-lvl/microllam-lvl-beams/), Boise Cascade bc.com/ewp |

### C. Foundations

| # | Document | Status | Where |
|---|---|---|---|
| 10 | IBC 2021/2024 §1808.6 "Design for expansive soils" | Free view only (ICC Digital Codes, as for the IRC). | codes.iccsafe.org, "2021 IBC", chapter 18. Practical summaries: [LADBS expansive-soil bulletin](https://ladbs.org/docs/default-source/publications/information-bulletins/building-code/foundation-design-for-expansive-soils-ib-p-bc2017-116.pdf?sfvrsn=18), [LA County BCM 1808.6](https://www.pw.lacounty.gov/bsd/lib/fp/Building/Building%20Code%20Manuals/2017/BCM%201808.6%20A1%20-%20Foundation%20Requirements%20on%20Expansive%20Soil.pdf) (2017 cycle). |
| 11 | PTI DC10.5-19 (PT slabs on expansive and stable soils) | Paid, from PTI. The script gets the errata and the PTI order form (price not visible in search). | post-tensioning.org publications |
| 12 | WRI "Design of Slab-on-Ground Foundations" | Not found as a download. The WRI method is reproduced in **ACI 360R Appendix 2** (paid, ACI). Contact the Wire Reinforcement Institute for the original. | ACI 360R: concrete.org |
| 13 | ACI 332-20 "Code Requirements for Residential Concrete" | Paid. The current title differs; "Residential Code Requirements for Structural Concrete" was the 332-10 title. The script gets the free preview. | concrete.org, or [ICC shop ACI 332-20](https://shop.iccsafe.org/aci-332-20-code-requirements-for-residential-concrete.html) |

### D. If only the free view: the listed IRC tables

Use the ICC Basic view to read and check each table: R301.2(1), R301.5, R401.4.1, R403.1(1), R404 tables, R502.3.1(1)/(2), R602.3(5)/(6), R602.7(1)/(2), R602.10.x, R802.4.1, R802.5.1. Saving them as files needs one of the three routes under A. The values most often needed for 2021 and 2024 can be checked against the 2018 IRC you already have, plus each edition's "Significant Changes" book (ICC, paid), which lists what moved between editions.

### E. Energy and windstorm

| Document | Status | Where |
|---|---|---|
| 2021 / 2024 IECC residential (Table R402.1.2) | Free view only (ICC). Texas statewide is still the 2015 IRC chapter 11 / 2015 IECC; SECO's 2024 update was not final as of the research. | codes.iccsafe.org |
| TDI 28 TAC §5.4013 (2024 IRC/IBC for windstorm from 2026-04-01) | **Free download** (script): TDI rule PDF and the Texas Register adoption of 2026-02-13. | [TDI rule PDF](https://tdi.texas.gov/rules/2025/documents/20269774.pdf), [Texas Register 2026-02-13](https://www.sos.state.tx.us/texreg/archive/February132026/Adopted%20Rules/28.INSURANCE.html) |
| TWIA windstorm certification requirements (WPI-8) | **Free** (script saves the page). | [TWIA windstorm certification](https://www.twia.org/windstorm-certification), [TDI windstorm info](https://agate.tdi.texas.gov/wind/geninfo.html) |
| Tex. Local Gov't Code §214.212, §233.153, §233.154 | **Free** (script saves texas.public.law copies). The official text is at statutes.capitol.texas.gov. | texas.public.law |

### F. City zoning tables (for the architect)

See `city-zoning-documents.csv`: 34 cities, with the typical district, the current values and their status, the best official link found, and a search string for Municode, AmLegal or eCode360. For any real lot, the **recorded plat** (county clerk) and the **PD ordinance** (if the lot is in a Planned Development) override the base district. Ask for both.

## Cost to buy the paid set (where prices were visible)

| Item | Price seen |
|---|---|
| SDPWS 2021 PDF | $65 (AWC) / $60 with commentary (ICC) |
| WFCM 2024 with commentary | $90 (ICC; $81 for members) |
| PTI DC10.1 design guide (for comparison) | $71.50 non-member |
| 2021 and 2024 IRC, ASCE 7-22, PTI DC10.5-19, ACI 332-20, NDS 2024 | price not shown in search; check the stores |
