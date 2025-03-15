s='helloworld'
#字符串的替换
new_s=s.replace('o','你好',1)
print(new_s)


#宽度范围居中
print(s.center(20))
print(s.center(20,'*'))


#去掉字符串的空格
s='     hello     world     '
print(s.strip())#去掉左右两侧空格
print(s.lstrip())#只去掉左侧
print(s.rstrip())#只去掉右侧


#去掉指定的字符
s3='dl-helloworld'
print(s3.strip('ld'))#去掉两侧的‘dl’
print(s3.lstrip('ld'))#去掉左侧的‘dl’
print(s3.rstrip('ld'))#去掉右侧的‘dl’
