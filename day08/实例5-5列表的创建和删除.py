from itertools import count

lst=['hello','world',98,100.7]
print(lst)


lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

print(lst+lst2+lst3)
print(lst3*3)
print(len(lst3))
print(max(lst3))
print(min(lst3))
print(lst2.count('o'))
print(lst2.index('o'))
lst4=[10,20,30]
print(lst4)
del lst4
#print(lst4)#name 'lst4' is not defined，已经删除了lst4
'''
enumerate函数，，枚举
'''
