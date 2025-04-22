## SQL, pyspark 코드 (같은 문제를 다른 코드로 작성하기기)
### airline dataset으로 zeppelin에서 sql/ pyspark 코드 작성하기

- https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7

- 요일별 출발 / 도착 지연 평균

```sql
%sql
SELECT DayOfWeek, AVG(DepDelay), AVG(ArrDelay)
FROM airline
GROUP BY DayOfWeek;

```
```spark
%pyspark
df.groupBy('DayOfWeek') \
    .agg(
        avg('DepDelay'),
        avg('ArrDelay')
    ).show()
```

- 항공사별, 월별 지연 및 운항 건수

```sql
%sql
SELECT UniqueCarrier, Month, COUNT(*), AVG(depDelay)
FROM airline
GROUP BY UniqueCarrier, Month
```

```spark
%pyspark
df.groupBy('UniqueCarrier', 'Month') \
    .agg(
        count('*'),
        avg('depDelay')
    ).show()

```

- 항공사별 취소율

```sql
%sql
SELECT
    *,
    (flight_cancelled_count / total_count * 100) AS cancel_rate
FROM
(SELECT
    UniqueCarrier,
    SUM(Cancelled) AS flight_cancelled_count,
    SUM(CASE WHEN Cancelled == 0 THEN 1 ELSE 0 END),
    COUNT(*) AS total_count
FROM airline
GROUP BY UniqueCarrier)
```

```spark
%pyspark
df.groupBy('UniqueCarrier')\
    .agg(
        sum('Cancelled').alias('flight_cancelled_count'),
        sum(when(df.Cancelled == 0, 1).otherwise(0)),
        count('*').alias('total_count'),
    ).withColumn('cancel_rate', col('flight_cancelled_count') / col('total_count')*100).show()
```

- 가장 붐비는 공항

```sql
%sql
SELECT *, origin_count + dest_count AS total
FROM
(
(SELECT Origin, COUNT(*) AS origin_count
FROM airline
GROUP BY Origin) AS origin_airline

JOIN

(SELECT Dest, COUNT(*) AS dest_count
FROM airline
GROUP BY Dest) AS dest_airline

ON origin_airline.Origin == dest_airline.Dest
)
ORDER BY total DESC LIMIT 10;
```

```spark
%pyspark

origin_df = df.groupBy('Origin').count()

dest_df = df.groupBy('Dest').count()

origin_df.join(dest_df, origin_df.Origin == dest_df.Dest).withColumn('total', origin_df['count'] + dest_df['count']).orderBy(desc('total')).show()

```

- 실제 비행시간 / 예상 비행시간 차이가 큰 비행노선

```sql
%sql
-- SELECT
--     Month,
--     DayofMonth,
--     ABS(ActualElapsedTime - CRSElapsedTime) AS diff
-- FROM airline
-- ORDER BY diff DESC

SELECT
    *, ABS(real_time - crs_time) AS diff_time
FROM
(SELECT 
    Origin, 
    Dest, 
    AVG(ActualElapsedTime) AS real_time, 
    AVG(CRSElapsedTime) AS crs_time
FROM airline
GROUP BY Origin, Dest)
ORDER BY diff_time DESC


```

```spark
%pyspark
df.groupBy('Origin', 'Dest') \
    .agg(
        avg('ActualElapsedTime').alias('real_time'),
        avg('CRSElapsedTime').alias('crs_time')
    ).withColumn('diff_time', abs(col('real_time')-col('crs_time'))) \
    .orderBy(desc('diff_time')).show()
    
```