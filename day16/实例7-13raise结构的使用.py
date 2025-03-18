#raise的关键字语法的结构为
#    raise [Exception类型(异常描述信息)]
try:
    gender=input('请输入你的性别')
    if gender !='man' and gender !='woman':
        raise Exception('性别只能是男或者女')
except Exception as e:
    print(e)
else:
    pass
