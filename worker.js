// Cloudflare Workers 진입점: /api/classify는 사진 판단 함수로, 나머지는 public/ 정적 파일로 보냅니다.
import { onRequestPost } from "./functions/api/classify.js";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/health") {
      // 설정 확인용: 값은 절대 보여주지 않고 이름과 키 유무만 보여줌
      return Response.json({ hasKey: !!env.ANTHROPIC_API_KEY, names: Object.keys(env).filter(k => k !== "ASSETS") });
    }
    if (url.pathname === "/api/classify") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      return onRequestPost({ request, env });
    }
    return env.ASSETS.fetch(request);
  },
};
