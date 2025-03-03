#倒三角形
for i in range(1,6):
    for j in range(1,7-i):
        print("*", end='')
    print()  # 空的输出用来换行
print("-"*20)
#等腰三角形
for i in range(1,6):#外层循环五行
    for j in range(1,6-i):
        print(" ", end='')
    for z in range(1,2*i):
        print("*", end='')
    print()