import math


class TT:
    def __init__(self, name, cb, freqDisk):
        self.name = name  # название ТТ
        self.cb = cb  # выключатель присоединения, с которого снимаются показания
        self.measurement = [[], [], []]
        self.freqDisk = freqDisk  # частота дискретизации
        self.i_tt = [0, 0, 0]

    def measure(self, value, phase):  # По сути это измерение тока за один период через ТТ
        if phase == 'A':
            self.measurement[0].append(value)
        elif phase == 'B':
            self.measurement[1].append(value)
        else:
            self.measurement[2].append(value)
        if (len(self.measurement[0]) == len(self.measurement[1]) == len(self.measurement[2]) ==
        self.freqDisk / 50):  # измерения ведутся по периодам
            for i in range(3):
                self.i_tt[i] = self.calc_sq(self.measurement[i])
            # print(f'Действующее значение тока фазы A, B, C =', '{0:.3f}'.format(self.i_tt[0]), end=' ,')
            print('Ia =', '{0:.3f}'.format(self.i_tt[0]), end=' ,')
            print('Ib =', '{0:.3f}'.format(self.i_tt[1]), end=' ,')
            print('Ic =', '{0:.3f}'.format(self.i_tt[2]))
            self.measurement = [[], [], []]

    def calc_sq(self, value):  # Вычисление действующего значения тока
        return math.sqrt(sum(m * m / len(value) for m in value))
