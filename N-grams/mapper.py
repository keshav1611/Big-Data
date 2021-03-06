import sys
import re
 
temp = ''
keywords = ['science','sea','fire']
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    temp = temp + re.sub(r'[^A-Za-z0-9 ]','',line) + ' '

words = temp.split()

for i, word in enumerate(words):
	if word in keywords:
		if i == 0:
			print('$_%s_%s\t%s' % (words[i+1],words[i+2], "1"))
		elif i == 1:
			print('%s_$_%s\t%s' % (words[i-1],words[i+1], "1"))
			print('$_%s_%s\t%s' % (words[i+1],words[i+2], "1"))
		elif i == len(words)-1:
			print('%s_%s_$\t%s' % (words[i-2],words[i-1], "1"))
		elif i == len(words)-2:
			print('%s_%s_$\t%s' % (words[i-2],words[i-1], "1"))
			print('%s_$_%s\t%s' % (words[i-1],words[i+1], "1"))
		else:
			print('%s_%s_$\t%s' % (words[i-2],words[i-1], "1"))
			print('%s_$_%s\t%s' % (words[i-1],words[i+1], "1"))
			print('$_%s_%s\t%s' % (words[i+1],words[i+2], "1"))
