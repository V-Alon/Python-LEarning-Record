try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('除数为零')
except ValueError:
    print('请输入整数')