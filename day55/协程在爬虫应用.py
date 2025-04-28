import asyncio


async def download(url):
    print('开始下载')
    await asyncio.sleep(1)#网络请求
    print('下载完成')


async def main():
    urls=[
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://www.pdd.com/',
        'https://www.jd.com/',
        'https://www.163.com',
    ]

