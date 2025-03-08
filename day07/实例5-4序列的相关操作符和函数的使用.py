s='helloworld'
print('e在helloworld中存在吗？',('e'in s))#T
print('e在helloworld中存在吗？',('v'in s))#F

print('e在helloworld中不存在吗？',('e' not in s))#F
print('e在helloworld中不存在吗？',('v' not in s))#T
#内置函数的使用
print('len',len(s))#10
#ASCII的最大值，最小值
print('max',max(s))
print('min',min(s))

#序列对象的使用方法
print('s.index()',s.index('o'))#o在s中第一次索引的位置
print('s.index()',s.index('l'))
print('s.count()',s.count('l'))
print('s.count()',s.count('o'))
