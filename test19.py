def intersection(a, b):
    i = 0
    j = 0
    listD = list()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] == b[j]:
            listD.append(a[i])
            i += 1
            j += 1
    return listD


listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
print(*intersection(listA, listB))
