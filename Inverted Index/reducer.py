import sys
 
invertedIndex = {}
 
for line in sys.stdin:
    line = line.strip()
 
    word, file = line.split('\t', 1)

    try:
        if file not in invertedIndex[word]:
            invertedIndex[word].append(file)
    except:
        invertedIndex[word] = [file]
 
for word in invertedIndex.keys():
    print('%s:\t%s'% ( word, ', '.join(invertedIndex[word])))