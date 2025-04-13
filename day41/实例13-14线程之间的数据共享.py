from threading import Thread
a=100
def add():
    print('加法线程开始执行')
    global a
    a+=30
    print(f'a的值为:{a}')
def sub():
    print('减法线程开始执行')
    global a
    a-=50
    print(f'a的值为:{a}')

if __name__ == '__main__':
    print(f'主线程开始执行')
    print(f'-----------全局变量a的值为:{a}')
    add=Thread(target=add)
    sub=Thread(target=sub)

    add.start()
    sub.start()

    add.join()
    sub.join()

    print('主线程执行完毕')