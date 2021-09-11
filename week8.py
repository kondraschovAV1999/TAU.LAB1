# Встроенный функции для работы с последовательностями
# sum()
# max()
# min()
# map()
# sorted()
# print(
#     *filter(
#         lambda x: x > 0,
#         map(
#             int,
#             input().split()
#         )
#     )
# )
# print(*enumerate('abcde'))
#  Функция enumerate(имяПослед.) нужна для нумерации эл-ов последовательности
# Функция any() хотя бы один эл-м последовательности истина(True), тогда значение функции будет также True
# print(any((True, False, True)))
# Функция all() все эл-ы последовательности истина(True), тогда значение функции будет также True
# print(
#     all(
#         map(
#             lambda x: x > 0,
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )
# Задача: Есть N людей и количество км, которое им необходимо проехать до дома
# а также есть N такси,в которых цены за километр разные
# требуется сопоставить каждому человеку определенное такси так, чтобы суммарные затраты были минимальными
#
# print(*
#       map(
#           lambda x: x[1][0],
#           sorted(
#               zip(
#                   sorted(
#                       enumerate(
#                           map(
#                               int,
#                               input().split())
#                       ),
#                       key=lambda x: x[1]
#                   ),
#                   sorted(
#                       enumerate(
#                           map(
#                               int,
#                               input().split())
#                       ),
#                       key=lambda x: x[1],
#                       reverse=True
#                   )
#               ),
#               key=lambda x: x[0][0]
#           )
#       )
#       )
# import itertools

# print(*itertools.combinations([1, 2, 3], 2))
# подмножества исходного множества
# print(*itertools.permutations([1, 2, 3]))
# все перестановки эл-ов множества
# print(*itertools.combinations_with_replacement([1, 2, 3], 2))
# import itertools

# prints = functools.partial(print, end=' ')
# # данный метод позволяет для функции задавать именнованный параметр по умолчанию
# prints(1)
# prints(2)
# print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))
# reduce() позволяет получать результат последовательного применения функции
# print(*itertools.accumulate([1, 4, 3, 5], max))
# Функция accumulate позволяет накапливать промежуточный результат
#
#
# def myRange(n):
#     i = 0
#     while i < n:
#         yield i**2
#         i += 1
#
#
# s = 0
# for i in myRange(10):
#     print(i)
