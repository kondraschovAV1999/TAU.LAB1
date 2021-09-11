import logging
import random
import threading
import time

time_start = time.time()


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Watting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value += 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)
counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args = (counter, ))
    t.start()

logging.debug('Wating for worker threads')
main_thread = threading.main_thread()
for i in threading.enumerate():
    if i is not main_thread:
        i.join()
logging.debug('Counter %d', counter.value)
print('\n --- %s seconds ---' % (time.time()-time_start))
