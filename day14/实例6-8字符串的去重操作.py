s1='helloworldhelloworldhelloworldhelloworldhelloworldhelloworlddasdwdsazxcvb'
#字符串的拼接和not in
new_s=''
for item in s1:
    if item not in new_s:
        new_s+=item#拼接操作
print(new_s)


#使用索引
new_s2=''
for i in range(len(s1)):
    if s1[i] not in new_s2:
        new_s2+=s1[i]
print(new_s2,'              ',len(new_s2))



#通过集合去重+列表的排序
new_s3=set(s1)
lst=list(new_s3)
print(lst,len(lst))
lst.sort(key=s1.index)
print(lst,len(lst))