# Чтение файлов
# f = open('input.txt', 'r', encoding='utf-8')
# data = f.read()
# data1 = f.readline()
# print(data1, end='')
# data2 = f.readlines()
# print(data2)
# print(data)
# Зачем закрывать файл
# f.close()
# for i in data2:
#     print(i.upper())
# with open('input.txt', 'r') as f:
#     data = f.read()
# print(data)
# Запись в файл
# with open('output.txt', 'w') as y:
#     y.write('more added data to new file')
# Если файла нет, то создается новый и записывается информация
# Если файл есть, то он очищается и опят же записывается информация
a = 100 / 0
try:
    with open('output.txt', 'x') as y:
        y.write('more added data to new file')
except:
    print('This is error')

except ZeroDivisionError as err:
    print("Don't division by zero, guy", err)


print('I am still working')
