"""문구 원본(src/)을 합쳐 public/index.html을 만듭니다.

- src/data.json      : 한국어·영어·간체 원본 + 언어 목록
- src/i18n/<code>.json : 나머지 언어 번역 (ja, vi, th, id, ru, mn …)
- 번체(tw)는 간체에서 자동 변환

사용: pip install opencc-python-reimplemented && python3 build.py
"""
import json, pathlib, sys, opencc

root = pathlib.Path(__file__).parent
d = json.loads((root / "src/data.json").read_text(encoding="utf-8"))
cc = opencc.OpenCC("s2twp")

# 1) 번역 파일 합치기
for f in sorted((root / "src/i18n").glob("*.json")):
    code = f.stem
    tr = json.loads(f.read_text(encoding="utf-8"))
    d["ui"][code] = tr["ui"]
    for key, name in tr["cat"].items():
        d["cat"][key]["n"][code] = name
    for r, t in zip(d["rules"], tr["rules"], strict=True):
        r["k"][code], r["v"][code] = t["k"], t["v"]
    for it, t in zip(d["items"], tr["items"], strict=True):
        it["t"][code] = {k: v for k, v in t.items() if k in ("name", "steps", "warn") and v}
    h = tr.get("help")
    if h:
        for n, x in zip(d["help"]["numbers"], h["numbers"], strict=True):
            n["t"][code] = x
        d["help"]["intro"]["t"][code] = h["intro"]
        d["help"]["place"]["t"][code] = h["place"]
        for sit, label in zip(d["help"]["situations"], h["situations"], strict=True):
            sit["t"][code] = label

# 2) 번체 자동 변환
conv = lambda x: [cc.convert(s) for s in x] if isinstance(x, list) else cc.convert(x)
d["ui"]["tw"] = {k: conv(v) for k, v in d["ui"]["zh"].items()}
for c in d["cat"].values():
    c["n"]["tw"] = conv(c["n"]["zh"])
for r in d["rules"]:
    r["k"]["tw"], r["v"]["tw"] = conv(r["k"]["zh"]), conv(r["v"]["zh"])
for it in d["items"]:
    it["t"]["tw"] = {k: conv(v) for k, v in it["t"]["zh"].items()}
for n in d["help"]["numbers"]:
    n["t"]["tw"] = {k: conv(v) for k, v in n["t"]["zh"].items()}
for x in (d["help"]["intro"], d["help"]["place"], *d["help"]["situations"]):
    x["t"]["tw"] = conv(x["t"]["zh"])

# 3) 빠진 번역이 없는지 검사
codes = [l["code"] for l in d["langs"]]
problems = []
for code in codes:
    if set(d["ui"].get(code, {})) != set(d["ui"]["en"]):
        problems.append(f"{code}: ui 항목 불일치")
    for k, c in d["cat"].items():
        if code not in c["n"]:
            problems.append(f"{code}: cat.{k} 없음")
    for i, r in enumerate(d["rules"]):
        if code not in r["k"] or code not in r["v"]:
            problems.append(f"{code}: rules[{i}] 없음")
    for i, it in enumerate(d["items"]):
        t = it["t"].get(code)
        if not t or len(t.get("steps", [])) != len(it["t"]["en"]["steps"]):
            problems.append(f"{code}: items[{i}] 없음 또는 단계 수 불일치")
    for i, n in enumerate(d["help"]["numbers"]):
        if code not in n["t"]:
            problems.append(f"{code}: help.numbers[{i}] 없음")
    if "{p}" not in d["help"]["place"]["t"].get(code, ""):
        problems.append(f"{code}: help.place 없음 또는 {{p}} 빠짐")
    if code not in d["help"]["intro"]["t"]:
        problems.append(f"{code}: help.intro 없음")
    for i, x in enumerate(d["help"]["situations"]):
        if code not in x["t"]:
            problems.append(f"{code}: help.situations[{i}] 없음")
if problems:
    sys.exit("번역 문제:\n" + "\n".join(problems))

import re
js = (root / "functions/api/classify.js").read_text(encoding="utf-8")
prompt = re.search(r"const prompt = language => `(.*?)`;", js, re.S).group(1)
html = (root / "src/template.html").read_text(encoding="utf-8")
sys.path.insert(0, str(root / "src")); import motifs
html = html.replace("__MOTIF_CSS__", motifs.css() + "\n" + motifs.css2())
app = (root / "src/app.js").read_text(encoding="utf-8")
app = app.replace("__PROMPT__", json.dumps(prompt, ensure_ascii=False))
html = html.replace("__SCRIPT__", app.replace("__DATA__", json.dumps(d, ensure_ascii=False)))
out = root / "public/index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
# Claude 미리보기 링크용: 문서 골격(doctype/html/head/body)을 뺀 버전
art = re.sub(r"<!doctype html>|</?html[^>]*>|</?head>|</?body>|<meta charset[^>]*>|<meta name=\"viewport\"[^>]*>", "", html)
art = art.replace("<title>", '<meta name="claude:viewport-fit-sides" content="cover">\n<title>', 1)
(root / "preview.html").write_text(art.strip() + "\n", encoding="utf-8")
print(f"built {out}: {len(codes)} languages, {len(d['items'])} items")
