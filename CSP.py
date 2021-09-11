class CSP:
    def __init__(self, name, ustavka, step, tt, cb):
        self.stepName = name  # название ступени
        self.ustavka = ustavka  # уставка по току
        self.step = step  # уставка по времени
        self.counter = 0.02  # счетчик времени превышения измеряемым током уставки
        self.tt = tt
        self.cb = cb

    def run(self):
        i_sq = self.tt.i_tt
        if (i_sq[0] >= self.ustavka or i_sq[1] >= self.ustavka or
                i_sq[2] >= self.ustavka):
            self.counter += 1 / self.tt.freqDisk
        elif (i_sq[0] <= 0.9 * self.ustavka or i_sq[1] <= 0.9 * self.ustavka or
                i_sq[2] <= 0.9 * self.ustavka):  # возврат защиты
            self.counter = 0.02
        if self.counter >= self.step:
            self.trip()

    def trip(self):  # Команда на отключение выключателя
        self.cb.turn_breaker_off()
        print(f'Сработала {self.stepName}')
