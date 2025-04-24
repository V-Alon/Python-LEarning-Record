#找到未加密的参数                               window.asrsea(参数，xxx，xxx)这个方法加密
#想办法把参数进行加密（模仿加密方式），params->bYE2x.encText   enSecKey->bYE2x.encSecKey
#q请求网易，拿到数据
url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
#请求方式是post
data={
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}



e='01001'

f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'

g='0CoJUm6Qyw8W8jud'

def get_encSecKey():
    pass
#处理加密过程
params=('6ZI6srR0zgTwQm3TzK9sMz6ineYDHpbzFDPtWNL/A8ybu7lY/3kj5ezya9lqrid3Ide'
        'zLR2Rlg/zTUULcGZsEKw+WzvxTUp/BU8rzikRyJjgZjtU9rFtjvLOCPOIhFP2W0R3k9lAxqgDbvdFANk4K3q+'
        'GylNvLrHcHssqZ9QszCTOUsrSsyVK/9FwITgHHxrin/gZJY1t8ZYB30wj7oed7LxCjZLi/nkPn5h7Bf+6E2uND1O'
        'KdMcHcmnyX4uRvX3HjSx56QG4zwbkDlMosNuM4j1Tdf9CS3UJNTM4RWfEuc=')
import requests


resp=requests.post(url)
print(resp.text)