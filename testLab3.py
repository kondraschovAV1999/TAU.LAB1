import math


class CurrentGenerator:  # Генератор тока
    def __init__(self):
        self.timeSC = None
        self.source = None

    def createbase(self):  # Ток нормального режима
        self.base_tok1 = (math.sin(i/180 * math.pi) * 5 for i in range(0, 36000, 18))
        for i in self.base_tok1:
            yield i

    def create1stLevel(self):  # Ток предшествущего режима(1 период для расчета дейст.знач+период) затем КЗ
        self.base_tok2 = (math.sin(i / 180 * math.pi) * 5 for i in range(0, 720, 18))
        for i in self.base_tok2:
            yield i
        self.tok1stLevel = (math.sin(i / 180 * math.pi) * 50 for i in range(720, 36000, 18))
        for i in self.tok1stLevel:
            yield i


class CircuitBreaker:
    def __init__(self, name):
        self.name = name
        self.__state = False

    def turn_breaker_on(self):  # Метод для включения выключателя
        self.__state = True

    def turn_breaker_off(self):  # Метод для отключения выключателя
        self.__state = False

    def get_state(self):  # Метод для получения информации о положении выключателя
        return self.__state


class Izmeritel:  # В моем случае это ТТ
    def __init__(self, name, cb, generator):
        self.name = name  # название ТТ
        self.cb = cb  # выключатель присоединения, с которого снимаются показания
        self.generator = generator
        self.measurement = 0

    def get_data(self):
        if self.cb.get_state():
            return next(self.generator)
        else:
            return 0

    def mesur(self):
        self.measurement = self.get_data()
        print(f'Мгновенное значение тока { self.name}  =', '{0:.2f}'.format(self.measurement))


class Mtz:
    def __init__(self, name, ustavka, step, tt, cb):
        self.stepName = name  # название ступени
        self.ustavka = ustavka  # уставка по току
        self.step = step  # уставка по времени
        self.counter = 0  # счетчик времени превышения измеряемым током уставки
        self.tt = tt
        self.cb = cb

    def run(self):
        if self.cb.get_state():  # проверка для того, чтобы если какая-то из ступеней сработала другие не срабатывали
            i_sq = abs(self.tt.measurement)
            # print(f'Мгновенное значение тока { self.stepName}  =', '{0:.2f}'.format(i_sq))
            if i_sq >= self.ustavka * math.sqrt(2):
                self.counter += 1
                # print(self.stepName, self.counter)
            elif i_sq <= 0.9 * self.ustavka * math.sqrt(2):  # возврат защиты
                self.counter = 0
            if self.counter >= self.step:
                self.trip()

    def trip(self):  # Команда на отключение выключателя
        self.cb.turn_breaker_off()
        print(f'Сработала {self.stepName}')


cb1 = CircuitBreaker('CB1')
cb1.turn_breaker_on()
current_generator = CurrentGenerator()
current_generator.source = current_generator.create1stLevel()
tt1 = Izmeritel('TT1', cb1, current_generator.source)
stupen1 = Mtz('stupen 1', 60, 1, tt1, cb1)
stupen2 = Mtz('stupen 2', 40, 5, tt1, cb1)
stupen3 = Mtz('stupen 3', 10, 10, tt1, cb1)
while cb1.get_state():
    tt1.mesur()
    stupen1.run()
    stupen2.run()
    stupen3.run()
# class CurrentGenerator:
#     def createbase(self):
#         self.base = (5 * i + 7 for i in range(10))
#         for i in self.base:
#             yield i
#
#
# CG = CurrentGenerator()
# cz = CG.createbase()
# print(cz)
# for i in cz:
#     print(i)
#
#
# class CurrentGenerator2:
#     def createbase2(self):
#         self.base = (5 * i + 7 for i in range(10))
#         for i in self.base:
#             yield i
#
#
# CG2 = CurrentGenerator2()
# cz2 = CG2.createbase2()
# print(cz2)
# for j in range(2):
#     print(j)
#     for i in cz2:
#         print(i)
#
#
# class CurrentGenerator3:
#     def createbase3(self):
#         self.base = (5 * i + 7 for i in range(10))
#         for i in self.base:
#             yield i
#
#
# CG3 = CurrentGenerator3()
# cz3 = CG3.createbase3()
# print(cz3)
# for j in range(2):
#     print(j)
#     for j in range(6):
#         print(next(cz3))
