`spark.md`
---
## spark, zeppelin 관련
---
`spark` 에서 `pyspark` 를 실행하기 위해서는 `spark-shell` 을 실행해야 한다.
![spark-shell](/assets/spark2.png)

![pyspark](/assets/spark1.png) 
> global python (3.11.12)버전으로 낮춰서 `pyspark` 를 실행 

![zeppelin/ localhost:8080](/assets/zeppelin.png)

https://www.mockaroo.com/
### 목업 가상의 데이터 만들기

![alt text](/assets/mockaroo.png)

---
`zeppelin` 에서 `python` 을 실행하면 `pyspark` 가 실행된다.
---
```
%pyspark
# Sc = SparkContext()

# 로컬 파일 읽기 (vscode 내에 data 폴더에 txt 파일 생성해서 그걸 가져오는 경우)
# file_path = 'file:///home/ubuntu/damf2/data/word.txt'
# lines = sc.textFile(file_path)
# print(lines.collect())

# HDFS에서 파일 읽기
file_path = 'hdfs://localhost:9000/input/word.txt'
lines = sc.textFile(file_path)
# print(lines.collect())

# 띄어쓰기 기준으로 단어들 쪼개주기 -> 단어 숫자 세기 (하나의 데이터로 평탄화 시킨다.)

words = lines.flatMap(lambda line: line.split()) #lambda 함수는 일회용 함수 (def가 아닌, 딱 이 안에서만 사용하는 규칙을 만들때)
# print(words.collect())

mapped_words = words.map(lambda word: (word, 1))
# print(mapped_words.collect())

reduced_words = mapped_words.reduceByKey(lambda a, b: a+b) # 같은 키(단어)인 친구들의 숫자를 합산
print(reduced_words.collect())
```
![0.RDD - Zeppelin](/assets/zeppelin2.png)

```
%pyspark
file_path = 'file:///home/ubuntu/damf2/data/logs/2024-01-01.log'
lines = sc.textFile(file_path)

# print(lines.collect())

# 한줄씩 쪼개기
mapped_lines = lines.map(lambda line: line.split())
# print(mapped_lines.collect())

# status 가  4로 시작하는 친구들만 filtering: line[5][0]
def filter_4xx(line):
    return line[5][0] == '4'
filtered_lines = mapped_lines.filter(filter_4xx) # true 혹은 false로 filtering 
# print(filtered_lines.collect())

#Reduce
# 총 몇번의 POST / GET 이 나타났는지
# method ('GET', 'POST') 별 요청수 계산
method_rdd = mapped_lines.map(lambda line: (line[2], 1)).reduceByKey(lambda a, b: a+b)
print(method_rdd.collect())

# 시간대별 요청수 찾기
# 내가 필요한 데이터의 위치 (시간): 1번째 [0] 에 ::: 사이중 22,23 등 이라는 시간이라는 첫번째 : 뒤의 숫자를 split
time_rdd = mapped_lines.map(lambda line: (line[1].split(':')[1],1)).reduceByKey(lambda a, b: a+b)
# print(time_rdd.collect())

# status_code, api method 별 count
count_rdd = mapped_lines.map(lambda line: ((line[5], line[2]), 1)).reduceByKey(lambda a, b: a+b)
print(count_rdd.collect())

```

![0.RDD - Zeppelin(1)](/assets/zeppelin3.png)

