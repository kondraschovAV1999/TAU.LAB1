A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if A1 >= B1 >= C1 or A1 >= C1 >= B1:
    if B1 >= C1:
        A1, B1, C1 = C1, B1, A1
    else:
        A1, B1, C1 = B1, C1, A1
elif B1 >= C1 >= A1 or B1 >= A1 >= C1:
    if C1 >= A1:
        A1, B1, C1 = A1, C1, B1
    else:
        A1, B1, C1 = C1, A1, B1
elif C1 >= A1 >= B1 or C1 >= B1 >= A1:
    if A1 >= B1:
        A1, B1, C1 = B1, A1, C1
    else:
        A1, B1, C1 = A1, B1, C1
if A2 >= B2 >= C2 or A2 >= C2 >= B2:
    if B2 >= C2:
        A2, B2, C2 = C2, B2, A2
    else:
        A2, B2, C2 = B2, C2, A2
elif B2 >= C2 >= A2 or B2 >= A2 >= C2:
    if C2 >= A2:
        A2, B2, C2 = A2, C2, B2
    else:
        A2, B2, C2 = C2, A2, B2
elif C2 >= A2 >= B2 or C2 >= B2 >= A2:
    if A2 >= B2:
        A2, B2, C2 = B2, A2, C2
    else:
        A2, B2, C2 = A2, B2, C2
if A1 >= A2 and B1 >= B2 and C1 >= C2 and (A1 != A2 or B1 != B2 or C1 != C2):
    print("The first box is larger than the second one")
elif A1 <= A2 and B1 <= B2 and C1 <= C2 and (A1 != A2 or B1 != B2 or C1 != C2):
    print('The first box is smaller than the second one')
elif A1 == A2 and B1 == B2 and C1 == C2:
    print('Boxes are equal')
else:
    print('Boxes are incomparable')
