#isdigit十进制的所有数字
print('123'.isdigit())
print('一二三'.isdigit())
print('0b1001'.isdigit())
#isnumeric所有字符都是数字
print('123'.isnumeric())
print('一二三'.isnumeric())
print('0b1001'.isnumeric())
print('壹'.isnumeric())
#所有都是字母
print('hello你好'.isalpha())
print('hello123'.isalpha())
print('hello你好一二三'.isalpha())
#字母加数字
print('hello你好'.isalnum())
#大小写
print('HelloWorld'.islower())
print('helloworld'.islower())
print('helloworld你好'.islower())


print('HelloWorld'.isupper())
print('HELLOWORLD'.isupper())
print('HELLOWORLD你好'.isupper())


#首字母大写
print('HelloWorld'.istitle())
print('Hello World'.istitle())
print('helloworld'.istitle())

#判断是否是空白字符
print('-'*50)
print('\t'.isspace())
print(' '.isspace())
print('\n'.isspace())