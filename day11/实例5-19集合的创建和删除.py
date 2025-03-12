#使用{}进行创建集合
s={10,20,30,40}
print(s)

#结集合当中只能存储不可变数据类型
# s={[10,20],[30,40]}#unhashable type: 'list'
# print(s)
#set 创建集合
s=set()#空集合布尔值是False
print(s)
s={}#是集合还是字典
print(s,type(s))
s=set('helloworld')
print(s)#无序的，不重复的

s2=set([10,20,30])
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列的一种
print(max(s3))
print(min(s3))
print(len(s3))

print('9在集合中存在吗',9 in s3)
print('9在集合中不存在吗',9 not in s3)

# del s3
# print(s3)