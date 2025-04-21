## Regression
- zeppelin `3.regression`
> zeppelin에서 ml 모듈을 사용하여 regression을 수행할 수 있다.

- `fish.csv` 파일을 이용해서 선형 회귀 (regression) 모델을 생성하고 예측한다.

```spark-shell
file_path = 'hdfs://localhost:9000/input/fish.csv'
# file_path = 'file:///home/ubuntu/damf2/data/fish.csv'
```
> csv 파일 위치 알려주는 코드는 위와 같이 `file_path`를 지정해서 알려줌. 

```spark-shell
%pyspark
from pyspark.ml.feature import StringIndexer
indexer = StringIndexer(inputCols=['Species'], outputCols=['species_idx'])
df = indexer.fit(df).transform(df)
```
![fish_regression](/assets/fish_regression.png)

---

## Classification
- zeppelin `4.classification`

```python
file_path = 'hdfs://localhost:9000/input/fish.csv'
df = spark.read.csv(file_path, header=True, inferSchema=True)

# ============

from pyspark.sql.functions import col
df = df.filter(col('Species').isin('Bream', 'Smelt'))

# ============

from pyspark.sql.functions import when
from pyspark.sql.functions import col
df = df.withColumn(
    'species_idx',
    when(col('Species') == 'Bream', 1)
    .otherwise(0)
)

# ============

from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=[
        'Weight',
        'Length1',
        'Length2',
        'Length3',
        'Height',
        'Width'
    ],
    outputCol='features'
)
df = assembler.transform(df)

# ============

train_data, test_data = df.randomSplit([0.8, 0.2])

# ============

from pyspark.ml.classification import LogisticRegression

lr = LogisticRegression(featuresCol='features', labelCol='species_idx')
lr_model = lr.fit(train_data)

# ============

prediction = lr_model.transform(test_data)

# ============

from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(labelCol='species_idx', rawPredictionCol='rawPrediction', metricName='areaUnderROC')
result = evaluator.evaluate(prediction)
print(result)

# ============

from pyspark.ml.classification import RandomForestClassifier

rf = RandomForestClassifier(featuresCol='features', labelCol='species_idx', maxBins=500)
rf_model = rf.fit(train_data)

# ============

prediction = rf_model.transform(test_data)
prediction.show()

```