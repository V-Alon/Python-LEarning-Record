a=10
b=20
print(dir(a))#一切皆对象
print(dir(b))
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(f'{a}小于{b}吗',a.__lt__(b))
print(f'{a}小于等于{b}吗',a.__le__(b))
print(f'{a}等于{b}吗',a.__eq__(b))
print('_'*50)
print(f'{a}大于{b}吗',a.__gt__(b))
print(f'{a}大于等于{b}吗',a.__ge__(b))
print(f'{a}不等于{b}吗',a.__ne__(b))


print('_'*50)
print(a.__mul__(b))#乘法
print(a.__truediv__(b))#除法
print(a.__mod__(b))


