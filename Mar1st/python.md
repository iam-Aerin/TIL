# 3월 2주차 TIL 내용 정리

## 4~7 Mar 2025
> 의 수업 내용 정리를 다룹니다. 
> 날짜별 정리 내용이 아닌, 관련 교육 내용 <ml>은 https://github.com/iam-Aerin/ml/tree/master [github]의 repository 를 통해 확인 가능합니다. 

#
> `git` 이외에도 노션 (https://www.notion.so/196d384c40db80129561c25961bf1bba) 을 통해 학습 내용을 정리 중입니다.
#

>이 내용은 날짜별 (혹은 주차별) TIL 기록을 위해 생성했습니다. 
>#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌

TIL(Today I Learned) 오늘 배운 내용을 기록합니다.


### Links (이번주 학습에 사용된 링크모음)
- ml 관련 내용 외에도 익명 질문 게시판을 통해 '데이터 분석가' 혹은 '개발자' 관련 커리어 질의응답 시간을 가졌음.
---
- 내가 가고 싶은 회사, 팀을 정하자! 무엇을 필요로 하는지 → 목표를 잡고 어떻게 준비해 나갈지 강사님께 여쭤볼 내용이 있으면, 적극적으로 여쭤보자.
---
- [전 세계 디자이너들 난리난 피그마 컨퍼런스 요약 | Config2024](: AI 활용) https://www.youtube.com/watch?v=aduVMrS-v4o
=> 문제 의식, 목적을 알고 인공지능을 사용할 줄 알아야 한다!


### keyword
> 선형회귀, 다중회귀, 릿지, 라쏘

> 한 일: 
- 선형회귀를 통해 `데이터를 가장 잘 대변하는 최적의 선`을 찾아보자.

> 자주 틀리는 내용!
- 


> 어려웠던 예제!
-

#
#
#

# 이번주 학습 내용 정리 목차
## `git`의 `ml` 폴더에서도 확인이 가능합니다.
#### https://github.com/iam-Aerin/ml/tree/master

1. k-최근접 이웃 회귀 (p. 115 ~ ) `3-1.ipynb`
    1. 회귀분석 `KNeighborsRegressor`
    > `from sklearn.neighbors import KNeighborsRegressor`
    2. 과대적합과 과소적합 (p.122 (?))
    
2. 선형 회귀 (Linear regression) (p.130) `3-2.ipynb`
    1. LinearRegression()
    > `from sklearn.linear_model import LinearRegression`
    2. 다항회귀 (p.139)
    > (lr.coef_, lr.intercept_)
    
3. 특성공학과 규제 (p.150) `3-3,ipynb`
    1. 특성공학
    2. 규제
    3. 릿지 ridge
    > `from sklearn.linear_model import Ridge`
    4. 라쏘 rasso
    > `from sklearn.linear_model import Lasso`

# 1. k-최근접 이웃 회귀 (K-Nearest Neighbors Regression)

## 1-1. 회귀 분석 `KNeighborsRegressor`
- K-최근접 이웃 회귀(KNN 회귀)는 **가장 가까운 K개의 데이터를 참고하여 평균을 계산**하는 방식으로 예측하는 회귀 모델이다.
- 선형적인 관계를 가정하지 않고, 데이터 분포에 따라 유연하게 조정 가능하다.

#### 📌 `KNeighborsRegressor` 사용법
```python
from sklearn.neighbors import KNeighborsRegressor
knn_regressor = KNeighborsRegressor(n_neighbors=5)
knn_regressor.fit(X_train, y_train)
predictions = knn_regressor.predict(X_test)
```
- `n_neighbors`: 고려할 최근접 이웃의 개수(K 값)
- `fit()`: 학습 데이터로 모델 훈련
- `predict()`: 새로운 데이터 예측

## 1-2. 과대적합과 과소적합

#### ✅ 과대적합 (Overfitting)
- K 값이 너무 작을 경우(예: K=1)
- 모델이 개별 데이터 포인트에 너무 민감해져서 훈련 데이터에 완벽히 맞지만, 테스트 데이터에 일반화되지 않음.

#### ✅ 과소적합 (Underfitting)
- K 값이 너무 클 경우(예: K=50)
- 모델이 지나치게 평균적인 예측을 하여 데이터의 패턴을 잘 반영하지 못함.

#### 🔹 최적의 K 값 찾기
- 일반적으로 **K=3~10** 사이에서 적절한 값을 선택하는 것이 일반적임.
- **교차 검증(Cross Validation)** 을 활용하여 최적의 K 값을 찾을 수 있음.

```python
from sklearn.model_selection import GridSearchCV
param_grid = {'n_neighbors': range(1, 20)}
grid_search = GridSearchCV(KNeighborsRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("Best K value:", grid_search.best_params_['n_neighbors'])
```

이렇게 최적의 K 값을 찾아 모델의 성능을 최적화할 수 있다.


# 2. 선형 회귀 (Simple Linear Regression)
# 독립 변수가 한 개일 때 사용 (단순한 선형 관계를 분석)

```
예제:
 - 키와 몸무게의 관계
 - 공부 시간과 시험 점수의 관계

 사용할 때:
 - 한 개의 독립 변수와 종속 변수 간의 관계를 분석할 때
 ```


### 다중 선형 회귀 (Multiple Linear Regression)
# 여러 개의 독립 변수가 종속 변수에 영향을 주는 경우 사용
# 종속 변수와 독립 변수 간의 관계를 선형으로 가정

# 예제:
# 집 가격 예측 (면적, 방 개수, 위치 등의 독립 변수를 사용)
# 광고 비용(독립 변수)과 매출(종속 변수)의 관계 분석

# 사용할 때:
# - 독립 변수들이 종속 변수에 영향을 주며, 관계가 선형일 것으로 예상될 때
# - 독립 변수 간 다중공선성(multicollinearity)이 크지 않을 때

## 3-3. 릿지 회귀 (Ridge Regression)
# 다중 선형 회귀에서 과적합(overfitting)을 방지하기 위해 L2 정규화(페널티)를 추가한 모델
# 회귀 계수를 너무 크게 만드는 것을 방지 → 다중공선성 문제 완화

# 예제:
# - 고차원의 데이터에서 다중 선형 회귀를 사용할 때 과적합을 방지하기 위해 활용
# - 의료 데이터(환자의 여러 건강 지표를 이용해 질병 확률 예측)에서 불필요한 계수의 크기를 줄이고 모델 안정성을 높일 때

# 사용할 때:
# - 다중공선성이 있는 데이터에서 과적합을 방지할 때
# - 예측 성능을 향상시키기 위해 회귀 계수 크기를 조정하고 싶을 때

## 3-4. 라쏘 회귀 (Lasso Regression)
# 다중 선형 회귀에서 L1 정규화(페널티)를 적용하여 계수 중 일부를 0으로 만듦 → 변수 선택 기능 제공
# 불필요한 독립 변수를 자동으로 제거 (모델이 스스로 중요한 변수만 선택)

# 예제:
# - 주식 가격 예측 (많은 변수 중 중요한 몇 개만 선택하여 분석)
# - 유전학 데이터 분석 (수천 개의 유전자 중 특정 질병과 관련된 소수만 선택)

# 사용할 때:
# - 데이터에 많은 변수가 있고, 그중 일부만 중요한 경우
# - 변수 선택을 자동화하고 싶을 때


# 정리: 언제 어떤 모델을 사용해야 할까?
# 상황별 모델 추천
situation_model_mapping = {
    "독립 변수가 여러 개이고, 선형 관계를 가정": "다중 선형 회귀",
    "다중공선성이 존재하고 과적합을 방지하고 싶음": "릿지 회귀",
    "독립 변수가 많고, 중요 변수만 선택하고 싶음": "라쏘 회귀",
    "독립 변수가 한 개만 있을 때": "단순 선형 회귀"
}

# 추천된 모델 출력
def recommend_model(situation):
    return situation_model_mapping.get(situation, "해당 상황에 맞는 모델이 없습니다.")

# 사용 예시
print(recommend_model("다중공선성이 존재하고 과적합을 방지하고 싶음"))


