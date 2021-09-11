year = int(input())
if year < 100 and year % 4 == 0:
    print('YES')
elif year >= 100 and year % 100 == 0:
    print('NO')
if year >= 100 and year % 100 != 0 and year % 4 == 0:
    print('YES')
elif year % 4 != 0:
    print('NO')
