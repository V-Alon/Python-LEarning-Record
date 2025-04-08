import os.path
print('获取目录或者文件的绝对路径',os.path.abspath('./'))
print('判断目录或者文件在磁盘上是否存在',os.path.exists('./'))
# print(os.path.join(os.path.abspath('./'),'/'))
print(os.path.split('a.txt'))
print(os.path.basename('a.txt'))
print(os.path.dirname('a.txt'))