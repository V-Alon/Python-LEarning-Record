from multiprocessing import Queue
if __name__ == '__main__':
    #创建一个队列
    q=Queue(3)
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())

    q.put('hello')
    q.put('world')
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())

    q.put('mkk')
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())

    print(q.qsize())

    print(q.get())
    print(q.qsize())


    q.put_nowait('html')
    # q.put_nowait('ccc')
    print(q.qsize())


#遍历队列
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())


    print(q.empty())
    print(q.qsize())
