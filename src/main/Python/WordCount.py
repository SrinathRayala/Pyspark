import pyspark
from pyspark import SparkConf, SparkContext
sc = SparkContext("local", "Simple App")
test_file=sc.textFile("c:\\password.txt")
counts= test_file.flatMap(lambda line: line.split(" ")) \
    .map(lambda word:(word,1)) \
    .reduceByKey(lambda a,b: a + b)
counts.saveAsTextFile("c:\\WordCount.txt")

