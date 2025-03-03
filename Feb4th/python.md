# 2월 4주차 TIL 내용 정리

## 24~28 Feb 2025
> 의 수업 내용 정리를 다룹니다. 
> 날짜별 정리 내용이 아닌, 관련 교육 내용 <python>은 https://github.com/iam-Aerin/python/tree/master [github]의 repository 를 통해 확인 가능합니다. 

#
https://www.notion.so/196d384c40db80129561c25961bf1bba
> `git` 이외에도 노션 (https://www.notion.so/196d384c40db80129561c25961bf1bba) 을 통해 학습 내용을 정리 중입니다.
#

>이 내용은 날짜별 (혹은 주차별) TIL 기록을 위해 생성했습니다. 
>#내맘대로TIL챌린지 #동아일보 #미디어프론티어 #글로벌소프트웨어캠퍼스 #GSC신촌

TIL(Today I Learned) 오늘 배운 내용을 기록합니다.

-> 현재 이 프로젝트/ 폴더가 어떤 내용인지를 설명하는 파일 (설명서) - (README)

linux
markdown
=> 코드가 바뀔 때 마다, 저장 - add - commit 을 거침.

### Links (이번주 학습에 사용된 링크모음)
- [numpy] (: 모듈 설치 및 가이드 documentation) https://numpy.org/doc/
- [pandas] (: 모듈 설치 및 가이드 documentation) https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

### keyword
> Series, 머신러닝, 딥러닝, KNN

> 한 일: 
- numpy, pandas 라이브러리를 통해 숫자 배열 관련 데이터 분석을 더 쉽게, 엑셀 혹은 csv 데이터를 불러와 그 안의 값을 들여다보기 등

- `programmers`에서 관련 예제 풀이 (`algo`: https://github.com/iam-Aerin/algo)를 통해 문제 풀이 세부 내용이 확인가능합니다. 


> 자주 틀리는 내용!


> 어려웠던 예제!


#
#
#

# 이번주 학습 내용 정리 목차
## `git`의 `pandas` 폴더에서도 확인이 가능합니다.
#### https://github.com/iam-Aerin/pandas/tree/master

1. Numpy
    1. ndarry 생성하기
    2. ndarry 자료형
    3. 산술연산
    4. 색인과 슬라이싱 (indexing, slicing)
    5. boolean 값으로 데이터 선택
    6. 팬시 색인 (fancy indexing)
    7. 배열 전치
    8. numpy 함수
2. Pandas
    1. Series
    2. NaN (Not a Number)
    3. fancy indexing
    4. bool indexing
    5. 결측치 (NaN) 처리
    6. 슬라이싱
    7. DataFrame
3. File 불러오기 (excel, csv)
4. 머신러닝닝

# 1. Numpy (넘파이)
- 라이브러리
- 항상 사용할 라이브러리를 코드 맨 윗줄에 `import numpy as np` 로 호출하기

## 1-1. ndarry
- np는 연산이 편하다. 
```python
my_array = np.arange(1000000)
my_array = my_array * 2
```
`.dim` 배열의 차원수를 알려주는 명령어
`np.zeros(10)` : 0이 열번 반복되는 숫자 배열을 만들어줘.
`([0]) * 10` : 위의 반복되는 숫자 배열을 만드는 방식과 똑같은 함수이다. 

## 1-2. ndarray 자료형
- 숫자 배열을 생성 할 때, 형을 지정해서 생성하도록 명령
`dtype=np.float64' 혹은 `dtype=np.int32` 와 같이 생성할 array 뒤에 생성하고자 하는 형태를 , 다음에 적어준다. 

e.g. 
```python
arr1 = np.array([1, 2, 3], dtype=np.float64)
```

만일, 원래의 형태를 다른 형태로 형변환 하고 싶다면? 
e.g. 기본값 (int) 를 (float) 타입으로 변환해본다면?
```python
arr1 = np.array([1, 2, 3])
# -> int타입 
float_arr1 = arrl.astype(np.float) # -> float 타입으로 바꿔줘. 
```

## 1-3. 산술연산
- 같은 위치의 아이템들끼리의 사칙연산의 기본값이다. 
- 비교연산도 가능하다. 

```python
arr = np.array([[1, 2, 3],[4, 5, 6]])
arr2 = np.array([[3, 2, 1], [1, 2, 3]])
print(arr > arr2)
# => 비교 연산 많이 쓰게 될 것이다. 
# => 아이템의 자리를 기준으로 같은 자리에 있는 값 중 > 부등호 비교를 통해 True 와 False를 반환한다. 
print(arr == 3)
# => == 조건에 부합하는 결과를 새로운 리스트로 반환 한다. 
```

## 1-4. 색인과 슬라이싱
- indexing and slicing
```python
arr = np.arange(10)
arr[2:5]
# => 2번째 데이터 부터 5번째 데이터 미만까지를 슬라이싱 해주세요. 
arr[2:5] = 10 # => 자른 다음 그 자른 값에 `10`을 대입할 수도 있다. 
```

- 2차원 데이터에 접근하는 방법
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr[1] # => [4, 5, 6]
arr[1][1] # => 5
arr[1, 1] # => 5
# 두번째와 세번째의 표현은 결국 같은 표현 방법이다. 
```
- 3차원 데이터에서 인덱싱 접근 방법도 동일하다. 

## 1-5. boolean 값으로 데이터 선택
#### 데이터 비교: 각각의 아이템들의 순서에 맞게 비교가 된다. 

## 1-6. fancy indexing 
#### 특정한 요소를 인덱싱해 골라낼 때 
- 행을 선택하거나
- 열을 함께 선택할 수 있다. 

## 1-7. 배열의 전치
#### 배열의 축을 바꾼다. 
- 행렬의 곱셈, 행렬의 내적, 곱
`arr @ arr.T`
`np.dot(arr, arr.T)`

## 1-8. numpy 함수
`np.random.standard_normal(size=(3, 3))` : 3, 3 의 행렬을 가지는 랜덤 숫자의 행렬을 만들어줘. 

`np.sqrt(samples)` : 숫자 배열에 루트를 씌워줘. 

### 만일, 값에 `nan`으로 출력된 값이 있다면, 그것은 python의 `none` 값과 유사한, 즉 `결측치` 이다. 

`np.abs(samples)` : samples라는 숫자배열에 절대값 (absolute)를 취해줘. 

`np.isnan(arr1)` : 나의 배열 arr1에 `nan`이 포함 되어 있나요?

# 2. Pandas
## 2. 1 Series 
### 대문자로 시작하는 `Series`는 클래스임을 알 수 있다. 
- dtype: `object` 는 판다스에서의 `string`이라고 보면 된다. 

- Series의 경우 음수 인덱싱은 적용 할 수 없다. 
    - e.g. s[-1] 은 불가능하다. 

## 2.2. NaN (Not a Number)

```python
s = pd.Series([1, 2, 3, np.nan])
# => 0  1.0
     1  2.0
     2  3.0
     3  NaN
     dtype: float64
```
## 2.3. fancy indexing
- 인덱스를 숫자가 아닌 문자로도 표현 할 수 있다. 
```python
pd.Series(f, index = list('abcd'))
# => f 배열의 인덱스를 문자 abcd로 표현해줘. 
# index = list('a', 'b', 'c', 'd'와 같은 의미이다. )
```

```python
s[['d', 'a']] # => d 인덱스를 첫번째로, 그리고 두번째로 a 인덱스를 호출 할 때때
```

## 2.4. bool indexing
#### 내가 원하는 값만을 데이터에서 불러올때

## 2.5. 결측치 (NaN) 처리
```python
s = pd.Series([1, 3, np.nan, 10, 11, np.nan])
# =>   0  1.0
#      1  3.0
#      2  Nan
#      3 10.0
#      4  11.0
#      5  Nan
#      dtype: float 64
```
#### NaN을 제외하고 숫자만 보고싶다면?
#### 먼저 NaN이 목록에 포함 되어 있는지를 확인한다.
`s.isnull()`
`s.isnan()`

#### NaN이 몇번째 행에 들어있는지를 확인하고 싶을 떄
`s[s.isna()]`
#### 혹은 그 반대로 NaN이 없는 행을 알고 싶을 때
`s[s.notna()]`

## 2.6. slicing
## 2.7 DataFrame
- 2차원 데이터 구조 (excel, sheet와 유사)
- 행 (row) 과 열 (column)의 구조

##
##
# 3. 파일 불러오기
### > `pandas/ 02_file_load_save.ipynb` 에서 확인 가능.

# 4. MACHINE LEARNING (ml)
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