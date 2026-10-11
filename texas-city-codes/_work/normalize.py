"""Idempotent clean-up of city files: unify ruleType ids, add a code-edition rule per city."""
import json, glob, re
REN = {"irc-edition": "code-edition-by-city", "irc-edition-variant": "code-edition-by-city",
       "code-edition-baseline": "code-edition-by-city", "other-drainage-to-storm": "lot-drainage",
       "mechanical-cooling-required": "mechanical-cooling-required"}
def retype(e):
    t = REN.get(e["ruleType"], e["ruleType"])
    if t == "other":
        c = e["change"].lower()
        if "snow" in c: t = "snow-load"
        elif "termite" in c: t = "termite-protection"
        elif "frost" in c or "water service" in c: t = "frost-depth"
    e["ruleType"] = t
for f in sorted(glob.glob("cities/*.json")):
    d = json.load(open(f))
    for e in d["engineChanges"]: retype(e)
    if not any(e["ruleType"] == "code-edition-by-city" for e in d["engineChanges"]):
        ed = d["codes"]["irc"]["edition"]; en = d["codes"]["energy"]["edition"]
        if ed.get("value"):
            d["engineChanges"].insert(0, {
                "id": f"{d['id']}-code-edition", "ruleType": "code-edition-by-city", "area": "plan",
                "change": f"Check plans against {ed['value']} (city adoption) and energy code {en.get('value') or 'unknown'} instead of the plain 2021 IRC model"
                          + ("" if ed["status"] != "Assumed" else " - edition is Assumed, show 'confirm with city' warning"),
                "priority": "must" if "2021" not in str(ed["value"]) else "should",
                "params": {"irc": ed["value"], "energy": en.get("value"), "editionStatus": ed["status"]},
                "source": ed["source"], "derived": "added by coordinator from codes.irc.edition"})
    json.dump(d, open(f, "w"), indent=2, ensure_ascii=False)
print("normalized")
