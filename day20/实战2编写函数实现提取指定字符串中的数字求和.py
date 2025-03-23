def get_digit(x):
    s=0
    lst=[]
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    #求和
    s=sum(lst)
    return s,lst

s=input('请输入一个字符串：')

lst,x=get_digit(s)
print('提取的数字',lst)
print('累加和为',x)
