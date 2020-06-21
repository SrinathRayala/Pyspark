from pyspark import SparkConf, SparkContext
sc = SparkContext("local", "Simple App")
test_file=sc.textFile("c:\\password.txt")
mylist = "abc 123 758 2344354 rt45 cde"
#df = test_file.map(lambda r: Row(r)).toDF["password"])
#errors=df.filter(col("password")).like("%"))
#errors.count(

#counts= test_file.flatMap(lambda line: line.split(" ")) \
  #  .map(lambda x: x.isdigit()) \
 #   .reduceByKey(lambda a,b: a + b)
#counts.saveAsTextFile("c:\\TestCount.txt")
#m = mylist.split(' ')
m = test_file.flatMap(lambda line: line.split(" "))
#m1= map(lambda x: x.isdigit(),m)
#m2= reduce(lambda x, y: x+y, m1)
print(m[0])
#print reduce(lambda x, y: x+y, map(lambda x: x.isdigit(),mylist.split(' ')))