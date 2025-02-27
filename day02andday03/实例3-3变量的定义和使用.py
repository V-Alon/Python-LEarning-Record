luck_number=8 #创建一个整型变量，赋值为8
print(luck_number)
my_name='穆康康'
print('luck—number的数据类型是：',type(luck_number))
print(my_name,'的幸运数字是',luck_number)
#Python动态修改变量的数据类型，通过赋值不同的类型的值
luck_number='mkk'
print('luck_number的数据类型是：',type(luck_number))
#Python允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no),id(number))