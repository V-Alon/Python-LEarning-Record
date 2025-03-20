# #个数可变的位置参数
# def fun(*para):
#     print(type(para))
#     for item in para:
#         print(item)
#
#
# fun(1,2,3)
# fun(1,2,3,4,5)
# fun([1,2,3,4])           #列表相当于一个元素
# fun(*[1,2,3,4])         #加上*号，把列表每一个元素当成独立元素对待
#

#个数可变的关键字参数
def fun1(**para):
    print(type(para))
    for key, value in para.items():
        print(key, '---',value)


#调用
fun1(name='kk',age=18,height=170)





d={'name':'kk','age':18,'height':170}
fun1(**d)#TypeError: fun1() takes 0 positional arguments but 1 was given
