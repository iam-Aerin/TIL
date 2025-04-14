# TIL: CRUD 개념 정리

## CRUD란?
CRUD는 데이터의 기본적인 처리 기능을 나타내는 네 가지 연산(**Create, Read, Update, Delete**)의 약어입니다. 이는 대부분의 소프트웨어 시스템에서 데이터 관리를 위한 기본적인 개념으로 사용됩니다.

## CRUD의 주요 개념
> 객체 관계 매핑, 모델링, ORM

### 1. Create (생성)
- 새로운 데이터를 추가하는 작업을 의미합니다.
- **예시:** 회원 가입 시 사용자 정보를 데이터베이스에 저장
- **SQL 예제:**
  ```sql
  INSERT INTO users (name, email) VALUES ('홍길동', 'hong@example.com');
  ```

### 2. Read (조회)
- 기존 데이터를 조회하거나 검색하는 작업을 의미합니다.
- **예시:** 사용자 목록을 불러오는 기능
- **SQL 예제:**
  ```sql
  SELECT * FROM users WHERE id = 1;
  ```

### 3. Update (수정)
- 기존 데이터를 수정하는 작업을 의미합니다.
- **예시:** 회원 정보 변경
- **SQL 예제:**
  ```sql
  UPDATE users SET email = 'new@example.com' WHERE id = 1;
  ```

### 4. Delete (삭제)
- 데이터를 삭제하는 작업을 의미합니다.
- **예시:** 회원 탈퇴 시 사용자 정보 삭제
- **SQL 예제:**
  ```sql
  DELETE FROM users WHERE id = 1;
  ```

## CRUD와 REST API
CRUD 개념은 REST API 설계에서도 사용됩니다. HTTP 메서드와 CRUD 연산은 다음과 같이 매칭됩니다:

| CRUD 연산 | HTTP 메서드  | 설명           |
|-----------|-------------|----------------|
| Create    | `POST`      | 새로운 리소스 생성 |
| Read      | `GET`       | 리소스 조회       |
| Update    | `PUT` / `PATCH` | 기존 리소스 수정 |
| Delete    | `DELETE`    | 리소스 삭제       |

## ORM(Object-Relational Mapping)이란?
ORM(Object-Relational Mapping)은 객체 지향 프로그래밍 언어에서 관계형 데이터베이스를 보다 쉽게 다룰 수 있도록 해주는 기술입니다. 즉, 데이터베이스의 테이블을 프로그래밍 언어의 객체로 매핑하여 SQL을 직접 사용하지 않고도 데이터를 조작할 수 있도록 합니다.

### ORM의 주요 개념
- **객체와 데이터베이스 테이블을 1:1 매핑**
- **SQL을 직접 작성하지 않고 메서드를 통해 데이터 조작 가능**
- **데이터베이스에 독립적인 코드 작성 가능**

### CRUD와 ORM의 관계
ORM은 CRUD 연산을 더욱 쉽게 구현할 수 있도록 도와줍니다. 기존의 SQL을 직접 사용하는 방식과 비교했을 때, ORM을 사용하면 더 간결하고 유지보수하기 쉬운 코드 작성을 할 수 있습니다.

| CRUD 연산 | SQL 예제 | ORM 예제 (Python + SQLAlchemy) |
|-----------|-------------------------------------------------|----------------------------------|
| Create    | `INSERT INTO users (name, email) VALUES ('홍길동', 'hong@example.com');` | `user = User(name='홍길동', email='hong@example.com'); session.add(user); session.commit();` |
| Read      | `SELECT * FROM users WHERE id = 1;` | `user = session.query(User).filter_by(id=1).first()` |
| Update    | `UPDATE users SET email = 'new@example.com' WHERE id = 1;` | `user.email = 'new@example.com'; session.commit();` |
| Delete    | `DELETE FROM users WHERE id = 1;` | `session.delete(user); session.commit();` |

## CRUD와 ORM의 장점
- **코드의 가독성이 향상됨** (SQL을 직접 작성하지 않아도 됨)
- **데이터베이스의 변경에 유연하게 대처 가능** (다른 DBMS로 쉽게 변경 가능)
- **보안성 증가** (SQL Injection 방지 효과)

## CRUD의 중요성
- 소프트웨어 시스템에서 데이터를 효율적으로 관리할 수 있도록 함
- 데이터베이스 및 API 설계의 기초 개념
- 보안 및 성능 최적화를 고려한 CRUD 연산이 중요함 (예: 대량 삭제 방지, 적절한 인덱스 사용 등)
