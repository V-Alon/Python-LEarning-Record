'''
enumearte函数，，枚举
'''
lst=['hello','world','python','php']
for item in lst:#使用遍历for循环列表元素
    print(item)

#使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])

#使用enumearte函数
for index,item in enumerate(lst):
    print(index,'-->',item)

for index,item in enumerate(lst,start=1):#手动设置从1开始
    print(index,'-->',item)