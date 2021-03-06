import sys
import re
 
temp = ''
for line in sys.stdin:
    line = line.strip()
    temp = temp + re.sub(r'[^A-Za-z0-9 ]','',line) + ' '

words = temp.split()

for word in words: 
    print('%s\t%s' % (word, "1"))
