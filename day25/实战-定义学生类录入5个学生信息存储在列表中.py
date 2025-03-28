class Student(object):
    def __init__(self, name, age,gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def info(self):
        print(self.name,self.age,self.gender,self.score)
print("请输入五位学生的信息:(姓名#年龄#性别#成绩)")
lst=[]
for i in range(5):
    s=input(f'请输入第{i}位学生信息及成绩:')
    s_lst=s.split('#')#索引为0的是姓名，为1是年龄，为2是性别，为3是成绩
    #创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
    #将学生对象添加到列表中
    lst.append(stu)
#遍历列表，调用info方法
for item in lst:
    item.info()
'''
lhb#24#女#99
pzh#23#男#90
mkk#23#男#88
劳大#24#女#24
牢底#28#男#69

'''