t=('python','hello','world')
print(t[0])
t2=t[0:3:2]#元组支持切片
print(t2)

#元租的遍历
for item in t:
    print(item)

#索引for加上range（）len()
for i in range(0,len(t)):
    print(i,t[i])

#使用enumerate()
for index,iten in enumerate(t,start=1):
    print(index,"-->",iten)