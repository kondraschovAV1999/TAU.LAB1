def keySort(lst):
    return lst[0]


def removeNumSchool(lst):
    for i in lst:
        i.pop(-2)


def changeS(lst):
    for i in lst:
        i[-1] = int(i[-1])
        i[-2] = int(i[-2])


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
students = list()
for student in inFile:
    students.append(list(student.split()))
changeS(students)
students.sort(key=keySort)
removeNumSchool(students)

for stud in students:
    for i in stud:
        print(i, sep=' ', file=outFile, end=' ')
    print(file=outFile)

inFile.close()
outFile.close()
