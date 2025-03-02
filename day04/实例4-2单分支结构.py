number=eval(input('请输入你的中奖号码'))
if number==3579:  #或者使用!=也可以
    print('你中奖了')
else:
    print('你没有中奖')
print('-------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔类型---------------')
number1=98#赋值操作
if number1%2: #余数是0.0就是false
    print('是奇数')
if not number1%2:   #not 0，就是True
    print('是偶数')
    