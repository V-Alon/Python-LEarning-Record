import os
print(os.getcwd())
lst=os.listdir()
print('当前路径下所有文件目录',lst)
print('当前路径下所有文件目录',os.listdir('D:\GitHub-works\Python-LEarning-Record'))
#创建目录
# os.mkdir('hello')#已经存在会报错[WinError 183] 当文件已存在时，无法创建该文件。: 'hello'
# os.makedirs('./aa/bb/cc')
#删除（空）目录
# os.rmdir('hello')#要删除的目录不存在也报错
# os.removedirs('./aa/bb/cc')
#修改
# os.chdir('')
#遍历目录树
for dirs,dirlst,filelst in os.walk('D:\GitHub-works\Python-LEarning-Record'):
     print(dirs)
    # print(dirlst)
    # print(filelst)