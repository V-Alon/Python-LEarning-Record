try:
    num1 = int(input('请输入一个整数：'))
    num2 = int(input('请输入另一个整数：'))
    result = num1 / num2

except ZeroDivisionError:
    print('除数为零')
except ValueError:
    print('请输入整数')
except BaseException:
    print('未知异常')
else:
    print('结果是：',result)