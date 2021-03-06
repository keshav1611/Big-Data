import sys
import re
import os

for line in sys.stdin:
    line = line.strip()
    temp = re.sub(r'[^A-Za-z0-9 ]','',line)
    words = temp.split()
    path = os.environ["map_input_file"]
    file = re.findall(r'\w+',path)[-2]

    for word in words:
    	print("%s\t%s.txt"% (word, file))
