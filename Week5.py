# Кортежы
# myTuple = [1, 2, 3]  # Создаем кортеж
# print(myTuple[1])
# sTuple = [4, 5, 6]
# print(myTuple + sTuple)
# print(len(myTuple))

# myTuple = (1, (2, 3), (4,))
# print(myTuple[1][0])

# man = ('Ivan', 'Ivanov', 28)
# print(man[-1])

# myTuple = 1, 2, 3
# a, b, c = myTuple
# print(b)

# Цикл For
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
# Функция range
# myRange = range(10)  # Правая граница не включается
# print(tuple(myRange))  # Команда tuple создает кортеж

# for color in ('red', 'green', 'yellow'):
#     print(color, 'apple')
# for i in range(25):
#     print(i)
# for i in range(10, 0, -1):
#     print(i, end=' ')

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()