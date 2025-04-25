#找到未加密的参数                               window.asrsea(参数，xxx，xxx)这个方法加密
#想办法把参数进行加密（模仿加密方式），params->bYE2x.encText   enSecKey->bYE2x.encSecKey
#q请求网易，拿到数据
#安装加密模块
from Crypto.Cipher import AES
from base64 import b64encode
import requests,json
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



#服务于d

f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

g="0CoJUm6Qyw8W8jud"
e="010001"
i="cxToWzewSnjLkgFF"   #手动固定的i，原网页中i是变化的随机的，i固定，ensecText就是固定的，c()函数就是固定的
def get_encSecKey():
    return "df64522bb8abc80a6ee9b73fa8ce51fb1c759d76b67c3f3fc99cb9b62a5c23bd9b4182d4cb9bafe7e9f5c4e8d6a70159fe1f2255e0c41f98e51298bf89d285998e746f846c8d6daa9c2af8e6ed7a4671af0b1f0a93f69f4caaf642020bf6955009327e333ecaddc61207e3913bf46b44b4c9cb7895fb954862e4fd6d2286603b"

#把参数进行加密
def get_params(data):#默认收到字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second#返回的就是params

#转化成16的倍数，为下方的加密算法做准备
def to_16(data):
    pad = 16 - len(data)%16
    data += chr(pad) * pad
    return data
def enc_params(data,key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))#内容长度为16的倍数
    return str(b64encode(bs),"utf-8")#转换成字符串返回


#处理加密过程在 ------->加密方式.txt
params=('6ZI6srR0zgTwQm3TzK9sMz6ineYDHpbzFDPtWNL/A8ybu7lY/3kj5ezya9lqrid3Ide'
        'zLR2Rlg/zTUULcGZsEKw+WzvxTUp/BU8rzikRyJjgZjtU9rFtjvLOCPOIhFP2W0R3k9lAxqgDbvdFANk4K3q+'
        'GylNvLrHcHssqZ9QszCTOUsrSsyVK/9FwITgHHxrin/gZJY1t8ZYB30wj7oed7LxCjZLi/nkPn5h7Bf+6E2uND1O'
        'KdMcHcmnyX4uRvX3HjSx56QG4zwbkDlMosNuM4j1Tdf9CS3UJNTM4RWfEuc=')


#发送请求得到结果
resp = requests.post(url,data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})
print(resp.text)