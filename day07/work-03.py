#输出九九乘法表
for i in range(1,10):#一共9行9列，输出左下角
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()#换行
