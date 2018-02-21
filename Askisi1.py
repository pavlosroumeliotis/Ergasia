from __future__ import division
import random

def getNumbers(a):
	arithmoi = []
	for i in range(100):
		arithmoi.append(random.sample(a,5))
	return arithmoi
def callNumbers(epilogi,a):
	k = [0]*80
	exit = True
	bingo = 0
	while exit:
		bingo = bingo+1
		x = random.sample(a,1)
		a.remove(x[0])
		for i in range(0,80):
			if x[0] in epilogi[i]:
				k[i] += 1
				if k[i] == 5:
					exit=False
	return bingo

bingos = 0
for i in range(1000):
	a=range(1,81)
	paiktes = getNumbers(a)
	bingos += callNumbers(paiktes,a)
print (bingos/1000)
