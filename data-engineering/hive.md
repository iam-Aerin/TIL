
# Apache Hive & HiveQL 기초 개념 정리 정리 
## 하이브 (Hive)

SQL 문법으로 (Java 없이) 대량의 데이터를 관리하는 방법
> 파일에 접근해서 데이터의 규칙을 불러오자
>
>HiveQL: SQL 문법 같이 보이지만, 100% SQL 문법은 아님

![hive architecture](https://i.stack.imgur.com/17mZy.png)

---

## Hive?

Apache Hive는 대용량 데이터 배치 및 분석을 위한 데이터 웨어하우스 인프라입니다. 주로 Hadoop 기반의 분산 저장 시스템(HDFS)과 연계되어 동작합니다.

- SQL 같은 문법(HiveQL)을 제공해 대규모 데이터를 연산 없이 분석할 수 있게 해줍니다.
- 발신, 분석, ETL 작업 등 배치성 작업에 포인트가 됩니다.


### 주요 특징

| 특징 | 설명 |
|--------|------|
| SQL 기반 조회 지원 | HiveQL 사용 |
| 배치 처리 | 대우량 데이터에 적적 |
| 스키마 온 리드 | 데이터 읽을 때 적용 |
| Hadoop 과 통합 | HDFS에 저장된 데이터에 지원 |
| 다양한 저장 포래트 | ORC, Parquet, Text, Avro 등 |

## HiveQL?

HiveQL(HQL)은 Hive에서 사용하는 SQL 유사 언어입니다. 전투적인 RDBMS의 SQL과 유사하지만 몇 가지 차이점이 있습니다.

### 기본 문법

#### 1. 테이블 생성

```sql
CREATE TABLE students (
  id INT,
  name STRING,
  score FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

#### 2. 데이터 로드

```sql
LOAD DATA INPATH '/user/hadoop/students.csv' INTO TABLE students;
```

#### 3. 기본 SELECT 구문

```sql
SELECT name, score
FROM students
WHERE score > 90;
```

#### 4. 집계 구문

```sql
SELECT AVG(score) AS avg_score
FROM students;
```

## Hive 아키텍쳐

```
사용자 → HiveQL → Hive Compiler → Execution Engine → Hadoop (MapReduce / Tez / Spark)
```

- Hive는 조회를 MapReduce 작업으로 변환해 지시하고 수행
- 모든 Hive의 규칙은 메타스토어(Metastore)에 저장
- MapReduce 밖에도 Tez, Spark을 시스템으로 이용가능

### Metastore 설명

Metastore는 Hive의 메타데이터를 관리하는 것으로, Hive의 테이블, 파티션, 파이널 저장 위치, 저장 포래트, 자바 패시트 값 등 모든 구조적 정보를 저장하는 **중앙 저장소**입니다.

- 일반적으로 RDBMS(MySQL, PostgreSQL 등)에 저장됨
- HiveQL 쿼리 수행 시, 컴파일러는 Metastore에 접근하여 테이블 스키마와 위치 등 정보를 참조함
- 다양한 Hive 컴포넌트들이 메타스토어를 공유할 수 있어 확장성과 일관성 확보 가능

## Hive vs RDBMS

| 항목 | Hive | RDBMS |
|------|------|--------|
| 목적 | 대부분 분석적 작업 | 특정 통신 프로세스 |
| 문법 | HiveQL (SQL 유사) | SQL |
| 처리 방식 | 배치 | 실시간 |
| 인덱스 | 제한적 또는 무 | 지원 |
| 스키마 | 읽을 때 적용 | 저장 전 적용 |

## Hive 구조요소

| 구조요소 | 설명 |
|--------------|------|
| Metastore | 테이블, 파티션, 위치 등 메타데이터 관리 |
| Driver | HiveQL 문법 번역, 시험계획 생성 |
| Compiler | HiveQL을 MapReduce/또는 Spark 시험계획으로 변환 |
| Execution Engine | MapReduce / Tez / Spark |
| CLI / Beeline | Hive에 조회 입력을 내리는 인터페이스 |

## Hive 실문에서 자주 사용하는 기능

- 파티션 (Partitioning): 특정 컬럼 값을 기준으로 데이터 그룹\uud574 구성
- 버트팅 (Bucketing): 해시 함수를 이용해 데이터 분산
- UDF (User Defined Function): 사용자 정의 함수 사용
- 조인, 서브조의, 윈도우 함수 등 지원

## 정리

- Hive는 Hadoop에서 SQL같은 문법으로 데이터를 배치 및 분석할 수 있게 해줌.
- HiveQL 문법을 통해 MapReduce 또는 다른 시스템에서 데이터의 분석을 가능이하게 해줌.


