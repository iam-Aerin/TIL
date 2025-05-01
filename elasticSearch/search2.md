GET /kibana_sample_data_ecommerce/_search
###sample data의 이름이 너무 길어서 
### alias 기능으로 이름에 별칭

## _aliases
### kibana_sample_data_ecommerce를 'ecommerce'라고 (테이블)이름 변경
POST _aliases
{
    "actions": [
      {
        "add": {
          "index": "kibana_sample_data_ecommerce",
          "alias": "ecommerce"
        }
      }
    ]
}

GET /ecommerce/_search
{
    "query": {
        "match_all": {}
    }
}

### 데이터 확인
GET /ecommerce/_mapping

##match query
### term 단위로 나누어서 검색 해당 단어가 포함된 경우를 출력
GET /ecommerce/_search
{
    "query": {
        "match": {
            "customer_full_name": "mary"
        }
    }
}


## multi match
### 여러컬럼을 동시에 조회할때
#### clothing이라는 단어가 category에 있는지/ products하위의 product_name에 들어있는지
GET /ecommerce/_search
{
    "query": {
        "multi_match": {
          "query": "Clothing",
          "fields": ["category", "products.product_name"]
        }
    }
}

GET /ecommerce/_search
{
    "query": {
        "multi_match": {
          "query": "dark",
          "fields": ["category", "products.product_name"]
        }
    }
}

## term query
## 키워드 검색 
### 대소문까지 완벽하게 일치해야 검색 가능
GET /ecommerce/_search
{
    "query": {
        "term": {
          "day_of_week": {
            "value": "Monday"
          }
        }
    }
}

## Bool query
### must/ must_not/ should/ filter
GET /ecommerce/_search
{
    "query": {
        "bool": {
            "must": [
              {
                "match": {
                  "category": "clothing"
                }
              }
            ],
            "must_not": [
              {
                "term": {
                  "day_of_week": {
                    "value": "Monday"
                  }
                }
              }
            ],
            "filter": [
              {
                "range": {
                  "taxful_total_price": {
                    "gte": 1,
                    "lte": 50
                  }
                }
              }
            ]
        }
    }
}

## Query String


## prefix
### 접두사

GET /ecommerce/_search
{

    "query": {
        "prefix": {
          "category": {
            "value": "me"
          }
        }
    }
}

## exist
GET /ecommerce/_search
{
    "query": {
        "exists": {
            "field": "currency"
        }
    }
}

## wildcard query
### 검색어가 와일드카드와 일치하는 구문을 찾는다.
### 이때 입력된 감색어는 형태소 분석이 이뤄지지 않는다.
#### *: 문자의 길이와 상관없이 / ?: 지정된 위치의 한 글자가 다른 경우의 문서를 찾음

GET /ecommerce/_search
{
    "query": {
        "wildcard": {
          "customer_first_name": {
            "value": "E????",
                "case_insensitive": true
          }
        }
    }
}

# === analyze ===
## 분석기 (영문)
POST _analyze
{
    "analyzer": "standard", 
    "text": "Hello world !!!! !!"
}
#### 필요없는 기호 (!)들은 빼고, 대문자는 소문자로 

POST _analyze
{
    "analyzer": "whitespace",
    "text": "Hello world @!!! !!"
}
#### whitespace: 기호도 지우지 않고, 띄어쓰기만을 기준으로 analyse

POST _analyze
{
    "analyzer": "standard",
    "text": "Is This Déjà Vu?"
}
### Déjà와 Deja를 다른 단어로 인식

POST _analyze
{
    "analyzer": "standard",
    "text": "Is This <b>Déjà</b> Vu?"
}
#### HTML의 <b></b>태그로 인식하지 않고 단순 글자로 인식함


## 형태소 분석 
### tokenizer로 customising
POST _analyze
{
    "tokenizer": "standard",
    "filter": ["lowercase", "asciifolding"],
    "text": "Is this Déjà Vu?",
    "explain": true
}

### English analyser
PUT /article
{
    "settings": {
        "analysis": {
            "analyzer": {
                "my_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "asciifolding"]
                }
            }
        }
    },

    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "my_analyzer"
            }
        }
    }
}


GET /article/_analyze
{
    "analyzer": "my_analyzer",
    "text": "Is this Déjà Vu?"
}

DELETE /article

### 기존 article을 지우고 새롭게
### version.2

PUT /article
{
    "settings": {
        "analysis": {
            "analyzer": {
                "my_analyzer": {
                    "type": "custom",
                    "char_filter": ["html_strip"],
                    "tokenizer": "standard",
                    "filter": ["lowercase", "asciifolding", "stemmer"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "my_analyzer"
            }
        }
    }
}

### 위에서 만든 "my_analyzer"가 어떻게 작동하는지 살펴보기
POST /article/_analyze
{
    "field": "content",
    "text": "<b>Is this Déjà Vu?</b>. foxes are jumping",
    "explain": true

}

## === log 데이터로 연산하기 ===

GET /kibana_sample_data_logs/_search
## aliases 별칭 주기
POST _aliases
{
    "actions": [
      {
        "add": {
          "index": "kibana_sample_data_logs",
          "alias": "logs"
        }
      }
    ]
}

GET /logs/_mapping
GET /logs/_search

GET /logs/_search?size=0
{
    "aggs": {
        "region_count": {
            "terms": {
                "field": "ip"
            }
        }
    }
}

GET /logs/_search?size=0
{
    "aggs": {
        "region_count": {
            "terms": {
                "field": "geo.dest"
            }
        }
    }
}

### response가 200, 404 등등 각 데이터 세어보기
#### response는 text field (text 데이터를 .keyword로 바꿔서)
GET /logs/_search?size=0
{
    "aggs": {
      "status_count": {
        "terms": {
            "field": "response.keyword"
        }
      }
    }
}

## 집계 영역
### 합산 집계 (5.2.1)

### 전체 데이터의 avg 연산 구하기
#### "avg"
GET /logs/_search?size=0
{
    "aggs": {
      "total_bytes": {
        "avg": {
            "field": "bytes"
        }
      }
    }
}
## > "avg", "sum", "min", "max" 등을 씀으로써 "최대, 최소, 평균, 합" 등을 구할 수 있음

### 총 데이터 합산이 아닌, 지정해서 내가 원하는 데이터끼리의 연산을 출력하기
#### geo.dest가 "CN"인 경우의 bytes의 합
GET /logs/_search?size=0
{
    "query": {
        "match": {
          "geo.dest": "CN"
        }
    },
    "aggs": {
      "total_bytes": {
        "sum": {
            "field": "bytes"
        }
      }
    }
}

## value_count
GET /logs/_search?size=0
{
    "query": {
        "match": {
            "geo.dest": "CN"
        }

    },
    "aggs": {
      "count": {
        "value_count": {
            "field": "ip"
        }
      }
    }
}


## 통계 집계 (5.2.6)
### Stats Aggregation

GET /logs/_search?size=0
{
    "aggs": {
      "stats": {
        "stats": {
            "field": "bytes"
        }
      }
    }
}

GET /logs/_search?size=0
{
    "aggs": {
      "stats": {
        "extended_stats": {
            "field": "bytes"
        }
      }
    }
}

## cardinality
### 고유값 (중복된 값은 제외한) 집계
GET /logs/_search?size=0
{
    "aggs": {
      "card": {
        "cardinality": {
            "field": "geo.dest"
        }
      }
    }
}

## 백분위수 집계
### Percentiles Aggregation - 중앙값 등등 출력
GET /logs/_search?size=0
{
    "aggs": {
        "percent": {
            "percentiles": {
                "field": "bytes"
            }
        }
    }
}

GET /logs/_search?size=0
{
    "aggs": {
        "percent": {
            "percentiles": {
                "field": "bytes",
                "percents": [50, 90, 99]
            }
        }
    }
}

### 이 숫자는 몇 퍼센트에 속하나요? 로 물어보려면
#### percentiles_ranks
GET /logs/_search?size=0
{
    "aggs": {
        "percent": {
            "percentile_ranks": {
                "field": "bytes",
                "values": [100, 9999]
            }
        }
    }
}

## 지형 집계
GET /logs/_search?size=10
{
    "aggs": {
      "viewport": {
        "geo_bounds": {
            "field": "geo.coordinates"
        }
      }
    }
}

## 버킷 집계
GET /logs/_search?size=0
{
    "aggs": {
      "byte_range": {
        "range": {
            "field": "bytes",
            "ranges": [
              {"from": 1000, "to": 2000},
              {"from": 2000, "to": 3000}
            ]
        }
      }
    }
}

## 날짜 범위 집계 (5.3.2)
GET /logs/_search?size=0
{
    "aggs": {
      "date-count": {
        "date_range": {
            "field": "@timestamp",
            "ranges": [
              {
                "from": "2025-06-11T09:22:09.711Z",
                "to": "2025-06-11T09:22:09.711Z"
              }
            ]
        }
      }
    }
}

GET /logs/_search?size=0
{
    "aggs": {
      "byte_histo": {
        "histogram": {
            "field": "bytes",
            "interval": 5000
        }
      }
    }
}

GET /logs/_search?size=0
{
    "aggs": {
      "date_histo": {
        "date_histogram": {
            "field": "@timestamp",
            "calendar_interval": "1d"
        }
      }
    }
}

## 파이프라인 집계 (5.4)
### pipeline

#### 형제 집계 (같은 선상에)

GET /logs/_search?size=0
{
    "aggs": {
      "date_histo": {
        "date_histogram": {
            "field": "@timestamp",
            "calendar_interval": "1d"
        },
        "aggs": {
          "bytes_sum": {
            "sum": {
                "field": "bytes"
            }
          }
        }
      },
      "min_bytes": {
        "min_bucket": {
          "buckets_path": "date_histo>bytes_sum"
        }
      }
    }
}

####  부모 집계
GET /logs/_search?size=0
{
    "aggs": {
      "date_histo": {
        "date_histogram": {
            "field": "@timestamp",
            "calendar_interval": "1d"
        },
        "aggs": {
            "bytes_max": {
                "max": {
                    "field": "bytes"
                }
             },
             "max_deriv": {
                "derivative": {
                  "buckets_path": "bytes_max"
                }
             }
        }
      }
    }
}

#1️⃣ date_histogram: 하루 단위로 버킷을 나눔
#2️⃣ 각 버킷에서:

#bytes_max: 그날의 bytes 최댓값을 구함

#max_deriv: 그 최댓값의 변화량(전일 대비 차이)을 계산






