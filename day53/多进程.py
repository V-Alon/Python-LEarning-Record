import time
from multiprocessing import Process


def func():
    for i in range(1000):
        print('子进程',i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    for i in range(1000):
        print('主进程',i)
        time.sleep(0.01)