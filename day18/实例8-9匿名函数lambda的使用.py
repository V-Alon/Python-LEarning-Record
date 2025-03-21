#语法结构 result=lambda 参数列表：表达式
def calc(a,b):
    return a+b
print(calc(10,20))

#匿名函数
s=lambda a,b:a+b
print(type(s))#<class 'function'>方法就是函数
#调用匿名函数
print(s(10,20))
print('-'*50)
#
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

print('-'*50)
for i in range(len(lst)):
    result=lambda x:x[i]#根据索引取值，result类型是function
    print(result(lst))#lst是实际函数

student_scores=[
    {'name':'韩梅梅','score':95},
    {'name': '王二' , 'score' :94},
    {'name': '张三' , 'score' :93},
    {'name': '李四' , 'score' :92}
]
#对列表进行排序
student_scores.sort(key=lambda x:x.get('score'),reverse=True)#降序
print(student_scores)