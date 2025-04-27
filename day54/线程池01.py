#如何提取单页数据
#上线程池，多个页面同时抓取
import requests,csv
from lxml import etree
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

from day46.豆瓣top250 import csv_writer
f=open('datacsv.csv',mode='w',encoding='utf-8')
csvwriter=csv.writer(f)


def download_one_page(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    html=etree.HTML(resp.text)
    table=html.xpath('/html/body/div[3]/table')[0]
    trs=table.xpath('./tr')#/html/body/div[3]/table/tbody/tr[1]
    for tr in trs:
        txt=tr.xpath('./td/text()')
        txt=(item.replace('\\','').replace('/','') for item in txt)
        csvwriter.writerow(txt)


if __name__ == '__main__':

    # for i in range(1,14870):
    #     download_one_page(f'http://www.shucai123.com/price/{i}.html')
    with ThreadPoolExecutor(max_workers=50) as t:
        for i in range(1, 200):
            t.submit(download_one_page,f'http://news.163.com/news?page={i}')