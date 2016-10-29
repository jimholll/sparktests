from pyspark import SparkContext
from random import random
from Math import sqrt

radius = 1
squarearea = 4
rangelimit = 10000

sc = SparkContext("local", "pi")

def randomize():
	x, y = random.uniform(0,1), random.uniform(0,1)
	if Math.sqrt(x**2 + y**2) <= 1:
		return 1
	return 0

percentarea = sc.parallelize(range(0,rangelimit)).map(randomize).reduce(lambda x,y: x+y)

print(percentarea * squarearea)/rangelimit
