lst=['hello','world','python']
print('原列表',lst,id(lst))
#增加元素的操作
lst.append('sql')
print('增加元素后',lst,id(lst))
#使用insert（index，x）在特定位置插入元素
lst.insert(1,100)
print(lst)
#列表元素删除
lst.remove('world')
print('删除元素后的列表',lst,id(lst))
#使用pop（index）
print(lst.pop(1))
print(lst)
#清除所有元素
# lst.clear()
# print(lst,id(lst))
#反向输出
lst.reverse()
print(lst)
#列表的copy
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素修改
lst[1]='mysql'
print(lst)