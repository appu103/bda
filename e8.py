# Experiment No. 8 - K-Means Clustering using MapReduce

from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("K-Means Clustering - Experiment 8")
    .getOrCreate()
)

data = [
    (1, 1),
    (1, 2),
    (2, 1),
    (8, 8),
    (9, 8),
    (8, 9),
]

df = spark.createDataFrame(data, ["x", "y"])

assembler = VectorAssembler(
    inputCols=["x", "y"],
    outputCol="features",
)
dataset = assembler.transform(df)

kmeans = KMeans(k=2, seed=1)
model = kmeans.fit(dataset)
predictions = model.transform(dataset)

print("K-Means Clustering Result:")
predictions.select("x", "y", "prediction").show()

print("Cluster Centers:")
for center in model.clusterCenters():
    print(center)

spark.stop()
