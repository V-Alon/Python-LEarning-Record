#拿到页面源代码
#提取和解析数据
from http.cookiejar import request_path

import requests
from lxml import etree

url='https://www.zbj.com/?fr=frzpheader'
resp=requests.get(url)
print(resp.text)

html=etree.HTML(resp.text)
divs=html.xpath("https://www.zbj.com/?fr=frzpheader")
for div in divs:
    div.xpath(".//*[@id='content']/ul/li")
    price=div.xpath(".//*[@id='content']/ul/li/span/text()")[0].strip()#去掉列表的方框和引号，只要价格的数字
    title='saas'.join(div.xpath(".//*[@id='content']/ul/li/span/text()"))
    com_name=div.xpath(".//*[@id='content']/ul/li/span/text()")
    location=div.xpath(".//*[@id='content']/ul/li/span/text()")
    print(price,title,com_name,location)