#拿到页面源代码
#提取和解析数据
import requests
from lxml import etree

url='https://www.zbj.com/?fr=frzpheader'
resp=requests.get(url)
print(resp.text)

html=etree.HTML(resp.text)