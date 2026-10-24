// Cloudflare Workers 진입점: /api/classify는 사진 판단 함수로, 나머지는 public/ 정적 파일로 보냅니다.
import { onRequestPost } from "./functions/api/classify.js";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/classify") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      return onRequestPost({ request, env });
    }
    return env.ASSETS.fetch(request);
  },
};
