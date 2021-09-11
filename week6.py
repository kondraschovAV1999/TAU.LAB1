# class Man:
#     height = 0
#     name = ''
#
#
# p = []
# n = int(input())
# for i in range(n):
#     h, n = input().split()
#     h = int(h)
#     man = Man()
#     man.height = h
#     man.name = n
#     p.append(man)
#
#
# def makeTuple(man):
#     return (man.height, man.name)
#
#
# p.sort(key=makeTuple)
# for now in p:
#     print(now.height, now.name)

# points = [(1, 1),
#           (5, 1),
#           (10, 10)]
# points.sort(key=lambda p: p[0]**2 + p[1]**2)
# print(*points)

# x = [1, 5, 2, 3]
# y = list(map(lambda x: x**2, x))
# print(*y)
# print(' '.join(map(lambda x: str(x**2), range(1, 101))))

# def printList(lst, mySep):
#     for i in range(len(lst)):
#         print(lst[i], mySep, sep='', end='')
#
#
# printList([1, 2, 3], ' ')
# printList([5, 6, 7], ' ')

# def printList(lst, mySep = ' '):
#     for i in range(len(lst) - 1):
#         print(lst[i], mySep, sep='', end='')
#     print(lst[len(lst) - 1], sep='')
#
#
# printList([1, 2, 3], mySep='a')
# printList([5, 6, 7], mySep='a')

#  Функция суммирующая бесконечное множество параметров
# def mySum(*args):
#     return sum(args)
#
#
# print(mySum(1, 2, 3, 4))
# print(mySum(1))


# def mySum(*args):
#     nowSum = 0
#     for now in args:
#         nowSum += now
#     return nowSum
#
#
# print(mySum(1, 2, 3, 4))
# print(mySum(1))

# def myMin(first, *others):
#     nowMin = first
#     for now in others:
#         if now < nowMin:
#             nowMin = now
#     return nowMin
#
#
# print(myMin(5, 2, 3, 4))
# print(myMin(1))

# Чтение до конца ввода

# fin = open('input.txt', 'r', encoding='utf8')
# a = int(fin.readline())
# b = int(fin.readline())
# print(a + b)
# lines = fin.readlines()
# print([lines[0].strip()], [lines[1].strip()])
# for line in fin:
#     print(int(line) + 1)
# fout = open('output.txt', 'w', encoding='utf8')
# print(sum(map(int, fin.readlines())), file=fout)
# fout.close()


# Сортировка подсчетом

# myList = list(map(int, input().split()))
# newList = []
# for i in range(len(myList)):
#     newList.append((myList[i], i))
# newList.sort()
# for now in newList:
#     print(now[1])

# myList = list(map(int, input().split()))
# grades = [0] * 11
# for now in myList:
#     grades[now] += 1
# for grade in range(len(grades)):
#     for i in range(grades[grade]):
#         print(grade, end=' ')

