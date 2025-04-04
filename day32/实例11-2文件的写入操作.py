#文件的基本操作
#文件的打开模式
'''
r 只读模式
rb 只读模式二进制文件
w 覆盖写模式，不存在创建，存在覆盖
wb 覆盖写模式二进制文件，不存在创建，存在覆盖
a 追加写模式，不存在创建，存在，则在文件最后追加内容
+ 和w,r,a，一起使用，在原有功能上增加同时读写功能
'''
#读写方式
'''
file
read(size)
readline(size)
readlines()
write(s)
wirtelines(lst)
seek(offset)
'''
def my_write(s):
    file=open('b.txt','a',encoding='utf-8')
    file.write(s)
    file.write('\n')
    file.close()
def my_write_list(file,lst):
    f=open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()

if __name__ == '__main__':
    # my_write('hello')
    # my_write('world')
    lst=['姓名\t','年龄\t','成绩\n','张三\t','30\t','99']
    my_write_list(file='c.txt',lst=lst)