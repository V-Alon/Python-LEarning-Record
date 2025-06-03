d={'hello':10,'world':20,'python':30}
#访问字典中元素
#1》使用d[key]
print(d['hello'])
#2，day86.get()
print(d.get('hello'))#二者之间有区别，如果key不存在，day86[key]报错，day86.get[key]可以指定默认值
# print(day86['java'])
print(d.get('java'))#None
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item)
#在使用for循环时，分别获key和value
for key,value in d.items():
    print(key,"-->",value)