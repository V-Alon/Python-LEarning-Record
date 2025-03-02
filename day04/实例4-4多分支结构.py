score=eval(input('请输入成绩'))
if score<0 or score>100:
    print('请重新输入成绩')
elif 90<score<=100:
    print('优秀')
elif 80<score<=89:
    print('良好')
elif 70<score<=79:
    print('一般')
elif 60<score<=69:
    print('合格')
else:
    print('不合格')