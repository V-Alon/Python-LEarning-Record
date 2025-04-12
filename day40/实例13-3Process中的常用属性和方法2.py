from multiprocessing import Process
import time,os
def sub_process(name):
    print(f'子进程PID{os.getpid()},父进程的PID{os.getppid()}，--------------------{name}')

    time.sleep(1)

def sub_process2(name):
    print(f'子进程PID{os.getpid()},父进程的PID{os.getppid()}，--------------------{name}')

    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始执行')
    for i in range(5):
        # 创建第一个子进程
        p1 = Process()#没有给定target参数，不会执行自己编写的函数的代码，会调用执行Process中的run方法
        # 创建第二个子进程
        p2 = Process()
        # 调用start()启动子进程
        p1.start()
        p2.start()
    print('主进程执行完毕了')
