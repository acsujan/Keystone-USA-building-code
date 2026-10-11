"""Assemble the deliverables from cities/*.json and _work/* fragments."""
import json, csv, glob, os, collections, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
cities = {}
for f in sorted(glob.glob("cities/*.json")):
    cities[json.load(open(f))["id"]] = (f, json.load(open(f)))

# 1. merge cost factors
cf = json.load(open("_work/cost-factors.json")) if os.path.exists("_work/cost-factors.json") else None
if cf:
    msas = cf["msas"]
    state = cf.get("texas") or cf.get("statewide")
    for cid, (f, d) in cities.items():
        code = str((d.get("msa") or {}).get("blsCode") or "")
        m = msas.get(code)
        if d["cost"].get("method") != "PENDING_COST_AGENT" and d["cost"]["factor"].get("value") is not None:
            continue
        src = {"id": "cost-factors", "title": "Keystone metro cost factor (BLS OEWS wages, see README cost method)", "url": cf.get("sourceUrl", "https://www.bls.gov/oes/tables.htm"), "read": "2026-10-11"}
        if m and m.get("factor") is not None:
            d["cost"]["factor"] = {"value": m["factor"], "unit": "x US national", "status": m.get("status", "Secondary"), "source": src,
                                   "note": f"MSA {code} {m.get('name','')}: labour index L={m.get('L')}, materials M={m.get('M')}. {m.get('notes','')}".strip()}
        elif state and state.get("factor") is not None:
            d["cost"]["factor"] = {"value": state["factor"], "unit": "x US national", "status": "Assumed", "source": src,
                                   "note": "No metro wage data for this place (non-metro or not in table); Texas statewide factor used."}
        d["cost"]["method"] = cf["method"]
        d["comparison"]["costFactor"] = str(d["cost"]["factor"]["value"])
        json.dump(d, open(f, "w"), indent=2, ensure_ascii=False)
        cities[cid] = (f, d)

# 2. sources.csv
rows = {}
for f in sorted(glob.glob("_work/sources-*.csv")):
    for r in csv.DictReader(open(f, encoding="utf-8")):
        if not r.get("url") and not r.get("title"): continue
        key = (r.get("url") or r.get("title")).strip()
        if key in rows:
            ids = set(filter(None, rows[key]["city_ids"].split(";"))) | set(filter(None, (r.get("city_ids") or "").split(";")))
            rows[key]["city_ids"] = ";".join(sorted(ids))
        else:
            rows[key] = {k: (r.get(k) or "").strip() for k in ["id","title","url","publisher","date_read","city_ids"]}
seen = collections.Counter()
with open("sources.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["id","title","url","publisher","date_read","city_ids"])
    w.writeheader()
    for r in sorted(rows.values(), key=lambda r: (r["city_ids"], r["id"])):
        seen[r["id"]] += 1
        if seen[r["id"]] > 1: r["id"] = f"{r['id']}-{seen[r['id']]}"
        w.writerow(r)

# 3. comparison table + engine-change stats -> _work/generated.md
cols = ["irc","energy","plumbing","district","setbacks","maxHeight","coverageFar","masonry","engFoundation","windstorm","flood","permitFeeExample","impactFees","costFactor"]
hdr = ["City","Tier","IRC edition","Energy code","Plumbing","Typical district","Front/side/rear ft","Max height","Coverage / FAR","Masonry rule","Engineer-sealed foundation","Windstorm","Flood note","Permit fee (2,400 sf example)","Impact fees","Cost factor"]
def cell(x): return str(x if x is not None else "").replace("|","/").replace("\n"," ")
order = lambda kv: (kv[1][1].get("tier", 9) if kv[1][1].get("tier") is not None else 9, kv[1][1]["name"])
lines = ["| " + " | ".join(hdr) + " |", "|" + "---|"*len(hdr)]
for cid, (f, d) in sorted(cities.items(), key=order):
    c = d.get("comparison", {})
    lines.append("| " + " | ".join([f"[{d['name']}](cities/{os.path.basename(f)})", cell(d.get("tier","fallback"))] + [cell(c.get(k)) for k in cols]) + " |")
rt = collections.defaultdict(lambda: {"cities": set(), "must": 0, "examples": []})
for cid, (f, d) in cities.items():
    for e in d.get("engineChanges", []):
        t = rt[e["ruleType"]]; t["cities"].add(cid); t["must"] += e["priority"] == "must"
        if len(t["examples"]) < 4: t["examples"].append(f"{cid}: {e['change']}")
stats = sorted(rt.items(), key=lambda kv: (-len(kv[1]["cities"]), -kv[1]["must"]))
json.dump({k: {"cities": sorted(v["cities"]), "must": v["must"], "examples": v["examples"]} for k, v in stats}, open("_work/ruletype-stats.json","w"), indent=1)
open("_work/comparison-table.md","w").write("\n".join(lines) + "\n")
print(len(cities), "cities;", len(rows), "sources;", len(rt), "rule types")
