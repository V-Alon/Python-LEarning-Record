'''
format(value,format_spec)将value以format_spec的格式进行显示
len(s)获取s的长度或者s元素的个数
id(obj)获取对象的内存地址
type(x)获取x的数据类型
eval(s)执s的字符串所表示的代码
'''
#format()
print(format(3.14,'20'))
print(format('hello','20'))
print(format('hello','*<20'))
print(format('hello','*>20'))
print(format(3.1415926,'2f'))
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'x'))
print('_'*50)
print(len('hello'))

print('_'*50)
print(id(10))
print(id('hello'))
print(type(10))
print(type('hello'))




print('_'*50)
print(eval('3.1415926'))
print(eval('10+20'))