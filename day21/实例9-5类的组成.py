class Student:
    # 类属性定义在类中，方法外的变量
    school = 'xa.....school'

    # 初始方法
    def __init__(self, name, age):  # name,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name = name  # 左侧是实例属性，name是局部变量将局部变量的值赋值给实例属性self.name
        self.age = age  # 实例的名称和局部变量的名称可以相同

    # 定义在类中的函数，成为方法，自带一个参数self
    def show(self):
        print(f'我叫: {self.name},今年: {self.age}岁了')

    @staticmethod
    def sm():
        # print(self.age)
        # self.name()
        print('这是一个静态方法,不能调用实例属性，也不能调用实例方法')

    @classmethod
    def cm(cls):  # cls是class的简写
        # print(self.name)
        # self.age()
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

# 创建类的对象
stu = Student('mkk', 18)  # 在__init__中，右两个形参，self是自带的参数，无需手动传入
# 实例属性，使用对象名进行打点调用
print(stu.name, stu.age)
# 类属性，直接使用类名，打点调用
print(Student.school) \
    # 实例方法，直接使用对象名进行打点调用
stu.show()
# 类的方法@classmethod
Student.cm()
# 静态方法，@staticmethod进行修饰的方法，直接进行类名打点调用
