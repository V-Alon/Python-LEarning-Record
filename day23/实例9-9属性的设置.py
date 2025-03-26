class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    #将方法转成属性使用
    @property
    def gender(self):
        return self.__gender
    #将gender设置为可写属性
    @gender.setter
    def gender(self, value):
        if value!='male' and value!='female':
            print('sex error')
            self.__gender ='error'
        else:
            self.__gender = value

stu=Student('laoda','male')
print(stu.name,'sex is',stu.gender)#stu,gender就会去调用stu.gendr
#尝试去修改gender
# stu.gender = 'female'#property 'gender' of 'Student' object has no setter
stu.gender='0'
print(stu.name,stu.gender)


