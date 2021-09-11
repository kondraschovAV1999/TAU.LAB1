import math
a, b, c = float(input()),  float(input()),  float(input())
D = b ** 2 - 4*a*c
if D > 0 and a != 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(2, min(x1, x2), max(x1, x2))
elif D < 0:
    print(0)
elif a == b == c == 0:
    print(3)
elif a == b == 0:
    print(0)
elif D == 0:
    x1 = -b / (2 * a)
    print(1, x1)
elif a == 0 and b != 0:
    x1 = - c / b
    print(1, x1)
