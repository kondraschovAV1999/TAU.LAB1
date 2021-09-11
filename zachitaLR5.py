import sqlite3
import matplotlib.pyplot as mpl


def getCur(cur, step, k):  # функция, необходимая для получения значений токов в кА и момента времени
    value = list()
    t1 = list()
    t2 = list()
    for i in range(step, len(cur), 3):
        value.append(k[step][0]*cur[i][0]+k[step][1])
        t1.append(cur[i][1])
        t2.append(cur[i][2])
    return value, t1, t2


def znach(cur, phase, regim):
    for i in range(len(cur[0])):
        cursor.execute('insert into "Znach" (regimId, measureId, znach, timeId) values(?,?,?,?)',
                       [regim, phase, cur[0][i], cur[2][i]])



connection = sqlite3.connect('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\LR5.db')
cursor = connection.cursor()
cof = list(cursor.execute('SELECT a, b FROM Coefficients where regimId = 2'))  # коэффициенты для получения токов
val = list(cursor.execute('SELECT "values", Time.value, Time.timeId FROM val '
                          'join Time on Time.timeId = val.timeId '
                          'where regimId = 2 '))
# Считываем данные и записмываем их в список
curA = getCur(val, 0, cof)
curB = getCur(val, 1, cof)
curC = getCur(val, 2, cof)
# # Строим график
# mpl.figure('Графики токов')
# mpl.title('График токов от времени')  # Заголовок графика
# mpl.subplot()
# mpl.grid(True)  # Включаем сетку
# mpl.axis([0, max(curA[1]), min(map(min, curA[0], curB[0], curC[0])) - 0.2, max(map(max, curA[0], curB[0], curC[0]))+0.2])
# # Задаем пределы по оси Х и по оси Y
# mpl.xlabel('t, mks')  # Обозначаем ось X
# mpl.ylabel('I, kA')  # Обозначаем ось Y
# lines = [None, None, None]
# lines[0], lines[1], lines[2] = mpl.plot(curA[1], curA[0], 'yellow', curB[1], curB[0], 'green', curC[1], curC[0], 'red')
# mpl.legend(lines, ['Ia', 'Ib', 'Ic'], loc='upper left')  # Создаем легенду и задаем ее положение на графике
# mpl.show()
znach(curA, 0, 2)
znach(curB, 1, 2)
znach(curC, 2, 2)
connection.commit()
connection.close()
