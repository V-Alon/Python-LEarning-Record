year=eval(input('请输入一个任4位年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('这个年份是闰年',year)
else:
    print('这个年份不是闰年',year)