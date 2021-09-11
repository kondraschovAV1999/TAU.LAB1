def sum_votes(dict1):
    sumVotes = 0
    for i in dict1.values():
        sumVotes += i
    return sumVotes


inFile = open('input.txt', 'r', encoding='utf8')
voteDict = {}
for line in inFile:
    words = line.strip()
    voteDict[words] = voteDict.get(words, 0) + 1
outFile = open('output.txt', 'w', encoding='utf8')
sumVotes = sum_votes(voteDict)
answer = sorted(voteDict.items(), key=lambda x: x[1], reverse=True)
if answer[0][1] > 0.5 * sumVotes:
    print(answer[0][0], file=outFile)
else:
    print(answer[0][0], answer[1][0], sep='\n', file=outFile)
