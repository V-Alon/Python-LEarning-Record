import requests,re
from prompt_toolkit.filters import has_validation_error

url='https://www.bqgyy.net/book/4708/1254324_2.html'
# GET
# <article id="article" class="content"    </article>   标签
# print(rsp.text)
headers={
# <a id="next_url" href="/book/4708/1254328.html">下一章 <i class="fa fa-forward"></i></a>
#     href="/book/4708/1254328.html
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'

}

resp=requests.get(url,headers=headers)
print(resp.text)

