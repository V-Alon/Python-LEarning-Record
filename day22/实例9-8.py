'''
#面向对象的三大特征
# 封装
# 继承
# 多态
#权限控制，通过对属性或者方法添加单下划线，双下划线，以及首尾双下划线来实现
'''


class Student():
    def __init__(self, name, age,gender):
        self._name = name#self._name受保护的，只能类本身和子类访问
        self.__age = age#self.__age表示私有的，只能类本身去访问
        self.gender = gender#普通实例属性，类，外部，内部，子类都可以访问


    def _fun1(self):
        print('子类及本身可以访问')
    def __fun2(self):
        print('只有类本身可以访问')

    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

#创建学生类
stu=Student('mkk',18,'male')
#类的外部
print(stu._name)
# print(stu.__age)
stu._fun1()
# stu.__fun2()

#私有的实例属性和方法真的不能访问吗，
print(stu._Student__age)


stu._Student__fun2()


print(dir(stu))