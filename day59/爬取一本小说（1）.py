import requests
import asyncio
import aiohttp
import json
import aiofiles

async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data_json = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data_json}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            if 'data' in dic and 'novel' in dic['data'] and 'content' in dic['data']['novel']:
                async with aiofiles.open(f'{title}.txt', 'w', encoding='utf-8') as f:
                    await f.write(dic['data']['novel']['content'])
            else:
                print(f"Failed to download chapter: {title}")

async def getCatalog(url):
    # 使用 aiohttp 发送异步请求获取章节列表
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            tasks = []
            for item in dic['data']['novel']['items']:  # 假设这里正确获取到章节信息
                title = item['title']
                cid = item['cid']
                tasks.append(aiodownload(cid, b_id, title))
            await asyncio.gather(*tasks)  # 使用 asyncio.gather 来运行所有异步任务

if __name__ == '__main__':
    b_id = "4306063500"
    data = {"book_id": b_id}
    data_json = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getCatalog?data={data_json}"
    asyncio.run(getCatalog(url))