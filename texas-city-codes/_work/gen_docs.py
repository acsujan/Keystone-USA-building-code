"""Generate README.md and engine-change-catalogue.md from cities/*.json (run after build.py)."""
import json, glob, os, collections, sys, csv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
sys.path.insert(0, "_work"); from catalogue_meta import META
C = {}
for f in sorted(glob.glob("cities/*.json")):
    d = json.load(open(f)); C[d["id"]] = d
def statuses(o, st):
    if isinstance(o, dict):
        if "status" in o and "source" in o: st[o["status"]] += 1
        for v in o.values(): statuses(v, st)
    elif isinstance(o, list):
        for v in o: statuses(v, st)
    return st
tierName = {0: "fallback", 1: "1", 2: "2"}
cities = [d for d in C.values() if d.get("tier") in (1, 2)]
fallbacks = [d for d in C.values() if d.get("tier") not in (1, 2)]
# rule stats
rt = collections.defaultdict(lambda: {"cities": set(), "must": 0, "should": 0, "nice": 0, "items": []})
for d in C.values():
    for e in d["engineChanges"]:
        r = rt[e["ruleType"]]; r["cities"].add(d["id"]); r[e["priority"]] += 1; r["items"].append((d["id"], e))
ranked = sorted(rt.items(), key=lambda kv: (-len([c for c in kv[1]["cities"] if C[c].get("tier") in (1,2)]), -kv[1]["must"]))
def ncity(r): return len([c for c in r["cities"] if C[c].get("tier") in (1,2)])
# completeness
def completeness(d):
    st = statuses(d, collections.Counter()); n = sum(st.values())
    return st, (st["Sourced"] + st["Secondary"]) / n if n else 0
rows = []
for d in sorted(cities, key=lambda d: (d["tier"], d["name"])):
    st, pct = completeness(d)
    rows.append((d, st, pct))
cmpcols = ["irc","energy","plumbing","district","setbacks","maxHeight","coverageFar","masonry","engFoundation","windstorm","flood","permitFeeExample","impactFees","costFactor"]
hdr = ["City","Tier","IRC edition","Energy code","Plumbing","Typical district","Front/side/rear (ft)","Max height","Coverage / FAR","Masonry rule","Engineer-sealed foundation","Windstorm","Flood note","Permit fee, 2,400 sf example","Impact fees","Cost factor"]
def cell(x): return str(x if x not in (None, "") else "–").replace("|", "/").replace("\n", " ")
T = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
T.append("| **IRC-2021 model (Keystone today)** | – | 2021 IRC | 2021 IECC ch. 11 | IPC | – | user value | 35 ft (no IRC limit) | – | none | no | no | none | – | none | 0.95 (single TX) |")
for d in sorted(fallbacks, key=lambda d: d["id"]) + [r[0] for r in rows]:
    c = d.get("comparison", {})
    T.append("| " + " | ".join([f"[{d['name']}](cities/{d['id']}.json)", tierName.get(d.get("tier"), "fallback")] + [cell(c.get(k)) for k in cmpcols]) + " |")
open("_work/comparison-table.md", "w").write("\n".join(T) + "\n")
# completeness table
CT = ["| City | Tier | Researched values (Sourced+Secondary) | Assumed | Share researched | Engine changes |", "|---|---|---|---|---|---|"]
for d, st, pct in rows + [(d, *completeness(d)) for d in fallbacks]:
    CT.append(f"| {d['name']} | {tierName.get(d.get('tier'),'fallback')} | {st['Sourced']+st['Secondary']} | {st['Assumed']} | {pct:.0%} | {len(d['engineChanges'])} |")
# top 10
TOP = ["| # | Rule type | Cities needing it (of %d) | must / should / nice | What the engine does |" % len(cities), "|---|---|---|---|---|"]
for i, (k, r) in enumerate(ranked[:10], 1):
    TOP.append(f"| {i} | `{k}` | {ncity(r)} | {r['must']} / {r['should']} / {r['nice']} | {META.get(k, (k, ''))[1][:220]} |")
# not found by city
NF = []
for d, st, pct in rows + [(d, *completeness(d)) for d in fallbacks]:
    nf = d.get("notFound") or []
    if nf: NF.append(f"- **{d['name']}:** " + "; ".join(str(x) for x in nf[:12]) + (" …" if len(nf) > 12 else ""))
json.dump({"top": [k for k, _ in ranked[:10]]}, open("_work/top.json", "w"))
open("_work/generated-blocks.md", "w").write("\n".join(["<!--COMPARISON-->"] + T + ["<!--COMPLETENESS-->"] + CT + ["<!--TOP-->"] + TOP + ["<!--NOTFOUND-->"] + NF))
# catalogue
L = ["# Engine change catalogue", "", "All engine changes from the city files, grouped into rule types. Each rule type is one thing the Keystone engine must learn to do. For each: what it does, the survey input it needs, the cities that use it, and a sketch of the data. Counts are cities (tier 1 + tier 2, not the two fallback profiles) that have at least one change of that type.", "", "Rule types are ranked by the number of cities that need them.", ""]
L.append("| Rule type | Cities | must | should | nice |"); L.append("|---|---|---|---|---|")
for k, r in ranked: L.append(f"| [`{k}`](#{k}) | {ncity(r)} | {r['must']} | {r['should']} | {r['nice']} |")
L.append("")
for k, r in ranked:
    title, what, inp, sketch = META.get(k, (k, "(no catalogue description yet)", "", "{}"))
    L += [f"## {k}", "", f"**{title}.** {what}", "", f"- **Survey input:** {inp}", f"- **Cities ({ncity(r)}):** " + ", ".join(sorted(c for c in r["cities"])),
          f"- **Priority mix:** {r['must']} must, {r['should']} should, {r['nice']} nice", "- **Data sketch:**", "", "```json", sketch, "```", "", "Examples from the city files:", ""]
    for cid, e in r["items"][:6]:
        s = e.get("source") or {}
        L.append(f"- `{cid}` ({e['priority']}, {e['area']}): {e['change']}" + (f" — source: [{s.get('title','')[:80]}]({s.get('url')})" if s.get("url") else " — source: " + s.get("title", "Assumed")[:80]))
    if len(r["items"]) > 6: L.append(f"- … and {len(r['items'])-6} more in the city files.")
    L.append("")
open("engine-change-catalogue.md", "w").write("\n".join(L) + "\n")
print("docs generated;", len(cities), "cities,", len(fallbacks), "fallbacks,", len(ranked), "rule types")
