## Hbase
> `NoSQL`
>
> Apache HBase is a distributed, scalable, NoSQL database that is part of the Apache Hadoop project. It's modeled after Google's Bigtable and designed to handle large amounts of data with fast, random access. HBase runs on top of the Hadoop Distributed File System (HDFS) or other distributed storage systems and is well-suited for big data applications requiring real-time access to data. 

![alt text](/assets/hbase.png)

컬럼 기반으로 데이터가 어떻게 저장되는지를 확인

> 하둡 (Hadoop) 이 실행되어야 실행됨

- ~ 위치에서 
hadoop 실행
```
hadoop-3.3.6 hbin/start-all.sh [뭔지 모름...]
```

hbase 실행

```
hbase-2.5.11/bin/start-hbase.sh
```

- hbase command
```
source ~/.bashrc
```
> hbase
> shell 실행
```bash
hbase shell
```

- 테이블 생성 -> 데이터 crud 실행
`NoSQL`

> 테이블 생성
```bash
create table 'students', 'info'
```
: info 라는 column family 생성

---
> Create
```
put 'students', '1', 'info:name', 'hong'
```
```
put 'students', '1', 'info:age', '20'
# 새로운 컬럼과 정보를 등록
```



---
> Read (테이블 조회)
```bash
get 'students', '1'
```
```bash
get 'students', '2'
```
- READ ALL (전체 데이터 조회)
```bash
scan 'students'
```
---
> Update (데이터 수정)
```bash
put 'students', '1', 'info:name', 'park'
```
```bash
put 'students', '1', 'info:age', '30'
```

---
> 테이블 삭제 

- 하나의 컬럼을 삭제
```bash
delete 'students', '2', 'info:address'
```

- 전체 데이터 삭제
```bash
deleteall 'students', '1'
```
- 전체 테이블 삭제
    - 비활성화 먼저 후, drop
```bash
disable 'students'
drop 'students'
```

---
- 채팅 서비스 모델링

`messages', `chatroom` 이라는 두개의 테이블 생성 후 각각 필요한 column 생성

```bash
create 'messages', 'info'
create 'chatroom', 'info'
```
```bash
 room1_144000                                column=info:text, timestamp=2025-04-14T14:40:01.879, value=python version?
 room1_144100                                column=info:text, timestamp=2025-04-14T14:41:05.050, value=3.13.2 :)
 room1_144103                                column=info:text, timestamp=2025-04-14T14:43:50.953, value=me too
 room2_144100                                column=info:text, timestamp=2025-04-14T14:41:50.406, value=tesla bad
 room2_144200                                column=info:text, timestamp=2025-04-14T14:42:07.474, value=:(
 room2_144203                                column=info:text, timestamp=2025-04-14T14:44:02.873, value=me too
 ```

 ### ID별로 (room1, room2)를 구분하여 데이터가 묶이게됨 => Hbase의 장점
 ```
전체를 그룹핑하기에 편하다. (순서대로 쌓이는게 아니라, id별로 묶이기 때문에)
 ```

 - 데이터 조회
 
 ```bash
 scan 'messages', { LIMIT => 2 }
```
: 2개만 조회 ({LIMIT})

```bash
scan 'messages', { COLUMNS => ['info:text'] }
```
: 특정 COLUMN만 조회

```bash
scan 'messages', {STARTROW => 'room1', STOPROW => 'room2'}
```
: 시작점과 끝점을 지정해서 조회

```bash
scan 'messages', { FILTER => "PrefixFilter('room')" }
```
: 특정한 접두어를 가진 경우만 조회