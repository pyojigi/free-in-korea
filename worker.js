// Cloudflare Workers 진입점
// /api/classify: 사진·글 판단, /api/hit: 방문 기록, /stats: 방문 통계, 나머지: public/ 정적 파일
// 방문 기록은 날짜·경로(src)·언어별 "숫자"만 저장합니다. IP·기기 정보 등 개인 정보는 저장하지 않아요.
import { onRequestPost } from "./functions/api/classify.js";

const kstDay = () => new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 10);
const clean = (v, re, max, dflt) => (typeof v === "string" && re.test(v) ? v.slice(0, max) : dflt);
const LANGS = ["ko", "en", "zh", "tw", "ja", "vi", "th", "id", "ru", "mn"];

async function bump(env, kind, src, lang) {
  if (!env.DB) return;
  try {
    await env.DB.prepare(
      "INSERT INTO hits (day, kind, src, lang, n) VALUES (?, ?, ?, ?, 1) ON CONFLICT(day, kind, src, lang) DO UPDATE SET n = n + 1"
    ).bind(kstDay(), kind, src, lang).run();
  } catch (e) { console.log("hit error", String(e)); }
}

async function stats(env, asHtml) {
  const since = new Date(Date.now() + 9 * 3600e3 - 30 * 864e5).toISOString().slice(0, 10);
  const { results } = await env.DB.prepare(
    "SELECT day, kind, src, lang, n FROM hits WHERE day >= ? ORDER BY day DESC, n DESC"
  ).bind(since).all();
  if (!asHtml) return Response.json({ since, rows: results }, { headers: { "cache-control": "no-store" } });
  const sum = (f) => { const m = {}; results.forEach(r => { const k = f(r); if (k) m[k] = (m[k] || 0) + r.n; }); return Object.entries(m).sort((a, b) => b[1] - a[1]); };
  const visits = results.filter(r => r.kind === "visit");
  const table = (title, rows) => `<h2>${title}</h2><table>${rows.map(([k, n]) => `<tr><td>${k.replace(/[<>&]/g, "")}</td><td>${n}</td></tr>`).join("") || "<tr><td>아직 없음</td><td></td></tr>"}</table>`;
  const total = visits.reduce((a, r) => a + r.n, 0), asks = results.filter(r => r.kind === "ask").reduce((a, r) => a + r.n, 0);
  const html = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Free in Korea 방문 통계</title>
<style>body{font:15px system-ui,sans-serif;margin:0 auto;max-width:640px;padding:16px;background:#f6f5f2;color:#1d2024}h1{font-size:22px}h2{font-size:16px;margin-top:22px}table{width:100%;border-collapse:collapse;background:#fff}td{border-bottom:1px solid #ddd;padding:6px 8px}td:last-child{text-align:right;font-variant-numeric:tabular-nums}.big{font-size:28px;font-weight:700}@media(prefers-color-scheme:dark){body{background:#121315;color:#eee}table{background:#1c1d20}td{border-color:#333}}</style>
<h1>Free in Korea 방문 통계 (최근 30일, 한국 시간)</h1>
<p>방문 <span class="big">${total}</span> · AI 판단 사용 <span class="big">${asks}</span></p>
<p style="color:#888">방문 = 브라우저 탭을 열 때 1번(새로고침은 안 셈). 개인 정보는 저장하지 않고 숫자만 셉니다.</p>
${table("어디서 왔나 (src)", sum(r => r.kind === "visit" && r.src))}
${table("날짜별 방문", sum(r => r.kind === "visit" && r.day))}
${table("언어별 방문", sum(r => r.kind === "visit" && r.lang))}`;
  return new Response(html, { headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" } });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/api/health") {
      // 설정 확인용: 값은 절대 보여주지 않고 이름과 키 유무만 보여줌
      return Response.json({ hasKey: !!env.ANTHROPIC_API_KEY, db: !!env.DB, names: Object.keys(env).filter(k => k !== "ASSETS") });
    }
    if (url.pathname === "/api/hit" && request.method === "POST") {
      let b = {}; try { b = await request.json(); } catch {}
      const src = clean(b.src, /^[a-z0-9][a-z0-9.\-_]*$/i, 40, "direct").toLowerCase();
      const lang = LANGS.includes(b.lang) ? b.lang : "-";
      ctx.waitUntil(bump(env, "visit", src, lang));
      return new Response(null, { status: 204 });
    }
    if (url.pathname === "/stats" || url.pathname === "/api/stats") {
      if (!env.DB) return new Response("DB not connected", { status: 500 });
      return stats(env, url.pathname === "/stats");
    }
    if (url.pathname === "/api/classify") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      const res = await onRequestPost({ request, env });
      if (res.ok) ctx.waitUntil(bump(env, "ask", "-", "-"));
      return res;
    }
    return env.ASSETS.fetch(request);
  },
};
