#小说地址url
#https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}------>所以章节内容（昵称，cid）
#章节内部内容
#https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests,asyncio,aiohttp,json,aiofiles
'''
第一步访问:getCatalog 拿到所以章节的cid和内容
第二步访问:getChapterContent 下载所有文章的内容
'''




async def aiodownload(cid,b_id,title):
    data={
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data=json.dumps(data)
    url=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()
            #
            async with aiofiles.open(f'{title}.txt','wb') as f:
                await  f.write(dic['data']['novel']['content'])




async def getCatalog(url):
    resp = requests.get(url)
    dic=resp.json()
    tasks=[]

    for item in dic['data']['novel']['items']:#item对应每个章节的名称和cid
        title=item['title']
        cid=item['cid']
        tasks.append(aiodownload(cid,b_id,title))
        #每个cid都是一个url，，，异步任务
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    b_id="4306063500"
    url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))