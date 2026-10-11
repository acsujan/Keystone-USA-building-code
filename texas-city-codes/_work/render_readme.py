import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
t = open("_work/README.template.md").read()
g = open("_work/generated-blocks.md").read()
blocks = dict(re.findall(r"<!--(\w+)-->\n(.*?)(?=\n<!--\w+-->|\Z)", g, re.S))
cf = json.load(open("_work/cost-factors.json"))
rows = ["| Metro (BLS code) | Trades found | Labour index L | Cost factor |", "|---|---|---|---|"]
for code, m in sorted(cf["msas"].items(), key=lambda kv: -(kv[1].get("factor") or 0)):
    n = sum(1 for w in m.get("wages", {}).values() if w.get("value"))
    rows.append(f"| {m['name']} ({code}) | {n}/5 | {m.get('L') if m.get('L') is not None else '–'} | {m.get('factor') if m.get('factor') is not None else 'use 19100 (0.95)'} |")
rows.append(f"| **Texas statewide** | 5/5 | {cf['texas']['L']} | **{cf['texas']['factor']}** |")
spot = open("_work/spotchecks.md").read().split("\n", 1)[1].strip()
nr = len(json.load(open("_work/ruletype-stats.json")))
for k, v in {"COMPARISON": blocks["COMPARISON"], "TOP": blocks["TOP"], "COMPLETENESS": blocks["COMPLETENESS"], "NOTFOUND": blocks.get("NOTFOUND", ""), "COSTTABLE": "\n".join(rows), "SPOT": spot, "NRULES": str(nr)}.items():
    t = t.replace(k, v.strip())
open("README.md", "w").write(t)
print("README", len(t))
