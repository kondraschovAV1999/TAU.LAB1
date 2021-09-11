import threading


def readData(bigMass, inData, numStolb):
    outList = []
    for line in inData:
        outList.append(line.strip().split()[numStolb])
    bigMass[numStolb-1].extend(outList)


with open('D:\Учеба\Вычислительные комплекслы в электроэнергетике\Лабораторны работы/KZonBus1.dat') as inFile:
    inData = inFile.readlines()
threads = []
outData = [[], [], [], []]
for i in range(1, 5):
    t = threading.Thread(target=readData, args=(outData, inData, i))
    threads.append(t)

for t in threads:
    t.start()
    print(t.getName(), 'Starting')

for i in threads:
    i.join()

for k in outData:
    print(len(k))
    # for n in range(3):
    #     print(k[n], end=' ')

print(len(outData))
