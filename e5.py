# Experiment No. 5 - Word Count using MapReduce

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("BDA Lab - Experiment 5 Word Count")
    .getOrCreate()
)

text = [
    "big data analytics",
    "big data is useful",
    "data analytics is important",
]

rdd = spark.sparkContext.parallelize(text)

word_counts = (
    rdd.flatMap(lambda line: line.split())
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

print("Word Count:")
for word, count in sorted(word_counts.collect()):
    print(word, count)

spark.stop()
