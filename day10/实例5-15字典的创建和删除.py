d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)#key相同value进行覆盖

#zip 函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)#
print(zipobj)#<zip object at 0x000001B24BED3FC0>
# print(list(zipobj))#[(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d=dict(zipobj)
print(d)#{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

#使用参数创建字典
d=dict(cat=10,dog=20)#cat是key,10 是value
print(d)



t=(10,20,30)
print({t:10})

# lst=[10,20,30]#unhashable type: 'list'
# print({lst:10})
#字典属于序列
print('min',min(d))
print('max',max(d))
print('len',len(d))

#删除
del d
#








