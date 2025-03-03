#三行四列
for i in range(1,4):#行数外循环
    for j in range(1,5):#列数内循环
        print("*",end='')
    print()#空的输出用来换行
print('-'*20)
#直角三角形
for i in range(1,6):#行数外循环
    for j in range(1,i+1):#列数内循环
        print("*",end='')
    print()#空的输出用来换行