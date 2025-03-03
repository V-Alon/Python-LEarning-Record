row=eval(input('请输入菱形的行数'))
while row%2==0:
    print('重新输入行数')
    row=eval(input(' 请输入菱形的行数'))

#输出菱形
top_row=(row+1)//2
#上半部分
for i in range(1,top_row+1):#外层循环五行
    for j in range(1,top_row+1-i):
        print(" ", end='')
    for z in range(1,2*i):
        print("*", end='')
    print()
#下半部分
bottom_row=(row)//2
    #直角三角形
for i in range(1,bottom_row+1):#外循环
    for j in range(1,i+1):
        print("=", end='')
    for z in range(1,bottom_row*2-2*i+2):
        print("*", end='')
    print()