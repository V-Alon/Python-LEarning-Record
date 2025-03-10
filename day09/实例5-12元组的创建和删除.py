#
t=('hello',[10,20,30],'python','world')
print(t)
#创建元组的方式
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在',(10 in t))
print(10 not in t)
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
print(t.index(10))
print(t.count(10))

y=(10,)
print(y,type(y))

#删除
# del t
# print(t,type(t))#name 't' is not defined