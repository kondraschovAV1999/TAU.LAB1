def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def creat_list(length):
    outList = list()
    for i in range(length):
        if i % 2 != 0:
            outList.append(i)
    return outList


my_list = creat_list(100)
print(*creat_list(100))
print(binary_search(my_list, 97))
print(my_list.index(51))
# print(binary_search(my_list, -1))
