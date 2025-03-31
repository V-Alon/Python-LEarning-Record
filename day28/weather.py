import requests
import re

def get_html():
    url = 'https://www.weather.com.cn/weather1d/101110101.shtml'  # 爬虫打开的浏览器上的网页
    resp = requests.get(url)  # 打开浏览器并且打开网址
    # 设置编码格式
    resp.encoding = 'utf-8'
    return resp.text

def parse_html(html_str):
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd=re.findall('<span class="wd">(.*)</span>',html_str)
    zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str)

    lst=[]
    for a, b, c, d in zip(city, weather, wd, zs):
        lst.append([a, b, c, d])
    return lst
#<span class="name">三亚</span>

# print(city)
# print(weather)
# print(wd)
# print(zs)

'''
<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">18/27℃</span>
<span class="zs">适宜</span>
'''