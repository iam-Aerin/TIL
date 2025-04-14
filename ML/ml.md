# Machine Learning (ML)
> 위 문서는 머신러닝 (혼자 공부하는 머신러닝 + 딥러닝 책을 기반으로) 공부한 내용을 `TIL` 챌린지를 위해 작성한 내용입니다. 
> #내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌
>
> `글로벌소프트웨어캠퍼스와 동아일보가 함께 진행하는 챌린지입니다.`
---
> 더 자세한 코드/ 예제는 <ml>은 https://github.com/iam-Aerin/ml/tree/master [github]의 repository 를 통해 확인 가능합니다. 

(수정후) **머신러닝** (주제별) 내용을 정리합니다.
(수정전) ~이 내용은 날짜별 (혹은 주차별) TIL 기록을 위해 생성했습니다.~

# TIL(Today I Learned) 오늘 배운 내용을 기록합니다.

### Links (학습에 사용된 링크모음)
- ml 관련 내용 외에도 익명 질문 게시판을 통해 '데이터 분석가' 혹은 '개발자' 관련 커리어 질의응답 시간을 가졌음.
---
- 내가 가고 싶은 회사, 팀을 정하자! 무엇을 필요로 하는지 → 목표를 잡고 어떻게 준비해 나갈지 강사님께 여쭤볼 내용이 있으면, 적극적으로 여쭤보자.
---
- [전 세계 디자이너들 난리난 피그마 컨퍼런스 요약 | Config2024](: AI 활용) https://www.youtube.com/watch?v=aduVMrS-v4o
=> 문제 의식, 목적을 알고 인공지능을 사용할 줄 알아야 한다!


### keyword
> 선형회귀, 다중회귀, 릿지, 라쏘, 로지스틱회귀, 다중회귀, 의사결정트리 알고리즘, 딥러닝, 머신러닝

> 한 일: 

- 파이썬 연습을 위해, 프로그래머스 - 입문 문제 풀이를 진행함. (https://github.com/iam-Aerin/algo) 에서 확인 가능함. 
- 선형회귀를 통해 `데이터를 가장 잘 대변하는 최적의 선`을 찾아보자.

> 자주 틀리는 내용!
- 


> 어려웠던 예제!
-

#
#
#

# 🤖 머신러닝 🤖
## `git`의 `ml` 폴더에서도 확인이 가능합니다.
> https://github.com/iam-Aerin/ml


## 🏷 목차

### 1. K-최근접 이웃 회귀 (KNN Regression) (p.115)  
   - [`3-1.ipynb`](#)  

### 2. 선형 회귀 (Linear Regression) (p.130)  
   - [`3-2.ipynb`](#)  

### 3. 특성 공학과 규제 (Feature Engineering & Regularization) (p.150)  
   - [`3-3.ipynb`](#)  

### 4. 로지스틱 회귀 (Logistic Regression) (p.176)  
   - [`4-1.ipynb`](#)  

### 5. 트리 알고리즘 (Tree Algorithms) (p.220)  
   - [`5-1.ipynb`](#)  

### 6. 비지도 학습 (Unsupervised Learning) (p.286)  
   - [`6-1.ipynb`](#)  
   - **6-1. 군집 알고리즘 (Clustering) (p.286)**  
   - **6-2. K-평균 (K-Means) (p.300)**  
     - [`6-2.ipynb`](#)  
   - **6-3. 주성분 분석 (PCA) (p.318)**  
     - [`6-3.ipynb`](#)  

### 7. 딥러닝 (Deep Learning) (p.339)  
   - [`7-1.ipynb`](#)  
   - **7-1. 인공 신경망 (Artificial Neural Networks) (p.339)**  
   - **7-2. 심층 신경망 (Deep Neural Networks) (p.367)**  
     - [`7-2.ipynb`](#)  

### 8. 합성곱 신경망 (CNN) (p.422)  
   - [`8-1.ipynb`](#)  
   - **8-1. 합성곱 (Convolution) (p.422)**  

# MACHINE LEARNING (ml)
### > `https://github.com/iam-Aerin/ml` 에 내용 정리함.
> #차트를 시각화해서 점찍어보기
- `#matplotlib library 를 설치해서 시각화하기 - 터미널에 (vscode)`

## KNN (K-Neareat Neighbours): K-최근접 이웃 알고리즘
- https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
- SciKit 라이브러리를 통해 (vscode에서 install 설치를 하고) -> 아래와 같이 내가 사용할
- `KNeighborsClassifier` 알고리즘 기능을 불러와 사용해보겠다.

## 02-1. 훈련 세트와 테스트 세트 (p.66)
- 지도학습으로 훈련 세트와 테스트 세트를 구분하여 나의 모델을 학습시킴.
- 학습 인풋/ 정답 데이터 & 테스트 인풋/ 정답 데이터를 만듦. 

## 02-2 데이터 전처리 (p.87)
- 표준점수화해서 데이터를 학습 시키고, 평가(테스트) 한다.
- 점수를 표준점수로 바꾸겠다
- 표준점수는 각 데이터가 원점에서 몇 표준편차만큼 떨어져 있는지를 나타내는 값이다.
> 자세한 예제 문제 코드는 `https://github.com/iam-Aerin/ml/blob/master/2.2.ipynb` 에서 확인 가능함.


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

---
# 🔍 K-최근접 이웃(KNN) 알고리즘 vs K-최근접 이웃 회귀(KNN 회귀)

K-최근접 이웃(KNN)은 **분류(Classification)와 회귀(Regression)에서 모두 사용**됩니다.  
두 방식 모두 **가장 가까운 `k`개의 데이터**를 사용하여 예측하지만, **예측 방식이 다릅니다.**  

---

## 📌 KNN 분류 (Classification)
- 새로운 데이터가 들어오면, **가장 가까운 `k`개의 데이터 중 다수결 투표**를 통해 클래스를 결정합니다.  
- **예측 방식:** `k`개의 이웃 중 **가장 많이 등장한 클래스(Label)를 선택**  
- `k`가 작으면 → **과대적합 위험** (훈련 데이터에 너무 민감)  
- `k`가 크면 → **과소적합 위험** (너무 단순한 모델)  

### ✅ **예제 (k=3)**  
```plaintext
🐱 🐶 🐶  → 과반수가 🐶 → 예측값: 🐶


---
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'n_neighbors': range(1, 20)}
grid_search = GridSearchCV(KNeighborsRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)
print("Best K value:", grid_search.best_params_['n_neighbors'])
```

이렇게 최적의 K 값을 찾아 모델의 성능을 최적화할 수 있다.


# 2. 선형 회귀 (Simple Linear Regression)
> 독립 변수가 한 개일 때 사용 (단순한 선형 관계를 분석)

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

### ✅ 예제
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

## **5-3. 트리의 앙상블**
- 랜덤 포레스트
> 현시점에서 가장 보편적으로, 성능이 높다고 알려진 알고리즘.
>
> 정형 데이터 에서 e.g. 표 구조의 숫자 데이터 (csv) 혹은 엑셀

`정형 데이터와 비정형 데이터`
- 부트스트랩 샘플링: 데이터 세트에서 중복을 허용하여 데이터를 샘플링하는 방식
`RandomForestRegressor()`

랜덤포레스트는 결정트리의 앙상블이기 떄문에
DecisionTreeClassifier 가 제공하는 중요한 매개 변수를 모두 제공함.
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

####  랜덤포레스트 실행
`RandomForestClassifier`

```python
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_jobs=1)
scores = cross_validate(rf, train_input, train_target, return_train_score=True, n_jobs=1)
print(scores)
```
 cross_validate는 교차 검증을 수행하여 모델의 성능을 평가하는 함수이다.
 return_train_score=True 옵션을 사용하면 훈련 세트 점수도 함께 제공된다.
 결과는 fit_time, score_time, test_score, train_score 등을 포함하는 딕셔너리 형태로 반환된다.

 💡 이 코드의 목적은 랜덤 포레스트 모델이 훈련 데이터와 검증 데이터에서 얼마나 잘 작동하는지를 확인하는 것!




#### 엑스트라 트리
- 엑스트라 트리는 랜덤 포레스트와 유사하지만, 노드를 분할할 때 최적의 분할을 찾는 것이 아니라 무작위로 분할하는 방식이다.
```python
from sklearn.ensemble import ExtraTreesClassifier
et = ExtraTreesClassifier(n_jobs=1)

scores = cross_validate(et, train_input, train_target, return_train_score=True, n_jobs=1)
print(scores)
```

- 그래디언트 부스팅 (Gradient Boosting)

그래디언트 부스팅은 트리의 오차를 보완하는 방법으로 앙상블을 구성하는 기법이다. 과대적합에 강하고 일반적으로 높은 일반화 성능을 기대할 수 있다.
```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_validate

gb = GradientBoostingClassifier(n_estimators=500)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=1)
print(scores)
```

---

## 7. 딥러닝 (Deep Learning) (p.339)

### ✅ 딥러닝이란?

딥러닝(Deep Learning)은 인공 신경망의 층(layer)을 깊게 쌓아 올려 복잡한 데이터의 패턴을 자동으로 학습하는 머신러닝의 한 분야이다.

- 기존 머신러닝과 달리 **특성(feature)을 자동으로 추출**함
- **비선형 문제** 및 **복잡한 데이터 처리**에 뛰어난 성능을 보임
- 대표적인 딥러닝 프레임워크: **TensorFlow, PyTorch**

---

## 7-1. 인공 신경망 (Artificial Neural Networks, ANN) (p.339)  
📂 [`7-1.ipynb`](#)

### ✅ 개념
- 사람의 뇌 신경망 구조에서 영감을 받아 개발한 알고리즘
- 입력층, 은닉층, 출력층으로 구성된 네트워크를 통해 데이터를 학습

### ✅ 주요 키워드
- **뉴런(Neuron)**: 신경망의 기본 단위로 입력값을 받아 처리하는 계산 단위
- **활성화 함수(Activation function)**: 뉴런이 출력값을 생성할 때 사용하는 함수
  - `Sigmoid`: 출력값을 0~1 사이로 변환 (이진 분류에서 사용)
  - **ReLU(렐루)**: 비선형 활성화 함수로 깊은 네트워크에서 주로 사용됨
- **손실함수(Loss Function)**: 실제값과 예측값 사이 오차를 측정 (예: MSE, Cross-Entropy)
- **옵티마이저(Optimizer)**: 오차를 최소화하기 위해 네트워크의 가중치를 조정하는 알고리즘 (예: SGD, Adam)

### ✅ TensorFlow로 ANN 모델 구축 예제
```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # 이진분류 예시
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=50, batch_size=32)
```

## 7-2. 심층 신경망 (Deep Neural Networks, DNN)

인공 신경망(ANN)에 은닉층(hidden layer)을 여러 개 추가하여 네트워크를 깊게 만든 형태이다.  
복잡한 데이터의 특성을 효과적으로 학습할 수 있다.

### ✅ 주요 활성화 함수 (Activation Functions)

- **시그모이드(sigmoid)**  
  - 출력값을 0과 1 사이로 변환하여 확률로 표현
  - 주로 이진 분류 문제에서 사용

- **소프트맥스(softmax)**  
  - 여러 클래스 간의 분류 확률을 나타낼 때 사용
  - 클래스별 확률의 총합은 항상 1

- **렐루(ReLU)**  
  - 음수 값은 0, 양수 값은 그대로 출력하는 함수
  - 기울기 소실 문제를 방지하여 깊은 신경망에서 널리 사용

### ✅ 심층 신경망 예시 (TensorFlow Keras)

```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

# 8. 합성곱 신경망 (Convolutional Neural Networks, CNN)

합성곱 신경망(CNN, Convolutional Neural Networks)은 이미지 또는 영상과 같은 공간적 특성을 가진 데이터를 처리할 때 효과적인 신경망 구조이다.

## ✅ CNN의 핵심 개념

### 📌 합성곱(Convolution)
- 이미지를 필터(커널)로 훑어가며 특성을 추출하는 과정
- 이미지의 지역적 픽셀 정보를 기반으로 학습한다.

### 📌 합성곱층(Convolution Layer)
- 여러 개의 필터를 적용하여 이미지에서 다양한 특징(feature)을 추출한다.
- 필터의 개수만큼 서로 다른 특징 맵(feature map)이 생성된다.

### 📌 풀링층(Pooling Layer)
- 특징 맵(feature map)의 크기를 축소하여 연산량을 감소시키고, 중요한 특징만을 유지한다.
- 대표적인 방식: MaxPooling(최대 풀링), AveragePooling(평균 풀링)

### 📌 패딩(Padding)
- 입력 이미지 가장자리에 가상의 데이터(주로 0)를 추가하여, 합성곱 연산 후에도 이미지 크기를 유지하고 가장자리 정보의 손실을 방지한다.


✅ **추가 예제 코드 (TensorFlow Keras)**  
```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(pool_size=(2,2)),
    keras.layers.Conv2D(64, kernel_size=(3,3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

## 8-1. 

## 9-1. 순차 데이터(Sequential Data)와 순환 신경망(RNN)

#### 순차 데이터(Sequential Data)
순차 데이터란 시간이나 순서가 중요한 데이터 유형을 의미한다. 각 데이터 포인트가 특정 순서에 따라 나타나며, 이전 데이터가 이후 데이터에 영향을 미치는 구조를 가지고 있다.

- 순차 데이터의 예시
- **자연어 처리 (NLP)**: 문장은 단어들이 특정 순서대로 배열되어 의미를 가짐.  
  예시:  
  ```text
  "I am a boy"
```
시계열 데이터: 주가, 날씨 데이터, 센서 데이터 등 시간에 따라 변화하는 데이터.
음성 및 오디오 데이터: 소리는 시간 축을 따라 변화하며 순차적 패턴을 가짐.
```

#### 순환 신경망 (RNN, Recurrent Neural Network)

RNN은 순차 데이터를 다루기 위해 설계된 신경망으로, 일반적인 신경망(MLP, CNN)과는 다르게 이전 정보(과거 데이터)를 기억하고 활용할 수 있는 구조를 가지고 있다.

#### RNN의 구조
일반적인 신경망은 입력을 독립적으로 처리하지만, RNN은 **"순환 연결(Loop Connection)"** 을 가지고 있어 과거 정보를 저장하는 **은닉 상태(hidden state)** 를 유지한다.  
즉, 이전 단계의 출력이 현재 단계의 입력으로 전달되므로, 순차적 관계를 학습할 수 있다.

- RNN의 활용 사례

  - 1. 자연어 처리 (NLP)
    - 기계 번역 (번역기)
    - 감정 분석 (긍정/부정 분류)
    - 챗봇 및 대화 모델 (ChatGPT 같은 모델의 기본 구조)

  - 2. 음성 및 오디오 처리
    - 음성 인식 (예: Siri, Google Assistant)
    - 음악 생성 (AI 작곡)

  - 3. 시계열 데이터 분석
    - 주식 가격 예측
    - 날씨 예측


---

#### RNN의 문제점

- 기울기 소실 (Vanishing Gradient)
  - 역전파 과정에서 시간이 길어질수록 기울기가 점점 작아져, 긴 시퀀스에서는 학습이 잘되지 않는다.

- 장기 의존성 문제
  - 너무 과거의 정보는 잘 기억하지 못한다.

이 문제를 해결하기 위해 LSTM (Long Short-Term Memory)과 GRU (Gated Recurrent Unit) 같은 개선된 순환 신경망이 등장했다.
