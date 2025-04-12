from multiprocessing import Process
import time,os
class MyProcess(Process):
    #
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print(f'子进程的名称{self.name},PID:{os.getpid()},父进程的PID:{os.getppid()}')

if __name__ == '__main__':
    print('父进程开始执行')
    lst=[]
    for i in range(1,6):
        p1=MyProcess(f'进程:{i}')
        p1.start()
        lst.append(p1)

    for item in lst:
        item.join()

    print('父进程执行完毕')