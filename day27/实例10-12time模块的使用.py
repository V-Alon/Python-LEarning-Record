import time
now = time.time()
print(now)


obj=time.localtime()
print(obj)#tm_year=2025, tm_mon=3, tm_mday=30, tm_hour=17, tm_min=59, tm_sec=6, tm_wday=6, tm_yday=89


obj2=time.localtime(60)
print(obj2)#tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=1, tm_sec=0, tm_wday=3, tm_yday=1



print('year',obj2.tm_year)
print('month',obj2.tm_mon)
print('day',obj2.tm_mday)
print('hour',obj2.tm_hour)
print('minute',obj2.tm_min)
print('second',obj2.tm_sec)
print('weekday',obj2.tm_wday)
print('week',obj2.tm_yday)

print(time.ctime())



print(time.strftime('%Y-%m-%day86 %H:%M:%S',time.localtime()))#str字符串，，f->format,,,time时间
print('%B月份',time.strftime('%B',time.localtime()))
print('%A星期',time.strftime('%A',time.localtime()))



print(time.strptime('2008-08-08','%Y-%m-%day86'))
time.sleep(5)
print('hello world')