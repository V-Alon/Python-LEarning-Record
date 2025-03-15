#使用占位符
name='马冬梅'
age=18
score=90.5
print('姓名:%s,年龄:%d,成绩:%f' % (name,age,score))
print('姓名:%s,年龄:%d,成绩:%1f' % (name,age,score))


#使用f-string    f+'字符串'
print(f'姓名:{name},年龄:{age},成绩:{score}')


#使用str.format()
print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))#0 1 2分别对应format中的序号
print('姓名:{2},年龄:{0},成绩:{1}'.format(age,score,name))