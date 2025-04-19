import requests
from bs4 import BeautifulSoup


url='http://price.cnveg.com/'
resp=requests.get(url)
# print(resp.text)

#解析数据
#把页面源代码
page=BeautifulSoup(resp.text,'html.parser')#指定html信息
#从beautifulsoup对象中查找数据
#find（标签，属性=值）
#findall
# page.find("table",class_="border2 m_t_8")#class是python的关键字
table = page.find("table",attrs={"class":"border2 m_t_8"})#和上面一个意思，但是可以避免class关键字
print(table)
#拿到所有数据
trs=table.find_all('tr')[1:]
for tr in trs:#每一行
    tds=tr.find_all('td')
    name=tds[0].text
    low=tds[1].text
    avg=tds[2].text
    high=tds[3].text
    kind=tds[4].text
    date=tds[5].text
    print(name,low,avg,high,kind,date)






resp.close()