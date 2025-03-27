class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好我是:{self.name}今年:{self.age}岁')