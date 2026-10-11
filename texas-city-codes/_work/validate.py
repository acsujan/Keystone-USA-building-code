import json, sys
LEAF_STATUS = {"Sourced", "Secondary", "Assumed"}
errs = []
def leaf(o, p):
    if not isinstance(o, dict): errs.append(f"{p}: not an object"); return
    for k in ("value", "status", "source"):
        if k not in o: errs.append(f"{p}: missing {k}")
    if o.get("status") not in LEAF_STATUS: errs.append(f"{p}: bad status {o.get('status')}")
    s = o.get("source")
    if not isinstance(s, dict) or not all(k in s for k in ("title", "url", "read")):
        errs.append(f"{p}: source needs title,url,read")
    elif o.get("status") != "Assumed" and not s.get("url"):
        errs.append(f"{p}: non-Assumed value needs url")
def chk(d, path, keys):
    for k in keys:
        if k not in d: errs.append(f"{path}.{k} missing")
for f in sys.argv[1:]:
    errs = []
    d = json.load(open(f))
    chk(d, "", ["id","name","state","counties","msa","population","climateZone","windstormCounty","codes","zoning","process","fees","cost","flood","engineChanges","plainLanguage","openQuestions","comparison"])
    for k in ["population","climateZone","windstormCounty","flood"]:
        if k in d: leaf(d[k], k)
    c = d.get("codes", {})
    if "irc" in c:
        leaf(c["irc"].get("edition"), "codes.irc.edition")
        for i, a in enumerate(c["irc"].get("amendments", [])):
            for k in ("topic","summary","status","source"):
                if k not in a: errs.append(f"codes.irc.amendments[{i}] missing {k}")
    for k in ["plumbing","electrical","fire","wind","seismic","frostDepth"]:
        leaf(c.get(k), f"codes.{k}")
    if "energy" in c: leaf(c["energy"].get("edition"), "codes.energy.edition")
    z = d.get("zoning", {})
    for k in ["hasZoning","typicalDistrict","minLotSqFt","maxHeightFt","maxLotCoverage","masonry","adu","parking"]:
        leaf(z.get(k), f"zoning.{k}")
    for k in ["front","side","rear","streetSide"]:
        leaf(z.get("setbacksFt", {}).get(k), f"zoning.setbacksFt.{k}")
    fe = d.get("fees", {})
    for k in ["permitFormula","workedExample2400sqft"]:
        leaf(fe.get(k), f"fees.{k}")
    for x in fe.get("impactFees", []) + fe.get("tapFees", []): leaf(x, "fees.list")
    co = d.get("cost", {})
    leaf(co.get("factor"), "cost.factor"); leaf(co.get("perSqFtMarket"), "cost.perSqFtMarket")
    for i, e in enumerate(d.get("engineChanges", [])):
        for k in ("id","ruleType","area","change","priority","source"):
            if k not in e: errs.append(f"engineChanges[{i}] missing {k}")
        if e.get("priority") not in ("must","should","nice"): errs.append(f"engineChanges[{i}] bad priority")
        if e.get("area") not in "setbacks massing plan structure envelope foundation estimate drawings survey".split():
            errs.append(f"engineChanges[{i}] bad area {e.get('area')}")
    print(f, "OK" if not errs else "ERRORS:\n  " + "\n  ".join(errs))
