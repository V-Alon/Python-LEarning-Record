import admin.my_admin as a
a.info()
print('-'*50)
from admin import my_admin as b#form 包名 import模块 as 别名
b.info()
print('-'*50)
from admin.my_admin import info#from 包名.模块名 import 函数/变量
info()
print('-'*50)
from admin.my_admin import *
print(name)