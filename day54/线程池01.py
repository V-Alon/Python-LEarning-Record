#如何提取单页数据
#上线程池，多个页面同时抓取
import requests
from lxml import etree




def download_one_page(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=etree.HTML(resp.text)
    table=html.xpath('/html/body/div[3]/table')[0]
    trs=table.xpath('./tr')#/html/body/div[3]/table/tbody/tr[1]
    for tr in trs:
        txt=tr.xpath('./td/text()')
        print(txt)


if __name__ == '__main__':
    download_one_page('http://www.shucai123.com/price/')