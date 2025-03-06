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
