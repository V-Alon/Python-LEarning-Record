def turn(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32))#ord()将字母转换为Unicode码整数，加上32，char将整数码转换成字符
        elif 'a'<=item<='z':
            lst.append(chr(ord(item) - 32))
        else:
            lst.append(item)
    return ''.join(lst)


s=input('请输入一个字符串：')
new_s=turn(s)
print(new_s)
