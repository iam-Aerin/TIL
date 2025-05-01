### Create an index
```
PUT /my-index
```
#my-index라는 인덱스를 생성 [PUT]


### Add a document to my-index
### 데이터 추가
```
POST /my-index/_doc
{
    "id": "park_rocky-mountain",
    "title": "my name",
    "description": "hi hello me myself"
}
```

### Perform a search in my-index
### GET 요청으로 
## rocky mountain 이라는 단어가 들어가있는 정보 (문서) 검색
```
GET /my-index/_search?q="rocky mountain"
```

# 스키마리스 방식으로 인덱스 생성
## 1. INDEX 만들기
```
PUT /movie
```

## 2. INDEX에 Data 넣기
```
PUT /movie/_doc/1
{
    "movieNm": "살아남은 아이",
    "prdtYear": 2017
}
```
```
PUT /movie/_doc/2
{
    "movieNm": "콘클라베",
    "prdtYear": 2024
}
```
## 3. 저장된 데이터 목록 확인 (GET 요청)
```
GET /movie/_search
```

##3-1. movie Index 구조 확인
```
GET /movie
```

## 4. 테이블 (INDEX)지우기
```
DELETE /movie
```

## <스키마 구조를 잡아서 INDEX 생성>
## 1. INDEX 만들기

### 표의 규격잡기 (mapping 하기)
```
PUT /movie
{
    "mappings": {
       
        "properties": {
            "movieNm": {
                "type": "text"
            },
            "prdtYear":{
                "type": "integer"
            }
        }
    }
}
```
## 2. PUT 으로 데이터 집어넣기
```
PUT /movie/_doc/1
{
    "movieNm": "Briget Jones",
    "prdtYear": 2002
}
```
```
PUT /movie/_doc/2
{
    "movieNm": "Briget Jones 2",
    "prdtYear": 2010
}
```

## 3. GET 요청으로 데이터 확인
```
GET /movie
```
```
GET /movie/_search
```
## 4. id가 2인 데이터 지우기
```
DELETE /movie/_doc/2
```

## 5. id지정 없이 데이터 추가하기
```
POST /movie/_doc
{
    "movieNm": "Harry Potter",
    "prdtYear": 2001
}
```

## 매핑 정보 확인
```
GET /movie/_mapping
```

## keyword 데이터 타입 추가하기
```
PUT /movie_mapping
```
```
PUT /movie_mapping/_mapping/
{
    "properties": {
        "multiMovieYn": {
            "type": "keyword"
        }
    }
}
```

## integer 타입 데이터 추가하기
```
PUT /movie_mapping/_mapping
{
    "properties": {
        "Year": {
            "type": "integer"
        }
    }
}
```

## date 타입 데이터 추가하기
```
PUT /movie_mapping/_mapping
{
    "properties": {
        "date": {
            "type": "date",
            "format": "yyyy-MM-dd"
        }
    }
}
```

## text 타입 데이터 추가하기
```
PUT movie_mapping/_mapping
{
    "properties": {
        "movieComment": {
            "type": "text"
        }
    }
}
```

## Range 데이터 타입
```
PUT movie_mapping/_mapping
{
    "properties": {
        "showRange": {
            "type": "date_range"
        }
    }
}
```
```
POST movie_mapping/_doc
{
    "showRange": {
        "gte": "2025-01-01",
        "lte": "2025-12-31"
    }
}
```

## Geo-Point 데이터 집어 넣기 
```
PUT movie_mapping/_mapping
{
    "properties": {
        "filmLocation": {
            "type": "geo-point"
        }
    }
}
```
```
POST movie_mapping/_doc
{
    "filmLocation": {
        "lat": 55,
        "lon": -1
    }
}
```

## 분석기: 텍스트 분석
## Analyzer
```
POST _analyze
{
    "analyzer": "standard",
    "text": "우리나라가 좋은나라, 대한민국 허허허"
}

```

## CRUD 로직으로 데이터 추가하기
```
PUT movie_mapping/_doc/1
{
    "movieNM": "Briget Jones 3"
}
```
# GET
## 데이터 전체 정보 가져오기
```
GET movie_mapping/
```
## id 1 지정해서 정보 가져오기
```
GET movie_mapping/_doc/1
```
# UPDATE
## 기존 문서를 지우고 데이터 업데이트하기
```
PUT movie_mapping/_doc/1
{
    "movieNm": "Briget Jones 2"
}
```
# DELETE 
## 데이터 지우기
```
DELETE movie_mapping/_doc/1
```

- vscode에서 faker 등등 사용해서 가상의 영화 데이터 추가해줌
```
GET movie/_search
```
> 챕터 4 (p.148)
>
> 검색 API

# URI 검색
# GET /movie/_search
# 파라미터를 "Key"="Value"형태로 전달하는 방

# 개봉년도가 2018년인 영화 검색
GET /movie/_search?q=prdtYear:2010
GET /movie/_search?q=movieNm:star

# Request Body 검색
GET /movie/_search
{
    "query": {
        "term": {"prdtYear": 2018}
    }
}

# query 방식의 검색
# 일반적으로 전문 검색에 사용 (다소 느림)
GET /movie/_search
{
    "query": {
        "bool":{
            "filter": {
                "term":{
                    "prdtYear": "2018"
                }
            }
        }  
    }
}


# from, size : 문서가 많다면, page nation(?) 을 통해

# sort
GET /movie/_search
{
    "query": {
        "term": {"movieNm": "star"}
    },
    "sort": {
        "prdtYear": {
            "order": "desc"
        }
    }
}


# _source (내가 보고싶은 컬럼만을 출력)
GET /movie/_search
{
    "query": {
        "term": {
            "movieNm": "star"
        }
    },
    "_source": ["movieNm"]
}

# 범위 검색
# Range
GET /movie/_search
{
    "query": {
        "range": {
            "prdtYear": {
                "gte": 2010,
                "lte": 2020
            }
        }
    }
}


# operator (and 혹은 or을 operator로 줌으로써 해당 단어를 가진 경우를 출력)
GET /movie/_search
{
    "query": {
        "match": {
            "movieNm": "Free threat"
        }
    }
}

# operator: and로 줄때 교집합만 출력
GET /movie/_search
{
  "query": {
    "match": {
      "movieNm": {
        "query": "Free threat",
        "operator": "and"
      }
    }
  }
}

# fuzziness : 오탈자 검색
# 영어에서는 가능하나, 한국어에서는 불가
GET /movie/_search
{
    "query": {
        "match": {
            "movieNm": {
                "query": "controll",
                "fuzziness": 1
            }
        }
    }
}


















