import jieba
#读取文件
with open('华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()
# print(s)

lst=jieba.lcut(s)
# print(lst)

set1=set(lst)#使用集合去重
#统计频率
d={}
for item in set1:
    if len(item)>=2:
        d[item]=0
# print(d)
for item in lst:
    if item in d:
        d[item]=d.get(item)+1
# print(d)
new_lst=[]
for item in d:
    new_lst.append([[item],d[item]])
# print(new_lst)

#列表排序
new_lst.sort(key=lambda x:x[1],reverse=True)
print(new_lst[0:11])

input()