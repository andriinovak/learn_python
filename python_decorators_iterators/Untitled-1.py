from urllib.request import urlretrieve
import os

file_url = 'https://www.overclockers.ua/peripheral/razer-basilisk-x-hyperspeed/01-razer-basilisk-x-hyperspeed.jpg'


def download_file(url):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = 'panda.jpg'
    urlretrieve(url, os.path.join(dir_path, filename))


import random
import time

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool


def test1():
    print("for loop with no multiproc: ")
    m = 10000000
    t = time.time()
    for i in range(m):
        pick = random.choice(['on', 'off', 'both'])
    print(time.time() - t)

def test2():
    print("map with no multiproc: ")
    m = 10000000
    t = time.time()
    map(lambda x: random.choice(['on', 'off', 'both']), range(m))
    print(time.time() - t)


def rdc(x):
    return random.choice(['on', 'off', 'both'])


def test3():

    pool = Pool(processes=4)
    m = 10000000

    print("map with multiproc: ")
    t = time.time()

    r = pool.map(rdc, range(m))
    print(time.time() - t)


def test4():

    pool = ThreadPool(processes=4)
    m = 10000000

    print("map with multithread: ")
    t = time.time()

    r = pool.map(rdc, range(m))
    print (time.time() - t)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
