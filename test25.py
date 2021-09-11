pupils = int(input())
languages = set()
pupilList = list()
for pupil in range(pupils):
    numberLanguages = int(input())
    for language in range(numberLanguages):
        languages.add(input())
    pupilList.append(languages)
    languages = set()
pupilList = sorted(pupilList, key=len)
k = 0
allKnow = list()
for i in pupilList[0]:
    for j in pupilList:
        if i in j:
            k += 1
    if k == len(pupilList):
        allKnow.append(i)
    k = 0
print(len(allKnow))
for now in allKnow:
    print(now)
pupilSet = set()
for elem in pupilList:
    for s in elem:
        pupilSet.add(s)
print(len(pupilSet))
for el in pupilSet:
    print(el)
