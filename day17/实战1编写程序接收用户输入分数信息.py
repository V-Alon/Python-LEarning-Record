try:
    score=eval(input('请输入你的成绩'))
    if 100>=score>0:
        print('分数为',score)
    else:
        raise Exception('分数不合法')

except Exception as e:
    print(e)
