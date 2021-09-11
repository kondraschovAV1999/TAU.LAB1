n = int(input())
if n % 2 != 0:
    i = 0
    while n != 0:
        n = int(input())
        if n == 0:
            continue
        if n % 2 == 0:
            i += 1
    print(i)
elif n != 0:
    j = 1
    while n != 0:
        n = int(input())
        if n == 0:
            continue
        if n % 2 == 0:
            j += 1
    print(j)
else:
    print(0)
