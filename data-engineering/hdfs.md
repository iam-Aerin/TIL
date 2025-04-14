## 작업	명령어

- hdfs 실행
> `sbin/start-all.sh`

- hiveserver2 실행
> `hiveserver2 --hiveconf hive.server2.thrift.port=10000 --hiveconf hive.root.logger=DEBUG,console`
---
- 파일 업로드	
>`hdfs dfs -put <로컬경로> <HDFS경로>`

- 파일 다운로드	
> `hdfs dfs -get <HDFS경로> <로컬경로>`

- 파일 목록 보기	
> `hdfs dfs -ls /경로`

- 파일 삭제	
> `hdfs dfs -rm /경로/파일`

- 폴더 삭제	
> `hdfs dfs -rm -r /경로`

- 폴더 생성	
> `hdfs dfs -mkdir /경로`

---
hdfs -> dbeaver랑 연결
> dbeaver를 통해 sql문을 위한 테이블을 생성하는데, 그 때 `create table` 안에 `location`을 지정해주면 된다. (hadoop에 연결)

`e.g.`
```sql
CREATE EXTERNAL TABLE books (
  ISBN STRING,
  Book_Title STRING,
  Book_Author STRING,
  Year_Of_Publication INT,
  Publisher STRING,
  Image_URL_S STRING,
  Image_URL_M STRING,
  Image_URL_L STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
  "separatorChar" = ";",
  "quoteChar"     = "\""
)
STORED AS TEXTFILE
LOCATION '/input/book/books';

```

> LOCATION '/input/book/books';