def changeS(lst):
    for i in lst:
        i[-1] = int(i[-1])
        i[-2] = int(i[-2])


def sP(lst):
    return lst[-1]


inFile = open('input.txt', 'r', encoding='utf8')
students = list()
for line in inFile:
    students.append(list(line.split()))
changeS(students)
class9, class10, class11 = list(), list(), list()
for pupil in students:
    if pupil[-2] == 9:
        class9.append(pupil)
    elif pupil[-2] == 10:
        class10.append(pupil)
    else:
        class11.append(pupil)

print(list(map(sP, class9)).count(max(map(sP, class9))), end=' ')
print(list(map(sP, class10)).count(max(map(sP, class10))), end=' ')
print(list(map(sP, class11)).count(max(map(sP, class11))))
