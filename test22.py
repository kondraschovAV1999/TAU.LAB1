def changeS(lst):
    for i in lst:
        i[-1] = int(i[-1])
        i[-2] = int(i[-2])
        i[-3] = int(i[-3])


def score(a):
    listScore = []
    for i in a:
        if i[-1] < 40 or i[-2] < 40 or i[-3] < 40:
            continue
        listScore.append(i[-1] + i[-2] + i[-3])
    return listScore


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = list()
k = int(inFile.readline())
for line in inFile:
    students.append(list(line.split()))
changeS(students)
scoreStudents = sorted(score(students), reverse=True)
j = 0
n = 0
theSame = scoreStudents[0]
if k >= len(scoreStudents):
    print(0, file=outFile)
else:
    while j <= k:
        if scoreStudents[j] == theSame:
            n += 1
        else:
            n = 0
            theSame = scoreStudents[j]
        j += 1
    if n + 1 > k:
        print(1, file=outFile)
    else:
        print(scoreStudents[k - n - 1], file=outFile)
