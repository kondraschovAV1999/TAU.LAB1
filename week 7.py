# fSet = {1, 2, 3}
# sSet = {3, 1, 2}
# print(fSet == sSet)
# Функция set() получает что-нибудь итерируемое и позволяет создавать из этого множество
# myList = map(int, input().split())
# mySet = set(myList)
# print(mySet)
# mySet = {1, 3.14, 'abc', (1, 2)}
# print(mySet)
# Неизменяемое множество frozenset()
# mySet = {1, 2, 3, 1, 4}
# print(*sorted(list(mySet)))
# Подсчет различного количества букв в строке
# mySet = set('abcdabc')  # Повторяющиеся элементы при этом пропадут
# print(len(mySet))
# Работа с множествами
# mySet = {1, 2, 3, 40000}
# for elem in mySet:
#     print(elem)
# mySet = {2, 3, 5, 7, 11, 13}
# n = int(input())
# if n in mySet:
#     print('in set')
# else:
#     print('not in set')
# mySet = {2, 3, 5, 7, 11, 13}
# n = int(input())
# if n not in mySet:
#     print('not in set')
# else:
#     print('in set')
# Работа с отдельными эл-тами множества
# mySet = {2, 3, 5, 7, 11, 11}
# mySet.add(17)  # добавление элемента в массив
# print(*mySet)
# mySet.remove(13)  # удаление элемента, но если эл-там нет,то будет ошибка
# mySet.discard(17)  # удаление элемента,но если такого эл-та нет, то ничего не происходит
# Операции с самим множеством
# a = {1, 2, 3, 4}
# b = {1, 3}
# print(a == b)
# print(a != b)
# print(a < b)  # a будет > b , если все эл-ты a входят в b и в b еще есть элементы
# print(a > b)
# a = {1, 2, 3, 4}
# b = {1, 3, 5}
# print(a | b)  # объединение двух множеств
# print(a & b)  # пересечение множеств
# print(a - b)  # все эл-ты, которые содержаться в а и не содержаться в b
# print(a ^ b)  # симметрическая разность ( все эл-ты входящие в объединение множеств, но не входящие в их пересечение)
# Словари
# capitals = {'Russia': 'Moscow', 'France': 'Paris'}
# capitals['USA'] = 'Washington'  # Таким образом добавляются эл-ты в словарь
# print(capitals['Russia'])
# print(capitals['USA'])
# print(capitals)
# print(*capitals)
# del capitals['France']  # Таким образом удаляется эл-т словоря
# print(capitals)
# print('Russia' in capitals)  # Проверка наличия ключа в словаре
# myDict = dict((('x', 5), ('y', 3)))
# print(myDict)
# # for i in myDict:
# #     print(i)
# # В этом случае будут перебираться только ключи
# # Если мы хотим перебарать пары ключ, значение, тогда:
# for i in myDict:
#     print(i, myDict[i])
# # Ключи уникальны и каждому из них сопоставлен некоторый объект-значение, а вот значения могут быть и изменяемыми.
# Когда нужно использовать словари
# Подсчет количества вхождения букв в строку
# s = input()
# letters = dict()
# for c in s:
#     if c not in letters:
#         letters[c] = 0
#     letters[c] += 1
# for c in sorted(letters):
#     print(c, letters[c])
# s = input()
# letters = dict()
# for c in s:
#     letters[c] = letters.get(c, 0) + 1
# for c in sorted(letters):
#     print(c, letters[c])
# # Метод get принимает два значения на вход, первое- это ключ, второе
# # это то, что нужно положить, если этого ключа нет
# gasCost = {}
# n = int(input())
# a92, a95, a98 = map(int, input().split())
# gasCost[92] = a92
# gasCost[95] = a95
# gasCost[98] = a98
# for i in range(n - 1):
#     a92, a95, a98 = map(int, input().split())
#     gasCost[92] = min(a92, gasCost[92])
#     gasCost[95] = min(a95, gasCost[95])
#     gasCost[98] = min(a98, gasCost[98])
# print(gasCost[92], gasCost[95], gasCost[98])
#  Полезные методы строк
# gasCost = {}
# n = int(input())
# costs = list(map(int, input().split()))
# btypes = (92, 95, 98)
# for now in range(len(btypes)):
#     gasCost[btypes[now]] = costs[now]
# for i in range(n - 1):
#     costs = list(map(int, input().split()))
#     for now in range(len(btypes)):
#         gasCost[btypes[now]] = min(costs[now], gasCost[btypes[now]])
# print(gasCost[92], gasCost[95], gasCost[98])
# s = input()
# print(s.isalpha())  # Метод выдает True , если строка состоит только из букв
# print(s.isalnum())  # Метод выдает True , если строка состоит из букв и цифр
# print(s.isdigit())  # Метод выдает True , если строка состоит из цифр
# print(s.islower())  # Метод выдает True , если строка состоит из строчных букв
# print(s.isupper())  # Метод выдает True , если строка состоит из заглавных букв
# print(s.strip())  # Метод позволяет обрезать пробельные символы по концам строки
# print(s.lstrip())  # Метод позволяет обрезать пробельные символы с левого конца
# print(s.rstrip())  # Метод позволяет обрезать пробельные символы с правого конца
# fin = open('input.txt')
# myDict = {}
# for line in fin:
#     eng, latins = line.split('-')
#     latinsList = latins.split(',')
#     eng = eng.strip()
#     for latin in latinsList:
#         if latin.strip() not in myDict:
#             myDict[latin.strip()] = []
#         myDict[latin.strip()].append(eng)
# for latin in sorted(myDict):
#     print(latin, '-', ','.join(sorted(myDict[latin])))

