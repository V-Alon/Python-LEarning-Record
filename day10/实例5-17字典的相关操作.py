d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)
#向字典中添加元素
d[1004]='张丽丽'#直接赋值
print(d)
#获取字典中所有的key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中使用value
values=d.values()
print(values)
print(list(values))
print(tuple(values))
#将字典中数据转为key-value的形式，以元租的方式
lst=list(d.items())
print(lst)

#
# day86=dict()
# print(day86)

#使用pop（）
print(d.pop(1001))
print(d)
#删除不存在的值
print(d.pop(1008,'不存在'))
print(d)
#随机删除
print(d.popitem())
print(d)
#删除字典中所有元素
d.clear()
print(d)
#python中一切皆对象
print(bool(d))