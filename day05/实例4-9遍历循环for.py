#遍历字符串
for i in 'hello':
    print(i)
    #range函数，产生一个[n,m)的正数数列，包含n，不包含m
for i in range(0,11):
    #print(i)
    if i % 2 == 0:
        print(i,'i是偶数')
#计算一到十累加
s=0
for i in range(1,11):
    s+=i#相当于s+i=s
print("一到十累加和为",s)
print('---100到999之间的水仙花数---')
"""
153=3*3*3+5*5*5+1*1*1
"""
for i in range(100,1000):#1533
    sd=i%10#获取个位上数字
    tens=i//10%10
    hs=i//100
    if sd**3+tens**3+hs**3:
        print(i)
    print('水仙花数是',)