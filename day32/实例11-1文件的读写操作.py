#文件
'''
打开文件
变量名=open(filename,mode,encoding)

操作文件
变量名.read()
变量名.write()

关闭文件
关闭文件.close()
'''
def my_write():
    file=open('a.txt','w',encoding='utf-8')
    file.write('伟大的中国梦')
    file.close()

def my_read():
    file=open('a.txt','r',encoding='utf-8')
    s=file.read()
    print(s)
    print(type(s))
    file.close()
# if __name__ == '__main__':
#     my_write()

if __name__ == '__main__':
    my_read()