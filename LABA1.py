# for i in 2, 3, 5:
#     print(i*i)

# for i in range(10, 1, -1):
#     print(i*i)

# def functionName(a, b):
#     return a + b
#
#
# print(functionName(4, 7))
# c = functionName(4, 7)
# print(c)

def listCreator(x):
    newList = []
    for i in range(x):
        newList.append(i)
    return newList


def listSum(theList):
    result = 0
    for i in theList:
        result += i
    return result


list1 = listCreator(8)
x = listSum([2, 5, 7, 0, 6])
print(list1)
print(x)
