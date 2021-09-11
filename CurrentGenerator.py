import math


class CurrentGenerator:  # Генератор тока
    def __init__(self):
        self.source = None
        self.ampNorm = int(input('Введите значение амплитуды тока нормального режима: '))
        self.ampSC = int(input('Введите значение амплитуды тока КЗ: '))
        self.timeSC = int(input('Введите кол-во периодов КЗ: '))

    def createbase(self):  # Ток нормального режима
        self.base_tok1 = (math.sin(i/180 * math.pi) * self.ampNorm for i in range(0, 36000, 18))
        for i in self.base_tok1:
            yield i

    def create1stLevel(self, timeNorm ):  # Ток предшествущего режима(2 периода) затем КЗ
        # timeNorm = int(input('Введите кол-во периодов предшествущего режима: '))
        self.base_tok2 = (math.sin(i / 180 * math.pi) * self.ampNorm for i in range(0, 360 * timeNorm, 18))
        for i in self.base_tok2:
            yield i
        self.tok1stLevel = (math.sin(i / 180 * math.pi) * self.ampSC for i in range(720, 360 * self.timeSC, 18))
        for i in self.tok1stLevel:
            yield i
