lst=[
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','小米',800]
]
print('编号\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print('\n')
#格式化操作
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{0:.2f}'.format(item[3])
print('编号\t\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print('\n')