#JSON模块
import json
lst=[
    {'name':'mkk','age':19,'score':100},
    {'name':'xxx','age':20,'score':99},
    {'name':'vvv','age':22,'score':98},
]
#使用dumps
s=json.dumps(lst,ensure_ascii=False,indent=4)

