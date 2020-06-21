from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
#from pyspark import Spar
#sc = SparkContext("local", "Simple App")
spark= SparkSession.builder.appName("local").master("local[*]").enableHiveSupport().getOrCreate()
print(spark)
sc= spark.sparkContext
testFile = sc.textFile("c:\\password.txt")
sc.setLogLevel("WARN")

print(sc.textFile("c:\\password.txt").first())
print(testFile.count())