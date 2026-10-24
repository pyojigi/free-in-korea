"""사진 판단 정확도 채점기

배포된 사이트의 /api/classify에 시험 사진을 하나씩 보내고, 한국 기준 정답(labels.csv)과 비교해
eval/report.md(요약)와 eval/results.csv(사진별 결과)를 만듭니다.

사용:
  pip install pillow
  python3 eval/run_eval.py https://<프로젝트>.pages.dev        # 전체
  python3 eval/run_eval.py https://<프로젝트>.pages.dev 5      # 앞의 5장만

API 키는 필요 없습니다(사이트 서버에 있는 키를 씀). 사진 1장 = AI 호출 1번이니 지출 한도 안에서 돌리세요.
"""
import base64, csv, io, json, pathlib, sys, time, urllib.request, urllib.error
from collections import Counter, defaultdict
from PIL import Image

HERE = pathlib.Path(__file__).parent
CATS = ["bag", "food", "rec", "spec"]
KO = {"bag": "종량제", "food": "음식물", "rec": "재활용", "spec": "따로 배출"}


def shrink(path):
    im = Image.open(path).convert("RGB")
    im.thumbnail((1024, 1024))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=80)
    return base64.b64encode(buf.getvalue()).decode()


def ask(url, image):
    req = urllib.request.Request(url.rstrip("/") + "/api/classify",
        data=json.dumps({"image": image, "mediaType": "image/jpeg", "lang": "en"}).encode(),
        headers={"content-type": "application/json", "user-agent": "Mozilla/5.0 (free-in-korea eval)"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        try: return None, json.load(e).get("error", str(e.code))
        except Exception: return None, str(e.code)
    except Exception as e:
        return None, type(e).__name__


def main():
    if len(sys.argv) < 2:
        sys.exit("사용: python3 eval/run_eval.py https://<프로젝트>.pages.dev")
    url = sys.argv[1]
    rows = list(csv.DictReader(open(HERE / "labels.csv", encoding="utf-8")))
    if len(sys.argv) > 2: rows = rows[: int(sys.argv[2])]  # 앞에서 몇 장만 시험할 때
    results = []
    for i, row in enumerate(rows, 1):
        r, err = ask(url, shrink(HERE / "photos" / row["file"]))
        first = (r or {}).get("items", [{}])[0] if r else {}
        got = first.get("cat", "ERROR") if r else "ERROR"
        results.append({**row, "got": got, "item": first.get("name", ""), "found": len((r or {}).get("items", [])),
                        "confident": (r or {}).get("confident", ""), "error": err or ""})
        mark = "O" if got == row["answer"] else "X"
        print(f"[{i}/{len(rows)}] {mark} {row['file']}: 정답 {row['answer']} / AI {got} {('('+err+')') if err else ''}", flush=True)
        if err == "busy": time.sleep(10)
        time.sleep(1)

    with open(HERE / "results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys())); w.writeheader(); w.writerows(results)

    ok = [r for r in results if r["got"] != "ERROR"]
    right = sum(r["got"] == r["answer"] for r in ok)
    by = defaultdict(lambda: [0, 0])
    conf = Counter()
    for r in ok:
        by[r["answer"]][1] += 1; by[r["answer"]][0] += r["got"] == r["answer"]
        conf[(r["answer"], r["got"])] += 1
    lines = [f"# 사진 판단 채점 결과", "",
             f"- 사이트: {url}", f"- 날짜: {time.strftime('%Y-%m-%d %H:%M')}",
             f"- 사진 {len(results)}장 중 응답 {len(ok)}장, 오류 {len(results)-len(ok)}장",
             f"- **정답률: {right}/{len(ok)} = {100*right/max(1,len(ok)):.1f}%**", "",
             "## 정답 종류별", "", "| 정답 | 맞힘 | 정답률 |", "|---|---|---|"]
    for c in CATS:
        a, n = by[c]
        if n: lines.append(f"| {KO[c]} | {a}/{n} | {100*a/n:.0f}% |")
    lines += ["", "## 헷갈린 조합 (정답 → AI 답)", "", "| 정답 \\ AI | " + " | ".join(KO[c] for c in CATS) + " |",
              "|---|" + "---|" * len(CATS)]
    for a in CATS:
        lines.append(f"| {KO[a]} | " + " | ".join(str(conf[(a, g)]) for g in CATS) + " |")
    miss = [r for r in ok if r["got"] != r["answer"]]
    lines += ["", f"## 틀린 사진 ({len(miss)}장)", ""]
    for r in miss:
        lines.append(f"- `{r['file']}` {r['note']}: 정답 {KO[r['answer']]}, AI는 {KO.get(r['got'], r['got'])} (AI가 본 물건: {r['item']})")
    (HERE / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n" + "\n".join(lines[:8]))
    print(f"\n자세한 결과: {HERE/'report.md'}")


if __name__ == "__main__":
    main()
