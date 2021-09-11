def former(string):
    outString = str()
    for i in string:
        if i.isdigit():
            outString += i
    return outString


def changer(listIn):
    for i in range(len(listIn)):
        if len(listIn[i]) == 11:
            listIn[i] = listIn[i][1:]
        else:
            listIn[i] = '495' + listIn[i]


inFile = open('input.txt')
inList = []
for line in inFile:
    inList.append(former(line))
changer(inList)
inList = list(map(int, inList))
for j in range(1, len(inList)):
    if inList[0] == inList[j]:
        print('YES')
    else:
        print('NO')
