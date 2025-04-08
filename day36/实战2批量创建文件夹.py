import os
import os.path
def mkdirs(path,num):
    for item in range(1,num+1):
        os.mkdir(path+'/'+str(item))

if __name__ == '__main__':
    path = './newdir'
    if not os.path.exists(path):
        os.mkdir(path)

    num=eval(input('请输入要创建的目录的个数:'))
    mkdirs(path,num)