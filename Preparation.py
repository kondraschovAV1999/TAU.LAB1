# set1 = set()  # Создаю множество
# for i in range(1, 11):  # Заполняю множество элекментам от 1 до 10
#     set1.add(i)
# print(set1)  # Вывожу полученное множество
# list1 = list()  # Создаю список
# for i in set1:  # Заполняю список элементами множества, при этом эл-ты кратные 3 увеличиваю в 4 разные остальные на 6
#     if i % 3 == 0:
#         list1.append(4 * i)
#     else:
#         list1.append(i + 6)
# print(list1) # Вывожу результат
# dict1 = dict.fromkeys(list(set1))  # Из списка создают словарь с ключами в виде множества
# print(dict1)
# for i in range(len(list1)):
#     dict1[list(set1)[i]] = list1[i]  # Заполняю словарь
# print(dict1)

# list1 = list()  # Создаю список
# for i in range(45, 7, -3):  # Заполняю список элементами
#     list1.append(i)
# print(list1)  # Вывожу списк
# set1 = set()  # Создаю множество
# n = 0  # Задаю счетчик нечетных эл-ов
# for i in list1:  # Заполняю множество четными эл-тами списка, и параллельно подсчитываю кол-во нечетных
#     if i % 2 == 0:
#         set1.add(i)
#     else:
#         n += 1
# print(set1)  # Вывожу множество
# print('Количество нечетных в списке -', n)
# for i in range(len(set1)):  # Добавляю в список эл-ты множества
#     list1.append(list(set1)[i])
# print(list1)  # Вывожу получившийся список
# for i in range(len(list1)):  # Добавляю эл-ты списки в множество
#     set1.add(list1[i])
# print(set1)  # Вывожу получившееся множество


tuple1 = list()
for i in range(7, 16):
    tuple1.append(i)
tuple1 = tuple(tuple1)
print(tuple1)
list1 = list()
for i in tuple1:
    if i % 2 == 0:
        list1.append(3 * i)
    else:
        list1.append(i / 3)
print(list1)
set1 = set()
list2 = list()
list2.extend(list1)
list2.extend(list(tuple1))
for i in list2:
    set1.add(i)
print(set1)
