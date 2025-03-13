s1='HelloWorld'
new_s2=s1.lower()
print(s1,new_s2)

new_s3=s1.upper()
print(s1,new_s3)

#字符串的分割
e_mail='mkk@163.com'
lst=e_mail.split('@')
print('邮件名',lst[0],'邮件服务器域名',lst[1])

#
print(s1.count('o'))

#检索
print(s1.find('o'))
print(s1.find('p'))

print(s1.index('o'))
#print(s1.index('p'))#ValueError: substring not found子串没有找到
#find没找到返回-1，index没有找到报错

#判断前缀后缀
print('demo.py'.endswith('.py'))#True
print('text.txt'.endswith('.txt'))#True
print(s1.startswith('H'))
print(s1.startswith('p'))