def copy(src,new_path):
    #打开源文件
    file1=open(src,'rb')
    #打开目标文件
    file2=open(new_path,'wb')
    #复制
    s=file1.read()
    file2.write(s)
    #关闭,先打开的先关闭，后打开的后关闭
    file2.close()
    file1.close()

if __name__ == '__main__':
    src='./google.jpg'#.代表当前解压目录
    new_path='../day32/copy_google.jpg'
