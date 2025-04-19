import re,requests,csv
import urllib3

urllib3.disable_warnings()

#定位到2025必看热片
#从2025必看片提取到子页面的链接地址
#请求子页面的链接地址，拿到我们想要的下载地址
domain='https://www.dytt8899.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
    'Cookie': 'UM_distinctid=1964936cd36541-0af3fc2a0f17568-4c657b58-144000-1964936cd3714e5; CNZZDATA1281410151=734299588-1744985050-%7C1745042718'
}
resp=requests.get(domain,verify=False,headers=headers,timeout=5)
#verify=False 去掉安全验证
resp.encoding='gb2312'#指定字符集
# print(resp.text)
obj1=re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?'
                r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1=obj1.finditer(resp.text)

child_herf_lst=[]
for i in result1:
    ul=i.group('ul')
    #拿到ul的值
    result2=obj2.finditer(ul)
    for j in result2:
        #拼接子页面链接  域名加上子页面链接
        child_href=domain+j.group('href').strip('/')
        child_herf_lst.append(child_href)
        # print(j.group('href'))

#提取子页面内容
for href in child_herf_lst:
    child_resp=requests.get(href,verify=False,headers=headers,timeout=5)
    child_resp.encoding='gbk'
    result3=obj3.search(child_resp.text)
    print(result3.group('movie'))
    print(result3.group('download'))

resp.close()