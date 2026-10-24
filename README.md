# Free in Korea (외국인 무료 도우미)

쓰레기 사진을 찍으면 어디에 버리는지 10개 언어로 알려주는 사이트. 지금은 이천시 기준.
언어: 한국어, English, 简体中文, 繁體中文, 日本語, Tiếng Việt, ภาษาไทย, Bahasa Indonesia, Русский, Монгол
휴대폰 언어를 보고 자동으로 고르고, 오른쪽 위에서 바꿀 수 있어요.
AI 키는 서버(Cloudflare)에만 있고, 사용자는 로그인 없이 링크만 열면 됩니다.

## 폴더 구성
- `public/index.html` — 사용자가 보는 화면 (배포되는 파일)
- `functions/api/classify.js` — 사진을 받아 Claude에게 묻는 서버 함수
- `src/data.json` — 한국어·영어·간체 원본 문구와 규칙
- `src/i18n/*.json` — 나머지 언어 번역 (AI 번역이라 원어민 검수 권장)
- `src/template.html`, `src/app.js` — 화면 틀과 동작
- `build.py` — 위 파일을 합쳐 `public/index.html`을 만듦. 번체는 간체에서 자동 변환, 빠진 번역이 있으면 멈추고 알려줌.
  문구를 고친 뒤 `pip install opencc-python-reimplemented && python3 build.py`

## 배포 순서
1. **Anthropic API 키 만들기**: console.anthropic.com 가입 → 결제수단 등록 → API Keys에서 키 생성.
   같은 곳의 사용 한도(Limits) 메뉴에서 **월 지출 한도를 꼭 낮게(예: 1~2만 원) 걸어두세요.** 누가 많이 써도 그 이상은 안 나갑니다.
2. **GitHub에 올리기**: 새 저장소(예: `icheon-sorter`)를 만들고 이 폴더 전체를 올립니다.
3. **Cloudflare Pages 연결**: Workers & Pages → Create → Pages → Connect to Git → 저장소 선택
   - Build command: 비워두기
   - Build output directory: `public`
4. **키 넣기**: 프로젝트 Settings → Variables and Secrets → Add
   - 이름 `ANTHROPIC_API_KEY`, 종류 **Secret**, 값은 1번의 키
   - 저장 후 Deployments에서 Retry deployment(재배포)
5. **확인**: `https://<프로젝트이름>.pages.dev`를 폰으로 열고 페트병 같은 걸 찍어 판단하기를 눌러보세요.

## 비용·보안
- 사진은 폰에서 긴 변 1024px로 줄여서 보내고, 서버는 저장하지 않습니다.
- 기본 모델은 가장 저렴한 Haiku(`claude-haiku-5-5`). 바꾸려면 환경변수 `MODEL`을 추가하세요.
- 다른 사이트에서 이 API를 가져다 쓰는 요청은 막아 둡니다. IP별 횟수 제한까지 걸려면 Cloudflare Rate Limiting 바인딩을 `RATE_LIMITER` 이름으로 추가하면 코드가 자동으로 사용합니다.

## 아직 확인이 필요한 것
- 이천시 정확한 배출 **시간**: 자료마다 다르게 적혀 있어 화면에는 "관리사무소 확인"으로 표시함. 확인되면 `src/data.json`의 "시간" 줄을 고치고 `build.py` 실행.

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
- `eval/photos/` 시험 사진 82장, `eval/labels.csv` 한국 기준 정답, 출처는 `eval/SOURCES.md`
- 배포 후: `pip install pillow && python3 eval/run_eval.py https://<프로젝트>.pages.dev`
- 결과: `eval/report.md`(정답률, 종류별 점수, 헷갈린 조합, 틀린 사진 목록)
