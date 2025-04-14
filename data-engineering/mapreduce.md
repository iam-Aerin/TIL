### AWS EMR
# Map Reduce

## `EC2`, `RDS` 를 많이 사용하게 될 것임. 

클러스터 생성하기: 4개의 컴퓨터 (인스턴스)를 묶어서 하나의 단위집단으로 구성하는 것

EMR: https://ap-northeast-2.console.aws.amazon.com/emr/home?region=ap-northeast-2#/clusters


## Map Reduce 맵리듀스
병열로 실행할 수 있는 프로그램
- map: 데이터를 분석하는 작업
- reduce: 결과를 합치는 작업

## Map Reduce
- MapReduce
- Hadoop
- Spark
- Flink

대규모 데이터 처리를 할 수 있게 만들어진 프로그램

![map reduce](https://www.todaysoftmag.com/images/articles/tsm33/large/a11.png)
> shuffling: sorting - 정렬
>
> reduce: 특정한 연산 => aggregation - 합계

> **모든 데이터의 분산 처리를 하는 것이 핵심** (`파이썬`과 다르게): 변수에 저장하는 식은 램을 너무 많이 차지하는 불필요한/ 효율적이지 못함 (하지만, 데이터의 양이 작다면, 파이썬이 훨씬 효율적일 수는 있음)
