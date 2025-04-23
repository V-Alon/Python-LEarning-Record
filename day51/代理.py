#原理   通过第三方的机器去访问
import requests

#221.6.139.190: 9002

proxies = {
    'https': 'https://221.6.139.190'
}


resp=requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding='utf-8'
print(resp.text)