import requests
import pandas as pd

# 발급받은 Twitter API Bearer Token
BEARER_TOKEN = "token 넣기"

# ✅ 검색 쿼리 (한글 포함 가능, lang:ko 추가)
query = "(포카 OR 포토카드 OR 응원봉 OR 굿즈) (양도 OR 양도해요 OR 양도합니다 OR 넘깁니다 OR 판매 OR 팝니다 OR 구매 OR 구합니다 OR 구해요 OR 삽니다 OR 급구 OR 구매해요 OR 구매 원해요) lang:ko"

# ✅ 검색 기간 (Twitter API 무료 버전은 최근 7일까지만 지원)
url = f"https://api.twitter.com/2/tweets/search/recent"
params = {
    "query": query,
    "max_results": "100",  # 최대 100개
    "tweet.fields": "created_at,text,lang",
}

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# ✅ API 호출
response = requests.get(url, headers=headers, params=params)

# ✅ 응답 처리
if response.status_code == 200:
    tweets = response.json().get("data", [])
    df = pd.DataFrame(tweets)
    df.to_csv("goods_tweets.csv", index=False, encoding="utf-8-sig")
    print(f"✅ 총 {len(df)}개의 트윗이 goods_tweets.csv에 저장되었습니다.")
else:
    print(f"❌ 요청 실패: {response.status_code}\n{response.text}")
