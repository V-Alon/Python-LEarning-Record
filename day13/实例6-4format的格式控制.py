s='helloworld'
print('{0:*<20}'.format(s))#字符串的显示宽度为20，左对齐，空白部分使用*号填充
print(len(s))#使用了10个*号
print('{0:*>20}'.format(s))#左填充
print('{0:*^20}'.format(s))#右填充


#居中对齐
print(s.center(20,'*'))


#千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.12345))


#浮点数小数部分的精度
print('{0:.2f}'.format(1.2345456))

#字符串类型 . 表示最大的显示长度
print('{0:.5}'.format('helloworld'))#最大显示长度为5


#整合类型
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))
#浮点数类型
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))