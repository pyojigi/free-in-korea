# Free in Korea (외국인 무료 도우미)

쓰레기 사진을 찍거나 이름을 적으면 어디에 어떻게 버리는지 10개 언어로 알려주는 무료 사이트.
주소: https://free-in-korea.foreigners.workers.dev
언어: 한국어, English, 简体中文, 繁體中文, 日本語, Tiếng Việt, ภาษาไทย, Bahasa Indonesia, Русский, Монгол
휴대폰 언어를 보고 자동으로 고르고, 오른쪽 위에서 바꿀 수 있어요.
AI 키는 서버(Cloudflare)에만 있고, 사용자는 로그인 없이 링크만 열면 됩니다.

## 폴더 구성
- `public/` — 사용자가 보는 화면(`index.html`, 공유 이미지 `og.png`, `robots.txt`, `sitemap.xml`)
- `worker.js`, `wrangler.jsonc` — Cloudflare Workers 진입점과 설정 (`/api/classify`, `/api/health`)
- `functions/api/classify.js` — 사진·글을 받아 Claude에게 묻는 서버 함수
- `src/data.json` — 한국어·영어·간체 원본 문구와 규칙, `src/i18n/*.json` — 나머지 언어
- `src/areas/` — '내 지역' 탭 데이터. `ko.json`은 시·구청 공식 홈페이지에서 확인한 원문, `tr_<언어>.json`은 번역
- `src/template.html`, `src/app.js`, `src/motifs.py` — 화면 틀, 동작, 나라별 그림
- `build.py` — 위 파일을 합쳐 `public/index.html`을 만듦 (번체는 자동 변환, 빠진 번역이 있으면 멈춤)
  문구를 고친 뒤 `pip install opencc-python-reimplemented && python3 build.py`
- `kit/` — 인쇄용 QR 포스터(`poster.pdf`), 나라별 홍보 글(`posts.md`), 기관·숙소용 메일 초안(`emails.md`)
- `eval/` — 시험 사진 87장과 채점기

## 배포 (지금 쓰는 방식: Cloudflare Workers + GitHub 자동 배포)
- GitHub `main`에 올리면 Cloudflare가 자동으로 다시 배포합니다 (Build command 비움, Deploy command `npx wrangler deploy`).
- API 키: Worker → Settings → **Runtime variables and secrets** → `ANTHROPIC_API_KEY` (Secret).
  Build 섹션 안의 변수 칸이 아닙니다. 잘 들어갔는지는 `/api/health`에서 `hasKey:true`로 확인.
- console.anthropic.com의 Limits에서 **월 지출 한도를 꼭 걸어두세요.**

## 비용·보안
- 사진은 폰에서 긴 변 1024px로 줄여서 보내고, 서버는 저장하지 않습니다.
- 기본 모델은 가장 저렴한 Haiku(`claude-haiku-5-5`). 바꾸려면 환경변수 `MODEL`을 추가하세요.
- 다른 사이트에서 이 API를 가져다 쓰는 요청은 막아 둡니다. IP별 횟수 제한까지 걸려면 Cloudflare Rate Limiting 바인딩을 `RATE_LIMITER` 이름으로 추가하면 코드가 자동으로 사용합니다.

## 아직 확인이 필요한 것
- 전국 데이터: 공공데이터포털 '생활쓰레기배출정보' 파일은 자동 다운로드가 막혀 있음. 직접 받거나 무료 API 키를 신청하면 전국으로 넓힐 수 있음.
- '내 지역'은 공식 홈페이지에서 확인한 곳만 넣음. 구청 사이트가 막혀 확인 못 한 곳(제주, 부산 해운대, 인천 부평·제물포, 대구 중구, 포천, 경주)은 '목록에 없음' 안내로 대신함.
- 번역은 AI 번역이라 원어민 검수 권장.

## 긴급 도움 탭
- 112·119·1330·1345 전화 버튼과 설명 (10개 언어)
- 상황과 위치를 고르면 한국어 신고 문장 + 발음 + 뜻을 보여주고, 휴대폰 음성으로 읽어줌
- 링크 끝에 `#help`를 붙이면 긴급 도움 탭으로 바로 열림 (QR용)
- 번호·운영시간 출처 (2026-10 확인):
  - 1330: https://eng.safekorea.go.kr/safekorea-eng/userful/links/eng/userfulLinks.do?menuSn=1013
  - 1345: https://immigration.go.kr/immigration/1530/subview.do
  - 112 통역(영·중 24시간): https://www.koreajoongangdaily.com/korea/police-expand-english-chinese-interpretation-for-112-hotline/10191336
  - 119 영상·문자 신고: https://www.incheon.go.kr/119/NE030401/2079152
  운영시간은 바뀔 수 있으니 반년에 한 번은 다시 확인하세요.

## 사진 판단 정확도 채점 (eval/)
- `eval/photos/` 시험 사진 87장, `eval/labels.csv` 한국 기준 정답, 출처는 `eval/SOURCES.md`
- 배포 후: `pip install pillow && python3 eval/run_eval.py https://free-in-korea.foreigners.workers.dev`
- 1차 결과 88.1%(74/84): `eval/report-v1.md`. 최신 결과: `eval/report.md`(정답률, 종류별 점수, 헷갈린 조합, 틀린 사진 목록)
