## Airflow

> 자동화된 작업을 위한 오픈소스 관리자 프로그램

- Airflow는 DAG(Directed Acyclic Graph)을 이용해 작업을 관리한다.
- DAG는 작업의 순서를 정의

---
### Airflow의 구성요소

- `DAG` : 작업의 순서를 정의
- `Task` : 작업을 수행하는 단위
- `Operator` : 작업을 수행하는 클래스
- `Sensors` : 작업이 끝나는 것을 감지하는 클래스
- `Trigger` : DAG를 시작하는 클래스
- `Task Instance` : DAG에서 수행되는 작업
- `Log` : 작업의 실행 결과를 로그로 남김
- `Sla` : 작업이 끝나는 시간을 제한하는 클래스

---
### DAG

: 작업의 순서를 정의

: 시각적으로 보기 좋게 만들어주고

: 각각의 흐름을 보기 좋게 
- 특정 시간마다 workflow를 관리하는 process

`DAG` : 유향 `비순환` 그래프 -> 방향성은 있지만, 순환은 되지 않는 작업들
=> 시작이 있다면 끝이 있는 작업

---
- task
- graph


