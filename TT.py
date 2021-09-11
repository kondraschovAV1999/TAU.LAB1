import math


class Izmeritel:  # В моем случае это ТТ
    def __init__(self, name, cb, generator=None):
        self.name = name  # название ТТ
        self.cb = cb  # выключатель присоединения, с которого снимаются показания
        self.generator = generator
        self.measurement = []
        self.i_tt = 0

    def get_data(self):
        if self.cb.get_state():
            return next(self.generator)
        else:
            return 0

    def measure(self):  # По сути это измерение тока за один период через ТТ
        self.measurement = []
        while len(self.measurement) < 20:
            self.measurement.append(self.get_data())
        self.i_tt = self.calc_sq(self.measurement)
        print(f'Действующее значение тока через {self.name} =', '{0:.2f}'.format(self.i_tt))

    def calc_sq(self, value):  # Вычисление действующего значения тока
        return math.sqrt(sum(m * m / len(value) for m in value))
