x=True
print(x)
print(type(x))
print(x+10)#10+1=11
print(False+10)#false=0
print('------------------------------------')
print(bool(18))
print(bool(0),bool(0.0))
#非零的整数布尔值都是True
print(bool('西安'))
print(bool(''))
print(bool(False))
print(bool(True))
#布尔值为零的情况：False，None，数值的0,0.0，虚数0，空序列，空元组，空字典，空集合。
#自定义对象的实例该对象的bool（）返回False或者len（）返回0