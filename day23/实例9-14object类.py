#object()类，所有类都间接或者直接是他的子类
#所有类都拥有object()类的属性和方法
#object()中的特殊方法
'''
_new_()  由系统调动，用于创建对象
_init_()   创建对象时手动使用，用于初始化对象属性值
_str_()   对象的描述，返回值是str类型，默认输出对象的内存地址
'''

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好我是:{self.name}今年:{self.age}岁')

#对象
per=Person('laoda',20)#创建对象的时候就自动调用__init__方法
per.show()
print(dir(per))


print(per)#自动调用__str__方法