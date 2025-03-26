'''
子类继承了父类就拥有了父类中公共成员和受保护的成员

父类的方法并不能完全适合子类的需要这个时候子类可以从写父类方法

子类在重写父类的方法时候，要求方法的名称必须和父类的方法名相同，在子类重写的方法中可以通过super().xxx调用父类中的方法
'''
#继承的语法结构：class 类名（父类1，父类2，。。。）:
#                       pass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我的名字是{self.name}我的年龄是{self.age}')

#student继承person类
class Student(Person):
    #初始化的方法
    def __init__(self, name, age, stunum):
        super().__init__(name,age)#调用父类的初始化方法
        self.stunum = stunum
    def show(self):
        print(f'我的名字是{self.name}我的年龄是{self.age}我的学号是{self.stunum}')

#Doctor类继承Person类
class Doctor(Person):
    # 初始化的方法
    def __init__(self, name, age,department):
        super().__init__(name,age)#调用父类的初始化方法
        self.department = department
    def show(self):
        print(f'我的名字是{self.name}我的年龄是{self.age}我的工作的科室是{self.department}')

#创建第一个子类
stu=Student('John',23,'001')
stu.show()

doctor=Doctor('Marry',29,'——心外科')
doctor.show()