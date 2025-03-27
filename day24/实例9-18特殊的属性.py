class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

a=A ()
b=B ()
c=C ('lalda',20)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
#查看字典内容
print(a.__class__)
print(b.__class__)
print(c.__class__)
#查看父类
print(A .__bases__)
print(B .__bases__)
print(C .__bases__)
#查看父类
print(A .__base__)
print(B .__base__)
print(C .__base__)
#层次结构
print(A .__mro__)
print(B .__mro__)
print(C .__mro__)#c类继承了a，b类，间接继承了object()类

#子类列表
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())