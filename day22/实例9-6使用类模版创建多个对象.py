class Student:
    # 类属性定义在类中，方法外的变量
    school = 'xa.....school'

    # 初始化方法
    def __init__(self, xm, age):  # name,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name = xm  # 左侧是实例属性，name是局部变量将局部变量的值赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，成为方法，自带一个参数self
    def show(self):
        print(f'我叫: {self.name},今年: {self.age}岁了')
#根据图纸创建n个对象
stu1=Student('mkk',22)
stu2=Student('pzh',22)
stu3=Student('kobe',8)
stu4=Student('laoda',24)