from sys import flags

number=eval(input('请输入你的中奖号码'))
if number==3579:  #或者使用!=也可以
    print('你中奖了')
if number!=3579:
    print('你没有中奖')
print('-------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔类型---------------')
number1=98#赋值操作
if number1%2: #余数是0.0就是false
    print('是奇数')
if not number1%2:   #not 0，就是True
    print('是偶数')
print('-'*20)
x=input('请输入一个字符串')
if x:           #字符串布尔值为1，非空字符串布尔值为True，空字符串为False
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')
print('表达式也可以是一个单纯的布尔类变量')
flag=eval(input('请输入一个布尔类型的值'))
if flag:                                      
    print('flag的值为True')
if not flag:
    print('flag的值为False')