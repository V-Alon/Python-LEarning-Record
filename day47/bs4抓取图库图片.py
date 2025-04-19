#拿到主页面的源代码，然后提取子页面的链接地址，href
#通过href拿到子页面的内容，从子页面中找到图片的下载地址


import requests,time
from bs4 import BeautifulSoup
from jinja2.async_utils import auto_to_list

url='http://umei.cc/bizhitupian/weimeibizhi/'
resp=requests.get(url)
resp.encoding='utf-8'

main_page=BeautifulSoup(resp.text,'html.parser')
alist=main_page.find("div",attrs={"class":"TypeList"}).find_all('a')
print(alist)
for a in alist:
    href=(a.get('href'))#直接头href拿到
    #拿到子页面的源代码
    child_page_resp=requests.get(href)
    child_page_resp.encoding='utf-8'
    child_page_text=child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page=BeautifulSoup(child_page_text,'html.parser')
    p=child_page.find("p",align="center")
    img=p.find("img")
    src=img.get('src')
    #下载图片
    img_resp=requests.get(src)
    # img_resp.content
    img_name=src.split('/')[-1]
    with open(img_name,mode='wb') as f:
        f.write(img_resp.content)#图片内容保存到文件

    print('over',img_name)
    time.sleep(1)

resp.close()