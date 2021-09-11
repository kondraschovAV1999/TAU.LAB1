inFile = open('input.txt')
wordDict = {}
for line in inFile:
    words = line.split()
    for word in words:
        wordDict[word] = wordDict.get(word, 0) - 1
# for i in wordDict.items():
#     print(i[::-1])
answer = sorted([i[::-1] for i in wordDict.items()])
for i in answer:
    print(i[1])
