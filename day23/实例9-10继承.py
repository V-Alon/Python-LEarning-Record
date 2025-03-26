#继承的语法结构：class 类名（父类1，父类2，。。。）:
#                       pass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'my name is {self.name} and my age is {self.age}')

#student继承person类
class Student(Person):
    #初始化的方法
    def __init__(self, name, age, stunum):
        super().__init__(name,age)#调用父类的初始化方法
        self.stunum = stunum

#Doctor类继承Person类
class Doctor(Person):
    # 初始化的方法
    def __init__(self, name, age,department):
        super().__init__(name,age)#调用父类的初始化方法
        self.department = department

#创建第一个子类
stu=Student('John',23,'001')
stu.show()

doctor=Doctor('Marry',29,'heart and brain')
doctor.show()