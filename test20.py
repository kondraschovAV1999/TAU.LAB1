def changeList(a):
    for j in a:
        j[-1] = int(j[-1])


n = int(input())
students = list()
for i in range(n):
    students.append(input().split())
changeList(students)
students.sort(key=lambda a: a[-1], reverse=True)
for student in students:
    print(student[0])
