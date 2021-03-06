import sys
import re
import numpy as np
 
test = np.genfromtxt('Test.csv', delimiter=',') 
test = np.delete(test,0,axis=0)
#normalizing the data using test set
xmin = test.min(axis=0)
xmax = test.max(axis=0)
test = (test-xmin)/(xmax-xmin)
count = 0
for line in sys.stdin:
	if(count==0):
		count +=1
		continue
	temp = re.sub(r'[^A-Za-z0-9,]','',line)
	train = temp.split(',')
	train1 = [float(x) for x in train]
	line1 = np.array(train1)
	line1 = np.append(((line1[:-1]-xmin)/(xmax-xmin)),line1[-1])    #normalize the train set
	distance = 0.0
	for r, test_line in enumerate(test):
		distance = np.sqrt((test_line - line1[:-1])**2).sum()
		line1 = np.append(line1, distance)
		print(str(r)+"\t"+str(line1[-2:]))
		line1 = line1[:-1]
