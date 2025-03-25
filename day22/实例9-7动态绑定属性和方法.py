class Student:
    # 类属性定义在类中，方法外的变量
    school = 'xa.....school'

    # 初始化方法
    def __init__(self, xm, age):  # name,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name = xm  # 左侧是实例属性，name是局部变量将局部变量的值赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，成为方法，自带一个参数self
    def show(self):
        print(f'我叫: {self.name},今年刚满: {self.age}岁了')
#创建两个对象
stu=Student('mkk',18)
stu1=Student('laoda',22)
print(stu.name,stu.age)
print(stu1.name,stu1.age)

#为stu2绑定一个动态属性
stu1.gender='male'
print(stu1.name,stu1.gender,stu1.age)
# print(stu.gender)# 'Student' object has no attribute 'gender'

#   D动态绑定方法
def introduce():
    print('我是一个函数，我被动态绑定了stu1对象的方法')
stu1.fun=introduce#函数的一个赋值


stu1.fun()
