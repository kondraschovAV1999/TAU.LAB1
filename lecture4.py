# def new_func(*args):
#     return args
#
#
# print(new_func(1, 'word 1', 2, 'word 2'))
#
#
# def my_func(**kwargs):
#     return kwargs
#
#
# print(my_func(el_1=1, el_2=2, el=2))

# my_func = lambda arg_1, arg_2: arg_1 + arg_2
#
# print(my_func(2, 5))
# print(my_func('abra', 'kadabra'))
# print((lambda arg_1, arg_2: arg_1 + arg_2)(2, 5))
# new_func = lambda *args: args
# print(new_func(1, 2, 3, 4))
#
#
# def new_funcr(param):
#     return param ** 0.5
#
#
# print(new_funcr(100))
# Функция map
# L = [1, 2, 3, 4]
# y = list(map(lambda x: x**2, L))
# print(*y)

# Функция filter
# def even_fn(x):
#     if x % 2 == 0:
#         return True
#     return False
#
#
# print(list(filter(even_fn, [1, 2, 3, 4])))
# print(list(filter(lambda x: x % 2)))

# import math
#
# print(max(1, 2, 3, 4, 5, 6, 7, 8))

# Локальная область видимости, глобальная область видимости, нелокальная область видимости
# 1 Локальная область видимости
# def full_s_calc():
#     global s_circle
#     r_val = float(input("Укажите длину: "))
#     h_val = float(input("Укажите ширину: "))
#     s_side = r_val * h_val
#     s_circle =(h_val**2 + r_val**2) ** 0.5
#     return s_side
#
# s_val = full_s_calc()
# print(s_val)
# print(s_circle)

# 2 Нелокальная область видимости
# def ext_func():
#     my_var = 0
#     def int_func():
#         nonlocal my_var
#         my_var += 1
#         return my_var
#     return int_func()
#
#
# func_object = ext_func()
# print(func_object)

# Импорт модулей в Python
# Псевдонимы. Если названия слишком длинные,
# или оно вам не нравится по каким-то причинам,
# то ддля него можно создать псевдоним, с помощью ключевого слова as
# import math as m
# генераторы списков и словарей в Python
# new_list = [i for i in sequence] общий алгоритм
# my_list = [2, 4, 6]
# new_list = [el + 10 for el in my_list]
# print(my_list)
# print(new_list)
# new_list2 = [i for i in range(5, 20, 3)]
# print(new_list2)
# new_set = {i for i in sequense}
# new_dict = {i }
# new_set = {i for i in range(5, 20, 3)}
# print(new_set)
# new_dict = {i * 2: i * 3 for  i in range (5, 20, 3)}
# print(new_dict)
# base_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list2 = [base_list[el] for el in range(1, len(base_list)) if base_list[el] > base_list[el - 1]]
# print(new_list2)
# yeld
# def createGenerator():
#     myList = range(4)
#     for i in myList:
#         yield i * i
#
#
# generator = createGenerator()
# print(next(generator))
# print(next(generator))
# print(next(generator))
