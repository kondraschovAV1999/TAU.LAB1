a, b, c, d = float(input()), float(input()), float(input()), float(input())
e, f = float(input()), float(input())
delta = a*d - b*c
if delta == 0:
    if a == b == c == d == e == f == 0:
        print(5)
    elif b == d == 0 and e*c == f*a and a != 0:
        print(3, e / a)
    elif b == d == 0 and e*c == f*a and c != 0:
        print(3, f / c)
    elif a == c == 0 and e*d == b*f and d != 0:
        print(4, f / d)
    elif a == c == 0 and e*d == b*f and b != 0:
        print(4, e / b)
    elif c != 0 and d != 0 and f != 0 and a / c == b / d == e / f:
        print(1, -c / d, f / d)
    elif a != 0 and b != 0 and e != 0 and c / a == d / b == f / e:
        print(1, - a / b, e / b)
    elif e == f == 0:
        print(1, - a / b, 0)
    else:
        print(0)
if delta != 0:
    deltaX = e * d - b * f
    deltaY = a * f - c * e
    x = deltaX / delta
    y = deltaY / delta
    print(2, x, y)
