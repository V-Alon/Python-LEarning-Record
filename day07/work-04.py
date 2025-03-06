#猜数游戏
"""
随机生成一个1-100的随机数，
然后循环猜这个数字，直到猜到为止，
猜的时候只提示猜大了猜小了，
输出用户猜的次数
"""
import random
rand=random.randint(1,100)
count=1
while count <= 10:
    guess_num=eval(input('请猜这个数字，我会告诉你大了还是小了'))
    if guess_num==rand:
        print('恭喜你猜对了')
        break
    elif guess_num<rand:
        print('猜小了')
        count=count+1
    else:
        print('猜大了')
        count=count+1
#判断次数
if count<=3:
    print('厉害,猜了',count,'次数')
elif count<7:
    print('还不错猜了',count,'次数')
elif count<10:
    print('菜就多练，猜了',count,'次数')
elif count<100:
    print('建议重开吧，孩子，猜了',count,'次数')
else:
    print('孩子你无敌了，猜了',count,'次数')