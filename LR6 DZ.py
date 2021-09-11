import threading
import time
import logging

class Reading:
    def __init__(self):
        self.regim = int(input(' Введите режим: 1 - Простой сбор списка '
                           '2 - сбор списка при помощи многопоточности'
                           ' 3 - сбор словаря '))  # задается режим работы с клавиатуры
        with open('inLR6', 'r', encoding='utf8') as inList:
            self.inData = inList.readlines()
            if self.regim > 1:
                self.colThreads = int(input('Введите кол-во потоков '))
        self.outList = []
        self.outDict = dict()

    def justList(self, data):  # Метод который просто записывет данные из файла в список
        # В списке каждая строка -это [Id,Ф, И, О]
        # print('start')
        # time.sleep(0)
        outList = list()
        for line in data:
            outList.append(line.split())
            self.outList.extend(line.split())
        # print(outList)
        logging.info(outList)

    def multList(self):
        argThread = list()
        threads = list()
        i = 0
        j = 0
        while i < len(self.inData):
            while i - j < len(self.inData) / self.colThreads:
                argThread.append(self.inData[i])
                i += 1
            j = i
            t = threading.Thread(target=self.justList, args=(argThread,))
            threads.append(t)
            argThread = list()
        for i in threads:
            i.start()

    def justDict(self, data):
        outDict = dict()
        for i in data:
            line = i.split()
            k = line[0]
            val = [line[i] for i in range(1, len(line))]
            outDict[k] = val
            self.outDict[k] = val
        logging.info(outDict)

    def multDict(self):
        with open('outLR6', 'w', encoding='utf8') as outList:
            for line in self.inData:
                print(line.rstrip(), file=outList)
        argThread = list()
        threads = list()
        i = 0
        j = 0
        while i < len(self.inData):
            while i - j < len(self.inData) / self.colThreads:
                argThread.append(self.inData[i])
                i += 1
            j = i
            t = threading.Thread(target=self.justDict, args=(argThread,))
            threads.append(t)
            argThread = list()
        for i in threads:
            i.start()

    def run(self):
        if self.regim == 1:
            self.justList(self.inData)
        elif self.regim == 2:
            self.multList()
        elif self.regim == 3:
            self.multDict()


logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
        # return outList

one = Reading()
one.run()
print(one.outDict)
print(one.outList)

def readData(inData, numStolb):
    outList = []
    for line in inData:
        outList.append(line.split()[numStolb])
    logging.info(outList)


with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы/KZonBus1.dat') as inFile:
    for i in range(1, 5):
        threads = []
        outData = []
        t = threading.Thread(target=readData, args=(inFile, i))
        threads.append(t)
for t in threads:
    logging.info(print(threading.current_thread().getName(), 'Starting'))
    t.start()

for i in threads:
    t.join()