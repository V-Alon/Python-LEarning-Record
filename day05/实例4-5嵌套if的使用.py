answer=input('请问你喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾')
    elif proof<80:
        print('酒驾')
    else:
        print('醉驾')
else:
    print('你走吧，没事了')