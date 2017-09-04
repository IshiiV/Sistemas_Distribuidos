import numpy
import threading
import time


lock = threading.Lock()

m = 4	#quantidade de linhas na primeira matriz
k = 4	#quantidade de colunas na primeira matriz e quantidade de linhas na segunda
n = 4	#quantidade de colunas na segunda matriz
result = 0
m1 = numpy.array([[2,3,1,-3], [0,1,2,2],[-1,4,4,6],[2,2,14,-8]])
m2 = numpy.array([[1,2,3,5], [13,-2,0,4],[2,-23,5,-9],[-11,0,1,-2]])
r = numpy.zeros((m,n))

def elemento(x,y):
	global result
	global r
	for a in range(k):
		result = result + m1[x][a]*m2[a][y]
	r[x][y] = result
	result = 0
	print(threading.current_thread().name)

for x in range(m):
	for y in range(n):
		t = threading.Thread(target = elemento, args=(x,y))
		t.start()



print (m1)
print (m2)
print (r)