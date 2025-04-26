# #线程
# #进程进程是资源单位，每一个进程至少要有一个线程
# #线程是执行单位
# def func():
#     for i in range(1000):
#         print('func',i)
# if __name__ == '__main__':
#     func()
#     for i in range(1000):
#         print('main',i)
import threading


#多线程
# from threading import *#线程类
# def func():
#     for i in range(1000):
#         print('func',i)
#
#
# if __name__ == '__main__':
#     t=Thread(target=func)
#     t.start()#开始执行线程，多线程，状态为可以开始工作，具体执行时间由CPU决定
#
#     for i in range(1000):
#         print('main',i)





class MyThread(threading.Thread):
    def run(self):  #固定的，当线程被执行时，被执行的就是run（）
        for i in range(100):
            print('子线程',i)


if __name__ == '__main__':
    t = MyThread()
    # t.run()#方法的调用，，，->单线程？？？
    t.start()#开启线程
    for i in range(100):
        print('主线程',i)
