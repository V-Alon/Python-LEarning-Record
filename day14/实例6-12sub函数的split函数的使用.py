import re
pattern = '黑客|破解|反爬'
s='我想学习python，想破解一些VIP视频，python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://cn.bing.com/search?q=ysj&qs=n&form=QBRE&sp'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)