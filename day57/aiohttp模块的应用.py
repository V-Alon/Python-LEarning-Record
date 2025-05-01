#requests.get()同步的代码->异步操作
#引入模块   aiohttp
from asyncio import create_task
from venv import create

import aiohttp,asyncio
urls=[
    'https://umei.ojbkcdn.com/file/bizhi/20220927/5wn4old1jef.jpg',
    'https://umei.ojbkcdn.com/file/bizhi/20220927/ho1jgdsb2rx.jpg',
    'https://umei.ojbkcdn.com/file/bizhi/20220927/1egms1ivvke.jpg'
]


async def aiodownload(url):
    name=url.rsplit('/',1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #请求回来了
            with open(name,mode='wb')as f:
                f.write(await resp.content.read())  #读取内容是异步的需要挂起
    print(name,'完成')
    #s = aiohttp.ClientSession().get(url)#<----->相当于之前的requests模块     requests.session()
    #requests。get()    .post()
    #s.get()     .post()

    #发送请求
    #得到图片的内容
    #保存的到文件
async def main():
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    asyncio.run(main())