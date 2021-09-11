# class Car:
#     def __init__(self, car_number, car_year):
#         self.car_number = car_number
#         self._car_year = car_year
#         self.__car_model = 'model'
#
#     def _protected_method(self):
#         print(f'Protected метод \n\t и год сборки машины {self._car_year}')
#
#     def __private_method(self):
#         print(f'Private метод \n\t и номер машины {self.__car_model}')
#
#     def call_method(self):
#         self.__private_method()
#
#     def get__car_model(self):
#         return self.__car_model
#
#
# new_car = Car('348BX', 2020)
# print(new_car.car_number)
# print(new_car._car_year)
# new_car._protected_method()
# new_car.call_method()
# print(new_car.get__car_model())

# class Transport:
#     def __init__(self, number, model):
#         self.number = number
#         self.model = model
#
#     def transport_method(self):
#         print('Метод класса Transport')
#
#
# class Car(Transport):
#     def new_method(self, arg1, arg2= None):
#         if arg2 is not None:
#             print(arg1 + arg2)
#         else:
#             print(arg1)
#
#     def transport_method(self):
#         print('Метод класса Car')
#
#
# class Bicycle(Transport):
#     pass
#
#
# a = Transport('number', 'model')
# a.transport_method()
# c = Car('car_number', 'car_model')
# c.new_method(20)
# c.new_method(20, 30)
# c.transport_method()
# b = Bicycle(20, 'ABB')
# b.transport_method()
# from abc import ABC, abstractmethod
#
#
# class AbstractIntarfaces(ABC):
#     @abstractmethod
#     def method_1(self):
#         pass
#
#
# class NewClass(AbstractIntarfaces):
#     def method_1(self):
#         print('Это абстрактный метод_1')
#     def __init__(self, name):
#         self.name = name
#
#
# a = NewClass('имя')
# print(a.name)
# a.method_1()
# class NewClass:
#     def __init__(self):
#         self.name = 'name'
#
#     def method_1(self, arg1, arg2):
#         print(self.name)
#         return arg1 * arg2
#
#     @staticmethod
#     def method_2(arg1, arg2):
#         return arg1 * arg2
#
#
# a = NewClass()
# print(a.method_1(5, 20))
# print(a.method_2(20, 5))
# print(NewClass.method_2(5, 20))
#



















