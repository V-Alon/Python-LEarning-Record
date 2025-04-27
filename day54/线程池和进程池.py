from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
#线程池：一次性开辟一些线程，用户直接给线程池提交任务，线程任务的调度交给线程池完成
#   50  100000
def fn(name):
    for i in range(1000):
        print(name,i)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(100):
            t.submit(fn,name=f'线程{i}')

    #等待线程池中的任务全部执行完毕，才继续执行（守护）
    print('123!!!')
#进程池：