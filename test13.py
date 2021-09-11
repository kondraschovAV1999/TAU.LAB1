a = list(map(int, input().split()))
k, c = list(map(int, input().split()))


def reverse(b, alist):
    for j in range(1, len(alist) - b):
        for i in range(b, len(alist) - j):
            alist[i], alist[i + 1] = alist[i + 1], alist[i]


reverse(k, a)
a.append(c)
reverse(k, a)
print(' '.join(map(str, a)))
