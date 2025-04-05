def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('你好啊')
    file.seek(0)

    #读取
    # s=file.read()
    # s=file.read(2)#2个字符
    # s=file.readline()
    # s=file.readline(2)
    # s=file.readlines()
    s=file.seek(3)
    print(type(s),s)
    file.close()

if __name__ == '__main__':
    my_read('d.txt')