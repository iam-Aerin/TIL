# 3월 2주차 TIL 내용 정리

## 4~7 Mar 2025
> 의 수업 내용 정리를 다룹니다. 
> 날짜별 정리 내용이 아닌, 관련 교육 내용 <ml>은 https://github.com/iam-Aerin/ml/tree/master [github]의 repository 를 통해 확인 가능합니다. 

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
> 선형회귀, 다중회귀, 릿지, 라쏘, 로지스틱회귀

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
    
3. 특성공학과 규제 (p.150) `3-3.ipynb`
    1. 특성공학
    2. 규제
    3. 릿지 ridge
    > `from sklearn.linear_model import Ridge`
    4. 라쏘 rasso
    > `from sklearn.linear_model import Lasso`

4. 로지스틱 회귀 (p.176) `4-1.ipynb`
   1. 이진 분류
   2. 시그모이드 함수
   3. 다중 분류
   4. 소프트맥스 함수
   5. 확률적 경사 하강법 (p.199) `4-2.ipynb`

5. 트리 알고리즘 (p.220) `5-1.ipynb`
   1. 결정트리
      1. 불순도
      2. 가지치기
   2. 교차 검증과 그리드 서치 (p.242) `5-2.ipynb`
      1. 검증 세트
      2. 교차 검증 
         `cross_validate()`
      3. 하이퍼 파라미터 튜닝

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


### ✅ 개념
- 선형 회귀는 **독립 변수(X)와 종속 변수(Y) 간의 관계를 직선(선형 함수)으로 모델링하는 회귀 기법**
- 입력 변수의 선형 결합을 통해 출력을 예측함

### ✅ 선형 회귀 공식

y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε

- **β₀** : 절편(intercept)
- **β₁, β₂, ..., βₙ** : 회귀 계수(가중치)
- **X₁, X₂, ..., Xₙ** : 독립 변수(설명 변수)
- **ε** : 오차항(residual error)

### ✅ 종류
1. **단순 선형 회귀(Simple Linear Regression)**
## 독립 변수가 **1개**일 때 사용
   ```python
   from sklearn.linear_model import LinearRegression
   model = LinearRegression()
   model.fit(X_train, y_train)
   predictions = model.predict(X_test)
   ```

2. **다중 선형 회귀(Multiple Linear Regression)**
 ## 독립 변수가 **여러 개**일 때 사용
   ```python
   model = LinearRegression()
   model.fit(X_train, y_train)
   ```

### ✅ 장점
- 해석이 간단하고 구현이 쉬움
- 계산량이 적어 빠르게 학습 가능
- 과적합이 적음 (단, 다중공선성이 있을 경우 문제 발생 가능)

### ✅ 단점
- **독립 변수와 종속 변수 간의 관계가 선형이어야 함**
- 이상치(Outlier)에 민감함
- 다중공선성(multicollinearity) 문제가 발생할 수 있음

---

## 2-2. 다항회귀 (Polynomial Regression)
### ✅ 개념
- 다항 회귀는 **독립 변수와 종속 변수 간의 관계가 곡선(비선형)일 때 적용하는 회귀 기법**
- 선형 회귀의 확장 개념이며, **입력 변수의 거듭제곱 항(제곱, 세제곱 등)을 추가**하여 곡선을 모델링

### ✅ 다항 회귀 공식

y = β₀ + β₁X + β₂X² + β₃X³ + ... + βₙXⁿ + ε

- **X², X³ 등의 고차항을 추가하여 비선형 관계를 학습 가능**
- 선형 회귀와 마찬가지로 가중치(β)를 학습하여 최적의 예측 모델 생성

### ✅ 예제 (Python 코드)
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# 2차 다항 회귀 모델 생성
poly_model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
poly_model.fit(X_train, y_train)
predictions = poly_model.predict(X_test)
```
- `PolynomialFeatures(degree=2)`: 입력 변수의 2차 항을 추가
- `make_pipeline()`: 다항 변환 후 선형 회귀를 적용하는 파이프라인 생성

### ✅ 장점
- 선형 회귀보다 **비선형 데이터 학습이 가능**
- 상대적으로 간단한 변환만으로 곡선 관계를 표현할 수 있음

### ✅ 단점
- 차수를 너무 높이면 **과적합(Overfitting)** 가능성 증가
- 다항식의 차수를 몇 차까지 설정할지 정하는 것이 중요

---

# 3. 특성 공학과 규제

## 3-1. 특성공학 (Feature Engineering)
- 머신러닝 모델의 성능을 향상시키기 위해 **데이터의 특성을 변형, 생성, 조합하는 과정**
- **좋은 특성을 만들어야 모델의 성능이 향상됨**

#### ✅ 특성 공학의 주요 기법
1. **다항 특성 생성**
   - 기존 특성을 거듭제곱하여 새로운 특성을 생성
   ```python
   from sklearn.preprocessing import PolynomialFeatures
   poly = PolynomialFeatures(degree=2, include_bias=False)
   X_poly = poly.fit_transform(X)
   ```

---

## 3-2. 규제 (Regularization)
- 머신러닝 모델이 과적합되지 않도록 **모델의 복잡도를 제한하는 기법**
- 선형 회귀 모델에서 **회귀 계수(가중치)를 제한하여 모델을 단순하게 유지**

#### ✅ 규제 종류: 릿지, 라쏘

## 3-3. **릿지 회귀 (Ridge Regression, L2 정규화)**
   - 회귀 계수의 제곱합을 최소화하여 과적합 방지
   ```python
   from sklearn.linear_model import Ridge
   ridge = Ridge(alpha=1.0)
   ridge.fit(X_train, y_train)
   ```

## 3-4. **라쏘 회귀 (Lasso Regression, L1 정규화)**
   - 일부 회귀 계수를 0으로 만들어 **불필요한 특성을 자동 선택**
   ```python
   from sklearn.linear_model import Lasso
   lasso = Lasso(alpha=0.1)
   lasso.fit(X_train, y_train)
   ```

#### ✅ 규제 사용 시기
- **릿지 회귀**: 다중공선성이 있는 데이터에서 과적합을 방지하고 싶을 때
- **라쏘 회귀**: 중요한 특성만 자동 선택하고 싶을 때


>정리: 언제 어떤 모델을 사용해야 할까?
- 상황별 모델 추천
situation_model_mapping = {
    "독립 변수가 여러 개이고, 선형 관계를 가정": "다중 선형 회귀",/
    "다중공선성이 존재하고 과적합을 방지하고 싶음": "릿지 회귀",/
    "독립 변수가 많고, 중요 변수만 선택하고 싶음": "라쏘 회귀",/
    "독립 변수가 한 개만 있을 때": "단순 선형 회귀"
}

# 로지스틱 회귀 & 트리 알고리즘

# **4. 로지스틱 회귀 (p.176) `4-1.ipynb`**
로지스틱 회귀는 **선형 회귀를 기반으로 확률을 예측하는 분류 모델**로, **이진 분류(Binary Classification)** 및 **다중 분류(Multi-Class Classification)** 문제에 사용됩니다.

---

## **4-1. 이진 분류**
- **출력값이 0 또는 1**인 문제를 해결하는 분류 알고리즘.
- 입력 데이터 \( X \)를 통해 **선형 회귀 값**을 계산한 후, **시그모이드 함수(Sigmoid Function)**를 적용하여 확률값을 출력.

---

## **4-2. 시그모이드 함수**
- **로지스틱 회귀에서 사용되는 활성화 함수**로, **출력을 0~1 사이의 확률 값으로 변환**함.

- **특징:**
  - 입력 값이 **작을수록 0에 가까운 확률**, **클수록 1에 가까운 확률**.
  - **이진 분류에서 확률적 예측을 수행**하는 데 사용됨.

---

## **4-3. 다중 분류**
- **3개 이상의 클래스**를 예측하는 문제를 해결하는 로지스틱 회귀 확장 버전.
- 개별 클래스에 대한 **선형 회귀 값을 계산한 후, 소프트맥스(Softmax) 함수**를 적용하여 확률을 구함.

---

## **4-4. 소프트맥스 함수**
- **다중 분류에서 사용되는 확률 변환 함수**로, 모든 클래스에 대해 확률 분포를 생성.

- **특징:**
  - 모든 클래스의 확률 총합이 **1이 되도록 정규화**.
  - 가장 높은 확률을 가진 클래스를 최종 예측값으로 사용.

---

## **4-5. 확률적 경사 하강법 (p.199) `4-2.ipynb`**
- 경사 하강법(GD)의 한 형태로, **모든 데이터가 아닌 하나의 샘플만 사용하여 가중치를 업데이트**.
- 일반적인 손실 함수:
  - **이진 분류** → **Binary Cross-Entropy (Log Loss)**
  - **다중 분류** → **Categorical Cross-Entropy**
- **장점:** 빠른 학습 속도, 실시간 업데이트 가능.
- **단점:** 기울기가 불안정하여 수렴 속도가 불규칙할 수 있음.

---

# **5. 트리 알고리즘 (p.220) `5-1.ipynb`**
트리 알고리즘은 **데이터를 분할하여 학습하는 비선형 모델**로, 결정 트리(Decision Tree)와 앙상블 학습(랜덤 포레스트, 그래디언트 부스팅 등)에 사용됨.

---

## **5-1. 결정 트리**
#### ✅ **(1) 불순도**
- **트리가 데이터를 분할하는 기준**.
- 대표적인 불순도 측정 방법:
  - **지니 불순도 (Gini Impurity)**

#### ✅ **(2) 가지치기 (Pruning)**
- **트리가 과적합되는 것을 방지**하기 위한 방법.
- **사전 가지치기(Pre-Pruning)**: 최대 깊이 제한, 최소 샘플 수 제한 적용.
- **사후 가지치기(Post-Pruning)**: 학습 후 필요 없는 노드를 제거.

---

## **5-2. 교차 검증과 그리드 서치 (p.242) `5-2.ipynb`**
#### ✅ **(1) 검증 세트**
- **모델 평가를 위한 데이터 세트**.
- 과적합 방지를 위해 **훈련 세트와 별도로 유지**.

#### ✅ **(2) 교차 검증 (`cross_validate()`)**
- 데이터를 **K개(예: 5-fold)로 나누어 모델을 평가**하는 기법.
- **일반적인 K-fold 교차 검증 과정**
  1. 데이터를 **K개로 분할**.
  2. **K-1개의 세트로 훈련**, 나머지 1개로 검증.
  3. **이 과정을 K번 반복하여 평균 성능을 계산**.

```python
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
scores = cross_validate(dt, train_input, train_target, cv=5, return_train_score=True)
print(scores['test_score'].mean())  # 평균 테스트 점수 출력
```