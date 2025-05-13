*5월 3주차*

> `May3rd.md`

_#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌_

_글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다._


---
# 3차 평가 (16.05.25에 예정)
- 엘라스틱서치

[지필평가]
## 1장
- 1장 1절: Restful API
- 1장 2절: 역색인 구조 등 엘라스틱 서치의 장점과 차별점

## 3장 데이터 모델링
- 매핑 API (데이터를 어떻게 집어넣을지에 대한 구조를) 이해하기
- 3장 3절: 

    ```
    데이터 타입 (필드에 어떤 데이터를 저장하는지)
        - 문자열, 날짜 등 비교 (숫자끼리, 객체끼리, geo 끼리): `키워드와 텍스트` (엘라스틱의 목표는 전문 검색 (역색인으로))가 어떤 차이가 있는지가 핵심
    ```
- 3장 4절: 엘라스틱서치 분석기 

    ```
    분석기의 흐름이 어떻게 일어나는지지
    ```

`Notion`에서 `code` 내용을 실습평가로 이루어짐

---
`scrape_tweets_api.py`
# FAIL: X API 사용용
## X API 사용해서 트윗 분석하기

- Colab에서 실습
- 무료 계정 (X API)라서 한번 요처아고 15-30분 걸림림

```
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
## FAIL: snscrape 패키지 사용용
- 위와 같은 코드로 snscrape 패키지를 이용해서 트윗을 수집하려고 했으나 `FAIL`
=> python 3.13 버전, 3.11 버전과 충돌이 일어나 python version 을 3.10로 다운그레이드 했으나 
`실패`

=> snscrap 자체가 X (Twitter 가 X로 전환 되면서) 보안 측면에서 막힌듯보임

## FAIL: `twitter_cookies.json`, `scrape_twitter_cookies.py` - selenium 으로 스크랩 자동화
- selenium으로 스크랩 자동화하려고했는데
1. 로그인된 x 페이지에 접근하기 실패
> json (twitter_cookie.json)으로 x에 로그인된 cookie 정보를 저장해서 selenium 실행시 성공
2. x api가 아니니 3회 이상 selenium 시도하니 막히는 것 같았음 
