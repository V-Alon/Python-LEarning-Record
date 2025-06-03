from datetime import datetime
dt = datetime.now()
print(dt)

#datetime是一个类，手动创建类
dt2=datetime(2020,2,3,13,2)
print(type(dt2),dt2)


#
labor_day=datetime(2020,2,3,13,2,21)
national_day=datetime(2040,2,3,5,6,3)
print(labor_day<national_day)

#datetime--->str
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%day86 %H:%M:%S')
print(type(nowdt_str),nowdt_str)
print(type(nowdt),nowdt)

str_datetime='2025年8月8日 20点4分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print(str_datetime,type(str_datetime))
print(type(dt3),dt3)
print('-'*50)

