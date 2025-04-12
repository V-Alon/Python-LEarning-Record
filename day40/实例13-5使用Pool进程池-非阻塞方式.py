from multiprocessing import Pool
import time,os
def task(name):
    print(f'子进程的PID:{os.getpid()}，执行的任务:{name}')
    time.sleep(1)

if __name__ == '__main__':
    #主进程
    start = time.time()
    print('父进程开始执行')
    p=Pool(3)
    #创建任务
    for i in range(10):
        p.apply_async(func=task,args=(i,))

    p.close()
    p.join()#阻塞
    print('所有子进程执行完毕，父进程执行完毕')
    print(time.time()-start)