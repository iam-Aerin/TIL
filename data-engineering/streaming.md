## Streaming
-zeppelin `6.streaming`

: 서비스 레벨에서는 이를 단독으로 사용하지는 않음. (kafka 를 함께 ...)

![spark_streaming](/assets/spark_streaming.png)

```python
%pyspark
from pyspark.sql.functions import current_timestamp

lines = spark.readStream.format('socket').option('host', 'localhost').option('port', '9999').load()

lines_with_time = lines.select(lines.value, current_timestamp())

query = lines_with_time.writeStream\
        .outputMode('append')\
        .format('csv')\
        .option('path', 'hdfs://localhost:9000/output/stream-test')\
        .option('checkPointLocation', 'hdfs://localhost:9000/output/stream-temp')\
        .start()
        
query.awaitTermination()
```
