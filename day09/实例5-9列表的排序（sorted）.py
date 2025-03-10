lst=[4,56,3,78,40,56,89]
print('原列表',lst)
asc_lst=sorted(lst)
print(asc_lst)
desc_lst=sorted(lst,reverse=True)
print(desc_lst)


lst2=['banana','apple','Cat','Orange']
print(lst2)
#忽略大小写
new_lst=sorted(lst2,key=str.lower)
print(new_lst)