# Downloads the FREE, publicly posted reference documents for the Keystone US structural
# check and Texas city rules into the folder next to IRC2018.pdf.
#
# Run on your Windows PC (PowerShell 5+):
#   powershell -ExecutionPolicy Bypass -File .\download-free-docs.ps1
# or choose another folder:
#   powershell -ExecutionPolicy Bypass -File .\download-free-docs.ps1 -Target "D:\somewhere"
#
# Only documents the publisher posts for free download are listed. Paid or view-only
# documents (ICC codes, AWC standards, ASCE 7, PTI, ACI, WRI) are NOT downloaded;
# see README.md for where to read or buy them. Every URL below came from a
# 2026-10-12 web search; if one has moved, the log says so and README.md gives
# the publisher page to find the new link.

param(
    [string]$Target = "E:\Github\keystone\US homes types"
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# Subfolder, file name, URL
$Docs = @(
    # B9. Manufacturer engineered-lumber design guides (free from the makers)
    @("B-engineered-lumber", "Boise-Cascade-MTP-E7000-US-East-Specifier-Guide-BCI-VERSA-LAM.pdf",
      "https://cdn.mediavalet.com/usva/boisecascade/ckUra9pD3EGXsF_upl2ruQ/WvvQ6PQx1U-MLXlCbmmlVA/Large/MTP-E7000%20US%20East%20Specifier%20Gd.pdf"),
    @("B-engineered-lumber", "Boise-Cascade-MTP-W7000-West-Specifier-Guide-BCI-VERSA-LAM.pdf",
      "https://cdn.mediavalet.com/usva/boisecascade/_DgIlMz1RkGNT741XBfSEA/L72LS7z6e0yzaPGtlDC7Fw/Original/MTP-W7000%20West%20Specifier%20Guide.pdf"),
    @("B-engineered-lumber", "Weyerhaeuser-Quick-Links-Guide-SOUTHWEST-USA-2024-04-19.pdf",
      "https://www.weyerhaeuser.com/application/files/1917/1389/5641/Quick_Links_Guide_-_April_19_2024_-_SOUTHWEST_USA.pdf"),
    @("B-engineered-lumber", "Weyerhaeuser-Visual-Reference-Guide-EAST-USA.pdf",
      "https://www.weyerhaeuser.com/application/files/2816/2431/8927/Visual_Reference_Guide_-_EAST_USA.pdf"),
    @("B-engineered-lumber", "Weyerhaeuser-TB-508-1.75in-2.0E-Microllam-LVL-wall-framing-2025-05.pdf",
      "https://www.weyerhaeuser.com/application/files/1417/4803/8900/TB-508.pdf"),

    # C13. ACI 332-20 free preview (front matter only; the full code is paid)
    @("C-foundations", "ACI-332-20-preview.pdf",
      "https://www.concrete.org/Portals/0/Files/PDF/Previews/332-20_preview.pdf"),
    # C11. PTI DC10.5-19 errata and PTI publication order form (the standard itself is paid)
    @("C-foundations", "PTI-DC10.5-19-Errata-1-2022-09-17.pdf",
      "https://www.post-tensioning.org/Portals/13/Files/Images/Publications/Addenda%20and%20Errata/DC10.5-19%20Standard%20Requirements%20-%20Errata%201%20220917.pdf"),
    @("C-foundations", "PTI-Publication-Order-Form.pdf",
      "https://www.post-tensioning.org/Portals/13/Files/PDFs/Publications/PTI%20Publication%20Order%20Form.pdf"),

    # E. Texas windstorm (TDI 28 TAC 5.4013, 2024 IRC/IBC from 2026-04-01) and TWIA
    @("E-texas-windstorm", "TDI-rule-28-TAC-5.4013-adoption-20269774.pdf",
      "https://tdi.texas.gov/rules/2025/documents/20269774.pdf"),
    @("E-texas-windstorm", "Texas-Register-2026-02-13-Adopted-Rules-Title-28-Insurance.html",
      "https://www.sos.state.tx.us/texreg/archive/February132026/Adopted%20Rules/28.INSURANCE.html"),
    @("E-texas-windstorm", "TDI-Windstorm-general-information.html",
      "https://agate.tdi.texas.gov/wind/geninfo.html"),
    @("E-texas-windstorm", "TWIA-windstorm-certification.html",
      "https://www.twia.org/windstorm-certification"),

    # E. Texas statutes (free mirrors; the official site is statutes.capitol.texas.gov)
    @("E-texas-statutes", "Tex-Local-Govt-Code-214.212-IRC.html",
      "https://texas.public.law/statutes/tex._local_gov%27t_code_section_214.212"),
    @("E-texas-statutes", "Tex-Local-Govt-Code-233.153-county-residential-standard.html",
      "https://texas.public.law/statutes/tex._local_gov%27t_code_section_233.153"),
    @("E-texas-statutes", "Tex-Local-Govt-Code-233.154-county-inspections.html",
      "https://texas.public.law/statutes/tex._local_gov%27t_code_section_233.154")
)

New-Item -ItemType Directory -Force -Path $Target | Out-Null
$Log = Join-Path $Target "download-log.txt"
"Download run $(Get-Date -Format s)" | Out-File -FilePath $Log -Encoding utf8

$ok = 0; $skip = 0; $fail = 0
foreach ($d in $Docs) {
    $dir = Join-Path $Target $d[0]
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $out = Join-Path $dir $d[1]
    if (Test-Path $out) { "SKIP (exists) $($d[1])" | Tee-Object -FilePath $Log -Append; $skip++; continue }
    try {
        Invoke-WebRequest -Uri $d[2] -OutFile $out -UserAgent $UserAgent -UseBasicParsing -TimeoutSec 120
        "OK   $($d[1])" | Tee-Object -FilePath $Log -Append; $ok++
    } catch {
        if (Test-Path $out) { Remove-Item $out -Force }
        "FAIL $($d[1]) <- $($d[2]) : $($_.Exception.Message)" | Tee-Object -FilePath $Log -Append; $fail++
    }
}
"Done: $ok downloaded, $skip already there, $fail failed. Log: $Log" | Tee-Object -FilePath $Log -Append
