'''
sorted(iter)对可迭代对象进行排序
reversed(sequence)反转序列生成新的迭代器对象
zip(iter1, iter2)将iter1和iter2打包成元组并且返回一个可迭代的zip对象
enumeraate(iter)根据iter对象创建一个enumerate对象
all(iter)判断可迭代对象iter中所有元素的布尔值是否都为Ture
any(iter)判断可迭代对象iter中所有元素的布尔值是否都为Ture
next(iter)获取迭代器的下一个对象
filter(function,iter)通过指定条件过滤序列并且返回一个迭代器对象
map(function,iter)通过函数function对可迭代对象iter的操作返回一个迭代器对象
'''
lst = [1,2,3,4,5,6,7,8,9]
#排序
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(asc_lst)
print(desc_lst)
#反向
new_lst=reversed(lst)#<class 'list_reverseiterator'>
print(type(new_lst))
print(list(new_lst))


#zip
x=['a','b','c','day86']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))
# print(list(zipobj))


#enumerate
enum=enumerate(y,start=1)
print(type(enum))

print(tuple(enum))



#all
lst2=[10,20,30,'']
print(all(lst2))#空字符串为false
print(any(lst))


#any
print(any(lst2))

#next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))


def fun(num):
    return num%2==1
obj=filter(fun,range(10))#将range（0-9）整数，都执行一次fun操作
print(list(obj))


def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))