import re

from fontTools.misc.cython import returns

# #findall：匹配字符串中所有符合正则的内容
# lst=re.findall(r"\d+",'我的电话号是10086,我好朋友的电话是10010')
# print(lst)
#
# #finditer：匹配字符串中的所有内容（返回的是迭代器）,从迭代器中拿到内容需要i.group()
# it = re.finditer(r"\d+",'我的电话号是10086,我好朋友的电话是10010')
# for i in it:
#     print(i.group())

# #search找到一个结果就返回，返回的结果是match结果，拿数据需要.group()
# s=re.search(r"\d+",'我的电话号是10086,我好朋友的电话是10010')
# print(s.group())

#
# #match从头开始匹配
# s=re.match(r"\d+",'我的电话号是10086,我好朋友的电话是10010')
# print(s.group())

# #预加载正则表达式
# obj=re.compile(r'\d+')
#
# ret=obj.finditer('我的电话号是10086,我好朋友的电话是10010')
# for i in ret:
#     print(i.group())


s="""
<div class='jay'><span id='1'>壹</span></div>
<div class='jj'><span id='2'>贰</span></div>
<div class='jilin'><span id='3'>叁</span></div>
<div class='sylar'><span id='4'>肆</span></div>
<div class='troy'><span id='5'>伍</span></div>
"""

#re.S的作用是让.能匹配 换行符
#(?P<a>.*?)  引用捕获组   ?P<name>可以从正匹配的内容进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<a>.*?)</span></div>",re.S)

result=obj.finditer(s)
for i in result:
    print(i.group('a'))