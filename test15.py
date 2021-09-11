def changeS(lst):
    for i in lst:
        i[-1] = int(i[-1])
        i[-2] = int(i[-2])


def averageScore(lst):
    sumScore = 0
    for i in lst:
        sumScore += i[-1]
    return sumScore / len(lst)


verFile = open('input.txt', 'r', encoding='utf8')
students = list()
for line in verFile:
    students.append(list(line.split()))
changeS(students)
class9 = list()
class10 = list()
class11 = list()
for pupil in students:
    if pupil[-2] == 9:
        class9.append(pupil)
    elif pupil[-2] == 10:
        class10.append(pupil)
    else:
        class11.append(pupil)
print(averageScore(class9), averageScore(class10), averageScore(class11))
