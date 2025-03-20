#函数的返回值的使用
def calc(a,b):
    print(a+b)


calc(10,20)
print(calc(10,20))#none


def calc2(a,b):
    s=a+b
    return s
print('-'*50)
gets=calc2(1,2)#存储在变量中
print(gets)



get_s2=calc2(calc2(1,2),calc2(2,1))
print(get_s2)



#返回值可以是多个
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s#三个值
#解包赋值
print('-'*50)
a,b,c=get_sum(10)#返回三个值
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(a)
print(b)
print(c)
