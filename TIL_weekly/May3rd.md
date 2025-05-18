# 5월 3주차 TIL

---

## 진행 파일 목록

`May3rd.md`, `save_twitter_cookies.py`, `save_twitter_login.py`, `scrape_tweets_api.py`,  
`scrape_twitter_with_cookies.py`, `twitter_cookies.json`, `project_diary.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._

---

## 3차 평가 (16.05.25에 예정) - 엘라스틱서치

### 지필평가

#### 1장

- 1장 1절: Restful API  
- 1장 2절: 역색인 구조 등 엘라스틱서치의 장점과 차별점  

#### 3장 데이터 모델링

- 매핑 API (데이터를 어떻게 집어넣을지에 대한 구조 이해)  
- 3장 3절:  

    ```
    데이터 타입 (필드에 어떤 데이터를 저장하는지)  
    - 문자열, 날짜 등 비교 (숫자끼리, 객체끼리, geo 끼리)  
    - `키워드`와 `텍스트`의 차이가 핵심 (엘라스틱의 목표는 전문 검색(역색인))
    ```

- 3장 4절: 엘라스틱서치 분석기  

    ```
    분석기의 흐름과 역할 이해
    ```

`Notion`에서 코드 내용을 실습평가로 진행 예정

### 엘라스틱서치 필수 개념

- **Restful API**  
HTTP 메서드를 활용해 데이터를 조회, 생성, 수정, 삭제하는 REST 원칙 준수 API

- **역색인 (Inverted Index)**  
텍스트 검색 최적화 자료구조로, 단어별로 문서 리스트를 저장하여 빠른 검색 지원

- **매핑 (Mapping)**  
엘라스틱서치에서 데이터 구조 및 필드 타입(문자열, 날짜 등)을 정의하는 과정  
`keyword`(정확 검색용)와 `text`(전문 검색용)의 차이점 이해 필수

- **분석기 (Analyzer)**  
텍스트를 토큰화하고 불용어 제거, 형태소 분석 등을 수행하여 인덱싱과 검색을 돕는 구성요소

> 엘라스틱서치는 역색인 기반 전문 검색에 최적화된 검색엔진으로,  
> 효율적인 데이터 모델링과 분석기 설정을 통해 정밀한 검색 결과를 제공합니다.

---

## 트위터 데이터 수집 시도 및 실패 경험

### X API를 활용한 트윗 분석

- Colab에서 실습 진행  
- 무료 계정 기준 1회 요청에 15~30분 소요  

```bash
!pip install tweepy
```
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = (
    "(포카 OR 포토카드 OR 응원봉 OR 굿즈) "
    "(양도 OR 양도해요 OR 양도합니다 OR 넘깁니다 "
    "OR 판매 OR 팝니다 "
    "OR 구매 OR 구합니다 OR 구해요 OR 삽니다 OR 급구 OR 구매해요 OR 구매 원해요) "
    "lang:ko since:2024-04-01 until:2024-05-10"
)

max_tweets = 1000

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_tweets:
        break
    tweets.append([tweet.date, tweet.content])

df = pd.DataFrame(tweets, columns=["created_at", "text"])
df.to_csv("goods_tweets.csv", index=False, encoding="utf-8-sig")
print(f" 총 {len(df)}개의 트윗이 goods_tweets.csv에 저장되었습니다.")
```
---

## 실패 사례 및 원인 분석

- `snscrape` 패키지를 이용한 트윗 수집 시도 중  
  Python 3.13, 3.11 버전과 충돌 발생 → Python 3.10으로 다운그레이드했으나 실패 지속

- `snscrape` 자체가 Twitter가 X로 전환되면서 보안 강화로 인해 차단된 것으로 추정

---

## Selenium과 쿠키 활용 스크랩 자동화 시도

- Selenium으로 로그인된 X 페이지 접근 자동화 시도  
- `twitter_cookies.json` 파일에 로그인된 쿠키 정보를 저장해 재사용하는 방식으로 성공  
- 하지만 3회 이상 자동 요청 시도 시 차단 발생  
- 공식 X API 미사용으로 지속적 데이터 수집은 어려운 상황

---

# Project 진행 Diary

### Django 중고거래 게시글 상세 페이지 컴포넌트 분리 및 UI 개선

---

## 프로젝트 개요 및 문제 상황

- Django로 만든 중고거래 웹사이트 게시글 상세 페이지 UI가 지나치게 복잡하고 중복된 코드가 많아 유지보수가 어려웠음

- 제목, 가격, 작성자 정보, 구매/찜/문의 버튼, 상품 상태, 설명, 작성자 전용 수정/삭제 버튼 등이 한 템플릿에 몰려 있어 가독성 저하

- 버튼 위치와 스타일 등 UI/UX 측면에서도 개선 필요

---

## 목표 및 개선 방향

- UI를 역할별로 명확히 나누고 컴포넌트로 분리해 코드 중복과 복잡도 감소, 유지보수성 향상

- 게시글 핵심 정보(제목, 가격, 작성자, 구매/찜/문의 버튼)는 `header_ui` 컴포넌트에,  
  상품 상세 정보(상품 상태, 설명 등)는 `content_ui` 컴포넌트에 각각 배치

- 작성자 전용 버튼(수정/삭제/판매완료)은 문의하기 버튼 아래 위치로 이동

- 버튼 스타일을 TailwindCSS로 깔끔하고 일관되게 수정

- 가격 정보는 크게, 오른쪽 정렬로 배치해 시각적 집중도 향상

---

## 주요 작업 내용

- `detail.html`에서 두 컴포넌트를 include 하여 역할 분리

- `components/post/_header_ui.html`  
  - 제목, 가격, 판매 상태, 작성자 프로필, 구매/찜/문의 버튼 담당  
  - 작성자 전용 버튼은 문의하기 버튼 아래 위치

- `components/post/_content_ui.html`  
  - 상품 상세 상태 정보(카테고리, 상태, 교환여부, 직거래 여부, 배송방법) 및 상품 설명 담당

- 버튼 크기, 색상, 간격, 호버 효과를 TailwindCSS 유틸리티 클래스로 일관성 있게 적용

- 불필요한 중복 제거 및 주석 추가로 코드 가독성 및 유지보수성 향상

---

## 프로젝트 폴더 구조 (핵심 부분)
```
ddokfarm/
├── migrations/
├── templates/
│ └── components/
│ ├── comment/
│ │ ├── _form_ui.html
│ │ └── _list_ui.html
│ └── post/
│ ├── _content_ui.html # 상품 상세 정보 테이블 및 설명
│ ├── _header_ui.html # 게시글 헤더 (제목, 가격, 작성자, 구매/찜/문의 버튼)
│ ├── _card_ui.html
│ ├── _form_ui.html
│ └── _post_card_ui.html
│ └── ddokfarm/
│ ├── detail.html # 상세 페이지 메인 템플릿, 컴포넌트 포함
│ ├── index.html
│ ├── create.html
│ └── update.html
├── models.py
├── views.py
├── urls.py
└── forms.py

yaml
Copy
```


---

## 각 파일별 역할

- **detail.html**  
  게시글 상세 페이지 메인 템플릿으로,  
  `header_ui`와 `content_ui` 컴포넌트를 포함하며 댓글 폼과 댓글 목록도 함께 보여줌.  
  작성자 전용 버튼도 여기서 관리.

- **components/post/_header_ui.html**  
  게시글 핵심 정보(제목, 가격, 판매 상태, 작성자 프로필)와  
  사용자 행동 유도 버튼(구매하기, 찜하기, 문의하기)을 담당.  
  작성자 전용 버튼은 문의하기 버튼 아래 배치.

- **components/post/_content_ui.html**  
  상품 상세 상태 정보(카테고리, 상태, 교환여부, 직거래 여부, 배송방법)와  
  상품 설명 텍스트를 테이블 형식으로 보여주는 역할.

- **views.py**  
  게시글 생성, 수정, 삭제, 상세보기, 댓글 생성 및 삭제 기능 구현.

---

## 배운 점 및 의의

- Django 템플릿 컴포넌트 분리를 통해 UI 관리가 훨씬 간편해지고, 코드 중복이 줄어듦

- TailwindCSS 유틸리티 클래스를 활용한 UI 스타일링은 일관성을 유지하면서도 빠르게 수정 가능

- 사용자 행동 흐름에 맞춰 버튼 위치와 크기를 조정하는 것이 UX에 큰 영향을 줌

- 작성자 전용 기능을 분리해 관리함으로써 권한별 UI 표시가 명확해지고 유지보수가 쉬워짐

---

## 향후 계획

- 댓글 UI 개선 및 실시간 반영 기능 추가

- 모바일 반응형 디자인 세밀화

- Django CBV 도입 검토 및 코드 리팩토링

- 사용자 피드백을 반영한 UI/UX 고도화

---
