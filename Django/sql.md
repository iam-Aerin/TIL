# SQL과 관계형 데이터베이스(RDBMS) 개념 정리

`PostgreSQL`, `Oracle`, `MySQL`, `Snowflake`,  / `Elasticsearch` &  `MongoDB` (문서형 데이터베이스)

---
MySQL 다운로드
https://dev.mysql.com/downloads/

> `MySQL Community Server`, 
`MySQL Workbench` (hwp / 한컴 과 같은 관계)    

![MySQL](/assets/1.png/)
---

## 1. 관계형 데이터베이스(RDBMS)란?

관계형 데이터베이스(Relational Database Management System, RDBMS)는 데이터를 테이블 형태로 구조화하여 저장하고 관리하는 시스템입니다. 이러한 테이블들은 서로 관계(relationship)를 맺을 수 있으며, 이를 통해 복잡한 데이터 구조를 효율적으로 표현할 수 있습니다.

### 핵심 특징
- **테이블 기반 구조**: 데이터는 행(row)과 열(column)로 구성된 테이블에 저장됩니다.
- **관계**: 테이블 간의 관계를 통해 데이터의 무결성과 일관성을 유지합니다.
- **정규화**: 데이터 중복을 최소화하고 일관성을 유지하기 위한 체계적인 방법입니다.
- **SQL 지원**: 표준화된 질의 언어인 SQL을 사용하여 데이터를 관리합니다.

### 주요 RDBMS 제품
- **SQLite**: 경량화된 파일 기반 데이터베이스로, 별도의 서버 프로세스 없이 애플리케이션에 내장될 수 있습니다.
- **MySQL**: 오픈소스 RDBMS로, 웹 애플리케이션에 널리 사용됩니다.
- **PostgreSQL**: 강력한 오픈소스 RDBMS로, 고급 기능과 확장성을 제공합니다.
- **Oracle Database**: 기업용 대규모 RDBMS로, 높은 성능과 보안을 제공합니다.


## 2. SQL(Structured Query Language) 기본 개념

SQL은 관계형 데이터베이스에서 데이터를 관리하기 위한 표준 언어입니다. 크게 다음과 같은 카테고리로 명령어가 분류됩니다.

### DDL(Data Definition Language, 데이터 정의어)
데이터베이스 객체(테이블, 인덱스 등)의 구조를 정의하는 명령어입니다.

- **CREATE**: 새로운 데이터베이스 객체를 생성합니다.
  ```sql
  CREATE TABLE 학생 (
      학번 INTEGER PRIMARY KEY,
      이름 TEXT NOT NULL,
      학과 TEXT,
      입학년도 INTEGER
  );
  ```

- **ALTER**: 기존 객체의 구조를 변경합니다.
  ```sql
  ALTER TABLE 학생 ADD COLUMN 이메일 TEXT;
  ```

- **DROP**: 객체를 삭제합니다.
  ```sql
  DROP TABLE 학생;
  ```

### DML(Data Manipulation Language, 데이터 조작어)
데이터베이스 내의 데이터를 조작하는 명령어입니다.

- **SELECT**: 데이터를 조회합니다.
  ```sql
  SELECT 이름, 학과 FROM 학생 WHERE 입학년도 >= 2020;
  ```

- **INSERT**: 새로운 데이터를 추가합니다.
  ```sql
  INSERT INTO 학생 (학번, 이름, 학과, 입학년도) 
  VALUES (20230001, '홍길동', '컴퓨터공학과', 2023);
  ```

- **UPDATE**: 기존 데이터를 수정합니다.
  ```sql
  UPDATE 학생 SET 학과 = '인공지능학과' WHERE 학번 = 20230001;
  ```

- **DELETE**: 데이터를 삭제합니다.
  ```sql
  DELETE FROM 학생 WHERE 입학년도 < 2010;
  ```

### DCL(Data Control Language, 데이터 제어어)
데이터베이스에 대한 접근 권한을 관리하는 명령어입니다.

- **GRANT**: 사용자에게 특정 권한을 부여합니다.
  ```sql
  GRANT SELECT, INSERT ON 학생 TO 사용자명;
  ```

- **REVOKE**: 사용자로부터 권한을 회수합니다.
  ```sql
  REVOKE INSERT ON 학생 FROM 사용자명;
  ```

### TCL(Transaction Control Language, 트랜잭션 제어어)
트랜잭션을 관리하는 명령어입니다.

- **COMMIT**: 트랜잭션의 변경사항을 확정합니다.
  ```sql
  COMMIT;
  ```

- **ROLLBACK**: 트랜잭션의 변경사항을 취소합니다.
  ```sql
  ROLLBACK;
  ```

- **SAVEPOINT**: 트랜잭션 내에 저장점을 설정합니다.
  ```sql
  SAVEPOINT 저장점이름;
  ```
## ON, WHERE, HAVING 절에 대한 설명
| 구분       | 사용 위치             | 주 대상             | 주 목적                           |
|------------|------------------------|----------------------|------------------------------------|
| `ON`       | `JOIN` 문 뒤           | 테이블 간 연결 조건    | 테이블 간 조인 기준 설정             |
| `WHERE`    | `FROM ~ WHERE` 사이    | 개별 행(row)         | 행 단위 필터링 (GROUP BY 이전)      |
| `HAVING`   | `GROUP BY ~ HAVING` 이후 | 그룹/집계 결과       | 집계 함수 결과 필터링 (GROUP BY 이후) |

---

## 3. SQL의 주요 기능과 문법

### SELECT 문과 데이터 조회
```sql
SELECT 컬럼1, 컬럼2, ... FROM 테이블명
WHERE 조건
GROUP BY 그룹화_기준
HAVING 그룹_조건
ORDER BY 정렬_기준 [ASC|DESC]
LIMIT 개수 OFFSET 시작위치;
```

#### 주요 절(Clause)
- **WHERE**: 조회할 데이터의 조건을 지정합니다.
  ```sql
  SELECT * FROM 학생 WHERE 학과 = '컴퓨터공학과' AND 입학년도 >= 2020;
  ```

- **GROUP BY**: 데이터를 그룹화합니다.
  ```sql
  SELECT 학과, COUNT(*) AS 학생수 FROM 학생 GROUP BY 학과;
  ```

- **HAVING**: 그룹화된 데이터에 조건을 적용합니다.
  ```sql
  SELECT 학과, COUNT(*) AS 학생수 FROM 학생 GROUP BY 학과 HAVING COUNT(*) > 10;
  ```

- **ORDER BY**: 결과를 정렬합니다.
  ```sql
  SELECT * FROM 학생 ORDER BY 입학년도 DESC, 이름 ASC;
  ```

- **LIMIT/OFFSET**: 결과의 일부만 반환합니다.
  ```sql
  SELECT * FROM 학생 ORDER BY 입학년도 DESC LIMIT 10 OFFSET 20;  -- 21~30번째 행 반환
  ```

### 조인(JOIN)
여러 테이블을 연결하여 데이터를 조회하는 방법입니다.

- **INNER JOIN**: 두 테이블에 모두 일치하는 데이터만 반환합니다.
  ```sql
  SELECT 학생.이름, 과목.과목명, 수강.점수
  FROM 학생
  INNER JOIN 수강 ON 학생.학번 = 수강.학번
  INNER JOIN 과목 ON 수강.과목코드 = 과목.과목코드;
  ```

- **LEFT JOIN**: 왼쪽 테이블의 모든 데이터와 오른쪽 테이블의 일치하는 데이터를 반환합니다.
  ```sql
  SELECT 학생.이름, 과목.과목명, 수강.점수
  FROM 학생
  LEFT JOIN 수강 ON 학생.학번 = 수강.학번
  LEFT JOIN 과목 ON 수강.과목코드 = 과목.과목코드;
  ```

- **RIGHT JOIN**: 오른쪽 테이블의 모든 데이터와 왼쪽 테이블의 일치하는 데이터를 반환합니다.
  ```sql
  SELECT 학생.이름, 과목.과목명, 수강.점수
  FROM 학생
  RIGHT JOIN 수강 ON 학생.학번 = 수강.학번
  RIGHT JOIN 과목 ON 수강.과목코드 = 과목.과목코드;
  ```

- **FULL JOIN**: 양쪽 테이블의 모든 데이터를 반환합니다.
  ```sql
  SELECT 학생.이름, 과목.과목명, 수강.점수
  FROM 학생
  FULL JOIN 수강 ON 학생.학번 = 수강.학번
  FULL JOIN 과목 ON 수강.과목코드 = 과목.과목코드;
  ```

### 서브쿼리(Subquery)
쿼리 내에 포함된 또 다른 쿼리입니다.

- **단일 행 서브쿼리**: 하나의 행을 반환하는 서브쿼리입니다.
  ```sql
  SELECT 이름, 학과
  FROM 학생
  WHERE 입학년도 = (SELECT MIN(입학년도) FROM 학생);
  ```

- **다중 행 서브쿼리**: 여러 행을 반환하는 서브쿼리입니다.
  ```sql
  SELECT 이름, 학과
  FROM 학생
  WHERE 학과 IN (SELECT 학과명 FROM 우수학과);
  ```

- **상관 서브쿼리**: 외부 쿼리의 값을 참조하는 서브쿼리입니다.
  ```sql
  SELECT 학과, 이름
  FROM 학생 s1
  WHERE 입학년도 = (
      SELECT MAX(입학년도)
      FROM 학생 s2
      WHERE s1.학과 = s2.학과
  );
  ```

## 4. SQLite 특징

SQLite는 가벼운 디스크 기반 데이터베이스로, 별도의 서버 프로세스 없이 애플리케이션에 내장될 수 있는 특징이 있습니다.

### 주요 특징
- **서버리스(Serverless)**: 별도의 서버 프로세스 없이 직접 데이터베이스 파일에 접근합니다.
- **자기완비성(Self-contained)**: 외부 종속성이 거의 없어 이식성이 뛰어납니다.
- **파일 기반**: 전체 데이터베이스가 단일 파일로 저장됩니다.
- **제로 설정(Zero-configuration)**: 설치나 설정이 필요 없습니다.
- **트랜잭션**: ACID 속성을 준수하는 트랜잭션을 지원합니다.

### 데이터 타입
SQLite는 동적 타입 시스템을 사용하며, 다음과 같은 기본 타입이 있습니다:
- **NULL**: 널 값
- **INTEGER**: 정수값
- **REAL**: 부동 소수점 값
- **TEXT**: 문자열
- **BLOB**: 바이너리 데이터

### 사용 예시
```sql
-- 데이터베이스 생성 및 연결
-- SQLite에서는 파일이 없으면 자동으로 생성됩니다.
-- 메모리 내 데이터베이스 사용
.open :memory:

-- 테이블 생성
CREATE TABLE 사용자 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    이름 TEXT NOT NULL,
    나이 INTEGER,
    이메일 TEXT UNIQUE
);

-- 데이터 삽입
INSERT INTO 사용자 (이름, 나이, 이메일) VALUES 
('김철수', 25, 'chulsoo@example.com'),
('이영희', 30, 'younghee@example.com');

-- 데이터 조회
SELECT * FROM 사용자;

-- 조건부 데이터 조회
SELECT 이름, 이메일 FROM 사용자 WHERE 나이 > 25;

-- 데이터 수정
UPDATE 사용자 SET 나이 = 26 WHERE 이름 = '김철수';

-- 데이터 삭제
DELETE FROM 사용자 WHERE 이름 = '이영희';
```

## 5. 고급 SQL 개념

### 인덱스(Index)
데이터 검색 속도를 향상시키는 데이터베이스 객체입니다.
```sql
CREATE INDEX idx_학생_학과 ON 학생(학과);
```

### 뷰(View)
저장된 쿼리의 결과를 테이블처럼 사용할 수 있는 가상 테이블입니다.
```sql
CREATE VIEW 컴공학생 AS
SELECT * FROM 학생 WHERE 학과 = '컴퓨터공학과';
```

### 트리거(Trigger)
특정 이벤트 발생 시 자동으로 실행되는 프로시저입니다.
```sql
CREATE TRIGGER 학생_로그
AFTER INSERT ON 학생
BEGIN
    INSERT INTO 로그 (메시지) VALUES ('새 학생이 추가됨: ' || NEW.이름);
END;
```

### 트랜잭션(Transaction)
데이터베이스의 상태를 변경하는 작업의 논리적 단위입니다.
```sql
BEGIN TRANSACTION;
    UPDATE 계좌 SET 잔액 = 잔액 - 1000 WHERE 계좌번호 = 'A001';
    UPDATE 계좌 SET 잔액 = 잔액 + 1000 WHERE 계좌번호 = 'B001';
    
    -- 조건에 따라 롤백 또는 커밋
    SELECT CASE WHEN (SELECT 잔액 FROM 계좌 WHERE 계좌번호 = 'A001') < 0
           THEN RAISE(ROLLBACK, '잔액 부족')
           ELSE 'OK'
           END;
COMMIT;
```

### 정규화(Normalization)
데이터 중복을 최소화하고 무결성을 유지하기 위한 테이블 설계 방법론입니다.

- **제1정규형(1NF)**: 각 열이 원자값(더 이상 분해할 수 없는 값)을 가져야 합니다.
- **제2정규형(2NF)**: 1NF를 만족하며, 부분 함수적 종속성이 없어야 합니다.
- **제3정규형(3NF)**: 2NF를 만족하며, 이행적 함수적 종속성이 없어야 합니다.
- **BCNF(Boyce-Codd 정규형)**: 3NF의 강화된 버전으로, 모든 결정자가 후보키여야 합니다.

## 6. 관계형 데이터베이스의 키(Key) 개념

### 기본 키(Primary Key)
테이블의 각 행을 고유하게 식별하는 열(또는 열의 조합)입니다.
```sql
CREATE TABLE 학생 (
    학번 INTEGER PRIMARY KEY,
    이름 TEXT NOT NULL
);
```

### 외래 키(Foreign Key)
다른 테이블의 기본 키를 참조하는 열로, 테이블 간의 관계를 정의합니다.
```sql
CREATE TABLE 수강 (
    id INTEGER PRIMARY KEY,
    학번 INTEGER,
    과목코드 TEXT,
    점수 REAL,
    FOREIGN KEY (학번) REFERENCES 학생(학번),
    FOREIGN KEY (과목코드) REFERENCES 과목(과목코드)
);
```

### 복합 키(Composite Key)
두 개 이상의 열로 구성된 키입니다.
```sql
CREATE TABLE 수강 (
    학번 INTEGER,
    과목코드 TEXT,
    학기 TEXT,
    점수 REAL,
    PRIMARY KEY (학번, 과목코드, 학기),
    FOREIGN KEY (학번) REFERENCES 학생(학번),
    FOREIGN KEY (과목코드) REFERENCES 과목(과목코드)
);
```

### 후보 키(Candidate Key)
테이블에서 각 행을 고유하게 식별할 수 있는 최소한의 열(또는 열의 조합)입니다. 기본 키는 후보 키 중 하나로 선택됩니다.

### 대체 키(Alternate Key)
기본 키로 선택되지 않은 후보 키입니다.

## 7. SQL 함수

### 집계 함수(Aggregate Functions)
여러 행의 데이터를 요약하는 함수입니다.
- **COUNT()**: 행의 개수를 반환합니다.
  ```sql
  SELECT COUNT(*) FROM 학생;
  ```
- **SUM()**: 값의 합계를 반환합니다.
  ```sql
  SELECT SUM(점수) FROM 수강 WHERE 과목코드 = 'CS101';
  ```
- **AVG()**: 값의 평균을 반환합니다.
  ```sql
  SELECT AVG(점수) FROM 수강 WHERE 학번 = 20230001;
  ```
- **MAX()**: 최댓값을 반환합니다.
  ```sql
  SELECT MAX(점수) FROM 수강;
  ```
- **MIN()**: 최솟값을 반환합니다.
  ```sql
  SELECT MIN(점수) FROM 수강;
  ```

### 문자열 함수
- **SUBSTR()**: 부분 문자열을 반환합니다.
  ```sql
  SELECT SUBSTR(이름, 1, 1) || '**' FROM 학생;  -- 첫 글자만 표시하고 나머지는 가림
  ```
- **UPPER()**: 대문자로 변환합니다.
  ```sql
  SELECT UPPER(이름) FROM 학생;
  ```
- **LOWER()**: 소문자로 변환합니다.
  ```sql
  SELECT LOWER(이메일) FROM 학생;
  ```
- **LENGTH()**: 문자열 길이를 반환합니다.
  ```sql
  SELECT 이름, LENGTH(이름) FROM 학생;
  ```

### 날짜/시간 함수
SQLite에서는 다음과 같은 날짜/시간 함수를 제공합니다.
- **DATE()**: 날짜 부분만 반환합니다.
  ```sql
  SELECT DATE('now');
  ```
- **TIME()**: 시간 부분만 반환합니다.
  ```sql
  SELECT TIME('now');
  ```
- **DATETIME()**: 날짜와 시간을 반환합니다.
  ```sql
  SELECT DATETIME('now');
  ```

### 조건부 함수
- **CASE**: 조건에 따라 다른 값을 반환합니다.
  ```sql
  SELECT 이름,
         CASE
             WHEN 점수 >= 90 THEN 'A'
             WHEN 점수 >= 80 THEN 'B'
             WHEN 점수 >= 70 THEN 'C'
             ELSE 'F'
         END AS 학점
  FROM 학생 JOIN 수강 ON 학생.학번 = 수강.학번;
  ```
- **COALESCE()**: 첫 번째 NULL이 아닌 값을 반환합니다.
  ```sql
  SELECT 이름, COALESCE(전화번호, 이메일, '연락처 없음') AS 연락처
  FROM 학생;
  ```
- **IFNULL()**: 첫 번째 인수가 NULL이면 두 번째 인수를 반환합니다.
  ```sql
  SELECT 이름, IFNULL(전화번호, '전화번호 없음') AS 전화번호
  FROM 학생;
  ```
---
✅ 실행 순서 요약 (개념 흐름)

```
FROM / JOIN → 테이블을 연결

ON → 조인 기준 조건 적용

WHERE → 개별 행(row) 필터링

GROUP BY → 그룹핑 수행

HAVING → 그룹 결과에 조건 필터링

SELECT → 원하는 컬럼 출력

ORDER BY → 정렬

LIMIT → 결과 수 제한
```
---
## 8. 데이터베이스 설계 원칙

### ACID 속성
트랜잭션이 안전하게 처리되기 위한 4가지 속성입니다.
- **원자성(Atomicity)**: 트랜잭션의 모든 연산이 완전히 수행되거나 전혀 수행되지 않아야 합니다.
- **일관성(Consistency)**: 트랜잭션 실행 전과 후에 데이터베이스는 일관된 상태를 유지해야 합니다.
- **격리성(Isolation)**: 동시에 실행되는 트랜잭션은 서로 영향을 미치지 않아야 합니다.
- **지속성(Durability)**: 성공적으로 완료된 트랜잭션의 결과는 영구적으로 보존되어야 합니다.

### 정규화 vs 비정규화
- **정규화**: 데이터 중복을 최소화하고 무결성을 유지하는 설계 방법입니다.
- **비정규화**: 성능 향상을 위해 의도적으로 중복 데이터를 허용하는 설계 방법입니다.

### 인덱스 설계 원칙
- 자주 검색되는 열에 인덱스를 생성하세요.
- 카디널리티(고유 값의 수)가 높은 열에 인덱스를 생성하세요.
- 복합 인덱스의 경우, 자주 사용되는 열을 앞에 배치하세요.
- 인덱스가 많을수록 삽입, 수정, 삭제 작업이 느려질 수 있음을 고려하세요.

### 데이터베이스 설계 원칙

데이터베이스 설계는 데이터베이스의 성능, 가용성, 안정성을 높이기 위해 고려해야 하는 여러 가지 요소를 포함합니다. 이를 위해 다음과 같은 5가지 원칙을 적용할 수 있습니다.

1. **데이터의 분리**: 데이터를 분리하여 각각의 테이블에 저장합니다. 이를 통해 데이터의 관리와 유지가 용이해집니다.
2. **데이터의 정의**: 데이터의 구조를 정의하여