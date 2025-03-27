class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'#返回值是一个字符串
#创建Person对象
per=Person('laoda',20)
print(per)#输出不再是内存地址，而是重写后的__str__方法的返回值
print(per.__str__())#手动调用
