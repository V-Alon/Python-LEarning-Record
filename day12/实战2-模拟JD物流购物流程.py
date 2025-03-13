#创建一个空列表
from sys import flags

lst=[]
for i in range(5):
    goods=input('请输入商品编号和名称，进行商品入库，每次只能输入一个：')
    lst.append(goods)
#输出所有商品信息
for item in lst:
    print(item)

#创建一个空列表，用来存储购物车内的物品
cart=[]
while True:
    flag=False#代表没有商品的情况
    num=input('请输入需要的商品编号：')
    #遍历商品列表，查询要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:#切片操作，从商品中切出序号
            flag=True
            cart.append(item)
            print('添加成功')
            break
    if not flag and num !='q':
        print('商品不存在')

    if num=='q':
        break
print('-'*50)
print('您购物车内已添加的商品有：')
cart.reverse()
for item in cart:
    print(item)
