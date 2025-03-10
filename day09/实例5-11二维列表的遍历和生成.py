lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)
#遍历，双重for
for row in lst:#行
    for item in row:#列
        print(item,end='\t')
    print()#换行


#列表生成式
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)
for row in lst2:
    for item in row:
        print(item,end='\t')
    print()