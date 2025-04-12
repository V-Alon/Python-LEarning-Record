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
        p1 = Process(target=sub_process,args=('会赢吗',))#没有给定target参数，不会执行自己编写的函数的代码，会调用执行Process中的run方法
        # 创建第二个子进程
        p2 = Process(target=sub_process2,args=('yes,you can',))
        # 调用start()启动子进程

        p1.start()#没有指定参数,调用Process中的run方法
        p2.start()


        p1.terminate()
        p2.terminate()

    print('主进程执行完毕了')
