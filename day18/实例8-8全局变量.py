a=100#全局变量
def calc(x,y):
    return a+x+y
print(a)
print(calc(10,20))


print('-'*50)

def calc2(x,y):
    a=200
    return a+x+y
print(calc2(10,20))#局部变量在局部内大于全局变量的定义
print(a)

print('-'*50)

def calc3(x,y):
    global s# s是在函数中定义的变量，但是加上了global关键字声明，就变成了全局变量
    s=300#声明和赋值分开进行
    return s+x+y
print(calc3(10,20))
print(s)

