import sqlite3
connection = sqlite3.connect('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\LR5.db')
cursor = connection.cursor()
with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\/normal.cfg') as cfg:
    # откраваем файл конфигурации для чтения необходимых коэффициентов
    listCFG = cfg.readlines()
    a = []
    b = []
    for i in range(2, 5):
        line = listCFG[i].split(',')
        a.append(float(line[5]))
        b.append(float(line[6]))
for i in range(3):
    cursor.execute('insert into Coefficients ("a", "b", "regimId" ,"measureId")  values (?,?,?,?)',
                   [a[i], b[i], 1, i + 1])
    # заносим эти данные в таблицу коэффициентов в БД
connection.commit()
dat = list((cursor.execute('SELECT max(timeId) from Time')))
# запрос необходимый для того, чтобы знать какое значение id у времени использовать
k = dat[0][0] + 1
with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\/normal.dat') as kz:
    # открываем файл данных для того, чтобы считать оттуда значения токов и занести их в БД
    readGen = (line for line in kz)
    for line in readGen:
        line = line.rstrip().split(',')
        for i in range(3):
            cursor.execute('insert into "Time" ("timeId", "value") values (?,?)', [k, int(line[1])])
            cursor.execute('insert into "val" ("values", "measureId", "regimId", "timeId")'
                           'values (?,?,?,?)',
                           [int(line[i + 2]), i + 1, 1, k])
            k += 1
connection.commit()
connection.close()

