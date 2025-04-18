#拿到页面源代码     requests
#通过re来提取需要的信息    re
import re, requests,csv
url='https://movie.douban.com/top250'
headers = {'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'}
resp=requests.get(url,headers=headers)
page_content=resp.text
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
               r'</span>.*?<p>.*?<br>(?P<year>.*?)&nbsp.*?'
               r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
               r'<span>(?P<num>.*?)人评价</span>',re.S)
#开始匹配
result=obj.finditer(page_content)
f=open('top250.csv','w',encoding='utf-8')
csv_writer=csv.writer(f)
for item in result:
    # print(item.group('name'))
    # print(item.group('year').strip())
    # print(item.group('score').strip())
    # print(item.group('num').strip()+'人评价')
    dic= item.groupdict()
    dic['year']=dic['year'].strip()
    csv_writer.writerow(dic.values())
f.close()
print('done')
resp.close()