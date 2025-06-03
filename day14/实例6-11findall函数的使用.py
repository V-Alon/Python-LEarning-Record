import re
pattern='\\day86\\.\\day86+'
s='I study python 3.12 everday 2.7'#待匹配字符串
s2='4.10 python I study everday'
s3='I study python everday'
lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)
print(lst)
print(lst2)
print(lst3)