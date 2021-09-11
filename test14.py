def makelist(listN, a):
    for k in range(a):
        tuple1 = (listN[k], k + 1)
        listN[k] = tuple1


def sortList(tupleN):
    return tupleN[0]


def srav(t1, t2):
    return t1[0] - t2[0]


n = int(input())
list1 = list(map(int, input().split(' ')))
m = int(input())
list2 = list(map(int, input().split(' ')))
makelist(list1, n)
makelist(list2, m)
list1.sort(key=sortList)
list2.sort(key=sortList)
list3 = list()
j = 0
i = 0
while i < n:
    if m == 1:
        list3.append((list1[i][1], list2[j][1]))
        i += 1
        continue
    if srav(list1[i], list2[j]) <= 0:
        list3.append((list1[i][1], list2[j][1]))
        i += 1
    elif abs(srav(list1[i], list2[j])) > abs(srav(list1[i], list2[j + 1])):
        j += 1
        if j == m - 1:
            while i < n:
                list3.append((list1[i][1], list2[j][1]))
                i += 1
    else:
        list3.append((list1[i][1], list2[j][1]))
        i += 1
list3.sort()
for i in range(len(list3)):
    print(list3[i][1], end=' ')
