'''
abs(x)获取x的绝对值
divmod(x, y)获取x和y的商和余数
max(sequence)获取sequence的最大值
min(sequence)获取sequence的最小值
sum(iter)对可迭代对象进行求和
pow(x, y)获取x的y次幂
round(x,day86)对x进行保留d位小数，结果四舍五入
'''
print(abs(-2))
print(abs(2))
print(divmod(2, 3))
print(max('hello'))
print(min('hello'))
print(max([1,2,3,4]))
print(sum([1,2,3,4]))
print(pow(2, 3))
print(round(3.14))#round函数只有一个参数与，保留整数
print(round(3.1415926,3))
print(round(314.15926,-1))#负数对个位进行舍去
print(round(314.15926,-2))#负数对十位个位进行舍去