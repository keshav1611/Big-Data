import sys
 
word2count = {}
 
for line in sys.stdin:
    line = line.strip()
 
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count

sortedCount = dict(sorted(word2count.items(), key=lambda item: item[1], reverse=True))
 
for word in list(sortedCount)[:10]:
    print('%s\t%s'% ( word, sortedCount[word] ))
