from CSP import CSP as Mtz
from CB import CircuitBreaker
from TT1 import TT
import matplotlib.pyplot as mpl

curA, curB, curC = [], [], []  # Создаем списки для каждого тока, чтобы в последствии построить графики
dataTime = []  # аналогично список момента снятия каждого тока
with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\KZonBus2.cfg') as cfg:
    # Открываем файл конфигурации, для получения поправочных коэффициентов
    listCFG = cfg.readlines()  # читаем весь файл и записываем в переменную
    # поправочные коэффициенты (формула для пересчета ax+b, где x-значение в .DAT файле)
    a = []
    b = []
    for i in range(2, 5):
        line = listCFG[i].split(',')
        a.append(float(line[5]))
        b.append(float(line[6]))
    freqDisk = int(listCFG[7].split(',')[0])
    # частота дискретизации нужна для определения кол-ва отсчетов тока за один период
print(a)
print(b)
cb1 = CircuitBreaker('CB1')  # Создаем экземпляр класса выключателя
cb1.turn_breaker_on()  # Включаем выключатель
tt1 = TT('TT1', cb1, freqDisk)  # Создаем ТТ
stupen1 = Mtz('stupen 1', 2, 0.1, tt1, cb1)  # Первая ступень ТСЗ
stupen2 = Mtz('stupen 2', 1.5, 0.5, tt1, cb1)  # Вторая ступень ТСЗ
stupen3 = Mtz('stupen 3', 0.9, 1, tt1, cb1)  # МТЗ
with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\KZonBus2.dat') as kz:
    # Открываем файл с записанной осцилограммой
    readGen = (line for line in kz)  # Чтобы не хранить в памяти весь файл будем использовать генератор
    for line in readGen:
        line = line.rstrip().split(',')
        if cb1.get_state():  # Если защита сработала, то прерываем чтение.
            tt1.measure(a[0] * int(line[2]) + b[0], 'A')
            curA.append(a[0] * int(line[2]) + b[0])
            tt1.measure(a[1] * int(line[3]) + b[1], 'B')
            curB.append(a[1] * int(line[3]) + b[1])
            tt1.measure(a[2] * int(line[4]) + b[2], 'C')
            curC.append(a[2] * int(line[4]) + b[2])
            stupen1.run()
            stupen2.run()
            stupen3.run()
        elif not cb1.get_state():
            curA.append(0)
            curB.append(0)
            curC.append(0)
        dataTime.append(int(line[1]))


print('Время от начала = ', '{0:.3f}'.format(max(dataTime)/1000000), 'c', sep='')

mpl.figure('Графики токов')
mpl.title('График токов от времени')  # Заголовок графика
mpl.subplot()
mpl.grid(True)  # Включаем сетку
mpl.axis([0, max(dataTime), min(map(min, curA, curB, curC)), max(map(max, curA, curB, curC))])
# Задаем пределы по оси Х и по оси Y
mpl.xlabel('t, mks')  # Обозначаем ось X
mpl.ylabel('I, kA')  # Обозначаем ось Y
lines = [None, None, None]
lines[0], lines[1], lines[2] = mpl.plot(dataTime, curA, 'yellow', dataTime, curB, 'green', dataTime, curC, 'red')
mpl.legend(lines, ['Ia', 'Ib', 'Ic'], loc='upper left')  # Создаем легенду и задаем ее положение на графике
mpl.show()
