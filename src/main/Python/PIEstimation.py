import random
from pyspark import SparkConf, SparkContext
sc = SparkContext("local", "Simple App")
def inside(p):
    x,y = random.random(), random.random()
    return x*x + y*y < 1
count = sc.parallelize(xrange(0,1)) \
    .filter(inside).count()
print("pi is roughly % f" %(4.0 * count / 1))
