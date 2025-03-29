#(1)import......
import my_info
print(my_info.name)
my_info.info()



import my_info as a
print(a.name)
a.info()

#(2)from...import...
from my_info import name#导入的是具体的变量而不是函数
print(name)
my_info.info()

from my_info import info
print(a.name)
info()

#通配符
from my_info import *
print(name)
info()

#同时导入多个模块
import math,time,random


