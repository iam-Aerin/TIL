# 코호트 리텐션 분석
`https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-electronics-store/data` kaggle data로 cohort retention 분석
& Funnel 퍼널 분석

# 📊 코호트 리텐션 분석이란?

**코호트 리텐션 분석**은  
같은 시점에 유입된 사용자 집단(코호트)이  
얼마나 오래 서비스에 머무는지를  
시간 흐름에 따라 분석하는 방법입니다.

---

## ✅ 핵심 개념

- **코호트(Cohort)**:  
  공통된 특성을 가진 사용자 집단  
  (예: 가입일 기준, 첫 구매일 기준)

- **리텐션(Retention)**:  
  일정 기간 후에도 남아있는 비율  
  (예: 7일차 리텐션 = 7일 후 잔존율)

---

## ✅ 왜 중요한가?

- 신규 유입자의 **품질 평가**
- 마케팅/기능 업데이트의 **효과 검증**
- 사용자 이탈 시점 파악
- 서비스의 **지속 사용성**과 **고객 충성도 평가**

---

## ✅ 예시 표

| 코호트 (가입월) | 0일차 리텐션 | 7일차 리텐션 |
|----------------|--------------|--------------|
| 2025년 1월     | 100%         | 30%          |
| 2025년 2월     | 100%         | 40%          |

---

👉 **한마디 요약:**  
> 코호트별 사용자 유지 흐름을 분석해  
> 서비스의 지속 사용성(얼마나 오래 사용하는지)과  고객 충성도를 파악하는 방법

---
kaggle `eCommerce events history in electronics store` 데이터 => damf2 폴더 data 폴더 안으로 옮김

event type 이 `view, cart, other`인지 => Funnel analysis

- 데이터 전처리 먼저 
`/home/ubuntu/damf2/kibana/ecommerce.py`

## ✅ 타임스탬프 처리

UTC 타임존이 포함된 데이터를 **로컬 시간대**로 변환하고, **년-월-일 시:분:초** 형식만 남깁니다.

```python
# UTC 타임존 제거 (로컬 타임스탬프만 남기기)
df['event_time'] = df['event_time'].dt.tz_localize(None)

# 예: '2020-09-24 11:57:06 UTC' → '2020-09-24 11:57:06'
print(df.head())

---
✅ 월 단위 그룹핑
to_period() 함수를 사용해 월 단위로 데이터를 그룹화할 새로운 컬럼을 생성합니다.
```
# 이벤트가 발생한 '월' 정보 추출
```
df['event_month'] = df['event_time'].dt.to_period('M')
```

✅ 코호트 인덱스 만들기
사용자가 **처음 방문한 월(cohort month)**을 기준으로 코호트 분석용 인덱스를 생성합니다.

```
# 사용자별 첫 방문한 월(cohort month) 계산
df['cohort_month'] = df.groupby('user_id')['event_month'].transform('min')
```

✅ 날짜 분리 및 코호트 인덱스 계산
년도와 월을 각각 분리하고, 처음 방문한 시점(cohort month)과 이벤트 시점(event month) 간의 차이를 계산합니다.

```
# '년도'와 '월'을 분리 추출
invoice_year = df['event_month'].dt.year
invoice_month = df['event_month'].dt.month
cohort_year = df['cohort_month'].dt.year
cohort_month = df['cohort_month'].dt.month
```
# 코호트 인덱스: (몇 개월 차인지)
```
df['cohort_index'] = (invoice_year - cohort_year) * 12 + (invoice_month - cohort_month) + 1
```

✅ 데이터 형식 변환 및 저장
event_month와 cohort_month를 문자열로 변환한 후, 최종 데이터를 CSV로 저장합니다.
```
# 'Period' 객체 → 문자열로 변환 (예: '2020-09')
df['event_month'] = df['event_month'].astype('str')
df['cohort_month'] = df['cohort_month'].astype('str')
```
# 전처리된 데이터 저장
```
df.to_csv('/home/ubuntu/damf2/data/cohort_events.csv', index=False)
```

- visualisation

- view / cart / purchase 로 cohort analysis

![alt text](/assets/kibana_vcp_cohort.png)

- 코호트별 사용자 유지율
![alt text](/assets/kibana_cohort_index_M.png)

## ✅ 구성

- **X축 (cohort_index):**  
  → 사용자가 첫 방문 후 몇 개월 차인지 표시  
  (1 = 첫 달, 2 = 두 번째 달, ...)

- **Y축 (cohort_month):**  
  → 사용자가 처음 방문한 월 (코호트 그룹)

- **셀 값:**  
  → 각 코호트의 각 개월 차에서 **고유 사용자 수**를 집계  
  (Unique count of user_id)

- **색상:**  
  → 진할수록 사용자 수가 많음을 의미

---

## ✅ 이 히트맵이 보여주는 것

- 각 코호트가 **첫 방문 후 몇 개월까지 유지되었는지** 확인 가능
- 코호트별 **유지율 흐름**을 한눈에 파악
- 이탈 시점과 **충성도 높은 코호트** 식별 가능

---

👉 **요약:**  
> 코호트별로 사용자 이탈과 유지를 시각화해,  
> 첫 방문 후 몇 개월까지 사용자들이 남아 있었는지 분석하는 히트맵
> 빨간색: 신규 유저가 많이 들어왔다.
> 빨간색 유지가 적은 코호트는 이탈이 빠르다.
