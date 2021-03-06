import sys
import numpy as np
from operator import itemgetter
from collections import Counter
k=5
distance = {}
testset = np.genfromtxt('Test.csv', delimiter=',') 
testset = np.delete(testset,0,axis=0)
for line in sys.stdin:
	line = line.strip()
	line1 = line.split('\t')
	#print(len(line1))
	test_line,train_line = line1[0],line1[1]
	try:
		distance[(test_line)].append(train_line)
	except:
		distance[(test_line)] = [train_line]
for test in distance:
	temp = sorted(distance[test],key = itemgetter(-1))	
	potential_out = [x for x in temp[:k]]
	#print(test,'\t',potential_out,'\n')
	potential_out1 = Counter(x[1] for x in potential_out)
	print(testset[int(test)],' Prediction\t',potential_out1.most_common()[0][0],'\n')
