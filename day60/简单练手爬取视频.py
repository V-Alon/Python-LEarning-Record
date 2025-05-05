'''
流程
1拿到页面源代码
2此页面源代码提取m3u8的url
3下载m3u8
4读取m3u8文件，下载视频
5合并视频
'''

import requests,re
url='https://www.shitaiyun.com/vodplay/142305_1_1.html'

resp=requests.get(url)

# print(resp.text)
obj = re.compile( r'"url"\s*:\s*"(.+?)"', re.S)#用来提取m3u8的url地址

urls = re.findall(obj, resp.text)

if len(urls) >= 2: # 拿到m3u8的地址
    m3u8_url = urls[1].replace('\\', '')  # 处理转义字符
    print(m3u8_url)


