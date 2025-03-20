def happybirthday(name='KoBe',age=18):
    print("Happy Birthday"+'   '+name)
    print(str(age)+" years old happy birthday")

happybirthday()
happybirthday('laoda',20)
happybirthday(age=19)

def fun(a,b):  #a作为位置参数，b作为默认值参数
    pass

#当位置参数和关键字（默认值）参数同时存在的时候，位置参数在后会报错

##当位置参数和关键字参数同时存在的时候，，应当遵循位置参数在前，默认值（关键字）参数在后