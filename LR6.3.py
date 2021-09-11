import threading
import time
import logging

start_time = time.time()


def worker():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.info('Exiting')


def my_service():
    logging.error('Starting')
    time.sleep(0.3)
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)
threads = list()
threads.append(t)
threads.append(w)
threads.append(w2)

for i in threads:
    i.start()
    # i.join()

for i in threads:
    i.join()
#
# w3 = worker()

print('\n --- %s seconds ---' % (time.time()-start_time))
