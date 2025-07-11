# 6월 4주차 TIL

---

## 진행 파일 목록

`project_diary.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._

---
## 프로젝트 진행
- `project_diary.md` 참고

- 이번주 프로젝트 TO DO
---
# 어덕해 프로젝트 TIL 정리

## 프로젝트 개요

- 팬덤 기반 플랫폼으로서 생일카페 등록 서비스인 덕생, 중고 굿즈 거래 플랫폼 덕팜, 후기/예절 기반 커뮤니티 덕담, 실시간 채팅 기능을 통합하고 있음.
- Django 백엔드, Tailwind 기반 프론트, Kakao Maps API, JavaScript 유틸 모듈 구조로 구성됨.
- 사용자 중심의 기능 흐름과 모바일 대응을 최우선으로 고려해 구현 중임.

---

## 이번 주 구현 요약 (6월 17일 ~ 6월 23일) & 계획

### 덕생 관련

- 생일카페 등록폼을 멀티스텝 구조로 구현함.
- 스텝별 유효성 검사 로직은 js 모듈에서 통합 관리함.
- 이미지 업로드는 삭제/순서 변경 포함한 미리보기 기능까지 포함됨.
- 상세페이지에서 이미지 슬라이드로 출력되도록 구성함.
- Kakao Maps 기반 지도 구현 완료
  - 마커 클릭 시 카드 출력
  - 내 위치 기반 거리 및 도보 시간 계산 포함됨
- FullCalendar 기반 주간/월간 생일 캘린더 구현함.
- 찜 기능은 통합 관리되며, 캐러셀 반영과 Ajax 갱신까지 구현됨.

### 덕팜 관련

- 게시글 카드 UI 전면 개편함.
- 판매/대여/분철 필터링 기능 추가됨.
- 가격 범위 필터, 정렬 기능 구현함.
- 찜 상태 유지 및 모바일 대응 보완됨.

### 채팅 기능

- WebSocket 기반 채팅방 구조 구현함.
- 이미지 전송, 거래 완료 상태 반영, 채팅 차단 기능까지 적용함.
- 리뷰 작성 폼 연결 및 계좌/주소 복사 기능 구현됨.
- 채팅방 리스트 UI를 고도화하고 거래글 정보 연동 완료함.

### 덕담 기능

- 예절샷 지도 연동, 댓글 알림 개선, 생일 후기 ↔ 덕생 게시글 연결 등 구현함.
- 공식 팬 마크 모바일 대응 완료함.

---

## 기능별 할 일 목록 (최종 정리)

<details>
<summary><strong>덕생</strong></summary>

- [x] 찜 캐러셀 및 스와이프 안내 구현
- [x] 중복 등록 확인 기능 완성
- [x] 검색 필터 정확도 개선 (멤버명 분기)
- [x] 주변 생일카페 필터링 완료
- [x] @ 제거 자동 처리
- [x] pagination 개선
- [x] 우측 네비게이션 UI 구성
- [ ] tour_map.html에서 찜한 카페만 표시
- [ ] 로그인 비회원 시 리다이렉트 강화
- [ ] 불필요 기능 및 모델 필드 정리

</details>

<details>
<summary><strong>덕팜</strong></summary>

- [x] 전체 UI 및 반응형 대응
- [x] 카드 정보 정리 (제목/가격/팬마크)
- [x] 필터링/정렬 기능 구현
- [x] 찜 상태 유지 구현
- [x] 작성 시간 표기 포맷 적용
- [ ] 게시글 신고 기능 고도화
- [ ] 게시글 편집됨 표시 기능 예정

</details>

<details>
<summary><strong>채팅</strong></summary>

- [x] 채팅 기본 구조 구현
- [x] 거래 완료 시 차단 처리
- [x] 이미지 첨부 기능 구현
- [x] 계좌/주소 복사 기능
- [x] 리뷰 폼 연결 완료
- [ ] 채팅방 URL UUID화
- [ ] 가격 오류 수정
- [ ] 분철 채팅방 모델링 검토 중

</details>

<details>
<summary><strong>덕담</strong></summary>

- [x] 전체 UI 리디자인
- [x] 지도 연동 (예절샷)
- [x] 게시글 연동 (생카 후기 → 덕생)
- [x] 댓글 알림 개선
- [x] 팬마크 모바일 대응
- [ ] 아티스트/멤버 통합 검색 기능 보완 예정

</details>

<details>
<summary><strong>마이페이지</strong></summary>

- [x] 팬덤 인증 시 찜 아티스트 우선 노출
- [x] 계좌/주소 등록 기능 구현
- [x] 온라인 상태 제거
- [x] 공개 프로필 정리
- [ ] 비밀번호 찾기 기능 예정
- [ ] 공개 프로필 UI 개선 예정

</details>

<details>
<summary><strong>공통 시스템 기능</strong></summary>

- [x] 신고 기능 구현 완료
- [x] 회원가입 시 아티스트 설정창 연결
- [ ] 알림 기능 정리 예정 (승인/인증/채팅)
- [ ] FAQ 문구 보완
- [ ] helpers 유틸 함수 통합 고려
- [ ] 관리자 페이지 통합 필요
- [ ] 콘솔 로그 제거 / 404 페이지 개선

</details>

<details>
<summary><strong>멘토링 및 포인트 시스템</strong></summary>

- [x] 생일 퀴즈 → 포인트 제공 기능 구현
- [ ] 리뷰 작성 시 포인트 지급 기능 예정
- [ ] 포인트 마이페이지에서 조회 기능 예정
- [ ] 생일카페 방문, 분철 성공 시 포인트 지급 검토

</details>

<details>
<summary><strong>최종 배포 준비</strong></summary>

- [ ] 이미지 저장 구조 → S3 적용 준비
- [ ] 게시글 편집 표시 기능 적용 예정
- [x] 생일 정보(csv) 정정 완료
- [ ] 마커 이미지 커스터마이징 예정
- [ ] 후순위 항목 정리 (배송비, 예약 기능 등)

</details>

---

## 배운 점 / 개선 포인트

- Django 뷰/컨텍스트/템플릿 구조를 일관되게 구성하면 재사용성과 유지보수성이 높아짐.
- JavaScript 모듈화를 철저히 하면 기능별 디버깅과 확장성이 좋아짐.
- 지도 기능은 유틸 함수화하여 다양한 뷰에서 재활용하는 것이 중요함.
- 실시간 채팅 기능은 이벤트 흐름 관리와 예외 처리가 핵심임.
- 백엔드-프론트 간 컨벤션을 명확히 설정해 두는 것이 전체 개발 속도에 큰 영향을 줌.

---

## 디렉토리 구조 예시

```
ddoksang/
├── templates/
│ └── ddoksang/
│ ├── components/
│ │ ├── _cafe_card.html
│ │ ├── _favorites_section.html
│ │ └── ...
│ ├── detail.html
│ ├── create.html
│ ├── tour_map.html
│ └── ...
├── static/
│ ├── js/
│ │ ├── ddoksang_create.js
│ │ ├── ddoksang_detail.js
│ │ └── ...
│ └── css/
│ └── ddoksang_detail.css
```