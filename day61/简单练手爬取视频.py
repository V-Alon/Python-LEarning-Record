'''
流程
1拿到页面源代码
2此页面源代码提取m3u8的url
3下载m3u8
4读取m3u8文件，下载视频
5合并视频
'''
from dataclasses import replace

import requests,re
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
}
url='https://www.shitaiyun.com/vodplay/142305_1_1.html'

resp=requests.get(url,headers=headers)

# print(resp.text)
obj = re.compile( r'"url"\s*:\s*"(.+?)"', re.S)#用来提取m3u8的url地址

urls = re.findall(obj, resp.text)

if len(urls) >= 2: # 拿到m3u8的地址
    m3u8_url = urls[1].replace('\\', '')  # 处理转义字符
    print(m3u8_url)
    with open('梦魇绝镇.m3u8', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) >= 3:
            third_line = lines[2].strip()
            # print(third_line)#读取到爬到的m3u8文件的第三行的内容去替代原本的url的后半部分 得到新的url来进行爬取视频
            url_parts = m3u8_url.split('/')  # 将URL按'/'分割成多个部分
            for i, part in enumerate(url_parts):
                if part == "index.m3u8":
                    url_parts[i] = third_line  # 替换最后一部分

            # 重新组合成新的URL
            new_url = '/'.join(url_parts)#得到最总的url

            # print(new_url)




# #下载m3u8文件
#     resp2=requests.get(m3u8_url,headers=headers)
#     with open('梦魇绝镇.m3u8','wb') as f:
#         f.write(resp2.content)
#     resp2.close()
#     print('下载完毕')



    # #再次请求完整的m3u8文件
    # # https://v12.tlkqc.com/wjv12/202409/22/id67xBdyyt84/video/1000k_720/hls/index.m3u8
    # resp3=requests.get(new_url,headers=headers)
    # with open('梦魇绝镇（最终）.m3u8','wb') as f:
    #     f.write(resp3.content)
    # resp3.close()
    # print('得到最终的m3u8了')


    #解析m3u8文件，
    n=1
    with open('梦魇绝镇（最终）.m3u8','r',encoding='utf-8') as file:
        for line in file:
            line=line.strip()#处理，去掉空白，空格，换行符，
            if line.startswith('#'):
                continue
            # print(line)
            #下载视频片段
            resp3=requests.get(line)
            f=open(f'videos/{n}.ts',mode='wb')
            f.write(resp3.content)
            f.close()
            resp3.close()
            print(f'完成了第{n}个的下载!!!')
            n+=1


