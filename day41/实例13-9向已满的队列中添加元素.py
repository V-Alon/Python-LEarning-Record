from multiprocessing import Queue
if __name__ == '__main__':
    q = Queue(3)
    #入队
    q.put(1)
    q.put(2)
    q.put(3)

    q.put(4)