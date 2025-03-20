def happybirthday(name,age):
    print("Happy Birthday"+'   '+name)
    print(str(age)+" years old happy birthday")

#关键字传参
happybirthday(age=20,name='KoBe')
happybirthday('KoBe',age=20)
# happybirthday(name='KoBe',20)SyntaxError: positional argument follows keyword argument