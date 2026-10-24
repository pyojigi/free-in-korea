# 시험 사진 출처

- `biological_*, battery_*, cardboard_*, clothes_*, glass_*, metal_*, paper_*, plastic_*, shoes_*, trash_*`
  Hugging Face `omasteam/waste-garbage-management-dataset` (MIT 라이선스) 에서 종류별 8장씩 무작위 추출.
  정답(answer)은 한국 분리배출 기준으로 사진을 직접 보고 다시 붙임 (예: 유리컵·와인잔은 재활용이 아니라 따로 배출, 옷·신발은 의류수거함).
  판단이 애매한 3장(합판처럼 보이는 종이, 은박지, 은박 접시)은 제외.
- `commons_*` — Wikimedia Commons 자유 이용 사진 (파일별 원본 제목은 labels.csv의 source_class 칸).

## 아직 부족한 것
- 뼈 1장, 영수증 3장, 호두 껍데기 1장, 계란 껍데기 1장만 확보. 조개껍데기·복숭아씨는 쓸 만한 자유 이용 사진을 못 찾음 → 한국에서 가장 많이 틀리는 항목이라 실제 사진 10장 정도 추가 권장.
- 대부분 깨끗한 배경의 상품 사진이라 실제 쓰레기장 사진보다 쉬움 → 실제 정확도는 이 점수보다 낮을 수 있음.
