class Student:
    #类属性定义在类中，方法外的变量
    school='xa.....school'
    #初始方法
    def __init__(self,name,age):#name,age是方法的参数，是局部变量，作用域是整个__init__方法
        self.name=name#左侧是实例属性，name是局部变量将局部变量的值赋值给实例属性self.name
        self.age=age#实例的名称和局部变量的名称可以相同

