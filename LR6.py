import threading
import time


def worker(num):
    time.sleep(5)  # просто ждем 5с
    print('Worker: %s' % num)


start_time = time.time()
print(start_time)
threads = []  # создается список для потоков
for i in range(5):  # создаем потоки
    t = threading.Thread(target=worker, args=(i, ))
    threads.append(t)

for t in threads:
    t.start()  # запускаем поток
    t.join()

# for t in threads:
#     t.join()  # запрещает другим потока идти дальше(основному тоже)

print('\n --- %s seconds ---' % (time.time()-start_time))  # выводим сколько времени потребовалось на их работу
