
*4월 5주차*

- elasticSearch
> `tableu.md`, `elasticSearch.md`, `korean_analysis.md`, `search.md`, `search2.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._


---

# Tableau
# 데이터 시각화
> 
> https://help.tableau.com/current/guides/get-started-tutorial/en-us/get-started-tutorial-home.htm?_gl=1*1d87mx9*_ga*MTQwMzk0NzAxOC4xNzQ0MjY1NzI0*_ga_8YLN0SNXVS*MTc0NTgwMDkyNy41LjEuMTc0NTgwMDk5OC4wLjAuMA..

- Public Tableau 버전 설치
> https://public.tableau.com/app/discover 

-  Tableau 샘플 데이터
> https://public.tableau.com/app/learn/sample-data?_gl=1*lta7eb*_ga*ODI4ODUxMjQwLjE3NDU4MDE1NDc.*_ga_8YLN0SNXVS*MTc0NTgwMTU0Ni4xLjAuMTc0NTgwMTU0Ni4wLjAuMA..
>
> `슈퍼스토어 매출	이 가상 회사에서 주요 개선 영역을 식별하는 데 도움이 되는 제품, 매출, 수익 등에 대한 정보가 들어 있습니다.` 슈퍼 스토어 데이터 사용

![tableu worksheet](/assets/tableau_worksheet.png)

---
## Tableau 관련 용어어
# Create a View

You set out to identify key areas for improvement, but where to start?  
With four years' worth of data, you decide to drill into the overall sales data to see what you find.  
Start by creating a simple chart.

> **Learn more: Terms in this section**

| **Term**                | **Description** |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Aggregation**: 집계         | Row-level data rolled up to a higher category, such as sum of sales or total profit. Tableau does this automatically so you can break data down to the level of detail that you want to work with. |
| **Dimension vs Measure**: 차원 및 측정값 | Dimensions are qualitative data, such as a name or date. By default, Tableau automatically classifies data that contains qualitative or categorical information as a dimension, for example, any field with text or date values. These fields generally appear as column headers for rows of data, such as Customer Name or Order Date, and also define the level of granularity that shows in the view.<br><br>Measures are quantitative numerical data. By default, Tableau treats any field containing this kind of data as a measure, for example, sales transactions or profit. Data that is classified as a measure can be aggregated based on a given dimension, for example, total sales (Measure) by region (Dimension). |
| **Continuous vs Discrete**: 연속형 및 불연속형 | Continuous fields can contain an infinite number of values. This can be a range of values such as sales within a specific date range or quantities. Continuous fields are coloured green in Tableau.<br><br>Discrete fields contain a finite number of values such as country, state, or customer name. Discrete fields are coloured blue in Tableau. |

---
- 측정값은 `차원`/ e.g. `날짜`는 '연속적인 측정값'/ `글자`는 '불연속적인 측정값'

# Tableau: Key Concepts 정리

## 1. Aggregation

- **정의**:  
  Row-level data를 요약하여 더 높은 수준(합계, 평균 등)으로 집계하는 것.
  Tableau는 기본적으로 데이터를 자동 집계하여 표시합니다.

- **표현 색상**:  
  - 별도로 색상 표현은 없음. (Aggregation은 차트 계산 로직에 해당)

- **예시**:  
  - 전체 매출 총합 (`SUM(Sales)`)
  - 평균 주문 금액 (`AVG(Order Amount)`)
  - 최대 이익 (`MAX(Profit)`)

---

## 2. Dimension vs Measure

| 구분 | 설명 | 색상 | 예시 |
|:---|:---|:---|:---|
| **Dimension** | 범주형 데이터. 데이터를 구분하는 데 사용. | 파란색 (Blue) | - 고객 이름 (Customer Name) <br> - 주문 날짜 (Order Date) <br> - 제품 카테고리 (Product Category) |
| **Measure** | 수치형 데이터. 계산 및 집계 대상이 됨. | 녹색 (Green) | - 매출 (Sales) <br> - 수량 (Quantity) <br> - 이익 (Profit) |

---

## 3. Continuous vs Discrete

| 구분 | 설명 | 색상 | 예시 |
|:---|:---|:---|:---|
| **Continuous** | 값의 범위가 연속적인 필드. 축(Axis) 생성. | 녹색 (Green) | - 연속된 판매 금액 (Sales Amount) <br> - 연도별 매출 (Year over Year Sales) <br> - 수량 (Quantity) |
| **Discrete** | 유한한 수의 고정된 값. 범주(Category) 생성. | 파란색 (Blue) | - 국가 (Country) <br> - 제품 이름 (Product Name) <br> - 고객 ID (Customer ID) |

---

# 요약

- **Dimension** = 파란색 (Blue) → 카테고리 구분용
- **Measure** = 녹색 (Green) → 수치 계산용
- **Continuous** = 녹색 (Green) → 연속된 값 (Axis 생성)
- **Discrete** = 파란색 (Blue) → 고정된 값 (Category 생성)




![tableau_sales_Orderdate_Sales](/assets/tableau_sales_Orderdate_Sales.png)
![tableau_sum](/assets/tableau_sum.png)
> tableau 측정값 변경시 합계/ 평균 등등 계산이 자동으로 적용됨.

![filtering_orderdate](/assets/filtering_orderdate.png)
> 원하는 년도를 필터링해서 볼 수 있음

![alt text](image-1.png)
> South  주들의 Sales를 출력
![alt text](image-2.png)
> 수치화 (패널: 통화 표시)
![alt text](image-3.png)
> 필터링 조건 [City]
![profitRatio newColumn](/assets/profiltratio.png)

---
# Elastic search 
> `elasticSearch` -  `elasticSearch.md`


## 데이터베이스

- Elastic Search (8.18.0 설치)
https://www.elastic.co/downloads/past-releases/elasticsearch-8-18-0

- kibana 설치 (8.18.0 설치)
https://artifacts.elastic.co/downloads/kibana/kibana-8.18.0-linux-x86_64.tar.gz

![eskibanarun](/assets/eSKibanaRun.png)

---
수집기 -> 색인기 - 검색기
          
          스토리지
-인덱스: 하나의 테이블 (표) - 데이터 전체
- Document: Row (행)
- Field: Column (열) - 데이터 매핑
- Mapping: Schema
- Query DSL: SQL

---
- Elastic Search 에서는 `HTTP`를 통한 `REST API`를 지원한다.

`curl -X(메서드) http://<host>:<port>/<인덱스>/(타입)/(문서id) -d (데이터)`

- `GET` : 조회
- `POST` : 생성
- `PUT` : 수정
- `DELETE` : 삭제

---
# 검색 시스템 이해하기

## 1. 검색 엔진, 검색 시스템, 검색 서비스

- **검색 엔진 (Search Engine)**:  
  광활한 웹에서 정보를 수집해 검색 결과를 제공하는 프로그램

- **검색 시스템 (Search System)**:  
  검색 엔진을 기반으로 신뢰성 있는 검색 결과를 제공하기 위해 구축된 시스템

- **검색 서비스 (Search Service)**:  
  검색 시스템을 포함해, 서비스를 제공하는 것

> 검색 엔진 → 검색 시스템 → 검색 서비스  
> 엘라스틱서치는 이 중 **검색 엔진**에 해당됨

---

## 2. 검색 시스템의 구성 요소
![es](/assets/es.png)
| 구성 요소 | 설명 |
|-----------|------|
| **수집기 (Crawler)** | 정보를 수집하는 프로그램. 수집된 정보는 검색 엔진이 검색 |
| **스토리지 (Storage)** | 데이터를 저장하는 물리적인 저장소 |
| **색인기 (Indexer)** | 수집된 데이터를 검색 가능한 구조로 가공. 형태소 분석기를 활용하여 의미 있는 용어 추출, 역색인 구조로 저장 |
| **검색기 (Searcher)** | 사용자 질의에 따라 결과 반환. 형태소 분석기 기반으로 검색하며, 검색 품질은 분석기에 따라 달라짐 |

---

## 3. 검색 시스템 vs 관계형 데이터베이스 (RDBMS)

- RDBMS 역시 질의어를 통해 데이터를 검색할 수 있음
- 그러나 RDBMS는:
  - **비정형 데이터 검색에 약함**
  - **텍스트 변형, 동의어/유의어 검색 불가**
- 검색엔진은:
  - **형태소 분석 기반 유연한 검색**
  - **역색인 구조로 고속 검색 가능**

---

## 4. 인덱스 개념의 차이

| 시스템 | 인덱스 의미 |
|--------|-------------|
| **엘라스틱서치** | 형태소 기반의 검색 최적화 도구 |
| **RDBMS** | WHERE/JOIN 절 최적화를 위한 보조 데이터 구조 |

---

## 5. 엘라스틱서치의 HTTP 메소드 vs RDBMS SQL문

| HTTP 메소드 | 기능 설명 | RDBMS 대응 SQL |
|-------------|-----------|----------------|
| GET         | 데이터 조회 | SELECT         |
| PUT         | 데이터 생성 | INSERT         |
| POST        | 인덱스 업데이트/데이터 조회 | UPDATE / SELECT |
| DELETE      | 데이터 삭제 | DELETE         |
| HEAD        | 인덱스 존재 확인 | -              |

- 엘라스틱서치는 **RESTful API + JSON** 구조를 사용함

---

## 6. 엘라스틱서치 API 기본 구조

```bash
curl -X(HTTP_METHOD) http://host:port/(index)/(type)/(document_id) -d '{json 데이터}'


## SQL vs 엘라스틱서치 검색 예시, 유연성, 그리고 장점 정리

### 📋 예시 데이터

| ID | Name   | Location | Gender | Date       |
|----|--------|----------|--------|------------|
| 1  | 가마돈 | 서울     | 남     | 2022-11-08 |

---

### 🔍 SQL 검색 방식

```sql
SELECT * FROM USER WHERE Name LIKE '%가마돈%';
```

- 단어 일치 기반 검색
- **대소문자 구분**, **오타**, **ud615태소 번서 무가**
- 정형 데이터 중심의 검색에 적합

---

### 🔎 엘라스틱서치 검색 방식

```http
GET http://localhost:9200/user/_search?q=Name:가마돈
```

- 결과는 **JSON 문서 형태**로 반환
- **비정형 데이터** 검색에 강함
- 대소문자나 체포에 **더 유연하게 대응 가능**

---

## 엘라스틱서치의 유연성

- 색인 시 문자열을 **소문자 혹은 대문자**로 통일하여 저장
- 검색 시에도 동일한 필터 적용으로 쿨러의 **uc77c관성 유지**
- 설정에 따라 **uc624타 허용**, **ub3d9의어 검색**, **ud615태소 번서** 등 고급 기능 가능

예시:
- `Apple`과 `apple` 모두 검색 가능
- `helo`로 `hello` 검색 가능 (Fuzzy Search)
- `run` → `running`, `ran`도 검색 가능 (Stemming, Lemmatization)

---

## 엘라스틱서치의 강점

| 장점 | 설명 |
|--------|------|
| **오픈소스 검색에진** | Apache Lucene 기반으로 다양한 사용자 가이 존재 |
| **전문 검색 지원** | Full-Text 검색으로 문서 전체를 색인 |
| **통계 배안 가능** | Kibana와 연동해 로그 배안 및 데시보드 시각화 가능 |
| **스키마리스 (Schemaless)** | 사전에 정의된 스키마 없이 유연한 구조 저장 |
| **RESTful API** | HTTP 기반 API를 통해 다양한 플랫폼에서 호출 가능 |
| **멀티템네넜시** | 서로 다른 인데크스의 필드명과 같으면 통합 검색 가능 |
| **문서 지형 저장 (Document-Oriented)** | JSON 문서 기반·계층 구조 저장 가능 |
| **역색인 (Inverted Index)** | 특정 단어로 문서 전체 위치를 빠른 소개 가능 |
| **확장성 및 고가용성** | 분산 구조로 대량의 문서 찾기 가능, 노드 확장이 쉽다 |

## 검색 API (책 - Chapter 4 (p.148))
엘라스틱서치는 색인 시점에 Analyzer를 통해 분석된 텀을 Term, 출현빈도, 문서번호와 같이 역색인 구조로 만들어 내부적으로 저장

---
# `korean_analysis.md`
---

