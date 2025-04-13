from multiprocessing import Queue
import time
a=100
def write_msg(q):
    global a
    if  not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('a入队的值:',a)


def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队a的值:',q.get())

if __name__ == '__main__':
    