# #python编写协程的程序
# import asyncio
#
# async def func():
#     print('hello world')
#
# if __name__ == '__main__':
#     g = func()  #此时的异步协程函数，此时函数执行得到的是一个协程对象
#     asyncio.run(g)#协程程序执行需要asyncio模块的支持
import asyncio
import time


async def func1():
    print('func1')
    # time.sleep(3)#程序出现同步操作的时候，异步就中断了
    await asyncio.sleep(3)#异步操作的代码
    print('func111')

async def func2():
    print('func2')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('func222')

async def func3():
    print('func3')
    # time.sleep(4)
    await asyncio.sleep(4)
    print('func333')

async def main():
    # f1 = func1()
    # await f1   第一种写法，await挂起操作放在协程对象前面
    #第二种写法
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [f1, f2, f3]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    t1=time.time()

    asyncio.run(main())
    t2=time.time()
    print(t2-t1)