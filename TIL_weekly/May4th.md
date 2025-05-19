# 5월 4주차 TIL

---

## 진행 파일 목록

`elasticSearch.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._

---
# elasticSearch 기본 개념 복습
- 작성 문법 

| 기능       | 쿼리 유형           | 설명                                |
| -------- | --------------- | --------------------------------- |
| 전체 검색    | `match_all`     | 모든 문서 검색                          |
| 단일 조건 검색 | `match`, `term` | 분석 vs 정확일치                        |
| 범위 검색    | `range`         | 숫자 필드 범위 조건                       |
| 복합 검색    | `bool`          | `must`, `must_not`, `filter` 등 조합 |
| 필드 존재 여부 | `exists`        | 필드가 있는 문서만 조회                     |
| 와일드카드    | `wildcard`      | 패턴 검색                             |
| 접두사 검색   | `prefix`        | 시작하는 단어로 검색                       |
| 정렬       | `sort`          | 오름/내림차순 정렬                        |
| 출력 필드 제한 | `_source`       | 원하는 필드만 결과로                       |
| 오타 허용 검색 | `fuzziness`     | 유사한 단어 검색                         |

- GET /_search & GET /_mapping 차이
# Elasticsearch API 비교: `GET /logs/_search` vs `GET /logs/_mapping`

Elasticsearch에서 자주 사용되는 두 API 요청, `GET /logs/_search`와 `GET /logs/_mapping`의 차이를 설명합니다. 각 요청은 용도, 반환 내용, 활용 방식이 다르며, 쿼리 작성 및 데이터 분석을 위해 함께 이해하는 것이 중요합니다.

## 1. GET /logs/_search

**역할**  
`logs` 인덱스에서 실제 저장된 문서(document)를 검색하는 요청입니다. 조건 기반 검색, 정렬, 필터링, 집계 등을 수행할 수 있습니다.

**사용 목적**  
- 로그 문서 확인  
- 키워드나 조건 기반 검색  
- 통계 집계, 시각화용 데이터 추출  

**예시 요청**
```
GET /logs/_search
```

**예시 응답 구조**
```json
{
  "hits": {
    "hits": [
      {
        "_source": {
          "ip": "192.168.0.1",
          "geo": {
            "dest": "CN"
          },
          "bytes": 5400
        }
      }
    ]
  }
}
```

## 2. GET /logs/_mapping

**역할**  
`logs` 인덱스의 필드 정의 및 자료형(type)을 조회하는 요청입니다. 쿼리 작성 전에 어떤 필드가 존재하고, 그 필드의 타입이 무엇인지 확인할 때 사용됩니다.

**사용 목적**  
- 인덱스 내 필드 목록 확인  
- `keyword`, `text`, `date`, `geo_point` 등 자료형 파악  
- 정렬 및 집계 가능 여부 판단  

**예시 요청**
```
GET /logs/_mapping
```

**예시 응답 구조**
```json
{
  "logs": {
    "mappings": {
      "properties": {
        "ip": {
          "type": "ip"
        },
        "geo": {
          "properties": {
            "dest": {
              "type": "keyword"
            },
            "coordinates": {
              "type": "geo_point"
            }
          }
        },
        "bytes": {
          "type": "long"
        }
      }
    }
  }
}
```

## 비교 요약

| 항목       | GET /logs/_search                   | GET /logs/_mapping                   |
|------------|-------------------------------------|--------------------------------------|
| 목적       | 문서(로그) 검색 및 내용 확인       | 인덱스의 스키마(필드 구조) 조회     |
| 반환 내용  | 저장된 문서 목록 (`_source`)       | 필드 이름과 자료형 (`type`) 정보    |
| 활용       | 검색, 필터링, 집계 분석            | 쿼리 작성 전 필드 및 자료형 확인    |

## 참고

- `logs`는 실제 인덱스 이름이거나 별칭(alias)일 수 있습니다.  
- 매핑 정보를 확인하지 않고 쿼리를 작성하면, `text` 타입 필드에 대해 정렬/집계를 시도하다 오류가 발생할 수 있습니다.  
- 따라서 검색 전에 `GET /_mapping`으로 필드 타입을 확인하는 것은 매우 중요합니다.

## 🧠 Elasticsearch 객관식 예상문제 모음

> 시험 유형: 객관식 10문제  
> 출제 범위: 1장(Restful API, 역색인) ~ 3장(데이터 모델링, 분석기)

### 문제 1  
Elasticsearch에서 "텍스트를 단어 단위로 쪼개는 기능"을 수행하는 구성요소는?

- A. Filter  
- B. Mapping  
- C. Index  
- ✅ D. Analyzer

> **해설**: Analyzer는 텍스트를 토큰화하고 불용어 제거 등의 처리를 한다.

---

### 문제 2  
Elasticsearch에서 역색인 구조의 장점으로 적절하지 않은 것은?

- A. 빠른 검색 속도  
- B. 텍스트 기반 전문 검색 최적화  
- ✅ C. 정형 데이터 처리에 특화됨  
- D. 단어 단위로 검색 가능

> **해설**: 역색인은 텍스트 분석에 최적화되어 있고 정형 데이터 처리는 RDBMS가 더 적합하다.

---

### 문제 3  
Elasticsearch에서 데이터 타입 중 텍스트 분석에 사용되는 타입은?

- A. integer  
- B. keyword  
- ✅ C. text  
- D. boolean

> **해설**: `text` 타입은 Analyzer가 적용되어 전문 검색용으로 사용된다.

---

### 문제 4  
다음 중 Elasticsearch에서 정확한 값을 검색할 때 사용하는 타입은?

- A. text  
- ✅ B. keyword  
- C. float  
- D. geo_point

> **해설**: keyword는 토큰화되지 않고 정렬, 집계 등에 사용된다.

---

### 문제 5  
Elasticsearch에서 데이터를 색인할 때 구조를 정의하는 것은?

- A. query  
- ✅ B. mapping  
- C. index  
- D. field

> **해설**: Mapping은 필드명과 데이터 타입을 정의한다.

---

### 문제 6  
Elasticsearch 쿼리에서 `must_not` 조건에 해당하는 동작은?

- A. 포함되는 문서 필터링  
- ✅ B. 제외할 문서 지정  
- C. 정렬 순서 변경  
- D. 필드 존재 확인

---

### 문제 7  
다음 중 오타 허용 검색(fuzziness)이 적용된 쿼리는?

- A. term query  
- ✅ B. match query with `fuzziness`  
- C. range query  
- D. wildcard query

---

### 문제 8  
Elasticsearch에서 `range` 쿼리로 할 수 없는 것은?

- A. 숫자 범위 조회  
- B. 날짜 범위 조회  
- ✅ C. 문자열 포함 여부 확인  
- D. 값 이상 이하 조건 지정

---

### 문제 9  
`_source` 옵션의 역할은?

- A. 검색 필드 설정  
- B. 정렬 기준 지정  
- ✅ C. 결과 출력 필드를 제한  
- D. 분석기 지정

---

### 문제 10  
Elasticsearch에서 `multi_match` 쿼리는 어떤 경우에 사용하는가?

- A. 여러 인덱스를 동시에 검색할 때  
- ✅ B. 여러 필드를 동시에 검색할 때  
- C. 여러 조건을 조합할 때  
- D. 여러 키워드를 필터링할 때

# Elasticsearch 객관식 예상문제 추가 모음

> ✅ 지필 시험 대비용 (객관식 중심)

---

### 문제 11  
Elasticsearch에서 `index`를 생성할 때 필요한 구성 요소가 아닌 것은?

- A. Mapping  
- ✅ B. Shard Allocation  
- C. Settings  
- D. Index Name

> **정답: B**  
> **해설**: Shard Allocation은 클러스터 내부 데이터 분산 설정이지 인덱스 생성 필수 요소는 아니다.

---

### 문제 12  
Elasticsearch에서 `text` 타입이 아닌 필드에 `match` 쿼리를 사용하면 어떻게 되는가?

- A. 내부적으로 keyword로 변환된다  
- ✅ B. 쿼리가 실패하거나 기대한 결과를 얻지 못한다  
- C. 자동으로 Analyzer가 적용된다  
- D. 무조건 정확 일치 검색이 된다

> **정답: B**  
> **해설**: `match` 쿼리는 분석이 필요한 텍스트 필드에 적합하며, keyword 필드나 숫자 필드에서는 적절히 작동하지 않는다.

---

### 문제 13  
아래 중 `bool` 쿼리에서 사용 가능한 절이 아닌 것은?

- A. must  
- B. filter  
- ✅ C. reduce  
- D. must_not

> **정답: C**  
> **해설**: reduce는 존재하지 않는 절이며, must, must_not, should, filter가 bool 쿼리에서 사용된다.

---

### 문제 14  
`term` 쿼리와 `match` 쿼리의 차이로 적절한 설명은?

- A. 둘 다 정렬에 사용된다  
- ✅ B. `term`은 정확 일치, `match`는 분석기를 거친 검색  
- C. `match`는 숫자 비교용 쿼리  
- D. `term`은 여러 필드에 적용된다

> **정답: B**

---

### 문제 15  
다음 중 `_source` 필드의 역할은?

- A. 문서의 ID 값을 지정한다  
- ✅ B. 검색 결과에 어떤 필드를 포함할지 지정  
- C. 인덱스의 매핑 정보를 반환한다  
- D. 인덱스를 재색인한다

> **정답: B**

---

### 문제 16  
다음 중 `range` 쿼리로 표현할 수 있는 조건은?

- A. 값이 특정 문자열을 포함  
- ✅ B. 숫자 값이 10 이상 100 이하  
- C. 단어가 'love'를 포함  
- D. 정확히 "hello"라는 문장이 있는 경우

> **정답: B**

---

### 문제 17  
Elasticsearch에서 `match_all` 쿼리의 기능은?

- ✅ A. 모든 문서를 반환한다  
- B. 필터된 문서만 반환  
- C. 존재하는 필드만 검색  
- D. 오타 검색용 쿼리

> **정답: A**

---

### 문제 18  
`fuzziness` 옵션이 의미하는 것은?

- A. 정확 일치를 요구하는 옵션  
- B. 검색 속도를 빠르게 만드는 옵션  
- ✅ C. 오타 허용 검색  
- D. 정렬 우선순위를 결정하는 옵션

> **정답: C**

---

### 문제 19  
`wildcard` 쿼리에서 `?`의 의미는?

- A. 아무 글자든 0개 이상  
- ✅ B. 정확히 1개의 문자  
- C. 대소문자 구분 없음  
- D. 공백 포함 조건

> **정답: B**

---

### 문제 20  
Elasticsearch에서 `multi_match` 쿼리의 목적은?

- A. 여러 인덱스 동시에 검색  
- B. 여러 값으로 term 검색  
- ✅ C. 여러 필드에서 동일한 검색어 조회  
- D. 여러 결과를 랜덤하게 추출

> **정답: C**

---

### 문제 21  
다음 중 분석기(analyzer)의 핵심 기능이 아닌 것은?

- A. 텍스트 토큰화  
- B. 불용어 제거  
- ✅ C. 정수형 데이터 계산  
- D. 소문자 변환

> **정답: C**

---


###문제 22**  
다음 중 오타 허용 검색을 가능하게 하는 쿼리는?  
A. term 쿼리  
✅ B. match 쿼리 + fuzziness  
C. wildcard 쿼리  
D. exists 쿼리  
**정답: B**

---

### 문제 23**  
다음 중 filter 조건에 적합한 것은?  
A. 사용자 검색 로그  
✅ B. 가격이 1000원 이상인 경우  
C. 전체 텍스트 검색  
D. 키워드 추천  
**정답: B**

---

### 문제 24**  
Elasticsearch에서 인덱스에 들어 있는 필드명과 타입 구조를 확인할 수 있는 API는?  
A. _search  
✅ B. _mapping  
C. _analyze  
D. _source  
**정답: B**

---

### 문제 25**  
Elasticsearch에서 날짜/숫자 범위를 설정할 때 사용하는 쿼리는?  
A. match  
B. term  
✅ C. range  
D. wildcard  
**정답: C**

---

### 문제 26**  
아래 중 `must`, `should`, `must_not`, `filter`를 조합해서 사용하는 쿼리는?  
A. multi_match  
B. match  
✅ C. bool  
D. exists  
**정답: C**

---

### 문제 27**  
Elasticsearch에서 `_source` 필드를 지정하는 이유는?  
A. 전체 문서를 삭제하기 위해  
B. 필드 존재 여부를 체크하기 위해  
✅ C. 특정 필드만 결과에 포함시키기 위해  
D. 색인 성능을 높이기 위해  
**정답: C**

---

### 문제 28**  
다음 중 `operator: and` 옵션을 match 쿼리에서 사용하면?  
✅ A. 검색어의 모든 단어가 포함된 문서만 검색된다  
B. 문서에 단 하나라도 단어가 있으면 검색된다  
C. 정렬이 적용된다  
D. 분석기가 비활성화된다  
**정답: A**

---