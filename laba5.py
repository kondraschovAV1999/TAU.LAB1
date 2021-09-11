import sqlite3
connection = sqlite3.connect('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы\LR5.db')
cursor = connection.cursor()
dat = cursor.execute('SELECT max(timeId) from Time')
for i in dat:
    print(int(dat))

# cursor.execute("select * from измерения")
# results = cursor.fetchall()
# results = cursor.fetchall()
connection.close()
