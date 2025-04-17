#安装requests模块
#pip install requests
import requests

query=input('输入喜欢的明星:')
url=f'https://www.sogou.com/web?query={query}'

dic={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'}
resp=requests.get(url, headers=dic)#处理反爬
print(resp)
print(resp.text)#拿到页面源代码