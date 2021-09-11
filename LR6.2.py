import threading
import time

start_time = time.time()


def worker():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Exiting')


def my_service():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Exiting')


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)
threads = list()
threads.append(t)
threads.append(w)
threads.append(w2)

for i in threads:
    i.start()
#     i.join()

for i in threads:
    i.join()

# w3 = worker()

print('\n --- %s seconds ---' % (time.time()-start_time))

