lst=[4,56,3,78,40,56,89]
print('原列表',lst)
#排序
lst.sort()
print('升序排列',lst)
lst.sort(reverse=True)
print(lst)


print('-'*50)
lst2=['banana','apple','Cat','Orange']
print(lst2)
lst2.sort()
print(lst2)
lst2.sort(reverse=True)
print(lst2)
#忽略大小写排序
lst2.sort(key=str.lower)
print(lst2)