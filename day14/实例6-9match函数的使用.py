import re#导入
from turtledemo.penrose import start

pattern='\\d\\.\\d+'#限定符,0-9数字出现1次或者多次’
s='I study python 3.12 everday'#待匹配字符串
match=re.match(pattern,s,re.I)
print(match)
s2='3.12 python I study everday'
match2=re.match(pattern,s2)
print(match2)#<re.Match object; span=(0, 4), match='3.12'>
print('匹配值得起始位置',match2.start())
print('匹配值得结束位置',match2.end())
print('匹配区间的位置元素',match2.span())
print('待匹配的字符串',match2.string)
print('待匹配的数据',match2.group())