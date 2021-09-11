def merge(a, b):
    i = 0
    j = 0
    listD = []
    while i < len(a) + 1:
        if j > len(b) - 1:
            listD.extend(a[i:])
            break
        if i > len(a) - 1:
            listD.extend(b[j:])
            break
        if a[i] > b[j]:
            listD.append(b[j])
            j += 1

        elif a[i] < b[j]:
            listD.append(a[i])
            i += 1

        elif a[i] == b[j]:
            listD.append(b[j])
            listD.append(b[j])
            i += 1
            j += 1
    return listD


listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
print(*merge(listA, listB))
