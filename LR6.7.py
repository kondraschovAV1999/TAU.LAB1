from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)
future = pool.submit(return_after_5_secs, ('Hello'))
print(future.done())
# sleep(5)
print(future.done())
print(future.result())
# ДЗ в moodle в ВЫЧ.КОМплексы ЛР по потоковым процессам надо сделать первые 4 пункта
