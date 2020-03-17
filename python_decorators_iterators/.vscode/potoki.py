import threading
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import time

def roman():
    x = 0.01
    while x <=1:
        x = x * 1.00000001
    print(f'x is {x}')


def in_processing():
    t1 = Process(target=roman)
    t2 = Process(target=roman)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    for _ in range(2):
        start = time.time()
        roman()
        print(time.time() - start)

    start = time.time()
    in_processing()
    print(time.time() - start) 
