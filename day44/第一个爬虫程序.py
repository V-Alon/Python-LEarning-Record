from urllib.request import urlopen
url = 'http://www.baidu.com'
resp = urlopen(url)

with open('mybaidu.html',mode='w',encoding=('utf-8'))as f:
    f.write(resp.read().decode('utf-8'))#读取到的网页源代码
print('over!')
