from pyspark import SparkContext

sc = SparkContext("local", "Euler")

sumnumber = sc.parallelize(range(0,1000)).filter(lambda x: x % 3 == 0 or x % 5 ==0).reduce(lambda x,y: x + y)
print(sumnumber)